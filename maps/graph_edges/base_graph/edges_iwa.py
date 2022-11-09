"""This file represents all edges of the world graph that have origin-nodes in the IWA (Mt. Rugged) area."""
edges_iwa = [
    # IWA_00 Mt Rugged 1
    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": []}, # Mt Rugged 1 Exit Left -> Train Station Exit Top Right
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_01", "id": 0}, "reqs": []}, # Mt Rugged 1 Exit Right -> Mt Rugged 2 Exit Bottom Left

    {"from": {"map": "IWA_00", "id": 0}, "to": {"map": "IWA_00", "id": 1}, "reqs": [["can_climb_steps", "Lakilester"]]}, #? Mt Rugged 1 Exit Left -> Mt Rugged 1 Exit Right
    {"from": {"map": "IWA_00", "id": 1}, "to": {"map": "IWA_00", "id": 0}, "reqs": []}, #? Mt Rugged 1 Exit Right -> Mt Rugged 1 Exit Left

    {"from": {"map": "IWA_00", "id": 0},         "to": {"map": "IWA_00", "id": "ItemA"},   "reqs": []}, #* Mt Rugged 1 Exit Left -> ItemA (Coin)
    {"from": {"map": "IWA_00", "id": "ItemA"},   "to": {"map": "IWA_00", "id": 0},         "reqs": []}, #* ItemA (Coin) -> Mt Rugged 1 Exit Left
    {"from": {"map": "IWA_00", "id": 0},         "to": {"map": "IWA_00", "id": "ItemB"},   "reqs": [["Kooper", "Lakilester"]]}, #* Mt Rugged 1 Exit Left -> ItemB (Coin)
    {"from": {"map": "IWA_00", "id": 1},         "to": {"map": "IWA_00", "id": "ItemB"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 1 Exit Right -> ItemB (Coin)
    {"from": {"map": "IWA_00", "id": "ItemB"},   "to": {"map": "IWA_00", "id": 0},         "reqs": []}, #* ItemB (Coin) -> Mt Rugged 1 Exit Left
    {"from": {"map": "IWA_00", "id": 0},         "to": {"map": "IWA_00", "id": "ItemC"},   "reqs": [["Kooper", "Lakilester"]]}, #* Mt Rugged 1 Exit Left -> ItemC (Coin)
    {"from": {"map": "IWA_00", "id": 1},         "to": {"map": "IWA_00", "id": "ItemC"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 1 Exit Right -> ItemC (Coin)
    {"from": {"map": "IWA_00", "id": "ItemC"},   "to": {"map": "IWA_00", "id": 0},         "reqs": []}, #* ItemC (Coin) -> Mt Rugged 1 Exit Left
    {"from": {"map": "IWA_00", "id": 1},         "to": {"map": "IWA_00", "id": "ItemD"},   "reqs": [["Hammer", "Bombette"],["RF_Missable"]]}, #* Mt Rugged 1 Exit Right -> ItemD (WhackasBump)
    {"from": {"map": "IWA_00", "id": "ItemD"},   "to": {"map": "IWA_00", "id": 1},         "reqs": []}, #* ItemD (WhackasBump) -> Mt Rugged 1 Exit Right
    {"from": {"map": "IWA_00", "id": 1},         "to": {"map": "IWA_00", "id": "YBlockA"}, "reqs": [["can_hit_floating_blocks"]]}, #* Mt Rugged 1 Exit Right -> YBlockA (SleepySheep)
    {"from": {"map": "IWA_00", "id": "YBlockA"}, "to": {"map": "IWA_00", "id": 1},         "reqs": []}, #* YBlockA (SleepySheep) -> Mt Rugged 1 Exit Right

    # IWA_01 Mt Rugged 2
    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_00", "id": 1}, "reqs": []}, # Mt Rugged 2 Exit Bottom Left -> Mt Rugged 1 Exit Right
    {"from": {"map": "IWA_01", "id": 1}, "to": {"map": "IWA_03", "id": 0}, "reqs": []}, # Mt Rugged 2 Exit Top Left -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 2}, "to": {"map": "IWA_02", "id": 0}, "reqs": []}, # Mt Rugged 2 Exit Bottom Right -> Mt Rugged 3 Exit Bottom Left
    {"from": {"map": "IWA_01", "id": 3}, "to": {"map": "IWA_02", "id": 1}, "reqs": []}, # Mt Rugged 2 Exit Top Right -> Mt Rugged 3 Exit Top Left

    {"from": {"map": "IWA_01", "id": 0}, "to": {"map": "IWA_01", "id": 2}, "reqs": [["Boots"]]}, #? Mt Rugged 2 Exit Bottom Left -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_01", "id": 2}, "to": {"map": "IWA_01", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Mt Rugged 2 Exit Bottom Right -> Mt Rugged 2 Exit Bottom Left
    {"from": {"map": "IWA_01", "id": 3}, "to": {"map": "IWA_01", "id": 1}, "reqs": []}, #? Mt Rugged 2 Exit Top Right -> Mt Rugged 2 Exit Top Left
    {"from": {"map": "IWA_01", "id": 1}, "to": {"map": "IWA_01", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Mt Rugged 2 Exit Top Left -> Mt Rugged 2 Exit Bottom Left

    {"from": {"map": "IWA_01", "id": 0},             "to": {"map": "IWA_01", "id": "HiddenPanel"}, "reqs": [["can_flip_panels"]]}, #* Mt Rugged 2 Exit Bottom Left -> HiddenPanel (StarPiece)
    {"from": {"map": "IWA_01", "id": "HiddenPanel"}, "to": {"map": "IWA_01", "id": 0},             "reqs": []}, #* HiddenPanel (StarPiece) -> Mt Rugged 2 Exit Bottom Left
    {"from": {"map": "IWA_01", "id": "ItemB"},       "to": {"map": "IWA_01", "id": "ItemA"},       "reqs": [["Parakarry"]]}, #* ItemB (Letter01) -> ItemA (QuakeHammer)
    {"from": {"map": "IWA_01", "id": "ItemA"},       "to": {"map": "IWA_01", "id": "ItemB"},       "reqs": []}, #* ItemA (QuakeHammer) -> ItemB (Letter01)
    {"from": {"map": "IWA_01", "id": 2},             "to": {"map": "IWA_01", "id": "ItemB"},       "reqs": [["Kooper","Parakarry"]]}, #* Mt Rugged 2 Exit Bottom Right -> ItemB (Letter01)
    {"from": {"map": "IWA_01", "id": "ItemB"},       "to": {"map": "IWA_01", "id": 2},             "reqs": []}, #* ItemB (Letter01) -> Mt Rugged 2 Exit Bottom Right

    # IWA_02 Mt Rugged 3
    {"from": {"map": "IWA_02", "id": 0}, "to": {"map": "IWA_01", "id": 2}, "reqs": []}, # Mt Rugged 3 Exit Bottom Left -> Mt Rugged 2 Exit Bottom Right
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_01", "id": 3}, "reqs": []}, # Mt Rugged 3 Exit Top Left -> Mt Rugged 2 Exit Top Right
    {"from": {"map": "IWA_02", "id": 2}, "to": {"map": "IWA_04", "id": 0}, "reqs": []}, # Mt Rugged 3 Exit Top Right -> Suspension Bridge Exit Left

    {"from": {"map": "IWA_02", "id": 0}, "to": {"map": "IWA_02", "id": 1}, "reqs": [["can_climb_steps"]]}, #? Mt Rugged 3 Exit Bottom Left -> Mt Rugged 3 Exit Top Left
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_02", "id": 0}, "reqs": []}, #? Mt Rugged 3 Exit Top Left -> Mt Rugged 3 Exit Bottom Left
    {"from": {"map": "IWA_02", "id": 1}, "to": {"map": "IWA_02", "id": 2}, "reqs": []}, #? Mt Rugged 3 Exit Top Left -> Mt Rugged 3 Exit Top Right
    {"from": {"map": "IWA_02", "id": 2}, "to": {"map": "IWA_02", "id": 1}, "reqs": []}, #? Mt Rugged 3 Exit Top Right -> Mt Rugged 3 Exit Top Left

    {"from": {"map": "IWA_02", "id": 0},       "to": {"map": "IWA_02", "id": "GiftA"}, "reqs": [["Parakarry"]]}, #* Mt Rugged 3 Exit Bottom Left -> GiftA (MagicalSeed2)
    {"from": {"map": "IWA_02", "id": "GiftA"}, "to": {"map": "IWA_02", "id": 0},       "reqs": []}, #* GiftA (MagicalSeed2) -> Mt Rugged 3 Exit Bottom Left
    {"from": {"map": "IWA_02", "id": 1},       "to": {"map": "IWA_02", "id": "ItemA"}, "reqs": []}, #* Mt Rugged 3 Exit Top Left -> ItemA (StarPiece)
    {"from": {"map": "IWA_02", "id": "ItemA"}, "to": {"map": "IWA_02", "id": 1},       "reqs": []}, #* ItemA (StarPiece) -> Mt Rugged 3 Exit Top Left

    # IWA_03 Mt Rugged 4
    {"from": {"map": "IWA_03", "id": 0}, "to": {"map": "IWA_01", "id": 1}, "reqs": []}, # Mt Rugged 4 Exit Bottom Right -> Mt Rugged 2 Exit Top Left

    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ChestA"},  "reqs": [["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> ChestA (DamageDodgeB)
    {"from": {"map": "IWA_03", "id": "ChestA"},  "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ChestA (DamageDodgeB) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemA"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemA (Letter25)
    {"from": {"map": "IWA_03", "id": "ItemA"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemA (Letter25) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemB"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemB (StarPiece)
    {"from": {"map": "IWA_03", "id": "ItemB"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemB (StarPiece) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemC"},   "reqs": [["Kooper","Parakarry"],["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemC (Coin) (circle-right)
    {"from": {"map": "IWA_03", "id": "ItemC"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemC (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemD"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemD (Coin)
    {"from": {"map": "IWA_03", "id": "ItemD"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemD (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemE"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemE (Coin)
    {"from": {"map": "IWA_03", "id": "ItemE"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemE (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemF"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemF (Coin)
    {"from": {"map": "IWA_03", "id": "ItemF"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemF (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemG"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemG (Coin)
    {"from": {"map": "IWA_03", "id": "ItemG"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemG (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemH"},   "reqs": [["Parakarry"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemH (Coin)
    {"from": {"map": "IWA_03", "id": "ItemH"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemH (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemI"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemI (Coin) (bottom1)
    {"from": {"map": "IWA_03", "id": "ItemI"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemI (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "ItemJ"},   "reqs": [["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> ItemJ (Coin) (bottom2)
    {"from": {"map": "IWA_03", "id": "ItemJ"},   "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* ItemJ (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "YBlockA"}, "reqs": [["can_hit_grounded_blocks"],["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> YBlockA (Coin)
    {"from": {"map": "IWA_03", "id": "YBlockA"}, "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* YBlockA (Coin) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "YBlockB"}, "reqs": [["can_hit_floating_blocks"]]}, #* Mt Rugged 4 Exit Bottom Right -> YBlockB (Mushroom)
    {"from": {"map": "IWA_03", "id": "YBlockB"}, "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* YBlockB (Mushroom) -> Mt Rugged 4 Exit Bottom Right
    {"from": {"map": "IWA_03", "id": 0},         "to": {"map": "IWA_03", "id": "YBlockC"}, "reqs": [["can_hit_grounded_blocks"],["can_climb_steps"]]}, #* Mt Rugged 4 Exit Bottom Right -> YBlockC (HoneySyrup)
    {"from": {"map": "IWA_03", "id": "YBlockC"}, "to": {"map": "IWA_03", "id": 0},         "reqs": []}, #* YBlockC (HoneySyrup) -> Mt Rugged 4 Exit Bottom Right

    # IWA_04 Suspension Bridge
    {"from": {"map": "IWA_04", "id": 0}, "to": {"map": "IWA_02", "id": 2}, "reqs": []}, # Suspension Bridge Exit Left -> Mt Rugged 3 Exit Top Right
    {"from": {"map": "IWA_04", "id": 1}, "to": {"map": "SBK_99", "id": 0}, "reqs": []}, # Suspension Bridge Exit Right -> Entrance Exit Left

    {"from": {"map": "IWA_04", "id": 0}, "to": {"map": "IWA_04", "id": 1}, "reqs": [["Parakarry"]]}, #? Suspension Bridge Exit Left -> Suspension Bridge Exit Right
    {"from": {"map": "IWA_04", "id": 1}, "to": {"map": "IWA_04", "id": 0}, "reqs": [["can_climb_steps"]]}, #? Suspension Bridge Exit Right -> Suspension Bridge Exit Left

    {"from": {"map": "IWA_04", "id": 0},       "to": {"map": "IWA_04", "id": "ItemA"}, "reqs": []}, #* Suspension Bridge Exit Left -> ItemA (Letter10)
    {"from": {"map": "IWA_04", "id": "ItemA"}, "to": {"map": "IWA_04", "id": 0},       "reqs": []}, #* ItemA (Letter10) -> Suspension Bridge Exit Left

    # IWA_10 Train Station
    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_11", "id": 1}, "reqs": []}, # Train Station Ride The Train -> Train Ride Scene Exit Right
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_00", "id": 0}, "reqs": []}, # Train Station Exit Top Right -> Mt Rugged 1 Exit Left

    {"from": {"map": "IWA_10", "id": 0}, "to": {"map": "IWA_10", "id": 1}, "reqs": [["Boots"]]}, #? Train Station Ride The Train -> Train Station Exit Top Right
    {"from": {"map": "IWA_10", "id": 1}, "to": {"map": "IWA_10", "id": 0}, "reqs": [["Boots"]]}, #? Train Station Exit Top Right -> Train Station Ride The Train

    {"from": {"map": "IWA_10", "id": 0},             "to": {"map": "IWA_10", "id": "Bush1_Drop1"}, "reqs": []}, #* Train Station Ride The Train -> Bush1_Drop1 (Coin) Bottom Bush
    {"from": {"map": "IWA_10", "id": 1},             "to": {"map": "IWA_10", "id": "Bush1_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush1_Drop1 (Coin) Bottom Bush
    {"from": {"map": "IWA_10", "id": "Bush1_Drop1"}, "to": {"map": "IWA_10", "id": 0},             "reqs": [["Boots"]]}, #* Bush1_Drop1 (Coin) Bottom Bush -> Train Station Ride The Train
    {"from": {"map": "IWA_10", "id": 0},             "to": {"map": "IWA_10", "id": "Bush2_Drop1"}, "reqs": []}, #* Train Station Ride The Train -> Bush2_Drop1 (Coin) Right Bush
    {"from": {"map": "IWA_10", "id": 1},             "to": {"map": "IWA_10", "id": "Bush2_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush2_Drop1 (Coin) Right Bush
    {"from": {"map": "IWA_10", "id": "Bush2_Drop1"}, "to": {"map": "IWA_10", "id": 0},             "reqs": [["Boots"]]}, #* Bush2_Drop1 (Coin) Right Bush -> Train Station Ride The Train
    {"from": {"map": "IWA_10", "id": 0},             "to": {"map": "IWA_10", "id": "Bush3_Drop1"}, "reqs": []}, #* Train Station Ride The Train -> Bush3_Drop1 (Coin) Left Bush
    {"from": {"map": "IWA_10", "id": 1},             "to": {"map": "IWA_10", "id": "Bush3_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush3_Drop1 (Coin) Left Bush
    {"from": {"map": "IWA_10", "id": "Bush3_Drop1"}, "to": {"map": "IWA_10", "id": 0},             "reqs": [["Boots"]]}, #* Bush3_Drop1 (Coin) Left Bush -> Train Station Ride The Train
    {"from": {"map": "IWA_10", "id": 0},             "to": {"map": "IWA_10", "id": "Bush4_Drop1"}, "reqs": []}, #* TrainTrain Station Ride The Train -> Bush4_Drop1 (Egg2) Top Bush
    {"from": {"map": "IWA_10", "id": 1},             "to": {"map": "IWA_10", "id": "Bush4_Drop1"}, "reqs": []}, #* Train Station Exit Top Right -> Bush4_Drop1 (Egg2) Top Bush
    {"from": {"map": "IWA_10", "id": "Bush4_Drop1"}, "to": {"map": "IWA_10", "id": 0},             "reqs": [["Boots"]]}, #* Bush4_Drop1 (Egg2) Top Bush -> Train Station Ride The Train
    {"from": {"map": "IWA_10", "id": 1},             "to": {"map": "IWA_10", "id": "Partner"},     "reqs": [["has_parakarry_letters"]]}, #* Train Station Exit Top Right -> Partner (Parakarry)
    {"from": {"map": "IWA_10", "id": "Partner"},     "to": {"map": "IWA_10", "id": 1},             "reqs": []}, #* Partner (Parakarry) -> Train Station Exit Top Right

    # IWA_11 Train Ride Scene
    {"from": {"map": "IWA_11", "id": 0}, "to": {"map": "MAC_03", "id": 1}, "reqs": []}, # Train Ride Scene Exit Left -> Station District Train
    {"from": {"map": "IWA_11", "id": 1}, "to": {"map": "IWA_10", "id": 0}, "reqs": []}, # Train Ride Scene Exit Right -> Train Station Ride The Train

    {"from": {"map": "IWA_11", "id": 0}, "to": {"map": "IWA_11", "id": 1}, "reqs": []}, #? Train Ride Scene Exit Left -> Train Ride Scene Exit Right
    {"from": {"map": "IWA_11", "id": 1}, "to": {"map": "IWA_11", "id": 0}, "reqs": []}, #? Train Ride Scene Exit Right -> Train Ride Scene Exit Left
]
