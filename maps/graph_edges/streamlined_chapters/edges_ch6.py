"""
This file represents edges of the world graph that should be modified when
Chapter 6 is not required for Streamlined Chapters.
"""
streamlined_edges_ch6_add = [
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 5}, 
    "reqs": [
        ["MagicalSeed1", "RF_MagicalSeed1"],
        ["MagicalSeed2", "RF_MagicalSeed2"],
        ["MagicalSeed3", "RF_MagicalSeed3"],
        ["MagicalSeed4", "RF_MagicalSeed4"],
        ["YOUWIN"]
    ]}
]

streamlined_edges_ch6_remove = [
    {"from": {"map": "MAC_01", "id": 0}, "to": {"map": "MAC_01", "id": 5}, 
    "reqs": [
        ["MagicalSeed1", "RF_MagicalSeed1"],
        ["MagicalSeed2", "RF_MagicalSeed2"],
        ["MagicalSeed3", "RF_MagicalSeed3"],
        ["MagicalSeed4", "RF_MagicalSeed4"]
    ]}
]
