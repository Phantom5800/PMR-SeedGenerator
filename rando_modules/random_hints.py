import json
import random

# always hints are always generated
always_hint_to_check_mapping = [
  {
    "name": "Blooper Chest",
    "check": "Blooper Boss 1 (B1) - Blooper Fight Reward"
  },
  {
    "name": "Dry Dry Ruins 4th Key Pedestal",
    "check": "Lunar Stone Room - On Pedestal"
  },
  {
    # this check is hinted when prologue is closed
    "name": "Goomba King's Tree",
    "check": "Goomba Kings Castle - In Tree Left Of Fortress",
    "req": "prologue_open",
    "req_val": False
  },
  {
    "name": "Lakilester",
    "check": "(NW) Lakilester - Lakilester Partner"
  },
  {
    "name": "Yoshi Chief",
    "check": "Village Cove - Village Leader Reward"
  }
]

# a subset of sometimes hints are generated at random each time
sometimes_hint_to_check_mapping = {
  "Anti Guy Chest": "BLU Anti-Guy Hall - In Chest",
  "Kolorado Camp Tree": "W3 Kolorados Camp - In Tree",
  "Kolorado Vase": "Village Buildings - Kolorado Volcano Vase Reward",
  "Lantern Ghost": "RED Lantern Ghost - Watt Partner",
  "Mayor Penguin": "Shiver City Mayor Area - Mayor Penguin Gift",
  "Merle": "Starborn Valley - Merle Gift",
  "Moles": "(East) Petunias Field - Petunia Gift",
  "Parakarry Letters": "Train Station - Parakarry Partner",
  "Shiver Mountain Sanctuary": "Merlars Sanctuary - On Pedestal",
  "Volcano Chest": "Sushi Tree - In Volcano Chest",
  "Yellow Yoshi": "Village Buildings - Yellow Yoshi Food Reward",
}
sometimes_hint_count = 4

# hint 1 barren category if possible, check all items in said group,
# if 0 key items are found, category can be hinted barren
barren_categories = [
  {
    "category": "Letters",
    "item_set": [
      "Plaza District - Merlon Letter Reward",
      "Southern District - Fice T. Letter Reward",
      "Basement - Igor Letter Reward",
      "Gate District - Russ T. Letter Reward",
      "E1 Nomadimouse - Nomadimouse Letter Reward",
      "Plaza District - Minh T. Letter Reward",
      "Koopa Village 2 - Kolorado Letter Reward",
      "Shiver City Mayor Area - Mayor Penguin Letter Reward",
      "Goomba Village - Goompa Letter Reward",
      "Goomba Village - Goompapa Letter Reward 1",
      "Merluvlees House - Merlow Letter Reward",
      "Ruined Castle Grounds - Muss T. Letter Reward"
      "Koopa Village 1 - Koover Letter Reward 1",
      "Port District - Fishmael Letter Reward",
      "Koopa Village 1 - Koover Letter Reward 2",
      "Outpost 2 - Mr. E. Letter Reward",
      "Gate District - Miss T. Letter Reward",
      "Outpost 1 - Little Mouser Letter Reward",
      "Foyer - Franky Letter Reward",
      "Station District - Dane T. Letter Reward 1",
      "Village Buildings - Red Yoshi Kid Letter Reward",
      "Station District - Dane T. Letter Reward 2",
      "Starborn Valley - Frost T. Letter Reward",
      "Goomba Village - Goompapa Letter Reward 2"
    ],
    "req": "include_letters_mode",
    "req_val": 3
  },
  {
    "category": "Rowf",
    "item_set": [
      "Plaza District - Rowfs Shop Set 1 - 1",
      "Plaza District - Rowfs Shop Set 1 - 2",
      "Plaza District - Rowfs Shop Set 1 - 3",
      "Plaza District - Rowfs Shop Set 1 - 4",
      "Plaza District - Rowfs Shop Set 2 - 1",
      "Plaza District - Rowfs Shop Set 2 - 2",
      "Plaza District - Rowfs Shop Set 2 - 3",
      "Plaza District - Rowfs Shop Set 3 - 1",
      "Plaza District - Rowfs Shop Set 3 - 2",
      "Plaza District - Rowfs Shop Set 3 - 3",
      "Plaza District - Rowfs Shop Set 4 - 1",
      "Plaza District - Rowfs Shop Set 4 - 2",
      "Plaza District - Rowfs Shop Set 4 - 3",
      "Plaza District - Rowfs Shop Set 5 - 1",
      "Plaza District - Rowfs Shop Set 5 - 2",
      "Plaza District - Rowfs Shop Set 5 - 3"
    ],
    "req": "progression_on_rowf",
    "req_val": True
  },
  {
    "category": "Tall Blocks",
    "item_set": [
      "Hall to Ultra Boots (B3) - Hidden Block",
      "Hall to Ultra Boots (B3) - Yellow Block Left",
      "Hall to Ultra Boots (B3) - Yellow Block Right",
      "Shiver Mountain Passage - Hidden Block",
      "Bridge to Shiver City (B2) - Yellow Block 1",
      "Bridge to Shiver City (B2) - Yellow Block 2",
      "Bridge to Shiver City (B2) - Yellow Block 3",
      "Bridge to Shiver City (B2) - Yellow Block 4",
      "Bridge to Shiver City (B2) - Yellow Block 5",
      "Room with Spikes (B2) - Yellow Block",
      "Huge Statue Room - Yellow Block",
      "Small Statue Room - Hidden Block"
    ]
  },
  {
    "category": "Ultra Hammer Blocks",
    "item_set": [
      "Dizzy Stomp Room - In Chest",
      "Ultra Boots Room (B3) - In Big Chest",
      "Boss Room - Yellow Block Left",
      "Boss Room - Yellow Block Right",
      "Sushi Tree - In Volcano Chest", # questionable though technically blocked by ultra hammer
      "Metal Block Room (B3) - In SuperBlock"
    ]
  },
  {
    "category": "Blue Berry",
    "item_set": [
      "(East) Old Well - Well BlueBerry Reward",
      "(West) Rosies Trellis - Rosie Gift",
      "(West) Path to Maze - Upper Hidden Block",
      "(West) Path to Maze - Lower Hidden Block"
    ]
  },
  {
    "category": "Red Berry",
    "item_set": [
      "(SW) Posie and Crystal Tree - Posie Gift 1",
      "(SW) Posie and Crystal Tree - Posie Gift 2",
      "(SW) Path to Crystal Tree - Hidden Panel",
      "(SW) Path to Crystal Tree - Central Vine",
      "(SW) Path to Crystal Tree - In Tree 1",
      "(SW) Path to Crystal Tree - In Tree 2"
    ]
  },
  {
    "category": "Yellow Berry",
    "item_set": [
      "(SE) Briar Platforming - In The Flowers",
      "(SE) Briar Platforming - In Tree 1",
      "(SE) Briar Platforming - In Tree 2",
      "(SE) Water Level Room - Hidden Panel",
      "(SE) Water Level Room - Hidden Block",
      "(SE) Water Level Room - Yellow Block",
      "(SE) Water Level Room - In Tree 1",
      "(SE) Water Level Room - In Tree 2",
      "(SE) Lilys Fountain - Lily Reward For WaterStone",
      "(SE) Lilys Fountain - In Tree"
    ]
  },
]

