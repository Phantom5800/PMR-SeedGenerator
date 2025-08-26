"""
This file represents edges of the world graph that have to be added
for Glitched Logic: Small Statue Skip

Skips pushing the small statue above the P-Up D-Down chest by climbing the large statue
and jumping out of bounds to the Palace Key chest.
"""
edges_pra_add_small_statue_skip= [
    #? Huge Statue Room Door West -> Huge Statue Room Basement Door
    {"from": {"map": "PRA_21", "id": 0}, "to": {"map": "PRA_21", "id": 1}, "reqs": [["UltraBoots"]], "mapchange": False}, 
]
