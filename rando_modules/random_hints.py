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

  with open("./res/hints.txt", "w", encoding="utf-8") as file:
    file.write("Hints:\n")
    file.write("===================================\n")
    file.write("Always Hints:\n")
    file.write(always_hints)
    file.write("===================================\n")
    file.write(f"Sometimes Hints ({sometimes_hint_count}):\n")
    file.write(sometimes_hints)
    file.write("===================================\n")
    file.write(json.dumps(item_spheres, indent=2))
