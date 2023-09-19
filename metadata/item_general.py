taycet_items = [
    0x0B0, # "SpicySoup",
    0x0B1, # "ApplePie",
    0x0B2, # "HoneyUltra",
    0x0B3, # "MapleUltra",
    0x0B4, # "JellyUltra",
    #0x0B5, # "Koopasta",
    0x0B6, # "FriedShroom",
    0x0B7, # "ShroomCake",
    0x0B8, # "ShroomSteak",
    0x0B9, # "HotShroom",
    0x0BA, # "SweetShroom",
    0x0BB, # "YummyMeal",
    0x0BC, # "HealthyJuice",
    0x0BD, # "BlandMeal",
    0x0BE, # "DeluxeFeast",
    0x0BF, # "SpecialShake",
    0x0C0, # "BigCookie",
    #0x0C1, # "Cake",
    #0x0C2, # "Mistake",
    #0x0C3, # "KoopaTea",
    0x0C4, # "HoneySuper",
    0x0C5, # "MapleSuper",
    0x0C6, # "JellySuper",
    0x0C7, # "Spaghetti",
    0x0C8, # "EggMissile",
    0x0C9, # "FriedEgg",
    0x0CA, # "HoneyShroom",
    0x0CB, # "HoneyCandy",
    0x0CC, # "ElectroPop",
    0x0CD, # "FirePop",
    0x0CE, # "LimeCandy",
    0x0CF, # "CocoPop",
    0x0D1, # "JellyPop",
    0x0D2, # "StrangeCake",
    #0x0D3, # "KookyCookie",
    0x0D4, # "FrozenFries",
    0x0D5, # "PotatoSalad",
    #0x0D6, # "NuttyCake",
    0x0D7, # "MapleShroom",
    0x0D8, # "BoiledEgg",
    0x0D9, # "YoshiCookie",
    0x0DA, # JellyShroom1
]

unused_items = [
    "InsecticideHerb",
    "HustleDrink",
    "SmashCharge0",
    "JumpCharge0",
    "Berserker",
    "RightOn",
    "AutoJump",
    "AutoSmash",
    "CrazyHeart",
    "MegaHPDrain",
    "AutoMultibounce",
    "FlowerFanatic",
    "SuperJump",
    "SuperSmash",
    "SuperFocus",
    "EarthquakeJump",
    "HappyHeartX",
    "FlowerSaverX",
    "DamageDodgeX",
    "PowerPlusX",
    "DefendPlusX",
    "DefendPlusY",
    "HappyFlowerX",
    "AttackFXF",
    "HPPlusX",
    "HPPlusY",
    "FPPlusX",
    "FPPlusY",
    "HealthyHealthy",
    "ShrinkSmash"
]

unused_duplicates = [
    "HappyHeartX",
    "FlowerSaverX",
    "DamageDodgeX",
    "PowerPlusX",
    "DefendPlusX",
    "DefendPlusY",
    "HappyFlowerX",
    "HPPlusX",
    "HPPlusY",
    "FPPlusX",
    "FPPlusY",
]

progressive_badges = [
    "SmashChargeProxy1",
    "SmashChargeProxy2",
    "SmashChargeProxy3",
    "JumpChargeProxy1",
    "JumpChargeProxy2",
    "JumpChargeProxy3",
    "PowerJumpProxy1",
    "PowerJumpProxy2",
    "PowerJumpProxy3",
    "PowerSmashProxy1",
    "PowerSmashProxy2",
    "PowerSmashProxy3",
    "QuakeHammerProxy1",
    "QuakeHammerProxy2",
    "QuakeHammerProxy3"
]

