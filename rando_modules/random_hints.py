import json
import random

# always hints are always generated
always_hint_to_check_mapping = {
  "Blooper Chest": "Blooper Boss 1 (B1) - Blooper Fight Reward",
  "Lakilester": "(NW) Lakilester - Lakilester Partner",
  "Yoshi Chief": "Village Cove - Village Leader Reward"
}

# a subset of sometimes hints are generated at random each time
sometimes_hint_to_check_mapping = {
  "Anti Guy Chest": "BLU Anti-Guy Hall - In Chest",
  "Kolorado Vase": "Village Buildings - Kolorado Volcano Vase Reward",
  "Lantern Ghost": "RED Lantern Ghost - Watt Partner",
  "Mayor Penguin": "Shiver City Mayor Area - Mayor Penguin Gift",
  "Merle": "Starborn Valley - Merle Gift",
  "Moles": "(East) Petunias Field - Petunia Gift",
  "Parakarry Letters": "Train Station - Parakarry Partner",
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

def generate_hints(item_spheres:dict):
  always_hints = ""
  for k in always_hint_to_check_mapping:
    always_hints += f"  {k} is {search_for_location(item_spheres, always_hint_to_check_mapping[k])}\n"

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
