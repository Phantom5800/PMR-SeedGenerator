import json

always_hint_to_check_mapping = {
  "Blooper Chest": "Blooper Boss 1 (B1) - Blooper Fight Reward",
  "Lakilester": "(NW) Lakilester - Lakilester Partner",
  "Yoshi Chief": "Village Cove - Village Leader Reward"
}

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

  with open("./res/hints.txt", "w", encoding="utf-8") as file:
    file.write("Hints:\n")
    file.write("===================================\n")
    file.write("Always Hints:\n")
    file.write(always_hints)
    file.write("===================================\n")
    file.write(json.dumps(item_spheres, indent=2))