unplaceable_items = [
    "Boots",
    "SuperBoots",
    "UltraBoots",
    "Hammer",
    "SuperHammer",
    "UltraHammer",
    "LuckyStar",
    "HomewardShroom",
    "BigMap",
    "KoopaFortressKey",
    "RuinsKey",
    "TubbaCastleKey",
    "BowserCastleKey",
    "MysticalKey",
    "SuspiciousNote",
    "Screwdriver",
    "ToadDoll",
    "UnusedLetter01",
    "UnusedLetter02",
    "UnusedLetter03",
    "UnusedLetter04",
    "UnusedLetter05",
    "UnusedLetter06",
    "UnusedLetter07",
    "BakingSugar",
    "BakingSalt",
    "BakingEgg",
    "BakingCream",
    "BakingStrawberry",
    "BakingButter",
    "BakingCleanser",
    "BakingWater",
    "BakingFlour",
    "BakingMilk",
    "PeachKey1",
    "SneakyParasol",
    "KootShell",
    "KootAltPhoto",
    "PeachKey2",
    "PrisonKey1",
    "PrisonKey2",
    "PrisonKey3",
    "PrisonKey4",
    "PleaseComeBack",
    "BlueBerry",
    "RedBerry",
    "YellowBerry",
    "BubbleBerry",
    "JellyShroom2",
    "JellyShroom3",
    "JellyShroom4",
    "JellyShroom5",
    "JellyShroom6",
    "MysteryScroll",
    "PowerSmash2",
    "PowerSmash3",
    "ShellCrack",
    "Kaiden",
    "AttackFXF2",
    "AttackFXF3",
    "AttackFXF4",
    "AttackFXF5",
    "PartnerAttack",
    "Heart",
    "HeartPiece",
    "StarPoint",
    "HeartPoint",
    "FlowerPoint",
    "StarPiece",
    "Present",
    "CakeDone",
    "CakeBare",
    "CakePan",
    "CakeBatter",
    "CakeBowl",
    "CakeMixed",
    "CakeWithIcing",
    "CakeWithBerries",
    "Hammer1Icon",
    "Hammer2Icon",
    "Hammer3Icon",
    "Boots1Icon",
    "Boots2Icon",
    "Boots3Icon",
    "ItemsIcon",
    "CakeKey",
    "BlueBerryKey1",
    "BlueBerryKey2",
    "RedBerryKey",
    "YellowBerryKey",
    "BubbleBerryKey",
    "Goompa",
]

