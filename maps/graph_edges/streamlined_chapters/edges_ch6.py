"""
This file represents edges of the world graph that should be modified when
Chapter 6 is not required for Streamlined Chapters.
"""
def get_streamlined_edges_ch6_add(dest):
    return [
        # Plaza District Flower Door -> Flower Fields Center Tree Door
        {"from": {"map": "MAC_01", "id": 5}, "to": dest,
        "reqs": [["YOUWIN"]]},
    ]


def get_streamlined_edges_ch6_remove(dest):
    return [
        # Plaza District Flower Door -> Flower Fields Center Tree Door
        {"from": {"map": "MAC_01", "id": 5}, "to": dest, "reqs": []},
    ]
