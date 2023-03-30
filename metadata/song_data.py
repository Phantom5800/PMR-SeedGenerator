"""unused
This file provides the data and categorization for different songs and
song variations used in the random audio module.
"""
from rando_enums.enum_types import SongType, SongMood

class SongData:
    def __init__(
        self,
        song_name:str,
        song_id:int,
        variation_name:str,
        variation_id:int,
        loops:bool,
        mood:SongMood,
        type:SongType
    ):
        self.song_name=song_name
        self.song_id=song_id
        self.variation_name=variation_name
        self.variation_id=variation_id
        self.loops=loops
        self.mood=mood
        self.type=type

song_data_array = [
    SongData("ToadTown",            0x0,  "with intro",          0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("ToadTown",            0x0,  "without intro",       1, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    # 0x1 unused
    SongData("NormalBattle",        0x2,  "default",             0, True,  SongMood.BATTLE,   SongType.BATTLE),
    SongData("NormalBattle",        0x2,  "player first strike", 1, True,  SongMood.BATTLE,   SongType.BATTLE),
    SongData("NormalBattle",        0x2,  "enemy first strike",  2, True,  SongMood.BATTLE,   SongType.BATTLE),
    SongData("NormalBattle",        0x2,  "just first strike",   3, False, SongMood.BATTLE,   SongType.JINGLE),
    SongData("SpecialBattle",       0x3,  "default",             0, True,  SongMood.BATTLE,   SongType.BATTLE),
    SongData("JrTroopaBattle",      0x4,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("FinalBowserBattle",   0x5,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("FinalBowserBattle",   0x5,  "organ intro only",    1, False, SongMood.BOSS,     SongType.JINGLE),
    # 0x6 unused
    SongData("GoombaKingBattle",    0x7,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("KoopaBrosBattle",     0x8,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("FakeBowserBattle",    0x9,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("TutankoopaBattle",    0xA,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("TubbaBlubbaBattle",   0xB,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("GeneralGuyBattle",    0xC,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("LavaPiranhaBattle",   0xD,  "phase 1",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("LavaPiranhaBattle",   0xD,  "phase 2",             1, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("HuffNPuffBattle",     0xE,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("CrystalKingBattle",   0xF,  "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("GoombaVillage",       0x10, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    #SongData("GoombaVillage",       0x10, "panicky version?",    1, True,  SongMood.CRISIS,   SongType.FIELDANDTOWN),
    SongData("PleasantPath",        0x11, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("FuzzyAttack",         0x12, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("KoopaVillage",        0x13, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("KoopaFortress",       0x14, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("KoopaFortress",       0x14, "with intro",          1, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("DryDryOutpost",       0x15, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("MtRugged",            0x16, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("DryDryDesert",        0x17, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("DryDryRuins",         0x18, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("RuinsBasement",       0x19, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("ForeverForest",       0x1A, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("BoosMansion",         0x1B, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("BoosMansion",         0x1B, "with intro",          1, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("CheerfulBoosMansion", 0x1C, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("GustyGulch",          0x1D, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("TubbasManor",         0x1E, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    #SongData("TubbasManor",         0x1E, "sped up?",            2, False, SongMood.CRISIS,   ),
    SongData("TubbaEscape",         0x1F, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("ShyGuyToybox",        0x20, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("ToyboxTrain",         0x21, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("CreepyToybox",        0x22, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    # 0x23 unused
    SongData("JadeJungle",          0x24, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    #SongData("JadeJungle",          0x24, "sped up?",            1, False,  SongMood.CRISIS , ),
    SongData("DeepJungle",          0x25, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    #SongData("DeepJungle",          0x25, "sped up?",            1, False,  SongMood.CRISIS , ),
    SongData("YoshisVillage",       0x26, "beach",               0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    #SongData("YoshisVillage",       0x26, "village w/o intro",   1, True,  SongMood.?       , ),
    SongData("YoshisVillage",       0x26, "village w/ intro",    2, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("YoshisPanic",         0x27, "default",             0, True,  SongMood.CRISIS,   SongType.FIELDANDTOWN),
    SongData("RaphaelRaven",        0x28, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("RaphaelRaven",        0x28, "default w/ intro",    1, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("MtLavalava",          0x29, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("VolcanoEscape",       0x2A, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("StarWay",             0x2B, "opens",               0, False, SongMood.RELAXED,  SongType.JINGLE),
    SongData("StarWay",             0x2B, "travel up",           1, False, SongMood.RELAXED,  SongType.JINGLE),
    SongData("StarWay",             0x2B, "travel down",         2, False, SongMood.RELAXED,  SongType.JINGLE),
    SongData("StarWay",             0x2B, "default",             3, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("MasterBattle",        0x2C, "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    #SongData("MasterBattle",        0x2C, "sped up?",            1, False,  SongMood.BOSS   , ),
    SongData("RadioIslandSounds",   0x2D, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("RadioHotHits",        0x2E, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("RadioGoldenOldies",   0x2F, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("FlowerFieldsCloudy",  0x30, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("FlowerFieldsSunny",   0x31, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("CloudyClimb",         0x32, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("PuffPuffMachine",     0x33, "default",             0, True,  SongMood.CRISIS,   SongType.FIELDANDTOWN),
    SongData("SunTowerCloudy",      0x34, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("SunTowerSunny",       0x35, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    # 0x36 unused
    SongData("CrystalPalace",       0x37, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    #SongData("CrystalPalace",       0x37, "sped up?",            1, False, SongMood.CRISIS,   ),
    SongData("ShiverCity",          0x38, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("PenguinMystery",      0x39, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    #SongData("PenguinMystery",      0x39, "sped up?",            1, False, SongMood.RELAXED,  ),
    SongData("ShiverSnowfield",     0x3A, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("ShiverMountain",      0x3B, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("StarbornValley",      0x3C, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("MerlarTheme",         0x3D, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    #SongData("MailCall",            0x3E, "default",             0, False, SongMood.RELAXED,  SongType.EVENT),
    SongData("PeachsCastleParty",   0x3F, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    #SongData("PeachsCastleParty",   0x3F, "sped up?",            2, False, SongMood.RELAXED,  ),
    SongData("ChapterEnd",          0x40, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("ChapterStart",        0x41, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("ChapterStart",        0x41, "SMB only",            0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("ItemUpgrade",         0x42, "default",             1, False, SongMood.UPBEAT,   SongType.JINGLE),
    # 0x43 unused
    SongData("PhonographMusic",     0x44, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("TutankoopaTheme",     0x45, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("KammyKoopaTheme",     0x46, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("JrTroopaTheme",       0x47, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("BulletBillAssault",   0x48, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    #SongData("BulletBillAssault",   0x48, "sped up?",            1, False, SongMood.CRISIS,   ),
    SongData("MontyMoleAssault",    0x49, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("ShyGuyInvasion",      0x4A, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("ToadTownTunnels",     0x4B, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("WhaleTheme",          0x4C, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    #SongData("ForeverForestWarning",0x4D, "unused?",             0, True,  SongMood.SINISTER, ),
    SongData("YoshiKidsFound",      0x4E, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("UnusedFanfare",       0x4F, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("GoombaKingTheme",     0x50, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("KoopaBrosInterlude",  0x51, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("KoopaBrosTheme",      0x52, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("KoopaBrosTheme",      0x52, "w/ sinister intro",   1, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("KoopaBrosTheme",      0x52, "BC version",          2, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("KoopaBrosTheme",      0x52, "intro only",          3, False, SongMood.SINISTER, SongType.JINGLE),
    SongData("TutankoopaWarning",   0x53, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("TutankoopaRevealed",  0x54, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("TubbaBlubbaTheme",    0x55, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("GeneralGuyTheme",     0x56, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("LavaPiranhaTheme",    0x57, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("HuffNPuffTheme",      0x58, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("CrystalKingTheme",    0x59, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("BlooperTheme",        0x5A, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("MinibossBattle",      0x5B, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("MonstarTheme",        0x5C, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("Club64",              0x5D, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    #SongData("ClubUnusedOpening64", 0x5E, "default",             0, False, SongMood.?       , ),
    SongData("BowsersCastleFalls",  0x5F, "default",             0, True,  SongMood.CRISIS,   SongType.EVENT),
    SongData("StarHaven",           0x60, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    #SongData("StarHaven",           0x60, "sped up?",            1, False, SongMood.?       , ),
    SongData("ShootingStarSummit",  0x61, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("StarshipTheme",       0x62, "w/ intro",            0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("StarshipTheme",       0x62, "w/o intro",           1, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("StarSanctuary",       0x63, "w/o intro",           0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("StarSanctuary",       0x63, "w/ intro",            1, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("StarSanctuary",       0x63, "intro only",          2, False, SongMood.RELAXED,  SongType.JINGLE),
    SongData("BowsersCastle",       0x64, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("BowsersCastle",       0x64, "upper floor",         1, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("BowsersCastleCaves",  0x65, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("BowserTheme",         0x66, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    #SongData("BowserTheme",         0x66, "sped up?",            2, False, SongMood.CRISIS,   ),
    SongData("BowserBattle",        0x67, "default",             0, True,  SongMood.BOSS,     SongType.BOSS),
    SongData("PeachWishes",         0x68, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("FileSelect",          0x69, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("MainTheme",           0x6A, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("BowserAttacks",       0x6B, "castle rises",        0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("BowserAttacks",       0x6B, "ch8 Peachs Castle",   1, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    #SongData("MarioFalls",          0x6C, "default",             0, False, SongMood.?       , ),
    SongData("PeachAppears",        0x6D, "default",             0, False, SongMood.UPBEAT,   SongType.EVENT),
    SongData("PeachAppears",        0x6D, "castle adress",       1, True,  SongMood.RELAXED,  SongType.EVENT),
    #SongData("PeachAppears",        0x6D, "sped up 1?",          2, False, SongMood.RELAXED,  ),
    SongData("TheEnd",              0x6E, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("RecoveredStarRod",    0x6F, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("TwinkTheme",          0x70, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("TwinkTheme",          0x70, "end game version",    1, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("StirringCake",        0x71, "default",             0, False, SongMood.UPBEAT,   SongType.EVENT),
    SongData("GourmetGuyFreakout",  0x72, "default",             0, False, SongMood.CRISIS,   SongType.EVENT),
    SongData("PrisonerPeachTheme",  0x73, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("PrisonerPeachTheme",  0x73, "on balcony",          1, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("PeachMission",        0x74, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("PeachSneaking",       0x75, "default",             0, True,  SongMood.SINISTER, SongType.FIELDANDTOWN),
    SongData("PeachCaught",         0x76, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("PeachQuiz",           0x77, "intro",               0, False, SongMood.UPBEAT,   SongType.EVENT),
    #SongData("PeachQuiz",           0x77, "default",             1, True,  SongMood.UPBEAT,   ),
    SongData("PeachQuiz",           0x77, "outro",               2, False, SongMood.UPBEAT,   SongType.EVENT),
    SongData("StarSpiritTheme",     0x78, "prologue",            0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("StarSpiritTheme",     0x78, "saved spirit",        1, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("PenguinWhodunit",     0x79, "w/ intro",            0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("PenguinWhodunit",     0x79, "w/o intro",           1, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("PenguinWakesUp",      0x7A, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    #SongData("PenguinWakesUp",      0x7A, "sped up?",            1, False, SongMood.UPBEAT,   ),
    SongData("MagicBeanstalk",      0x7B, "stalk grows",         0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("CastingSpell",        0x7C, "Merlee",              0, False, SongMood.UPBEAT,   SongType.EVENT),
    SongData("CastingSpell",        0x7C, "Merlon",              1, False, SongMood.UPBEAT,   SongType.EVENT),
    SongData("CastingSpell",        0x7C, "Merluvlee",           2, False, SongMood.UPBEAT,   SongType.EVENT),
    SongData("LakilesterTheme",     0x7D, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("GoombaBrosRetreat",   0x7E, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("GoombaBrosRetreat",   0x7E, "w/ GK castle intro",  1, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("SunshineReturns",     0x7F, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("MtRuggedTrain",       0x80, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    #SongData("MtRuggedTrain",       0x80, "sped up?",            1, False, SongMood.UPBEAT,   ),
    SongData("RidingTheWhale",      0x81, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    #SongData("RidingTheWhale",      0x81, "unused version",      1, False, SongMood.RELAXED,  ),
    SongData("NewPartnerUS",        0x82, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("DryDryRuinsAppear",   0x83, "default",             0, False, SongMood.SINISTER, SongType.EVENT),
    SongData("CandyCanes",          0x84, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("Playroom",            0x85, "default",             0, True,  SongMood.UPBEAT,   SongType.FIELDANDTOWN),
    SongData("MoustafaTheme",       0x86, "default",             0, True,  SongMood.SINISTER, SongType.EVENT),
    SongData("GameOver",            0x87, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("TakingRest",          0x88, "default",             0, False, SongMood.RELAXED,  SongType.JINGLE),
    SongData("FlowerNPCTheme",      0x89, "Petunia",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("FlowerNPCTheme",      0x89, "Posie",               1, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("FlowerNPCTheme",      0x89, "Lily",                2, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("FlowerNPCTheme",      0x89, "Rosie",               3, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("FlowerGateAppears",   0x8A, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("BattleEnd",           0x8B, "default",             0, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("BattleEnd",           0x8B, "w/ echo",             1, False, SongMood.UPBEAT,   SongType.JINGLE),
    SongData("PopDivaSong",         0x8C, "default",             0, False, SongMood.RELAXED,  SongType.EVENT),
    SongData("PopDivaSong",         0x8C, "longer version",      1, False, SongMood.RELAXED,  SongType.EVENT),
    SongData("BooMinigame",         0x8D, "default",             0, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("LevelUp",             0x8E, "w/ end of battle",    0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("LevelUp",             0x8E, "w/ echo",             1, True,  SongMood.UPBEAT,   SongType.EVENT),
    # 0x8F unused,
    #SongData("ParadeDay",           0x90, "default",             0, False, SongMood.?       , ),
    #SongData("ParadeDay",           0x90, "slightly muted",      1, False, SongMood.?       , ),
    #SongData("ParadeNight",         0x91, "default",             0, False, SongMood.?       , ),
    #SongData("ParadeNight",         0x91, "shy guy sped up?",    1, False, SongMood.?       , ),
    # 0x92 unused
    # 0x93 unused
    SongData("MarioBrosHouse",      0x94, "default",             0, True,  SongMood.RELAXED,  SongType.FIELDANDTOWN),
    SongData("IntroStory",          0x95, "start",               0, False, SongMood.RELAXED,  SongType.EVENT),
    SongData("IntroStory",          0x95, "bowser part",         1, False, SongMood.SINISTER, SongType.EVENT),
    SongData("IntroStory",          0x95, "hopeful part",        2, False, SongMood.RELAXED,  SongType.EVENT),
    SongData("IntroStory",          0x95, "Peachs castle falls", 3, True,  SongMood.RELAXED,  SongType.EVENT),
    SongData("NewPartnerJP",        0x96, "default",             0, True,  SongMood.UPBEAT,   SongType.EVENT),
    SongData("NewPartnerJP",        0x96, "w/ echo",             1, True,  SongMood.UPBEAT,   SongType.EVENT),
    # 0x97 - 0x9F unused
]