# List of 0xFF items for displaying a seed hash on the save select screen.
# The list indices do not correspond to ingame item ids here, this list is
# explicitly coded into the base rom like this instead.
seed_hash_item_names = [
    "Lucky Star",
    "First Degree Card",
    "Second Degree Card",
    "Third Degree Card",
    "Fourth Degree Card",
    "Diploma",
    "Ultra Stone",
    "Koopa Fortress Key",
    "Ruins Key",
    "Pulse Stone",
    "Tubba Castle Key",
    "Crystal Palace Key",
    "Lunar Stone",
    "Pyramid Stone",
    "Diamond Stone",
    "Volcano Vase",
    "Kooper Shell",
    "Bowser Castle Key",
    "Forest Pass",
    "Boo Weight",
    "Boo Portrait",
    "Crystal Berry",
    "Mystical Key",
    "Storeroom Key",
    "Toy Train",
    "Boo Record",
    "Frying Pan",
    "Dictionary",
    "Mystery Note",
    "Suspicious Note",
    "Crystal Ball",
    "Screwdriver",
    "Cookbook",
    "Jade Raven",
    "Magical Seed 1",
    "Magical Seed 2",
    "Magical Seed 3",
    "Magical Seed 4",
    "Toad Doll",
    "Calculator",
    "Snowman Bucket",
    "Snowman Scarf",
    "Red Key",
    "Blue Key",
    "Letter01",
    "Artifact",
    "Dolly",
    "Water Stone",
    "Magical Bean",
    "Fertile Soil",
    "Miracle Water",
    "Baking Sugar",
    "Baking Salt",
    "Baking Egg",
    "Baking Cream",
    "Baking Strawberry",
    "Baking Butter",
    "Baking Cleanser",
    "Baking Water",
    "Baking Flour",
    "Baking Milk",
    "Lyrics",
    "Melody",
    "Mailbag",
    "Peach Key",
    "Star Stone",
    "Sneaky Parasol",
    "Koot Tape",
    "Koot Koopa Legends",
    "Koot Luigi Autograph",
    "Koot Empty Wallet",
    "Koot Merluvlee Autograph",
    "Koot Shell",
    "Koot Old Photo",
    "Koot Glasses",
    "Koot Package",
    "Koot Red Jar",
    "Silver Credit",
    "Gold Credit",
    "Fire Flower",
    "Snowman Doll",
    "Thunder Rage",
    "Shooting Star",
    "Thunder Bolt",
    "Pebble",
    "Dusty Hammer",
    "Insecticide Herb",
    "Stone Cap",
    "Tasty Tonic",
    "Mushroom",
    "Volt Shroom",
    "Super Shroom",
    "Dried Shroom",
    "Ultra Shroom",
    "Sleepy Sheep",
    "POW Block",
    "Hustle Drink",
    "Stop Watch",
    "Whackas Bump",
    "Apple",
    "Life Shroom",
    "Mystery",
    "Repel Gel",
    "Fright Jar",
    "Please Come Back",
    "Dizzy Dial",
    "Super Soda",
    "Lemon",
    "Lime",
    "Blue Berry",
    "Red Berry",
    "Yellow Berry",
    "Bubble Berry",
    "Jammin Jelly",
    "Maple Syrup",
    "Honey Syrup",
    "Goomnut",
    "Koopa Leaf",
    "Dried Pasta",
    "Dried Fruit",
    "Strange Leaf",
    "Cake Mix",
    "Egg",
    "Coconut",
    "Melon",
    "Stinky Herb",
    "Iced Potato",
    "Spicy Soup",
    "Apple Pie",
    "Honey Ultra",
    "Maple Ultra",
    "Jelly Ultra",
    "Koopasta",
    "Fried Shroom",
    "Shroom Cake",
    "Shroom Steak",
    "Hot Shroom",
    "Sweet Shroom",
    "Yummy Meal",
    "Healthy Juice",
    "Bland Meal",
    "Deluxe Feast",
    "Special Shake",
    "Big Cookie",
    "Cake",
    "Mistake",
    "Koopa Tea",
    "Honey Super",
    "Maple Super",
    "Jelly Super",
    "Spaghetti",
    "Egg Missile",
    "Fried Egg",
    "Honey Shroom",
    "Honey Candy",
    "Electro Pop",
    "Fire Pop",
    "Lime Candy",
    "Coco Pop",
    "Lemon Candy",
    "Jelly Pop",
    "Strange Cake",
    "Kooky Cookie",
    "Frozen Fries",
    "Potato Salad",
    "Nutty Cake",
    "Maple Shroom",
    "Boiled Egg",
    "Yoshi Cookie",
    "Jelly Shroom",
    "Spin Smash",
    "Multibounce",
    "Dodge Master",
    "Power Bounce",
    "Spike Shield",
    "First Attack",
    "Quake Hammer",
    "Double Dip",
    "Sleep Stomp",
    "Fire Shield",
    "Quick Change",
    "D Down Pound",
    "Dizzy Stomp",
    "Mini Smash Chg",
    "Pretty Lucky",
    "Feeling Fine",
    "Attack FX A",
    "Allor Nothing",
    "HP Drain",
    "Mini Jump Chg",
    "Slow Go",
    "Mega Rush",
    "Ice Power",
    "Pay Off",
    "Money Money",
    "Chill Out",
    "Zap Tap",
    "Berserker",
    "Right On",
    "Runaway Pay",
    "Refund",
    "Triple Dip",
    "Hammer Throw",
    "Mega Quake",
    "Smash Charge",
    "Jump Charge",
    "S Smash Chg",
    "S Jump Chg",
    "Power Rush",
    "Auto Jump",
    "Auto Smash",
    "Crazy Heart",
    "Last Stand",
    "Close Call",
    "P Up D Down",
    "Lucky Day",
    "Mega HP Drain",
    "P Down D Up",
    "Power Quake",
    "Auto Multibounce",
    "Flower Fanatic",
    "Heart Finder",
    "Flower Finder",
    "Spin Attack",
    "Dizzy Attack",
    "I Spy",
    "Speedy Spin",
    "Bump Attack",
    "Power Jump",
    "Super Jump",
    "Mega Jump",
    "Power Smash",
    "Super Smash",
    "Mega Smash",
    "Shrink Smash",
    "Kaiden",
    "DDown Jump",
    "Shrink Stomp",
    "Earthquake Jump",
    "Deep Focus",
    "HP Plus",
    "FP Plus",
    "Flower Saver",
    "Damage Dodge",
    "Power Plus",
    "Defend Plus",
    "Happy Heart",
    "Happy Flower",
    "Group Focus",
    "Peekaboo",
    "Attack FX D",
    "Attack FX B",
    "Attack FX E",
    "Attack FX C",
    "Attack FX F",
    "Healthy Healthy",
    #"Heart",
    #"Coin",
    #"Star Point",
    #"Heart Point",
    #"Flower Point",
    #"Star Piece",
    #"Cake Done",
    #"Cake Bare",
    #"Cake Pan",
    #"Cake Batter",
    #"Cake Bowl",
    #"Cake Mixed",
    #"Cake With Icing",
    #"Cake With Berries",
    #"Hammer",
    #"Super Hammer",
    #"Ultra Hammer",
    #"Boots",
    #"Super Boots",
    #"Ultra Boots",
]
