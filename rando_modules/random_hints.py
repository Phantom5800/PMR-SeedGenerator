import json
import random

# always hints are always generated
always_hint_to_check_mapping = [
  {
    "name": "Blooper Chest",
    "check": "Blooper Boss 1 (B1) - Blooper Fight Reward"
  },
  {
    "name": "Dry Dry Ruins 4th Key Pedestal",
    "check": "Lunar Stone Room - On Pedestal"
  },
  {
    # this check is hinted when prologue is closed
    "name": "Goomba King's Tree",
    "check": "Goomba Kings Castle - In Tree Left Of Fortress",
    "req": "prologue_open",
    "req_val": False
  },
  {
    "name": "Lakilester",
    "check": "(NW) Lakilester - Lakilester Partner"
  },
  {
    "name": "Yoshi Chief",
    "check": "Village Cove - Village Leader Reward"
  }
]

# a subset of sometimes hints are generated at random each time
sometimes_hint_to_check_mapping = {
  "Anti Guy Chest": "BLU Anti-Guy Hall - In Chest",
  "Kolorado Camp Tree": "W3 Kolorados Camp - In Tree",
  "Kolorado Vase": "Village Buildings - Kolorado Volcano Vase Reward",
  "Lantern Ghost": "RED Lantern Ghost - Watt Partner",
  "Mayor Penguin": "Shiver City Mayor Area - Mayor Penguin Gift",
  "Merle": "Starborn Valley - Merle Gift",
  "Moles": "(East) Petunias Field - Petunia Gift",
  "Parakarry Letters": "Train Station - Parakarry Partner",
  "Shiver Mountain Sanctuary": "Merlars Sanctuary - On Pedestal",
  "Volcano Chest": "Sushi Tree - In Volcano Chest",
  "Yellow Yoshi": "Village Buildings - Yellow Yoshi Food Reward",
}
sometimes_hint_count = 4

# Hint 1 barren category if possible, check all items in said group,
# if 0 key items are found, category can be hinted barren.
# This set of categories is ordered by what would be the most impactful at the top to least
# at the bottom in case giving highest priority is better than random.
barren_categories = [
  {
    "category": "Letter Delivery",
    "item_set": [
      "Plaza District - Merlon Letter Reward",
      "Koopa Village 2 - Kolorado Letter Reward",
      "Koopa Village 1 - Mort T. Letter Reward",
      "E1 Nomadimouse - Nomadimouse Letter Reward",
      "Goomba Village - Goompa Letter Reward",
      "Southern District - Fice T. Letter Reward",
      "Basement - Igor Letter Reward",
      "Gate District - Russ T. Letter Reward",
      "Plaza District - Minh T. Letter Reward",
      "Shiver City Mayor Area - Mayor Penguin Letter Reward",
      "Merluvlees House - Merlow Letter Reward"
      "Goomba Village - Goompapa Letter Reward 1",
      "Ruined Castle Grounds - Muss T. Letter Reward"
      "Koopa Village 1 - Koover Letter Reward 1",
      "Port District - Fishmael Letter Reward",
      "Koopa Village 1 - Koover Letter Reward 2",
      "Outpost 2 - Mr. E. Letter Reward",
      "Gate District - Miss T. Letter Reward",
      "Outpost 1 - Little Mouser Letter Reward",
      "Foyer - Franky Letter Reward",
      "Station District - Dane T. Letter Reward 1",
      "Village Buildings - Red Yoshi Kid Letter Reward",
      "Station District - Dane T. Letter Reward 2",
      "Starborn Valley - Frost T. Letter Reward",
      "Goomba Village - Goompapa Letter Reward 2"
    ],
    "req": "include_letters_mode",
    "req_val": 3, # full random
    "priority": 1
  },
  {
    "category": "Rowf",
    "item_set": [
      "Plaza District - Rowfs Shop Set 1 - 1",
      "Plaza District - Rowfs Shop Set 1 - 2",
      "Plaza District - Rowfs Shop Set 1 - 3",
      "Plaza District - Rowfs Shop Set 1 - 4",
      "Plaza District - Rowfs Shop Set 2 - 1",
      "Plaza District - Rowfs Shop Set 2 - 2",
      "Plaza District - Rowfs Shop Set 2 - 3",
      "Plaza District - Rowfs Shop Set 3 - 1",
      "Plaza District - Rowfs Shop Set 3 - 2",
      "Plaza District - Rowfs Shop Set 3 - 3",
      "Plaza District - Rowfs Shop Set 4 - 1",
      "Plaza District - Rowfs Shop Set 4 - 2",
      "Plaza District - Rowfs Shop Set 4 - 3",
      "Plaza District - Rowfs Shop Set 5 - 1",
      "Plaza District - Rowfs Shop Set 5 - 2",
      "Plaza District - Rowfs Shop Set 5 - 3"
    ],
    "req": "progression_on_rowf",
    "req_val": 5,
    "priority": 1
  },
  {
    "category": "Letter Delivery",
    "item_set": [
      "Plaza District - Merlon Letter Reward",
      "Koopa Village 2 - Kolorado Letter Reward",
      "Koopa Village 1 - Mort T. Letter Reward",
      "E1 Nomadimouse - Nomadimouse Letter Reward",
      "Goomba Village - Goompa Letter Reward",
      "Southern District - Fice T. Letter Reward",
      "Basement - Igor Letter Reward",
      "Gate District - Russ T. Letter Reward",
      "Plaza District - Minh T. Letter Reward",
      "Shiver City Mayor Area - Mayor Penguin Letter Reward",
      "Merluvlees House - Merlow Letter Reward"
    ],
    "req": "include_letters_mode",
    "req_val": 1, # vanilla letter chain
    "priority": 2
  },
    {
    "category": "Letter Delivery",
    "item_set": [
      "Plaza District - Merlon Letter Reward",
      "Koopa Village 2 - Kolorado Letter Reward",
      "Koopa Village 1 - Mort T. Letter Reward",
      "E1 Nomadimouse - Nomadimouse Letter Reward",
      "Goomba Village - Goompa Letter Reward",
      "Southern District - Fice T. Letter Reward",
      "Basement - Igor Letter Reward",
      "Gate District - Russ T. Letter Reward",
      "Plaza District - Minh T. Letter Reward",
      "Shiver City Mayor Area - Mayor Penguin Letter Reward",
      "Merluvlees House - Merlow Letter Reward"
      "Goomba Village - Goompapa Letter Reward 2"
    ],
    "req": "include_letters_mode",
    "req_val": 2, # basic letters and letter chain final letter
    "priority": 2
  },
  {
    # hint only applies to items in tall blocks, does not mean the entirity of chapter 7 can be dead
    "category": "Ultra Boots",
    "item_set": [
      "Hall to Ultra Boots (B3) - Hidden Block",
      "Hall to Ultra Boots (B3) - Yellow Block Left",
      "Hall to Ultra Boots (B3) - Yellow Block Right",
      "Shiver Mountain Passage - Hidden Block",
      "Bridge to Shiver City (B2) - Yellow Block 1",
      "Bridge to Shiver City (B2) - Yellow Block 2",
      "Bridge to Shiver City (B2) - Yellow Block 3",
      "Bridge to Shiver City (B2) - Yellow Block 4",
      "Bridge to Shiver City (B2) - Yellow Block 5",
      "Room with Spikes (B2) - Yellow Block",
      "Huge Statue Room - Yellow Block",
      "Small Statue Room - Hidden Block"
    ],
    "priority": 2
  },
  {
    # hint only applies to checks behind the yellow plant, does not include the vines next to said plant
    "category": "Yellow Berry",
    "item_set": [
      "(SE) Briar Platforming - In The Flowers",
      "(SE) Briar Platforming - In Tree 1",
      "(SE) Briar Platforming - In Tree 2",
      "(SE) Briar Platforming - In SuperBlock",
      "(SE) Water Level Room - Hidden Panel",
      "(SE) Water Level Room - Hidden Block",
      "(SE) Water Level Room - Yellow Block",
      "(SE) Water Level Room - In Tree 1",
      "(SE) Water Level Room - In Tree 2",
      "(SE) Lilys Fountain - Lily Reward For WaterStone",
      "(SE) Lilys Fountain - In Tree"
    ],
    "priority": 2
  },
  {
    # hint only applies to items behind metal blocks
    "category": "Ultra Hammer",
    "item_set": [
      "Dizzy Stomp Room - In Chest",
      "Ultra Boots Room (B3) - In Big Chest",
      "Boss Room - Yellow Block Left",
      "Boss Room - Yellow Block Right",
      "Metal Block Room (B3) - In SuperBlock"
    ],
    "priority": 3
  },
  {
    "category": "Coconut Trees",
    "item_set": [
      "Whale Cove - In Palm Tree",
      "Beach - In Palm Tree 1",
      "Beach - In Palm Tree 2",
      "Beach - In Palm Tree 3",
      "Beach - In Palm Tree 4",
      "Beach - In Palm Tree 5",
      "Beach - In Palm Tree 6",
      "Beach - In Palm Tree 6 2",
      "Village Cove - In Palm Tree Left",
      "Village Cove - In Palm Tree Right",
      "Village Buildings - In Palm Tree"
    ],
    "priority": 3
  },
  {
    "category": "Blue Berry",
    "item_set": [
      "(East) Old Well - Well BlueBerry Reward",
      "(West) Rosies Trellis - Rosie Gift",
      "(West) Path to Maze - Upper Hidden Block",
      "(West) Path to Maze - Lower Hidden Block"
    ],
    "priority": 3
  },
  {
    "category": "Red Berry",
    "item_set": [
      "(SW) Posie and Crystal Tree - Posie Gift 1",
      "(SW) Posie and Crystal Tree - Posie Gift 2",
      "(SW) Path to Crystal Tree - Hidden Panel",
      "(SW) Path to Crystal Tree - Central Vine",
      "(SW) Path to Crystal Tree - In Tree 1",
      "(SW) Path to Crystal Tree - In Tree 2"
    ],
    "priority": 3
  },
]

