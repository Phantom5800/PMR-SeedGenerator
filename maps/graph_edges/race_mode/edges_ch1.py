"""
This file represents edges of the world graph that should be modified when
Chapter 1 is not required in Race Mode.
"""


def get_edges_ch1_add(chapter_count):
    return [
        # Gate District Exit Left -> Toad Town Entrance Exit Right
        {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "KMR_10", "id": 1},
         "reqs": [[{"starspirits": chapter_count}]]},

        # Plaza District Exit Right -> Pleasant Path Entry Exit Left
        {"from": {"map": "MAC_01", "id": 1}, "to": {"map": "NOK_11", "id": 0},
         "reqs": [[{"starspirits": chapter_count}]]},

        # Warp Zone 1 (B1) Blue Warp Pipe (Right) -> Goomba Village Blue Warp Pipe
        {"from": {"map": "TIK_01", "id": 2}, "to": {"map": "KMR_02", "id": 3},
         "reqs": [[{"starspirits": chapter_count}]]},

        # Warp Zone 1 (B1) Blue Warp Pipe (Center) -> Koopa Village 2 Blue Pipe
        {"from": {"map": "TIK_01", "id": 3}, "to": {"map": "NOK_02", "id": 2},
         "reqs": [[{"starspirits": chapter_count}]]},
    ]


edges_ch1_remove = [
    # Gate District Exit Left -> Toad Town Entrance Exit Right
    {"from": {"map": "MAC_00", "id": 0}, "to": {"map": "KMR_10", "id": 1}, "reqs": []},

    # Plaza District Exit Right -> Pleasant Path Entry Exit Left
    {"from": {"map": "MAC_01", "id": 1}, "to": {"map": "NOK_11", "id": 0}, "reqs": []},

    # Warp Zone 1 (B1) Blue Warp Pipe (Right) -> Goomba Village Blue Warp Pipe
    {"from": {"map": "TIK_01", "id": 2}, "to": {"map": "KMR_02", "id": 3}, "reqs": []},

    # Warp Zone 1 (B1) Blue Warp Pipe (Center) -> Koopa Village 2 Blue Pipe
    {"from": {"map": "TIK_01", "id": 3}, "to": {"map": "NOK_02", "id": 2}, "reqs": []},
]
