"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Laki Jailbreak.
"""
edges_trd_add_laki_jailbreak = [
    #? Central Hall Exit Bottom Left -> ItemA (KoopaFortressKey)
    {"from": {"map": "TRD_03", "id": 0}, "to": {"map": "TRD_03", "id": "ItemA"}, "reqs": [["Lakilester"]], "mapchange": False},
    #?ItemA (KoopaFortressKey) ->  Central Hall Exit Top Left
    {"from": {"map": "TRD_03", "id": "ItemA"}, "to": {"map": "TRD_03", "id": 2}, "reqs": [["Lakilester"]], "mapchange": False},
]