# Hint 3 barren regions if possible, check all items in said group,
# if 0 key items are found, region can be hinted barren.
# If a dungeon can be hinted barren, prioritize 1 dungeon.
# Some region exceptions:
#  * Flower Fields excluded because of berry categories,
#  * Shy Guys Toy Box split into 4 stations, each station is not considered
#    for the dungeon barren hint.
barren_regions = [
  {
    "category": "Koopa Bros. Fortress",
    "item_set": [
      "Fortress Exterior - Chest Behind Fortress",
      "Left Tower - Top Of Tower",
      "Left Tower - Koopa Troopa Reward",
      "Central Hall - Left Cell",
      "Central Hall - Right Cell",
      "Central Hall - Center Cell",
      "Jail - Bombette Partner",
      "Dungeon Fire Room - On The Ground",
      "Battlement - Block Behind Rock"
    ],
    "dungeon": True
  },
  {
    "category": "Dry Dry Ruins",
    "item_set": [
      "Sarcophagus Hall 1 - In Sarcophagus",
      "Sand Drainage Room 1 - On The Ground",
      "Sand Drainage Room 2 - In The Sand",
      "Sand Drainage Room 2 - On Ledge",
      "Sarcophagus Hall 2 - Pokey Gauntlet Reward",
      "Sarcophagus Hall 2 - Behind Hammer Block",
      "Super Hammer Room - In Big Chest",
      "Super Hammer Room - Hidden Chest",
      "Pyramid Stone Room - On Pedestal",
      "Lunar Stone Room - On Pedestal",
      "Diamond Stone Room - On Pedestal"
    ],
    "dungeon": True
  },
  {
    "category": "Tubba's Castle",
    "item_set": [
      "Table/Clock Room (1/2F) - On Table",
      "Basement - In Chest",
      "Study (1F) - On Table",
      "Covered Tables Room (1F) - On Table",
      "Spike Trap Room (2F) - In Chest",
      "Hidden Bedroom (2F) - In Hidden Room",
      "Hidden Bedroom (2F) - On Bed 1",
      "Hidden Bedroom (2F) - On Bed 2",
      "Hidden Bedroom (2F) - On Bed 3",
      "Hidden Bedroom (2F) - On Bed 4",
      "Hidden Bedroom (2F) - On Bed 5",
      "Hidden Bedroom (2F) - On Bed 6",
      "Stairs to Third Floor - Yellow Block",
      "Sleeping Clubbas Room (3F) - On Pedestal",
    ],
    "dungeon": True
  },
  {
    "category": "Blue Station",
    "item_set": [
      "BLU Large Playroom - Hidden Block 1",
      "BLU Large Playroom - Hidden Block 2",
      "BLU Large Playroom - Calculator Thief 1",
      "BLU Large Playroom - Calculator Thief 2",
      "BLU Large Playroom - Shy Guy 2",
      "BLU Large Playroom - Shy Guy 3",
      "BLU Large Playroom - Shy Guy 4",
      "BLU Large Playroom - Shy Guy 5",
      "BLU Station - Hidden Panel",
      "BLU Station - Hidden Block",
      "BLU Block City - In Chest",
      "BLU Block City - Infront Of Chest",
      "BLU Block City - Midair 1",
      "BLU Block City - Midair 2",
      "BLU Block City - Midair 3",
      "BLU Block City - Midair 4",
      "BLU Block City - Midair 5",
      "BLU Block City - Midair 6",
      "BLU Block City - Midair 7",
      "BLU Block City - Midair 8",
      "BLU Block City - On Building",
      "BLU Block City - Behind Building Block",
      "BLU Block City - Yellow Block 1",
      "BLU Block City - Yellow Block 2",
      "BLU Block City - Yellow Block On Ledge",
      "BLU Anti-Guy Hall - In Chest",
      "BLU Anti-Guy Hall - Hidden Block",
      "BLU Anti-Guy Hall - Yellow Block",
    ],
    "dungeon": False
  },
  {
    "category": "Pink Station",
    "item_set": [
      "PNK Gourmet Guy Crossing - Hidden Block Right",
      "PNK Gourmet Guy Crossing - Hidden Block Left",
      "PNK Gourmet Guy Crossing - Gourmet Guy Reward",
      "PNK Gourmet Guy Crossing - Yellow Block 1",
      "PNK Gourmet Guy Crossing - Yellow Block 2",
      "PNK Station - In Chest",
      "PNK Station - Hidden Panel",
      "PNK Station - Hidden Block",
      "PNK Playhouse - In Chest (Far Right)",
      "PNK Playhouse - In Chest (Top Left)",
      "PNK Playhouse - In Chest (Right)",
      "PNK Playhouse - Infront Of Chest (Right)",
      "PNK Playhouse - Yellow Block",
      "PNK Tracks Hallway - Yellow Block South",
      "PNK Tracks Hallway - Yellow Block North 1",
      "PNK Tracks Hallway - Yellow Block North 2",
    ],
    "dungeon": False
  },
  {
    "category": "Green Station",
    "item_set": [
      "GRN Station - Hidden Panel",
      "GRN Station - Hidden Block",
      "GRN Treadmills/Slot Machine - In Chest",
      "GRN Treadmills/Slot Machine - Infront Of Chest",
      "GRN Treadmills/Slot Machine - On Treadmill 1",
      "GRN Treadmills/Slot Machine - On Treadmill 2",
      "GRN Treadmills/Slot Machine - On Treadmill 3",
      "GRN Treadmills/Slot Machine - On Treadmill 4",
      "GRN Treadmills/Slot Machine - On Treadmill 5",
      "GRN Treadmills/Slot Machine - On Treadmill 6",
      "GRN Treadmills/Slot Machine - Hidden Room Center",
      "GRN Treadmills/Slot Machine - Hidden Room 1",
      "GRN Treadmills/Slot Machine - Hidden Room 2",
      "GRN Treadmills/Slot Machine - Hidden Room 3",
      "GRN Treadmills/Slot Machine - Hidden Room 4",
      "GRN Treadmills/Slot Machine - Hidden Room 5",
      "GRN Treadmills/Slot Machine - Hidden Room 6",
      "GRN Treadmills/Slot Machine - Defeat Shy Guy",
    ],
    "dungeon": False
  },
  {
    "category": "Red Station",
    "item_set": [
      "RED Boss Barricade - Hidden Block Left",
      "RED Boss Barricade - On Brick Block",
      "RED Boss Barricade - Yellow Block Right",
      "RED Station - Hidden Panel",
      "RED Station - Hidden Block",
      "RED Moving Platforms - Hidden Block Center",
      "RED Moving Platforms - Hidden Block Right",
      "RED Moving Platforms - Hidden Block Left",
      "RED Moving Platforms - Yellow Block 1",
      "RED Moving Platforms - Yellow Block 2",
      "RED Lantern Ghost - Watt Partner",
    ],
    "dungeon": False
  },
  {
    "category": "Mt. Lavalava",
    "item_set": [
      "Central Cavern - On Stone Pillar",
      "Central Cavern - On Brick Block",
      "Central Cavern - Yellow Block 1",
      "Central Cavern - Yellow Block 2",
      "Central Cavern - Yellow Block 3",
      "Central Cavern - Yellow Block 4",
      "Flowing Lava Puzzle - Hidden Block",
      "Ultra Hammer Room - In Big Chest",
      "Dizzy Stomp Room - In Chest",
      "Zipline Cavern - Hidden Panel",
      "Boss Antechamber - Hidden Panel",
      "Boss Room - Yellow Block Left",
      "Boss Room - Yellow Block Right",
    ],
    "dungeon": True
  },
  {
    "category": "Crystal Palace",
    "item_set": [
      "Reflected Save Room - Yellow Block",
      "Blue Key Room - In Chest",
      "Shooting Star Room - On The Ground",
      "Red Key Room - In Chest",
      "P-Down, D-Up Room - In Chest",
      "Star Piece Cave - On The Ground",
      "Huge Statue Room - Hidden Panel",
      "Huge Statue Room - Yellow Block",
      "Small Statue Room - Hidden Panel",
      "Small Statue Room - Hidden Block",
      "Palace Key Room - In Chest",
      "P-Up, D-Down Room - In Chest",
      "Triple Dip Room - In Chest",
    ],
    "dungeon": True
  },
  {
    "category": "Goomba Village",
    "item_set": [
      "Goomba Village - Bush Bottom Right",
      "Goomba Village - Goompa Gift",
      "Goomba Village - On The Balcony",
      "Goomba Village - Goombario Partner",
      "Goomba Village - Goomnut Tree",
      "Goomba Village - Goombaria Dolly Reward",
      "Goomba Village - Goompapa Letter Reward 1",
      "Goomba Village - Goompapa Letter Reward 2",
      "Goomba Village - Goompa Letter Reward",
      "Goomba Village - Goompa Koopa Koot Favor"
    ],
    "dungeon": False
  },
  {
    "category": "Goomba Playground", # includes the two screens between village and playground
    "item_set": [
      "Bottom of the Cliff - Floating Coin 1",
      "Bottom of the Cliff - Floating Coin 2",
      "Bottom of the Cliff - Floating Coin 3",
      "Bottom of the Cliff - Floating Coin 4",
      "Bottom of the Cliff - Upper Ledge",
      "Bottom of the Cliff - In Tree",
      "Bottom of the Cliff - Block On Ground",
      "Jr. Troopas Playground - Bush Right",
      "Jr. Troopas Playground - Bush Bottom Right",
      "Jr. Troopas Playground - Bush Top 1",
      "Jr. Troopas Playground - Bush Top 2",
      "Jr. Troopas Playground - Bush Center",
      "Jr. Troopas Playground - Bush Top Left",
      "Jr. Troopas Playground - In Hammer Bush",
      "Jr. Troopas Playground - In Tree Left",
      "Jr. Troopas Playground - In Tree Top",
      "Jr. Troopas Playground - In Tree Right",
      "Behind the Village - On Ledge",
      "Behind the Village - In Tree",
    ],
    "dungeon": False
  },
  {
    "category": "Goomba Road", # includes Goomba King's Castle room and room before Toad Town
    "item_set": [
      "Goomba Road 2 - On the Sign",
      "Goomba Road 2 - Red Block",
      "Goomba Road 1 - Yellow Block Left",
      "Goomba Road 1 - Yellow Block Right",
      "Toad Town Entrance - Chest On Roof",
      "Toad Town Entrance - Yellow Block",
      "Goomba Kings Castle - In Tree Left Of Fortress",
      "Goomba Kings Castle - In Tree Right Of Cliff",
      "Goomba Kings Castle - Hidden Yellow Block",
    ],
    "dungeon": False
  },
  {
    "category": "Toad Town",
    "item_set": [
      "Gate District - Dojo: Chan",
      "Gate District - Dojo: Lee",
      "Gate District - Dojo: Master 1",
      "Gate District - Dojo: Master 2",
      "Gate District - Dojo: Master 3",
      "Gate District - Miss T. Letter Reward",
      "Gate District - Shop Item 1",
      "Gate District - Shop Item 2",
      "Gate District - Shop Item 3",
      "Gate District - Shop Item 4",
      "Gate District - Shop Item 5",
      "Gate District - Shop Item 6",
      "Plaza District - Rowfs Shop Set 1 - 1",
      "Plaza District - Rowfs Shop Set 1 - 2",
      "Plaza District - Rowfs Shop Set 1 - 3",
      "Plaza District - Rowfs Shop Set 1 - 4",
      "Plaza District - Rowfs Shop Set 2 - 1",
      "Plaza District - Rowfs Shop Set 2 - 2",
      "Plaza District - Rowfs Shop Set 2 - 3",
      "Plaza District - Rowfs Shop Set 3 - 1",
      "Plaza District - Rowfs Shop Set 3 - 2",
      "Plaza District - Rowfs Shop Set 3 - 3",
      "Plaza District - Rowfs Shop Set 4 - 1",
      "Plaza District - Rowfs Shop Set 4 - 2",
      "Plaza District - Rowfs Shop Set 4 - 3",
      "Plaza District - Rowfs Shop Set 5 - 1",
      "Plaza District - Rowfs Shop Set 5 - 2",
      "Plaza District - Rowfs Shop Set 5 - 3",
      "Plaza District - In Tree",
      "Southern District - Bub-ulb Gift",
      "Residental District - Shop Item 1",
      "Residental District - Shop Item 2",
      "Residental District - Shop Item 3",
      "Residental District - Shop Item 4",
      "Residental District - Shop Item 5",
      "Residental District - Shop Item 6",
      "Port District - Poet Gift",
      "Gate District - Hidden Panel",
      "Plaza District - Postmaster MailBag Reward",
      "Plaza District - Merlon House Stomp x3",
      "Southern District - Hidden Panel",
      "Southern District - Inside Blue House",
      "Station District - Hidden Panel",
      "Port District - Hidden Panel",
      "Gate District - Russ T. Letter Reward",
      "Plaza District - Merlon Letter Reward",
      "Plaza District - Minh T. Letter Reward",
      "Southern District - Tayce T. Frying Pan Reward",
      "Gate District - Russ T. Dictionary Reward",
      "Port District - Fishmael Letter Reward",
      "Gate District - Sushie Island",
      "Port District - Poet Melody Reward",
      "Southern District - Fice T. Letter Reward",
      "Residental District - Storeroom Item 1",
      "Residental District - Storeroom Item 2",
      "Residental District - Storeroom Item 3",
      "Residental District - Storeroom Item 4",
      "Station District - Dane T. Letter Reward 1",
      "Gate District - Radio Trade Event 1 Reward",
      "Plaza District - Rowf Calculator Reward",
      "Port District - Radio Trade Event 3 Reward",
      "Station District - Dane T. Letter Reward 2",
      "Southern District - Fice T. Forest Pass",
    ],
    "dungeon": False
  },
  {
    "category": "Toad Town Tunnels",
    "item_set": [
      "Blooper Boss 1 (B1) - Blooper Fight Reward",
      "Hall to Blooper 1 (B1) - Hidden Block",
      "Blue Pushblock Room (B2) - Hidden Block Left",
      "Blue Pushblock Room (B2) - Hidden Block Center",
      "Blue Pushblock Room (B2) - Hidden Block Right",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 1",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 2",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 3",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 4",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 5",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 6",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 7",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 8",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 9",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 10",
      "Rip Cheatos Home (B3) - Rip Cheato Offer 11",
      "Bridge to Shiver City (B2) - Yellow Block 1",
      "Winding Path (Spiny Room) - Hidden Block Center",
      "Winding Path (Spiny Room) - Hidden Block Right",
      "Winding Path (Spiny Room) - Hidden Block Left",
      "Winding Path (Spiny Room) - Yellow Block",
      "Short Elevator Room (B1) - Yellow Block Center",
      "Short Elevator Room (B1) - Yellow Block Left",
      "Short Elevator Room (B1) - Yellow Block Right",
      "Spring Room (B2) - Chest On Ledge",
      "Elevator Attic Room (B2) - On Parakarry Ledge",
      "Room with Spikes (B2) - Yellow Block",
      "Bridge to Shiver City (B2) - Yellow Block 2",
      "Bridge to Shiver City (B2) - Yellow Block 3",
      "Bridge to Shiver City (B2) - Yellow Block 4",
      "Bridge to Shiver City (B2) - Yellow Block 5",
      "Hall to Ultra Boots (B3) - Hidden Block",
      "Hall to Ultra Boots (B3) - Yellow Block Left",
      "Hall to Ultra Boots (B3) - Yellow Block Right",
      "Ultra Boots Room (B3) - In Big Chest",
    ],
    "dungeon": False
  },
  {
    "category": "Pleasant Path",
    "item_set": [
      "Pleasant Path Entry - Red Block Center",
      "Pleasant Path Entry - Yellow Block Left",
      "Pleasant Path Entry - Yellow Block Right",
      "Pleasant Path Bridge - Behind Fence",
      "Pleasant Path Bridge - Yellow Block",
      "Pleasant Crossroads - Behind Peg",
      "Pleasant Crossroads - Brick Block Puzzle",
      "Path to Fortress 1 - X On Ground 1",
      "Path to Fortress 1 - X On Ground 2",
      "Path to Fortress 1 - X On Ground 3",
      "Path to Fortress 1 - X On Ground 4",
      "Path to Fortress 1 - X On Ground 5",
      "Fortress Exterior - Chest On Ledge",
      "Pleasant Path Bridge - Kooper Island",
      "Path to Fortress 1 - Hidden Block",
      "Path to Fortress 2 - In Tree",
      "Path to Fortress 1 - On Brick Block",
      "Pleasant Crossroads - Hidden Panel",
      "Path to Fortress 1 - Hidden Panel",
    ],
    "dungeon": False
  },
  {
    "category": "Koopa Village",
    "item_set": [
      "Koopa Village 1 - Bush Far Left",
      "Koopa Village 1 - Bush Left Front",
      "Koopa Village 1 - Bush Infront Of Tree",
      "Koopa Village 1 - Bush Second From Right",
      "Koopa Village 1 - Shop Item 1",
      "Koopa Village 1 - Shop Item 2",
      "Koopa Village 1 - Shop Item 3",
      "Koopa Village 1 - Shop Item 4",
      "Koopa Village 1 - Shop Item 5",
      "Koopa Village 1 - Shop Item 6",
      "Koopa Village 2 - Bush Far Left",
      "Koopa Village 2 - Bush Far Right",
      "Koopa Village 2 - Kolorados Wife (Koopa Koot Favor)",
      "Koopa Village 2 - Push Block Puzzle",
      "Fuzzy Forest - Fuzzy Battle Reward",
      "Koopa Village 1 - Mort T. Letter Reward",
      "Koopa Village 2 - Kolorado Letter Reward",
      "Behind Koopa Village - On Stump",
      "Koopa Village 1 - Koover Letter Reward 1",
      "Koopa Village 2 - Kolorado Artifact Reward",
      "Koopa Village 1 - Hidden Panel",
      "Koopa Village 2 - Favor 1 Reward (KoopaLegends)",
      "Koopa Village 2 - Favor 2 Reward 2 (SleepySheep)",
      "Koopa Village 2 - Favor 2 Reward 1 (SleepySheep)",
      "Koopa Village 1 - Koover Letter Reward 2",
      "Koopa Village 2 - Kooper Partner",
      "Koopa Village 2 - Favor 3 Reward (Tape)",
      "Koopa Village 2 - Favor 4 Reward (KoopaTea)",
      "Koopa Village 1 - Bush Far Right (Koopa Koot Favor)",
      "Koopa Village 2 - Favor 5 Reward (LuigiAutograph)",
      "Koopa Village 2 - Favor 6 Reward (Wallet)",
      "Koopa Village 2 - Favor 7 Reward (TastyTonic)",
      "Koopa Village 2 - Favor 10 Reward 2 (LifeShroom)",
      "Koopa Village 2 - Favor 8 Reward (MerluvleeAutograph)",
      "Koopa Village 2 - Favor 9 Reward (News)",
      "Koopa Village 2 - Favor 10 Reward 1 (LifeShroom)",
      "Koopa Village 2 - Favor 11 Reward (NuttyCake)",
      "Koopa Village 2 - Favor 12 Reward (Bob-ombs)",
      "Koopa Village 1 - Bush Second From Left (Koopa Koot Favor)",
      "Koopa Village 2 - Favor 13 Reward (OldPhoto)",
      "Koopa Village 2 - Favor 14 Reward (Koopasta)",
      "Koopa Village 2 - Favor 15 Reward (Glasses)",
      "Koopa Village 2 - Favor 16 Reward (Lime)",
      "Koopa Village 2 - Favor 17 Reward (KookyCookie)",
      "Koopa Village 2 - Favor 18 Reward (Package)",
      "Koopa Village 2 - Favor 19 Reward (Coconut)",
      "Koopa Village 2 - Favor 20 Reward (RedJar)",
    ],
    "dungeon": False
  },
  {
    "category": "Mt. Rugged",
    "item_set": [
      "Mt Rugged 1 - On Slide 1",
      "Mt Rugged 1 - On Slide 2",
      "Mt Rugged 1 - On Slide 3",
      "Mt Rugged 1 - Yellow Block",
      "Mt Rugged 3 - On Scaffolding",
      "Mt Rugged 4 - Hidden Cave Chest",
      "Mt Rugged 4 - Slide Ledge",
      "Mt Rugged 4 - Bottom Left 1",
      "Mt Rugged 4 - Bottom Left 2",
      "Mt Rugged 4 - Yellow Block Top Left",
      "Mt Rugged 4 - Yellow Block Floating",
      "Mt Rugged 4 - Yellow Block Top Right",
      "Suspension Bridge - Bottom Of Cliff",
      "Train Station - Bush 1",
      "Train Station - Bush 2",
      "Train Station - Bush 3",
      "Train Station - Bush Top",
      "Mt Rugged 2 - Hidden Panel",
      "Mt Rugged 2 - Parakarry Ledge",
      "Mt Rugged 2 - Kooper Ledge",
      "Mt Rugged 3 - Bub-ulb Gift",
      "Mt Rugged 4 - Left Ledge Center",
      "Mt Rugged 4 - Left Ledge Right",
      "Mt Rugged 4 - Left Ledge 3",
      "Mt Rugged 4 - Left Ledge 4",
      "Mt Rugged 4 - Left Ledge 5",
      "Mt Rugged 4 - Left Ledge 6",
      "Mt Rugged 4 - Left Ledge 7",
      "Train Station - Parakarry Partner",
      "Mt Rugged 1 - Hurting Whacka",
    ],
    "dungeon": False
  },
  {
    "category": "Dry Dry Desert",
    "item_set": [
      "N3W3 - Yellow Block Left",
      "N3W3 - Yellow Block Right",
      "N3E2 Pokey Army - Behind Cactus",
      "N3E3 - In Tree",
      "N2W3 - Hidden Block",
      "N2E1 (Tweester A) - Yellow Block Left",
      "N2E1 (Tweester A) - Yellow Block Right",
      "N1W3 Special Block - Hit Block x1",
      "N1W3 Special Block - Hit Block x5",
      "N1W3 Special Block - Hit Block x10",
      "N1W1 - Yellow Block 1",
      "N1W1 - Yellow Block 2",
      "N1W1 - Yellow Block 3",
      "N1W1 - Yellow Block 4",
      "N1W1 - Yellow Block Center",
      "N1E1 Palm Trio - Hidden Block",
      "N1E3 - In Tree",
      "Center (Tweester C) - Hidden Panel",
      "E1 Nomadimouse - In Tree",
      "E2 - In Tree Far Left",
      "E3 Outside Outpost - In Tree (Far Left)",
      "E3 Outside Outpost - In Tree (Second From Left)",
      "E3 Outside Outpost - In Tree (Fourth From Right)",
      "E3 Outside Outpost - In Tree (Far Right)",
      "S1 - Yellow Block",
      "S1E2 Small Bluffs - Ontop Of Bluffs",
      "S1E3 North of Oasis - Hidden Block",
      "S1E3 North of Oasis - Tree Bottom Left",
      "S1E3 North of Oasis - Yellow Block",
      "S2E2 West of Oasis - Behind Bush",
      "S2E2 West of Oasis - In Tree",
      "S2E3 Oasis - In Fruit Tree (Left)",
      "S2E3 Oasis - In Fruit Tree (Right)",
      "S2E3 Oasis - In Tree (Far Left)",
      "S2E3 Oasis - In Tree (Front Right)",
      "S3W2 Hidden AttackFX - Hidden Block",
      "S3E1 - Yellow Block",
      "S3E3 South of Oasis - In Tree (Far Right)",
      "E1 Nomadimouse - Nomadimouse Letter Reward",
    ],
    "dungeon": False
  },
  {
    "category": "Dry Dry Outpost",
    "item_set": [
      "Outpost 1 - Shop Item 1",
      "Outpost 1 - Shop Item 2",
      "Outpost 1 - Shop Item 3",
      "Outpost 1 - Shop Item 4",
      "Outpost 1 - Shop Item 5",
      "Outpost 1 - Shop Item 6",
      "Outpost 1 - In Red Tree",
      "Outpost 2 - Moustafa Gift",
      "Outpost 2 - Hidden Panel",
      "Outpost 2 - Toad House Roof",
      "Outpost 2 - Mr. E. Letter Reward",
      "Outpost 1 - Little Mouser Letter Reward",
      "Outpost 1 - Composer Lyrics Reward",
      "Outpost 2 - Merlee Request (Koopa Koot Favor)",
      "Outpost 1 - Store Legend (RedJar Code)",
    ],
    "dungeon": False
  },
  {
    "category": "Forever Forest", # includes 2 checks outside boo's mansion
    "item_set": [
      "Tree Face (Bub-ulb) - Bub-ulb Gift",
      "Bee Hive (HP Plus) - Central Block",
      "Flowers Appear (FP Plus) - Central Block",
      "Outside Boos Mansion - In Bush (Back Right)",
      "Outside Boos Mansion - Yellow Block",
    ],
    "dungeon": False
  },
  {
    "category": "Boo's Mansion",
    "item_set": [
      "Record Room - Boo Ring Game",
      "Foyer - Hidden Panel",
      "Basement Stairs - Hidden Panel",
      "Basement - In Crate",
      "Super Boots Room - In Big Chest",
      "Super Boots Room - In Crate",
      "Super Boots Room - Hidden Panel",
      "Pot Room - In Crate 1",
      "Pot Room - In Crate 2",
      "Library - In Crate",
      "Record Room - Hidden Panel",
      "Library - On Bookshelf",
      "Basement - Shop Item 1",
      "Basement - Shop Item 2",
      "Basement - Shop Item 3",
      "Basement - Shop Item 4",
      "Basement - Shop Item 5",
      "Basement - Shop Item 6",
      "Record Player Room - In Chest",
      "Lady Bows Room - Bow Partner",
      "Foyer - Franky Letter Reward",
      "Basement - Igor Letter Reward",
      "Foyer - From Franky (Koopa Koot Favor)",
    ],
    "dungeon": False
  },
  {
    "category": "Gusty Gulch", # includes the hidden panel past the gate
    "item_set": [
      "Exit to Gusty Gulch - Hidden Panel",
      "Wasteland Ascent 1 - Infront Of Branch",
      "Wasteland Ascent 1 - Yellow Block 1",
      "Wasteland Ascent 1 - Yellow Block 2",
      "Wasteland Ascent 1 - Yellow Block Right",
      "Wasteland Ascent 1 - On Rock",
      "Ghost Town 1 - Yellow Block In House",
      "Wasteland Ascent 2 - Behind Rock",
      "Wasteland Ascent 2 - Yellow Block Left",
      "Wasteland Ascent 2 - Yellow Block Right",
      "Ghost Town 1 - From Boo (Koopa Koot Favor)",
    ],
    "dungeon": False
  },
  {
    "category": "Jade Jungle", # includes beach
    "item_set": [
      "Whale Cove - Over Flower 1",
      "Whale Cove - Over Flower 2",
      "Whale Cove - Behind Bush",
      "Whale Cove - In Palm Tree",
      "Beach - Hidden Block Left",
      "Beach - Hidden Block Right",
      "Beach - On The Rocks",
      "Beach - Over Flower 1",
      "Beach - Over Flower 2",
      "Beach - In Palm Tree 1",
      "Beach - In Palm Tree 2",
      "Beach - In Palm Tree 3",
      "Beach - In Palm Tree 4",
      "Beach - In Palm Tree 5",
      "Beach - In Palm Tree 6",
      "Beach - In Palm Tree 6 2",
      "Sushi Tree - Sushie Partner",
      "SE Jungle (Quake Hammer) - Bush (Bottom Right)",
      "SE Jungle (Quake Hammer) - In Tree (Right)",
      "SW Jungle (Super Block) - Bush (Bottom Left)",
      "Path to the Volcano - Behind Tree",
      "Sushi Tree - On Island",
      "Sushi Tree - In Island Tree",
      "SE Jungle (Quake Hammer) - Bush (Bottom Left)",
      "SE Jungle (Quake Hammer) - Red Block",
      "NE Jungle (Raven Statue) - Underwater",
      "NE Jungle (Raven Statue) - In Tree (Top Left)",
      "Small Jungle Ledge - In Tree",
      "SW Jungle (Super Block) - Bush (Top Right)",
      "SW Jungle (Super Block) - Hidden Block",
      "SW Jungle (Super Block) - Underwater 1",
      "SW Jungle (Super Block) - Underwater 2",
      "SW Jungle (Super Block) - Underwater 3",
      "SW Jungle (Super Block) - In Tree (Top)",
      "SW Jungle (Super Block) - In Tree (Right)",
      "NW Jungle (Large Ledge) - Bush 1",
      "NW Jungle (Large Ledge) - Bush 2",
      "NW Jungle (Large Ledge) - In Tree On Ledge",
      "NW Jungle (Large Ledge) - In Tree Right",
      "Western Dead End - Underwater",
      "Sushi Tree - In Volcano Chest",
      "Deep Jungle 1 - Hidden Block",
      "Deep Jungle 1 - In Tree (Vine)",
      "Deep Jungle 1 - In Tree (Hit)",
      "Deep Jungle 2 (Block Puzzle) - Hidden Block",
      "Deep Jungle 2 (Block Puzzle) - In Tree (Left)",
      "Deep Jungle 3 - Tree Vine Second Left",
      "Deep Jungle 3 - Tree Vine Far Right",
      "Deep Jungle 4 (Ambush) - Hidden Panel",
      "Deep Jungle 4 (Ambush) - In Tree (Right)",
      "Great Tree Vine Ascent - End Of Vine",
      "Path to the Volcano - Raphael Gift",
    ],
    "dungeon": False
  },
  {
    "category": "Yoshi Village",
    "item_set": [
      "Village Cove - Hidden Panel",
      "Village Cove - In Palm Tree Left",
      "Village Cove - In Palm Tree Right",
      "Village Buildings - Shop Item 1",
      "Village Buildings - Shop Item 2",
      "Village Buildings - Shop Item 3",
      "Village Buildings - Shop Item 4",
      "Village Buildings - Shop Item 5",
      "Village Buildings - Shop Item 6",
      "Village Buildings - In Palm Tree",
      "Village Cove - Village Leader Reward",
      "Village Buildings - Kolorado Volcano Vase Reward",
      "Village Buildings - Yellow Yoshi Food Reward",
      "Village Buildings - Red Yoshi Kid Letter Reward"
    ],
    "dungeon": False
  },
  {
    "category": "Shiver City",
    "item_set": [
      "Shiver City Mayor Area - Chest In House",
      "Shiver City Center - Sleep At Toad House",
      "Shiver City Pond Area - In Frozen Pond",
      "Shiver City Mayor Area - Mayor Penguin Gift",
      "Shiver City Mayor Area - Hidden Panel",
      "Shiver City Center - Shop Item 1",
      "Shiver City Center - Shop Item 2",
      "Shiver City Center - Shop Item 3",
      "Shiver City Center - Shop Item 4",
      "Shiver City Center - Shop Item 5",
      "Shiver City Center - Shop Item 6",
      "Shiver City Center - Snowmen Gift 1",
      "Shiver City Center - Snowmen Gift 2",
      "Shiver City Center - Snowmen Gift 3",
      "Shiver City Center - Snowmen Gift 4",
      "Shiver City Center - Snowmen Gift 5",
      "Shiver City Mayor Area - Mayor Penguin Letter Reward"
    ],
    "dungeon": False
  },
  {
    "category": "Shiver Mountain",
    "item_set": [
      "Shiver Mountain Passage - Hidden Block",
      "Shiver Mountain Hills - Bottom Path",
      "Shiver Mountain Tunnel - Socket 1",
      "Shiver Mountain Tunnel - Socket 2",
      "Shiver Mountain Tunnel - Socket 3",
      "Shiver Mountain Peaks - Left Ledge",
      "Shiver Mountain Peaks - Red Block",
      "Merlars Sanctuary - On Pedestal",
    ],
    "dungeon": False
  },
  {
    "category": "Shiver Snowfield", # includes Starborn Valley
    "item_set": [
      "Shiver Snowfield - Hidden Panel",
      "Shiver Snowfield - Behind Tree Right",
      "Shiver Snowfield - In Tree Left",
      "Path to Starborn Valley - Hidden Block",
      "Path to Starborn Valley - Behind Icicle",
      "Starborn Valley - Merle Gift",
      "Starborn Valley - Frost T. Letter Reward"
    ],
    "dungeon": False
  },
]
barren_region_hint_count = 3

