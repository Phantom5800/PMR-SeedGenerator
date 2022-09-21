"""
This file represents edges of the world graph that should be modified when
Chapter 7 is not required in Race Mode.
"""


def get_edges_ch7_add(chapter_count):
    return [
        # Frozen Room (B3) Green Pipe Right -> Shiver City Center Greep Pipe
        {"from": {"map": "TIK_17", "id": 1}, "to": {"map": "SAM_02", "id": 2},
         "reqs": [[{"starspirits": chapter_count}]]},
    ]


edges_ch7_remove = [
    # Frozen Room (B3) Green Pipe Right -> Shiver City Center Greep Pipe
    {"from": {"map": "TIK_17", "id": 1}, "to": {"map": "SAM_02", "id": 2}, "reqs": []},
]
