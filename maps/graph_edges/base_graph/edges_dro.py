"""This file represents all edges of the world graph that have origin-nodes in the DRO (Dry Dry Outpost) area."""
edges_dro = [
    # DRO_01 Outpost 1
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "SBK_36", "id": 1}, "reqs": []}, # Outpost 1 Exit West -> E3 Outside Outpost Exit East
    {"from": {"map": "DRO_01", "id": 1}, "to": {"map": "DRO_02", "id": 0}, "reqs": []}, # Outpost 1 Exit East -> Outpost 2 Exit West
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "TIK_01", "id": 4}, "reqs": []}, # Outpost 1 Blue Warp Pipe -> Warp Zone 1 (B1) Blue Warp Pipe (Left)
    
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 1}, "reqs": []}, #? Outpost 1 Exit West -> Outpost 1 Exit East
    {"from": {"map": "DRO_01", "id": 1}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, #? Outpost 1 Exit East -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0}, "to": {"map": "DRO_01", "id": 2}, "reqs": [["GF_TIK01_WarpPipes"]]}, #? Outpost 1 Exit West -> Outpost 1 Blue Warp Pipe
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "DRO_01", "id": 0}, "reqs": []}, #? Outpost 1 Blue Warp Pipe -> Outpost 1 Exit West
    
    {"from": {"map": "DRO_01", "id": 2}, "to": {"map": "DRO_01", "id": 2}, "reqs": [], "pseudoitems": ["GF_TIK01_WarpPipes"]}, #+ Outpost 1 Blue Warp Pipe
    
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "GiftA"},     "reqs": [["Lyrics"]]}, #* Outpost 1 Exit West -> GiftA (Melody)
    {"from": {"map": "DRO_01", "id": "GiftA"},     "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* GiftA (Melody) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "GiftB"},     "reqs": [["RF_MouserReturned"],["FAVOR_7_02_done"]]}, #* Outpost 1 Exit West -> GiftB (KootRedJar)
    {"from": {"map": "DRO_01", "id": "GiftB"},     "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* GiftB (KootRedJar) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "GiftC"},     "reqs": [["RF_MouserReturned"],["Parakarry"],["Letter19"]]}, #* Outpost 1 Exit West -> GiftC (Letter12)
    {"from": {"map": "DRO_01", "id": "GiftC"},     "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* GiftC (Letter12) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemA"}, "reqs": [["RF_MouserReturned"]]}, #* Outpost 1 Exit West -> ShopItemA (ThunderBolt)
    {"from": {"map": "DRO_01", "id": "ShopItemA"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemA (ThunderBolt) -> Outpost 1 Exit West
    # {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemB"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemB (DustyHammer)
    # {"from": {"map": "DRO_01", "id": "ShopItemB"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemB (DustyHammer) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemC"}, "reqs": [["RF_MouserReturned"]]}, #* Outpost 1 Exit West -> ShopItemC (HoneySyrup)
    {"from": {"map": "DRO_01", "id": "ShopItemC"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemC (HoneySyrup) -> Outpost 1 Exit West
    # {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemD"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemD (DriedShroom)
    # {"from": {"map": "DRO_01", "id": "ShopItemD"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemD (DriedShroom) -> Outpost 1 Exit West
    # {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemE"}, "reqs": []}, #* Outpost 1 Exit West -> ShopItemE (DriedPasta)
    # {"from": {"map": "DRO_01", "id": "ShopItemE"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemE (DriedPasta) -> Outpost 1 Exit West
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": "ShopItemF"}, "reqs": [["RF_MouserReturned"]]}, #* Outpost 1 Exit West -> ShopItemF (Mushroom)
    {"from": {"map": "DRO_01", "id": "ShopItemF"}, "to": {"map": "DRO_01", "id": 0},           "reqs": []}, #* ShopItemF (Mushroom) -> Outpost 1 Exit West

    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": 0}, "reqs": [["RF_MouserReturned"]], "pseudoitems": ["DriedPasta"]}, #+ ShopItemE
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": 0}, "reqs": [["RF_MouserReturned"],["RF_CanUseDROCode"]], "pseudoitems": ["RF_CanMeetMoustafa"]}, #+ ShopItemE
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": 0}, "reqs": [], "pseudoitems": ["RF_MouserLeftShop"]}, #+ ShopItemE
    {"from": {"map": "DRO_01", "id": 0},           "to": {"map": "DRO_01", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_DRO_1",
                                                                                                             #    "StarPiece_DRO_2",
                                                                                                             #    "StarPiece_DRO_3",
                                                                                                             #    "StarPiece_DRO_4",
                                                                                                             #    "StarPiece_DRO_5",
                                                                                                             #    "StarPiece_DRO_6",
                                                                                                             #    "StarPiece_DRO_7",
                                                                                                                 "StarPiece_DRO_8"]}, #+ Quizmo StarPieces

    # DRO_02 Outpost 2
    {"from": {"map": "DRO_02", "id": 0}, "to": {"map": "DRO_01", "id": 1}, "reqs": []}, # Outpost 2 Exit West -> Outpost 1 Exit East
    
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "GiftA"},       "reqs": [["GF_HOS06_MerluvleeRequestedCrystalBall"]]}, #* Outpost 2 Exit West -> GiftA (CrystalBall)
    {"from": {"map": "DRO_02", "id": "GiftA"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* GiftA (CrystalBall) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "GiftB"},       "reqs": [["RF_CanMeetMoustafa"]]}, #* Outpost 2 Exit West -> GiftB (PulseStone)
    {"from": {"map": "DRO_02", "id": "GiftB"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* GiftB (PulseStone) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "GiftC"},       "reqs": [["Parakarry"],["Letter17"]]}, #* Outpost 2 Exit West -> GiftC (Letter18)
    {"from": {"map": "DRO_02", "id": "GiftC"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* GiftC (Letter18) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"],["RF_CanMeetMoustafa"]]}, #* Outpost 2 Exit West -> HiddenPanel (StarPiece)
    {"from": {"map": "DRO_02", "id": "HiddenPanel"}, "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Outpost 2 Exit West
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": "ItemA"},       "reqs": [["RF_CanMeetMoustafa"]]}, #* Outpost 2 Exit West -> ItemA (Letter08)
    {"from": {"map": "DRO_02", "id": "ItemA"},       "to": {"map": "DRO_02", "id": 0},             "reqs": []}, #* ItemA (Letter08) -> Outpost 2 Exit West
 
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": 0}, "reqs": [["RF_MouserLeftShop"]], "pseudoitems": ["RF_MouserReturned"]}, #+ Chapter Progress
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": 0}, "reqs": [["Lemon"]], "pseudoitems": ["RF_CanUseDROCode"]}, #+ Chapter Progress
    {"from": {"map": "DRO_02", "id": 0},             "to": {"map": "DRO_02", "id": 0}, "reqs": [], "pseudoitems": ["StarPiece_DRO_1",
                                                                                                                #   "StarPiece_DRO_2",
                                                                                                                #   "StarPiece_DRO_3",
                                                                                                                #   "StarPiece_DRO_4",
                                                                                                                #   "StarPiece_DRO_5",
                                                                                                                #   "StarPiece_DRO_6",
                                                                                                                #   "StarPiece_DRO_7",
                                                                                                                   "StarPiece_DRO_8"]}, #+ Quizmo StarPieces
]