# incredibly naive recursive search through item sphere's by location name
# there's 100% a better way, but this was easy for a prototype
def search_for_location(item_spheres:dict, location:str) -> str:
  if isinstance(item_spheres, dict):
    if location in item_spheres:
      return item_spheres[location]
    for child in item_spheres:
      result = search_for_location(item_spheres[child], location)
      if result != "[Nothing Found]":
        return result
  return "[Nothing Found]"

# check if given key item is useful for logic settings
# 1) additional work would need to be done for glitch logic
# 2) checking the reward for certain item turn ins should be done here as well to determine
#    if, ex, Koopers Shell is a "required" item
def item_is_useful(item:str, logic_settings) -> bool:
  if item == "Goombario*":
    return False
  if "Letter" in item and getattr(logic_settings, "include_letters_mode") == 0:
    return False
  return '*' in item

def generate_hints(item_spheres:dict, logic_settings):
  global sometimes_hint_count

  # useful barren hint generation data
  letter_turnin = search_for_location(item_spheres, "Train Station - Parakarry Partner")
  letters_useful = getattr(logic_settings, "include_letters_mode") > 0 or item_is_useful(letter_turnin, logic_settings)

  # search for barren categories and choose one at random
  barren_category_hint = "  Could not generate\n"
  last_priority = -1
  valid_barren_categories = []
  for i,cat in enumerate(barren_categories):
    # exit early if barren categories of higher priority have been found already
    if last_priority > 0 and cat["priority"] > last_priority:
      break
    if 'req' in cat:
      if getattr(logic_settings, cat['req']) != cat['req_val']:
        continue
    valid = True
    for loc in cat["item_set"]:
      item = search_for_location(item_spheres, loc)

      # if key item that is not goombario, cannot mark barren
      if item_is_useful(item, logic_settings):
        valid = False
        break
    if valid:
      last_priority = cat["priority"]
      valid_barren_categories.append(i)
  if len(valid_barren_categories) > 0:
    barren_category_hint = f"  {barren_categories[random.choice(valid_barren_categories)]['category']} yields no progression\n"
  else:
    sometimes_hint_count += 1 # give an extra sometimes hint if no barren category could be generated

  # search for barren regions (would be astounding to not find 3)
  barren_region_hint = ""
  valid_barren_dungeons = []
  valid_barren_regions = []
  for i,region in enumerate(barren_regions):
    valid = True
    for loc in region["item_set"]:
      item = search_for_location(item_spheres, loc)
      if item_is_useful(item, logic_settings):
        valid = False
        break
    if valid:
      if region["dungeon"]:
        valid_barren_dungeons.append(i)
      else:
        valid_barren_regions.append(i)

  random.shuffle(valid_barren_categories)
  if len(valid_barren_dungeons) > 0:
    random.shuffle(valid_barren_dungeons)
    valid_barren_categories.insert(0, valid_barren_dungeons[0])

  if len(valid_barren_regions) > 0:
    for i,barren_region in enumerate(valid_barren_regions):
      if i >= barren_region_hint_count:
        break
      barren_region_hint += f"  {barren_regions[barren_region]['category']}\n"
  else:
    barren_region_hint = "  Could not generate"
  barren_region_empty_hints = barren_region_hint_count - len(valid_barren_regions)
  sometimes_hint_count += barren_region_empty_hints # add any unfilled barren region hints with more sometimes hints

  # display what items are available in the always hints
  always_hints = ""
  for hint in always_hint_to_check_mapping:
    if 'req' in hint:
      if getattr(logic_settings, hint['req']) != hint['req_val']:
        continue
    always_hints += f"  {hint['name']} is {search_for_location(item_spheres, hint['check'])}\n"

  # pick a subset of sometimes hints at random to output
  sometimes_hints = ""
  sometimes_keys = list(sometimes_hint_to_check_mapping.keys())
  random.shuffle(sometimes_keys)
  for i,k in enumerate(sometimes_keys):
    if i >= sometimes_hint_count:
      break
    sometimes_hints += f"  {k} is {search_for_location(item_spheres, sometimes_hint_to_check_mapping[k])}\n"

  # output the hints data file
  with open("./res/hints.txt", "w", encoding="utf-8") as file:
    file.write("Hints:\n")
    file.write("===================================\n")
    file.write(f"Barren Regions:\n")
    file.write(barren_region_hint)
    file.write("===================================\n")
    file.write("Barren Category:\n")
    file.write(barren_category_hint)
    file.write("===================================\n")
    file.write("Always Hints:\n")
    file.write(always_hints)
    file.write("===================================\n")
    file.write(f"Sometimes Hints ({sometimes_hint_count}):\n")
    file.write(sometimes_hints)
    file.write("===================================\n")
    file.write(json.dumps(item_spheres, indent=2))
