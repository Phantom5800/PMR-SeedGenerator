import re
import os
import sys
import json
import time
import copy
import shutil
import random
import sqlite3 as sql
import threading
import configparser

from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic

from enums import Enums, create_enums
from table import Table
from utility import resource_path, sr_dump, sr_copy, sr_compile
from logic import place_items
from parse import get_default_table, get_table_info, create_table, gather_keys, gather_values

from db.map_area import MapArea
from db.item import Item, create_items
from db.itemlocation import ItemLocation, create_item_locations
from db.quiz import Quiz, create_quizzes
from db.option import Option, create_options
from db.item_price import ItemPrice, create_item_prices
from db.entrance import Entrance, create_entrances
from db.actor_attribute import ActorAttribute, create_actor_attributes

# Create enums from ./globals/enum/
create_enums()

# Uncomment to build database from scratch
"""
gather_keys()
gather_values()
create_options()
create_items()
create_item_locations()
create_item_prices()
create_actor_attributes()
create_quizzes()
create_entrances()
shutil.copy("db.sqlite", "default_db.sqlite")
quit()
# END
"""


class Stream(QtCore.QObject):
	newText = QtCore.pyqtSignal(str)

	def write(self, text):
		self.newText.emit(str(text))


class Window(QMainWindow):

	def __init__(self, app):
		super(Window, self).__init__()
		uic.loadUi(resource_path("gui/main.ui"), self)

		# Icons
		self.setWindowIcon(QtGui.QIcon(resource_path("gui/icons/random_bag.ico")))
		self.tabwidget.setTabIcon(0, QtGui.QIcon(resource_path("gui/icons/starrod.ico")))
		self.tabwidget.setTabIcon(1, QtGui.QIcon(resource_path("gui/icons/fireflower.ico")))
		self.tabwidget.setTabIcon(2, QtGui.QIcon(resource_path("gui/icons/pupddown.ico")))

		# Setup
		self.setWindowTitle("Paper Mario Open World Randomizer")
		self.app = app
		self.app.setStyle("Fusion")
		self.progress_bar.setVisible(False)
		
		# Buttons
		self.button_compile.clicked.connect(self.compile_mod)
		self.button_load_settings.clicked.connect(self.load_settings)
		self.button_save_settings.clicked.connect(self.save_settings)
		self.button_randomize.clicked.connect(self.randomize)
		self.button_about.clicked.connect(self.about)

		# Move to center of window
		rectangle = self.frameGeometry()
		center_point = QDesktopWidget().availableGeometry().center()
		rectangle.moveCenter(center_point)
		self.move(rectangle.topLeft())

		self.show()
		self.configure()

		# Log
		self.log.moveCursor(QtGui.QTextCursor.Start)
		self.log.ensureCursorVisible()
		self.stream = Stream(newText=self.on_update_text)
		sys.stdout = self.stream

		# Check if the ROM already exists in the correct location
		rom_exists = False
		for filename in os.listdir("../ROM"):
			if filename == "PM64.z64":
				rom_exists = True
				break
		if not rom_exists:
			self.select_rom()
			if self.rom_path:
				shutil.copyfile(self.rom_path, "../ROM/PM64.z64")
		else:
			self.display(f"Successfully found ROM")

	def on_update_text(self, text):
		cursor = self.log.textCursor()
		cursor.movePosition(QtGui.QTextCursor.End)
		cursor.insertText(text)
		self.log.setTextCursor(cursor)
		self.log.ensureCursorVisible()

	def about(self):
		msg = QMessageBox()
		msg.setWindowIcon(QtGui.QIcon(resource_path("gui/icons/book.ico")))
		msg.setWindowTitle("About")
		msg.setText(
			"This is an open world randomizer for Paper Mario 64.\n" \
			"It's pretty neat."
		)
		msg.exec_()

	def load_settings(self):
		# Prompt user for a database to use for populating GUI widgets
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename, ok = QFileDialog.getOpenFileName(self, "Select Settings File", "", "Sqlite Files (*.sqlite)", options=options)

		if not ok:
			# Poor lil' GUI :(
			return

		# Update the temporary DB with data from this file
		options = {
			"InitialCoins": Option.get(Option.name == "InitialCoins"),
			"ReplaceDuplicateKeys": Option.get(Option.name == "ReplaceDuplicateKeys"),
			"DuplicateKeyReplacement": Option.get(Option.name == "DuplicateKeyReplacement"),
			"FlowerGateOpen": Option.get(Option.name == "FlowerGateOpen"),
			"BlueHouseOpen": Option.get(Option.name == "BlueHouseOpen"),
			"BlocksMatchContent": Option.get(Option.name == "BlocksMatchContent"),
			"SkipQuiz": Option.get(Option.name == "SkipQuiz"),
			"CapEnemyXP": Option.get(Option.name == "CapEnemyXP"),
			"2xDamage": Option.get(Option.name == "2xDamage"),
			"4xDamage": Option.get(Option.name == "4xDamage"),
			"OHKO": Option.get(Option.name == "OHKO"),
			"ShuffleItems": Option.get(Option.name == "ShuffleItems"),
			"IncludeCoins": Option.get(Option.name == "IncludeCoins"),
			"IncludeShops": Option.get(Option.name == "IncludeShops"),
		}

		connection = sql.connect(filename)
		cursor = connection.cursor()
		for name,option in options.items():
			cursor.execute(f"SELECT * FROM option WHERE name = '{name}' LIMIT 1")
			result = cursor.fetchone()
			options[name].value = result[-1] # Set to value in settings database provided
			options[name].save()

		self.configure()
		self.display(f"Loaded: {filename}")

	def save_settings(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		filename, ok = QFileDialog.getSaveFileName(self ,"Save Settings", "", "Sqlite Files (*.sqlite)", options=options)
		if ok:
			if not filename.endswith(".sqlite"):
				filename += ".sqlite"

			self.update_db()
			shutil.copy("db.sqlite", filename)
			self.display(f"Saved: {filename}")

	def configure(self):
		# Read configuration data
		self.config = configparser.ConfigParser()
		self.config.read("./config.ini")
		self.sr_path = self.config.get("starrod", "path")

		# Seed
		self.edit_seed.setText(self.config.get("options", "seed"))

		# Initial Coin Amount
		self.edit_coins.setText(str(Option.get(Option.name == "InitialCoins").value))
		self.edit_coins.setValidator(QtGui.QIntValidator())

		# Duplicate Key Replacement
		self.chk_replace_keys.setChecked(Option.get(Option.name == "ReplaceDuplicateKeys").value)
		self.chk_replace_keys.clicked.connect(lambda checked: self.combo_replace.setEnabled(checked))
		self.combo_replace.setEnabled(self.chk_replace_keys.isChecked())

		# Get all regular item names
		self.item_choices = []
		"""
		for item_id in range(0x01, 0x16D):
			name = Enums.get("Item")[item_id]
			if Item.get_type(item_id) == "ITEM":
				self.item_choices.append((name, item_id))
		"""
		self.item_choices.append(("Mistake", 0xC2))
		self.item_choices.append(("Coin", 0x157))

		# Sort alphabetically and populate combobox
		self.item_choices.sort(key=lambda t: t[0])
		for choice in self.item_choices:
			self.combo_replace.addItem(choice[0])

		# Get the default item ID for replacement and select that index
		db_item_id = Option.get(Option.name == "DuplicateKeyReplacement").value
		for i,(name,item_id) in enumerate(self.item_choices):
			if item_id == db_item_id:
				self.combo_replace.setCurrentIndex(i)
				break

		# Checkboxes
		self.chk_flower_gate.setChecked(Option.get(Option.name == "FlowerGateOpen").value)
		self.chk_blue_house.setChecked(Option.get(Option.name == "BlueHouseOpen").value)
		self.chk_blocks_content.setChecked(Option.get(Option.name == "BlocksMatchContent").value)
		self.chk_skip_quiz.setChecked(Option.get(Option.name == "SkipQuiz").value)
		self.chk_cap_xp.setChecked(Option.get(Option.name == "CapEnemyXP").value)

		# Radioboxes
		self.radio_ohko.setChecked(Option.get(Option.name == "OHKO").value)
		self.radio_damage_4.setChecked(Option.get(Option.name == "4xDamage").value)
		self.radio_damage_2.setChecked(Option.get(Option.name == "2xDamage").value)
		self.radio_damage_1.setChecked(all([
			not self.radio_ohko.isChecked(),
			not self.radio_damage_4.isChecked(),
			not self.radio_damage_2.isChecked(),
		]))

		# Item Options
		self.chk_shuffle_items.setChecked(Option.get(Option.name == "ShuffleItems").value)
		self.chk_include_coins.setChecked(Option.get(Option.name == "IncludeCoins").value)
		self.chk_include_shops.setChecked(Option.get(Option.name == "IncludeShops").value)

		# Ensure ShuffleItems is checked if extra item options are selected
		def update(checked):
			if checked:
				self.chk_shuffle_items.setChecked(True)
		self.chk_include_coins.clicked.connect(lambda checked: update(checked))
		self.chk_include_shops.clicked.connect(lambda checked: update(checked))

		# Disable/Enable extra item options when ShuffleItems changes
		def reset(checked, chk_widget):
			if not checked:
				chk_widget.setChecked(False)
		self.chk_shuffle_items.clicked.connect(lambda checked: reset(checked, self.chk_include_coins))
		self.chk_shuffle_items.clicked.connect(lambda checked: reset(checked, self.chk_include_shops))

	def display(self, message):
		self.statusBar().showMessage(message)

	def select_rom(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.rom_path, _ = QFileDialog.getOpenFileName(self, "Select ROM", "./", "z64(*.z64)", options=options)

	def compile_mod(self):
		self.log.clear()
		self.progress_bar.setVisible(True)
		self.progress_bar.setValue(0)
		self.progress_bar.setFormat(f"Dumping ROM")
		thread = sr_dump(self.sr_path, console=True)
		while thread.is_alive():
			self.app.processEvents()

		self.progress_bar.setValue(33)
		self.progress_bar.setFormat(f"Copying ROM")
		thread = sr_copy(self.sr_path, console=True)
		while thread.is_alive():
			self.app.processEvents()

		self.progress_bar.setValue(66)
		self.progress_bar.setFormat(f"Compiling ROM")
		thread = sr_compile(self.sr_path, console=True)
		while thread.is_alive():
			self.app.processEvents()
		
		self.progress_bar.setVisible(False)
		self.display(f"Finished Compiling Mod")

	def update_db(self):
		options = {
			"InitialCoins": Option.get(Option.name == "InitialCoins"),
			"ReplaceDuplicateKeys": Option.get(Option.name == "ReplaceDuplicateKeys"),
			"DuplicateKeyReplacement": Option.get(Option.name == "DuplicateKeyReplacement"),
			"FlowerGateOpen": Option.get(Option.name == "FlowerGateOpen"),
			"BlueHouseOpen": Option.get(Option.name == "BlueHouseOpen"),
			"BlocksMatchContent": Option.get(Option.name == "BlocksMatchContent"),
			"SkipQuiz": Option.get(Option.name == "SkipQuiz"),
			"CapEnemyXP": Option.get(Option.name == "CapEnemyXP"),
			"2xDamage": Option.get(Option.name == "2xDamage"),
			"4xDamage": Option.get(Option.name == "4xDamage"),
			"OHKO": Option.get(Option.name == "OHKO"),
			"ShuffleItems": Option.get(Option.name == "ShuffleItems"),
			"IncludeCoins": Option.get(Option.name == "IncludeCoins"),
			"IncludeShops": Option.get(Option.name == "IncludeShops"),
		}

		options["InitialCoins"].value = int(self.edit_coins.text())
		options["ReplaceDuplicateKeys"].value = int(self.chk_replace_keys.isChecked())
		options["DuplicateKeyReplacement"].value = self.item_choices[self.combo_replace.currentIndex()][1]
		options["FlowerGateOpen"].value = int(self.chk_flower_gate.isChecked())
		options["BlueHouseOpen"].value = int(self.chk_blue_house.isChecked())
		options["BlocksMatchContent"].value = int(self.chk_blocks_content.isChecked())
		options["SkipQuiz"].value = int(self.chk_skip_quiz.isChecked())
		options["CapEnemyXP"].value = int(self.chk_cap_xp.isChecked())
		options["2xDamage"].value = int(self.radio_damage_2.isChecked())
		options["4xDamage"].value = int(self.radio_damage_4.isChecked())
		options["OHKO"].value = int(self.radio_ohko.isChecked())
		options["ShuffleItems"].value = int(self.chk_shuffle_items.isChecked())
		options["IncludeCoins"].value = int(self.chk_include_coins.isChecked())
		options["IncludeShops"].value = int(self.chk_include_shops.isChecked())

		for option in options.values():
			option.save()

	def randomize(self):
		self.log.clear()
		self.progress_bar.setVisible(True)
		# Initialize Random Seed
		self.seed = hash(self.edit_seed.text()) & 0xFFFFFFFF
		random.seed(self.seed)

		# Create the ROM table
		rom_table = Table()
		rom_table.create()

		# Update database values from widgets
		self.update_db()

		# Item Placement
		for text,percent_complete in place_items(self.app, isShuffle=True, algorithm="forward_fill"):
			self.progress_bar.setValue(percent_complete)
			self.progress_bar.setFormat(f"{text} ({percent_complete}%)")
			self.app.processEvents()

		# Make everything inexpensive
		item_prices = [item_price for item_price in ItemPrice.select()]
		for item_price in item_prices:
			item = item_price.itemlocation.get() # ?
			item_price.value = 1
			item_price.save()

		# Create a sorted list of key:value pairs to be written into the ROM
		table_data = rom_table.generate_pairs(entrances=False)

		# Update table info with variable data
		rom_table.info["num_entries"] = len(table_data)
		rom_table.info["seed"] = self.seed

		# Write data to log file
		with open("./debug/log.txt", "w") as log:
			log.write("OPTIONS:\n\n")
			log.write(f"Seed: 0x{self.seed:0X} \"{self.edit_seed.text()}\"\n")
			for name,data in rom_table["Options"].items():
				log.write(f"{name:20}: {data['value']}\n")
			log.write("\n")

		# Modify the table data in the ROM
		with open("../out/PM64.z64", "r+b") as file:
			# Write the header
			file.seek(rom_table.info["address"])
			file.write(rom_table.info["magic_value"].to_bytes(4, byteorder="big"))
			file.write(rom_table.info["header_size"].to_bytes(4, byteorder="big"))
			file.write(rom_table.info["num_entries"].to_bytes(4, byteorder="big"))
			file.write(rom_table.info["seed"].to_bytes(4, byteorder="big"))

			# Write table data and generate log file
			file.seek(rom_table.info["address"] + rom_table.info["header_size"])
			with open("./debug/log.txt", "a") as log:
				log.write("ITEM CHANGES:\n\n")

				num_pairs = len(table_data)
				for i,pair in enumerate(table_data):
					self.progress_bar.setValue(int(100 * i / num_pairs))
					self.progress_bar.setFormat(f"Writing ROM Data ({int(100 * i / num_pairs)}%)")
					self.app.processEvents()

					key_int = pair["key"].to_bytes(4, byteorder="big")
					value_int = pair["value"].to_bytes(4, byteorder="big")
					file.write(key_int)
					file.write(value_int)
					if enum_type := pair.get("enum_type"):
						if enum_type == "Item":
							if "ShopPrice" not in pair["attribute"]:
								column_left = f"[{pair['table']}][{pair['attribute']}]"
								original_item_id = rom_table.default_db[pair["table"]][pair['attribute']]["value"]
								original_item = Enums.get("Item")[original_item_id]
								column_right = f"{original_item} -> {Enums.get('Item')[pair['value']]}"
								log_statement = f"{column_left:25} : {column_right}"
								log.write(log_statement + "\n")
						if enum_type == "Entrance":
							pass #print(pair)

		self.progress_bar.setVisible(False)
		self.progress_bar.setValue(0)
		self.display("Finished Randomizing ROM")

		answer = QMessageBox.question(self, "Open ROM", "Open ROM with Default Application?", QMessageBox.Yes | QMessageBox.No)
		if answer == QMessageBox.Yes:
			path = str(Path(__file__).parent).replace("\\", "/")
			path = "".join(path.split("tools"))[0:-1]
			os.startfile(path + "/out/PM64.z64")


app = QApplication(sys.argv)
window = Window(app)
sys.exit(app.exec_())