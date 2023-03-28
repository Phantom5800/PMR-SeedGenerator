"""
This file represents edges of the world graph that should be modified when
Chapter 4 is not required for Streamlined Chapters.
"""
streamlined_edges_ch4_add = [
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 2}, 
    "reqs": [["Bow","RF_ToyboxOpen"],["can_climb_steps"],["YOUWIN"]]}
]

streamlined_edges_ch4_remove = [
    {"from": {"map": "MAC_04", "id": 0}, "to": {"map": "MAC_04", "id": 2}, 
    "reqs": [["Bow","RF_ToyboxOpen"],["can_climb_steps"]]}
]