def search_for_location(item_spheres:dict, location:str) -> str:
  if isinstance(item_spheres, dict):
    if location in item_spheres:
      return item_spheres[location]
    for child in item_spheres:
      result = search_for_location(item_spheres[child], location)
      if result != "[Nothing Found]":
        return result
  return "[Nothing Found]"

def generate_hints(item_spheres:dict, logic_settings):
  always_hints = ""
  for hint in always_hint_to_check_mapping:
    if 'req' in hint:
      if getattr(logic_settings, hint['req']) != hint['req_val']:
        continue
    always_hints += f"  {hint['name']} is {search_for_location(item_spheres, hint['check'])}\n"

  sometimes_hints = ""
  sometimes_keys = list(sometimes_hint_to_check_mapping.keys())
  random.shuffle(sometimes_keys)
  for i,k in enumerate(sometimes_keys):
    if i >= sometimes_hint_count:
      break
    sometimes_hints += f"  {k} is {search_for_location(item_spheres, sometimes_hint_to_check_mapping[k])}\n"

  barren_category = "  Could not generate"
  valid_barren_categories = []
  for i,cat in enumerate(barren_categories):
    if 'req' in cat:
      if getattr(logic_settings, cat['req']) != cat['req_val']:
        continue
    valid = True
    for loc in cat["item_set"]:
      item = search_for_location(item_spheres, loc)
      if '*' in item:
        valid = False
        break
    if valid:
      valid_barren_categories.append(i)
  if len(valid_barren_categories) > 0:
    barren_category = f"  {barren_categories[random.choice(valid_barren_categories)]['category']} yields no progression\n"

  with open("./res/hints.txt", "w", encoding="utf-8") as file:
    file.write("Hints:\n")
    file.write("===================================\n")
    file.write("Barren Category:\n")
    file.write(barren_category)
    file.write("===================================\n")
    file.write("Always Hints:\n")
    file.write(always_hints)
    file.write("===================================\n")
    file.write(f"Sometimes Hints ({sometimes_hint_count}):\n")
    file.write(sometimes_hints)
    file.write("===================================\n")
    file.write(json.dumps(item_spheres, indent=2))
