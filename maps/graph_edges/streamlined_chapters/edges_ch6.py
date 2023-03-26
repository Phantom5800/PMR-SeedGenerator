"""
This file represents edges of the world graph that should be modified when
Chapter 6 is not required for Streamlined Chapters.
"""
def get_streamlined_edges_ch6_add():
    return [
        # Plaza District Flower Door -> Flower Fields Center Tree Door
        {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "FLO_00", "id": 0},
        "reqs": [["YOUWIN"]]},
    ]


def get_streamlined_edges_ch6_remove():
    return [
        # Plaza District Flower Door -> Flower Fields Center Tree Door
        {"from": {"map": "MAC_01", "id": 5}, "to": {"map": "FLO_00", "id": 0}, "reqs": []},
    ]
