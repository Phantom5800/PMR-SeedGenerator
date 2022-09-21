"""
This file represents edges of the world graph that should be modified when
Chapter 4 is not required in Race Mode.
"""


def get_edges_ch4_add(chapter_count):
    return [
        # Residental District Toybox Spring -> BLU Station Spring Exit
        {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "OMO_03", "id": 4},
         "reqs": [[{"starspirits": chapter_count}]]},
    ]


edges_ch4_remove = [
    # Residental District Toybox Spring -> BLU Station Spring Exit
    {"from": {"map": "MAC_04", "id": 2}, "to": {"map": "OMO_03", "id": 4}, "reqs": []},
]
