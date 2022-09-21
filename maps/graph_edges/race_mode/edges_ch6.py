"""
This file represents edges of the world graph that should be modified when
Chapter 6 is not required in Race Mode.
"""


def get_edges_ch6_add(chapter_count):
    return [
        # Plaza District Flower Door -> Flower Fields Center Tree Door
        {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "FLO_00", "id": 0},
         "reqs": [[{"starspirits": chapter_count}]]},
    ]


edges_ch6_remove = [
    # Plaza District Flower Door -> Flower Fields Center Tree Door
    {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "FLO_00", "id": 0}, "reqs": []},
]
