from enum import IntEnum
from utils.encryption import convert_short, convert_ushort, convert_int, convert_long, convert_float, convert_double, convert_string, convert_uint, convert_ulong, create_key
import inspect

def dump_table(table_instance) -> list:
    excel_name = table_instance.__class__.__name__.removesuffix("Table")
    module_parts = table_instance.__class__.__module__.split(".")
    source = "ExcelDB" if "ExcelDB" in module_parts else "Excel"
    current_module = inspect.getmodule(inspect.currentframe())
    dump_func = getattr(current_module, f"dump_{source}_{excel_name}")
    password = create_key(excel_name.removesuffix("Excel"))
    return [dump_func(table_instance.DataList(j), password) for j in range(table_instance.DataListLength())]

class GroundNodeType(IntEnum):
    None_ = 0
    WalkAble = 1
    JumpAble = 2
    TSSOnly = 3
    NotWalkAble = 4

class BubbleType(IntEnum):
    Idle = 0
    Monologue = 1
    EmoticonNormal = 2
    EmoticonFavorite = 3
    EmoticonReward = 4
    EmoticonGiveGift = 5

class FurnitureCategory(IntEnum):
    Furnitures = 0
    Decorations = 1
    Interiors = 2

class FurnitureSubCategory(IntEnum):
    Table = 0
    Closet = 1
    Chair = 2
    Bed = 3
    Prop = 4
    FurnitureEtc = 5
    FurnitureSubCategory1 = 6
    HomeAppliance = 7
    Trophy = 8
    WallDecoration = 9
    FloorDecoration = 10
    DecorationEtc = 11
    DecorationSubCategory1 = 12
    Floor = 13
    Background = 14
    Wallpaper = 15
    InteriorsSubCategory1 = 16
    All = 17

class FurnitureLocation(IntEnum):
    None_ = 0
    Inventory = 1
    Floor = 2
    WallLeft = 3
    WallRight = 4

class AcademyMessageConditions(IntEnum):
    None_ = 0
    FavorRankUp = 1
    AcademySchedule = 2
    Answer = 3
    Feedback = 4

class AcademyMessageTypes(IntEnum):
    None_ = 0
    Text = 1
    Image = 2

class VoiceEvent(IntEnum):
    OnTSA = 0
    FormationPickUp = 1
    CampaignResultDefeat = 2
    CampaignResultVictory = 3
    CharacterLevelUp = 4
    CharacterTranscendence = 5
    SkillLevelUp = 6
    Formation = 7
    CampaignCharacterSpawn = 8
    BattleStartTimeline = 9
    BattleVictoryTimeline = 10
    CharacterFavor = 11
    BattleMiss = 12
    BattleBlock = 13
    BattleCover = 14
    BattleMove = 15
    BattleMoveToForamtionBeacon = 16
    MGS_GameStart = 17
    MGS_CharacterSelect = 18
    MGS_Attacking = 19
    MGS_GeasGet = 20
    EXSkill = 21
    EXSkillLevel = 22
    EXSkill2 = 23
    EXSkillLevel2 = 24
    EXSkill3 = 25
    EXSkillLevel3 = 26
    EXSkill4 = 27
    EXSkillLevel4 = 28
    PublicSkill01 = 29
    PublicSkill02 = 30
    InteractionPublicSkill01 = 31
    InteractionPublicSkill02 = 32
    FormationStyleChange = 33
    BattleInteractionVictoryTimeline = 34

class UnitType(IntEnum):
    None_ = 0
    AR = 1
    RF = 2
    HG = 3
    MG = 4
    SMG = 5
    SG = 6
    HZ = 7
    Melee = 8

class AttackType(IntEnum):
    Single = 0
    Splash = 1
    Through = 2
    Heal = 3

class ProjectileType(IntEnum):
    Guided = 0
    Ground = 1
    GuidedExplosion = 2
    GroundConstDistance = 3
    AirConstDistance = 4

class DamageFontColor(IntEnum):
    Blue = 0
    White = 1
    Yellow = 2
    Red = 3
    Green = 4

class EmoticonEvent(IntEnum):
    CoverEnter = 0
    ShelterEnter = 1
    Panic = 2
    NearlyDead = 3
    Reload = 4
    Found = 5
    GetBeacon = 6
    Warning = 7

class BulletType(IntEnum):
    Normal = 0
    Pierce = 1
    Explosion = 2
    Siege = 3
    Mystic = 4
    None_ = 5
    Sonic = 6
    Chemical = 7

class ActionType(IntEnum):
    Crush = 0
    Courage = 1
    Tactic = 2

class BuffOverlap(IntEnum):
    Able = 0
    Unable = 1
    Change = 2
    Additive = 3

class ReArrangeTargetType(IntEnum):
    AllySelf = 0
    AllyAll = 1
    AllyUnitType = 2
    AllyGroup = 3

class ArmorType(IntEnum):
    LightArmor = 0
    HeavyArmor = 1
    Unarmed = 2
    Structure = 3
    Normal = 4
    ElasticArmor = 5
    CompositeArmor = 6

class WeaponType(IntEnum):
    None_ = 0
    SG = 1
    SMG = 2
    AR = 3
    GL = 4
    HG = 5
    RL = 6
    SR = 7
    DSMG = 8
    RG = 9
    DSG = 10
    Vulcan = 11
    Missile = 12
    Cannon = 13
    Taser = 14
    MG = 15
    Binah = 16
    MT = 17
    Relic = 18
    FT = 19
    Akemi = 20
    KetherCannon = 21

class EntityMaterialType(IntEnum):
    Wood = 0
    Stone = 1
    Flesh = 2
    Metal = 3

class CoverMotionType(IntEnum):
    All = 0
    Kneel = 1

class TargetSortBy(IntEnum):
    DISTANCE = 0
    HP = 1
    DAMAGE_EFFICIENCY = 2
    TARGETED_COUNT = 3
    RANDOM = 4
    FRONT_FORMATION = 5

class PositioningType(IntEnum):
    CloseToObstacle = 0
    CloseToTarget = 1

class ExternalBTNodeType(IntEnum):
    Sequence = 0
    Selector = 1
    Instant = 2
    SubNode = 3
    ExecuteAll = 4

class ExternalBTTrigger(IntEnum):
    None_ = 0
    HPUnder = 1
    ApplySkillEffectCategory = 2
    HaveNextExSkillActiveGauge = 3
    UseNormalSkill = 4
    UseExSkill = 5
    CheckActiveGaugeOver = 6
    CheckPeriod = 7
    CheckSummonCharacterCountOver = 8
    CheckSummonCharacterCountUnder = 9
    ApplyGroggy = 10
    ApplyLogicEffectTemplateId = 11
    OnSpawned = 12
    CheckActiveGaugeBetween = 13
    DestroyParts = 14
    CheckHallucinationCountOver = 15
    CheckHallucinationCountUnder = 16
    UseSkillEndGroupId = 17

class ExternalBehavior(IntEnum):
    UseNextExSkill = 0
    ChangePhase = 1
    ChangeSection = 2
    AddActiveGauge = 3
    UseSelectExSkill = 4
    ClearNormalSkill = 5
    MoveLeft = 6
    MoveRight = 7
    AllUseSelectExSkill = 8
    ConnectCharacterToDummy = 9
    ConnectExSkillToParts = 10
    SetMaxHPToParts = 11
    AlivePartsUseExSkill = 12
    ActivatePart = 13
    AddGroggy = 14
    SelectTargetToUseSkillAlly = 15
    ForceChangePhase = 16
    ClearUseSkillEndGroupId = 17
    ChangePhaseKeepATG = 18
    ForceChangePhaseKeepATG = 19

class TacticEntityType(IntEnum):
    None_ = 0
    Student = 1
    Minion = 2
    Elite = 4
    Champion = 8
    Boss = 16
    Obstacle = 32
    Servant = 64
    Vehicle = 128
    Summoned = 256
    Hallucination = 512
    DestructibleProjectile = 1024

class Difficulty(IntEnum):
    Normal = 0
    Hard = 1
    VeryHard = 2
    Hardcore = 3
    Extreme = 4
    Insane = 5
    Torment = 6
    Lunatic = 7

class EngageType(IntEnum):
    SearchAndMove = 0
    HoldPosition = 1

class HitEffectPosition(IntEnum):
    Position = 0
    HeadBone = 1
    BodyBone = 2
    Follow = 3

class StageTopography(IntEnum):
    Street = 0
    Outdoor = 1
    Indoor = 2

class TerrainAdaptationStat(IntEnum):
    D = 0
    C = 1
    B = 2
    A = 3
    S = 4
    SS = 5

class SquadType(IntEnum):
    None_ = 0
    Main = 1
    Support = 2
    TSS = 3

class ObstacleDestroyType(IntEnum):
    Remain = 0
    Remove = 1

class ObstacleHeightType(IntEnum):
    Low = 0
    Middle = 1
    High = 2

class AimIKType(IntEnum):
    None_ = 0
    OneHandRight = 1
    OneHandLeft = 2
    TwoHandRight = 3
    TwoHandLeft = 4
    Tripod = 5
    Dual = 6
    Max = 7

class DamageAttribute(IntEnum):
    Resist = 0
    Normal = 1
    Weak = 2
    Effective = 3

class SkillPriorityCheckTarget(IntEnum):
    Ally = 0
    Enemy = 1
    All = 2

class StageType(IntEnum):
    Main = 0
    Sub = 1

class OperatorCondition(IntEnum):
    None_ = 0
    StrategyStart = 1
    StrategyVictory = 2
    StrategyDefeat = 3
    AdventureCombatStart = 4
    AdventureCombatVictory = 5
    AdventureCombatDefeat = 6
    ArenaCombatStart = 7
    ArenaCombatVictory = 8
    ArenaCombatDefeat = 9
    WeekDungeonCombatStart = 10
    WeekDungeonCombatVictory = 11
    WeekDungeonCombatDefeat = 12
    SchoolDungeonCombatStart = 13
    SchoolDungeonCombatVictory = 14
    SchoolDungeonCombatDefeat = 15
    StrategyWarpUnitFromHideTile = 16
    TimeAttackDungeonStart = 17
    TimeAttackDungeonVictory = 18
    TimeAttackDungeonDefeat = 19
    WorldRaidBossSpawn = 20
    WorldRaidBossKill = 21
    WorldRaidBossDamaged = 22
    WorldRaidScenarioBattle = 23
    MinigameTBGThemaOpen = 24
    MinigameTBGThemaComeback = 25
    MinigameTBGAllyRevive = 26
    MinigameTBGItemUse = 27

class KnockbackDirection(IntEnum):
    TargetToCaster = 0
    CasterToTarget = 1
    TargetToHitPosition = 2
    HitPositionToTarget = 3
    CasterToHitPosition = 4
    HitPositionToCaster = 5
    Caster = 6
    Target = 7

class EndCondition(IntEnum):
    Duration = 0
    ReloadCount = 1
    AmmoCount = 2
    AmmoHit = 3
    HitCount = 4
    None_ = 5
    UseExSkillCount = 6
    UseTargetSlotExSkillCount = 7
    UseExSkillOverloadedCount = 8

class EffectBone(IntEnum):
    None_ = 0
    Shot = 1
    Head = 2
    Body = 3
    Shot2 = 4
    Shot3 = 5
    Extra = 6
    Extra2 = 7
    Extra3 = 8

class ArenaSimulatorServer(IntEnum):
    Preset = 0
    Live = 1
    Dev = 2
    QA = 3

class WorldRaidDifficulty(IntEnum):
    None_ = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7

class TacticSpeed(IntEnum):
    None_ = 0
    Slow = 1
    Normal = 2
    Fast = 3

class TacticSkillUse(IntEnum):
    None_ = 0
    Auto = 1
    Manual = 2

class ShowSkillCutIn(IntEnum):
    None_ = 0
    Once = 1
    Always = 2

class BattleCalculationStat(IntEnum):
    FinalDamage = 0
    FinalHeal = 1
    FinalDamageRatio = 2
    FinalDamageRatio2 = 3
    FinalCriticalRate = 4

class StatTransType(IntEnum):
    SpecialTransStat = 0
    TSATransStat = 1

class BattleDialogType(IntEnum):
    Talk = 0
    Think = 1
    Shout = 2

class UIEnemyCountType(IntEnum):
    Normal = 0
    None_ = 1
    Wave = 2
    FindGift = 3

class CharacterVoiceOverridePriority(IntEnum):
    None_ = 0
    High = 1
    Low = 2

class SkillSlotShowType(IntEnum):
    None_ = 0
    Ex = 1
    Public = 2
    Passive = 3
    Global = 4

class SkillSlotHighLightType(IntEnum):
    None_ = 0
    New = 1
    Upgrade = 2

class StatLevelUpType(IntEnum):
    Standard = 0
    Premature = 1
    LateBloom = 2
    Obstacle = 3
    TimeAttack = 4

class StatType(IntEnum):
    None_ = 0
    MaxHP = 1
    AttackPower = 2
    DefensePower = 3
    HealPower = 4
    AccuracyPoint = 5
    AccuracyRate = 6
    DodgePoint = 7
    DodgeRate = 8
    CriticalPoint = 9
    CriticalChanceRate = 10
    CriticalResistChanceRate = 11
    CriticalDamageRate = 12
    MoveSpeed = 13
    SightRange = 14
    ActiveGauge = 15
    StabilityPoint = 16
    StabilityRate = 17
    ReloadTime = 18
    MaxBulletCount = 19
    IgnoreDelayCount = 20
    WeaponRange = 21
    BlockRate = 22
    BodyRadius = 23
    ActionCount = 24
    StrategyMobility = 25
    StrategySightRange = 26
    StreetBattleAdaptation = 27
    OutdoorBattleAdaptation = 28
    IndoorBattleAdaptation = 29
    HealEffectivenessRate = 30
    CriticalChanceResistPoint = 31
    CriticalDamageResistRate = 32
    LifeRecoverOnHit = 33
    NormalAttackSpeed = 34
    AmmoCost = 35
    GroggyGauge = 36
    GroggyTime = 37
    DamageRatio = 38
    DamagedRatio = 39
    OppressionPower = 40
    OppressionResist = 41
    RegenCost = 42
    InitialWeaponRangeRate = 43
    DefensePenetration = 44
    DefensePenetrationResisit = 45
    ExtendBuffDuration = 46
    ExtendDebuffDuration = 47
    ExtendCrowdControlDuration = 48
    EnhanceExplosionRate = 49
    EnhancePierceRate = 50
    EnhanceMysticRate = 51
    EnhanceLightArmorRate = 52
    EnhanceHeavyArmorRate = 53
    EnhanceUnarmedRate = 54
    EnhanceSiegeRate = 55
    EnhanceNormalRate = 56
    EnhanceStructureRate = 57
    EnhanceNormalArmorRate = 58
    DamageRatio2Increase = 59
    DamageRatio2Decrease = 60
    DamagedRatio2Increase = 61
    DamagedRatio2Decrease = 62
    EnhanceSonicRate = 63
    EnhanceElasticArmorRate = 64
    ExDamagedRatioIncrease = 65
    ExDamagedRatioDecrease = 66
    EnhanceExDamageRate = 67
    ReduceExDamagedRate = 68
    EnhanceBasicsDamageRate = 69
    ReduceBasicsDamagedRate = 70
    HealRate = 71
    HealLightArmorRate = 72
    HealHeavyArmorRate = 73
    HealUnarmedRate = 74
    HealElasticArmorRate = 75
    HealNormalArmorRate = 76
    HealedExplosionRate = 77
    HealedPierceRate = 78
    HealedMysticRate = 79
    HealedSonicRate = 80
    HealedNormalRate = 81
    GrowthScore = 82
    CharacterBulletTypeEnhanceRate = 83
    MaxCostIncrease = 84
    EnhanceChemicalRate = 85
    EnhanceCompositeArmorRate = 86
    EnhanceWeakDamageRate = 87
    ReduceWeakDamagedRate = 88
    WeakDamagedRatio = 89
    EffectiveDamagedRatio = 90
    NormalDamagedRatio = 91
    ResistDamagedRatio = 92
    Max = 93

class ProductionStep(IntEnum):
    ToDo = 0
    Doing = 1
    Complete = 2
    Release = 3

class TacticRange(IntEnum):
    Back = 0
    Front = 1
    Middle = 2

class CVCollectionType(IntEnum):
    CVNormal = 0
    CVEvent = 1
    CVEtc = 2

class CVPrintType(IntEnum):
    CharacterOverwrite = 0
    PrefabOverwrite = 1
    Add = 2

class PotentialStatBonusRateType(IntEnum):
    None_ = 0
    MaxHP = 1
    AttackPower = 2
    HealPower = 3

class GrowthFactor(IntEnum):
    CharacterLevel = 0
    CharacterGrade = 1
    ExSkillLevel = 2
    PublicSkillLevel = 3
    PassiveSkillLevel = 4
    ExtraPassiveSkillLevel = 5
    Equipment01Tier = 6
    Equipment01Level = 7
    Equipment02Tier = 8
    Equipment02Level = 9
    Equipment03Tier = 10
    Equipment03Level = 11
    CharacterWeaponTier = 12
    CharacterWeponLevel = 13
    PotentialStat01Level = 14
    PotentialStat02Level = 15
    PotentialStat03Level = 16
    FavorRank = 17
    Max = 18

class ClanRewardType(IntEnum):
    None_ = 0
    AssistTerm = 1
    AssistRent = 2
    Attendance = 3

class ConquestEnemyType(IntEnum):
    None_ = 0
    Normal = 1
    MiddleBoss = 2
    Boss = 3
    UnexpectedEvent = 4
    Challenge = 5
    IndividualErosion = 6
    MassErosion = 7

class ConquestTeamType(IntEnum):
    None_ = 0
    Team1 = 1
    Team2 = 2
    Team3 = 3

class ConquestTileType(IntEnum):
    None_ = 0
    Start = 1
    Normal = 2
    Battle = 3
    Base = 4

class ConquestObjectType(IntEnum):
    None_ = 0
    ParcelOneTimePerAccount = 1

class ConquestProgressType(IntEnum):
    None_ = 0
    Upgrade = 1
    Manage = 2

class ConquestEventType(IntEnum):
    None_ = 0
    Event01 = 1
    Event02 = 2

class ConquestConditionType(IntEnum):
    None_ = 0
    OpenDateOffset = 1
    ItemAcquire = 2
    ParcelUse = 3
    KillUnit = 4

class ConquestErosionType(IntEnum):
    None_ = 0
    IndividualErosion = 1
    MassErosion = 2

class ContentType(IntEnum):
    None_ = 0
    CampaignMainStage = 1
    CampaignSubStage = 2
    WeekDungeon = 3
    EventContentMainStage = 4
    EventContentSubStage = 5
    CampaignTutorialStage = 6
    EventContentMainGroundStage = 7
    SchoolDungeon = 8
    TimeAttackDungeon = 9
    Raid = 10
    Conquest = 11
    EventContentStoryStage = 12
    CampaignExtraStage = 13
    StoryStrategyStage = 14
    ScenarioMode = 15
    EventContent = 16
    WorldRaid = 17
    EliminateRaid = 18
    Chaser = 19
    FieldContentStage = 20
    MultiFloorRaid = 21
    MinigameDefense = 22
    InteractiveWorldRaid = 23
    PermanentRaid = 24

class EventContentType(IntEnum):
    Stage = 0
    Gacha = 1
    Mission = 2
    Shop = 3
    Raid = 4
    Arena = 5
    BoxGacha = 6
    Collection = 7
    Recollection = 8
    MiniGameRhythm = 9
    CardShop = 10
    EventLocation = 11
    MinigameRhythmEvent = 12
    FortuneGachaShop = 13
    SubEvent = 14
    EventMeetup = 15
    BoxGachaResult = 16
    Conquest = 17
    WorldRaid = 18
    DiceRace = 19
    MiniGameRhythmMission = 20
    WorldRaidEntrance = 21
    MiniEvent = 22
    MiniGameShooting = 23
    MiniGameShootingMission = 24
    MiniGameTBG = 25
    TimeAttackDungeon = 26
    EliminateRaid = 27
    Treasure = 28
    Field = 29
    MultiFloorRaid = 30
    MinigameDreamMaker = 31
    MiniGameDefense = 32
    OpenWebView = 33
    SpecialMiniEvent = 34
    ScenarioCollection = 35
    ScenarioShortcut = 36
    SeasonalEvent = 37
    MiniShop = 38
    MiniGameRoad = 39
    MiniGameCCG = 40
    Concentration = 41
    InteractiveWorldRaid = 42
    ClueSearch = 43

class StarGoalType(IntEnum):
    None_ = 0
    AllAlive = 1
    Clear = 2
    GetBoxes = 3
    ClearTimeInSec = 4
    AllyBaseDamage = 5

class OpenConditionContent(IntEnum):
    Shop = 0
    Gacha = 1
    LobbyIllust = 2
    Raid = 3
    Cafe = 4
    Unit_Growth_Skill = 5
    Unit_Growth_LevelUp = 6
    Unit_Growth_Transcendence = 7
    Arena = 8
    Academy = 9
    Equip = 10
    Item = 11
    Favor = 12
    Prologue = 13
    Mission = 14
    WeekDungeon_Chase = 15
    __Deprecated_WeekDungeon_FindGift = 16
    __Deprecated_WeekDungeon_Blood = 17
    Story_Sub = 18
    Story_Replay = 19
    WeekDungeon = 20
    None_ = 21
    Shop_Gem = 22
    Craft = 23
    Student = 24
    GuideMission = 25
    Clan = 26
    Echelon = 27
    Campaign = 28
    EventContent = 29
    Guild = 30
    EventStage_1 = 31
    EventStage_2 = 32
    Talk = 33
    Billing = 34
    Schedule = 35
    Story = 36
    Tactic_Speed = 37
    Cafe_Invite = 38
    EventMiniGame_1 = 39
    SchoolDungeon = 40
    TimeAttackDungeon = 41
    ShiftingCraft = 42
    WorldRaid = 43
    Tactic_Skip = 44
    Mulligan = 45
    EventPermanent = 46
    Main_L_1_2 = 47
    Main_L_1_3 = 48
    Main_L_1_4 = 49
    EliminateRaid = 50
    Cafe_2 = 51
    Cafe_Invite_2 = 52
    MultiFloorRaid = 53
    StrategySkip = 54
    MinigameDreamMaker = 55
    MiniGameDefense = 56
    MiniGameCCG = 57
    Main_L_1_5 = 58
    Main_SNS = 59
    PermanentRaid = 60

class TutorialFailureContentType(IntEnum):
    None_ = 0
    Campaign = 1
    WeekDungeon = 2
    Raid = 3
    TimeAttackDungeon = 4
    WorldRaid = 5
    Conquest = 6
    EliminateRaid = 7
    MultiFloorRaid = 8
    InteractiveWorldRaid = 9

class FeverBattleType(IntEnum):
    Campaign = 0
    Raid = 1
    WeekDungeon = 2
    Arena = 3

class EventContentScenarioConditionType(IntEnum):
    None_ = 0
    DayAfter = 1
    EventPoint = 2

class EventTargetType(IntEnum):
    WeekDungeon = 0
    Chaser = 1
    Campaign_Normal = 2
    Campaign_Hard = 3
    SchoolDungeon = 4
    AcademySchedule = 5
    TimeAttackDungeon = 6
    AccountLevelExpIncrease = 7
    Raid = 8
    EliminateRaid = 9
    MultiFloorRaid = 10

class EventContentItemType(IntEnum):
    EventPoint = 0
    EventToken1 = 1
    EventToken2 = 2
    EventToken3 = 3
    EventToken4 = 4
    EventToken5 = 5
    EventMeetUpTicket = 6
    EventEtcItem = 7
    Concentration = 8

class CollectionUnlockType(IntEnum):
    None_ = 0
    ClearSpecificEventStage = 1
    ClearSpecificEventScenario = 2
    ClearSpecificEventMission = 3
    PurchaseSpecificItemCount = 4
    SpecificEventLocationRank = 5
    DiceRaceConsumeDiceCount = 6
    MinigameTBGThemaClear = 7
    MinigameEnter = 8
    MinigameDreamMakerParameter = 9
    ClearSpecificScenario = 10
    MinigameCCGBuyPerk = 11

class ShortcutContentType(IntEnum):
    None_ = 0
    CampaignStage = 1
    EventStage = 2
    Blood = 3
    WeekDungeon = 4
    Arena = 5
    Raid = 6
    Shop = 7
    ItemInventory = 8
    Craft = 9
    SchoolDungeon = 10
    Academy = 11
    Mission = 12
    MultiFloorRaid = 13

class SchoolDungeonType(IntEnum):
    SchoolA = 0
    SchoolB = 1
    SchoolC = 2
    None_ = 3

class EventContentBuffFindRule(IntEnum):
    None_ = 0
    WeaponType = 1
    SquadType = 2
    StreetBattleAdaptation = 3
    OutdoorBattleAdaptation = 4
    IndoorBattleAdaptation = 5
    BulletType = 6
    School = 7
    TacticRange = 8

class TimeAttackDungeonRewardType(IntEnum):
    Fixed = 0
    TimeWeight = 1

class TimeAttackDungeonType(IntEnum):
    None_ = 0
    Defense = 1
    Shooting = 2
    Destruction = 3
    Escort = 4

class SuddenMissionContentType(IntEnum):
    OrdinaryState = 0
    CampaignNormalStage = 1
    CampaignHardStage = 2
    EventStage = 3
    WeekDungeon = 4
    Chaser = 5
    SchoolDungeon = 6
    TimeAttackDungeon = 7
    Raid = 8

class EventNotifyType(IntEnum):
    RewardIncreaseEvent = 0
    AccountExpIncreaseEvent = 1
    RaidSeasonManager = 2
    TimeAttackDungeonSeasonManage = 3
    EliminateRaidSeasonManage = 4
    MultiFloorRaidSeasonManage = 5

class EventContentDiceRaceResultType(IntEnum):
    DiceResult1 = 0
    DiceResult2 = 1
    DiceResult3 = 2
    DiceResult4 = 3
    DiceResult5 = 4
    DiceResult6 = 5
    MoveForward = 6
    LapFinish = 7
    EventOccur = 8
    DiceResultFixed1 = 9
    DiceResultFixed2 = 10
    DiceResultFixed3 = 11
    DiceResultFixed4 = 12
    DiceResultFixed5 = 13
    DiceResultFixed6 = 14
    SpecialReward = 15

class EventContentDiceRaceNodeType(IntEnum):
    StartNode = 0
    RewardNode = 1
    MoveForwardNode = 2
    SpecialRewardNode = 3

class MeetupConditionType(IntEnum):
    None_ = 0
    EventContentStageClear = 1
    ScenarioClear = 2

class MeetupConditionPrintType(IntEnum):
    None_ = 0
    Lock = 1
    Hide = 2

class GuideMissionTabType(IntEnum):
    None_ = 0
    Daily = 1
    StageClear = 2

class EventContentReleaseType(IntEnum):
    None_ = 0
    Permanent = 1
    MainStory = 2
    PermanentSpecialOperate = 3
    PermanentConquest = 4

class SubEventType(IntEnum):
    None_ = 0
    SubEvent = 1
    SubEventPermanent = 2

class ConcentrationVoiceCondition(IntEnum):
    None_ = 0
    PairMatchFail = 1
    PairMatchSuccess = 2
    RoundRenewal = 3

class ConcentrationRewardType(IntEnum):
    None_ = 0
    PairMatch = 1
    RoundRenewal = 2

class RecipeDisplayOptions(IntEnum):
    None_ = 0
    Always = 1
    HideNoMaterials = 2

class SpoilerPopupType(IntEnum):
    None_ = 0
    Default = 1
    Warning = 2
    WarningNoGo = 3

class RaidBossGroupType(IntEnum):
    None_ = 0
    Binah = 1
    Chesed = 2
    ShiroKuro = 3
    Hieronymus = 4
    Kaitenger = 5
    Perorozilla = 6
    HOD = 7
    Goz = 8
    HoverCraft = 9
    EN0005 = 10
    EN0006 = 11
    EN0010 = 12
    EN0013 = 13
    EN0022 = 14

class EquipmentCategory(IntEnum):
    Unable = 0
    Exp = 1
    Bag = 2
    Hat = 3
    Gloves = 4
    Shoes = 5
    Badge = 6
    Hairpin = 7
    Charm = 8
    Watch = 9
    Necklace = 10
    WeaponExpGrowthA = 11
    WeaponExpGrowthB = 12
    WeaponExpGrowthC = 13
    WeaponExpGrowthZ = 14

class EquipmentOptionType(IntEnum):
    None_ = 0
    MaxHP_Base = 1
    MaxHP_Coefficient = 2
    AttackPower_Base = 3
    AttackPower_Coefficient = 4
    DefensePower_Base = 5
    DefensePower_Coefficient = 6
    HealPower_Base = 7
    HealPower_Coefficient = 8
    CriticalPoint_Base = 9
    CriticalPoint_Coefficient = 10
    CriticalChanceRate_Base = 11
    CriticalDamageRate_Base = 12
    CriticalDamageRate_Coefficient = 13
    SightRange_Base = 14
    SightRange_Coefficient = 15
    MaxBulletCount_Base = 16
    MaxBulletCount_Coefficient = 17
    HPRecoverOnKill_Base = 18
    HPRecoverOnKill_Coefficient = 19
    StreetBattleAdaptation_Base = 20
    OutdoorBattleAdaptation_Base = 21
    IndoorBattleAdaptation_Base = 22
    HealEffectivenessRate_Base = 23
    HealEffectivenessRate_Coefficient = 24
    CriticalChanceResistPoint_Base = 25
    CriticalChanceResistPoint_Coefficient = 26
    CriticalDamageResistRate_Base = 27
    CriticalDamageResistRate_Coefficient = 28
    ExSkillUpgrade = 29
    OppressionPower_Base = 30
    OppressionPower_Coefficient = 31
    OppressionResist_Base = 32
    OppressionResist_Coefficient = 33
    StabilityPoint_Base = 34
    StabilityPoint_Coefficient = 35
    AccuracyPoint_Base = 36
    AccuracyPoint_Coefficient = 37
    DodgePoint_Base = 38
    DodgePoint_Coefficient = 39
    MoveSpeed_Base = 40
    MoveSpeed_Coefficient = 41
    Max = 42
    NormalAttackSpeed_Base = 43
    NormalAttackSpeed_Coefficient = 44
    DefensePenetration_Base = 45
    DefensePenetrationResisit_Base = 46
    ExtendBuffDuration_Base = 47
    ExtendDebuffDuration_Base = 48
    ExtendCrowdControlDuration_Base = 49
    EnhanceExplosionRate_Base = 50
    EnhanceExplosionRate_Coefficient = 51
    EnhancePierceRate_Base = 52
    EnhancePierceRate_Coefficient = 53
    EnhanceMysticRate_Base = 54
    EnhanceMysticRate_Coefficient = 55
    EnhanceLightArmorRate_Base = 56
    EnhanceLightArmorRate_Coefficient = 57
    EnhanceHeavyArmorRate_Base = 58
    EnhanceHeavyArmorRate_Coefficient = 59
    EnhanceUnarmedRate_Base = 60
    EnhanceUnarmedRate_Coefficient = 61
    EnhanceSiegeRate_Base = 62
    EnhanceSiegeRate_Coefficient = 63
    EnhanceNormalRate_Base = 64
    EnhanceNormalRate_Coefficient = 65
    EnhanceStructureRate_Base = 66
    EnhanceStructureRate_Coefficient = 67
    EnhanceNormalArmorRate_Base = 68
    EnhanceNormalArmorRate_Coefficient = 69
    DamageRatio2Increase_Base = 70
    DamageRatio2Increase_Coefficient = 71
    DamageRatio2Decrease_Base = 72
    DamageRatio2Decrease_Coefficient = 73
    DamagedRatio2Increase_Base = 74
    DamagedRatio2Increase_Coefficient = 75
    DamagedRatio2Decrease_Base = 76
    DamagedRatio2Decrease_Coefficient = 77
    EnhanceSonicRate_Base = 78
    EnhanceSonicRate_Coefficient = 79
    EnhanceElasticArmorRate_Base = 80
    EnhanceElasticArmorRate_Coefficient = 81
    IgnoreDelayCount_Base = 82
    WeaponRange_Base = 83
    BlockRate_Base = 84
    BlockRate_Coefficient = 85
    AmmoCost_Base = 86
    RegenCost_Base = 87
    RegenCost_Coefficient = 88
    MaxCostIncrease_Base = 89
    HealRate_Base = 90
    EnhanceChemicalRate_Base = 91
    EnhanceChemicalRate_Coefficient = 92
    EnhanceCompositeArmorRate_Base = 93
    EnhanceCompositeArmorRate_Coefficient = 94

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1
    Count = 2

class WeekDay(IntEnum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    All = 7

class EchelonType(IntEnum):
    None_ = 0
    Adventure = 1
    Raid = 2
    ArenaAttack = 3
    ArenaDefence = 4
    WeekDungeonChaserA = 5
    Scenario = 6
    WeekDungeonBlood = 7
    WeekDungeonChaserB = 8
    WeekDungeonChaserC = 9
    WeekDungeonFindGift = 10
    EventContent = 11
    SchoolDungeonA = 12
    SchoolDungeonB = 13
    SchoolDungeonC = 14
    TimeAttack = 15
    WorldRaid = 16
    Conquest = 17
    ConquestManage = 18
    StoryStrategyStage = 19
    EliminateRaid01 = 20
    EliminateRaid02 = 21
    EliminateRaid03 = 22
    Field = 23
    MultiFloorRaid = 24
    MinigameDefense = 25
    PermanentRaid = 26

class EchelonExtensionType(IntEnum):
    Base = 0
    Extension = 1

class ArenaRewardType(IntEnum):
    None_ = 0
    Time = 1
    Daily = 2
    SeasonRecord = 3
    OverallRecord = 4
    SeasonClose = 5
    AttackVictory = 6
    DefenseVictory = 7
    RankIcon = 8

class ServiceActionType(IntEnum):
    ClanCreate = 0
    HardAdventurePlayCountRecover = 1

class WebAPIErrorLevel(IntEnum):
    None_ = 0
    Warning = 1
    Error = 2

class GachaTicketType(IntEnum):
    None_ = 0
    PackageThreeStar = 1
    ThreeStar = 2
    TwoStar = 3
    Normal = 4
    NormalOnce = 5
    StartDash = 6
    SelectRecruit = 7
    PackagePropertyThreeStar = 8
    Temp_1 = 9
    PackageAcademyThreeStar = 10
    SelectPickup = 11
    SelectPickupOnce = 12
    PackageLimitedThreeStar = 13
    PackageThreeStar_R88_Explosion = 14
    PackageThreeStar_R88_Mystic = 15
    PackageThreeStar_R88_Pierce = 16
    PackageThreeStar_R88_Sonic = 17

class EventChangeType(IntEnum):
    MainSub = 0
    SubMain = 1

class FurnitureFunctionType(IntEnum):
    None_ = 0
    EventCollection = 1
    VideoPlay = 2
    TrophyCollection = 3
    InteractionBGMPlay = 4

class EmblemCategory(IntEnum):
    None_ = 0
    Default = 1
    Mission = 2
    GroupStory = 3
    Event = 4
    MainStory = 5
    Favor = 6
    Boss = 7
    Etc = 8
    Etc_Anniversary = 9
    MultiFloorRaid = 10
    Potential = 11
    BattlePass = 12

class EmblemDisplayType(IntEnum):
    Always = 0
    Time = 1
    Favor = 2
    Potential = 3

class EmblemCheckPassType(IntEnum):
    None_ = 0
    Default = 1
    Favor = 2
    Story = 3
    Potential = 4

class StickerGetConditionType(IntEnum):
    None_ = 0
    StickerCheckPass = 1
    GetStickerCondition = 2

class Nation(IntEnum):
    None_ = 0
    All = 1
    JP = 2
    GL = 3
    KR = 4

class CVUnlockScenarioType(IntEnum):
    Main = 0
    Event = 1
    SpecialOperation = 2

class PeriodType(IntEnum):
    None_ = 0
    Daily = 1
    Weekly = 2
    Monthly = 3

class AssistRewardType(IntEnum):
    None_ = 0
    AssistTerm = 1
    AssistRent = 2

class WorldRaidConditionType(IntEnum):
    None_ = 0
    BossClear = 1
    EventScenarioClear = 2
    EventStageClear = 3
    MainScenarioClear = 4
    BossHprateUnder = 5

class WorldRaidMapType(IntEnum):
    None_ = 0
    Carrier = 1
    WorldMap = 2

class GachaPhase(IntEnum):
    GachaIntro = 0
    CharacterAppearance = 1
    SignatureIntro = 2
    SignatureWait = 3
    SignatureConfirm = 4
    Result = 5

class DirectingCharacter(IntEnum):
    None_ = 0
    Arona = 1
    Plana = 2
    Both = 3

class FieldConditionType(IntEnum):
    Invalid = 0
    Interaction = 1
    QuestInProgress = 2
    QuestClear = 3
    Date = 4
    StageClear = 5
    HasKeyword = 6
    HasEvidence = 7
    OpenDate = 8
    OpenDateAfter = 9
    Scenario = 10
    Timeline = 11

class FieldInteractionType(IntEnum):
    None_ = 0
    Scenario = 1
    Reward = 2
    Dialog = 3
    Stage = 4
    KeywordFound = 5
    EvidenceFound = 6
    SceneChange = 7
    Timeline = 8
    ActionTrigger = 9
    Interplay = 10
    UnderCoverStage = 11
    SNSOpen = 12

class FieldConditionClass(IntEnum):
    AndOr = 0
    OrAnd = 1
    Multi = 2

class FieldDialogType(IntEnum):
    None_ = 0
    Talk = 1
    Think = 2
    Exclaim = 3
    Question = 4
    Upset = 5
    Surprise = 6
    Bulb = 7
    Heart = 8
    Sweat = 9
    Angry = 10
    Music = 11
    Dot = 12
    Momotalk = 13
    Phone = 14
    Keyword = 15
    Evidence = 16
    Chat = 17
    Keyword_843 = 18
    Angry_Nobubble = 19
    Sad_Nobubble = 20
    Steam_Nobubble = 21
    Respond_Nobubble = 22
    Sweat_Nobubble = 23
    Twinkle_Nobubble = 24
    ZZZ_Nobubble = 25
    Chat_Nobubble = 26
    Keyword_90101000 = 27
    SNS = 28
    ItemSack = 29
    ItemFlyer = 30
    ItemDocument = 31

class FieldTutorialType(IntEnum):
    None_ = 0
    MasteryHUD = 1
    QuestHUD = 2
    WorldMapHUD = 3

class FieldWorldMapButtonType(IntEnum):
    DefaultMode = 0
    Normal = 1
    Combat = 2
    Combat_VeryHard = 3
    UnderCover = 4

class FieldContentType(IntEnum):
    Event = 0
    Narrative = 1

class FieldSNSStateType(IntEnum):
    Open = 0
    Close = 1

class FieldSNSPostType(IntEnum):
    None_ = 0
    Normal = 1
    Bookmark = 2

class ItemCategory(IntEnum):
    Coin = 0
    CharacterExpGrowth = 1
    SecretStone = 2
    Material = 3
    Consumable = 4
    Collectible = 5
    Favor = 6
    RecruitCoin = 7
    MonthlyBonus = 8
    InvisibleToken = 9
    BattlePass = 10
    ProductSelect = 11
    ProductDailyRecord = 12

class DisplayGroupType(IntEnum):
    None_ = 0
    Default = 1
    Formation = 2
    Battle = 3
    Scenario = 4
    Momotalk = 5
    Cafe = 6
    Field = 7
    MinigameUndercover = 8
    MinigameShooting = 9
    MinigameRoad = 10
    MinigameCCG = 11

class MailType(IntEnum):
    System = 0
    Attendance = 1
    Event = 2
    MassTrade = 3
    InventoryFull = 4
    ArenaDefenseVictory = 5
    CouponUsageReward = 6
    ArenaSeasonClose = 7
    ProductReward = 8
    MonthlyProductReward = 9
    ExpiryChangeItem = 10
    ClanAttendance = 11
    AccountLink = 12
    NewUserBonus = 13
    LeftClanAssistReward = 14
    CashShopBuy = 15
    MonthlyProductPackage = 16
    WebEventReward = 17
    AttendanceImmediately = 18
    WeeklyProductReward = 19
    BiweeklyProductReward = 20
    Temp_1 = 21
    Temp_2 = 22
    Temp_3 = 23
    CouponCompleteReward = 24
    BirthdayMail = 25
    FromCS = 26
    ExpiryChangeCurrency = 27
    ExpiryBattlePassItem = 28
    FreeProductReward = 29
    ProductGooglePointReward = 30
    PaymentCenterProduct = 31
    PaymentCenterMonthly = 32
    PaymentCenterBattlePass = 33
    PaymentCenterDailyRecord = 34
    ExpiryProductDailyRecordItem = 35

class AttendanceType(IntEnum):
    Basic = 0
    Event = 1
    Newbie = 2
    EventCountDown = 3
    Event20Days = 4

class AttendanceCountRule(IntEnum):
    Accumulation = 0
    Date = 1

class AttendanceResetType(IntEnum):
    User = 0
    Server = 1

class WelcomeCampaignAttendanceType(IntEnum):
    Normal = 0
    Continuous = 1

class CCGCharacterType(IntEnum):
    None_ = 0
    Striker = 1
    Special = 2

class CCGCardType(IntEnum):
    None_ = 0
    Spell = 1
    Equipment = 2
    Zone = 3

class CCGEntityType(IntEnum):
    None_ = 0
    Character = 1
    Card = 2

class CCGStageType(IntEnum):
    None_ = 0
    Battle = 1
    Event = 2
    Camp = 3

class CCGStageRewardType(IntEnum):
    None_ = 0
    All = 1
    Random = 2
    Select = 3

class CCGLevelNodeIcon(IntEnum):
    None_ = 0
    Battle = 1
    Event = 2
    Camp = 3
    Boss = 4

class CCGTagType(IntEnum):
    None_ = 0
    Token = 1
    Supply = 2
    Trinity = 3
    Gehenna = 4
    Hyakkiyako = 5
    Kronos = 6
    Odyssey = 7
    Justice = 8
    TeaParty = 9
    HotSprings = 10
    GourmetResearch = 11
    Helmet = 12
    Sukeban = 13
    Pursuer = 14
    Kaitenger = 15
    PrefectTeam = 16
    MakeUpWork = 17
    FestivalOperations = 18
    NinjutsuResearch = 19
    Striker = 20
    Special = 21
    Spell = 22
    Equipment = 23
    Zone = 24
    Summoned = 25

class DreamMakerMultiplierCondition(IntEnum):
    None_ = 0
    Round = 1
    CollectionCount = 2
    EndingCount = 3

class DreamMakerParameterType(IntEnum):
    None_ = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4

class DreamMakerResult(IntEnum):
    None_ = 0
    Fail = 1
    Success = 2
    Perfect = 3

class DreamMakerParamOperationType(IntEnum):
    None_ = 0
    GrowUpHigh = 1
    GrowUp = 2
    GrowDownHigh = 3
    GrowDown = 4

class DreamMakerEndingCondition(IntEnum):
    None_ = 0
    Param01 = 1
    Param02 = 2
    Param03 = 3
    Param04 = 4
    Round = 5
    CollectionCount = 6

class DreamMakerVoiceCondition(IntEnum):
    None_ = 0
    Fail = 1
    Success = 2
    Perfect = 3
    DailyResult = 4

class DreamMakerEndingType(IntEnum):
    None_ = 0
    Normal = 1
    Special = 2

class DreamMakerEndingRewardType(IntEnum):
    None_ = 0
    FirstEndingReward = 1
    LoopEndingReward = 2

class RoadPuzzleMapTileType(IntEnum):
    None_ = 0
    Start = 1
    End = 2
    Transit = 3
    Obstacle = 4
    Empty = 5

class RoadPuzzleRailTileType(IntEnum):
    None_ = 0
    Straight = 1
    CurveBig = 2
    CurveSmall = 3

class RoadPuzzleVoiceCondition(IntEnum):
    None_ = 0
    TrainDepart = 1
    RailConnectSuccess = 2
    SaveSuccess = 3

class Geas(IntEnum):
    ForwardProjectile = 0
    DiagonalProjectile = 1
    SideProjectile = 2
    Pierce = 3
    Reflect = 4
    Burn = 5
    Chill = 6
    AttackPower = 7
    AttackSpeed = 8
    Critical = 9
    Heal = 10
    MoveSpeed = 11
    LifeSteal = 12
    Evasion = 13

class TBGObjectType(IntEnum):
    None_ = 0
    EnemyBoss = 1
    EnemyMinion = 2
    Random = 3
    Facility = 4
    TreasureBox = 5
    Start = 6
    Portal = 7

class TBGOptionSuccessType(IntEnum):
    None_ = 0
    TBGItemAcquire = 1
    ItemAcquire = 2
    TBGDiceAcquire = 3
    Portal = 4

class TBGItemType(IntEnum):
    None_ = 0
    Dice = 1
    Heal = 2
    HealExpansion = 3
    Defence = 4
    Guide = 5
    DiceResultValue = 6
    DefenceCritical = 7
    DiceResultConfirm = 8

class TBGItemEffectType(IntEnum):
    None_ = 0
    PermanentContinuity = 1
    TemporaryContinuation = 2
    Immediately = 3

class TBGThemaType(IntEnum):
    None_ = 0
    Normal = 1
    Hidden = 2

class TBGPortalCondition(IntEnum):
    None_ = 0
    ObjectAllEncounter = 1
    Round = 2

class TBGProbModifyCondition(IntEnum):
    None_ = 0
    AllyRevive = 1
    DicePlayFail = 2

class TBGVoiceCondition(IntEnum):
    None_ = 0
    DiceResultSuccess = 1
    DiceResultFailBattle = 2
    DiceResultFailRandom = 3
    EnemyDie = 4
    TreasureBoxNormal = 5
    TreasureBoxSpecial = 6
    FacilityResult = 7

class MiniGameTBGThemaRewardType(IntEnum):
    TreasureReward = 0
    EmptyTreasureReward = 1
    HiddenThemaTreasureReward = 2

class MissionCategory(IntEnum):
    Challenge = 0
    Daily = 1
    Weekly = 2
    Achievement = 3
    GuideMission = 4
    All = 5
    MiniGameScore = 6
    MiniGameEvent = 7
    EventAchievement = 8
    DailySudden = 9
    DailyFixed = 10
    EventFixed = 11
    WelcomeMission = 12

class MissionResetType(IntEnum):
    None_ = 0
    Daily = 1
    Weekly = 2
    Limit = 3

class MissionCompleteConditionType(IntEnum):
    None_ = 0
    Reset_DailyLogin = 1
    Reset_DailyLoginCount = 2
    Reset_CompleteMission = 3
    Achieve_EquipmentLevelUpCount = 4
    Achieve_EquipmentTierUpCount = 5
    Achieve_CharacterLevelUpCount = 6
    Reset_CharacterTranscendenceCount = 7
    Reset_ClearTaticBattleCount = 8
    Achieve_ClearCampaignStageCount = 9
    Reset_KillSpecificEnemyCount = 10
    Reset_KillEnemyWithTagCount = 11
    Reset_GetCharacterCount = 12
    Reset_GetCharacterWithTagCount = 13
    Reset_GetSpecificCharacterCount = 14
    Reset_AccountLevelUp = 15
    Reset_GetEquipmentCount = 16
    Reset_GachaCount = 17
    Reset_UseGem = 18
    Reset_GetGem = 19
    Reset_GetGemPaid = 20
    Achieve_GetGold = 21
    Achieve_GetItem = 22
    Reset_GetFavorLevel = 23
    Reset___Deprecated_EquipmentAtSpecificLevelCount = 24
    Achieve_EquipmentAtSpecificTierUpCount = 25
    Reset_CharacterAtSpecificLevelCount = 26
    Reset_CharacterAtSpecificTranscendenceCount = 27
    Achieve_CharacterSkillLevelUpCount = 28
    Reset_CharacterAtSpecificSkillLevelCount = 29
    Reset_CompleteScheduleCount = 30
    Reset_CompleteScheduleGroupCount = 31
    Reset_AcademyLocationRankSum = 32
    Reset_CraftCount = 33
    Achieve_GetComfortPoint = 34
    Achieve_GetWeaponCount = 35
    Reset_EquipWeaponCount_Obsolete = 36
    Reset_CompleteScheduleWithSpecificCharacter = 37
    Reset_CafeInteractionCount = 38
    Reset_SpecificCharacterAtSpecificLevel = 39
    Reset_SpecificCharacterAtSpecificTranscendence = 40
    Reset_LobbyInteraction = 41
    Achieve_ClearFindGiftAndBloodDungeonCount = 42
    Reset_ClearSpecificFindGiftAndBloodDungeonCount = 43
    Achieve_JoinRaidCount = 44
    Reset_JoinSpecificRaidCount = 45
    Achieve_JoinArenaCount = 46
    Reset_ArenaVictoryCount = 47
    Reset_RaidDamageAmountOnOneBattle = 48
    Reset_ClearEventStageCount = 49
    Reset_UseSpecificCharacterCount = 50
    Achieve_UseGold = 51
    Reset_UseTiket = 52
    Reset_ShopBuyCount = 53
    Reset_ShopBuyActionPointCount = 54
    Reset_SpecificCharacterAtSpecificFavorRank = 55
    Reset_ClearSpecificScenario = 56
    Reset_GetSpecificItemCount = 57
    Achieve_TotalGetClearStarCount = 58
    Reset_CompleteCampaignStageMinimumTurn = 59
    Achieve_TotalLoginCount = 60
    Reset_LoginAtSpecificTime = 61
    Reset_CompleteFavorSchedule = 62
    Reset_CompleteFavorScheduleAtSpecificCharacter = 63
    Reset_GetMemoryLobbyCount = 64
    Reset_GetFurnitureGroupCount = 65
    Reset_AcademyLocationAtSpecificRank = 66
    Reset_ClearCampaignStageDifficultyNormal = 67
    Reset_ClearCampaignStageDifficultyHard = 68
    Achieve_ClearChaserDungeonCount = 69
    Reset_ClearSpecificChaserDungeonCount = 70
    Reset_GetCafeRank = 71
    Reset_SpecificStarCharacterCount = 72
    Reset_EventClearCampaignStageCount = 73
    Reset_EventClearSpecificCampaignStageCount = 74
    Reset_EventCompleteCampaignStageMinimumTurn = 75
    Reset_EventClearCampaignStageDifficultyNormal = 76
    Reset_EventClearCampaignStageDifficultyHard = 77
    Reset_ClearSpecificCampaignStageCount = 78
    Reset_GetItemWithTagCount = 79
    Reset_GetFurnitureWithTagCount = 80
    Reset_GetEquipmentWithTagCount = 81
    Reset_ClearCampaignStageTimeLimitFromSecond = 82
    Reset_ClearEventStageTimeLimitFromSecond = 83
    Reset_ClearRaidTimeLimitFromSecond = 84
    Reset_ClearBattleWithTagCount = 85
    Reset_ClearFindGiftAndBloodDungeonTimeLimitFromSecond = 86
    Reset_CompleteScheduleWithTagCount = 87
    Reset_ClearChaserDungeonTimeLimitFromSecond = 88
    Reset_GetTotalScoreRhythm = 89
    Reset_GetBestScoreRhythm = 90
    Reset_GetSpecificScoreRhythm = 91
    Reset_ClearStageRhythm = 92
    Reset_GetComboCountRhythm = 93
    Reset_GetFullComboRhythm = 94
    Reset_GetFeverCountRhythm = 95
    Reset_UseActionPoint = 96
    Achieve_ClearSchoolDungeonCount = 97
    Reset_ClearSchoolDungeonTimeLimitFromSecond = 98
    Reset_ClearSpecificSchoolDungeonCount = 99
    Reset_GetCriticalCountRhythm = 100
    Achieve_WeaponTranscendenceCount = 101
    Achieve_WeaponLevelUpCount = 102
    Reset_WeaponAtSpecificTranscendenceCount = 103
    Reset_WeaponAtSpecificLevelUpCount = 104
    Reset_BuyShopGoods = 105
    Reset_ClanLogin = 106
    Reset_AssistCharacterSetting = 107
    Reset_DailyMissionFulfill = 108
    Reset_SelectedMissionFulfill = 109
    Reset_TotalDamageToWorldRaid = 110
    Reset_JoinWorldRaidTypeNumber = 111
    Reset_JoinWorldRaidBattleWithTagCount = 112
    Reset_ClearWorldRaidTimeLimitFromSecond = 113
    Achieve_KillEnemyWithDecagrammatonSPOTagCount = 114
    Reset_ConquerTileCount = 115
    Reset_ConquerSpecificStepTileCount = 116
    Reset_ConquerSpecificStepTileAll = 117
    Reset_UpgradeConquestBaseTileCount = 118
    Reset_KillConquestBoss = 119
    Reset_ClearEventConquestTileTimeLimitFromSecond = 120
    Reset_DiceRaceUseDiceCount = 121
    Reset_DiceRaceFinishLapCount = 122
    Reset_FortuneGachaCount = 123
    Reset_FortuneGachaCountByGrade = 124
    Reset_ClearCountShooting = 125
    Reset_ClearSpecificStageShooting = 126
    Reset_ClearSpecificCharacterShooting = 127
    Reset_ClearSpecificSectionShooting = 128
    Achieve_JoinEliminateRaidCount = 129
    Reset_TBGCompleteRoundCount = 130
    Reset_CompleteStage = 131
    Reset_TBGClearSpecificThema = 132
    Reset_ClearGeneralChaserDungeonCount = 133
    Reset_ClearGeneralFindGiftAndBloodDungeonCount = 134
    Reset_ClearGeneralSchoolDungeonCount = 135
    Reset_JoinArenaCount = 136
    Reset_GetCafe2ndRank = 137
    Achieve_GetComfort2ndPoint = 138
    Reset_ClearSpecificTimeAttackDungeonCount = 139
    Reset_GetScoreTimeAttackDungeon = 140
    Reset_GetTotalScoreTimeAttackDungeon = 141
    Reset_JoinRaidCount = 142
    Reset_ClearTimeAttackDungeonCount = 143
    Reset_JoinEliminateRaidCount = 144
    Reset_FieldClearSpecificDate = 145
    Reset_FieldGetEvidenceCount = 146
    Reset_FieldMasteryLevel = 147
    Reset_TreasureCheckedCellCount = 148
    Reset_TreasureGetTreasureCount = 149
    Reset_TreasureRoundRefreshCount = 150
    Achieve_UseTicketCount = 151
    Reset_ClearMultiFloorRaidStage = 152
    Achieve_CharacterPotentialUpCount = 153
    Reset_CharacterPotentialUpCount = 154
    Reset_CharacterAtSpecificPotentialCount = 155
    Reset_PotentialAttackPowerAtSpecificLevel = 156
    Reset_PotentialMaxHPAtSpecificLevel = 157
    Reset_PotentialHealPowerAtSpecificLevel = 158
    Reset_DreamGetSpecificParameter = 159
    Reset_DreamGetSpecificScheduleCount = 160
    Reset_DreamGetScheduleCount = 161
    Reset_DreamGetEndingCount = 162
    Reset_DreamGetSpecificEndingCount = 163
    Reset_DreamGetCollectionScenarioCount = 164
    Reset_ClearCountDefense = 165
    Reset_ClearSpecificDefenseStage = 166
    Reset_ClearCharacterLimitDefense = 167
    Reset_ClearTimeLimitDefenseFromSecond = 168
    Reset_JoinMultiFloorRaidCount = 169
    Reset_GivePresentCharacterCount = 170
    Reset_CharacterInviteCount = 171
    Reset_RoadpuzzleTileCount = 172
    Reset_ClearSpecificRoundRoadpuzzle = 173
    Reset_ClearCountRoadpuzzle = 174
    Reset_CCGResultCount = 175
    Reset_CCGCompleteCount = 176
    Reset_CCGUseCostCount = 177
    Reset_CCGTotalDamageCount = 178
    Reset_CCGRetreatCount = 179
    Reset_CCGSkillWithTagCount = 180
    Reset_CCGActivatePerkCount = 181
    Reset_ClearMultiFloorRaid = 182
    Reset_DayCompleteMission = 183
    Reset_ConcentrationCardMatchCount = 184
    Reset_ConcentrationClearCount = 185
    Reset_WorldRaidSpecificBossClear = 186
    Reset_WorldRaidActivateCoreCount = 187
    Reset_WorldRaidActivateUSBCount = 188
    Reset_EnterUICount = 189

class MissionToastDisplayConditionType(IntEnum):
    Always = 0
    Complete = 1
    Never = 2

class GetStickerConditionType(IntEnum):
    None_ = 0
    Reset_StikcerGetCondition_AccountLevel = 1
    Reset_StickerGetCondition_ScenarioModeId = 2
    Reset_StickerGetCondition_EnemyKillCount = 3
    Reset_StickerGetCondition_GetItemCount = 4
    Reset_StickerGetCondition_BuyItemCount = 5
    Reset_StickerGetCondition_ScheduleRank = 6
    Reset_StickerGetCondition_Change_LobbyCharacter = 7
    Reset_StickerGetCondition_Cafe_Character_Visit_Count = 8
    Reset_StickerGetCondition_Cafe_Chracter_Invite_Count = 9
    Reset_StickerGetCondition_GetChracterCount = 10
    Reset_StickerGetCondition_Cafe_Furniture_Interaction = 11
    Reset_StickerGetCondition_GetFurniture = 12
    Reset_StickerGetCondition_SetFurniture = 13
    Reset_StickerGetCondition_GivePresentChracterCount = 14
    Reset_StickerGetCondition_GivePresentCount = 15
    Reset_StickerGetCondition_MomotalkStudentCount = 16
    Reset_StickerGetCondition_CombatwithCharacterCount = 17
    Reset_StickerGetCondition_GachaCharacterCount = 18
    Reset_StickerGetCondition_TouchLobbyCharacter = 19
    Reset_StickerGetCondition_UseCircleEmoticonCount = 20
    Reset_StickerGetCondition_CraftCount = 21
    Reset_StickerGetCondition_NormalStageClear = 22
    Reset_StickerGetCondition_NormalStageClear3Star = 23
    Reset_StickerGetCondition_HardStageClear = 24
    Reset_StickerGetCondition_HardStageClear3Star = 25
    Achieve_StikcerGetCondition_AccountLevel = 26
    Achieve_StickerGetCondition_ClearStageId = 27
    Achieve_StickerGetCondition_ScenarioModeId = 28
    Achieve_StickerGetCondition_EnemyKillCount = 29
    Achieve_StickerGetCondition_GetItemCount = 30
    Achieve_StickerGetCondition_BuyItemCount = 31
    Achieve_StickerGetCondition_ScheduleRank = 32
    Achieve_StickerGetCondition_Change_LobbyCharacter = 33
    Achieve_StickerGetCondition_Cafe_Character_Visit_Count = 34
    Achieve_StickerGetCondition_Cafe_Chracter_Invite_Count = 35
    Achieve_StickerGetCondition_GetChracterCount = 36
    Achieve_StickerGetCondition_Cafe_Furniture_Interaction = 37
    Achieve_StickerGetCondition_GetFurniture = 38
    Achieve_StickerGetCondition_SetFurniture = 39
    Achieve_StickerGetCondition_GivePresentChracterCount = 40
    Achieve_StickerGetCondition_GivePresentCount = 41
    Achieve_StickerGetCondition_MomotalkStudentCount = 42
    Achieve_StickerGetCondition_CombatwithCharacterCount = 43
    Achieve_StickerGetCondition_GachaCharacterCount = 44
    Achieve_StickerGetCondition_TouchLobbyCharacter = 45
    Achieve_StickerGetCondition_UseCircleEmoticonCount = 46
    Achieve_StickerGetCondition_CraftCount = 47
    Achieve_StickerGetCondition_NormalStageClear = 48
    Achieve_StickerGetCondition_NormalStageClear3Star = 49
    Achieve_StickerGetCondition_HardStageClear = 50
    Achieve_StickerGetCondition_HardStageClear3Star = 51
    Reset_StickerGetCondition_EnemyKillCountbyTag = 52
    Reset_StickerGetCondition_GetItemCountbyTag = 53
    Reset_StickerGetCondition_ClearCampaignOrEventStageCount = 54
    Reset_StickerGetCondition_CompleteCampaignStageMinimumTurn = 55
    Reset_StickerGetCondition_ClearCampaignStageDifficultyNormal = 56
    Reset_StickerGetCondition_ClearCampaignStageDifficultyHard = 57
    Reset_StickerGetCondition_EventClearCampaignStageCount = 58
    Reset_StickerGetCondition_EventClearSpecificCampaignStageCount = 59
    Reset_StickerGetCondition_EventCompleteCampaignStageMinimumTurn = 60
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyNormal = 61
    Reset_StickerGetCondition_EventClearCampaignStageDifficultyHard = 62
    Reset_StickerGetCondition_ClearSpecificCampaignStageCount = 63
    Reset_StickerGetCondition_ClearCampaignStageTimeLimitFromSecond = 64
    Reset_StickerGetCondition_ClearEventStageTimeLimitFromSecond = 65
    Reset_StickerGetCondition_ClearStageRhythm = 66
    Reset_StickerGetCondition_ClearSpecificStageShooting = 67
    Reset_StickerGetCondition_CompleteStage = 68
    Achieve_StickerGetCondition_ClearCampaignStageCount = 69
    Achieve_StickerGetCondition_ClearChaserDungeonCount = 70
    Reset_StickerGetCondition_ClearSpecificChaserDungeonCount = 71
    Achieve_StickerGetCondition_ClearSchoolDungeonCount = 72
    Reset_StickerGetCondition_ClearSpecificSchoolDungeonCount = 73
    Reset_StickerGetCondition_ClearSpecificWeekDungeonCount = 74
    Achieve_StickerGetCondition_ClearFindGiftAndBloodDungeonCount = 75

class StickerCheckPassType(IntEnum):
    None_ = 0
    ClearScenarioModeId = 1
    ClearCampaignStageId = 2

class MissionCompleteUIPrefabType(IntEnum):
    None_ = 0
    UIStageSelect = 1
    UIAcademyLobby = 2
    UIArena = 3
    UIRaidLobby = 4
    UICafe = 5
    UIShop = 6
    UIGacha = 7
    UIScenarioMode = 8
    UICharacterCollection = 9
    UIWeekDungeonLobby = 10
    UISchoolDungeonLobby = 11
    UIMultiFloorRaid_Lobby = 12
    UIWeekDungeonLobby_Chaser = 13
    UIEliminateRaidLobby = 14

class ConditionType(IntEnum):
    CompleteScenario = 0
    SaveCafePreset = 1
    AcademyMessage = 2
    ClearBattleWithinFrame = 3
    UseSameExSkill = 4
    RecruitPickupGacha = 5
    UnlockMaxStarGrade = 6
    EquipCharacterWeapon = 7
    StayMemorialLobby = 8
    OpenSeasonBirthdayPlayerDialog = 9
    AssistUsedByOther = 10
    EquipCharacterGear = 11
    CompleteTutorial = 12

class AchievementType(IntEnum):
    Unlock = 0
    Step = 1

class ParcelType(IntEnum):
    None_ = 0
    Character = 1
    Currency = 2
    Equipment = 3
    Item = 4
    GachaGroup = 5
    Product = 6
    Shop = 7
    MemoryLobby = 8
    AccountExp = 9
    CharacterExp = 10
    FavorExp = 11
    TSS = 12
    Furniture = 13
    ShopRefresh = 14
    LocationExp = 15
    Recipe = 16
    CharacterWeapon = 17
    ProductMonthly = 18
    CharacterGear = 19
    IdCardBackground = 20
    Emblem = 21
    Sticker = 22
    Costume = 23
    PossessionCheck = 24
    BattlePassExp = 25
    SelectedCharacter = 26
    UnSelectedCharacter = 27
    ProductBattlePass = 28
    ProductSelect = 29
    SNSPost = 30
    ProductDailyRecord = 31

class Rarity(IntEnum):
    N = 0
    R = 1
    SR = 2
    SSR = 3

class CurrencyTypes(IntEnum):
    Invalid = 0
    Gold = 1
    GemPaid = 2
    GemBonus = 3
    Gem = 4
    ActionPoint = 5
    AcademyTicket = 6
    ArenaTicket = 7
    RaidTicket = 8
    WeekDungeonChaserATicket = 9
    WeekDungeonFindGiftTicket = 10
    WeekDungeonBloodTicket = 11
    WeekDungeonChaserBTicket = 12
    WeekDungeonChaserCTicket = 13
    SchoolDungeonATicket = 14
    SchoolDungeonBTicket = 15
    SchoolDungeonCTicket = 16
    TimeAttackDungeonTicket = 17
    MasterCoin = 18
    WorldRaidTicketA = 19
    WorldRaidTicketB = 20
    WorldRaidTicketC = 21
    ChaserTotalTicket = 22
    SchoolDungeonTotalTicket = 23
    EliminateTicketA = 24
    EliminateTicketB = 25
    EliminateTicketC = 26
    EliminateTicketD = 27
    CafeSummonTicket1 = 28
    CafeSummonTicket2 = 29
    Max = 30

class CurrencyOverChargeType(IntEnum):
    CanNotCharge = 0
    FitToLimit = 1
    ChargeOverLimit = 2

class CurrencyAdditionalChargeType(IntEnum):
    EnableAutoChargeOverLimit = 0
    DisableAutoChargeOverLimit = 1

class RecipeType(IntEnum):
    None_ = 0
    Craft = 1
    SkillLevelUp = 2
    CharacterTranscendence = 3
    EquipmentTierUp = 4
    CafeRankUp = 5
    SelectionItem = 6
    WeaponTranscendence = 7
    SelectRecruit = 8
    CharacterPotential = 9

class GachaGroupType(IntEnum):
    None_ = 0
    Reward_General = 1
    System_Craft = 2
    Reward_Pack = 3

class ConsumeCondition(IntEnum):
    And = 0
    Or = 1

class DailyRefillType(IntEnum):
    None_ = 0
    Default = 1
    Login = 2

class ScenarioBGType(IntEnum):
    None_ = 0
    Image = 1
    BlurRT = 2
    Spine = 3
    Hide = 4

class ScenarioCharacterAction(IntEnum):
    Idle = 0
    Shake = 1
    Greeting = 2
    FalldownLeft = 3
    FalldownRight = 4
    Stiff = 5
    Hophop = 6
    Jump = 7

class ScenarioCharacterShapes(IntEnum):
    None_ = 0
    Signal = 1
    BlackSilhouette = 2
    Closeup = 3
    Highlight = 4
    WhiteSilhouette = 5
    Glitch = 6

class ScenarioBGScroll(IntEnum):
    None_ = 0
    Vertical = 1
    Horizontal = 2

class DialogCategory(IntEnum):
    Cafe = 0
    Echelon = 1
    CharacterSSRNew = 2
    CharacterGet = 3
    Birthday = 4
    Dating = 5
    Title = 6
    UILobby = 7
    UILobbySpecial = 8
    UIShop = 9
    UIGacha = 10
    UIRaidLobby = 11
    UIWork = 12
    UITitle = 13
    UIWeekDungeon = 14
    UIAcademyLobby = 15
    UIRaidLobbySeasonOff = 16
    UIRaidLobbySeasonOn = 17
    UIWorkAronaSit = 18
    UIWorkAronaSleep = 19
    UIWorkAronaWatch = 20
    UIGuideMission = 21
    UILobby2 = 22
    UIClanSearchList = 23
    UIAttendance = 24
    UIAttendanceEvent01 = 25
    UIEventLobby = 26
    UIEventShop = 27
    UIEventBoxGachaShop = 28
    UIAttendanceEvent02 = 29
    UIAttendanceEvent03 = 30
    UIEventCardShop = 31
    UISchoolDungeon = 32
    UIAttendanceEvent = 33
    UISpecialOperationLobby = 34
    WeaponGet = 35
    UIAttendanceEvent04 = 36
    UIEventFortuneGachaShop = 37
    UIAttendanceEvent05 = 38
    UIAttendanceEvent06 = 39
    UIMission = 40
    UIEventMission = 41
    UIAttendanceEvent08 = 42
    UIAttendanceEvent07 = 43
    UIEventMiniGameMission = 44
    UIAttendanceEvent09 = 45
    UIAttendanceEvent10 = 46
    UIAttendanceEvent11 = 47
    UIWorkPlanaSit = 48
    UIWorkPlanaUmbrella = 49
    UIWorkPlanaCabinet = 50
    UIWorkCoexist_AronaSleepSit = 51
    UIWorkCoexist_PlanaWatchSky = 52
    UIWorkCoexist_PlanaSitPeek = 53
    UIWorkCoexist_AronaSleepPeek = 54
    UIEventArchive = 55
    UIAttendanceEvent12 = 56
    UIAttendanceEvent13 = 57
    UIAttendanceEvent14 = 58
    GlobalAttendance01 = 59
    GlobalAttendance02 = 60
    GlobalAttendance03 = 61
    GlobalAttendance04 = 62
    GlobalAttendance05 = 63
    UIAttendanceEvent15 = 64
    UILobbySpecial2 = 65
    UIAttendanceEvent16 = 66
    UIEventTreasure = 67
    UIMultiFloorRaid = 68
    UIEventMiniGameDreamMaker = 69
    UIAttendanceEvent17 = 70
    UIAttendanceEvent18 = 71
    UIBattlePassLobby = 72
    UIBattlePassMission = 73
    UIAttendanceEvent19 = 74
    UIAttendanceEvent20 = 75
    UIAttendanceEvent21 = 76
    UIEventClueSearch = 77
    UIWorkAronaWatering = 78
    UIWorkCoexist_PlanaWatchPot = 79

class DialogCondition(IntEnum):
    Idle = 0
    Enter = 1
    Exit = 2
    Buy = 3
    SoldOut = 4
    BoxGachaNormal = 5
    BoxGachaPrize = 6
    Prize0 = 7
    Prize1 = 8
    Prize2 = 9
    Prize3 = 10
    Interaction = 11
    Luck0 = 12
    Luck1 = 13
    Luck2 = 14
    Luck3 = 15
    Luck4 = 16
    Luck5 = 17
    StoryOpen = 18
    CollectionOpen = 19
    BoxGachaFinish = 20
    FindTreasure = 21
    GetTreasure = 22
    RoundRenewal = 23
    MiniGameDreamMakerEnough01 = 24
    MiniGameDreamMakerEnough02 = 25
    MiniGameDreamMakerEnough03 = 26
    MiniGameDreamMakerEnough04 = 27
    MiniGameDreamMakerDefault = 28
    PassLevelUp = 29
    UnlockPassReward = 30
    ClueSearch = 31
    ClueRegistration = 32
    ClueCompletion = 33

class DialogConditionDetail(IntEnum):
    None_ = 0
    Day = 1
    Close = 2
    MiniGameDreamMakerDay = 3
    PassLevel = 4

class DialogType(IntEnum):
    Talk = 0
    Think = 1
    UITalk = 2

class Anniversary(IntEnum):
    None_ = 0
    UserBDay = 1
    StudentBDay = 2

class School(IntEnum):
    None_ = 0
    Hyakkiyako = 1
    RedWinter = 2
    Trinity = 3
    Gehenna = 4
    Abydos = 5
    Millennium = 6
    Arius = 7
    Shanhaijing = 8
    Valkyrie = 9
    WildHunt = 10
    SRT = 11
    SCHALE = 12
    ETC = 13
    Tokiwadai = 14
    Sakugawa = 15
    Highlander = 16

class StoryCondition(IntEnum):
    Open = 0
    Locked = 1
    ComingSoon = 2
    Hide = 3

class EmojiEvent(IntEnum):
    EnterConver = 0
    EnterShelter = 1
    SignalLeader = 2
    Nice = 3
    Reload = 4
    Blind = 5
    Panic = 6
    Silence = 7
    NearyDead = 8
    Run = 9
    TerrainAdaptionS = 10
    TerrainAdaptionA = 11
    TerrainAdaptionB = 12
    TerrainAdaptionC = 13
    TerrainAdaptionD = 14
    TerrainAdaptionSS = 15
    Dot = 16
    Angry = 17
    Bulb = 18
    Exclaim = 19
    Surprise = 20
    Sad = 21
    Sigh = 22
    Steam = 23
    Upset = 24
    Respond = 25
    Question = 26
    Sweat = 27
    Music = 28
    Chat = 29
    Twinkle = 30
    Zzz = 31
    Tear = 32
    Heart = 33
    Shy = 34
    Think = 35

class ScenarioModeTypes(IntEnum):
    None_ = 0
    Main = 1
    Sub = 2
    Replay = 3
    Mini = 4
    SpecialOperation = 5
    Prologue = 6

class ScenarioModeSubTypes(IntEnum):
    None_ = 0
    Club = 1
    Series1 = 2
    Series2 = 3

class ScenarioModeReplayTypes(IntEnum):
    None_ = 0
    Event = 1
    Favor = 2
    Work = 3
    EventMeetup = 4

class ScenarioZoomAnchors(IntEnum):
    Center = 0
    LeftTop = 1
    LeftBottom = 2
    RightTop = 3
    RightBottom = 4

class ScenarioZoomType(IntEnum):
    Instant = 0
    Slide = 1

class ScenarioContentType(IntEnum):
    Prologue = 0
    WeekDungeon = 1
    Raid = 2
    Arena = 3
    Favor = 4
    Shop = 5
    EventContent = 6
    Craft = 7
    Chaser = 8
    EventContentMeetup = 9
    TimeAttack = 10
    Mission = 11
    EventContentPermanentPrologue = 12
    EventContentReturnSeason = 13
    MiniEvent = 14
    EliminateRaid = 15
    MultiFloorRaid = 16
    EventContentPermanent = 17

class MemoryLobbyCategory(IntEnum):
    None_ = 0
    UILobbySpecial = 1
    UILobbySpecial2 = 2

class PurchaseCountResetType(IntEnum):
    None_ = 0
    Day = 1
    Week = 2
    Month = 3

class ShopGroupType(IntEnum):
    None_ = 0
    General = 1
    SecretStone = 2
    Raid = 3
    Arena = 4
    MasterCoin = 5
    SecretStoneGrowth = 6
    TimeAttack = 7
    EliminateRaid = 8
    Gem = 9
    Chaser = 10

class StoreType(IntEnum):
    None_ = 0
    GooglePlay = 1
    AppStore = 2
    OneStore = 3
    MicrosoftStore = 4
    GalaxyStore = 5
    STEAM = 6
    FreeProduct = 7
    Twitch = 8
    Chzzk = 9
    PaymentCenter = 10
    PCStore = 11

class PurchasePeriodType(IntEnum):
    None_ = 0
    Day = 1
    Week = 2
    Month = 3

class PurchaseSourceType(IntEnum):
    None_ = 0
    Product = 1
    ProductMonthly = 2
    ProductBattlePass = 3
    ProductSelect = 4
    ProductGooglePoint = 5
    ProductDailyRecord = 6

class ProductCategory(IntEnum):
    None_ = 0
    Gem = 1
    Monthly = 2
    Package = 3
    GachaDirect_DontUseGlobal = 4
    TimeLimit = 5
    BattlePass = 6
    GooglePoint = 7
    DailyRecord = 8

class ProductDisplayTag(IntEnum):
    None_ = 0
    New = 1
    Hot = 2
    Sale = 3
    Limited = 4
    Free = 5

class ProductTagType(IntEnum):
    Monthly = 0
    Weekly = 1
    Biweekly = 2

class ShopFreeRecruitType(IntEnum):
    None_ = 0
    Accumulation = 1
    Reset = 2

class GachaDisplayTag(IntEnum):
    None_ = 0
    Limited = 1
    TwoStar = 2
    ThreeStar = 3
    Free = 4
    New = 5
    Fes = 6
    SelectRecruit = 7
    LimitedThreeStar = 8
    Revival = 9
    SelectLimited = 10
    NewbieDateLimited = 11

class ShopFilterType(IntEnum):
    GachaTicket = 0
    SecretStone = 1
    SecretStone_1 = 2
    SkillBook_Ultimate = 3
    ExSkill = 4
    SkillBook = 5
    Craft = 6
    AP = 7
    CharacterExpItem = 8
    Equip = 9
    Material = 10
    Creddit = 11
    Furniture = 12
    SelectItem = 13
    Currency = 14
    Hyakkiyako = 15
    RedWinter = 16
    Trinity = 17
    Gehenna = 18
    Abydos = 19
    Millennium = 20
    Arius = 21
    Shanhaijing = 22
    Valkyrie = 23
    WildHunt = 24
    Event = 25
    ChaserTotalTicket = 26
    SchoolTotalTicket = 27
    SRT = 28
    Highlander = 29
    ShopFilterDUMMY_3 = 30
    ShopFilterDUMMY_4 = 31
    ShopFilterDUMMY_5 = 32
    ShopFilterDUMMY_6 = 33
    ShopFilterDUMMY_7 = 34
    ETC = 35
    Bundle = 36
    FavorItem = 37

class ShopRefresherType(IntEnum):
    None_ = 0
    User = 1
    Server = 2

class ShopRefreshPeriodType(IntEnum):
    None_ = 0
    Day = 1
    Week = 2
    Month = 3

class ShopPurchasePopupType(IntEnum):
    None_ = 0
    Bundle = 1
    Piece = 2

class ProductSaleType(IntEnum):
    Limited = 0
    SaleDay = 1

class ProductSelectSubType(IntEnum):
    Select = 0
    AutoSelect = 1

class AutoSelectPopupType(IntEnum):
    None_ = 0
    FavorItem = 1
    GrowthItem = 2

class AccountState(IntEnum):
    WaitingSignIn = 0
    Normal = 1
    Dormant = 2
    Comeback = 3
    Newbie = 4

class MessagePopupLayout(IntEnum):
    TextOnly = 0
    ImageBig = 1
    ImageSmall = 2
    UnlockCondition = 3

class MessagePopupImagePositionType(IntEnum):
    ImageFirst = 0
    TextFirst = 1

class MessagePopupButtonType(IntEnum):
    Accept = 0
    Cancel = 1
    Command = 2

class ToastType(IntEnum):
    None_ = 0
    Tactic_Left = 1
    Tactic_Right = 2
    Social_Center = 3
    Social_Mission = 4
    Social_Right = 5
    Notice_Center = 6
    PC_LeftCenter = 7

class TargetGroup(IntEnum):
    WaitingSignIn = 0
    Normal = 1
    Dormant = 2
    Comeback = 3
    Newbie = 4

class StrategyAIType(IntEnum):
    None_ = 0
    Guard = 1
    Pursuit = 2

class StageDifficulty(IntEnum):
    None_ = 0
    Normal = 1
    Hard = 2
    VeryHard = 3
    VeryHard_Ex = 4

class HexaUnitGrade(IntEnum):
    Grade1 = 0
    Grade2 = 1
    Grade3 = 2
    Boss = 3

class TacticEnvironment(IntEnum):
    None_ = 0
    WarFog = 1

class StrategyObjectType(IntEnum):
    None_ = 0
    Start = 1
    Heal = 2
    Skill = 3
    StatBuff = 4
    Parcel = 5
    ParcelOneTimePerAccount = 6
    Portal = 7
    PortalOneWayEnterance = 8
    PortalOneWayExit = 9
    Observatory = 10
    Beacon = 11
    BeaconOneTime = 12
    EnemySpawn = 13
    SwitchToggle = 14
    SwitchMovableWhenToggleOff = 15
    SwitchMovableWhenToggleOn = 16
    FixedStart01 = 17
    FixedStart02 = 18
    FixedStart03 = 19
    FixedStart04 = 20

class StrategyEnvironment(IntEnum):
    None_ = 0
    MapFog = 1

class Tag(IntEnum):
    A = 0
    a = 1
    B = 2
    b = 3
    C = 4
    c = 5
    D = 6
    d = 7
    E = 8
    e = 9
    F = 10
    f = 11
    G = 12
    g = 13
    H = 14
    h = 15
    I = 16
    i = 17
    J = 18
    j = 19
    K = 20
    k = 21
    L = 22
    l = 23
    M = 24
    m = 25
    N = 26
    n = 27
    O = 28
    o = 29
    P = 30
    p = 31
    Q = 32
    q = 33
    R = 34
    r = 35
    S = 36
    s = 37
    T = 38
    t = 39
    U = 40
    u = 41
    V = 42
    v = 43
    W = 44
    w = 45
    X = 46
    x = 47
    Y = 48
    y = 49
    Z = 50
    z = 51
    aA = 52
    aa = 53
    aB = 54
    ab = 55
    aC = 56
    ac = 57
    aD = 58
    ad = 59
    aE = 60
    ae = 61
    aF = 62
    af = 63
    aG = 64
    ag = 65
    aH = 66
    ah = 67
    aI = 68
    ai = 69
    aJ = 70
    aj = 71
    aK = 72
    ak = 73
    aL = 74
    al = 75
    aM = 76
    am = 77
    aN = 78
    an = 79
    aO = 80
    ao = 81
    aP = 82
    ap = 83
    aQ = 84
    aq = 85
    aR = 86
    ar = 87
    aS = 88
    as_ = 89
    aT = 90
    at = 91
    aU = 92
    au = 93
    aV = 94
    av = 95
    aW = 96
    aw = 97
    aX = 98
    ax = 99
    aY = 100
    ay = 101
    aZ = 102
    az = 103
    BA = 104
    Ba = 105
    BB = 106
    Bb = 107
    BC = 108
    Bc = 109
    BD = 110
    Bd = 111
    BE = 112
    Be = 113
    BF = 114
    Bf = 115
    BG = 116
    Bg = 117
    BH = 118
    Bh = 119
    BI = 120
    Bi = 121
    BJ = 122
    Bj = 123
    BK = 124
    Bk = 125
    BL = 126
    Bl = 127
    BM = 128
    Bm = 129
    BN = 130
    Bn = 131
    BO = 132
    Bo = 133
    BP = 134
    Bp = 135
    BQ = 136
    Bq = 137
    BR = 138
    Br = 139
    BS = 140
    Bs = 141
    BT = 142
    Bt = 143
    BU = 144
    Bu = 145
    BV = 146
    Bv = 147
    BW = 148
    Bw = 149
    BX = 150
    Bx = 151
    BY = 152
    By = 153
    BZ = 154
    Bz = 155
    bA = 156
    ba = 157
    bB = 158
    bb = 159
    bC = 160
    bc = 161
    bD = 162
    bd = 163
    bE = 164
    be = 165
    bF = 166
    bf = 167
    bG = 168
    bg = 169
    bH = 170
    bh = 171
    bI = 172
    bi = 173
    bJ = 174
    bj = 175
    bK = 176
    bk = 177
    bL = 178
    bl = 179
    bM = 180
    bm = 181
    bN = 182
    bn = 183
    bO = 184
    bo = 185
    bP = 186
    bp = 187
    bQ = 188
    bq = 189
    bR = 190
    br = 191
    bS = 192
    bs = 193
    bT = 194
    bt = 195
    bU = 196
    bu = 197
    bV = 198
    bv = 199
    bW = 200
    bw = 201
    bX = 202
    bx = 203
    bY = 204
    by = 205
    bZ = 206
    bz = 207
    CA = 208
    Ca = 209
    CB = 210
    Cb = 211
    CC = 212
    Cc = 213
    CD = 214
    Cd = 215
    CE = 216
    Ce = 217
    CF = 218
    Cf = 219
    CG = 220
    Cg = 221
    CH = 222
    Ch = 223
    CI = 224
    Ci = 225
    CJ = 226
    Cj = 227
    CK = 228
    Ck = 229
    CL = 230
    Cl = 231
    CM = 232
    Cm = 233
    CN = 234
    Cn = 235
    CO = 236
    Co = 237
    CP = 238
    Cp = 239
    CQ = 240
    Cq = 241
    CR = 242
    Cr = 243
    CS = 244
    Cs = 245
    CT = 246
    Ct = 247
    CU = 248
    Cu = 249
    CV = 250
    Cv = 251
    CW = 252
    Cw = 253
    CX = 254
    Cx = 255
    CY = 256
    Cy = 257
    CZ = 258
    Cz = 259
    cA = 260
    ca = 261
    cB = 262
    cb = 263
    cC = 264
    cc = 265
    cD = 266
    cd = 267
    cE = 268
    ce = 269
    cF = 270
    cf = 271
    cG = 272
    cg = 273
    cH = 274
    ch = 275
    cI = 276
    ci = 277
    cJ = 278
    cj = 279
    cK = 280
    ck = 281
    cL = 282
    cl = 283
    cM = 284
    cm = 285
    cN = 286
    cn = 287
    cO = 288
    co = 289
    cP = 290
    cp = 291
    cQ = 292
    cq = 293
    cR = 294
    cr = 295
    cS = 296
    cs = 297
    cT = 298
    ct = 299
    cU = 300
    cu = 301
    cV = 302
    cv = 303
    cW = 304
    cw = 305
    cX = 306
    cx = 307
    cY = 308
    cy = 309
    cZ = 310
    cz = 311
    DA = 312
    Da = 313
    DB = 314
    Db = 315
    DC = 316
    Dc = 317
    DD = 318
    Dd = 319
    DE = 320
    De = 321
    DF = 322
    Df = 323
    DG = 324
    Dg = 325
    DH = 326
    Dh = 327
    DI = 328
    Di = 329
    DJ = 330
    Dj = 331
    DK = 332
    Dk = 333
    DL = 334
    Dl = 335
    DM = 336
    Dm = 337
    DN = 338
    Dn = 339
    DO = 340
    Do = 341
    DP = 342
    Dp = 343
    DQ = 344
    Dq = 345
    DR = 346
    Dr = 347
    DS = 348
    Ds = 349
    DT = 350
    Dt = 351
    DU = 352
    Du = 353
    DV = 354
    Dv = 355
    DW = 356
    Dw = 357
    DX = 358
    Dx = 359
    DY = 360
    Dy = 361
    DZ = 362
    Dz = 363
    dA = 364
    da = 365
    dB = 366
    db = 367
    dC = 368
    dc = 369
    dD = 370
    dd = 371
    dE = 372
    de = 373
    dF = 374
    df = 375
    dG = 376
    dg = 377
    dH = 378
    dh = 379
    dI = 380
    di = 381
    dJ = 382
    dj = 383
    dK = 384
    dk = 385
    dL = 386
    dl = 387
    dM = 388
    dm = 389
    dN = 390
    dn = 391
    dO = 392
    do = 393
    dP = 394
    dp = 395
    dQ = 396
    dq = 397
    dR = 398
    dr = 399
    dS = 400
    ds = 401
    dT = 402
    dt = 403
    dU = 404
    du = 405
    dV = 406
    dv = 407
    dW = 408
    dw = 409
    dX = 410
    dx = 411
    dY = 412
    dy = 413
    dZ = 414
    dz = 415
    EA = 416
    Ea = 417
    EB = 418
    Eb = 419
    EC = 420
    Ec = 421
    ED = 422
    Ed = 423
    EE = 424
    Ee = 425
    EF = 426
    Ef = 427
    EG = 428
    Eg = 429
    EH = 430
    Eh = 431
    EI = 432
    Ei = 433
    EJ = 434
    Ej = 435
    EK = 436
    Ek = 437
    EL = 438
    El = 439
    EM = 440
    Em = 441
    EN = 442
    En = 443
    EO = 444
    Eo = 445
    EP = 446
    Ep = 447
    EQ = 448
    Eq = 449
    ER = 450
    Er = 451
    ES = 452
    Es = 453
    ET = 454
    Et = 455
    EU = 456
    Eu = 457
    EV = 458
    Ev = 459
    EW = 460
    Ew = 461
    EX = 462
    Ex = 463
    EY = 464
    Ey = 465
    EZ = 466
    Ez = 467
    eA = 468
    ea = 469
    eB = 470
    eb = 471
    eC = 472
    ec = 473
    eD = 474
    ed = 475
    eE = 476
    ee = 477
    eF = 478
    ef = 479
    eG = 480
    eg = 481
    eH = 482
    eh = 483
    eI = 484
    ei = 485
    eJ = 486
    ej = 487
    eK = 488
    ek = 489
    eL = 490
    el = 491
    eM = 492
    em = 493
    eN = 494
    en = 495
    eO = 496
    eo = 497
    eP = 498
    ep = 499
    eQ = 500
    eq = 501
    eR = 502
    er = 503
    eS = 504
    es = 505
    eT = 506
    et = 507
    eU = 508
    eu = 509
    eV = 510
    ev = 511
    eW = 512
    ew = 513
    eX = 514
    ex = 515
    eY = 516
    ey = 517
    eZ = 518
    ez = 519
    FA = 520
    Fa = 521
    FB = 522
    Fb = 523
    FC = 524
    Fc = 525
    FD = 526
    Fd = 527
    FE = 528
    Fe = 529
    FF = 530
    Ff = 531
    FG = 532
    Fg = 533
    FH = 534
    Fh = 535
    FI = 536
    Fi = 537
    FJ = 538
    Fj = 539
    FK = 540
    Fk = 541
    FL = 542
    Fl = 543
    FM = 544
    Fm = 545
    FN = 546
    Fn = 547
    FO = 548
    Fo = 549
    FP = 550
    Fp = 551
    FQ = 552
    Fq = 553
    FR = 554
    Fr = 555
    FS = 556
    Fs = 557
    FT = 558
    Ft = 559
    FU = 560
    Fu = 561
    FV = 562
    Fv = 563
    FW = 564
    Fw = 565
    FX = 566
    Fx = 567
    FY = 568
    Fy = 569
    FZ = 570
    Fz = 571
    fA = 572
    fa = 573
    fB = 574
    fb = 575
    fC = 576
    fc = 577
    fD = 578
    fd = 579
    fE = 580
    fe = 581
    fF = 582
    ff = 583
    fG = 584
    fg = 585
    fH = 586
    fh = 587
    fI = 588
    fi = 589
    fJ = 590
    fj = 591
    fK = 592
    fk = 593
    fL = 594
    fl = 595
    fM = 596
    fm = 597
    fN = 598
    fn = 599
    fO = 600
    fo = 601
    fP = 602
    fp = 603
    fQ = 604
    fq = 605
    fR = 606
    fr = 607
    fS = 608
    fs = 609
    fT = 610
    ft = 611
    fU = 612
    fu = 613
    fV = 614
    fv = 615
    fW = 616
    fw = 617
    fX = 618
    fx = 619
    fY = 620
    fy = 621
    fZ = 622
    fz = 623
    GA = 624
    Ga = 625
    GB = 626
    Gb = 627
    GC = 628
    Gc = 629
    GD = 630
    Gd = 631
    GE = 632
    Ge = 633
    GF = 634
    Gf = 635
    GG = 636
    Gg = 637
    GH = 638
    Gh = 639
    GI = 640
    Gi = 641
    GJ = 642
    Gj = 643
    GK = 644
    Gk = 645
    GL = 646
    Gl = 647
    GM = 648
    Gm = 649
    GN = 650
    Gn = 651
    GO = 652
    Go = 653
    GP = 654
    Gp = 655
    GQ = 656
    Gq = 657
    GR = 658
    Gr = 659
    GS = 660
    Gs = 661
    GT = 662
    Gt = 663
    GU = 664
    Gu = 665
    GV = 666
    Gv = 667
    GW = 668
    Gw = 669
    GX = 670
    Gx = 671
    GY = 672
    Gy = 673
    GZ = 674
    Gz = 675
    gA = 676
    ga = 677
    gB = 678
    gb = 679
    gC = 680
    gc = 681
    gD = 682
    gd = 683
    gE = 684
    ge = 685
    gF = 686
    gf = 687
    gG = 688
    gg = 689
    gH = 690
    gh = 691
    gI = 692
    gi = 693
    gJ = 694
    gj = 695
    gK = 696
    gk = 697
    gL = 698
    gl = 699
    gM = 700
    gm = 701
    gN = 702
    gn = 703
    gO = 704
    go = 705
    gP = 706
    gp = 707
    gQ = 708
    gq = 709
    gR = 710
    gr = 711
    gS = 712
    gs = 713
    gT = 714
    gt = 715
    gU = 716
    gu = 717
    gV = 718
    gv = 719
    gW = 720
    gw = 721
    gX = 722
    gx = 723
    gY = 724
    gy = 725
    gZ = 726
    gz = 727
    HA = 728
    Ha = 729
    HB = 730
    Hb = 731
    HC = 732
    Hc = 733
    HD = 734
    Hd = 735
    HE = 736
    He = 737
    HF = 738
    Hf = 739
    HG = 740
    Hg = 741
    HH = 742
    Hh = 743
    HI = 744
    Hi = 745
    HJ = 746
    Hj = 747
    HK = 748
    Hk = 749
    HL = 750
    Hl = 751
    HM = 752
    Hm = 753
    HN = 754
    Hn = 755
    HO = 756
    Ho = 757
    HP = 758
    Hp = 759
    HQ = 760
    Hq = 761
    HR = 762
    Hr = 763
    HS = 764
    Hs = 765
    HT = 766
    Ht = 767
    HU = 768
    Hu = 769
    HV = 770
    Hv = 771
    HW = 772
    Hw = 773
    HX = 774
    Hx = 775
    HY = 776
    Hy = 777
    HZ = 778
    Hz = 779
    hA = 780
    ha = 781
    hB = 782
    hb = 783
    hC = 784
    hc = 785
    hD = 786
    hd = 787
    hE = 788
    he = 789
    hF = 790
    hf = 791
    hG = 792
    hg = 793
    hH = 794
    hh = 795
    hI = 796
    hi = 797
    hJ = 798
    hj = 799
    hK = 800
    hk = 801
    hL = 802
    hl = 803
    hM = 804
    hm = 805
    hN = 806
    hn = 807
    hO = 808
    ho = 809
    hP = 810
    hp = 811
    hQ = 812
    hq = 813
    hR = 814
    hr = 815
    hS = 816
    hs = 817
    hT = 818
    ht = 819
    hU = 820
    hu = 821
    hV = 822
    hv = 823
    hW = 824
    hw = 825
    hX = 826
    hx = 827
    hY = 828
    hy = 829
    hZ = 830
    hz = 831
    IA = 832
    Ia = 833
    IB = 834
    Ib = 835
    IC = 836
    Ic = 837
    ID = 838
    Id = 839
    IE = 840
    Ie = 841
    IF = 842
    If = 843
    IG = 844
    Ig = 845
    IH = 846
    Ih = 847
    II = 848
    Ii = 849
    IJ = 850
    Ij = 851
    IK = 852
    Ik = 853
    IL = 854
    Il = 855
    IM = 856
    Im = 857
    IN = 858
    In = 859
    IO = 860
    Io = 861
    IP = 862
    Ip = 863
    IQ = 864
    Iq = 865
    IR = 866
    Ir = 867
    IS = 868
    Is = 869
    IT = 870
    It = 871
    IU = 872
    Iu = 873
    IV = 874
    Iv = 875
    IW = 876
    Iw = 877
    IX = 878
    Ix = 879
    IY = 880
    Iy = 881
    IZ = 882
    Iz = 883
    iA = 884
    ia = 885
    iB = 886
    ib = 887
    iC = 888
    ic = 889
    iD = 890
    id = 891
    iE = 892
    ie = 893
    iF = 894
    if_ = 895
    iG = 896
    ig = 897
    iH = 898
    ih = 899
    iI = 900
    ii = 901
    iJ = 902
    ij = 903
    iK = 904
    ik = 905
    iL = 906
    il = 907
    iM = 908
    im = 909
    iN = 910
    in_ = 911
    iO = 912
    io = 913
    iP = 914
    ip = 915
    iQ = 916
    iq = 917
    iR = 918
    ir = 919
    iS = 920
    is_ = 921
    iT = 922
    it = 923
    iU = 924
    iu = 925
    iV = 926
    iv = 927
    iW = 928
    iw = 929
    iX = 930
    ix = 931
    iY = 932
    iy = 933
    iZ = 934
    iz = 935
    JA = 936
    Ja = 937
    JB = 938
    Jb = 939
    JC = 940
    Jc = 941
    JD = 942
    Jd = 943
    JE = 944
    Je = 945
    JF = 946
    Jf = 947
    JG = 948
    Jg = 949
    JH = 950
    Jh = 951
    JI = 952
    Ji = 953
    JJ = 954
    Jj = 955
    JK = 956
    Jk = 957
    JL = 958
    Jl = 959
    JM = 960
    Jm = 961
    JN = 962
    Jn = 963
    JO = 964
    Jo = 965
    JP = 966
    Jp = 967
    JQ = 968
    Jq = 969
    JR = 970
    Jr = 971
    JS = 972
    Js = 973
    JT = 974
    Jt = 975
    JU = 976
    Ju = 977
    JV = 978
    Jv = 979
    JW = 980
    Jw = 981
    JX = 982
    Jx = 983
    JY = 984
    Jy = 985
    JZ = 986
    Jz = 987
    jA = 988
    ja = 989
    jB = 990
    jb = 991
    jC = 992
    jc = 993
    jD = 994
    jd = 995
    jE = 996
    je = 997
    jF = 998
    jf = 999
    jG = 1000
    jg = 1001
    jH = 1002
    jh = 1003
    jI = 1004
    ji = 1005
    jJ = 1006
    jj = 1007
    jK = 1008
    jk = 1009
    jL = 1010
    jl = 1011
    jM = 1012
    jm = 1013
    jN = 1014
    jn = 1015
    jO = 1016
    jo = 1017
    jP = 1018
    jp = 1019
    jQ = 1020
    jq = 1021
    jR = 1022
    jr = 1023
    jS = 1024
    js = 1025
    jT = 1026
    jt = 1027
    jU = 1028
    ju = 1029
    jV = 1030
    jv = 1031
    jW = 1032
    jw = 1033
    jX = 1034
    jx = 1035
    jY = 1036
    jy = 1037
    jZ = 1038
    jz = 1039
    KA = 1040
    Ka = 1041
    KB = 1042
    Kb = 1043
    KC = 1044
    Kc = 1045
    KD = 1046
    Kd = 1047
    KE = 1048
    Ke = 1049
    KF = 1050
    Kf = 1051
    KG = 1052
    Kg = 1053
    KH = 1054
    Kh = 1055
    KI = 1056
    Ki = 1057
    KJ = 1058
    Kj = 1059
    KK = 1060
    Kk = 1061
    KL = 1062
    Kl = 1063
    KM = 1064
    Km = 1065
    KN = 1066
    Kn = 1067
    KO = 1068
    Ko = 1069
    KP = 1070
    Kp = 1071
    KQ = 1072
    Kq = 1073
    KR = 1074
    Kr = 1075
    KS = 1076
    Ks = 1077
    KT = 1078
    Kt = 1079
    KU = 1080
    Ku = 1081
    KV = 1082
    Kv = 1083
    KW = 1084
    Kw = 1085
    KX = 1086
    Kx = 1087
    KY = 1088
    Ky = 1089
    KZ = 1090
    Kz = 1091
    kA = 1092
    ka = 1093
    kB = 1094
    kb = 1095
    kC = 1096
    kc = 1097
    kD = 1098
    kd = 1099
    kE = 1100
    ke = 1101
    kF = 1102
    kf = 1103
    kG = 1104
    kg = 1105
    kH = 1106
    kh = 1107
    kI = 1108
    ki = 1109
    kJ = 1110
    kj = 1111
    kK = 1112
    kk = 1113
    kL = 1114
    kl = 1115
    kM = 1116
    km = 1117
    kN = 1118
    kn = 1119
    kO = 1120
    ko = 1121
    kP = 1122
    kp = 1123
    kQ = 1124
    kq = 1125
    kR = 1126
    kr = 1127
    kS = 1128
    ks = 1129
    kT = 1130
    kt = 1131
    kU = 1132
    ku = 1133
    kV = 1134
    kv = 1135
    kW = 1136
    kw = 1137
    kX = 1138
    kx = 1139
    kY = 1140
    ky = 1141
    kZ = 1142
    kz = 1143
    LA = 1144
    La = 1145
    LB = 1146
    Lb = 1147
    LC = 1148
    Lc = 1149
    LD = 1150
    Ld = 1151
    LE = 1152
    Le = 1153
    LF = 1154
    Lf = 1155
    LG = 1156
    Lg = 1157
    LH = 1158
    Lh = 1159
    LI = 1160
    Li = 1161
    LJ = 1162
    Lj = 1163
    LK = 1164
    Lk = 1165
    LL = 1166
    Ll = 1167
    LM = 1168
    Lm = 1169
    LN = 1170
    Ln = 1171
    LO = 1172
    Lo = 1173
    LP = 1174
    Lp = 1175
    LQ = 1176
    Lq = 1177
    LR = 1178
    Lr = 1179
    LS = 1180
    Ls = 1181
    LT = 1182
    Lt = 1183
    LU = 1184
    Lu = 1185
    LV = 1186
    Lv = 1187
    LW = 1188
    Lw = 1189
    LX = 1190
    Lx = 1191
    LY = 1192
    Ly = 1193
    LZ = 1194
    Lz = 1195
    lA = 1196
    la = 1197
    lB = 1198
    lb = 1199
    lC = 1200
    lc = 1201
    lD = 1202
    ld = 1203
    lE = 1204
    le = 1205
    lF = 1206
    lf = 1207
    lG = 1208
    lg = 1209
    lH = 1210
    lh = 1211
    lI = 1212
    li = 1213
    lJ = 1214
    lj = 1215
    lK = 1216
    lk = 1217
    lL = 1218
    ll = 1219
    lM = 1220
    lm = 1221
    lN = 1222
    ln = 1223
    lO = 1224
    lo = 1225
    lP = 1226
    lp = 1227
    lQ = 1228
    lq = 1229
    lR = 1230
    lr = 1231
    lS = 1232
    ls = 1233
    lT = 1234
    lt = 1235
    lU = 1236
    lu = 1237
    lV = 1238
    lv = 1239
    lW = 1240
    lw = 1241
    lX = 1242
    lx = 1243
    lY = 1244
    ly = 1245
    lZ = 1246
    lz = 1247
    MA = 1248
    Ma = 1249
    MB = 1250
    Mb = 1251
    MC = 1252
    Mc = 1253
    MD = 1254
    Md = 1255
    ME = 1256
    Me = 1257
    MF = 1258
    Mf = 1259
    MG = 1260
    Mg = 1261
    MH = 1262
    Mh = 1263
    MI = 1264
    Mi = 1265
    MJ = 1266
    Mj = 1267
    MK = 1268
    Mk = 1269
    ML = 1270
    Ml = 1271
    MM = 1272
    Mm = 1273
    MN = 1274
    Mn = 1275
    MO = 1276
    Mo = 1277
    MP = 1278
    Mp = 1279
    MQ = 1280
    Mq = 1281
    MR = 1282
    Mr = 1283
    MS = 1284
    Ms = 1285
    MT = 1286
    Mt = 1287
    MU = 1288
    Mu = 1289
    MV = 1290
    Mv = 1291
    MW = 1292
    Mw = 1293
    MX = 1294
    Mx = 1295
    MY = 1296
    My = 1297
    MZ = 1298
    Mz = 1299
    mA = 1300
    ma = 1301
    mB = 1302
    mb = 1303
    mC = 1304
    mc = 1305
    mD = 1306
    md = 1307
    mE = 1308
    me = 1309
    mF = 1310
    mf = 1311
    mG = 1312
    mg = 1313
    mH = 1314
    mh = 1315
    mI = 1316
    mi = 1317
    mJ = 1318
    mj = 1319
    mK = 1320
    mk = 1321
    mL = 1322
    ml = 1323
    mM = 1324
    mm = 1325
    mN = 1326
    mn = 1327
    mO = 1328
    mo = 1329
    mP = 1330
    mp = 1331
    mQ = 1332
    mq = 1333
    mR = 1334
    mr = 1335
    mS = 1336
    ms = 1337
    mT = 1338
    mt = 1339
    mU = 1340
    mu = 1341
    mV = 1342
    mv = 1343
    mW = 1344
    mw = 1345
    mX = 1346
    mx = 1347
    mY = 1348
    my = 1349
    mZ = 1350
    mz = 1351
    NA = 1352
    Na = 1353
    NB = 1354
    Nb = 1355
    NC = 1356
    Nc = 1357
    ND = 1358
    Nd = 1359
    NE = 1360
    Ne = 1361
    NF = 1362
    Nf = 1363
    NG = 1364
    Ng = 1365
    NH = 1366
    Nh = 1367
    NI = 1368
    Ni = 1369
    NJ = 1370
    Nj = 1371
    NK = 1372
    Nk = 1373
    NL = 1374
    Nl = 1375
    NM = 1376
    Nm = 1377
    NN = 1378
    Nn = 1379
    NO = 1380
    No = 1381
    NP = 1382
    Np = 1383
    NQ = 1384
    Nq = 1385
    NR = 1386
    Nr = 1387
    NS = 1388
    Ns = 1389
    NT = 1390
    Nt = 1391
    NU = 1392
    Nu = 1393
    NV = 1394
    Nv = 1395
    NW = 1396
    Nw = 1397
    NX = 1398
    Nx = 1399
    NY = 1400
    Ny = 1401
    NZ = 1402
    Nz = 1403
    nA = 1404
    na = 1405
    nB = 1406
    nb = 1407
    nC = 1408
    nc = 1409
    nD = 1410
    nd = 1411
    nE = 1412
    ne = 1413
    nF = 1414
    nf = 1415
    nG = 1416
    ng = 1417
    nH = 1418
    nh = 1419
    nI = 1420
    ni = 1421
    nJ = 1422
    nj = 1423
    nK = 1424
    nk = 1425
    nL = 1426
    nl = 1427
    nM = 1428
    nm = 1429
    nN = 1430
    nn = 1431
    nO = 1432
    no = 1433
    nP = 1434
    np = 1435
    nQ = 1436
    nq = 1437
    nR = 1438
    nr = 1439
    nS = 1440
    ns = 1441
    nT = 1442
    nt = 1443
    nU = 1444
    nu = 1445
    nV = 1446
    nv = 1447
    nW = 1448
    nw = 1449
    nX = 1450
    nx = 1451
    nY = 1452
    ny = 1453
    nZ = 1454
    nz = 1455
    OA = 1456
    Oa = 1457
    OB = 1458
    Ob = 1459
    OC = 1460
    Oc = 1461
    OD = 1462
    Od = 1463
    OE = 1464
    Oe = 1465
    OF = 1466
    Of = 1467
    OG = 1468
    Og = 1469
    OH = 1470
    Oh = 1471
    OI = 1472
    Oi = 1473
    OJ = 1474
    Oj = 1475
    OK = 1476
    Ok = 1477
    OL = 1478
    Ol = 1479
    OM = 1480
    Om = 1481
    ON = 1482
    On = 1483
    OO = 1484
    Oo = 1485
    OP = 1486
    Op = 1487
    OQ = 1488
    Oq = 1489
    OR = 1490
    Or = 1491
    OS = 1492
    Os = 1493
    OT = 1494
    Ot = 1495
    OU = 1496
    Ou = 1497
    OV = 1498
    Ov = 1499
    OW = 1500
    Ow = 1501
    OX = 1502
    Ox = 1503
    OY = 1504
    Oy = 1505
    OZ = 1506
    Oz = 1507
    oA = 1508
    oa = 1509
    oB = 1510
    ob = 1511
    oC = 1512
    oc = 1513
    oD = 1514
    od = 1515
    oE = 1516
    oe = 1517
    oF = 1518
    of = 1519
    oG = 1520
    og = 1521
    oH = 1522
    oh = 1523
    oI = 1524
    oi = 1525
    oJ = 1526
    oj = 1527
    oK = 1528
    ok = 1529
    oL = 1530
    ol = 1531
    oM = 1532
    om = 1533
    oN = 1534
    on = 1535
    oO = 1536
    oo = 1537
    oP = 1538
    op = 1539
    oQ = 1540
    oq = 1541
    oR = 1542
    or_ = 1543
    oS = 1544
    os = 1545
    oT = 1546
    ot = 1547
    oU = 1548
    ou = 1549
    oV = 1550
    ov = 1551
    oW = 1552
    ow = 1553
    oX = 1554
    ox = 1555
    oY = 1556
    oy = 1557
    oZ = 1558
    oz = 1559
    PA = 1560
    Pa = 1561
    PB = 1562
    Pb = 1563
    PC = 1564
    Pc = 1565
    PD = 1566
    Pd = 1567
    PE = 1568
    Pe = 1569
    PF = 1570
    Pf = 1571
    PG = 1572
    Pg = 1573
    PH = 1574
    Ph = 1575
    PI = 1576
    Pi = 1577
    PJ = 1578
    Pj = 1579
    PK = 1580
    Pk = 1581
    PL = 1582
    Pl = 1583
    PM = 1584
    Pm = 1585
    PN = 1586
    Pn = 1587
    PO = 1588
    Po = 1589
    PP = 1590
    Pp = 1591
    PQ = 1592
    Pq = 1593
    PR = 1594
    Pr = 1595
    PS = 1596
    Ps = 1597
    PT = 1598
    Pt = 1599
    PU = 1600
    Pu = 1601
    PV = 1602
    Pv = 1603
    PW = 1604
    Pw = 1605
    PX = 1606
    Px = 1607
    PY = 1608
    Py = 1609
    PZ = 1610
    Pz = 1611
    pA = 1612
    pa = 1613
    pB = 1614
    pb = 1615
    pC = 1616
    pc = 1617
    pD = 1618
    pd = 1619
    pE = 1620
    pe = 1621
    pF = 1622
    pf = 1623
    pG = 1624
    pg = 1625
    pH = 1626
    ph = 1627
    pI = 1628
    pi = 1629
    pJ = 1630
    pj = 1631
    pK = 1632
    pk = 1633
    pL = 1634
    pl = 1635
    pM = 1636
    pm = 1637
    pN = 1638
    pn = 1639
    pO = 1640
    po = 1641
    pP = 1642
    pp = 1643
    pQ = 1644
    pq = 1645
    pR = 1646
    pr = 1647
    pS = 1648
    ps = 1649
    pT = 1650
    pt = 1651
    pU = 1652
    pu = 1653
    pV = 1654
    pv = 1655
    pW = 1656
    pw = 1657
    pX = 1658
    px = 1659
    pY = 1660
    py = 1661
    pZ = 1662
    pz = 1663
    QA = 1664
    Qa = 1665
    QB = 1666
    Qb = 1667
    QC = 1668
    Qc = 1669
    QD = 1670
    Qd = 1671
    QE = 1672
    Qe = 1673
    QF = 1674
    Qf = 1675
    QG = 1676
    Qg = 1677
    QH = 1678
    Qh = 1679
    QI = 1680
    Qi = 1681
    QJ = 1682
    Qj = 1683
    QK = 1684
    Qk = 1685
    QL = 1686
    Ql = 1687
    QM = 1688
    Qm = 1689
    QN = 1690
    Qn = 1691
    QO = 1692
    Qo = 1693
    QP = 1694
    Qp = 1695
    QQ = 1696
    Qq = 1697
    QR = 1698
    Qr = 1699
    QS = 1700
    Qs = 1701
    QT = 1702
    Qt = 1703
    QU = 1704
    Qu = 1705
    QV = 1706
    Qv = 1707
    QW = 1708
    Qw = 1709
    QX = 1710
    Qx = 1711
    QY = 1712
    Qy = 1713
    QZ = 1714
    Qz = 1715
    qA = 1716
    qa = 1717
    qB = 1718
    qb = 1719
    qC = 1720
    qc = 1721
    qD = 1722
    qd = 1723
    qE = 1724
    qe = 1725
    qF = 1726
    qf = 1727
    qG = 1728
    qg = 1729
    qH = 1730
    qh = 1731
    qI = 1732
    qi = 1733
    qJ = 1734
    qj = 1735
    qK = 1736
    qk = 1737
    qL = 1738
    ql = 1739
    qM = 1740
    qm = 1741
    qN = 1742
    qn = 1743
    qO = 1744
    qo = 1745
    qP = 1746
    qp = 1747
    qQ = 1748
    qq = 1749
    qR = 1750
    qr = 1751
    qS = 1752
    qs = 1753
    qT = 1754
    qt = 1755
    qU = 1756
    qu = 1757
    qV = 1758
    qv = 1759
    qW = 1760
    qw = 1761
    qX = 1762
    qx = 1763
    qY = 1764
    qy = 1765
    qZ = 1766
    qz = 1767
    RA = 1768
    Ra = 1769
    RB = 1770
    Rb = 1771
    RC = 1772
    Rc = 1773
    RD = 1774
    Rd = 1775
    RE = 1776
    Re = 1777
    RF = 1778
    Rf = 1779
    RG = 1780
    Rg = 1781
    RH = 1782
    Rh = 1783
    RI = 1784
    Ri = 1785
    RJ = 1786
    Rj = 1787
    RK = 1788
    Rk = 1789
    RL = 1790
    Rl = 1791
    RM = 1792
    Rm = 1793
    RN = 1794
    Rn = 1795
    RO = 1796
    Ro = 1797
    RP = 1798
    Rp = 1799
    RQ = 1800
    Rq = 1801
    RR = 1802
    Rr = 1803
    RS = 1804
    Rs = 1805
    RT = 1806
    Rt = 1807
    RU = 1808
    Ru = 1809
    RV = 1810
    Rv = 1811
    RW = 1812
    Rw = 1813
    RX = 1814
    Rx = 1815
    RY = 1816
    Ry = 1817
    RZ = 1818
    Rz = 1819
    rA = 1820
    ra = 1821
    rB = 1822
    rb = 1823
    rC = 1824
    rc = 1825
    rD = 1826
    rd = 1827
    rE = 1828
    re = 1829
    rF = 1830
    rf = 1831
    rG = 1832
    rg = 1833
    rH = 1834
    rh = 1835
    rI = 1836
    ri = 1837
    rJ = 1838
    rj = 1839
    rK = 1840
    rk = 1841
    rL = 1842
    rl = 1843
    rM = 1844
    rm = 1845
    rN = 1846
    rn = 1847
    rO = 1848
    ro = 1849
    rP = 1850
    rp = 1851
    rQ = 1852
    rq = 1853
    rR = 1854
    rr = 1855
    rS = 1856
    rs = 1857
    rT = 1858
    rt = 1859
    rU = 1860
    ru = 1861
    rV = 1862
    rv = 1863
    rW = 1864
    rw = 1865
    rX = 1866
    rx = 1867
    rY = 1868
    ry = 1869
    rZ = 1870
    rz = 1871
    SA = 1872
    Sa = 1873
    SB = 1874
    Sb = 1875
    SC = 1876
    Sc = 1877
    SD = 1878
    Sd = 1879
    SE = 1880
    Se = 1881
    SF = 1882
    Sf = 1883
    SG = 1884
    Sg = 1885
    SH = 1886
    Sh = 1887
    SI = 1888
    Si = 1889
    SJ = 1890
    Sj = 1891
    SK = 1892
    Sk = 1893
    SL = 1894
    Sl = 1895
    SM = 1896
    Sm = 1897
    SN = 1898
    Sn = 1899
    SO = 1900
    So = 1901
    SP = 1902
    Sp = 1903
    SQ = 1904
    Sq = 1905
    SR = 1906
    Sr = 1907
    SS = 1908
    Ss = 1909
    ST = 1910
    St = 1911
    SU = 1912
    Su = 1913
    SV = 1914
    Sv = 1915
    SW = 1916
    Sw = 1917
    SX = 1918
    Sx = 1919
    SY = 1920
    Sy = 1921
    SZ = 1922
    Sz = 1923
    sA = 1924
    sa = 1925
    sB = 1926
    sb = 1927
    sC = 1928
    sc = 1929
    sD = 1930
    sd = 1931
    sE = 1932
    se = 1933
    sF = 1934
    sf = 1935
    sG = 1936
    sg = 1937
    sH = 1938
    sh = 1939
    sI = 1940
    si = 1941
    sJ = 1942
    sj = 1943
    sK = 1944
    sk = 1945
    sL = 1946
    sl = 1947
    sM = 1948
    sm = 1949
    sN = 1950
    sn = 1951
    sO = 1952
    so = 1953
    sP = 1954
    sp = 1955
    sQ = 1956
    sq = 1957
    sR = 1958
    sr = 1959
    sS = 1960
    ss = 1961
    sT = 1962
    st = 1963
    sU = 1964
    su = 1965
    sV = 1966
    sv = 1967
    sW = 1968
    sw = 1969
    sX = 1970
    sx = 1971
    sY = 1972
    sy = 1973
    sZ = 1974
    sz = 1975
    TA = 1976
    Ta = 1977
    TB = 1978
    Tb = 1979
    TC = 1980
    Tc = 1981
    TD = 1982
    Td = 1983
    TE = 1984
    Te = 1985
    TF = 1986
    Tf = 1987
    TG = 1988
    Tg = 1989
    TH = 1990
    Th = 1991
    TI = 1992
    Ti = 1993
    TJ = 1994
    Tj = 1995
    TK = 1996
    Tk = 1997
    TL = 1998
    Tl = 1999
    TM = 2000
    Tm = 2001
    TN = 2002
    Tn = 2003
    TO = 2004
    To = 2005
    TP = 2006
    Tp = 2007
    TQ = 2008
    Tq = 2009
    TR = 2010
    Tr = 2011
    TS = 2012
    Ts = 2013
    TT = 2014
    Tt = 2015
    TU = 2016
    Tu = 2017
    TV = 2018
    Tv = 2019
    TW = 2020
    Tw = 2021
    TX = 2022
    Tx = 2023
    TY = 2024
    Ty = 2025
    TZ = 2026
    Tz = 2027
    tA = 2028
    ta = 2029
    tB = 2030
    tb = 2031
    tC = 2032
    tc = 2033
    tD = 2034
    td = 2035
    tE = 2036
    te = 2037
    tF = 2038
    tf = 2039
    tG = 2040
    tg = 2041
    tH = 2042
    th = 2043
    tI = 2044
    ti = 2045
    tJ = 2046
    tj = 2047
    tK = 2048
    tk = 2049
    tL = 2050
    tl = 2051
    tM = 2052
    tm = 2053
    tN = 2054
    tn = 2055
    tO = 2056
    to = 2057
    tP = 2058
    tp = 2059
    tQ = 2060
    tq = 2061
    tR = 2062
    tr = 2063
    tS = 2064
    ts = 2065
    tT = 2066
    tt = 2067
    tU = 2068
    tu = 2069
    tV = 2070
    tv = 2071
    tW = 2072
    tw = 2073
    tX = 2074
    tx = 2075
    tY = 2076
    ty = 2077
    tZ = 2078
    tz = 2079
    UA = 2080
    Ua = 2081
    UB = 2082
    Ub = 2083
    UC = 2084
    Uc = 2085
    UD = 2086
    Ud = 2087
    UE = 2088
    Ue = 2089
    UF = 2090
    Uf = 2091
    UG = 2092
    Ug = 2093
    UH = 2094
    Uh = 2095
    UI = 2096
    Ui = 2097
    UJ = 2098
    Uj = 2099
    UK = 2100
    Uk = 2101
    UL = 2102
    Ul = 2103
    UM = 2104
    Um = 2105
    UN = 2106
    Un = 2107
    UO = 2108
    Uo = 2109
    UP = 2110
    Up = 2111
    UQ = 2112
    Uq = 2113
    UR = 2114
    Ur = 2115
    US = 2116
    Us = 2117
    UT = 2118
    Ut = 2119
    UU = 2120
    Uu = 2121
    UV = 2122
    Uv = 2123
    UW = 2124
    Uw = 2125
    UX = 2126
    Ux = 2127
    UY = 2128
    Uy = 2129
    UZ = 2130
    Uz = 2131
    uA = 2132
    ua = 2133
    uB = 2134
    ub = 2135
    uC = 2136
    uc = 2137
    uD = 2138
    ud = 2139
    uE = 2140
    ue = 2141
    uF = 2142
    uf = 2143
    uG = 2144
    ug = 2145
    uH = 2146
    uh = 2147
    uI = 2148
    ui = 2149
    uJ = 2150
    uj = 2151
    uK = 2152
    uk = 2153
    uL = 2154
    ul = 2155
    uM = 2156
    um = 2157
    uN = 2158
    un = 2159
    uO = 2160
    uo = 2161
    uP = 2162
    up = 2163
    uQ = 2164
    uq = 2165
    uR = 2166
    ur = 2167
    uS = 2168
    us = 2169
    uT = 2170
    ut = 2171
    uU = 2172
    uu = 2173
    uV = 2174
    uv = 2175
    uW = 2176
    uw = 2177
    uX = 2178
    ux = 2179
    uY = 2180
    uy = 2181
    uZ = 2182
    uz = 2183
    VA = 2184
    Va = 2185
    VB = 2186
    Vb = 2187
    VC = 2188
    Vc = 2189
    VD = 2190
    Vd = 2191
    VE = 2192
    Ve = 2193
    VF = 2194
    Vf = 2195
    VG = 2196
    Vg = 2197
    VH = 2198
    Vh = 2199
    VI = 2200
    Vi = 2201
    VJ = 2202
    Vj = 2203
    VK = 2204
    Vk = 2205
    VL = 2206
    Vl = 2207
    VM = 2208
    Vm = 2209
    VN = 2210
    Vn = 2211
    VO = 2212
    Vo = 2213
    VP = 2214
    Vp = 2215
    VQ = 2216
    Vq = 2217
    VR = 2218
    Vr = 2219
    VS = 2220
    Vs = 2221
    VT = 2222
    Vt = 2223
    VU = 2224
    Vu = 2225
    VV = 2226
    Vv = 2227
    VW = 2228
    Vw = 2229
    VX = 2230
    Vx = 2231
    VY = 2232
    Vy = 2233
    VZ = 2234
    Vz = 2235
    vA = 2236
    va = 2237
    vB = 2238
    vb = 2239
    vC = 2240
    vc = 2241
    vD = 2242
    vd = 2243
    vE = 2244
    ve = 2245
    vF = 2246
    vf = 2247
    vG = 2248
    vg = 2249
    vH = 2250
    vh = 2251
    vI = 2252
    vi = 2253
    vJ = 2254
    vj = 2255
    vK = 2256
    vk = 2257
    vL = 2258
    vl = 2259
    vM = 2260
    vm = 2261
    vN = 2262
    vn = 2263
    vO = 2264
    vo = 2265
    vP = 2266
    vp = 2267
    vQ = 2268
    vq = 2269
    vR = 2270
    vr = 2271
    vS = 2272
    vs = 2273
    vT = 2274
    vt = 2275
    vU = 2276
    vu = 2277
    vV = 2278
    vv = 2279
    vW = 2280
    vw = 2281
    vX = 2282
    vx = 2283
    vY = 2284
    vy = 2285
    vZ = 2286
    vz = 2287
    WA = 2288
    Wa = 2289
    WB = 2290
    Wb = 2291
    WC = 2292
    Wc = 2293
    WD = 2294
    Wd = 2295
    WE = 2296
    We = 2297
    WF = 2298
    Wf = 2299
    WG = 2300
    Wg = 2301
    WH = 2302
    Wh = 2303
    WI = 2304
    Wi = 2305
    WJ = 2306
    Wj = 2307
    WK = 2308
    Wk = 2309
    WL = 2310
    Wl = 2311
    WM = 2312
    Wm = 2313
    WN = 2314
    Wn = 2315
    WO = 2316
    Wo = 2317
    WP = 2318
    Wp = 2319
    WQ = 2320
    Wq = 2321
    WR = 2322
    Wr = 2323
    WS = 2324
    Ws = 2325
    WT = 2326
    Wt = 2327
    WU = 2328
    Wu = 2329
    WV = 2330
    Wv = 2331
    WW = 2332
    Ww = 2333
    WX = 2334
    Wx = 2335
    WY = 2336
    Wy = 2337
    WZ = 2338
    Wz = 2339
    wA = 2340
    wa = 2341
    wB = 2342
    wb = 2343
    wC = 2344
    wc = 2345
    wD = 2346
    wd = 2347
    wE = 2348
    we = 2349
    wF = 2350
    wf = 2351
    wG = 2352
    wg = 2353
    wH = 2354
    wh = 2355
    wI = 2356
    wi = 2357
    wJ = 2358
    wj = 2359
    wK = 2360
    wk = 2361
    wL = 2362
    wl = 2363
    wM = 2364
    wm = 2365
    wN = 2366
    wn = 2367
    wO = 2368
    wo = 2369
    wP = 2370
    wp = 2371
    wQ = 2372
    wq = 2373
    wR = 2374
    wr = 2375
    wS = 2376
    ws = 2377
    wT = 2378
    wt = 2379
    wU = 2380
    wu = 2381
    wV = 2382
    wv = 2383
    wW = 2384
    ww = 2385
    wX = 2386
    wx = 2387
    wY = 2388
    wy = 2389
    wZ = 2390
    wz = 2391
    XA = 2392
    Xa = 2393
    XB = 2394
    Xb = 2395
    XC = 2396
    Xc = 2397
    XD = 2398
    Xd = 2399
    XE = 2400
    Xe = 2401
    XF = 2402
    Xf = 2403
    XG = 2404
    Xg = 2405
    XH = 2406
    Xh = 2407
    XI = 2408
    Xi = 2409
    XJ = 2410
    Xj = 2411
    XK = 2412
    Xk = 2413
    XL = 2414
    Xl = 2415
    XM = 2416
    Xm = 2417
    XN = 2418
    Xn = 2419
    XO = 2420
    Xo = 2421
    XP = 2422
    Xp = 2423
    XQ = 2424
    Xq = 2425
    XR = 2426
    Xr = 2427
    XS = 2428
    Xs = 2429
    XT = 2430
    Xt = 2431
    XU = 2432
    Xu = 2433
    XV = 2434
    Xv = 2435
    XW = 2436
    Xw = 2437
    XX = 2438
    Xx = 2439
    XY = 2440
    Xy = 2441
    XZ = 2442
    Xz = 2443
    xA = 2444
    xa = 2445
    xB = 2446
    xb = 2447
    xC = 2448
    xc = 2449
    xD = 2450
    xd = 2451
    xE = 2452
    xe = 2453
    xF = 2454
    xf = 2455
    xG = 2456
    xg = 2457
    xH = 2458
    xh = 2459
    xI = 2460
    xi = 2461
    xJ = 2462
    xj = 2463
    xK = 2464
    xk = 2465
    xL = 2466
    xl = 2467
    xM = 2468
    xm = 2469
    xN = 2470
    xn = 2471
    xO = 2472
    xo = 2473
    xP = 2474
    xp = 2475
    xQ = 2476
    xq = 2477
    xR = 2478
    xr = 2479
    xS = 2480
    xs = 2481
    xT = 2482
    xt = 2483
    xU = 2484
    xu = 2485
    xV = 2486
    xv = 2487
    xW = 2488
    xw = 2489
    xX = 2490
    xx = 2491
    xY = 2492
    xy = 2493
    xZ = 2494
    xz = 2495
    YA = 2496
    Ya = 2497
    YB = 2498
    Yb = 2499
    YC = 2500
    Yc = 2501
    YD = 2502
    Yd = 2503
    YE = 2504
    Ye = 2505
    YF = 2506
    Yf = 2507
    YG = 2508
    Yg = 2509
    YH = 2510
    Yh = 2511
    YI = 2512
    Yi = 2513
    YJ = 2514
    Yj = 2515
    YK = 2516
    Yk = 2517
    YL = 2518
    Yl = 2519
    YM = 2520
    Ym = 2521
    YN = 2522
    Yn = 2523
    YO = 2524
    Yo = 2525
    YP = 2526
    Yp = 2527
    YQ = 2528
    Yq = 2529
    YR = 2530
    Yr = 2531
    YS = 2532
    Ys = 2533
    YT = 2534
    Yt = 2535
    YU = 2536
    Yu = 2537
    YV = 2538
    Yv = 2539
    YW = 2540
    Yw = 2541
    YX = 2542
    Yx = 2543
    YY = 2544
    Yy = 2545
    YZ = 2546
    Yz = 2547
    yA = 2548
    ya = 2549
    yB = 2550
    yb = 2551
    yC = 2552
    yc = 2553
    yD = 2554
    yd = 2555
    yE = 2556
    ye = 2557
    yF = 2558
    yf = 2559
    yG = 2560
    yg = 2561
    yH = 2562
    yh = 2563
    yI = 2564
    yi = 2565
    yJ = 2566
    yj = 2567
    yK = 2568
    yk = 2569
    yL = 2570
    yl = 2571
    yM = 2572
    ym = 2573
    yN = 2574
    yn = 2575
    yO = 2576
    yo = 2577
    yP = 2578
    yp = 2579
    yQ = 2580
    yq = 2581
    yR = 2582
    yr = 2583
    yS = 2584
    ys = 2585
    yT = 2586
    yt = 2587
    yU = 2588
    yu = 2589
    yV = 2590
    yv = 2591
    yW = 2592
    yw = 2593
    yX = 2594
    yx = 2595
    yY = 2596
    yy = 2597
    yZ = 2598
    yz = 2599
    ZA = 2600
    Za = 2601
    ZB = 2602
    Zb = 2603
    ZC = 2604
    Zc = 2605
    ZD = 2606
    Zd = 2607
    ZE = 2608
    Ze = 2609
    ZF = 2610
    Zf = 2611
    ZG = 2612
    Zg = 2613
    ZH = 2614
    Zh = 2615
    ZI = 2616
    Zi = 2617
    ZJ = 2618
    Zj = 2619
    ZK = 2620
    Zk = 2621
    ZL = 2622
    Zl = 2623
    ZM = 2624
    Zm = 2625
    ZN = 2626
    Zn = 2627
    ZO = 2628
    Zo = 2629
    ZP = 2630
    Zp = 2631
    ZQ = 2632
    Zq = 2633
    ZR = 2634
    Zr = 2635
    ZS = 2636
    Zs = 2637
    ZT = 2638
    Zt = 2639
    ZU = 2640
    Zu = 2641
    ZV = 2642
    Zv = 2643
    ZW = 2644
    Zw = 2645
    ZX = 2646
    Zx = 2647
    ZY = 2648
    Zy = 2649
    ZZ = 2650
    Zz = 2651
    zA = 2652
    za = 2653
    zB = 2654
    zb = 2655
    zC = 2656
    zc = 2657
    zD = 2658
    zd = 2659
    zE = 2660
    ze = 2661
    zF = 2662
    zf = 2663
    zG = 2664
    zg = 2665
    zH = 2666
    zh = 2667
    zI = 2668
    zi = 2669
    zJ = 2670
    zj = 2671
    zK = 2672
    zk = 2673
    zL = 2674
    zl = 2675
    zM = 2676
    zm = 2677
    zN = 2678
    zn = 2679
    zO = 2680
    zo = 2681
    zP = 2682
    zp = 2683
    zQ = 2684
    zq = 2685
    zR = 2686
    zr = 2687
    zS = 2688
    zs = 2689
    zT = 2690
    zt = 2691
    zU = 2692
    zu = 2693
    zV = 2694
    zv = 2695
    zW = 2696
    zw = 2697
    zX = 2698
    zx = 2699
    zY = 2700
    zy = 2701
    zZ = 2702
    zz = 2703
    aAA = 2704
    aAa = 2705
    aAB = 2706
    aAb = 2707
    aAC = 2708
    aAc = 2709
    aAD = 2710
    aAd = 2711
    aAE = 2712
    aAe = 2713
    aAF = 2714
    aAf = 2715
    aAG = 2716
    aAg = 2717
    aAH = 2718
    aAh = 2719
    aAI = 2720
    aAi = 2721
    aAJ = 2722
    aAj = 2723
    aAK = 2724
    aAk = 2725
    aAL = 2726
    aAl = 2727
    aAM = 2728
    aAm = 2729
    aAN = 2730
    aAn = 2731
    aAO = 2732
    aAo = 2733
    aAP = 2734
    aAp = 2735
    aAQ = 2736
    aAq = 2737
    aAR = 2738
    aAr = 2739
    aAS = 2740
    aAs = 2741
    aAT = 2742
    aAt = 2743
    aAU = 2744
    aAu = 2745
    aAV = 2746
    aAv = 2747
    aAW = 2748
    aAw = 2749
    aAX = 2750
    aAx = 2751
    aAY = 2752
    aAy = 2753
    aAZ = 2754
    aAz = 2755
    aaA = 2756
    aaa = 2757
    aaB = 2758
    aab = 2759
    aaC = 2760
    aac = 2761
    aaD = 2762
    aad = 2763
    aaE = 2764
    aae = 2765
    aaF = 2766
    aaf = 2767
    aaG = 2768
    aag = 2769
    aaH = 2770
    aah = 2771
    aaI = 2772
    aai = 2773
    aaJ = 2774
    aaj = 2775
    aaK = 2776
    aak = 2777
    aaL = 2778
    aal = 2779
    aaM = 2780
    aam = 2781
    aaN = 2782
    aan = 2783
    aaO = 2784
    aao = 2785
    aaP = 2786
    aap = 2787
    aaQ = 2788
    aaq = 2789
    aaR = 2790
    aar = 2791
    aaS = 2792
    aas = 2793
    aaT = 2794
    aat = 2795
    aaU = 2796
    aau = 2797
    aaV = 2798
    aav = 2799
    aaW = 2800
    aaw = 2801
    aaX = 2802
    aax = 2803
    aaY = 2804
    aay = 2805
    aaZ = 2806
    aaz = 2807
    aBA = 2808
    aBa = 2809
    aBB = 2810
    aBb = 2811
    aBC = 2812
    aBc = 2813
    aBD = 2814
    aBd = 2815
    aBE = 2816
    aBe = 2817
    aBF = 2818
    aBf = 2819
    aBG = 2820
    aBg = 2821
    aBH = 2822
    aBh = 2823
    aBI = 2824
    aBi = 2825
    aBJ = 2826
    aBj = 2827
    aBK = 2828
    aBk = 2829
    aBL = 2830
    aBl = 2831
    aBM = 2832
    aBm = 2833
    aBN = 2834
    aBn = 2835
    aBO = 2836
    aBo = 2837
    aBP = 2838
    aBp = 2839
    aBQ = 2840
    aBq = 2841
    aBR = 2842
    aBr = 2843
    aBS = 2844
    aBs = 2845
    aBT = 2846
    aBt = 2847
    aBU = 2848
    aBu = 2849
    aBV = 2850
    aBv = 2851
    aBW = 2852
    aBw = 2853
    aBX = 2854
    aBx = 2855
    aBY = 2856
    aBy = 2857
    aBZ = 2858
    aBz = 2859
    abA = 2860
    aba = 2861
    abB = 2862
    abb = 2863
    abC = 2864
    abc = 2865
    abD = 2866
    abd = 2867
    abE = 2868
    abe = 2869
    abF = 2870
    abf = 2871
    abG = 2872
    abg = 2873
    abH = 2874
    abh = 2875
    abI = 2876
    abi = 2877
    abJ = 2878
    abj = 2879
    abK = 2880
    abk = 2881
    abL = 2882
    abl = 2883
    abM = 2884
    abm = 2885
    abN = 2886
    abn = 2887
    abO = 2888
    abo = 2889
    abP = 2890
    abp = 2891
    abQ = 2892
    abq = 2893
    abR = 2894
    abr = 2895
    abS = 2896
    abs = 2897
    abT = 2898
    abt = 2899
    abU = 2900
    abu = 2901
    abV = 2902
    abv = 2903
    abW = 2904
    abw = 2905
    abX = 2906
    abx = 2907
    abY = 2908
    aby = 2909
    abZ = 2910
    abz = 2911
    aCA = 2912
    aCa = 2913
    aCB = 2914
    aCb = 2915
    aCC = 2916
    aCc = 2917
    aCD = 2918
    aCd = 2919
    aCE = 2920
    aCe = 2921
    aCF = 2922
    aCf = 2923
    aCG = 2924
    aCg = 2925
    aCH = 2926
    aCh = 2927
    aCI = 2928
    aCi = 2929
    aCJ = 2930
    aCj = 2931
    aCK = 2932
    aCk = 2933
    aCL = 2934
    aCl = 2935
    aCM = 2936
    aCm = 2937
    aCN = 2938
    aCn = 2939
    aCO = 2940
    aCo = 2941
    aCP = 2942
    aCp = 2943
    aCQ = 2944
    aCq = 2945
    aCR = 2946
    aCr = 2947
    aCS = 2948
    aCs = 2949
    aCT = 2950
    aCt = 2951
    aCU = 2952
    aCu = 2953
    aCV = 2954
    aCv = 2955
    aCW = 2956
    aCw = 2957
    aCX = 2958
    aCx = 2959
    aCY = 2960
    aCy = 2961
    aCZ = 2962
    aCz = 2963
    acA = 2964
    aca = 2965
    acB = 2966
    acb = 2967
    acC = 2968
    acc = 2969
    acD = 2970
    acd = 2971
    acE = 2972
    ace = 2973
    acF = 2974
    acf = 2975
    acG = 2976
    acg = 2977
    acH = 2978
    ach = 2979
    acI = 2980
    aci = 2981
    acJ = 2982
    acj = 2983
    acK = 2984
    ack = 2985
    acL = 2986
    acl = 2987
    acM = 2988
    acm = 2989
    acN = 2990
    acn = 2991
    acO = 2992
    aco = 2993
    acP = 2994
    acp = 2995
    acQ = 2996
    acq = 2997
    acR = 2998
    acr = 2999
    acS = 3000
    acs = 3001
    acT = 3002
    act = 3003

class Club(IntEnum):
    None_ = 0
    Engineer = 1
    CleanNClearing = 2
    KnightsHospitaller = 3
    IndeGEHENNA = 4
    IndeMILLENNIUM = 5
    IndeHyakkiyako = 6
    IndeShanhaijing = 7
    IndeTrinity = 8
    FoodService = 9
    Countermeasure = 10
    BookClub = 11
    MatsuriOffice = 12
    GourmetClub = 13
    HoukagoDessert = 14
    RedwinterSecretary = 15
    Schale = 16
    TheSeminar = 17
    AriusSqud = 18
    Justice = 19
    Fuuki = 20
    Kohshinjo68 = 21
    Meihuayuan = 22
    SisterHood = 23
    GameDev = 24
    anzenkyoku = 25
    RemedialClass = 26
    SPTF = 27
    TrinityVigilance = 28
    Veritas = 29
    TrainingClub = 30
    Onmyobu = 31
    Shugyobu = 32
    Endanbou = 33
    NinpoKenkyubu = 34
    Class227 = 35
    EmptyClub = 36
    Emergentology = 37
    RabbitPlatoon = 38
    PandemoniumSociety = 39
    HotSpringsDepartment = 40
    TeaParty = 41
    PublicPeaceBureau = 42
    Genryumon = 43
    BlackTortoisePromenade = 44
    LaborParty = 45
    KnowledgeLiberationFront = 46
    Hyakkayouran = 47
    ShinySparkleSociety = 48
    AbydosStudentCouncil = 49
    CentralControlCenter = 50
    FreightLogisticsDepartment = 51
    OccultClub = 52
    PrefectBrigade = 53
    FreeTradeCartel = 54
    NicomediasTroop = 55
    PublishingDepartment = 56
    FoxSquad = 57


def dump_Excel_AddressableBlackListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "FolderPath": [convert_string(excel_instance.FolderPathField(j), password) for j in range(excel_instance.FolderPathFieldLength())],
        "ResourcePath": [convert_string(excel_instance.ResourcePathField(j), password) for j in range(excel_instance.ResourcePathFieldLength())],
    }

def dump_Excel_AddressableWhiteListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "FolderPath": [convert_string(excel_instance.FolderPathField(j), password) for j in range(excel_instance.FolderPathFieldLength())],
        "ResourcePath": [convert_string(excel_instance.ResourcePathField(j), password) for j in range(excel_instance.ResourcePathFieldLength())],
    }

def dump_Excel_AnimationBlendTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataListLength": convert_int(excel_instance.DataListLengthField(), password),
    }

def dump_Excel_BlendData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Type": convert_int(excel_instance.TypeField(), password),
        "InfoList": [excel_instance.InfoListField(j) for j in range(excel_instance.InfoListFieldLength())],
    }

def dump_Excel_BlendInfo(excel_instance, password: bytes = b"") -> dict:
    return {
        "From": convert_int(excel_instance.FromField(), password),
        "To": convert_int(excel_instance.ToField(), password),
        "Blend": convert_float(excel_instance.BlendField(), password),
    }

def dump_Excel_AnimatorDataTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_AnimatorData(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_AnimatorData(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultStateName": convert_string(excel_instance.DefaultStateNameField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "DataList": [excel_instance.DataListField(j) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_AniStateData(excel_instance, password: bytes = b"") -> dict:
    return {
        "StateName": convert_string(excel_instance.StateNameField(), password),
        "StatePrefix": convert_string(excel_instance.StatePrefixField(), password),
        "StateNameWithPrefix": convert_string(excel_instance.StateNameWithPrefixField(), password),
        "Tag": convert_string(excel_instance.TagField(), password),
        "SpeedParameterName": convert_string(excel_instance.SpeedParameterNameField(), password),
        "SpeedParamter": convert_float(excel_instance.SpeedParamterField(), password),
        "StateSpeed": convert_float(excel_instance.StateSpeedField(), password),
        "ClipName": convert_string(excel_instance.ClipNameField(), password),
        "Length": convert_float(excel_instance.LengthField(), password),
        "FrameRate": convert_float(excel_instance.FrameRateField(), password),
        "IsLooping": bool(excel_instance.IsLoopingField()),
        "Events": [excel_instance.EventsField(j) for j in range(excel_instance.EventsFieldLength())],
    }

def dump_Excel_AniEventData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.NameField(), password),
        "Time": convert_float(excel_instance.TimeField(), password),
        "IntParam": convert_int(excel_instance.IntParamField(), password),
        "FloatParam": convert_float(excel_instance.FloatParamField(), password),
        "StringParam": convert_string(excel_instance.StringParamField(), password),
    }

def dump_Excel_BattleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [UnitType(convert_int(excel_instance.NoneField(j), password)).name for j in range(excel_instance.NoneFieldLength())],
        "Single": AttackType(convert_int(excel_instance.SingleField(), password)).name,
        "Guided": ProjectileType(convert_int(excel_instance.GuidedField(), password)).name,
        "Blue": DamageFontColor(convert_int(excel_instance.BlueField(), password)).name,
        "CoverEnter": EmoticonEvent(convert_int(excel_instance.CoverEnterField(), password)).name,
        "Normal": [BulletType(convert_int(excel_instance.NormalField(j), password)).name for j in range(excel_instance.NormalFieldLength())],
        "Crush": ActionType(convert_int(excel_instance.CrushField(), password)).name,
        "Able": BuffOverlap(convert_int(excel_instance.AbleField(), password)).name,
        "AllySelf": ReArrangeTargetType(convert_int(excel_instance.AllySelfField(), password)).name,
        "LightArmor": ArmorType(convert_int(excel_instance.LightArmorField(), password)).name,
        "Wood": EntityMaterialType(convert_int(excel_instance.WoodField(), password)).name,
        "All": [CoverMotionType(convert_int(excel_instance.AllField(j), password)).name for j in range(excel_instance.AllFieldLength())],
        "DISTANCE": TargetSortBy(convert_int(excel_instance.DISTANCEField(), password)).name,
        "CloseToObstacle": PositioningType(convert_int(excel_instance.CloseToObstacleField(), password)).name,
        "Students": [TacticEntityType(convert_int(excel_instance.StudentsField(j), password)).name for j in range(excel_instance.StudentsFieldLength())],
        "Sequence": ExternalBTNodeType(convert_int(excel_instance.SequenceField(), password)).name,
        "UseNextExSkill": ExternalBehavior(convert_int(excel_instance.UseNextExSkillField(), password)).name,
        "Student": TacticEntityType(convert_int(excel_instance.StudentField(), password)).name,
        "SearchAndMove": EngageType(convert_int(excel_instance.SearchAndMoveField(), password)).name,
        "Position": HitEffectPosition(convert_int(excel_instance.PositionField(), password)).name,
        "Street": StageTopography(convert_int(excel_instance.StreetField(), password)).name,
        "D": TerrainAdaptationStat(convert_int(excel_instance.DField(), password)).name,
        "MAIN": StageType(convert_int(excel_instance.MAINField(), password)).name,
        "Remain": ObstacleDestroyType(convert_int(excel_instance.RemainField(), password)).name,
        "Low": ObstacleHeightType(convert_int(excel_instance.LowField(), password)).name,
        "Resist": DamageAttribute(convert_int(excel_instance.ResistField(), password)).name,
        "Ally": SkillPriorityCheckTarget(convert_int(excel_instance.AllyField(), password)).name,
        "Main": StageType(convert_int(excel_instance.MainField(), password)).name,
        "TargetToCaster": KnockbackDirection(convert_int(excel_instance.TargetToCasterField(), password)).name,
        "Duration": EndCondition(convert_int(excel_instance.DurationField(), password)).name,
        "Preset": ArenaSimulatorServer(convert_int(excel_instance.PresetField(), password)).name,
        "FinalDamage": BattleCalculationStat(convert_int(excel_instance.FinalDamageField(), password)).name,
        "SpecialTransStat": StatTransType(convert_int(excel_instance.SpecialTransStatField(), password)).name,
        "Talk": BattleDialogType(convert_int(excel_instance.TalkField(), password)).name,
    }

def dump_Excel_BossPhaseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "AIPhase": convert_int(excel_instance.AIPhaseField(), password),
        "NormalAttackSkillUniqueName": convert_string(excel_instance.NormalAttackSkillUniqueNameField(), password),
        "UseExSkill": [bool(excel_instance.UseExSkillField(j)) for j in range(excel_instance.UseExSkillFieldLength())],
    }

def dump_Excel_BuffParticleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "UniqueName": convert_string(excel_instance.UniqueNameField(), password),
        "BuffType": convert_string(excel_instance.BuffTypeField(), password),
        "BuffName": convert_string(excel_instance.BuffNameField(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePathField(), password),
    }

def dump_Excel_CharacterDialogFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "Phase": convert_int(excel_instance.PhaseField(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndexField(), password),
        "DialogType": FieldDialogType(convert_int(excel_instance.DialogTypeField(), password)).name,
        "Duration": convert_int(excel_instance.DurationField(), password),
        "MotionName": convert_string(excel_instance.MotionNameField(), password),
        "IsInteractionDialog": bool(excel_instance.IsInteractionDialogField()),
        "HideUI": bool(excel_instance.HideUIField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
    }

def dump_Excel_CheatCodeListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CheatCode": [convert_string(excel_instance.CheatCodeField(j), password) for j in range(excel_instance.CheatCodeFieldLength())],
        "InputTitle": [convert_string(excel_instance.InputTitleField(j), password) for j in range(excel_instance.InputTitleFieldLength())],
        "Desc": convert_string(excel_instance.DescField(), password),
    }

def dump_Excel_ClearDeckRuleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "SizeLimit": convert_int(excel_instance.SizeLimitField(), password),
    }

def dump_Excel_ConquestStepExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficultyField(), password)).name,
        "Step": convert_int(excel_instance.StepField(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalizeField(), password),
        "StepEnterScenarioGroupId": convert_int(excel_instance.StepEnterScenarioGroupIdField(), password),
        "StepEnterItemType": ParcelType(convert_int(excel_instance.StepEnterItemTypeField(), password)).name,
        "StepEnterItemUniqueId": convert_int(excel_instance.StepEnterItemUniqueIdField(), password),
        "StepEnterItemAmount": convert_int(excel_instance.StepEnterItemAmountField(), password),
        "UnexpectedEventUnitId": [convert_int(excel_instance.UnexpectedEventUnitIdField(j), password) for j in range(excel_instance.UnexpectedEventUnitIdFieldLength())],
        "UnexpectedEventPrefab": convert_string(excel_instance.UnexpectedEventPrefabField(), password),
        "TreasureBoxObjectId": convert_int(excel_instance.TreasureBoxObjectIdField(), password),
        "TreasureBoxCountPerStepOpen": convert_int(excel_instance.TreasureBoxCountPerStepOpenField(), password),
    }

def dump_Excel_ConstArenaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttackCoolTime": convert_int(excel_instance.AttackCoolTimeField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "DefenseCoolTime": convert_int(excel_instance.DefenseCoolTimeField(), password),
        "TSSStartCoolTime": convert_int(excel_instance.TSSStartCoolTimeField(), password),
        "EndAlarm": convert_int(excel_instance.EndAlarmField(), password),
        "TimeRewardMaxAmount": convert_int(excel_instance.TimeRewardMaxAmountField(), password),
        "EnterCostType": ParcelType(convert_int(excel_instance.EnterCostTypeField(), password)).name,
        "EnterCostId": convert_int(excel_instance.EnterCostIdField(), password),
        "TicketCost": convert_int(excel_instance.TicketCostField(), password),
        "DailyRewardResetTime": convert_string(excel_instance.DailyRewardResetTimeField(), password),
        "OpenScenarioId": convert_string(excel_instance.OpenScenarioIdField(), password),
        "CharacterSlotHideRank": [convert_int(excel_instance.CharacterSlotHideRankField(j), password) for j in range(excel_instance.CharacterSlotHideRankFieldLength())],
        "MapSlotHideRank": convert_int(excel_instance.MapSlotHideRankField(), password),
        "RelativeOpponentRankStart": [convert_int(excel_instance.RelativeOpponentRankStartField(j), password) for j in range(excel_instance.RelativeOpponentRankStartFieldLength())],
        "RelativeOpponentRankEnd": [convert_int(excel_instance.RelativeOpponentRankEndField(j), password) for j in range(excel_instance.RelativeOpponentRankEndFieldLength())],
        "ModifiedStatType": [StatType(convert_int(excel_instance.ModifiedStatTypeField(j), password)).name for j in range(excel_instance.ModifiedStatTypeFieldLength())],
        "StatMulFactor": [convert_int(excel_instance.StatMulFactorField(j), password) for j in range(excel_instance.StatMulFactorFieldLength())],
        "StatSumFactor": [convert_int(excel_instance.StatSumFactorField(j), password) for j in range(excel_instance.StatSumFactorFieldLength())],
        "NPCName": [convert_string(excel_instance.NPCNameField(j), password) for j in range(excel_instance.NPCNameFieldLength())],
        "NPCMainCharacterCount": convert_int(excel_instance.NPCMainCharacterCountField(), password),
        "NPCSupportCharacterCount": convert_int(excel_instance.NPCSupportCharacterCountField(), password),
        "NPCCharacterSkillLevel": convert_int(excel_instance.NPCCharacterSkillLevelField(), password),
        "TimeSpanInDaysForBattleHistory": convert_int(excel_instance.TimeSpanInDaysForBattleHistoryField(), password),
        "HiddenCharacterImagePath": convert_string(excel_instance.HiddenCharacterImagePathField(), password),
        "DefenseVictoryRewardMaxCount": convert_int(excel_instance.DefenseVictoryRewardMaxCountField(), password),
        "TopRankerCountLimit": convert_int(excel_instance.TopRankerCountLimitField(), password),
        "AutoRefreshIntervalMilliSeconds": convert_int(excel_instance.AutoRefreshIntervalMilliSecondsField(), password),
        "EchelonSettingIntervalMilliSeconds": convert_int(excel_instance.EchelonSettingIntervalMilliSecondsField(), password),
        "SkipAllowedTimeMilliSeconds": convert_int(excel_instance.SkipAllowedTimeMilliSecondsField(), password),
        "ShowSeasonChangeInfoStartTime": convert_string(excel_instance.ShowSeasonChangeInfoStartTimeField(), password),
        "ShowSeasonChangeInfoEndTime": convert_string(excel_instance.ShowSeasonChangeInfoEndTimeField(), password),
        "ShowSeasonId": convert_int(excel_instance.ShowSeasonIdField(), password),
        "ArenaHistoryQueryLimitDays": convert_int(excel_instance.ArenaHistoryQueryLimitDaysField(), password),
    }

def dump_Excel_ConstAudioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultSnapShotName": convert_string(excel_instance.DefaultSnapShotNameField(), password),
        "BattleSnapShotName": convert_string(excel_instance.BattleSnapShotNameField(), password),
        "RaidSnapShotName": convert_string(excel_instance.RaidSnapShotNameField(), password),
        "ExSkillCutInSnapShotName": convert_string(excel_instance.ExSkillCutInSnapShotNameField(), password),
    }

def dump_Excel_ConstCombatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SkillHandCount": convert_int(excel_instance.SkillHandCountField(), password),
        "DyingTime": convert_int(excel_instance.DyingTimeField(), password),
        "BuffIconBlinkTime": convert_int(excel_instance.BuffIconBlinkTimeField(), password),
        "ShowBufficonEXSkill": bool(excel_instance.ShowBufficonEXSkillField()),
        "ShowBufficonPassiveSkill": bool(excel_instance.ShowBufficonPassiveSkillField()),
        "ShowBufficonExtraPassiveSkill": bool(excel_instance.ShowBufficonExtraPassiveSkillField()),
        "ShowBufficonLeaderSkill": bool(excel_instance.ShowBufficonLeaderSkillField()),
        "ShowBufficonGroundPassiveSkill": bool(excel_instance.ShowBufficonGroundPassiveSkillField()),
        "SuppliesConditionStringId": convert_string(excel_instance.SuppliesConditionStringIdField(), password),
        "PublicSpeechBubbleOffsetX": convert_float(excel_instance.PublicSpeechBubbleOffsetXField(), password),
        "PublicSpeechBubbleOffsetY": convert_float(excel_instance.PublicSpeechBubbleOffsetYField(), password),
        "PublicSpeechBubbleOffsetZ": convert_float(excel_instance.PublicSpeechBubbleOffsetZField(), password),
        "ShowRaidListCount": convert_int(excel_instance.ShowRaidListCountField(), password),
        "MaxRaidTicketCount": convert_int(excel_instance.MaxRaidTicketCountField(), password),
        "MaxRaidBossSkillSlot": convert_int(excel_instance.MaxRaidBossSkillSlotField(), password),
        "EngageTimelinePath": convert_string(excel_instance.EngageTimelinePathField(), password),
        "EngageWithSupporterTimelinePath": convert_string(excel_instance.EngageWithSupporterTimelinePathField(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePathField(), password),
        "TimeLimitAlarm": convert_int(excel_instance.TimeLimitAlarmField(), password),
        "EchelonMaxCommonCost": convert_int(excel_instance.EchelonMaxCommonCostField(), password),
        "EchelonInitCommonCost": convert_int(excel_instance.EchelonInitCommonCostField(), password),
        "SkillSlotCoolTime": convert_int(excel_instance.SkillSlotCoolTimeField(), password),
        "EnemyRegenCost": convert_int(excel_instance.EnemyRegenCostField(), password),
        "ChampionRegenCost": convert_int(excel_instance.ChampionRegenCostField(), password),
        "PlayerRegenCostDelay": convert_int(excel_instance.PlayerRegenCostDelayField(), password),
        "CrowdControlFactor": convert_int(excel_instance.CrowdControlFactorField(), password),
        "RaidOpenScenarioId": convert_string(excel_instance.RaidOpenScenarioIdField(), password),
        "EliminateRaidOpenScenarioId": convert_string(excel_instance.EliminateRaidOpenScenarioIdField(), password),
        "DefenceConstA": convert_int(excel_instance.DefenceConstAField(), password),
        "DefenceConstB": convert_int(excel_instance.DefenceConstBField(), password),
        "DefenceConstC": convert_int(excel_instance.DefenceConstCField(), password),
        "DefenceConstD": convert_int(excel_instance.DefenceConstDField(), password),
        "AccuracyConstA": convert_int(excel_instance.AccuracyConstAField(), password),
        "AccuracyConstB": convert_int(excel_instance.AccuracyConstBField(), password),
        "AccuracyConstC": convert_int(excel_instance.AccuracyConstCField(), password),
        "AccuracyConstD": convert_int(excel_instance.AccuracyConstDField(), password),
        "CriticalConstA": convert_int(excel_instance.CriticalConstAField(), password),
        "CriticalConstB": convert_int(excel_instance.CriticalConstBField(), password),
        "CriticalConstC": convert_int(excel_instance.CriticalConstCField(), password),
        "CriticalConstD": convert_int(excel_instance.CriticalConstDField(), password),
        "MaxGroupBuffLevel": convert_int(excel_instance.MaxGroupBuffLevelField(), password),
        "EmojiDefaultTime": convert_int(excel_instance.EmojiDefaultTimeField(), password),
        "TimeLineActionRotateSpeed": convert_int(excel_instance.TimeLineActionRotateSpeedField(), password),
        "BodyRotateSpeed": convert_int(excel_instance.BodyRotateSpeedField(), password),
        "NormalTimeScale": convert_int(excel_instance.NormalTimeScaleField(), password),
        "FastTimeScale": convert_int(excel_instance.FastTimeScaleField(), password),
        "BulletTimeScale": convert_int(excel_instance.BulletTimeScaleField(), password),
        "UIDisplayDelayAfterSkillCutIn": convert_int(excel_instance.UIDisplayDelayAfterSkillCutInField(), password),
        "UseInitialRangeForCoverMove": bool(excel_instance.UseInitialRangeForCoverMoveField()),
        "SlowTimeScale": convert_int(excel_instance.SlowTimeScaleField(), password),
        "AimIKMinDegree": convert_float(excel_instance.AimIKMinDegreeField(), password),
        "AimIKMaxDegree": convert_float(excel_instance.AimIKMaxDegreeField(), password),
        "MinimumClearTime": convert_int(excel_instance.MinimumClearTimeField(), password),
        "MinimumClearLevelGap": convert_int(excel_instance.MinimumClearLevelGapField(), password),
        "CheckCheaterMaxUseCostNonArena": convert_int(excel_instance.CheckCheaterMaxUseCostNonArenaField(), password),
        "CheckCheaterMaxUseCostArena": convert_int(excel_instance.CheckCheaterMaxUseCostArenaField(), password),
        "AllowedMaxTimeScale": convert_int(excel_instance.AllowedMaxTimeScaleField(), password),
        "RandomAnimationOutput": convert_int(excel_instance.RandomAnimationOutputField(), password),
        "SummonedTeleportDistance": convert_int(excel_instance.SummonedTeleportDistanceField(), password),
        "ArenaMinimumClearTime": convert_int(excel_instance.ArenaMinimumClearTimeField(), password),
        "WORLDBOSSBATTLELITTLE": convert_int(excel_instance.WORLDBOSSBATTLELITTLEField(), password),
        "WORLDBOSSBATTLELITTLETw": convert_int(excel_instance.WORLDBOSSBATTLELITTLETwField(), password),
        "WORLDBOSSBATTLELITTLEAsia": convert_int(excel_instance.WORLDBOSSBATTLELITTLEAsiaField(), password),
        "WORLDBOSSBATTLELITTLENa": convert_int(excel_instance.WORLDBOSSBATTLELITTLENaField(), password),
        "WORLDBOSSBATTLELITTLEGlobal": convert_int(excel_instance.WORLDBOSSBATTLELITTLEGlobalField(), password),
        "WORLDBOSSBATTLEMIDDLE": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLEField(), password),
        "WORLDBOSSBATTLEMIDDLETw": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLETwField(), password),
        "WORLDBOSSBATTLEMIDDLEAsia": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLEAsiaField(), password),
        "WORLDBOSSBATTLEMIDDLENa": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLENaField(), password),
        "WORLDBOSSBATTLEMIDDLEGlobal": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLEGlobalField(), password),
        "WORLDBOSSBATTLEHIGH": convert_int(excel_instance.WORLDBOSSBATTLEHIGHField(), password),
        "WORLDBOSSBATTLEHIGHTw": convert_int(excel_instance.WORLDBOSSBATTLEHIGHTwField(), password),
        "WORLDBOSSBATTLEHIGHAsia": convert_int(excel_instance.WORLDBOSSBATTLEHIGHAsiaField(), password),
        "WORLDBOSSBATTLEHIGHNa": convert_int(excel_instance.WORLDBOSSBATTLEHIGHNaField(), password),
        "WORLDBOSSBATTLEHIGHGlobal": convert_int(excel_instance.WORLDBOSSBATTLEHIGHGlobalField(), password),
        "WORLDBOSSBATTLEVERYHIGH": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHField(), password),
        "WORLDBOSSBATTLEVERYHIGHTw": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHTwField(), password),
        "WORLDBOSSBATTLEVERYHIGHAsia": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHAsiaField(), password),
        "WORLDBOSSBATTLEVERYHIGHNa": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHNaField(), password),
        "WORLDBOSSBATTLEVERYHIGHGlobal": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHGlobalField(), password),
        "WorldRaidAutoSyncTermSecond": convert_int(excel_instance.WorldRaidAutoSyncTermSecondField(), password),
        "WorldRaidBossHpDecreaseTerm": convert_int(excel_instance.WorldRaidBossHpDecreaseTermField(), password),
        "WorldRaidBossParcelReactionDelay": convert_int(excel_instance.WorldRaidBossParcelReactionDelayField(), password),
        "RaidRankingJumpMinimumWaitingTime": convert_int(excel_instance.RaidRankingJumpMinimumWaitingTimeField(), password),
        "EffectTeleportDistance": convert_float(excel_instance.EffectTeleportDistanceField(), password),
        "AuraExitThresholdMargin": convert_int(excel_instance.AuraExitThresholdMarginField(), password),
        "TSAInteractionDamageFactor": convert_int(excel_instance.TSAInteractionDamageFactorField(), password),
        "VictoryInteractionRate": convert_int(excel_instance.VictoryInteractionRateField(), password),
        "EchelonExtensionEngageTimelinePath": convert_string(excel_instance.EchelonExtensionEngageTimelinePathField(), password),
        "EchelonExtensionEngageWithSupporterTimelinePath": convert_string(excel_instance.EchelonExtensionEngageWithSupporterTimelinePathField(), password),
        "EchelonExtensionVictoryTimelinePath": convert_string(excel_instance.EchelonExtensionVictoryTimelinePathField(), password),
        "EchelonExtensionEchelonMaxCommonCost": convert_int(excel_instance.EchelonExtensionEchelonMaxCommonCostField(), password),
        "EchelonMaxOverloadCost": convert_int(excel_instance.EchelonMaxOverloadCostField(), password),
        "EchelonExtensionMaxOverloadCost": convert_int(excel_instance.EchelonExtensionMaxOverloadCostField(), password),
        "EchelonExtensionEchelonInitCommonCost": convert_int(excel_instance.EchelonExtensionEchelonInitCommonCostField(), password),
        "EchelonExtensionCostRegenRatio": convert_int(excel_instance.EchelonExtensionCostRegenRatioField(), password),
        "EchelonOverloadCostRegenRatio": convert_int(excel_instance.EchelonOverloadCostRegenRatioField(), password),
        "EchelonExtensionOverloadCostRegenRatio": convert_int(excel_instance.EchelonExtensionOverloadCostRegenRatioField(), password),
        "CheckCheaterMaxUseCostMultiFloorRaid": convert_int(excel_instance.CheckCheaterMaxUseCostMultiFloorRaidField(), password),
        "ExcessiveTouchCheckTime": convert_float(excel_instance.ExcessiveTouchCheckTimeField(), password),
        "ExcessiveTouchCheckCount": convert_int(excel_instance.ExcessiveTouchCheckCountField(), password),
        "CampaignAlertPopupLevelGap": convert_int(excel_instance.CampaignAlertPopupLevelGapField(), password),
        "MoveCorrectionSkipRatio": convert_int(excel_instance.MoveCorrectionSkipRatioField(), password),
        "ObstacleColliderHeightJumpable": convert_float(excel_instance.ObstacleColliderHeightJumpableField(), password),
        "ObstacleColliderHeightNotJumpable": convert_float(excel_instance.ObstacleColliderHeightNotJumpableField(), password),
    }

def dump_Excel_ConstCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CampaignMainStageMaxRank": convert_int(excel_instance.CampaignMainStageMaxRankField(), password),
        "CampaignMainStageBestRecord": convert_int(excel_instance.CampaignMainStageBestRecordField(), password),
        "HardAdventurePlayCountRecoverDailyNumber": convert_int(excel_instance.HardAdventurePlayCountRecoverDailyNumberField(), password),
        "HardStageCount": convert_int(excel_instance.HardStageCountField(), password),
        "TacticRankClearTime": convert_int(excel_instance.TacticRankClearTimeField(), password),
        "BaseTimeScale": convert_int(excel_instance.BaseTimeScaleField(), password),
        "GachaPercentage": convert_int(excel_instance.GachaPercentageField(), password),
        "AcademyFavorZoneId": convert_int(excel_instance.AcademyFavorZoneIdField(), password),
        "CafePresetSlotCount": convert_int(excel_instance.CafePresetSlotCountField(), password),
        "CafeMonologueIntervalMillisec": convert_int(excel_instance.CafeMonologueIntervalMillisecField(), password),
        "CafeMonologueDefaultDuration": convert_int(excel_instance.CafeMonologueDefaultDurationField(), password),
        "CafeBubbleIdleDurationMilliSec": convert_int(excel_instance.CafeBubbleIdleDurationMilliSecField(), password),
        "FindGiftTimeLimit": convert_int(excel_instance.FindGiftTimeLimitField(), password),
        "CafeAutoChargePeriodInMsc": convert_int(excel_instance.CafeAutoChargePeriodInMscField(), password),
        "CafeProductionDecimalPosition": convert_int(excel_instance.CafeProductionDecimalPositionField(), password),
        "CafeSetGroupApplyCount": convert_int(excel_instance.CafeSetGroupApplyCountField(), password),
        "WeekDungeonFindGiftRewardLimitCount": convert_int(excel_instance.WeekDungeonFindGiftRewardLimitCountField(), password),
        "StageFailedCurrencyRefundRate": convert_int(excel_instance.StageFailedCurrencyRefundRateField(), password),
        "EnterDeposit": convert_int(excel_instance.EnterDepositField(), password),
        "AccountMaxLevel": convert_int(excel_instance.AccountMaxLevelField(), password),
        "MainSquadExpBonus": convert_int(excel_instance.MainSquadExpBonusField(), password),
        "SupportSquadExpBonus": convert_int(excel_instance.SupportSquadExpBonusField(), password),
        "AccountExpRatio": convert_int(excel_instance.AccountExpRatioField(), password),
        "MissionToastLifeTime": convert_int(excel_instance.MissionToastLifeTimeField(), password),
        "ExpItemInsertLimit": convert_int(excel_instance.ExpItemInsertLimitField(), password),
        "ExpItemInsertAccelTime": convert_int(excel_instance.ExpItemInsertAccelTimeField(), password),
        "CharacterLvUpCoefficient": convert_int(excel_instance.CharacterLvUpCoefficientField(), password),
        "EquipmentLvUpCoefficient": convert_int(excel_instance.EquipmentLvUpCoefficientField(), password),
        "ExpEquipInsertLimit": convert_int(excel_instance.ExpEquipInsertLimitField(), password),
        "EquipLvUpCoefficient": convert_int(excel_instance.EquipLvUpCoefficientField(), password),
        "NicknameLength": convert_int(excel_instance.NicknameLengthField(), password),
        "CraftDuration": [convert_int(excel_instance.CraftDurationField(j), password) for j in range(excel_instance.CraftDurationFieldLength())],
        "CraftLimitTime": convert_int(excel_instance.CraftLimitTimeField(), password),
        "ShiftingCraftDuration": [convert_int(excel_instance.ShiftingCraftDurationField(j), password) for j in range(excel_instance.ShiftingCraftDurationFieldLength())],
        "ShiftingCraftTicketConsumeAmount": convert_int(excel_instance.ShiftingCraftTicketConsumeAmountField(), password),
        "ShiftingCraftSlotMaxCapacity": convert_int(excel_instance.ShiftingCraftSlotMaxCapacityField(), password),
        "CraftTicketItemUniqueId": convert_int(excel_instance.CraftTicketItemUniqueIdField(), password),
        "CraftTicketConsumeAmount": convert_int(excel_instance.CraftTicketConsumeAmountField(), password),
        "AcademyEnterCostType": ParcelType(convert_int(excel_instance.AcademyEnterCostTypeField(), password)).name,
        "AcademyEnterCostId": convert_int(excel_instance.AcademyEnterCostIdField(), password),
        "AcademyTicketCost": convert_int(excel_instance.AcademyTicketCostField(), password),
        "MassangerMessageExpireDay": convert_int(excel_instance.MassangerMessageExpireDayField(), password),
        "CraftLeafNodeGenerateLv1Count": convert_int(excel_instance.CraftLeafNodeGenerateLv1CountField(), password),
        "CraftLeafNodeGenerateLv2Count": convert_int(excel_instance.CraftLeafNodeGenerateLv2CountField(), password),
        "TutorialGachaShopId": convert_int(excel_instance.TutorialGachaShopIdField(), password),
        "BeforehandGachaShopId": convert_int(excel_instance.BeforehandGachaShopIdField(), password),
        "TutorialGachaGoodsId": convert_int(excel_instance.TutorialGachaGoodsIdField(), password),
        "EquipmentSlotOpenLevel": [convert_int(excel_instance.EquipmentSlotOpenLevelField(j), password) for j in range(excel_instance.EquipmentSlotOpenLevelFieldLength())],
        "JoinOrCreateClanCoolTimeFromHour": convert_int(excel_instance.JoinOrCreateClanCoolTimeFromHourField(), password),
        "ClanMaxMember": convert_int(excel_instance.ClanMaxMemberField(), password),
        "ClanSearchResultCount": convert_int(excel_instance.ClanSearchResultCountField(), password),
        "ClanMaxApplicant": convert_int(excel_instance.ClanMaxApplicantField(), password),
        "ClanRejoinCoolTimeFromSecond": convert_int(excel_instance.ClanRejoinCoolTimeFromSecondField(), password),
        "ClanWordBalloonMaxCharacter": convert_int(excel_instance.ClanWordBalloonMaxCharacterField(), password),
        "CallNameRenameCoolTimeFromHour": convert_int(excel_instance.CallNameRenameCoolTimeFromHourField(), password),
        "CallNameMinimumLength": convert_int(excel_instance.CallNameMinimumLengthField(), password),
        "CallNameMaximumLength": convert_int(excel_instance.CallNameMaximumLengthField(), password),
        "LobbyToScreenModeWaitTime": convert_int(excel_instance.LobbyToScreenModeWaitTimeField(), password),
        "ScreenshotToLobbyButtonHideDelay": convert_int(excel_instance.ScreenshotToLobbyButtonHideDelayField(), password),
        "PrologueScenarioID01": convert_int(excel_instance.PrologueScenarioID01Field(), password),
        "PrologueScenarioID02": convert_int(excel_instance.PrologueScenarioID02Field(), password),
        "TutorialHardStage11": convert_int(excel_instance.TutorialHardStage11Field(), password),
        "TutorialSpeedButtonStage": convert_int(excel_instance.TutorialSpeedButtonStageField(), password),
        "TutorialCharacterDefaultCount": convert_int(excel_instance.TutorialCharacterDefaultCountField(), password),
        "TutorialShopCategoryType": convert_float(excel_instance.TutorialShopCategoryTypeField(), password),
        "AdventureStrategyPlayTimeLimitInSeconds": convert_int(excel_instance.AdventureStrategyPlayTimeLimitInSecondsField(), password),
        "WeekDungoenTacticPlayTimeLimitInSeconds": convert_int(excel_instance.WeekDungoenTacticPlayTimeLimitInSecondsField(), password),
        "RaidTacticPlayTimeLimitInSeconds": convert_int(excel_instance.RaidTacticPlayTimeLimitInSecondsField(), password),
        "RaidOpponentListAmount": convert_int(excel_instance.RaidOpponentListAmountField(), password),
        "CraftBaseGoldRequired": [convert_int(excel_instance.CraftBaseGoldRequiredField(j), password) for j in range(excel_instance.CraftBaseGoldRequiredFieldLength())],
        "PostExpiredDayAttendance": convert_int(excel_instance.PostExpiredDayAttendanceField(), password),
        "PostExpiredDayInventoryOverflow": convert_int(excel_instance.PostExpiredDayInventoryOverflowField(), password),
        "PostExpiredDayGameManager": convert_int(excel_instance.PostExpiredDayGameManagerField(), password),
        "UILabelCharacterWrap": convert_string(excel_instance.UILabelCharacterWrapField(), password),
        "RequestTimeOut": convert_float(excel_instance.RequestTimeOutField(), password),
        "MailStorageSoftCap": convert_int(excel_instance.MailStorageSoftCapField(), password),
        "MailStorageHardCap": convert_int(excel_instance.MailStorageHardCapField(), password),
        "ClearDeckStorageSize": convert_int(excel_instance.ClearDeckStorageSizeField(), password),
        "ClearDeckNoStarViewCount": convert_int(excel_instance.ClearDeckNoStarViewCountField(), password),
        "ClearDeck1StarViewCount": convert_int(excel_instance.ClearDeck1StarViewCountField(), password),
        "ClearDeck2StarViewCount": convert_int(excel_instance.ClearDeck2StarViewCountField(), password),
        "ClearDeck3StarViewCount": convert_int(excel_instance.ClearDeck3StarViewCountField(), password),
        "ExSkillLevelMax": convert_int(excel_instance.ExSkillLevelMaxField(), password),
        "PublicSkillLevelMax": convert_int(excel_instance.PublicSkillLevelMaxField(), password),
        "PassiveSkillLevelMax": convert_int(excel_instance.PassiveSkillLevelMaxField(), password),
        "ExtraPassiveSkillLevelMax": convert_int(excel_instance.ExtraPassiveSkillLevelMaxField(), password),
        "AccountCommentMaxLength": convert_int(excel_instance.AccountCommentMaxLengthField(), password),
        "CafeSummonCoolTimeFromHour": convert_int(excel_instance.CafeSummonCoolTimeFromHourField(), password),
        "LimitedStageDailyClearCount": convert_int(excel_instance.LimitedStageDailyClearCountField(), password),
        "LimitedStageEntryTimeLimit": convert_int(excel_instance.LimitedStageEntryTimeLimitField(), password),
        "LimitedStageEntryTimeBuffer": convert_int(excel_instance.LimitedStageEntryTimeBufferField(), password),
        "LimitedStagePointAmount": convert_int(excel_instance.LimitedStagePointAmountField(), password),
        "LimitedStagePointPerApMin": convert_int(excel_instance.LimitedStagePointPerApMinField(), password),
        "LimitedStagePointPerApMax": convert_int(excel_instance.LimitedStagePointPerApMaxField(), password),
        "AccountLinkReward": convert_int(excel_instance.AccountLinkRewardField(), password),
        "MonthlyProductCheckDays": convert_int(excel_instance.MonthlyProductCheckDaysField(), password),
        "WeaponLvUpCoefficient": convert_int(excel_instance.WeaponLvUpCoefficientField(), password),
        "ShowRaidMyListCount": convert_int(excel_instance.ShowRaidMyListCountField(), password),
        "RaidEnterCostType": ParcelType(convert_int(excel_instance.RaidEnterCostTypeField(), password)).name,
        "RaidEnterCostId": convert_int(excel_instance.RaidEnterCostIdField(), password),
        "RaidTicketCost": convert_int(excel_instance.RaidTicketCostField(), password),
        "TimeAttackDungeonScenarioId": convert_string(excel_instance.TimeAttackDungeonScenarioIdField(), password),
        "TimeAttackDungoenPlayCountPerTicket": convert_int(excel_instance.TimeAttackDungoenPlayCountPerTicketField(), password),
        "TimeAttackDungeonEnterCostType": ParcelType(convert_int(excel_instance.TimeAttackDungeonEnterCostTypeField(), password)).name,
        "TimeAttackDungeonEnterCostId": convert_int(excel_instance.TimeAttackDungeonEnterCostIdField(), password),
        "TimeAttackDungeonEnterCost": convert_int(excel_instance.TimeAttackDungeonEnterCostField(), password),
        "ClanLeaderTransferLastLoginLimit": convert_int(excel_instance.ClanLeaderTransferLastLoginLimitField(), password),
        "MonthlyProductRepurchasePopupLimit": convert_int(excel_instance.MonthlyProductRepurchasePopupLimitField(), password),
        "CommonFavorItemTags": [Tag(convert_int(excel_instance.CommonFavorItemTagsField(j), password)).name for j in range(excel_instance.CommonFavorItemTagsFieldLength())],
        "MaxApMasterCoinPerWeek": convert_int(excel_instance.MaxApMasterCoinPerWeekField(), password),
        "CraftOpenExpTier1": convert_int(excel_instance.CraftOpenExpTier1Field(), password),
        "CraftOpenExpTier2": convert_int(excel_instance.CraftOpenExpTier2Field(), password),
        "CraftOpenExpTier3": convert_int(excel_instance.CraftOpenExpTier3Field(), password),
        "CharacterEquipmentGearSlot": convert_int(excel_instance.CharacterEquipmentGearSlotField(), password),
        "BirthDayDDay": convert_int(excel_instance.BirthDayDDayField(), password),
        "RecommendedFriendsLvDifferenceLimit": convert_int(excel_instance.RecommendedFriendsLvDifferenceLimitField(), password),
        "DDosDetectCount": convert_int(excel_instance.DDosDetectCountField(), password),
        "DDosCheckIntervalInSeconds": convert_int(excel_instance.DDosCheckIntervalInSecondsField(), password),
        "MaxFriendsCount": convert_int(excel_instance.MaxFriendsCountField(), password),
        "MaxFriendsRequest": convert_int(excel_instance.MaxFriendsRequestField(), password),
        "FriendsSearchRequestCount": convert_int(excel_instance.FriendsSearchRequestCountField(), password),
        "FriendsMaxApplicant": convert_int(excel_instance.FriendsMaxApplicantField(), password),
        "IdCardDefaultCharacterId": convert_int(excel_instance.IdCardDefaultCharacterIdField(), password),
        "IdCardDefaultBgId": convert_int(excel_instance.IdCardDefaultBgIdField(), password),
        "WorldRaidGemEnterCost": convert_int(excel_instance.WorldRaidGemEnterCostField(), password),
        "WorldRaidGemEnterAmout": convert_int(excel_instance.WorldRaidGemEnterAmoutField(), password),
        "FriendIdCardCommentMaxLength": convert_int(excel_instance.FriendIdCardCommentMaxLengthField(), password),
        "FormationPresetNumberOfEchelonTab": convert_int(excel_instance.FormationPresetNumberOfEchelonTabField(), password),
        "FormationPresetNumberOfEchelon": convert_int(excel_instance.FormationPresetNumberOfEchelonField(), password),
        "FormationPresetRecentNumberOfEchelon": convert_int(excel_instance.FormationPresetRecentNumberOfEchelonField(), password),
        "FormationPresetEchelonTabTextLength": convert_int(excel_instance.FormationPresetEchelonTabTextLengthField(), password),
        "FormationPresetEchelonSlotTextLength": convert_int(excel_instance.FormationPresetEchelonSlotTextLengthField(), password),
        "CharProfileRowIntervalKr": convert_int(excel_instance.CharProfileRowIntervalKrField(), password),
        "CallnameLengthEn": convert_int(excel_instance.CallnameLengthEnField(), password),
        "CallnameLengthKr": convert_int(excel_instance.CallnameLengthKrField(), password),
        "NicknameLengthKr": convert_int(excel_instance.NicknameLengthKrField(), password),
        "ClanNameLength": convert_int(excel_instance.ClanNameLengthField(), password),
        "CafePresetEditNameLength": convert_int(excel_instance.CafePresetEditNameLengthField(), password),
        "FormationPresetEchelonTabTextLengthKr": convert_int(excel_instance.FormationPresetEchelonTabTextLengthKrField(), password),
        "FormationPresetEchelonSlotTextLengthKr": convert_int(excel_instance.FormationPresetEchelonSlotTextLengthKrField(), password),
        "CharProfileRowIntervalJp": convert_int(excel_instance.CharProfileRowIntervalJpField(), password),
        "CharProfilePopupRowIntervalKr": convert_int(excel_instance.CharProfilePopupRowIntervalKrField(), password),
        "CharProfilePopupRowIntervalJp": convert_int(excel_instance.CharProfilePopupRowIntervalJpField(), password),
        "BeforehandGachaCount": convert_int(excel_instance.BeforehandGachaCountField(), password),
        "LowMemorySizeGL": convert_int(excel_instance.LowMemorySizeGLField(), password),
        "BeforehandGachaGroupId": convert_int(excel_instance.BeforehandGachaGroupIdField(), password),
        "RenewalDisplayOrderDay": convert_int(excel_instance.RenewalDisplayOrderDayField(), password),
        "EmblemDefaultId": convert_int(excel_instance.EmblemDefaultIdField(), password),
        "BirthdayMailStartDate": convert_string(excel_instance.BirthdayMailStartDateField(), password),
        "BirthdayMailRemainDate": convert_int(excel_instance.BirthdayMailRemainDateField(), password),
        "BirthdayMailParcelType": ParcelType(convert_int(excel_instance.BirthdayMailParcelTypeField(), password)).name,
        "BirthdayMailParcelId": convert_int(excel_instance.BirthdayMailParcelIdField(), password),
        "BirthdayMailParcelAmount": convert_int(excel_instance.BirthdayMailParcelAmountField(), password),
        "ClearDeckAverageDeckCount": convert_int(excel_instance.ClearDeckAverageDeckCountField(), password),
        "ClearDeckWorldRaidSaveConditionCoefficient": convert_int(excel_instance.ClearDeckWorldRaidSaveConditionCoefficientField(), password),
        "ClearDeckShowCount": convert_int(excel_instance.ClearDeckShowCountField(), password),
        "CharacterMaxLevel": convert_int(excel_instance.CharacterMaxLevelField(), password),
        "PotentialBonusStatMaxLevelMaxHP": convert_int(excel_instance.PotentialBonusStatMaxLevelMaxHPField(), password),
        "PotentialBonusStatMaxLevelAttackPower": convert_int(excel_instance.PotentialBonusStatMaxLevelAttackPowerField(), password),
        "PotentialBonusStatMaxLevelHealPower": convert_int(excel_instance.PotentialBonusStatMaxLevelHealPowerField(), password),
        "PotentialOpenConditionCharacterLevel": convert_int(excel_instance.PotentialOpenConditionCharacterLevelField(), password),
        "AssistStrangerMinLevel": convert_int(excel_instance.AssistStrangerMinLevelField(), password),
        "ClanChattingNoticeCautionDelay": convert_float(excel_instance.ClanChattingNoticeCautionDelayField(), password),
        "CallNameWaitTimeGL": convert_float(excel_instance.CallNameWaitTimeGLField(), password),
        "AssistStrangerMaxLevel": convert_int(excel_instance.AssistStrangerMaxLevelField(), password),
        "MaxBlockedUserCount": convert_int(excel_instance.MaxBlockedUserCountField(), password),
        "CafeRandomVisitMinComfortBonus": convert_int(excel_instance.CafeRandomVisitMinComfortBonusField(), password),
        "CafeRandomVisitMinLastLogin": convert_int(excel_instance.CafeRandomVisitMinLastLoginField(), password),
        "CafeTravelSyncIntervalByMillisec": convert_int(excel_instance.CafeTravelSyncIntervalByMillisecField(), password),
        "RankBracketPercentage1": convert_int(excel_instance.RankBracketPercentage1Field(), password),
        "RankBracketPercentage2": convert_int(excel_instance.RankBracketPercentage2Field(), password),
        "RankBracketPercentage3": convert_int(excel_instance.RankBracketPercentage3Field(), password),
        "RankBracketPercentage4": convert_int(excel_instance.RankBracketPercentage4Field(), password),
        "RankBracketPercentage5": convert_int(excel_instance.RankBracketPercentage5Field(), password),
        "RankBracketPercentage6": convert_int(excel_instance.RankBracketPercentage6Field(), password),
        "RankBracketPercentage7": convert_int(excel_instance.RankBracketPercentage7Field(), password),
        "ExpiryBattlePassItemReceiveDay": convert_int(excel_instance.ExpiryBattlePassItemReceiveDayField(), password),
        "BattlePassFlavorTextIdleDurationMilliSec": convert_int(excel_instance.BattlePassFlavorTextIdleDurationMilliSecField(), password),
        "BattlePassEndImminentDay": convert_int(excel_instance.BattlePassEndImminentDayField(), password),
        "BattlePassExpIconPath": convert_string(excel_instance.BattlePassExpIconPathField(), password),
        "CafeCameraDragThreshold": convert_float(excel_instance.CafeCameraDragThresholdField(), password),
        "CafeSummonTicketBuyLimitForValidate": convert_int(excel_instance.CafeSummonTicketBuyLimitForValidateField(), password),
        "BattlePassNotifyDateGL": convert_int(excel_instance.BattlePassNotifyDateGLField(), password),
        "PurchaseMailExpiredDayGL": convert_int(excel_instance.PurchaseMailExpiredDayGLField(), password),
        "ReviewEventDateGL": convert_string(excel_instance.ReviewEventDateGLField(), password),
        "ReviewEventStageIDGL": convert_int(excel_instance.ReviewEventStageIDGLField(), password),
        "ReviewEventCharIDGL": convert_int(excel_instance.ReviewEventCharIDGLField(), password),
        "AutoCraftPresetCountLimit": convert_int(excel_instance.AutoCraftPresetCountLimitField(), password),
        "AutoCraftNodeSelectCount": convert_int(excel_instance.AutoCraftNodeSelectCountField(), password),
        "CraftPresetNameMaxLength": convert_int(excel_instance.CraftPresetNameMaxLengthField(), password),
        "SelectionWaitTime": convert_int(excel_instance.SelectionWaitTimeField(), password),
        "RewardWaitTime": convert_int(excel_instance.RewardWaitTimeField(), password),
        "EpisodeContinueWaitTime": convert_int(excel_instance.EpisodeContinueWaitTimeField(), password),
        "ScenarioAutoDelayMillisecLong": convert_float(excel_instance.ScenarioAutoDelayMillisecLongField(), password),
        "ScenarioAutoDelayMillisec": convert_float(excel_instance.ScenarioAutoDelayMillisecField(), password),
        "ScenarioAutoDelayMillisecShort": convert_float(excel_instance.ScenarioAutoDelayMillisecShortField(), password),
        "ScenarioAutoDelayMillisecVeryShort": convert_float(excel_instance.ScenarioAutoDelayMillisecVeryShortField(), password),
        "PcBuildEnterInformation": convert_int(excel_instance.PcBuildEnterInformationField(), password),
        "ComebackUserStandardDay": convert_int(excel_instance.ComebackUserStandardDayField(), password),
        "ComebackUserLogSaveDay": convert_int(excel_instance.ComebackUserLogSaveDayField(), password),
        "ComeBackActivateCooldown": convert_int(excel_instance.ComeBackActivateCooldownField(), password),
        "CafeCopyPresetSlotCount": convert_int(excel_instance.CafeCopyPresetSlotCountField(), password),
        "ExpiryProductDailyRecordItemReceiveDay": convert_int(excel_instance.ExpiryProductDailyRecordItemReceiveDayField(), password),
        "NewbieUserStandardDay": convert_int(excel_instance.NewbieUserStandardDayField(), password),
        "NewbieStateHoldDay": convert_int(excel_instance.NewbieStateHoldDayField(), password),
        "QRIconUrlDev": convert_string(excel_instance.QRIconUrlDevField(), password),
        "QRIconUrlLive": convert_string(excel_instance.QRIconUrlLiveField(), password),
        "ProbablityInfoBtnLinkKR": convert_string(excel_instance.ProbablityInfoBtnLinkKRField(), password),
        "ClearDeckEchelonShowMaxCount": convert_int(excel_instance.ClearDeckEchelonShowMaxCountField(), password),
    }

def dump_Excel_ConstConquestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ManageUnitChange": convert_int(excel_instance.ManageUnitChangeField(), password),
        "AssistCount": convert_int(excel_instance.AssistCountField(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSecondsField(), password),
        "AnimationUnitAmountMin": convert_int(excel_instance.AnimationUnitAmountMinField(), password),
        "AnimationUnitAmountMax": convert_int(excel_instance.AnimationUnitAmountMaxField(), password),
        "AnimationUnitDelay": convert_float(excel_instance.AnimationUnitDelayField(), password),
    }

def dump_Excel_ConstContentsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UseSearchFieldOptimize": bool(excel_instance.UseSearchFieldOptimizeField()),
        "SearchUpdateTime": convert_float(excel_instance.SearchUpdateTimeField(), password),
        "LobbyDayTimeFrom": convert_int(excel_instance.LobbyDayTimeFromField(), password),
        "LobbyNightTimeFrom": convert_int(excel_instance.LobbyNightTimeFromField(), password),
    }

def dump_Excel_ConstEventCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentHardStageCount": convert_int(excel_instance.EventContentHardStageCountField(), password),
        "EventStrategyPlayTimeLimitInSeconds": convert_int(excel_instance.EventStrategyPlayTimeLimitInSecondsField(), password),
        "SubEventChangeLimitSeconds": convert_int(excel_instance.SubEventChangeLimitSecondsField(), password),
        "SubEventInstantClear": bool(excel_instance.SubEventInstantClearField()),
        "CardShopProbWeightCount": convert_int(excel_instance.CardShopProbWeightCountField(), password),
        "CardShopProbWeightRarity": Rarity(convert_int(excel_instance.CardShopProbWeightRarityField(), password)).name,
        "MeetupScenarioReplayResource": convert_string(excel_instance.MeetupScenarioReplayResourceField(), password),
        "MeetupScenarioReplayTitleLocalize": convert_string(excel_instance.MeetupScenarioReplayTitleLocalizeField(), password),
        "SpecialOperactionCollectionGroupId": convert_int(excel_instance.SpecialOperactionCollectionGroupIdField(), password),
        "TreasureNormalVariationAmount": convert_int(excel_instance.TreasureNormalVariationAmountField(), password),
        "TreasureLoopVariationAmount": convert_int(excel_instance.TreasureLoopVariationAmountField(), password),
        "TreasureLimitVariationLoopCount": convert_int(excel_instance.TreasureLimitVariationLoopCountField(), password),
        "TreasureLimitVariationClearLoopCount": convert_int(excel_instance.TreasureLimitVariationClearLoopCountField(), password),
        "EventStoryReplayHideEventContentId": convert_int(excel_instance.EventStoryReplayHideEventContentIdField(), password),
    }

def dump_Excel_ConstFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DialogSmoothTime": convert_int(excel_instance.DialogSmoothTimeField(), password),
        "TalkDialogDurationDefault": convert_int(excel_instance.TalkDialogDurationDefaultField(), password),
        "ThinkDialogDurationDefault": convert_int(excel_instance.ThinkDialogDurationDefaultField(), password),
        "IdleThinkDelayMin": convert_int(excel_instance.IdleThinkDelayMinField(), password),
        "IdleThinkDelayMax": convert_int(excel_instance.IdleThinkDelayMaxField(), password),
    }

def dump_Excel_ConstKeyMappingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DragSensitivity": convert_float(excel_instance.DragSensitivityField(), password),
        "PcInformationGroupID": convert_int(excel_instance.PcInformationGroupIDField(), password),
        "PcControllerInformationGroupID": convert_int(excel_instance.PcControllerInformationGroupIDField(), password),
        "ScrollWheelFactor": convert_float(excel_instance.ScrollWheelFactorField(), password),
        "RemoveKeycodeWord": convert_string(excel_instance.RemoveKeycodeWordField(), password),
        "TutorialDialogTouchKey": convert_string(excel_instance.TutorialDialogTouchKeyField(), password),
        "ControllerCursorFactorSlow": convert_int(excel_instance.ControllerCursorFactorSlowField(), password),
        "ControllerCursorFactor": convert_int(excel_instance.ControllerCursorFactorField(), password),
        "ControllerCursorFactorFast": convert_int(excel_instance.ControllerCursorFactorFastField(), password),
        "VibrationSec": convert_float(excel_instance.VibrationSecField(), password),
        "VibrationPower": convert_float(excel_instance.VibrationPowerField(), password),
        "ControllerScrollWheelFactor": convert_float(excel_instance.ControllerScrollWheelFactorField(), password),
        "ControllerZoomSensitivity": convert_float(excel_instance.ControllerZoomSensitivityField(), password),
        "ControllerDpadMoveCheckRangeX": convert_float(excel_instance.ControllerDpadMoveCheckRangeXField(), password),
        "ControllerDpadMoveCheckRangeY": convert_float(excel_instance.ControllerDpadMoveCheckRangeYField(), password),
        "ControllerCursorClickScale": convert_float(excel_instance.ControllerCursorClickScaleField(), password),
        "ControllerScrollSensitivity": convert_float(excel_instance.ControllerScrollSensitivityField(), password),
    }

def dump_Excel_ConstMinigameCCGExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TurnDrawCount": convert_int(excel_instance.TurnDrawCountField(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRightField(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTopField(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottomField(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetXField(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetYField(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngleField(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMaxField(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMinField(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefaultField(), password),
        "ThemaLoadingProgressTime": convert_float(excel_instance.ThemaLoadingProgressTimeField(), password),
        "MapAllyRotation": convert_float(excel_instance.MapAllyRotationField(), password),
        "AniAllyBattleAttack": convert_string(excel_instance.AniAllyBattleAttackField(), password),
        "MaxHandCount": convert_int(excel_instance.MaxHandCountField(), password),
        "MaxCost": convert_int(excel_instance.MaxCostField(), password),
        "StartCost": convert_int(excel_instance.StartCostField(), password),
        "TurnCost": convert_int(excel_instance.TurnCostField(), password),
        "StrikerSwapFrontCost": convert_int(excel_instance.StrikerSwapFrontCostField(), password),
        "StrikerMaxEquipCount": convert_int(excel_instance.StrikerMaxEquipCountField(), password),
        "StartDrawCount": convert_int(excel_instance.StartDrawCountField(), password),
        "CampReviveHealthRate": convert_int(excel_instance.CampReviveHealthRateField(), password),
        "BaseRewardRerollPoint": convert_int(excel_instance.BaseRewardRerollPointField(), password),
        "SelectRewardOptionCount": convert_int(excel_instance.SelectRewardOptionCountField(), password),
        "AlternativeCardImagePath": convert_string(excel_instance.AlternativeCardImagePathField(), password),
    }

def dump_Excel_ConstMinigameRoadPuzzleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RoadPuzzleMapBoundaryOffsetLeft": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetLeftField(), password),
        "RoadPuzzleMapBoundaryOffsetRight": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetRightField(), password),
        "RoadPuzzleMapBoundaryOffsetTop": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetTopField(), password),
        "RoadPuzzleMapBoundaryOffsetBottom": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetBottomField(), password),
        "RoadPuzzleMapCenterOffsetX": convert_float(excel_instance.RoadPuzzleMapCenterOffsetXField(), password),
        "RoadPuzzleMapCenterOffsetY": convert_float(excel_instance.RoadPuzzleMapCenterOffsetYField(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngleField(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMaxField(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMinField(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefaultField(), password),
        "StageLoadingProgressTime": convert_float(excel_instance.StageLoadingProgressTimeField(), password),
        "TileRotationDegree": convert_int(excel_instance.TileRotationDegreeField(), password),
        "StartStageIndex": convert_int(excel_instance.StartStageIndexField(), password),
        "LoopStageIndex": convert_int(excel_instance.LoopStageIndexField(), password),
    }

def dump_Excel_ConstMiniGameShootingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NormalStageId": convert_int(excel_instance.NormalStageIdField(), password),
        "NormalSectionCount": convert_int(excel_instance.NormalSectionCountField(), password),
        "HardStageId": convert_int(excel_instance.HardStageIdField(), password),
        "HardSectionCount": convert_int(excel_instance.HardSectionCountField(), password),
        "FreeStageId": convert_int(excel_instance.FreeStageIdField(), password),
        "FreeSectionCount": convert_int(excel_instance.FreeSectionCountField(), password),
        "PlayerCharacterId": [convert_int(excel_instance.PlayerCharacterIdField(j), password) for j in range(excel_instance.PlayerCharacterIdFieldLength())],
        "HiddenPlayerCharacterId": convert_int(excel_instance.HiddenPlayerCharacterIdField(), password),
        "CameraSmoothTime": convert_float(excel_instance.CameraSmoothTimeField(), password),
        "SpawnEffectPath": convert_string(excel_instance.SpawnEffectPathField(), password),
        "WaitTimeAfterSpawn": convert_float(excel_instance.WaitTimeAfterSpawnField(), password),
        "FreeGearInterval": convert_int(excel_instance.FreeGearIntervalField(), password),
    }

def dump_Excel_ConstMinigameTBGExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestMapBoundaryOffsetLeft": convert_float(excel_instance.ConquestMapBoundaryOffsetLeftField(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRightField(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTopField(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottomField(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetXField(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetYField(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngleField(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMaxField(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMinField(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefaultField(), password),
        "ThemaLoadingProgressTime": convert_float(excel_instance.ThemaLoadingProgressTimeField(), password),
        "MapAllyRotation": convert_float(excel_instance.MapAllyRotationField(), password),
        "AniAllyBattleAttack": convert_string(excel_instance.AniAllyBattleAttackField(), password),
        "EffectAllyBattleAttack": convert_string(excel_instance.EffectAllyBattleAttackField(), password),
        "EffectAllyBattleDamage": convert_string(excel_instance.EffectAllyBattleDamageField(), password),
        "AniEnemyBattleAttack": convert_string(excel_instance.AniEnemyBattleAttackField(), password),
        "EffectEnemyBattleAttack": convert_string(excel_instance.EffectEnemyBattleAttackField(), password),
        "EffectEnemyBattleDamage": convert_string(excel_instance.EffectEnemyBattleDamageField(), password),
        "EncounterAllyRotation": convert_float(excel_instance.EncounterAllyRotationField(), password),
        "EncounterEnemyRotation": convert_float(excel_instance.EncounterEnemyRotationField(), password),
        "EncounterRewardReceiveIndex": convert_int(excel_instance.EncounterRewardReceiveIndexField(), password),
    }

def dump_Excel_ConstNewbieContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NewbieGachaReleaseDate": convert_string(excel_instance.NewbieGachaReleaseDateField(), password),
        "NewbieGachaCheckDays": convert_int(excel_instance.NewbieGachaCheckDaysField(), password),
        "NewbieGachaTokenGraceTime": convert_int(excel_instance.NewbieGachaTokenGraceTimeField(), password),
        "NewbieAttendanceReleaseDate": convert_string(excel_instance.NewbieAttendanceReleaseDateField(), password),
        "NewbieAttendanceStartableEndDay": convert_int(excel_instance.NewbieAttendanceStartableEndDayField(), password),
        "NewbieAttendanceEndDay": convert_int(excel_instance.NewbieAttendanceEndDayField(), password),
    }

def dump_Excel_ConstStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "HexaMapBoundaryOffset": convert_float(excel_instance.HexaMapBoundaryOffsetField(), password),
        "HexaMapStartCameraOffset": convert_float(excel_instance.HexaMapStartCameraOffsetField(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMaxField(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMinField(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefaultField(), password),
        "HealCostType": CurrencyTypes(convert_int(excel_instance.HealCostTypeField(), password)).name,
        "HealCostAmount": [convert_int(excel_instance.HealCostAmountField(j), password) for j in range(excel_instance.HealCostAmountFieldLength())],
        "CanHealHpRate": convert_int(excel_instance.CanHealHpRateField(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSecondsField(), password),
        "AdventureEchelonCount": convert_int(excel_instance.AdventureEchelonCountField(), password),
        "RaidEchelonCount": convert_int(excel_instance.RaidEchelonCountField(), password),
        "DefaultEchelonCount": convert_int(excel_instance.DefaultEchelonCountField(), password),
        "EventContentEchelonCount": convert_int(excel_instance.EventContentEchelonCountField(), password),
        "TimeAttackDungeonEchelonCount": convert_int(excel_instance.TimeAttackDungeonEchelonCountField(), password),
        "WorldRaidEchelonCount": convert_int(excel_instance.WorldRaidEchelonCountField(), password),
        "TacticSkipClearTimeSeconds": convert_int(excel_instance.TacticSkipClearTimeSecondsField(), password),
        "TacticSkipFramePerSecond": convert_int(excel_instance.TacticSkipFramePerSecondField(), password),
        "ConquestEchelonCount": convert_int(excel_instance.ConquestEchelonCountField(), password),
        "StoryEchelonCount": convert_int(excel_instance.StoryEchelonCountField(), password),
        "MultiSweepPresetCount": convert_int(excel_instance.MultiSweepPresetCountField(), password),
        "MultiSweepPresetNameMaxLength": convert_int(excel_instance.MultiSweepPresetNameMaxLengthField(), password),
        "MultiSweepPresetNameMaxLengthKr": convert_int(excel_instance.MultiSweepPresetNameMaxLengthKrField(), password),
        "MultiSweepPresetSelectStageMaxCount": convert_int(excel_instance.MultiSweepPresetSelectStageMaxCountField(), password),
        "MultiSweepPresetMaxSweepCount": convert_int(excel_instance.MultiSweepPresetMaxSweepCountField(), password),
        "MultiSweepPresetSelectParcelMaxCount": convert_int(excel_instance.MultiSweepPresetSelectParcelMaxCountField(), password),
    }

def dump_Excel_CouponStuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StuffId": convert_int(excel_instance.StuffIdField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelIdField(), password),
        "LimitAmount": convert_int(excel_instance.LimitAmountField(), password),
        "CouponStuffNameLocalizeKey": convert_string(excel_instance.CouponStuffNameLocalizeKeyField(), password),
    }

def dump_Excel_CumulativeTimeRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Description": convert_string(excel_instance.DescriptionField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "TimeCondition": [convert_int(excel_instance.TimeConditionField(j), password) for j in range(excel_instance.TimeConditionFieldLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardId": [convert_int(excel_instance.RewardIdField(j), password) for j in range(excel_instance.RewardIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_Excel_DefaultCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "FavoriteCharacter": bool(excel_instance.FavoriteCharacterField()),
        "Level": convert_int(excel_instance.LevelField(), password),
        "Exp": convert_int(excel_instance.ExpField(), password),
        "FavorExp": convert_int(excel_instance.FavorExpField(), password),
        "FavorRank": convert_int(excel_instance.FavorRankField(), password),
        "StarGrade": convert_int(excel_instance.StarGradeField(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevelField(), password),
        "PassiveSkillLevel": convert_int(excel_instance.PassiveSkillLevelField(), password),
        "ExtraPassiveSkillLevel": convert_int(excel_instance.ExtraPassiveSkillLevelField(), password),
        "CommonSkillLevel": convert_int(excel_instance.CommonSkillLevelField(), password),
        "LeaderSkillLevel": convert_int(excel_instance.LeaderSkillLevelField(), password),
    }

def dump_Excel_DefaultEchelonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EchlonId": convert_int(excel_instance.EchlonIdField(), password),
        "LeaderId": convert_int(excel_instance.LeaderIdField(), password),
        "MainId": [convert_int(excel_instance.MainIdField(j), password) for j in range(excel_instance.MainIdFieldLength())],
        "SupportId": [convert_int(excel_instance.SupportIdField(j), password) for j in range(excel_instance.SupportIdFieldLength())],
        "TssId": convert_int(excel_instance.TssIdField(), password),
    }

def dump_Excel_DefaultFurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Location": FurnitureLocation(convert_int(excel_instance.LocationField(), password)).name,
        "PositionX": convert_float(excel_instance.PositionXField(), password),
        "PositionY": convert_float(excel_instance.PositionYField(), password),
        "Rotation": convert_float(excel_instance.RotationField(), password),
    }

def dump_Excel_DefaultMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeIdField(), password),
        "MailType": MailType(convert_int(excel_instance.MailTypeField(), password)).name,
        "MailSendPeriodFrom": convert_string(excel_instance.MailSendPeriodFromField(), password),
        "MailSendPeriodTo": convert_string(excel_instance.MailSendPeriodToField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_Excel_DefaultParcelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelIdField(), password),
        "ParcelAmount": convert_int(excel_instance.ParcelAmountField(), password),
    }

def dump_Excel_EmoticonSpecialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "CharacterUniqueId": convert_int(excel_instance.CharacterUniqueIdField(), password),
        "Random": convert_string(excel_instance.RandomField(), password),
    }

def dump_Excel_EventContentBoxGachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "Round": convert_int(excel_instance.RoundField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
    }

def dump_Excel_EventContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "BgImagePath": convert_string(excel_instance.BgImagePathField(), password),
    }

def dump_Excel_FieldContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "AreaId": convert_int(excel_instance.AreaIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficultyField(), password)).name,
        "PrevStageId": convert_int(excel_instance.PrevStageIdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostTypeField(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostIdField(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmountField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "GroundID": convert_int(excel_instance.GroundIDField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "InstantClear": bool(excel_instance.InstantClearField()),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "SkipFormationSettings": bool(excel_instance.SkipFormationSettingsField()),
        "DailyLastPlay": bool(excel_instance.DailyLastPlayField()),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoalField(j), password)).name for j in range(excel_instance.StarGoalFieldLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmountField(j), password) for j in range(excel_instance.StarGoalAmountFieldLength())],
    }

def dump_Excel_FieldContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "RewardProb": convert_int(excel_instance.RewardProbField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_Excel_FieldCurtainCallFreeModeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "OpenDate": convert_int(excel_instance.OpenDateField(), password),
        "SetFieldDateID": convert_int(excel_instance.SetFieldDateIDField(), password),
        "SetFieldQuestOpenDate": convert_int(excel_instance.SetFieldQuestOpenDateField(), password),
    }

def dump_Excel_FieldDateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "OpenDate": convert_int(excel_instance.OpenDateField(), password),
        "DateLocalizeKey": convert_string(excel_instance.DateLocalizeKeyField(), password),
        "EntrySceneId": convert_int(excel_instance.EntrySceneIdField(), password),
        "StartConditionType": FieldConditionType(convert_int(excel_instance.StartConditionTypeField(), password)).name,
        "StartConditionId": convert_int(excel_instance.StartConditionIdField(), password),
        "EndConditionType": FieldConditionType(convert_int(excel_instance.EndConditionTypeField(), password)).name,
        "EndConditionId": convert_int(excel_instance.EndConditionIdField(), password),
        "EndReadyConditionType": FieldConditionType(convert_int(excel_instance.EndReadyConditionTypeField(), password)).name,
        "EndReadyConditionId": convert_int(excel_instance.EndReadyConditionIdField(), password),
        "OpenConditionStage": convert_int(excel_instance.OpenConditionStageField(), password),
        "CharacterIconPath": convert_string(excel_instance.CharacterIconPathField(), password),
        "DateResultBGPath": convert_string(excel_instance.DateResultBGPathField(), password),
        "DateResultSpinePath": convert_string(excel_instance.DateResultSpinePathField(), password),
        "DateResultSpineOffsetX": convert_float(excel_instance.DateResultSpineOffsetXField(), password),
    }

def dump_Excel_FieldEvidenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "NameLocalizeKey": convert_string(excel_instance.NameLocalizeKeyField(), password),
        "DescriptionLocalizeKey": convert_string(excel_instance.DescriptionLocalizeKeyField(), password),
        "DetailLocalizeKey": convert_string(excel_instance.DetailLocalizeKeyField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
    }

def dump_Excel_FieldInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeasonId": convert_long(excel_instance.FieldSeasonIdField(), password),
        "UniqueId": convert_long(excel_instance.UniqueIdField(), password),
        "FieldDateId": convert_long(excel_instance.FieldDateIdField(), password),
        "ShowEmoji": bool(excel_instance.ShowEmojiField()),
        "KeywordLocalize": convert_string(excel_instance.KeywordLocalizeField(), password),
        "InteractionType": [FieldInteractionType(convert_int(excel_instance.InteractionTypeField(j), password)).name for j in range(excel_instance.InteractionTypeFieldLength())],
        "InteractionId": [convert_long(excel_instance.InteractionIdField(j), password) for j in range(excel_instance.InteractionIdFieldLength())],
        "ConditionClass": FieldConditionClass(convert_int(excel_instance.ConditionClassField(), password)).name,
        "ConditionClassParameters": [convert_long(excel_instance.ConditionClassParametersField(j), password) for j in range(excel_instance.ConditionClassParametersFieldLength())],
        "OnceOnly": bool(excel_instance.OnceOnlyField()),
        "ConditionIndex": [convert_long(excel_instance.ConditionIndexField(j), password) for j in range(excel_instance.ConditionIndexFieldLength())],
        "ConditionType": [FieldConditionType(convert_int(excel_instance.ConditionTypeField(j), password)).name for j in range(excel_instance.ConditionTypeFieldLength())],
        "ConditionId": [convert_long(excel_instance.ConditionIdField(j), password) for j in range(excel_instance.ConditionIdFieldLength())],
        "NegateCondition": [bool(excel_instance.NegateConditionField(j)) for j in range(excel_instance.NegateConditionFieldLength())],
    }

def dump_Excel_FieldKeywordExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "NameLocalizeKey": convert_string(excel_instance.NameLocalizeKeyField(), password),
        "DescriptionLocalizeKey": convert_string(excel_instance.DescriptionLocalizeKeyField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
    }

def dump_Excel_FieldMasteryExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "Order": convert_int(excel_instance.OrderField(), password),
        "ExpAmount": convert_int(excel_instance.ExpAmountField(), password),
        "TokenType": ParcelType(convert_int(excel_instance.TokenTypeField(), password)).name,
        "TokenId": convert_int(excel_instance.TokenIdField(), password),
        "TokenRequirement": convert_int(excel_instance.TokenRequirementField(), password),
        "AccomplishmentConditionType": FieldConditionType(convert_int(excel_instance.AccomplishmentConditionTypeField(), password)).name,
        "AccomplishmentConditionId": convert_int(excel_instance.AccomplishmentConditionIdField(), password),
    }

def dump_Excel_FieldMasteryLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "Id": [convert_int(excel_instance.IdField(j), password) for j in range(excel_instance.IdFieldLength())],
        "Exp": [convert_int(excel_instance.ExpField(j), password) for j in range(excel_instance.ExpFieldLength())],
        "TotalExp": [convert_int(excel_instance.TotalExpField(j), password) for j in range(excel_instance.TotalExpFieldLength())],
        "RewardId": [convert_int(excel_instance.RewardIdField(j), password) for j in range(excel_instance.RewardIdFieldLength())],
    }

def dump_Excel_FieldMasteryManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeason": convert_int(excel_instance.FieldSeasonField(), password),
        "LocalizeEtc": convert_uint(excel_instance.LocalizeEtcField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
        "LevelId": convert_int(excel_instance.LevelIdField(), password),
    }

def dump_Excel_FieldQuestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeasonId": convert_int(excel_instance.FieldSeasonIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "IsDaily": bool(excel_instance.IsDailyField()),
        "FieldDateId": convert_int(excel_instance.FieldDateIdField(), password),
        "Opendate": convert_int(excel_instance.OpendateField(), password),
        "QuestGroupId": convert_int(excel_instance.QuestGroupIdField(), password),
        "AssetPath": convert_string(excel_instance.AssetPathField(), password),
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "QuestNamKey": convert_uint(excel_instance.QuestNamKeyField(), password),
        "QuestDescKey": convert_uint(excel_instance.QuestDescKeyField(), password),
    }

def dump_Excel_FieldRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupIdField(), password),
        "RewardProb": convert_int(excel_instance.RewardProbField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_long(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
    }

def dump_Excel_FieldSceneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueIdField(), password),
        "DateId": convert_long(excel_instance.DateIdField(), password),
        "GroupId": convert_long(excel_instance.GroupIdField(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPathField(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPathField(), password),
        "BGMId": convert_long(excel_instance.BGMIdField(), password),
        "ConditionalBGMQuestId": [convert_long(excel_instance.ConditionalBGMQuestIdField(j), password) for j in range(excel_instance.ConditionalBGMQuestIdFieldLength())],
        "BeginConditionalBGMScenarioGroupId": [convert_long(excel_instance.BeginConditionalBGMScenarioGroupIdField(j), password) for j in range(excel_instance.BeginConditionalBGMScenarioGroupIdFieldLength())],
        "BeginConditionalBGMInteractionId": [convert_long(excel_instance.BeginConditionalBGMInteractionIdField(j), password) for j in range(excel_instance.BeginConditionalBGMInteractionIdFieldLength())],
        "EndConditionalBGMScenarioGroupId": [convert_long(excel_instance.EndConditionalBGMScenarioGroupIdField(j), password) for j in range(excel_instance.EndConditionalBGMScenarioGroupIdFieldLength())],
        "EndConditionalBGMInteractionId": [convert_long(excel_instance.EndConditionalBGMInteractionIdField(j), password) for j in range(excel_instance.EndConditionalBGMInteractionIdFieldLength())],
        "ConditionalBGMId": [convert_long(excel_instance.ConditionalBGMIdField(j), password) for j in range(excel_instance.ConditionalBGMIdFieldLength())],
    }

def dump_Excel_FieldSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "FieldContentType": FieldContentType(convert_int(excel_instance.FieldContentTypeField(), password)).name,
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EntryDateId": convert_int(excel_instance.EntryDateIdField(), password),
        "InstantEntryDateId": convert_int(excel_instance.InstantEntryDateIdField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "LobbyBGMChangeStageId": convert_int(excel_instance.LobbyBGMChangeStageIdField(), password),
        "FieldPrefabControlID": convert_int(excel_instance.FieldPrefabControlIDField(), password),
        "FieldGetKeywordCallDialogEnum": FieldDialogType(convert_int(excel_instance.FieldGetKeywordCallDialogEnumField(), password)).name,
        "MasteryImagePath": convert_string(excel_instance.MasteryImagePathField(), password),
        "FieldLobbyTitleImagePath": convert_string(excel_instance.FieldLobbyTitleImagePathField(), password),
        "KeywordLogoImagePath": convert_string(excel_instance.KeywordLogoImagePathField(), password),
    }

def dump_Excel_FieldStoryStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "GroundID": convert_int(excel_instance.GroundIDField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "SkipFormationSettings": bool(excel_instance.SkipFormationSettingsField()),
    }

def dump_Excel_FieldTutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "TutorialType": [FieldTutorialType(convert_int(excel_instance.TutorialTypeField(j), password)).name for j in range(excel_instance.TutorialTypeFieldLength())],
        "ConditionType": [FieldConditionType(convert_int(excel_instance.ConditionTypeField(j), password)).name for j in range(excel_instance.ConditionTypeFieldLength())],
        "ConditionId": [convert_int(excel_instance.ConditionIdField(j), password) for j in range(excel_instance.ConditionIdFieldLength())],
    }

def dump_Excel_FieldWorldMapZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "Date": convert_int(excel_instance.DateField(), password),
        "OpenConditionType": FieldConditionType(convert_int(excel_instance.OpenConditionTypeField(), password)).name,
        "OpenConditionId": convert_int(excel_instance.OpenConditionIdField(), password),
        "CloseConditionType": FieldConditionType(convert_int(excel_instance.CloseConditionTypeField(), password)).name,
        "CloseConditionId": convert_int(excel_instance.CloseConditionIdField(), password),
        "ResultFieldScene": convert_int(excel_instance.ResultFieldSceneField(), password),
        "FieldStageInteractionId": convert_int(excel_instance.FieldStageInteractionIdField(), password),
        "WorldMapButtonType": FieldWorldMapButtonType(convert_int(excel_instance.WorldMapButtonTypeField(), password)).name,
        "LocalizeCode": convert_uint(excel_instance.LocalizeCodeField(), password),
        "NewTagDisplay": bool(excel_instance.NewTagDisplayField()),
    }

def dump_Excel_GroundGridFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.XField(), password),
        "Y": convert_int(excel_instance.YField(), password),
        "StartX": convert_float(excel_instance.StartXField(), password),
        "StartY": convert_float(excel_instance.StartYField(), password),
        "Gap": convert_float(excel_instance.GapField(), password),
        "Nodes": [excel_instance.NodesField(j) for j in range(excel_instance.NodesFieldLength())],
        "Version": convert_string(excel_instance.VersionField(), password),
    }

def dump_Excel_GroundNodeFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.XField(), password),
        "Y": convert_int(excel_instance.YField(), password),
        "IsCanNotUseSkill": bool(excel_instance.IsCanNotUseSkillField()),
        "Position": excel_instance.PositionField(),
        "NodeType": GroundNodeType(convert_int(excel_instance.NodeTypeField(), password)).name,
        "OriginalNodeType": GroundNodeType(convert_int(excel_instance.OriginalNodeTypeField(), password)).name,
    }

def dump_Excel_GroundNodeLayerFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "Layers": [excel_instance.LayersField(j) for j in range(excel_instance.LayersFieldLength())],
    }

def dump_Excel_KatakanaConvertExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
    }

def dump_Excel_KnockBackExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_int(excel_instance.IndexField(), password),
        "Dist": convert_float(excel_instance.DistField(), password),
        "Speed": convert_float(excel_instance.SpeedField(), password),
    }

def dump_Excel_LimitedStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficultyField(), password)).name,
        "StageNumber": convert_string(excel_instance.StageNumberField(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplayField(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageIdField(), password),
        "OpenDate": convert_int(excel_instance.OpenDateField(), password),
        "OpenEventPoint": convert_int(excel_instance.OpenEventPointField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostTypeField(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostIdField(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmountField(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCountField(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCountField(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCountField(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupIdField(j), password) for j in range(excel_instance.EnterScenarioGroupIdFieldLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupIdField(j), password) for j in range(excel_instance.ClearScenarioGroupIdFieldLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMapField(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBGField(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardIdField(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurnField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "BgmId": convert_int(excel_instance.BgmIdField(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironmentField(), password)).name,
        "GroundID": convert_int(excel_instance.GroundIDField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "InstantClear": bool(excel_instance.InstantClearField()),
        "BuffContentId": convert_int(excel_instance.BuffContentIdField(), password),
        "ChallengeDisplay": bool(excel_instance.ChallengeDisplayField()),
    }

def dump_Excel_LimitedStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "RewardProb": convert_int(excel_instance.RewardProbField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_Excel_LimitedStageSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "TypeACount": convert_int(excel_instance.TypeACountField(), password),
        "TypeBCount": convert_int(excel_instance.TypeBCountField(), password),
        "TypeCCount": convert_int(excel_instance.TypeCCountField(), password),
    }

def dump_Excel_MinigameCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [CCGCharacterType(convert_int(excel_instance.NoneField(j), password)).name for j in range(excel_instance.NoneFieldLength())],
    }

def dump_Excel_MinigameRoadExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [RoadPuzzleMapTileType(convert_int(excel_instance.NoneField(j), password)).name for j in range(excel_instance.NoneFieldLength())],
    }

def dump_Excel_NormalSkillTemplateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_int(excel_instance.IndexField(), password),
        "FirstCoolTime": convert_float(excel_instance.FirstCoolTimeField(), password),
        "CoolTime": convert_float(excel_instance.CoolTimeField(), password),
        "MultiAni": bool(excel_instance.MultiAniField()),
    }

def dump_Excel_ObstacleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_int(excel_instance.IndexField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "JumpAble": bool(excel_instance.JumpAbleField()),
        "SubOffset": [convert_float(excel_instance.SubOffsetField(j), password) for j in range(excel_instance.SubOffsetFieldLength())],
        "X": convert_float(excel_instance.XField(), password),
        "Z": convert_float(excel_instance.ZField(), password),
        "Hp": convert_int(excel_instance.HpField(), password),
        "MaxHp": convert_int(excel_instance.MaxHpField(), password),
        "BlockRate": convert_int(excel_instance.BlockRateField(), password),
        "EvasionRate": convert_int(excel_instance.EvasionRateField(), password),
        "DestroyType": ObstacleDestroyType(convert_int(excel_instance.DestroyTypeField(), password)).name,
        "Point1Offeset": [convert_float(excel_instance.Point1OffesetField(j), password) for j in range(excel_instance.Point1OffesetFieldLength())],
        "EnemyPoint1Osset": [convert_float(excel_instance.EnemyPoint1OssetField(j), password) for j in range(excel_instance.EnemyPoint1OssetFieldLength())],
        "Point2Offeset": [convert_float(excel_instance.Point2OffesetField(j), password) for j in range(excel_instance.Point2OffesetFieldLength())],
        "EnemyPoint2Osset": [convert_float(excel_instance.EnemyPoint2OssetField(j), password) for j in range(excel_instance.EnemyPoint2OssetFieldLength())],
        "SubObstacleID": [convert_int(excel_instance.SubObstacleIDField(j), password) for j in range(excel_instance.SubObstacleIDFieldLength())],
    }

def dump_Excel_PropVector3(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.XField(), password),
        "Y": convert_float(excel_instance.YField(), password),
        "Z": convert_float(excel_instance.ZField(), password),
    }

def dump_Excel_PropMotion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.NameField(), password),
        "Positions": [excel_instance.PositionsField(j) for j in range(excel_instance.PositionsFieldLength())],
        "Rotations": [excel_instance.RotationsField(j) for j in range(excel_instance.RotationsFieldLength())],
    }

def dump_Excel_PropRootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "RootMotions": [excel_instance.RootMotionsField(j) for j in range(excel_instance.RootMotionsFieldLength())],
    }

def dump_Excel_ProtocolSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Protocol": convert_string(excel_instance.ProtocolField(), password),
        "OpenConditionContent": OpenConditionContent(convert_int(excel_instance.OpenConditionContentField(), password)).name,
        "Currency": bool(excel_instance.CurrencyField()),
        "Inventory": bool(excel_instance.InventoryField()),
        "Mail": bool(excel_instance.MailField()),
    }

def dump_Excel_RecipeCraftExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeTypeField(), password)).name,
        "RecipeIngredientId": convert_int(excel_instance.RecipeIngredientIdField(), password),
        "RecipeIngredientDevName": convert_string(excel_instance.RecipeIngredientDevNameField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelDevName": [convert_string(excel_instance.ParcelDevNameField(j), password) for j in range(excel_instance.ParcelDevNameFieldLength())],
        "ResultAmountMin": [convert_int(excel_instance.ResultAmountMinField(j), password) for j in range(excel_instance.ResultAmountMinFieldLength())],
        "ResultAmountMax": [convert_int(excel_instance.ResultAmountMaxField(j), password) for j in range(excel_instance.ResultAmountMaxFieldLength())],
    }

def dump_Excel_Position(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.XField(), password),
        "Z": convert_float(excel_instance.ZField(), password),
    }

def dump_Excel_Motion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.NameField(), password),
        "Positions": [excel_instance.PositionsField(j) for j in range(excel_instance.PositionsFieldLength())],
    }

def dump_Excel_MoveEnd(excel_instance, password: bytes = b"") -> dict:
    return {
        "Normal": excel_instance.NormalField(),
        "Stand": excel_instance.StandField(),
        "Kneel": excel_instance.KneelField(),
    }

def dump_Excel_Form(excel_instance, password: bytes = b"") -> dict:
    return {
        "MoveEnd": excel_instance.MoveEndField(),
        "PublicSkill": excel_instance.PublicSkillField(),
    }

def dump_Excel_RootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "Forms": [excel_instance.FormsField(j) for j in range(excel_instance.FormsFieldLength())],
        "ExSkills": [excel_instance.ExSkillsField(j) for j in range(excel_instance.ExSkillsFieldLength())],
        "MoveLeft": excel_instance.MoveLeftField(),
        "MoveRight": excel_instance.MoveRightField(),
    }

def dump_Excel_ScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [ScenarioBGType(convert_int(excel_instance.NoneField(j), password)).name for j in range(excel_instance.NoneFieldLength())],
        "Idle": [ScenarioCharacterAction(convert_int(excel_instance.IdleField(j), password)).name for j in range(excel_instance.IdleFieldLength())],
        "Cafe": DialogCategory(convert_int(excel_instance.CafeField(), password)).name,
        "Talk": DialogType(convert_int(excel_instance.TalkField(), password)).name,
        "Open": StoryCondition(convert_int(excel_instance.OpenField(), password)).name,
        "EnterConver": EmojiEvent(convert_int(excel_instance.EnterConverField(), password)).name,
        "Center": ScenarioZoomAnchors(convert_int(excel_instance.CenterField(), password)).name,
        "Instant": ScenarioZoomType(convert_int(excel_instance.InstantField(), password)).name,
        "Prologue": ScenarioContentType(convert_int(excel_instance.PrologueField(), password)).name,
    }

def dump_Excel_ScenarioReplayExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_int(excel_instance.ModeIdField(), password),
        "VolumeId": convert_int(excel_instance.VolumeIdField(), password),
        "ReplayType": ScenarioModeReplayTypes(convert_int(excel_instance.ReplayTypeField(), password)).name,
        "ChapterId": convert_int(excel_instance.ChapterIdField(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeIdField(), password),
        "FrontScenarioGroupId": [convert_int(excel_instance.FrontScenarioGroupIdField(j), password) for j in range(excel_instance.FrontScenarioGroupIdFieldLength())],
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "BackScenarioGroupId": [convert_int(excel_instance.BackScenarioGroupIdField(j), password) for j in range(excel_instance.BackScenarioGroupIdFieldLength())],
    }

def dump_Excel_SpecialLobbyIllustExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "CharacterCostumeUniqueId": convert_int(excel_instance.CharacterCostumeUniqueIdField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "SlotTextureName": convert_string(excel_instance.SlotTextureNameField(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureNameField(), password),
    }

def dump_Excel_StringTestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "String": [convert_string(excel_instance.StringField(j), password) for j in range(excel_instance.StringFieldLength())],
        "Sentence1": convert_string(excel_instance.Sentence1Field(), password),
        "Script": convert_string(excel_instance.ScriptField(), password),
    }

def dump_Excel_SystemMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MailType": MailType(convert_int(excel_instance.MailTypeField(), password)).name,
        "IsProductMail": bool(excel_instance.IsProductMailField()),
        "IsVariableExpiredDay": bool(excel_instance.IsVariableExpiredDayField()),
        "ExpiredDay": convert_int(excel_instance.ExpiredDayField(), password),
        "Sender": convert_string(excel_instance.SenderField(), password),
        "Comment": convert_string(excel_instance.CommentField(), password),
    }

def dump_Excel_TacticArenaSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.OrderField(), password),
        "Repeat": convert_int(excel_instance.RepeatField(), password),
        "AttackerFrom": ArenaSimulatorServer(convert_int(excel_instance.AttackerFromField(), password)).name,
        "AttackerUserArenaGroup": convert_int(excel_instance.AttackerUserArenaGroupField(), password),
        "AttackerUserArenaRank": convert_int(excel_instance.AttackerUserArenaRankField(), password),
        "AttackerPresetGroupId": convert_int(excel_instance.AttackerPresetGroupIdField(), password),
        "AttackerStrikerNum": convert_int(excel_instance.AttackerStrikerNumField(), password),
        "AttackerSpecialNum": convert_int(excel_instance.AttackerSpecialNumField(), password),
        "DefenderFrom": ArenaSimulatorServer(convert_int(excel_instance.DefenderFromField(), password)).name,
        "DefenderUserArenaGroup": convert_int(excel_instance.DefenderUserArenaGroupField(), password),
        "DefenderUserArenaRank": convert_int(excel_instance.DefenderUserArenaRankField(), password),
        "DefenderPresetGroupId": convert_int(excel_instance.DefenderPresetGroupIdField(), password),
        "DefenderStrikerNum": convert_int(excel_instance.DefenderStrikerNumField(), password),
        "DefenderSpecialNum": convert_int(excel_instance.DefenderSpecialNumField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
    }

def dump_Excel_TacticDamageSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.OrderField(), password),
        "Repeat": convert_int(excel_instance.RepeatField(), password),
        "TestPreset": convert_int(excel_instance.TestPresetField(), password),
        "TestBattleTime": convert_int(excel_instance.TestBattleTimeField(), password),
        "StrikerSquard": convert_int(excel_instance.StrikerSquardField(), password),
        "SpecialSquard": convert_int(excel_instance.SpecialSquardField(), password),
        "ReplaceCharacterCostRegen": bool(excel_instance.ReplaceCharacterCostRegenField()),
        "ReplaceCostRegenValue": convert_int(excel_instance.ReplaceCostRegenValueField(), password),
        "UseAutoSkill": bool(excel_instance.UseAutoSkillField()),
        "OverrideStreetAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideStreetAdaptationField(), password)).name,
        "OverrideOutdoorAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideOutdoorAdaptationField(), password)).name,
        "OverrideIndoorAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideIndoorAdaptationField(), password)).name,
        "ApplyOverrideAdaptation": bool(excel_instance.ApplyOverrideAdaptationField()),
        "OverrideFavorLevel": convert_int(excel_instance.OverrideFavorLevelField(), password),
        "ApplyOverrideFavorLevel": bool(excel_instance.ApplyOverrideFavorLevelField()),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "FixedCharacter": [convert_int(excel_instance.FixedCharacterField(j), password) for j in range(excel_instance.FixedCharacterFieldLength())],
    }

def dump_Excel_TacticSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
    }

def dump_Excel_TacticTimeAttackSimulatorConfigExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.OrderField(), password),
        "Repeat": convert_int(excel_instance.RepeatField(), password),
        "PresetGroupId": convert_int(excel_instance.PresetGroupIdField(), password),
        "AttackStrikerNum": convert_int(excel_instance.AttackStrikerNumField(), password),
        "AttackSpecialNum": convert_int(excel_instance.AttackSpecialNumField(), password),
        "GeasId": convert_int(excel_instance.GeasIdField(), password),
    }

def dump_Excel_TagExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Furniture": Tag(convert_int(excel_instance.FurnitureField(), password)).name,
        "None_": Club(convert_int(excel_instance.NoneField(), password)).name,
    }

def dump_Excel_TranscendenceRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "CostCurrencyType": CurrencyTypes(convert_int(excel_instance.CostCurrencyTypeField(), password)).name,
        "CostCurrencyAmount": convert_int(excel_instance.CostCurrencyAmountField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
    }

def dump_Excel_VoiceSkillUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.NameField(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHashField(j), password) for j in range(excel_instance.VoiceHashFieldLength())],
    }

def dump_Excel_WeekDungeonFindGiftRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageRewardId": convert_int(excel_instance.StageRewardIdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
        "RewardParcelProbability": [convert_int(excel_instance.RewardParcelProbabilityField(j), password) for j in range(excel_instance.RewardParcelProbabilityFieldLength())],
        "DropItemModelPrefabPath": [convert_string(excel_instance.DropItemModelPrefabPathField(j), password) for j in range(excel_instance.DropItemModelPrefabPathFieldLength())],
    }

def dump_ExcelDB_AcademyFavorScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "ScheduleGroupId": convert_int(excel_instance.ScheduleGroupIdField(), password),
        "OrderInGroup": convert_int(excel_instance.OrderInGroupField(), password),
        "Location": convert_string(excel_instance.LocationField(), password),
        "LocalizeScenarioId": convert_uint(excel_instance.LocalizeScenarioIdField(), password),
        "FavorRank": convert_int(excel_instance.FavorRankField(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmountField(), password),
        "ScenarioSriptGroupId": convert_int(excel_instance.ScenarioSriptGroupIdField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_AcademyLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPathField(), password),
        "IconImagePath": convert_string(excel_instance.IconImagePathField(), password),
        "OpenCondition": [School(convert_int(excel_instance.OpenConditionField(j), password)).name for j in range(excel_instance.OpenConditionFieldLength())],
        "OpenConditionCount": [convert_int(excel_instance.OpenConditionCountField(j), password) for j in range(excel_instance.OpenConditionCountFieldLength())],
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "OpenTeacherRank": convert_int(excel_instance.OpenTeacherRankField(), password),
    }

def dump_ExcelDB_AcademyLocationRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Rank": convert_int(excel_instance.RankField(), password),
        "RankExp": convert_int(excel_instance.RankExpField(), password),
        "TotalExp": convert_int(excel_instance.TotalExpField(), password),
    }

def dump_ExcelDB_AcademyMessangerExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_int(excel_instance.MessageGroupIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageConditionField(), password)).name,
        "ConditionValue": convert_int(excel_instance.ConditionValueField(), password),
        "PreConditionGroupId": convert_int(excel_instance.PreConditionGroupIdField(), password),
        "PreConditionFavorScheduleId": convert_int(excel_instance.PreConditionFavorScheduleIdField(), password),
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleIdField(), password),
        "NextGroupId": convert_int(excel_instance.NextGroupIdField(), password),
        "FeedbackTimeMillisec": convert_int(excel_instance.FeedbackTimeMillisecField(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageTypeField(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
        "MessageKR": convert_string(excel_instance.MessageKRField(), password),
        "MessageJP": convert_string(excel_instance.MessageJPField(), password),
        "MessageTH": convert_string(excel_instance.MessageTHField(), password),
        "MessageTW": convert_string(excel_instance.MessageTWField(), password),
        "MessageEN": convert_string(excel_instance.MessageENField(), password),
    }

def dump_ExcelDB_AcademyRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Location": convert_string(excel_instance.LocationField(), password),
        "ScheduleGroupId": convert_int(excel_instance.ScheduleGroupIdField(), password),
        "OrderInGroup": convert_int(excel_instance.OrderInGroupField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "ProgressTexture": convert_string(excel_instance.ProgressTextureField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "LocationRank": convert_int(excel_instance.LocationRankField(), password),
        "FavorExp": convert_int(excel_instance.FavorExpField(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmountField(), password),
        "SecretStoneProb": convert_int(excel_instance.SecretStoneProbField(), password),
        "ExtraFavorExp": convert_int(excel_instance.ExtraFavorExpField(), password),
        "ExtraFavorExpProb": convert_int(excel_instance.ExtraFavorExpProbField(), password),
        "ExtraRewardParcelType": [ParcelType(convert_int(excel_instance.ExtraRewardParcelTypeField(j), password)).name for j in range(excel_instance.ExtraRewardParcelTypeFieldLength())],
        "ExtraRewardParcelId": [convert_int(excel_instance.ExtraRewardParcelIdField(j), password) for j in range(excel_instance.ExtraRewardParcelIdFieldLength())],
        "ExtraRewardAmount": [convert_int(excel_instance.ExtraRewardAmountField(j), password) for j in range(excel_instance.ExtraRewardAmountFieldLength())],
        "ExtraRewardProb": [convert_int(excel_instance.ExtraRewardProbField(j), password) for j in range(excel_instance.ExtraRewardProbFieldLength())],
        "IsExtraRewardDisplayed": [bool(excel_instance.IsExtraRewardDisplayedField(j)) for j in range(excel_instance.IsExtraRewardDisplayedFieldLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_AcademyTicketExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocationRankSum": convert_int(excel_instance.LocationRankSumField(), password),
        "ScheduleTicktetMax": convert_int(excel_instance.ScheduleTicktetMaxField(), password),
    }

def dump_ExcelDB_AcademyZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocationId": convert_int(excel_instance.LocationIdField(), password),
        "LocationRankForUnlock": convert_int(excel_instance.LocationRankForUnlockField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "StudentVisitProb": [convert_int(excel_instance.StudentVisitProbField(j), password) for j in range(excel_instance.StudentVisitProbFieldLength())],
        "RewardGroupId": convert_int(excel_instance.RewardGroupIdField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
    }

def dump_ExcelDB_AccountLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "Exp": convert_int(excel_instance.ExpField(), password),
        "NewbieExpRatio": convert_int(excel_instance.NewbieExpRatioField(), password),
        "CloseInterval": convert_int(excel_instance.CloseIntervalField(), password),
        "APAutoChargeMax": convert_int(excel_instance.APAutoChargeMaxField(), password),
        "NeedReportEvent": bool(excel_instance.NeedReportEventField()),
    }

def dump_ExcelDB_AccountLevelRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_AlertPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CheckConfirmAble": bool(excel_instance.CheckConfirmAbleField()),
        "SystemPopupTitle": convert_uint(excel_instance.SystemPopupTitleField(), password),
        "SystemPopupDescription": convert_uint(excel_instance.SystemPopupDescriptionField(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitleField(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescriptionField(), password),
        "PopupType": SpoilerPopupType(convert_int(excel_instance.PopupTypeField(), password)).name,
    }

def dump_ExcelDB_ArenaLevelSectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ArenaSeasonId": convert_int(excel_instance.ArenaSeasonIdField(), password),
        "StartLevel": convert_int(excel_instance.StartLevelField(), password),
        "LastLevel": convert_int(excel_instance.LastLevelField(), password),
        "UserCount": convert_int(excel_instance.UserCountField(), password),
    }

def dump_ExcelDB_ArenaMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ArenaSeasonId": convert_int(excel_instance.ArenaSeasonIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "TerrainType": convert_int(excel_instance.TerrainTypeField(), password),
        "TerrainTypeLocalizeKey": convert_string(excel_instance.TerrainTypeLocalizeKeyField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
        "GroundGroupId": convert_int(excel_instance.GroundGroupIdField(), password),
        "GroundGroupNameLocalizeKey": convert_string(excel_instance.GroundGroupNameLocalizeKeyField(), password),
        "StartRank": convert_int(excel_instance.StartRankField(), password),
        "EndRank": convert_int(excel_instance.EndRankField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
    }

def dump_ExcelDB_ArenaNPCExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "Rank": convert_int(excel_instance.RankField(), password),
        "NPCAccountLevel": convert_int(excel_instance.NPCAccountLevelField(), password),
        "NPCLevel": convert_int(excel_instance.NPCLevelField(), password),
        "NPCLevelDeviation": convert_int(excel_instance.NPCLevelDeviationField(), password),
        "NPCStarGrade": convert_int(excel_instance.NPCStarGradeField(), password),
        "ExceptionCharacterRarities": [Rarity(convert_int(excel_instance.ExceptionCharacterRaritiesField(j), password)).name for j in range(excel_instance.ExceptionCharacterRaritiesFieldLength())],
        "ExceptionMainCharacterIds": [convert_int(excel_instance.ExceptionMainCharacterIdsField(j), password) for j in range(excel_instance.ExceptionMainCharacterIdsFieldLength())],
        "ExceptionSupportCharacterIds": [convert_int(excel_instance.ExceptionSupportCharacterIdsField(j), password) for j in range(excel_instance.ExceptionSupportCharacterIdsFieldLength())],
        "ExceptionTSSIds": [convert_int(excel_instance.ExceptionTSSIdsField(j), password) for j in range(excel_instance.ExceptionTSSIdsFieldLength())],
    }

def dump_ExcelDB_ArenaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "ArenaRewardType": ArenaRewardType(convert_int(excel_instance.ArenaRewardTypeField(), password)).name,
        "RankStart": convert_int(excel_instance.RankStartField(), password),
        "RankEnd": convert_int(excel_instance.RankEndField(), password),
        "RankIconPath": convert_string(excel_instance.RankIconPathField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_ArenaSeasonCloseRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "RankStart": convert_int(excel_instance.RankStartField(), password),
        "RankEnd": convert_int(excel_instance.RankEndField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_ArenaSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDateField(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDateField(), password),
        "SeasonGroupLimit": convert_int(excel_instance.SeasonGroupLimitField(), password),
        "PrevSeasonId": convert_int(excel_instance.PrevSeasonIdField(), password),
        "InformationGroupId": convert_int(excel_instance.InformationGroupIdField(), password),
    }

def dump_ExcelDB_AssistEchelonTypeConvertExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Contents": EchelonType(convert_int(excel_instance.ContentsField(), password)).name,
        "ConvertTo": EchelonType(convert_int(excel_instance.ConvertToField(), password)).name,
    }

def dump_ExcelDB_AssistRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RewardType": AssistRewardType(convert_int(excel_instance.RewardTypeField(), password)).name,
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonTypeField(), password)).name,
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_AssistSlotExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SlotId": convert_int(excel_instance.SlotIdField(), password),
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonTypeField(), password)).name,
        "SlotNumber": convert_int(excel_instance.SlotNumberField(), password),
        "AssistTermRewardPeriodFromSec": convert_int(excel_instance.AssistTermRewardPeriodFromSecField(), password),
        "AssistRewardLimit": convert_int(excel_instance.AssistRewardLimitField(), password),
        "AssistRentRewardDailyMaxCount": convert_int(excel_instance.AssistRentRewardDailyMaxCountField(), password),
        "AssistRentalFeeAmount": convert_int(excel_instance.AssistRentalFeeAmountField(), password),
        "AssistRentalFeeAmountStranger": convert_int(excel_instance.AssistRentalFeeAmountStrangerField(), password),
    }

def dump_ExcelDB_AttendanceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Type": AttendanceType(convert_int(excel_instance.TypeField(), password)).name,
        "CountdownPrefab": convert_string(excel_instance.CountdownPrefabField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimitField(), password),
        "Title": convert_string(excel_instance.TitleField(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCodeField(), password),
        "CountRule": AttendanceCountRule(convert_int(excel_instance.CountRuleField(), password)).name,
        "CountReset": AttendanceResetType(convert_int(excel_instance.CountResetField(), password)).name,
        "BookSize": convert_int(excel_instance.BookSizeField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDateField(), password),
        "MailType": MailType(convert_int(excel_instance.MailTypeField(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategoryField(), password)).name,
        "TitleImagePath": convert_string(excel_instance.TitleImagePathField(), password),
        "DecorationImagePath": convert_string(excel_instance.DecorationImagePathField(), password),
        "DecorationGarlandImagePath": convert_string(excel_instance.DecorationGarlandImagePathField(), password),
    }

def dump_ExcelDB_AttendanceRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttendanceId": convert_int(excel_instance.AttendanceIdField(), password),
        "Day": convert_int(excel_instance.DayField(), password),
        "RewardIcon": convert_string(excel_instance.RewardIconField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardId": [convert_int(excel_instance.RewardIdField(j), password) for j in range(excel_instance.RewardIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_AudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHashField(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefixField(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHashField(), password),
        "StateName": convert_string(excel_instance.StateNameField(), password),
        "IgnoreInterruptDelay": bool(excel_instance.IgnoreInterruptDelayField()),
        "IgnoreInterruptPlay": bool(excel_instance.IgnoreInterruptPlayField()),
        "IgnoreVelocity": bool(excel_instance.IgnoreVelocityField()),
        "Volume": convert_float(excel_instance.VolumeField(), password),
        "Delay": convert_float(excel_instance.DelayField(), password),
        "RandomPitchMin": convert_int(excel_instance.RandomPitchMinField(), password),
        "RandomPitchMax": convert_int(excel_instance.RandomPitchMaxField(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriorityField(), password),
        "AudioClipPath": [convert_string(excel_instance.AudioClipPathField(j), password) for j in range(excel_instance.AudioClipPathFieldLength())],
        "VoiceHash": [convert_uint(excel_instance.VoiceHashField(j), password) for j in range(excel_instance.VoiceHashFieldLength())],
    }

def dump_ExcelDB_BattleLevelFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiffField(), password),
        "DamageRate": convert_int(excel_instance.DamageRateField(), password),
    }

def dump_ExcelDB_BattlePassExpLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BattlePassId": convert_int(excel_instance.BattlePassIdField(), password),
        "LimitStartTime": convert_string(excel_instance.LimitStartTimeField(), password),
        "LimitEndTime": convert_string(excel_instance.LimitEndTimeField(), password),
        "ExpLimitAmount": convert_int(excel_instance.ExpLimitAmountField(), password),
    }

def dump_ExcelDB_BattlePassFlavorTextExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "TextGroup": convert_int(excel_instance.TextGroupField(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeIdField(), password),
        "Sort": convert_int(excel_instance.SortField(), password),
    }

def dump_ExcelDB_BattlePassInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "FreeRewardGroupID": convert_int(excel_instance.FreeRewardGroupIDField(), password),
        "PurchaseRewardGroupID": convert_int(excel_instance.PurchaseRewardGroupIDField(), password),
        "NormalProductGroupID": convert_int(excel_instance.NormalProductGroupIDField(), password),
        "PremiumProductGroupID": convert_int(excel_instance.PremiumProductGroupIDField(), password),
        "DiscountPremiumProductGroupID": convert_int(excel_instance.DiscountPremiumProductGroupIDField(), password),
        "NextLvNeedExp": convert_int(excel_instance.NextLvNeedExpField(), password),
        "PassLvUpGoodsID": convert_int(excel_instance.PassLvUpGoodsIDField(), password),
        "BuyPremiumLvUpAmount": convert_int(excel_instance.BuyPremiumLvUpAmountField(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFromField(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodToField(), password),
        "VideoId": [convert_int(excel_instance.VideoIdField(j), password) for j in range(excel_instance.VideoIdFieldLength())],
        "FlavorTextGroupID": convert_int(excel_instance.FlavorTextGroupIDField(), password),
        "ExclusiveRewardID": convert_int(excel_instance.ExclusiveRewardIDField(), password),
        "ExclusiveEmblemID": convert_int(excel_instance.ExclusiveEmblemIDField(), password),
        "PassExpLocalizeEtcId": convert_uint(excel_instance.PassExpLocalizeEtcIdField(), password),
        "LobbyBannerPath": convert_string(excel_instance.LobbyBannerPathField(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPathField(), password),
        "PurchaseStepProductImagePath": convert_string(excel_instance.PurchaseStepProductImagePathField(), password),
    }

def dump_ExcelDB_BattlePassLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BattlePassId": convert_int(excel_instance.BattlePassIdField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "IsPickUpReward": bool(excel_instance.IsPickUpRewardField()),
    }

def dump_ExcelDB_BattlePassMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BattlePassId": convert_int(excel_instance.BattlePassIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "Category": MissionCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "PreMissionId": [convert_int(excel_instance.PreMissionIdField(j), password) for j in range(excel_instance.PreMissionIdFieldLength())],
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetTypeField(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayTypeField(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePathField(), password),
        "ViewFlag": bool(excel_instance.ViewFlagField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUIField(j), password) for j in range(excel_instance.ShortcutUIFieldLength())],
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcutField(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionTypeField(), password)).name,
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCountField(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameterField(j), password) for j in range(excel_instance.CompleteConditionParameterFieldLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTagField(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagFieldLength())],
        "BattlePassExpAmount": convert_int(excel_instance.BattlePassExpAmountField(), password),
    }

def dump_ExcelDB_BattlePassRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupIdField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelUniqueId": convert_int(excel_instance.RewardParcelUniqueIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_BGMExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Nation": [Nation(convert_int(excel_instance.NationField(j), password)).name for j in range(excel_instance.NationFieldLength())],
        "Path": [convert_string(excel_instance.PathField(j), password) for j in range(excel_instance.PathFieldLength())],
        "Volume": [convert_float(excel_instance.VolumeField(j), password) for j in range(excel_instance.VolumeFieldLength())],
        "LoopStartTime": [convert_float(excel_instance.LoopStartTimeField(j), password) for j in range(excel_instance.LoopStartTimeFieldLength())],
        "LoopEndTime": [convert_float(excel_instance.LoopEndTimeField(j), password) for j in range(excel_instance.LoopEndTimeFieldLength())],
        "LoopTranstionTime": [convert_float(excel_instance.LoopTranstionTimeField(j), password) for j in range(excel_instance.LoopTranstionTimeFieldLength())],
        "LoopOffsetTime": [convert_float(excel_instance.LoopOffsetTimeField(j), password) for j in range(excel_instance.LoopOffsetTimeFieldLength())],
    }

def dump_ExcelDB_BGMRaidExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageIdField(), password),
        "PhaseIndex": convert_int(excel_instance.PhaseIndexField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
    }

def dump_ExcelDB_BGMUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UIPrefab": convert_uint(excel_instance.UIPrefabField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "BGMId2nd": convert_int(excel_instance.BGMId2NdField(), password),
        "BGMId3rd": convert_int(excel_instance.BGMId3RdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
    }

def dump_ExcelDB_BGM_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupBGMId": convert_int(excel_instance.GroupBGMIdField(), password),
        "BGMIdKr": convert_int(excel_instance.BGMIdKrField(), password),
        "BGMIdJp": convert_int(excel_instance.BGMIdJpField(), password),
        "BGMIdTh": convert_int(excel_instance.BGMIdThField(), password),
        "BGMIdTw": convert_int(excel_instance.BGMIdTwField(), password),
        "BGMIdEn": convert_int(excel_instance.BGMIdEnField(), password),
    }

def dump_ExcelDB_BossExternalBTExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ExternalBTId": convert_int(excel_instance.ExternalBTIdField(), password),
        "AIPhase": convert_int(excel_instance.AIPhaseField(), password),
        "ExternalBTNodeType": ExternalBTNodeType(convert_int(excel_instance.ExternalBTNodeTypeField(), password)).name,
        "ExternalBTTrigger": ExternalBTTrigger(convert_int(excel_instance.ExternalBTTriggerField(), password)).name,
        "TriggerArgument": convert_string(excel_instance.TriggerArgumentField(), password),
        "BehaviorRate": convert_int(excel_instance.BehaviorRateField(), password),
        "ExternalBehavior": ExternalBehavior(convert_int(excel_instance.ExternalBehaviorField(), password)).name,
        "BehaviorArgument": convert_string(excel_instance.BehaviorArgumentField(), password),
    }

def dump_ExcelDB_BulletArmorDamageFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupIdField(), password),
        "BulletType": BulletType(convert_int(excel_instance.BulletTypeField(), password)).name,
        "ArmorType": ArmorType(convert_int(excel_instance.ArmorTypeField(), password)).name,
        "DamageRate": convert_int(excel_instance.DamageRateField(), password),
        "DamageAttribute": DamageAttribute(convert_int(excel_instance.DamageAttributeField(), password)).name,
        "MinDamageRate": convert_int(excel_instance.MinDamageRateField(), password),
        "MaxDamageRate": convert_int(excel_instance.MaxDamageRateField(), password),
        "ShowHighlightFloater": bool(excel_instance.ShowHighlightFloaterField()),
    }

def dump_ExcelDB_CafeInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeIdField(), password),
        "IsDefault": bool(excel_instance.IsDefaultField()),
        "OpenConditionCafeId": OpenConditionContent(convert_int(excel_instance.OpenConditionCafeIdField(), password)).name,
        "OpenConditionCafeInvite": OpenConditionContent(convert_int(excel_instance.OpenConditionCafeInviteField(), password)).name,
        "SummonParcelType": ParcelType(convert_int(excel_instance.SummonParcelTypeField(), password)).name,
        "SummonParcelId": convert_int(excel_instance.SummonParcelIdField(), password),
        "SummonParcelAmount": convert_int(excel_instance.SummonParcelAmountField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "SummonTicketIconPath": convert_string(excel_instance.SummonTicketIconPathField(), password),
    }

def dump_ExcelDB_CafeInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "IgnoreIfUnobtained": bool(excel_instance.IgnoreIfUnobtainedField()),
        "IgnoreIfUnobtainedStartDate": convert_string(excel_instance.IgnoreIfUnobtainedStartDateField(), password),
        "IgnoreIfUnobtainedEndDate": convert_string(excel_instance.IgnoreIfUnobtainedEndDateField(), password),
        "BubbleType": [BubbleType(convert_int(excel_instance.BubbleTypeField(j), password)).name for j in range(excel_instance.BubbleTypeFieldLength())],
        "BubbleDuration": [convert_int(excel_instance.BubbleDurationField(j), password) for j in range(excel_instance.BubbleDurationFieldLength())],
        "FavorEmoticonRewardParcelType": ParcelType(convert_int(excel_instance.FavorEmoticonRewardParcelTypeField(), password)).name,
        "FavorEmoticonRewardId": convert_int(excel_instance.FavorEmoticonRewardIdField(), password),
        "FavorEmoticonRewardAmount": convert_int(excel_instance.FavorEmoticonRewardAmountField(), password),
        "CafeCharacterState": [convert_string(excel_instance.CafeCharacterStateField(j), password) for j in range(excel_instance.CafeCharacterStateFieldLength())],
    }

def dump_ExcelDB_CafeProductionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeIdField(), password),
        "Rank": convert_int(excel_instance.RankField(), password),
        "CafeProductionParcelType": ParcelType(convert_int(excel_instance.CafeProductionParcelTypeField(), password)).name,
        "CafeProductionParcelId": convert_int(excel_instance.CafeProductionParcelIdField(), password),
        "ParcelProductionCoefficient": convert_int(excel_instance.ParcelProductionCoefficientField(), password),
        "ParcelProductionCorrectionValue": convert_int(excel_instance.ParcelProductionCorrectionValueField(), password),
        "ParcelStorageMax": convert_int(excel_instance.ParcelStorageMaxField(), password),
    }

def dump_ExcelDB_CafeRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeIdField(), password),
        "Rank": convert_int(excel_instance.RankField(), password),
        "RecipeId": convert_int(excel_instance.RecipeIdField(), password),
        "ComfortMax": convert_int(excel_instance.ComfortMaxField(), password),
        "TagCountMax": convert_int(excel_instance.TagCountMaxField(), password),
        "CharacterVisitMin": convert_int(excel_instance.CharacterVisitMinField(), password),
        "CharacterVisitMax": convert_int(excel_instance.CharacterVisitMaxField(), password),
        "CafeVisitWeightBase": convert_int(excel_instance.CafeVisitWeightBaseField(), password),
        "CafeVisitWeightTagBonusStep": [convert_int(excel_instance.CafeVisitWeightTagBonusStepField(j), password) for j in range(excel_instance.CafeVisitWeightTagBonusStepFieldLength())],
        "CafeVisitWeightTagBonus": [convert_int(excel_instance.CafeVisitWeightTagBonusField(j), password) for j in range(excel_instance.CafeVisitWeightTagBonusFieldLength())],
    }

def dump_ExcelDB_CameraExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "MinDistance": convert_float(excel_instance.MinDistanceField(), password),
        "MaxDistance": convert_float(excel_instance.MaxDistanceField(), password),
        "RotationX": convert_float(excel_instance.RotationXField(), password),
        "RotationY": convert_float(excel_instance.RotationYField(), password),
        "MoveInstantly": bool(excel_instance.MoveInstantlyField()),
        "MoveInstantlyRotationSave": bool(excel_instance.MoveInstantlyRotationSaveField()),
        "LeftMargin": convert_float(excel_instance.LeftMarginField(), password),
        "BottomMargin": convert_float(excel_instance.BottomMarginField(), password),
        "IgnoreEnemies": bool(excel_instance.IgnoreEnemiesField()),
        "UseRailPointCompensation": bool(excel_instance.UseRailPointCompensationField()),
    }

def dump_ExcelDB_CampaignChapterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "NormalImagePath": convert_string(excel_instance.NormalImagePathField(), password),
        "HardImagePath": convert_string(excel_instance.HardImagePathField(), password),
        "Order": convert_int(excel_instance.OrderField(), password),
        "PreChapterId": [convert_int(excel_instance.PreChapterIdField(j), password) for j in range(excel_instance.PreChapterIdFieldLength())],
        "ChapterRewardId": convert_int(excel_instance.ChapterRewardIdField(), password),
        "ChapterHardRewardId": convert_int(excel_instance.ChapterHardRewardIdField(), password),
        "ChapterVeryHardRewardId": convert_int(excel_instance.ChapterVeryHardRewardIdField(), password),
        "NormalCampaignStageId": [convert_int(excel_instance.NormalCampaignStageIdField(j), password) for j in range(excel_instance.NormalCampaignStageIdFieldLength())],
        "NormalExtraStageId": [convert_int(excel_instance.NormalExtraStageIdField(j), password) for j in range(excel_instance.NormalExtraStageIdFieldLength())],
        "HardCampaignStageId": [convert_int(excel_instance.HardCampaignStageIdField(j), password) for j in range(excel_instance.HardCampaignStageIdFieldLength())],
        "VeryHardCampaignStageId": [convert_int(excel_instance.VeryHardCampaignStageIdField(j), password) for j in range(excel_instance.VeryHardCampaignStageIdFieldLength())],
        "IsTacticSkip": bool(excel_instance.IsTacticSkipField()),
    }

def dump_ExcelDB_CampaignChapterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CampaignChapterStar": convert_int(excel_instance.CampaignChapterStarField(), password),
        "ChapterRewardParcelType": [ParcelType(convert_int(excel_instance.ChapterRewardParcelTypeField(j), password)).name for j in range(excel_instance.ChapterRewardParcelTypeFieldLength())],
        "ChapterRewardId": [convert_int(excel_instance.ChapterRewardIdField(j), password) for j in range(excel_instance.ChapterRewardIdFieldLength())],
        "ChapterRewardAmount": [convert_int(excel_instance.ChapterRewardAmountField(j), password) for j in range(excel_instance.ChapterRewardAmountFieldLength())],
    }

def dump_ExcelDB_CampaignStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Deprecated": bool(excel_instance.DeprecatedField()),
        "Name": convert_string(excel_instance.NameField(), password),
        "StageNumber": convert_string(excel_instance.StageNumberField(), password),
        "CleardScenarioId": convert_int(excel_instance.CleardScenarioIdField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostTypeField(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostIdField(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmountField(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCountField(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCountField(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCountField(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupIdField(j), password) for j in range(excel_instance.EnterScenarioGroupIdFieldLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupIdField(j), password) for j in range(excel_instance.ClearScenarioGroupIdFieldLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMapField(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBGField(), password),
        "CampaignStageRewardId": convert_int(excel_instance.CampaignStageRewardIdField(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurnField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "RecommandLevelGapForGuide": convert_int(excel_instance.RecommandLevelGapForGuideField(), password),
        "MinEquipmentTierForGuide": [convert_int(excel_instance.MinEquipmentTierForGuideField(j), password) for j in range(excel_instance.MinEquipmentTierForGuideFieldLength())],
        "MinSkillLevelForGuide": [convert_int(excel_instance.MinSkillLevelForGuideField(j), password) for j in range(excel_instance.MinSkillLevelForGuideFieldLength())],
        "BgmId": convert_int(excel_instance.BgmIdField(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironmentField(), password)).name,
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "StrategySkipGroundId": convert_int(excel_instance.StrategySkipGroundIdField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventNameField(), password),
        "FirstClearFunnelMessage": convert_string(excel_instance.FirstClearFunnelMessageField(), password),
        "FirstClearEventMessage": convert_string(excel_instance.FirstClearEventMessageField(), password),
        "FirstStartFunnelMessage": convert_string(excel_instance.FirstStartFunnelMessageField(), password),
        "TacticRewardExp": convert_int(excel_instance.TacticRewardExpField(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_CampaignStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "StageRewardProb": convert_int(excel_instance.StageRewardProbField(), password),
        "StageRewardParcelType": ParcelType(convert_int(excel_instance.StageRewardParcelTypeField(), password)).name,
        "StageRewardId": convert_int(excel_instance.StageRewardIdField(), password),
        "StageRewardAmount": convert_int(excel_instance.StageRewardAmountField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_ExcelDB_CampaignStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "StrategyObjectType": StrategyObjectType(convert_int(excel_instance.StrategyObjectTypeField(), password)).name,
        "StrategyRewardParcelType": ParcelType(convert_int(excel_instance.StrategyRewardParcelTypeField(), password)).name,
        "StrategyRewardID": convert_int(excel_instance.StrategyRewardIDField(), password),
        "StrategyRewardName": convert_string(excel_instance.StrategyRewardNameField(), password),
        "StrategyRewardAmount": convert_int(excel_instance.StrategyRewardAmountField(), password),
        "StrategySightRange": convert_int(excel_instance.StrategySightRangeField(), password),
        "PortalId": convert_int(excel_instance.PortalIdField(), password),
        "HealValue": convert_int(excel_instance.HealValueField(), password),
        "SwithId": convert_int(excel_instance.SwithIdField(), password),
        "BuffId": convert_int(excel_instance.BuffIdField(), password),
        "Disposable": bool(excel_instance.DisposableField()),
    }

def dump_ExcelDB_CampaignUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "StrategyPrefabName": convert_string(excel_instance.StrategyPrefabNameField(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupIdField(j), password) for j in range(excel_instance.EnterScenarioGroupIdFieldLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupIdField(j), password) for j in range(excel_instance.ClearScenarioGroupIdFieldLength())],
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "MoveRange": convert_int(excel_instance.MoveRangeField(), password),
        "AIMoveType": StrategyAIType(convert_int(excel_instance.AIMoveTypeField(), password)).name,
        "Grade": HexaUnitGrade(convert_int(excel_instance.GradeField(), password)).name,
        "EnvironmentType": TacticEnvironment(convert_int(excel_instance.EnvironmentTypeField(), password)).name,
        "Scale": convert_float(excel_instance.ScaleField(), password),
        "IsTacticSkip": bool(excel_instance.IsTacticSkipField()),
    }

def dump_ExcelDB_CharacterAcademyTagsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "FavorTags": [Tag(convert_int(excel_instance.FavorTagsField(j), password)).name for j in range(excel_instance.FavorTagsFieldLength())],
        "FavorItemTags": [Tag(convert_int(excel_instance.FavorItemTagsField(j), password)).name for j in range(excel_instance.FavorItemTagsFieldLength())],
        "FavorItemUniqueTags": [Tag(convert_int(excel_instance.FavorItemUniqueTagsField(j), password)).name for j in range(excel_instance.FavorItemUniqueTagsFieldLength())],
        "ForbiddenTags": [Tag(convert_int(excel_instance.ForbiddenTagsField(j), password)).name for j in range(excel_instance.ForbiddenTagsFieldLength())],
        "ZoneWhiteListTags": [Tag(convert_int(excel_instance.ZoneWhiteListTagsField(j), password)).name for j in range(excel_instance.ZoneWhiteListTagsFieldLength())],
    }

def dump_ExcelDB_CharacterAIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EngageType": EngageType(convert_int(excel_instance.EngageTypeField(), password)).name,
        "Positioning": PositioningType(convert_int(excel_instance.PositioningField(), password)).name,
        "CheckCanUseAutoSkill": bool(excel_instance.CheckCanUseAutoSkillField()),
        "DistanceReduceRatioObstaclePath": convert_int(excel_instance.DistanceReduceRatioObstaclePathField(), password),
        "DistanceReduceObstaclePath": convert_int(excel_instance.DistanceReduceObstaclePathField(), password),
        "DistanceReduceRatioFormationPath": convert_int(excel_instance.DistanceReduceRatioFormationPathField(), password),
        "DistanceReduceFormationPath": convert_int(excel_instance.DistanceReduceFormationPathField(), password),
        "MinimumPositionGap": convert_int(excel_instance.MinimumPositionGapField(), password),
        "CanUseObstacleOfKneelMotion": bool(excel_instance.CanUseObstacleOfKneelMotionField()),
        "CanUseObstacleOfStandMotion": bool(excel_instance.CanUseObstacleOfStandMotionField()),
        "HasTargetSwitchingMotion": bool(excel_instance.HasTargetSwitchingMotionField()),
    }

def dump_ExcelDB_CharacterCalculationLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityTypeField(), password)).name,
        "CalculationValue": BattleCalculationStat(convert_int(excel_instance.CalculationValueField(), password)).name,
        "MinValue": convert_int(excel_instance.MinValueField(), password),
        "MaxValue": convert_int(excel_instance.MaxValueField(), password),
        "LimitStartValue": [convert_int(excel_instance.LimitStartValueField(j), password) for j in range(excel_instance.LimitStartValueFieldLength())],
        "DecreaseRate": [convert_int(excel_instance.DecreaseRateField(j), password) for j in range(excel_instance.DecreaseRateFieldLength())],
    }

def dump_ExcelDB_CharacterCombatSkinExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_string(excel_instance.GroupIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePathField(), password),
    }

def dump_ExcelDB_CharacterDialogBattlePassExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "OriginalCharacterId": convert_int(excel_instance.OriginalCharacterIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "BattlePassID": convert_int(excel_instance.BattlePassIDField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategoryField(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogConditionField(), password)).name,
        "DialogConditionDetail": DialogConditionDetail(convert_int(excel_instance.DialogConditionDetailField(), password)).name,
        "DialogConditionDetailValue": convert_int(excel_instance.DialogConditionDetailValueField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogTypeField(), password)).name,
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "UnlockBattlePassId": convert_int(excel_instance.UnlockBattlePassIdField(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "TeenMode": bool(excel_instance.TeenModeField()),
    }

def dump_ExcelDB_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndexField(), password),
        "DialogType": convert_string(excel_instance.DialogTypeField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "DurationAdd": convert_int(excel_instance.DurationAddField(), password),
        "HideUI": bool(excel_instance.HideUIField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "CVUnlockScenarioType": CVUnlockScenarioType(convert_int(excel_instance.CVUnlockScenarioTypeField(), password)).name,
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
        "UnlockEventSeason": convert_int(excel_instance.UnlockEventSeasonField(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
    }

def dump_ExcelDB_CharacterDialogEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "OriginalCharacterId": convert_int(excel_instance.OriginalCharacterIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "EventID": convert_int(excel_instance.EventIDField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategoryField(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogConditionField(), password)).name,
        "DialogConditionDetail": DialogConditionDetail(convert_int(excel_instance.DialogConditionDetailField(), password)).name,
        "DialogConditionDetailValue": convert_int(excel_instance.DialogConditionDetailValueField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogTypeField(), password)).name,
        "ActionName": convert_string(excel_instance.ActionNameField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "CVUnlockScenarioType": CVUnlockScenarioType(convert_int(excel_instance.CVUnlockScenarioTypeField(), password)).name,
        "UnlockEventSeason": convert_int(excel_instance.UnlockEventSeasonField(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "ScenarioCharacterShapes": ScenarioCharacterShapes(convert_int(excel_instance.ScenarioCharacterShapesField(), password)).name,
    }

def dump_ExcelDB_CharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategoryField(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogConditionField(), password)).name,
        "Anniversary": Anniversary(convert_int(excel_instance.AnniversaryField(), password)).name,
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogTypeField(), password)).name,
        "ActionName": convert_string(excel_instance.ActionNameField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "ApplyPosition": bool(excel_instance.ApplyPositionField()),
        "PosX": convert_float(excel_instance.PosXField(), password),
        "PosY": convert_float(excel_instance.PosYField(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRankField(), password),
        "UnlockEquipWeapon": bool(excel_instance.UnlockEquipWeaponField()),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "TeenMode": bool(excel_instance.TeenModeField()),
    }

def dump_ExcelDB_CharacterDialogSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "TLMID": convert_string(excel_instance.TLMIDField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "Separate": bool(excel_instance.SeparateField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
    }

def dump_ExcelDB_CharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "CostumeGroupId": convert_int(excel_instance.CostumeGroupIdField(), password),
        "IsPlayable": bool(excel_instance.IsPlayableField()),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "ReleaseDate": convert_string(excel_instance.ReleaseDateField(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDateField(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDateField(), password),
        "IsPlayableCharacter": bool(excel_instance.IsPlayableCharacterField()),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "IsNPC": bool(excel_instance.IsNPCField()),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityTypeField(), password)).name,
        "CanSurvive": bool(excel_instance.CanSurviveField()),
        "IsDummy": bool(excel_instance.IsDummyField()),
        "SubPartsCount": convert_int(excel_instance.SubPartsCountField(), password),
        "TacticRole": convert_float(excel_instance.TacticRoleField(), password),
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponTypeField(), password)).name,
        "TacticRange": TacticRange(convert_int(excel_instance.TacticRangeField(), password)).name,
        "BulletType": BulletType(convert_int(excel_instance.BulletTypeField(), password)).name,
        "ArmorType": ArmorType(convert_int(excel_instance.ArmorTypeField(), password)).name,
        "AimIKType": AimIKType(convert_int(excel_instance.AimIKTypeField(), password)).name,
        "School": School(convert_int(excel_instance.SchoolField(), password)).name,
        "Club": Club(convert_int(excel_instance.ClubField(), password)).name,
        "DefaultStarGrade": convert_int(excel_instance.DefaultStarGradeField(), password),
        "MaxStarGrade": convert_int(excel_instance.MaxStarGradeField(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpTypeField(), password)).name,
        "SquadType": SquadType(convert_int(excel_instance.SquadTypeField(), password)).name,
        "Jumpable": bool(excel_instance.JumpableField()),
        "PersonalityId": convert_int(excel_instance.PersonalityIdField(), password),
        "CharacterAIId": convert_int(excel_instance.CharacterAIIdField(), password),
        "ExternalBTId": convert_int(excel_instance.ExternalBTIdField(), password),
        "MainCombatStyleId": convert_int(excel_instance.MainCombatStyleIdField(), password),
        "CombatStyleIndex": convert_int(excel_instance.CombatStyleIndexField(), password),
        "UseRepStyleOnCharacterGrowth": bool(excel_instance.UseRepStyleOnCharacterGrowthField()),
        "ScenarioCharacter": convert_string(excel_instance.ScenarioCharacterField(), password),
        "SpawnTemplateId": convert_uint(excel_instance.SpawnTemplateIdField(), password),
        "FavorLevelupType": convert_int(excel_instance.FavorLevelupTypeField(), password),
        "EquipmentSlot": [EquipmentCategory(convert_int(excel_instance.EquipmentSlotField(j), password)).name for j in range(excel_instance.EquipmentSlotFieldLength())],
        "WeaponLocalizeId": convert_uint(excel_instance.WeaponLocalizeIdField(), password),
        "DisplayEnemyInfo": bool(excel_instance.DisplayEnemyInfoField()),
        "BodyRadius": convert_int(excel_instance.BodyRadiusField(), password),
        "RandomEffectRadius": convert_int(excel_instance.RandomEffectRadiusField(), password),
        "TargetGuideScale": convert_float(excel_instance.TargetGuideScaleField(), password),
        "HPBarHide": bool(excel_instance.HPBarHideField()),
        "HpBarHeight": convert_float(excel_instance.HpBarHeightField(), password),
        "HighlightFloaterHeight": convert_float(excel_instance.HighlightFloaterHeightField(), password),
        "EmojiOffsetX": convert_float(excel_instance.EmojiOffsetXField(), password),
        "EmojiOffsetY": convert_float(excel_instance.EmojiOffsetYField(), password),
        "MoveStartFrame": convert_int(excel_instance.MoveStartFrameField(), password),
        "MoveEndFrame": convert_int(excel_instance.MoveEndFrameField(), password),
        "JumpMotionFrame": convert_int(excel_instance.JumpMotionFrameField(), password),
        "AppearFrame": convert_int(excel_instance.AppearFrameField(), password),
        "CanMove": bool(excel_instance.CanMoveField()),
        "CanFix": bool(excel_instance.CanFixField()),
        "CanCrowdControl": bool(excel_instance.CanCrowdControlField()),
        "CanBattleItemMove": bool(excel_instance.CanBattleItemMoveField()),
        "IgnoreObstacle": bool(excel_instance.IgnoreObstacleField()),
        "IsAirUnit": bool(excel_instance.IsAirUnitField()),
        "AirUnitHeight": convert_int(excel_instance.AirUnitHeightField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
        "SecretStoneItemId": convert_int(excel_instance.SecretStoneItemIdField(), password),
        "SecretStoneItemAmount": convert_int(excel_instance.SecretStoneItemAmountField(), password),
        "CharacterPieceItemId": convert_int(excel_instance.CharacterPieceItemIdField(), password),
        "CharacterPieceItemAmount": convert_int(excel_instance.CharacterPieceItemAmountField(), password),
        "CombineRecipeId": convert_int(excel_instance.CombineRecipeIdField(), password),
    }

def dump_ExcelDB_CharacterGearExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpTypeField(), password)).name,
        "Tier": convert_int(excel_instance.TierField(), password),
        "NextTierEquipment": convert_int(excel_instance.NextTierEquipmentField(), password),
        "RecipeId": convert_int(excel_instance.RecipeIdField(), password),
        "OpenFavorLevel": convert_int(excel_instance.OpenFavorLevelField(), password),
        "MaxLevel": convert_int(excel_instance.MaxLevelField(), password),
        "LearnSkillSlot": convert_string(excel_instance.LearnSkillSlotField(), password),
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatTypeField(j), password)).name for j in range(excel_instance.StatTypeFieldLength())],
        "MinStatValue": [convert_int(excel_instance.MinStatValueField(j), password) for j in range(excel_instance.MinStatValueFieldLength())],
        "MaxStatValue": [convert_int(excel_instance.MaxStatValueField(j), password) for j in range(excel_instance.MaxStatValueFieldLength())],
        "Icon": convert_string(excel_instance.IconField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
    }

def dump_ExcelDB_CharacterGearLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "TierLevelExp": [convert_int(excel_instance.TierLevelExpField(j), password) for j in range(excel_instance.TierLevelExpFieldLength())],
        "TotalExp": [convert_int(excel_instance.TotalExpField(j), password) for j in range(excel_instance.TotalExpFieldLength())],
    }

def dump_ExcelDB_CharacterIllustCoordinateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CharacterBodyCenterX": convert_float(excel_instance.CharacterBodyCenterXField(), password),
        "CharacterBodyCenterY": convert_float(excel_instance.CharacterBodyCenterYField(), password),
        "DefaultScale": convert_float(excel_instance.DefaultScaleField(), password),
        "MinScale": convert_float(excel_instance.MinScaleField(), password),
        "MaxScale": convert_float(excel_instance.MaxScaleField(), password),
    }

def dump_ExcelDB_CharacterLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "Exp": convert_int(excel_instance.ExpField(), password),
        "TotalExp": convert_int(excel_instance.TotalExpField(), password),
    }

def dump_ExcelDB_CharacterLevelStatFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "CriticalFactor": convert_int(excel_instance.CriticalFactorField(), password),
        "StabilityFactor": convert_int(excel_instance.StabilityFactorField(), password),
        "DefenceFactor": convert_int(excel_instance.DefenceFactorField(), password),
        "AccuracyFactor": convert_int(excel_instance.AccuracyFactorField(), password),
    }

def dump_ExcelDB_CharacterPotentialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "PotentialStatGroupId": convert_int(excel_instance.PotentialStatGroupIdField(), password),
        "PotentialStatBonusRateType": PotentialStatBonusRateType(convert_int(excel_instance.PotentialStatBonusRateTypeField(), password)).name,
        "IsUnnecessaryStat": bool(excel_instance.IsUnnecessaryStatField()),
    }

def dump_ExcelDB_CharacterPotentialRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RequirePotentialStatType": [PotentialStatBonusRateType(convert_int(excel_instance.RequirePotentialStatTypeField(j), password)).name for j in range(excel_instance.RequirePotentialStatTypeFieldLength())],
        "RequirePotentialStatLevel": [convert_int(excel_instance.RequirePotentialStatLevelField(j), password) for j in range(excel_instance.RequirePotentialStatLevelFieldLength())],
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
    }

def dump_ExcelDB_CharacterPotentialStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PotentialStatGroupId": convert_int(excel_instance.PotentialStatGroupIdField(), password),
        "PotentialLevel": convert_int(excel_instance.PotentialLevelField(), password),
        "RecipeId": convert_int(excel_instance.RecipeIdField(), password),
        "StatBonusRate": convert_int(excel_instance.StatBonusRateField(), password),
    }

def dump_ExcelDB_CharacterSkillListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterSkillListGroupId": convert_int(excel_instance.CharacterSkillListGroupIdField(), password),
        "MinimumGradeCharacterWeapon": convert_int(excel_instance.MinimumGradeCharacterWeaponField(), password),
        "MinimumTierCharacterGear": convert_int(excel_instance.MinimumTierCharacterGearField(), password),
        "FormIndex": convert_int(excel_instance.FormIndexField(), password),
        "IsRootMotion": bool(excel_instance.IsRootMotionField()),
        "IsMoveLeftRight": bool(excel_instance.IsMoveLeftRightField()),
        "UseRandomExSkillTimeline": bool(excel_instance.UseRandomExSkillTimelineField()),
        "TSAInteractionId": convert_int(excel_instance.TSAInteractionIdField(), password),
        "NormalSkillGroupId": [convert_string(excel_instance.NormalSkillGroupIdField(j), password) for j in range(excel_instance.NormalSkillGroupIdFieldLength())],
        "NormalSkillTimeLineIndex": [convert_int(excel_instance.NormalSkillTimeLineIndexField(j), password) for j in range(excel_instance.NormalSkillTimeLineIndexFieldLength())],
        "SelectExSkillActionSkillSlot": convert_int(excel_instance.SelectExSkillActionSkillSlotField(), password),
        "ExSkillGroupId": [convert_string(excel_instance.ExSkillGroupIdField(j), password) for j in range(excel_instance.ExSkillGroupIdFieldLength())],
        "ExSkillCutInTimeLineIndex": [convert_string(excel_instance.ExSkillCutInTimeLineIndexField(j), password) for j in range(excel_instance.ExSkillCutInTimeLineIndexFieldLength())],
        "ExSkillLevelTimeLineIndex": [convert_string(excel_instance.ExSkillLevelTimeLineIndexField(j), password) for j in range(excel_instance.ExSkillLevelTimeLineIndexFieldLength())],
        "PublicSkillGroupId": [convert_string(excel_instance.PublicSkillGroupIdField(j), password) for j in range(excel_instance.PublicSkillGroupIdFieldLength())],
        "PublicSkillTimeLineIndex": [convert_int(excel_instance.PublicSkillTimeLineIndexField(j), password) for j in range(excel_instance.PublicSkillTimeLineIndexFieldLength())],
        "PassiveSkillGroupId": [convert_string(excel_instance.PassiveSkillGroupIdField(j), password) for j in range(excel_instance.PassiveSkillGroupIdFieldLength())],
        "LeaderSkillGroupId": [convert_string(excel_instance.LeaderSkillGroupIdField(j), password) for j in range(excel_instance.LeaderSkillGroupIdFieldLength())],
        "ExtraPassiveSkillGroupId": [convert_string(excel_instance.ExtraPassiveSkillGroupIdField(j), password) for j in range(excel_instance.ExtraPassiveSkillGroupIdFieldLength())],
        "HiddenPassiveSkillGroupId": [convert_string(excel_instance.HiddenPassiveSkillGroupIdField(j), password) for j in range(excel_instance.HiddenPassiveSkillGroupIdFieldLength())],
    }

def dump_ExcelDB_CharacterStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "StabilityRate": convert_int(excel_instance.StabilityRateField(), password),
        "StabilityPoint": convert_int(excel_instance.StabilityPointField(), password),
        "AttackPower1": convert_int(excel_instance.AttackPower1Field(), password),
        "AttackPower100": convert_int(excel_instance.AttackPower100Field(), password),
        "MaxHP1": convert_int(excel_instance.MaxHP1Field(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100Field(), password),
        "DefensePower1": convert_int(excel_instance.DefensePower1Field(), password),
        "DefensePower100": convert_int(excel_instance.DefensePower100Field(), password),
        "HealPower1": convert_int(excel_instance.HealPower1Field(), password),
        "HealPower100": convert_int(excel_instance.HealPower100Field(), password),
        "DodgePoint": convert_int(excel_instance.DodgePointField(), password),
        "AccuracyPoint": convert_int(excel_instance.AccuracyPointField(), password),
        "CriticalPoint": convert_int(excel_instance.CriticalPointField(), password),
        "CriticalResistPoint": convert_int(excel_instance.CriticalResistPointField(), password),
        "CriticalDamageRate": convert_int(excel_instance.CriticalDamageRateField(), password),
        "CriticalDamageResistRate": convert_int(excel_instance.CriticalDamageResistRateField(), password),
        "BlockRate": convert_int(excel_instance.BlockRateField(), password),
        "HealEffectivenessRate": convert_int(excel_instance.HealEffectivenessRateField(), password),
        "OppressionPower": convert_int(excel_instance.OppressionPowerField(), password),
        "OppressionResist": convert_int(excel_instance.OppressionResistField(), password),
        "DefensePenetration1": convert_int(excel_instance.DefensePenetration1Field(), password),
        "DefensePenetration100": convert_int(excel_instance.DefensePenetration100Field(), password),
        "DefensePenetrationResist1": convert_int(excel_instance.DefensePenetrationResist1Field(), password),
        "DefensePenetrationResist100": convert_int(excel_instance.DefensePenetrationResist100Field(), password),
        "EnhanceExplosionRate": convert_int(excel_instance.EnhanceExplosionRateField(), password),
        "EnhancePierceRate": convert_int(excel_instance.EnhancePierceRateField(), password),
        "EnhanceMysticRate": convert_int(excel_instance.EnhanceMysticRateField(), password),
        "EnhanceSonicRate": convert_int(excel_instance.EnhanceSonicRateField(), password),
        "EnhanceChemicalRate": convert_int(excel_instance.EnhanceChemicalRateField(), password),
        "EnhanceSiegeRate": convert_int(excel_instance.EnhanceSiegeRateField(), password),
        "EnhanceNormalRate": convert_int(excel_instance.EnhanceNormalRateField(), password),
        "EnhanceLightArmorRate": convert_int(excel_instance.EnhanceLightArmorRateField(), password),
        "EnhanceHeavyArmorRate": convert_int(excel_instance.EnhanceHeavyArmorRateField(), password),
        "EnhanceUnarmedRate": convert_int(excel_instance.EnhanceUnarmedRateField(), password),
        "EnhanceElasticArmorRate": convert_int(excel_instance.EnhanceElasticArmorRateField(), password),
        "EnhanceCompositeArmorRate": convert_int(excel_instance.EnhanceCompositeArmorRateField(), password),
        "EnhanceStructureRate": convert_int(excel_instance.EnhanceStructureRateField(), password),
        "EnhanceNormalArmorRate": convert_int(excel_instance.EnhanceNormalArmorRateField(), password),
        "ExtendBuffDuration": convert_int(excel_instance.ExtendBuffDurationField(), password),
        "ExtendDebuffDuration": convert_int(excel_instance.ExtendDebuffDurationField(), password),
        "ExtendCrowdControlDuration": convert_int(excel_instance.ExtendCrowdControlDurationField(), password),
        "AmmoCount": convert_int(excel_instance.AmmoCountField(), password),
        "AmmoCost": convert_int(excel_instance.AmmoCostField(), password),
        "IgnoreDelayCount": convert_int(excel_instance.IgnoreDelayCountField(), password),
        "NormalAttackSpeed": convert_int(excel_instance.NormalAttackSpeedField(), password),
        "Range": convert_int(excel_instance.RangeField(), password),
        "InitialRangeRate": convert_int(excel_instance.InitialRangeRateField(), password),
        "MoveSpeed": convert_int(excel_instance.MoveSpeedField(), password),
        "SightPoint": convert_int(excel_instance.SightPointField(), password),
        "ActiveGauge": convert_int(excel_instance.ActiveGaugeField(), password),
        "GroggyGauge": convert_int(excel_instance.GroggyGaugeField(), password),
        "GroggyTime": convert_int(excel_instance.GroggyTimeField(), password),
        "StrategyMobility": convert_int(excel_instance.StrategyMobilityField(), password),
        "ActionCount": convert_int(excel_instance.ActionCountField(), password),
        "StrategySightRange": convert_int(excel_instance.StrategySightRangeField(), password),
        "DamageRatio": convert_int(excel_instance.DamageRatioField(), password),
        "DamagedRatio": convert_int(excel_instance.DamagedRatioField(), password),
        "DamageRatio2Increase": convert_int(excel_instance.DamageRatio2IncreaseField(), password),
        "DamageRatio2Decrease": convert_int(excel_instance.DamageRatio2DecreaseField(), password),
        "DamagedRatio2Increase": convert_int(excel_instance.DamagedRatio2IncreaseField(), password),
        "DamagedRatio2Decrease": convert_int(excel_instance.DamagedRatio2DecreaseField(), password),
        "ExDamagedRatioIncrease": convert_int(excel_instance.ExDamagedRatioIncreaseField(), password),
        "ExDamagedRatioDecrease": convert_int(excel_instance.ExDamagedRatioDecreaseField(), password),
        "EnhanceExDamageRate": convert_int(excel_instance.EnhanceExDamageRateField(), password),
        "ReduceExDamagedRate": convert_int(excel_instance.ReduceExDamagedRateField(), password),
        "EnhanceBasicsDamageRate": convert_int(excel_instance.EnhanceBasicsDamageRateField(), password),
        "ReduceBasicsDamagedRate": convert_int(excel_instance.ReduceBasicsDamagedRateField(), password),
        "EnhanceWeakDamageRate": convert_int(excel_instance.EnhanceWeakDamageRateField(), password),
        "ReduceWeakDamagedRate": convert_int(excel_instance.ReduceWeakDamagedRateField(), password),
        "WeakDamagedRatio": convert_int(excel_instance.WeakDamagedRatioField(), password),
        "EffectiveDamagedRatio": convert_int(excel_instance.EffectiveDamagedRatioField(), password),
        "NormalDamagedRatio": convert_int(excel_instance.NormalDamagedRatioField(), password),
        "ResistDamagedRatio": convert_int(excel_instance.ResistDamagedRatioField(), password),
        "HealRate": convert_int(excel_instance.HealRateField(), password),
        "HealLightArmorRate": convert_int(excel_instance.HealLightArmorRateField(), password),
        "HealHeavyArmorRate": convert_int(excel_instance.HealHeavyArmorRateField(), password),
        "HealUnarmedRate": convert_int(excel_instance.HealUnarmedRateField(), password),
        "HealElasticArmorRate": convert_int(excel_instance.HealElasticArmorRateField(), password),
        "HealNormalArmorRate": convert_int(excel_instance.HealNormalArmorRateField(), password),
        "HealedExplosionRate": convert_int(excel_instance.HealedExplosionRateField(), password),
        "HealedPierceRate": convert_int(excel_instance.HealedPierceRateField(), password),
        "HealedMysticRate": convert_int(excel_instance.HealedMysticRateField(), password),
        "HealedSonicRate": convert_int(excel_instance.HealedSonicRateField(), password),
        "HealedNormalRate": convert_int(excel_instance.HealedNormalRateField(), password),
        "StreetBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.StreetBattleAdaptationField(), password)).name,
        "OutdoorBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OutdoorBattleAdaptationField(), password)).name,
        "IndoorBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.IndoorBattleAdaptationField(), password)).name,
        "RegenCost": convert_int(excel_instance.RegenCostField(), password),
    }

def dump_ExcelDB_CharacterStatLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityTypeField(), password)).name,
        "StatType": StatType(convert_int(excel_instance.StatTypeField(), password)).name,
        "StatMinValue": convert_int(excel_instance.StatMinValueField(), password),
        "StatMaxValue": convert_int(excel_instance.StatMaxValueField(), password),
        "StatRatioMinValue": convert_int(excel_instance.StatRatioMinValueField(), password),
        "StatRatioMaxValue": convert_int(excel_instance.StatRatioMaxValueField(), password),
    }

def dump_ExcelDB_CharacterStatsDetailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DetailShowStats": [StatType(convert_int(excel_instance.DetailShowStatsField(j), password)).name for j in range(excel_instance.DetailShowStatsFieldLength())],
        "IsStatsPercent": [bool(excel_instance.IsStatsPercentField(j)) for j in range(excel_instance.IsStatsPercentFieldLength())],
    }

def dump_ExcelDB_CharacterStatsTransExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TransSupportStats": StatType(convert_int(excel_instance.TransSupportStatsField(), password)).name,
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
        "TransSupportStatsFactor": convert_int(excel_instance.TransSupportStatsFactorField(), password),
        "StatTransType": StatTransType(convert_int(excel_instance.StatTransTypeField(), password)).name,
    }

def dump_ExcelDB_CharacterTranscendenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "MaxFavorLevel": [convert_int(excel_instance.MaxFavorLevelField(j), password) for j in range(excel_instance.MaxFavorLevelFieldLength())],
        "StatBonusRateAttack": [convert_int(excel_instance.StatBonusRateAttackField(j), password) for j in range(excel_instance.StatBonusRateAttackFieldLength())],
        "StatBonusRateHP": [convert_int(excel_instance.StatBonusRateHPField(j), password) for j in range(excel_instance.StatBonusRateHPFieldLength())],
        "StatBonusRateHeal": [convert_int(excel_instance.StatBonusRateHealField(j), password) for j in range(excel_instance.StatBonusRateHealFieldLength())],
        "RecipeId": [convert_int(excel_instance.RecipeIdField(j), password) for j in range(excel_instance.RecipeIdFieldLength())],
        "SkillSlotA": [convert_string(excel_instance.SkillSlotAField(j), password) for j in range(excel_instance.SkillSlotAFieldLength())],
        "SkillSlotB": [convert_string(excel_instance.SkillSlotBField(j), password) for j in range(excel_instance.SkillSlotBFieldLength())],
        "SkillSlotC": [convert_string(excel_instance.SkillSlotCField(j), password) for j in range(excel_instance.SkillSlotCFieldLength())],
        "MaxlevelStar": [convert_int(excel_instance.MaxlevelStarField(j), password) for j in range(excel_instance.MaxlevelStarFieldLength())],
    }

def dump_ExcelDB_CharacterVictoryInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "InteractionId": convert_int(excel_instance.InteractionIdField(), password),
        "CostumeId01": convert_int(excel_instance.CostumeId01Field(), password),
        "PositionIndex01": convert_int(excel_instance.PositionIndex01Field(), password),
        "VictoryStartAnimationPath01": convert_string(excel_instance.VictoryStartAnimationPath01Field(), password),
        "VictoryEndAnimationPath01": convert_string(excel_instance.VictoryEndAnimationPath01Field(), password),
        "VoiceEvent01": VoiceEvent(convert_int(excel_instance.VoiceEvent01Field(), password)).name,
        "CostumeId02": convert_int(excel_instance.CostumeId02Field(), password),
        "PositionIndex02": convert_int(excel_instance.PositionIndex02Field(), password),
        "VictoryStartAnimationPath02": convert_string(excel_instance.VictoryStartAnimationPath02Field(), password),
        "VictoryEndAnimationPath02": convert_string(excel_instance.VictoryEndAnimationPath02Field(), password),
        "VoiceEvent02": VoiceEvent(convert_int(excel_instance.VoiceEvent02Field(), password)).name,
        "CostumeId03": convert_int(excel_instance.CostumeId03Field(), password),
        "PositionIndex03": convert_int(excel_instance.PositionIndex03Field(), password),
        "VictoryStartAnimationPath03": convert_string(excel_instance.VictoryStartAnimationPath03Field(), password),
        "VictoryEndAnimationPath03": convert_string(excel_instance.VictoryEndAnimationPath03Field(), password),
        "VoiceEvent03": VoiceEvent(convert_int(excel_instance.VoiceEvent03Field(), password)).name,
        "CostumeId04": convert_int(excel_instance.CostumeId04Field(), password),
        "PositionIndex04": convert_int(excel_instance.PositionIndex04Field(), password),
        "VictoryStartAnimationPath04": convert_string(excel_instance.VictoryStartAnimationPath04Field(), password),
        "VictoryEndAnimationPath04": convert_string(excel_instance.VictoryEndAnimationPath04Field(), password),
        "VoiceEvent04": VoiceEvent(convert_int(excel_instance.VoiceEvent04Field(), password)).name,
        "CostumeId05": convert_int(excel_instance.CostumeId05Field(), password),
        "PositionIndex05": convert_int(excel_instance.PositionIndex05Field(), password),
        "VictoryStartAnimationPath05": convert_string(excel_instance.VictoryStartAnimationPath05Field(), password),
        "VictoryEndAnimationPath05": convert_string(excel_instance.VictoryEndAnimationPath05Field(), password),
        "VoiceEvent05": VoiceEvent(convert_int(excel_instance.VoiceEvent05Field(), password)).name,
        "CostumeId06": convert_int(excel_instance.CostumeId06Field(), password),
        "PositionIndex06": convert_int(excel_instance.PositionIndex06Field(), password),
        "VictoryStartAnimationPath06": convert_string(excel_instance.VictoryStartAnimationPath06Field(), password),
        "VictoryEndAnimationPath06": convert_string(excel_instance.VictoryEndAnimationPath06Field(), password),
        "VoiceEvent06": VoiceEvent(convert_int(excel_instance.VoiceEvent06Field(), password)).name,
    }

def dump_ExcelDB_CharacterVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterVoiceUniqueId": convert_int(excel_instance.CharacterVoiceUniqueIdField(), password),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupIdField(), password),
        "VoiceHash": convert_uint(excel_instance.VoiceHashField(), password),
        "OnlyOne": bool(excel_instance.OnlyOneField()),
        "Priority": convert_int(excel_instance.PriorityField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRankField(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "Nation": [Nation(convert_int(excel_instance.NationField(j), password)).name for j in range(excel_instance.NationFieldLength())],
        "Volume": [convert_float(excel_instance.VolumeField(j), password) for j in range(excel_instance.VolumeFieldLength())],
        "Delay": [convert_float(excel_instance.DelayField(j), password) for j in range(excel_instance.DelayFieldLength())],
        "Path": [convert_string(excel_instance.PathField(j), password) for j in range(excel_instance.PathFieldLength())],
    }

def dump_ExcelDB_CharacterVoiceSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupIdField(), password),
        "TLMID": convert_string(excel_instance.TLMIDField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "Separate": bool(excel_instance.SeparateField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
    }

def dump_ExcelDB_CharacterWeaponExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
        "SetRecipe": convert_int(excel_instance.SetRecipeField(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpTypeField(), password)).name,
        "AttackPower": convert_int(excel_instance.AttackPowerField(), password),
        "AttackPower100": convert_int(excel_instance.AttackPower100Field(), password),
        "MaxHP": convert_int(excel_instance.MaxHPField(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100Field(), password),
        "HealPower": convert_int(excel_instance.HealPowerField(), password),
        "HealPower100": convert_int(excel_instance.HealPower100Field(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
        "Unlock": [bool(excel_instance.UnlockField(j)) for j in range(excel_instance.UnlockFieldLength())],
        "RecipeId": [convert_int(excel_instance.RecipeIdField(j), password) for j in range(excel_instance.RecipeIdFieldLength())],
        "MaxLevel": [convert_int(excel_instance.MaxLevelField(j), password) for j in range(excel_instance.MaxLevelFieldLength())],
        "LearnSkillSlot": [convert_string(excel_instance.LearnSkillSlotField(j), password) for j in range(excel_instance.LearnSkillSlotFieldLength())],
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatTypeField(j), password)).name for j in range(excel_instance.StatTypeFieldLength())],
        "StatValue": [convert_int(excel_instance.StatValueField(j), password) for j in range(excel_instance.StatValueFieldLength())],
    }

def dump_ExcelDB_CharacterWeaponExpBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponTypeField(), password)).name,
        "WeaponExpGrowthA": convert_int(excel_instance.WeaponExpGrowthAField(), password),
        "WeaponExpGrowthB": convert_int(excel_instance.WeaponExpGrowthBField(), password),
        "WeaponExpGrowthC": convert_int(excel_instance.WeaponExpGrowthCField(), password),
        "WeaponExpGrowthZ": convert_int(excel_instance.WeaponExpGrowthZField(), password),
    }

def dump_ExcelDB_CharacterWeaponLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "Exp": convert_int(excel_instance.ExpField(), password),
        "TotalExp": convert_int(excel_instance.TotalExpField(), password),
    }

def dump_ExcelDB_ClanChattingEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TabGroupId": convert_int(excel_instance.TabGroupIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKrField(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJpField(), password),
        "ImagePathTh": convert_string(excel_instance.ImagePathThField(), password),
        "ImagePathTw": convert_string(excel_instance.ImagePathTwField(), password),
        "ImagePathEn": convert_string(excel_instance.ImagePathEnField(), password),
    }

def dump_ExcelDB_ClanRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ClanRewardType": ClanRewardType(convert_int(excel_instance.ClanRewardTypeField(), password)).name,
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonTypeField(), password)).name,
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_CombatEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "EmojiEvent": EmojiEvent(convert_int(excel_instance.EmojiEventField(), password)).name,
        "OrderOfPriority": convert_int(excel_instance.OrderOfPriorityField(), password),
        "EmojiDuration": bool(excel_instance.EmojiDurationField()),
        "EmojiReversal": bool(excel_instance.EmojiReversalField()),
        "EmojiTurnOn": bool(excel_instance.EmojiTurnOnField()),
        "ShowEmojiDelay": convert_int(excel_instance.ShowEmojiDelayField(), password),
        "ShowDefaultBG": bool(excel_instance.ShowDefaultBGField()),
    }

def dump_ExcelDB_ConquestCalculateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CalculateConditionParcelType": ParcelType(convert_int(excel_instance.CalculateConditionParcelTypeField(), password)).name,
        "CalculateConditionParcelUniqueId": convert_int(excel_instance.CalculateConditionParcelUniqueIdField(), password),
        "CalculateConditionParcelAmount": convert_int(excel_instance.CalculateConditionParcelAmountField(), password),
    }

def dump_ExcelDB_ConquestCameraSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ConquestMapBoundaryOffsetLeft": convert_float(excel_instance.ConquestMapBoundaryOffsetLeftField(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRightField(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTopField(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottomField(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetXField(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetYField(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngleField(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMaxField(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMinField(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefaultField(), password),
    }

def dump_ExcelDB_ConquestErosionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "ErosionType": ConquestErosionType(convert_int(excel_instance.ErosionTypeField(), password)).name,
        "Phase": convert_int(excel_instance.PhaseField(), password),
        "PhaseAlarm": bool(excel_instance.PhaseAlarmField()),
        "StepIndex": convert_int(excel_instance.StepIndexField(), password),
        "PhaseStartConditionType": [ConquestConditionType(convert_int(excel_instance.PhaseStartConditionTypeField(j), password)).name for j in range(excel_instance.PhaseStartConditionTypeFieldLength())],
        "PhaseStartConditionParameter": [convert_string(excel_instance.PhaseStartConditionParameterField(j), password) for j in range(excel_instance.PhaseStartConditionParameterFieldLength())],
        "PhaseBeforeExposeConditionType": [ConquestConditionType(convert_int(excel_instance.PhaseBeforeExposeConditionTypeField(j), password)).name for j in range(excel_instance.PhaseBeforeExposeConditionTypeFieldLength())],
        "PhaseBeforeExposeConditionParameter": [convert_string(excel_instance.PhaseBeforeExposeConditionParameterField(j), password) for j in range(excel_instance.PhaseBeforeExposeConditionParameterFieldLength())],
        "ErosionBattleConditionParcelType": ParcelType(convert_int(excel_instance.ErosionBattleConditionParcelTypeField(), password)).name,
        "ErosionBattleConditionParcelUniqueId": convert_int(excel_instance.ErosionBattleConditionParcelUniqueIdField(), password),
        "ErosionBattleConditionParcelAmount": convert_int(excel_instance.ErosionBattleConditionParcelAmountField(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardIdField(), password),
    }

def dump_ExcelDB_ConquestErosionUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TilePrefabId": convert_int(excel_instance.TilePrefabIdField(), password),
        "MassErosionUnitId": convert_int(excel_instance.MassErosionUnitIdField(), password),
        "MassErosionUnitRotationY": convert_float(excel_instance.MassErosionUnitRotationYField(), password),
        "IndividualErosionUnitId": convert_int(excel_instance.IndividualErosionUnitIdField(), password),
        "IndividualErosionUnitRotationY": convert_float(excel_instance.IndividualErosionUnitRotationYField(), password),
    }

def dump_ExcelDB_ConquestEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "MainStoryEventContentId": convert_int(excel_instance.MainStoryEventContentIdField(), password),
        "ConquestEventType": ConquestEventType(convert_int(excel_instance.ConquestEventTypeField(), password)).name,
        "UseErosion": bool(excel_instance.UseErosionField()),
        "UseUnexpectedEvent": bool(excel_instance.UseUnexpectedEventField()),
        "UseCalculate": bool(excel_instance.UseCalculateField()),
        "UseConquestObject": bool(excel_instance.UseConquestObjectField()),
        "EvnetMapGoalLocalize": convert_string(excel_instance.EvnetMapGoalLocalizeField(), password),
        "EvnetMapNameLocalize": convert_string(excel_instance.EvnetMapNameLocalizeField(), password),
        "MapEnterScenarioGroupId": convert_int(excel_instance.MapEnterScenarioGroupIdField(), password),
        "EvnetScenarioBG": convert_string(excel_instance.EvnetScenarioBGField(), password),
        "ManageUnitChange": convert_int(excel_instance.ManageUnitChangeField(), password),
        "AssistCount": convert_int(excel_instance.AssistCountField(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSecondsField(), password),
        "AnimationUnitAmountMin": convert_int(excel_instance.AnimationUnitAmountMinField(), password),
        "AnimationUnitAmountMax": convert_int(excel_instance.AnimationUnitAmountMaxField(), password),
        "AnimationUnitDelay": convert_float(excel_instance.AnimationUnitDelayField(), password),
        "LocalizeUnexpected": convert_string(excel_instance.LocalizeUnexpectedField(), password),
        "LocalizeErosions": convert_string(excel_instance.LocalizeErosionsField(), password),
        "LocalizeStep": convert_string(excel_instance.LocalizeStepField(), password),
        "LocalizeTile": convert_string(excel_instance.LocalizeTileField(), password),
        "LocalizeMapInfo": convert_string(excel_instance.LocalizeMapInfoField(), password),
        "LocalizeManage": convert_string(excel_instance.LocalizeManageField(), password),
        "LocalizeUpgrade": convert_string(excel_instance.LocalizeUpgradeField(), password),
        "LocalizeTreasureBox": convert_string(excel_instance.LocalizeTreasureBoxField(), password),
        "IndividualErosionDailyCount": convert_int(excel_instance.IndividualErosionDailyCountField(), password),
    }

def dump_ExcelDB_ConquestGroupBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBonusId": convert_int(excel_instance.ConquestBonusIdField(), password),
        "School": [School(convert_int(excel_instance.SchoolField(j), password)).name for j in range(excel_instance.SchoolFieldLength())],
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcIdField(), password),
        "BonusParcelType": [ParcelType(convert_int(excel_instance.BonusParcelTypeField(j), password)).name for j in range(excel_instance.BonusParcelTypeFieldLength())],
        "BonusId": [convert_int(excel_instance.BonusIdField(j), password) for j in range(excel_instance.BonusIdFieldLength())],
        "BonusCharacterCount1": [convert_int(excel_instance.BonusCharacterCount1Field(j), password) for j in range(excel_instance.BonusCharacterCount1FieldLength())],
        "BonusPercentage1": [convert_int(excel_instance.BonusPercentage1Field(j), password) for j in range(excel_instance.BonusPercentage1FieldLength())],
        "BonusCharacterCount2": [convert_int(excel_instance.BonusCharacterCount2Field(j), password) for j in range(excel_instance.BonusCharacterCount2FieldLength())],
        "BonusPercentage2": [convert_int(excel_instance.BonusPercentage2Field(j), password) for j in range(excel_instance.BonusPercentage2FieldLength())],
        "BonusCharacterCount3": [convert_int(excel_instance.BonusCharacterCount3Field(j), password) for j in range(excel_instance.BonusCharacterCount3FieldLength())],
        "BonusPercentage3": [convert_int(excel_instance.BonusPercentage3Field(j), password) for j in range(excel_instance.BonusPercentage3FieldLength())],
    }

def dump_ExcelDB_ConquestGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBuffId": convert_int(excel_instance.ConquestBuffIdField(), password),
        "School": [School(convert_int(excel_instance.SchoolField(j), password)).name for j in range(excel_instance.SchoolFieldLength())],
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcIdField(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupIdField(), password),
    }

def dump_ExcelDB_ConquestMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficultyField(), password)).name,
        "StepIndex": convert_int(excel_instance.StepIndexField(), password),
        "ConquestMap": convert_string(excel_instance.ConquestMapField(), password),
        "StepEnterScenarioGroupId": convert_int(excel_instance.StepEnterScenarioGroupIdField(), password),
        "StepOpenConditionType": [ConquestConditionType(convert_int(excel_instance.StepOpenConditionTypeField(j), password)).name for j in range(excel_instance.StepOpenConditionTypeFieldLength())],
        "StepOpenConditionParameter": [convert_string(excel_instance.StepOpenConditionParameterField(j), password) for j in range(excel_instance.StepOpenConditionParameterFieldLength())],
        "MapGoalLocalize": convert_string(excel_instance.MapGoalLocalizeField(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalizeField(), password),
        "StepNameLocalize": convert_string(excel_instance.StepNameLocalizeField(), password),
        "ConquestMapBG": convert_string(excel_instance.ConquestMapBGField(), password),
        "CameraSettingId": convert_int(excel_instance.CameraSettingIdField(), password),
    }

def dump_ExcelDB_ConquestObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ConquestObjectType": ConquestObjectType(convert_int(excel_instance.ConquestObjectTypeField(), password)).name,
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "ConquestRewardParcelType": ParcelType(convert_int(excel_instance.ConquestRewardParcelTypeField(), password)).name,
        "ConquestRewardID": convert_int(excel_instance.ConquestRewardIDField(), password),
        "ConquestRewardAmount": convert_int(excel_instance.ConquestRewardAmountField(), password),
        "Disposable": bool(excel_instance.DisposableField()),
        "StepIndex": convert_int(excel_instance.StepIndexField(), password),
        "StepObjectCount": convert_int(excel_instance.StepObjectCountField(), password),
    }

def dump_ExcelDB_ConquestPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitleField(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePathField(), password),
        "GuideText": convert_string(excel_instance.GuideTextField(), password),
    }

def dump_ExcelDB_ConquestProgressResourceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Group": ConquestProgressType(convert_int(excel_instance.GroupField(), password)).name,
        "ProgressResource": convert_string(excel_instance.ProgressResourceField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "ProgressLocalizeCode": convert_string(excel_instance.ProgressLocalizeCodeField(), password),
    }

def dump_ExcelDB_ConquestRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "RewardProb": convert_int(excel_instance.RewardProbField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_ExcelDB_ConquestTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "EventId": convert_int(excel_instance.EventIdField(), password),
        "Step": convert_int(excel_instance.StepField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "TileNameLocalize": convert_string(excel_instance.TileNameLocalizeField(), password),
        "TileImageName": convert_string(excel_instance.TileImageNameField(), password),
        "Playable": bool(excel_instance.PlayableField()),
        "TileType": ConquestTileType(convert_int(excel_instance.TileTypeField(), password)).name,
        "NotMapFog": bool(excel_instance.NotMapFogField()),
        "GroupBonusId": convert_int(excel_instance.GroupBonusIdField(), password),
        "ConquestCostType": ParcelType(convert_int(excel_instance.ConquestCostTypeField(), password)).name,
        "ConquestCostId": convert_int(excel_instance.ConquestCostIdField(), password),
        "ConquestCostAmount": convert_int(excel_instance.ConquestCostAmountField(), password),
        "ManageCostType": ParcelType(convert_int(excel_instance.ManageCostTypeField(), password)).name,
        "ManageCostId": convert_int(excel_instance.ManageCostIdField(), password),
        "ManageCostAmount": convert_int(excel_instance.ManageCostAmountField(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardIdField(), password),
        "MassErosionId": convert_int(excel_instance.MassErosionIdField(), password),
        "Upgrade2CostType": ParcelType(convert_int(excel_instance.Upgrade2CostTypeField(), password)).name,
        "Upgrade2CostId": convert_int(excel_instance.Upgrade2CostIdField(), password),
        "Upgrade2CostAmount": convert_int(excel_instance.Upgrade2CostAmountField(), password),
        "Upgrade3CostType": ParcelType(convert_int(excel_instance.Upgrade3CostTypeField(), password)).name,
        "Upgrade3CostId": convert_int(excel_instance.Upgrade3CostIdField(), password),
        "Upgrade3CostAmount": convert_int(excel_instance.Upgrade3CostAmountField(), password),
    }

def dump_ExcelDB_ConquestUnexpectedEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UnexpectedEventConditionType": ParcelType(convert_int(excel_instance.UnexpectedEventConditionTypeField(), password)).name,
        "UnexpectedEventConditionUniqueId": convert_int(excel_instance.UnexpectedEventConditionUniqueIdField(), password),
        "UnexpectedEventConditionAmount": convert_int(excel_instance.UnexpectedEventConditionAmountField(), password),
        "UnexpectedEventOccurDailyLimitCount": convert_int(excel_instance.UnexpectedEventOccurDailyLimitCountField(), password),
        "UnitCountPerStep": convert_int(excel_instance.UnitCountPerStepField(), password),
        "UnexpectedEventPrefab": [convert_string(excel_instance.UnexpectedEventPrefabField(j), password) for j in range(excel_instance.UnexpectedEventPrefabFieldLength())],
        "UnexpectedEventUnitId": [convert_int(excel_instance.UnexpectedEventUnitIdField(j), password) for j in range(excel_instance.UnexpectedEventUnitIdFieldLength())],
    }

def dump_ExcelDB_ConquestUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "StrategyPrefabName": convert_string(excel_instance.StrategyPrefabNameField(), password),
        "Scale": convert_float(excel_instance.ScaleField(), password),
        "ShieldEffectScale": convert_float(excel_instance.ShieldEffectScaleField(), password),
        "UnitFxPrefabName": convert_string(excel_instance.UnitFxPrefabNameField(), password),
        "PointAnimation": convert_string(excel_instance.PointAnimationField(), password),
        "EnemyType": ConquestEnemyType(convert_int(excel_instance.EnemyTypeField(), password)).name,
        "Team": ConquestTeamType(convert_int(excel_instance.TeamField(), password)).name,
        "UnitGroup": convert_int(excel_instance.UnitGroupField(), password),
        "PrevUnitGroup": convert_int(excel_instance.PrevUnitGroupField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoalField(j), password)).name for j in range(excel_instance.StarGoalFieldLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmountField(j), password) for j in range(excel_instance.StarGoalAmountFieldLength())],
        "GroupBuffId": convert_int(excel_instance.GroupBuffIdField(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostTypeField(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostIdField(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmountField(), password),
        "ManageEchelonStageEnterCostType": ParcelType(convert_int(excel_instance.ManageEchelonStageEnterCostTypeField(), password)).name,
        "ManageEchelonStageEnterCostId": convert_int(excel_instance.ManageEchelonStageEnterCostIdField(), password),
        "ManageEchelonStageEnterCostAmount": convert_int(excel_instance.ManageEchelonStageEnterCostAmountField(), password),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupIdField(), password),
        "ClearScenarioGroupId": convert_int(excel_instance.ClearScenarioGroupIdField(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardIdField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "TacticRewardExp": convert_int(excel_instance.TacticRewardExpField(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_ContentEnterCostReduceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EnterCostReduceGroupId": convert_int(excel_instance.EnterCostReduceGroupIdField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "StageId": convert_int(excel_instance.StageIdField(), password),
        "ReduceEnterCostType": ParcelType(convert_int(excel_instance.ReduceEnterCostTypeField(), password)).name,
        "ReduceEnterCostId": convert_int(excel_instance.ReduceEnterCostIdField(), password),
        "ReduceAmount": convert_int(excel_instance.ReduceAmountField(), password),
    }

def dump_ExcelDB_ContentsFeverExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConditionContent": FeverBattleType(convert_int(excel_instance.ConditionContentField(), password)).name,
        "SkillFeverCheckCondition": SkillPriorityCheckTarget(convert_int(excel_instance.SkillFeverCheckConditionField(), password)).name,
        "SkillCostFever": convert_int(excel_instance.SkillCostFeverField(), password),
        "FeverStartTime": convert_int(excel_instance.FeverStartTimeField(), password),
        "FeverDurationTime": convert_int(excel_instance.FeverDurationTimeField(), password),
    }

def dump_ExcelDB_ContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitleField(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescriptionField(), password),
        "PopupType": SpoilerPopupType(convert_int(excel_instance.PopupTypeField(), password)).name,
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeIdField(), password),
    }

def dump_ExcelDB_ContentsScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.IdField(), password),
        "LocalizeId": convert_uint(excel_instance.LocalizeIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ScenarioContentType": ScenarioContentType(convert_int(excel_instance.ScenarioContentTypeField(), password)).name,
        "ScenarioGroupId": [convert_int(excel_instance.ScenarioGroupIdField(j), password) for j in range(excel_instance.ScenarioGroupIdFieldLength())],
    }

def dump_ExcelDB_ContentsShortcutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ScenarioModeType": ScenarioModeTypes(convert_int(excel_instance.ScenarioModeTypeField(), password)).name,
        "ScenarioModeSubType": ScenarioModeSubTypes(convert_int(excel_instance.ScenarioModeSubTypeField(), password)).name,
        "ScenarioModeVolume": convert_int(excel_instance.ScenarioModeVolumeField(), password),
        "ScenarioModeChapter": convert_int(excel_instance.ScenarioModeChapterField(), password),
        "ShortcutOpenTime": convert_string(excel_instance.ShortcutOpenTimeField(), password),
        "ShortcutCloseTime": convert_string(excel_instance.ShortcutCloseTimeField(), password),
        "ConditionContentId": convert_int(excel_instance.ConditionContentIdField(), password),
        "ConquestMapDifficulty": StageDifficulty(convert_int(excel_instance.ConquestMapDifficultyField(), password)).name,
        "ConquestStepIndex": convert_int(excel_instance.ConquestStepIndexField(), password),
        "ShortcutContentId": convert_int(excel_instance.ShortcutContentIdField(), password),
        "ShortcutUIName": [convert_string(excel_instance.ShortcutUINameField(j), password) for j in range(excel_instance.ShortcutUINameFieldLength())],
        "Localize": convert_string(excel_instance.LocalizeField(), password),
    }

def dump_ExcelDB_ContentTargetGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "AccountType": [AccountState(convert_int(excel_instance.AccountTypeField(j), password)).name for j in range(excel_instance.AccountTypeFieldLength())],
    }

def dump_ExcelDB_CostumeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeGroupId": convert_int(excel_instance.CostumeGroupIdField(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "IsDefault": bool(excel_instance.IsDefaultField()),
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "ReleaseDate": convert_string(excel_instance.ReleaseDateField(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDateField(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDateField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "CharacterSkillListGroupId": convert_int(excel_instance.CharacterSkillListGroupIdField(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceNameField(), password),
        "SpineResourceNameDiorama": convert_string(excel_instance.SpineResourceNameDioramaField(), password),
        "SpineResourceNameDioramaForFormConversion": [convert_string(excel_instance.SpineResourceNameDioramaForFormConversionField(j), password) for j in range(excel_instance.SpineResourceNameDioramaForFormConversionFieldLength())],
        "EntityMaterialType": EntityMaterialType(convert_int(excel_instance.EntityMaterialTypeField(), password)).name,
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabNameField(), password),
        "AnimatorName": convert_string(excel_instance.AnimatorNameField(), password),
        "CafeModelPrefabName": convert_string(excel_instance.CafeModelPrefabNameField(), password),
        "EchelonModelPrefabName": convert_string(excel_instance.EchelonModelPrefabNameField(), password),
        "StrategyModelPrefabName": convert_string(excel_instance.StrategyModelPrefabNameField(), password),
        "TextureDir": convert_string(excel_instance.TextureDirField(), password),
        "CollectionTexturePath": convert_string(excel_instance.CollectionTexturePathField(), password),
        "CollectionBGTexturePath": convert_string(excel_instance.CollectionBGTexturePathField(), password),
        "CombatStyleTexturePath": convert_string(excel_instance.CombatStyleTexturePathField(), password),
        "UseObjectHPBAR": bool(excel_instance.UseObjectHPBARField()),
        "TextureBoss": convert_string(excel_instance.TextureBossField(), password),
        "TextureSkillCard": [convert_string(excel_instance.TextureSkillCardField(j), password) for j in range(excel_instance.TextureSkillCardFieldLength())],
        "InformationPacel": convert_string(excel_instance.InformationPacelField(), password),
        "AnimationSSR": convert_string(excel_instance.AnimationSSRField(), password),
        "EnterStrategyAnimationName": convert_string(excel_instance.EnterStrategyAnimationNameField(), password),
        "AnimationValidator": bool(excel_instance.AnimationValidatorField()),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupIdField(), password),
        "ShowObjectHpStatus": bool(excel_instance.ShowObjectHpStatusField()),
    }

def dump_ExcelDB_CurrencyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "CurrencyType": CurrencyTypes(convert_int(excel_instance.CurrencyTypeField(), password)).name,
        "CurrencyName": convert_string(excel_instance.CurrencyNameField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "AutoChargeMsc": convert_int(excel_instance.AutoChargeMscField(), password),
        "AutoChargeAmount": convert_int(excel_instance.AutoChargeAmountField(), password),
        "CurrencyOverChargeType": CurrencyOverChargeType(convert_int(excel_instance.CurrencyOverChargeTypeField(), password)).name,
        "CurrencyAdditionalChargeType": CurrencyAdditionalChargeType(convert_int(excel_instance.CurrencyAdditionalChargeTypeField(), password)).name,
        "ChargeLimit": convert_int(excel_instance.ChargeLimitField(), password),
        "OverChargeLimit": convert_int(excel_instance.OverChargeLimitField(), password),
        "SpriteName": convert_string(excel_instance.SpriteNameField(), password),
        "DailyRefillType": DailyRefillType(convert_int(excel_instance.DailyRefillTypeField(), password)).name,
        "DailyRefillAmount": convert_int(excel_instance.DailyRefillAmountField(), password),
        "DailyRefillTime": [convert_int(excel_instance.DailyRefillTimeField(j), password) for j in range(excel_instance.DailyRefillTimeFieldLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTimeField(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateInField(), password),
        "ExpiryChangeParcelType": ParcelType(convert_int(excel_instance.ExpiryChangeParcelTypeField(), password)).name,
        "ExpiryChangeId": convert_int(excel_instance.ExpiryChangeIdField(), password),
        "ExpiryChangeAmount": convert_int(excel_instance.ExpiryChangeAmountField(), password),
        "ResetType": PeriodType(convert_int(excel_instance.ResetTypeField(), password)).name,
        "ResetAmount": convert_int(excel_instance.ResetAmountField(), password),
    }

def dump_ExcelDB_DuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ItemCategory": ItemCategory(convert_int(excel_instance.ItemCategoryField(), password)).name,
        "ItemId": convert_int(excel_instance.ItemIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_EchelonConstraintExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "IsWhiteList": bool(excel_instance.IsWhiteListField()),
        "CharacterId": [convert_int(excel_instance.CharacterIdField(j), password) for j in range(excel_instance.CharacterIdFieldLength())],
        "PersonalityId": [convert_int(excel_instance.PersonalityIdField(j), password) for j in range(excel_instance.PersonalityIdFieldLength())],
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponTypeField(), password)).name,
        "School": School(convert_int(excel_instance.SchoolField(), password)).name,
        "Club": Club(convert_int(excel_instance.ClubField(), password)).name,
        "Role": convert_float(excel_instance.RoleField(), password),
    }

def dump_ExcelDB_EliminateRaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "RankStart": convert_int(excel_instance.RankStartField(), password),
        "RankEnd": convert_int(excel_instance.RankEndField(), password),
        "RankStartTw": convert_int(excel_instance.RankStartTwField(), password),
        "RankEndTw": convert_int(excel_instance.RankEndTwField(), password),
        "RankStartAsia": convert_int(excel_instance.RankStartAsiaField(), password),
        "RankEndAsia": convert_int(excel_instance.RankEndAsiaField(), password),
        "RankStartNa": convert_int(excel_instance.RankStartNaField(), password),
        "RankEndNa": convert_int(excel_instance.RankEndNaField(), password),
        "RankStartGlobal": convert_int(excel_instance.RankStartGlobalField(), password),
        "RankEndGlobal": convert_int(excel_instance.RankEndGlobalField(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStartField(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEndField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
        "RewardParcelUniqueName": [convert_string(excel_instance.RewardParcelUniqueNameField(j), password) for j in range(excel_instance.RewardParcelUniqueNameFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EliminateRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "SeasonDisplay": convert_int(excel_instance.SeasonDisplayField(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartDataField(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDateField(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndDataField(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDateField(), password),
        "LobbyTableBGPath": convert_string(excel_instance.LobbyTableBGPathField(), password),
        "LobbyScreenBGPath": convert_string(excel_instance.LobbyScreenBGPathField(), password),
        "OpenRaidBossGroup01": convert_string(excel_instance.OpenRaidBossGroup01Field(), password),
        "OpenRaidBossGroup02": convert_string(excel_instance.OpenRaidBossGroup02Field(), password),
        "OpenRaidBossGroup03": convert_string(excel_instance.OpenRaidBossGroup03Field(), password),
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupIdField(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauageField(), password),
        "StackedSeasonRewardGauge": [convert_int(excel_instance.StackedSeasonRewardGaugeField(j), password) for j in range(excel_instance.StackedSeasonRewardGaugeFieldLength())],
        "SeasonRewardId": [convert_int(excel_instance.SeasonRewardIdField(j), password) for j in range(excel_instance.SeasonRewardIdFieldLength())],
        "LimitedRewardIdNormal": convert_int(excel_instance.LimitedRewardIdNormalField(), password),
        "LimitedRewardIdHard": convert_int(excel_instance.LimitedRewardIdHardField(), password),
        "LimitedRewardIdVeryhard": convert_int(excel_instance.LimitedRewardIdVeryhardField(), password),
        "LimitedRewardIdHardcore": convert_int(excel_instance.LimitedRewardIdHardcoreField(), password),
        "LimitedRewardIdExtreme": convert_int(excel_instance.LimitedRewardIdExtremeField(), password),
        "LimitedRewardIdInsane": convert_int(excel_instance.LimitedRewardIdInsaneField(), password),
        "LimitedRewardIdTorment": convert_int(excel_instance.LimitedRewardIdTormentField(), password),
    }

def dump_ExcelDB_EliminateRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndexField()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSyncField()),
        "RaidBossGroup": convert_string(excel_instance.RaidBossGroupField(), password),
        "RaidEnterCostType": ParcelType(convert_int(excel_instance.RaidEnterCostTypeField(), password)).name,
        "RaidEnterCostId": convert_int(excel_instance.RaidEnterCostIdField(), password),
        "RaidEnterCostAmount": convert_int(excel_instance.RaidEnterCostAmountField(), password),
        "BossSpinePath": convert_string(excel_instance.BossSpinePathField(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPathField(), password),
        "BGPath": convert_string(excel_instance.BGPathField(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterIdField(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterIdField(j), password) for j in range(excel_instance.BossCharacterIdFieldLength())],
        "Difficulty": Difficulty(convert_int(excel_instance.DifficultyField(), password)).name,
        "IsOpen": bool(excel_instance.IsOpenField()),
        "MaxPlayerCount": convert_int(excel_instance.MaxPlayerCountField(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTimeField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "RaidBossGroupType": RaidBossGroupType(convert_int(excel_instance.RaidBossGroupTypeField(), password)).name,
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLineField(), password),
        "TacticEnvironment": TacticEnvironment(convert_int(excel_instance.TacticEnvironmentField(), password)).name,
        "DefaultClearScore": convert_int(excel_instance.DefaultClearScoreField(), password),
        "MaximumScore": convert_int(excel_instance.MaximumScoreField(), password),
        "PerSecondMinusScore": convert_int(excel_instance.PerSecondMinusScoreField(), password),
        "HPPercentScore": convert_int(excel_instance.HPPercentScoreField(), password),
        "MinimumAcquisitionScore": convert_int(excel_instance.MinimumAcquisitionScoreField(), password),
        "MaximumAcquisitionScore": convert_int(excel_instance.MaximumAcquisitionScoreField(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupIdField(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePathField(j), password) for j in range(excel_instance.BattleReadyTimelinePathFieldLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStartField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartFieldLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEndField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndFieldLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePathField(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePathField(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhaseField(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKeyField(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKeyField(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCardField()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKeyField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_EliminateRaidStageLimitedRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LimitedRewardId": convert_int(excel_instance.LimitedRewardIdField(), password),
        "LimitedRewardParcelType": [ParcelType(convert_int(excel_instance.LimitedRewardParcelTypeField(j), password)).name for j in range(excel_instance.LimitedRewardParcelTypeFieldLength())],
        "LimitedRewardParcelUniqueId": [convert_int(excel_instance.LimitedRewardParcelUniqueIdField(j), password) for j in range(excel_instance.LimitedRewardParcelUniqueIdFieldLength())],
        "LimitedRewardAmount": [convert_int(excel_instance.LimitedRewardAmountField(j), password) for j in range(excel_instance.LimitedRewardAmountFieldLength())],
    }

def dump_ExcelDB_EliminateRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfoField()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProbField(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelTypeField(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueIDField(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmountField(), password),
    }

def dump_ExcelDB_EliminateRaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_int(excel_instance.SeasonRewardIdField(), password),
        "SeasonRewardParcelType": [ParcelType(convert_int(excel_instance.SeasonRewardParcelTypeField(j), password)).name for j in range(excel_instance.SeasonRewardParcelTypeFieldLength())],
        "SeasonRewardParcelUniqueId": [convert_int(excel_instance.SeasonRewardParcelUniqueIdField(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueIdFieldLength())],
        "SeasonRewardAmount": [convert_int(excel_instance.SeasonRewardAmountField(j), password) for j in range(excel_instance.SeasonRewardAmountFieldLength())],
    }

def dump_ExcelDB_EmblemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Category": EmblemCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeIdField(), password),
        "UseAtLocalizeId": convert_int(excel_instance.UseAtLocalizeIdField(), password),
        "EmblemTextVisible": bool(excel_instance.EmblemTextVisibleField()),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "EmblemIconPath": convert_string(excel_instance.EmblemIconPathField(), password),
        "EmblemIconNumControl": convert_int(excel_instance.EmblemIconNumControlField(), password),
        "EmblemIconBGPath": convert_string(excel_instance.EmblemIconBGPathField(), password),
        "EmblemBGPathJp": convert_string(excel_instance.EmblemBGPathJpField(), password),
        "EmblemBGPathKr": convert_string(excel_instance.EmblemBGPathKrField(), password),
        "EmblemBGPathTh": convert_string(excel_instance.EmblemBGPathThField(), password),
        "EmblemBGPathTw": convert_string(excel_instance.EmblemBGPathTwField(), password),
        "EmblemBGPathEn": convert_string(excel_instance.EmblemBGPathEnField(), password),
        "EmblemEffectPath": convert_string(excel_instance.EmblemEffectPathField(), password),
        "DisplayType": EmblemDisplayType(convert_int(excel_instance.DisplayTypeField(), password)).name,
        "DisplayStartDate": convert_string(excel_instance.DisplayStartDateField(), password),
        "DisplayEndDate": convert_string(excel_instance.DisplayEndDateField(), password),
        "DislpayFavorLevel": convert_int(excel_instance.DislpayFavorLevelField(), password),
        "CheckPassType": EmblemCheckPassType(convert_int(excel_instance.CheckPassTypeField(), password)).name,
        "EmblemParameter": convert_int(excel_instance.EmblemParameterField(), password),
        "CheckPassCount": convert_int(excel_instance.CheckPassCountField(), password),
    }

def dump_ExcelDB_EquipmentChangePieceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EquipmentId": convert_int(excel_instance.EquipmentIdField(), password),
        "ChangeEquipmentId": convert_int(excel_instance.ChangeEquipmentIdField(), password),
        "ChangeAmount": convert_int(excel_instance.ChangeAmountField(), password),
    }

def dump_ExcelDB_EquipmentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EquipmentCategory": EquipmentCategory(convert_int(excel_instance.EquipmentCategoryField(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "Wear": bool(excel_instance.WearField()),
        "MaxLevel": convert_int(excel_instance.MaxLevelField(), password),
        "RecipeId": convert_int(excel_instance.RecipeIdField(), password),
        "TierInit": convert_int(excel_instance.TierInitField(), password),
        "NextTierEquipment": convert_int(excel_instance.NextTierEquipmentField(), password),
        "StackableMax": convert_int(excel_instance.StackableMaxField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
        "ImageName": convert_string(excel_instance.ImageNameField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0Field(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1Field(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2Field(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQualityField(), password),
        "ShopCategory": [convert_float(excel_instance.ShopCategoryField(j), password) for j in range(excel_instance.ShopCategoryFieldLength())],
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeIdField(), password),
        "RedirectItemId": convert_int(excel_instance.RedirectItemIdField(), password),
    }

def dump_ExcelDB_EquipmentLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "TierLevelExp": [convert_int(excel_instance.TierLevelExpField(j), password) for j in range(excel_instance.TierLevelExpFieldLength())],
        "TotalExp": [convert_int(excel_instance.TotalExpField(j), password) for j in range(excel_instance.TotalExpFieldLength())],
    }

def dump_ExcelDB_EquipmentStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EquipmentId": convert_int(excel_instance.EquipmentIdField(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpTypeField(), password)).name,
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatTypeField(j), password)).name for j in range(excel_instance.StatTypeFieldLength())],
        "MinStat": [convert_int(excel_instance.MinStatField(j), password) for j in range(excel_instance.MinStatFieldLength())],
        "MaxStat": [convert_int(excel_instance.MaxStatField(j), password) for j in range(excel_instance.MaxStatFieldLength())],
        "LevelUpInsertLimit": convert_int(excel_instance.LevelUpInsertLimitField(), password),
        "LevelUpFeedExp": convert_int(excel_instance.LevelUpFeedExpField(), password),
        "LevelUpFeedCostCurrency": CurrencyTypes(convert_int(excel_instance.LevelUpFeedCostCurrencyField(), password)).name,
        "LevelUpFeedCostAmount": convert_int(excel_instance.LevelUpFeedCostAmountField(), password),
        "EquipmentCategory": EquipmentCategory(convert_int(excel_instance.EquipmentCategoryField(), password)).name,
        "LevelUpFeedAddExp": convert_int(excel_instance.LevelUpFeedAddExpField(), password),
        "DefaultMaxLevel": convert_int(excel_instance.DefaultMaxLevelField(), password),
        "TranscendenceMax": convert_int(excel_instance.TranscendenceMaxField(), password),
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupIdField(), password),
    }

def dump_ExcelDB_EventContentArchiveBannerOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "OffsetX": convert_float(excel_instance.OffsetXField(), password),
        "OffsetY": convert_float(excel_instance.OffsetYField(), password),
        "ScaleX": convert_float(excel_instance.ScaleXField(), password),
        "ScaleY": convert_float(excel_instance.ScaleYField(), password),
    }

def dump_ExcelDB_EventContentBoxGachaManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Round": convert_int(excel_instance.RoundField(), password),
        "GoodsId": convert_int(excel_instance.GoodsIdField(), password),
        "IsLoop": bool(excel_instance.IsLoopField()),
    }

def dump_ExcelDB_EventContentBoxGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "GroupElementAmount": convert_int(excel_instance.GroupElementAmountField(), password),
        "Round": convert_int(excel_instance.RoundField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "IsPrize": bool(excel_instance.IsPrizeField()),
        "GoodsId": [convert_int(excel_instance.GoodsIdField(j), password) for j in range(excel_instance.GoodsIdFieldLength())],
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
    }

def dump_ExcelDB_EventContentBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentBuffId": convert_int(excel_instance.EventContentBuffIdField(), password),
        "IsBuff": bool(excel_instance.IsBuffField()),
        "CharacterTag": Tag(convert_int(excel_instance.CharacterTagField(), password)).name,
        "EnumType": EventContentBuffFindRule(convert_int(excel_instance.EnumTypeField(), password)).name,
        "EnumTypeValue": [convert_string(excel_instance.EnumTypeValueField(j), password) for j in range(excel_instance.EnumTypeValueFieldLength())],
        "SkillGroupId": convert_string(excel_instance.SkillGroupIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "SpriteName": convert_string(excel_instance.SpriteNameField(), password),
        "BuffDescriptionLocalizeCodeId": convert_string(excel_instance.BuffDescriptionLocalizeCodeIdField(), password),
    }

def dump_ExcelDB_EventContentBuffGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "BuffContentId": convert_int(excel_instance.BuffContentIdField(), password),
        "BuffGroupId": convert_int(excel_instance.BuffGroupIdField(), password),
        "BuffGroupNameLocalizeCodeId": convert_string(excel_instance.BuffGroupNameLocalizeCodeIdField(), password),
        "EventContentBuffId1": convert_int(excel_instance.EventContentBuffId1Field(), password),
        "BuffNameLocalizeCodeId1": convert_string(excel_instance.BuffNameLocalizeCodeId1Field(), password),
        "BuffDescriptionIconPath1": convert_string(excel_instance.BuffDescriptionIconPath1Field(), password),
        "EventContentBuffId2": convert_int(excel_instance.EventContentBuffId2Field(), password),
        "BuffNameLocalizeCodeId2": convert_string(excel_instance.BuffNameLocalizeCodeId2Field(), password),
        "BuffDescriptionIconPath2": convert_string(excel_instance.BuffDescriptionIconPath2Field(), password),
        "EventContentDebuffId": convert_int(excel_instance.EventContentDebuffIdField(), password),
        "DebuffNameLocalizeCodeId": convert_string(excel_instance.DebuffNameLocalizeCodeIdField(), password),
        "DeBuffDescriptionIconPath": convert_string(excel_instance.DeBuffDescriptionIconPathField(), password),
        "BuffGroupProb": convert_int(excel_instance.BuffGroupProbField(), password),
    }

def dump_ExcelDB_EventContentCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CardGroupId": convert_int(excel_instance.CardGroupIdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "BackIconPath": convert_string(excel_instance.BackIconPathField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
    }

def dump_ExcelDB_EventContentCardShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "CostGoodsId": convert_int(excel_instance.CostGoodsIdField(), password),
        "CardGroupId": convert_int(excel_instance.CardGroupIdField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "RefreshGroup": convert_int(excel_instance.RefreshGroupField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "ProbWeight1": convert_int(excel_instance.ProbWeight1Field(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentCardShopModifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabNameField(), password),
    }

def dump_ExcelDB_EventContentChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ChangeCount": convert_int(excel_instance.ChangeCountField(), password),
        "IsLast": bool(excel_instance.IsLastField()),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
        "ChangeCostType": ParcelType(convert_int(excel_instance.ChangeCostTypeField(), password)).name,
        "ChangeCostId": convert_int(excel_instance.ChangeCostIdField(), password),
        "ChangeCostAmount": convert_int(excel_instance.ChangeCostAmountField(), password),
    }

def dump_ExcelDB_EventContentChangeScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ChangeType": EventChangeType(convert_int(excel_instance.ChangeTypeField(), password)).name,
        "ChangeCount": convert_int(excel_instance.ChangeCountField(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
    }

def dump_ExcelDB_EventContentCharacterBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "EventContentItemType": [EventContentItemType(convert_int(excel_instance.EventContentItemTypeField(j), password)).name for j in range(excel_instance.EventContentItemTypeFieldLength())],
        "BonusPercentage": [convert_int(excel_instance.BonusPercentageField(j), password) for j in range(excel_instance.BonusPercentageFieldLength())],
    }

def dump_ExcelDB_EventContentClueExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ClueId": convert_int(excel_instance.ClueIdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "SlotClueImagePath": convert_string(excel_instance.SlotClueImagePathField(), password),
        "ClueImagePath": convert_string(excel_instance.ClueImagePathField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
        "HintUse": bool(excel_instance.HintUseField()),
        "Hintlocalizeid": convert_uint(excel_instance.HintlocalizeidField(), password),
    }

def dump_ExcelDB_EventContentClueSearchExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "TitleLocalize": convert_uint(excel_instance.TitleLocalizeField(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabNameField(), password),
        "ClueBGImagePath": convert_string(excel_instance.ClueBGImagePathField(), password),
    }

def dump_ExcelDB_EventContentClueSearchRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentClueSearchRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Round": convert_int(excel_instance.RoundField(), password),
        "IsLoop": bool(excel_instance.IsLoopField()),
        "TargetImagePath": convert_string(excel_instance.TargetImagePathField(), password),
        "Localizeld": convert_uint(excel_instance.LocalizeldField(), password),
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "ClueSlotNumber": [convert_int(excel_instance.ClueSlotNumberField(j), password) for j in range(excel_instance.ClueSlotNumberFieldLength())],
        "ClueId": [convert_int(excel_instance.ClueIdField(j), password) for j in range(excel_instance.ClueIdFieldLength())],
        "ClueCostAmount": [convert_int(excel_instance.ClueCostAmountField(j), password) for j in range(excel_instance.ClueCostAmountFieldLength())],
        "HintlocalizeId": convert_uint(excel_instance.HintlocalizeIdField(), password),
        "ClearlocalizeId": convert_uint(excel_instance.ClearlocalizeIdField(), password),
        "ClearPageImagePath": convert_string(excel_instance.ClearPageImagePathField(), password),
    }

def dump_ExcelDB_EventContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "UnlockConditionType": CollectionUnlockType(convert_int(excel_instance.UnlockConditionTypeField(), password)).name,
        "UnlockConditionParameter": [convert_int(excel_instance.UnlockConditionParameterField(j), password) for j in range(excel_instance.UnlockConditionParameterFieldLength())],
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckTypeField(), password)).name,
        "UnlockConditionCount": convert_int(excel_instance.UnlockConditionCountField(), password),
        "IsObject": bool(excel_instance.IsObjectField()),
        "IsObjectOnFullResource": bool(excel_instance.IsObjectOnFullResourceField()),
        "IsHorizon": bool(excel_instance.IsHorizonField()),
        "EmblemResource": convert_string(excel_instance.EmblemResourceField(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResourceField(), password),
        "FullResource": convert_string(excel_instance.FullResourceField(), password),
        "Decoration": convert_string(excel_instance.DecorationField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeIdField(), password),
    }

def dump_ExcelDB_EventContentConcentrationCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CardId": convert_int(excel_instance.CardIdField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
    }

def dump_ExcelDB_EventContentConcentrationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsIdField(), password),
        "MaxCardPairCount": convert_int(excel_instance.MaxCardPairCountField(), password),
        "MaxCardOpenCount": convert_int(excel_instance.MaxCardOpenCountField(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRoundField(), password),
        "CardBoardPrefabs": convert_string(excel_instance.CardBoardPrefabsField(), password),
        "BackImagePath": convert_string(excel_instance.BackImagePathField(), password),
    }

def dump_ExcelDB_EventContentConcentrationRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "ConcentrationRewardType": ConcentrationRewardType(convert_int(excel_instance.ConcentrationRewardTypeField(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "Round": convert_int(excel_instance.RoundField(), password),
        "IsLoop": bool(excel_instance.IsLoopField()),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentConcentrationVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "VoiceCondition": ConcentrationVoiceCondition(convert_int(excel_instance.VoiceConditionField(), password)).name,
        "VoiceClip": convert_uint(excel_instance.VoiceClipField(), password),
    }

def dump_ExcelDB_EventContentCurrencyItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentItemType": EventContentItemType(convert_int(excel_instance.EventContentItemTypeField(), password)).name,
        "ItemUniqueId": convert_int(excel_instance.ItemUniqueIdField(), password),
        "UseShortCutContentType": convert_string(excel_instance.UseShortCutContentTypeField(), password),
    }

def dump_ExcelDB_EventContentDebuffRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventStageId": convert_int(excel_instance.EventStageIdField(), password),
        "EventContentItemType": EventContentItemType(convert_int(excel_instance.EventContentItemTypeField(), password)).name,
        "RewardPercentage": convert_int(excel_instance.RewardPercentageField(), password),
    }

def dump_ExcelDB_EventContentDiceRaceEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentDiceRaceResultType": EventContentDiceRaceResultType(convert_int(excel_instance.EventContentDiceRaceResultTypeField(), password)).name,
        "IsDiceResult": bool(excel_instance.IsDiceResultField()),
        "AniClip": convert_string(excel_instance.AniClipField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DiceCostGoodsId": convert_int(excel_instance.DiceCostGoodsIdField(), password),
        "SkipableLap": convert_int(excel_instance.SkipableLapField(), password),
        "DiceRacePawnPrefab": convert_string(excel_instance.DiceRacePawnPrefabField(), password),
        "IsUsingFixedDice": bool(excel_instance.IsUsingFixedDiceField()),
        "FixedDiceIcon": [convert_string(excel_instance.FixedDiceIconField(j), password) for j in range(excel_instance.FixedDiceIconFieldLength())],
        "DiceRaceEventType": [convert_string(excel_instance.DiceRaceEventTypeField(j), password) for j in range(excel_instance.DiceRaceEventTypeFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "NodeId": convert_int(excel_instance.NodeIdField(), password),
        "EventContentDiceRaceNodeType": EventContentDiceRaceNodeType(convert_int(excel_instance.EventContentDiceRaceNodeTypeField(), password)).name,
        "MoveForwardTypeArg": convert_int(excel_instance.MoveForwardTypeArgField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceProbExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentDiceRaceResultType": EventContentDiceRaceResultType(convert_int(excel_instance.EventContentDiceRaceResultTypeField(), password)).name,
        "CostItemId": convert_int(excel_instance.CostItemIdField(), password),
        "CostItemAmount": convert_int(excel_instance.CostItemAmountField(), password),
        "DiceResult": convert_int(excel_instance.DiceResultField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
    }

def dump_ExcelDB_EventContentDiceRaceTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "RewardID": convert_int(excel_instance.RewardIDField(), password),
        "RequiredLapFinishCount": convert_int(excel_instance.RequiredLapFinishCountField(), password),
        "DisplayLapFinishCount": convert_int(excel_instance.DisplayLapFinishCountField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentFortuneGachaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupIdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "NameImagePath": convert_string(excel_instance.NameImagePathField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
    }

def dump_ExcelDB_EventContentFortuneGachaModifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "TargetGrade": convert_int(excel_instance.TargetGradeField(), password),
        "ProbModifyStartCount": convert_int(excel_instance.ProbModifyStartCountField(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabNameField(), password),
        "BucketImagePath": convert_string(excel_instance.BucketImagePathField(), password),
        "ShopBgImagePath": convert_string(excel_instance.ShopBgImagePathField(), password),
        "TitleLocalizeKey": convert_string(excel_instance.TitleLocalizeKeyField(), password),
    }

def dump_ExcelDB_EventContentFortuneGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "Grade": convert_int(excel_instance.GradeField(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsIdField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupIdField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "ProbModifyValue": convert_int(excel_instance.ProbModifyValueField(), password),
        "ProbModifyLimit": convert_int(excel_instance.ProbModifyLimitField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentLobbyMenuExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentTypeField(), password)).name,
        "IconSpriteName": convert_string(excel_instance.IconSpriteNameField(), password),
        "ButtonText": convert_string(excel_instance.ButtonTextField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "IconOffsetX": convert_float(excel_instance.IconOffsetXField(), password),
        "IconOffsetY": convert_float(excel_instance.IconOffsetYField(), password),
        "ReddotSpriteName": convert_string(excel_instance.ReddotSpriteNameField(), password),
    }

def dump_ExcelDB_EventContentLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPathField(), password),
        "LocationResetScheduleCount": convert_int(excel_instance.LocationResetScheduleCountField(), password),
        "ScheduleEventPointCostParcelType": ParcelType(convert_int(excel_instance.ScheduleEventPointCostParcelTypeField(), password)).name,
        "ScheduleEventPointCostParcelId": convert_int(excel_instance.ScheduleEventPointCostParcelIdField(), password),
        "ScheduleEventPointCostParcelAmount": convert_int(excel_instance.ScheduleEventPointCostParcelAmountField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "InformationGroupId": convert_int(excel_instance.InformationGroupIdField(), password),
    }

def dump_ExcelDB_EventContentLocationRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Location": convert_string(excel_instance.LocationField(), password),
        "ScheduleGroupId": convert_int(excel_instance.ScheduleGroupIdField(), password),
        "OrderInGroup": convert_int(excel_instance.OrderInGroupField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "ProgressTexture": convert_string(excel_instance.ProgressTextureField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "LocationRank": convert_int(excel_instance.LocationRankField(), password),
        "FavorExp": convert_int(excel_instance.FavorExpField(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmountField(), password),
        "SecretStoneProb": convert_int(excel_instance.SecretStoneProbField(), password),
        "ExtraFavorExp": convert_int(excel_instance.ExtraFavorExpField(), password),
        "ExtraFavorExpProb": convert_int(excel_instance.ExtraFavorExpProbField(), password),
        "ExtraRewardParcelType": [ParcelType(convert_int(excel_instance.ExtraRewardParcelTypeField(j), password)).name for j in range(excel_instance.ExtraRewardParcelTypeFieldLength())],
        "ExtraRewardParcelId": [convert_int(excel_instance.ExtraRewardParcelIdField(j), password) for j in range(excel_instance.ExtraRewardParcelIdFieldLength())],
        "ExtraRewardAmount": [convert_int(excel_instance.ExtraRewardAmountField(j), password) for j in range(excel_instance.ExtraRewardAmountFieldLength())],
        "ExtraRewardProb": [convert_int(excel_instance.ExtraRewardProbField(j), password) for j in range(excel_instance.ExtraRewardProbFieldLength())],
        "IsExtraRewardDisplayed": [bool(excel_instance.IsExtraRewardDisplayedField(j)) for j in range(excel_instance.IsExtraRewardDisplayedFieldLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_EventContentMeetupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "ConditionScenarioGroupId": convert_int(excel_instance.ConditionScenarioGroupIdField(), password),
        "ConditionType": MeetupConditionType(convert_int(excel_instance.ConditionTypeField(), password)).name,
        "ConditionParameter": [convert_int(excel_instance.ConditionParameterField(j), password) for j in range(excel_instance.ConditionParameterFieldLength())],
        "ConditionPrintType": MeetupConditionPrintType(convert_int(excel_instance.ConditionPrintTypeField(), password)).name,
    }

def dump_ExcelDB_EventContentMeetupInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CostParcelType": ParcelType(convert_int(excel_instance.CostParcelTypeField(), password)).name,
        "CostId": convert_int(excel_instance.CostIdField(), password),
        "CostAmount": convert_int(excel_instance.CostAmountField(), password),
    }

def dump_ExcelDB_EventContentMiniEventShortCutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "ShorcutContentType": EventTargetType(convert_int(excel_instance.ShorcutContentTypeField(), password)).name,
        "ShortcutUI": convert_string(excel_instance.ShortcutUIField(), password),
    }

def dump_ExcelDB_EventContentMiniEventTokenExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ItemUniqueId": convert_int(excel_instance.ItemUniqueIdField(), password),
        "MaximumAmount": convert_int(excel_instance.MaximumAmountField(), password),
    }

def dump_ExcelDB_EventContentMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "GroupName": convert_string(excel_instance.GroupNameField(), password),
        "Category": MissionCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetTypeField(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayTypeField(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePathField(), password),
        "ViewFlag": bool(excel_instance.ViewFlagField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionIdField(j), password) for j in range(excel_instance.PreMissionIdFieldLength())],
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "AccountLevel": convert_int(excel_instance.AccountLevelField(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUIField(j), password) for j in range(excel_instance.ShortcutUIFieldLength())],
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcutField(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionTypeField(), password)).name,
        "IsCompleteExtensionTime": bool(excel_instance.IsCompleteExtensionTimeField()),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCountField(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameterField(j), password) for j in range(excel_instance.CompleteConditionParameterFieldLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTagField(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagFieldLength())],
        "RewardIcon": convert_string(excel_instance.RewardIconField(), password),
        "CompleteConditionMissionId": [convert_int(excel_instance.CompleteConditionMissionIdField(j), password) for j in range(excel_instance.CompleteConditionMissionIdFieldLength())],
        "CompleteConditionMissionCount": convert_int(excel_instance.CompleteConditionMissionCountField(), password),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelTypeField(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeFieldLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelIdField(j), password) for j in range(excel_instance.MissionRewardParcelIdFieldLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmountField(j), password) for j in range(excel_instance.MissionRewardAmountFieldLength())],
        "ConditionRewardParcelType": [ParcelType(convert_int(excel_instance.ConditionRewardParcelTypeField(j), password)).name for j in range(excel_instance.ConditionRewardParcelTypeFieldLength())],
        "ConditionRewardParcelId": [convert_int(excel_instance.ConditionRewardParcelIdField(j), password) for j in range(excel_instance.ConditionRewardParcelIdFieldLength())],
        "ConditionRewardAmount": [convert_int(excel_instance.ConditionRewardAmountField(j), password) for j in range(excel_instance.ConditionRewardAmountFieldLength())],
    }

def dump_ExcelDB_EventContentNotifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "EventNotifyType": EventNotifyType(convert_int(excel_instance.EventNotifyTypeField(), password)).name,
        "EventTargetType": EventTargetType(convert_int(excel_instance.EventTargetTypeField(), password)).name,
        "ShortcutEventTargetType": EventTargetType(convert_int(excel_instance.ShortcutEventTargetTypeField(), password)).name,
        "IsShortcutEnable": bool(excel_instance.IsShortcutEnableField()),
    }

def dump_ExcelDB_EventContentPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "IsPcBuild": bool(excel_instance.IsPcBuildField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitleField(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePathField(), password),
        "GuideText": convert_string(excel_instance.GuideTextField(), password),
    }

def dump_ExcelDB_EventContentScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ReturnScenarioPlay": bool(excel_instance.ReturnScenarioPlayField()),
        "ReplayDisplayGroup": convert_int(excel_instance.ReplayDisplayGroupField(), password),
        "Order": convert_int(excel_instance.OrderField(), password),
        "RecollectionNumber": convert_int(excel_instance.RecollectionNumberField(), password),
        "IsRecollection": bool(excel_instance.IsRecollectionField()),
        "IsMeetup": bool(excel_instance.IsMeetupField()),
        "IsOmnibus": bool(excel_instance.IsOmnibusField()),
        "ScenarioGroupId": [convert_int(excel_instance.ScenarioGroupIdField(j), password) for j in range(excel_instance.ScenarioGroupIdFieldLength())],
        "ScenarioConditionType": EventContentScenarioConditionType(convert_int(excel_instance.ScenarioConditionTypeField(), password)).name,
        "ConditionAmount": convert_int(excel_instance.ConditionAmountField(), password),
        "ConditionEventContentId": convert_int(excel_instance.ConditionEventContentIdField(), password),
        "ClearedScenarioGroupId": convert_int(excel_instance.ClearedScenarioGroupIdField(), password),
        "RecollectionSummaryLocalizeScenarioId": convert_uint(excel_instance.RecollectionSummaryLocalizeScenarioIdField(), password),
        "RecollectionResource": convert_string(excel_instance.RecollectionResourceField(), password),
        "IsRecollectionHorizon": bool(excel_instance.IsRecollectionHorizonField()),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardId": [convert_int(excel_instance.RewardIdField(j), password) for j in range(excel_instance.RewardIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_EventContentSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "OriginalEventContentId": convert_int(excel_instance.OriginalEventContentIdField(), password),
        "IsReturn": bool(excel_instance.IsReturnField()),
        "Name": convert_string(excel_instance.NameField(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentTypeField(), password)).name,
        "OpenConditionContent": OpenConditionContent(convert_int(excel_instance.OpenConditionContentField(), password)).name,
        "EventDisplay": bool(excel_instance.EventDisplayField()),
        "IconOrder": convert_int(excel_instance.IconOrderField(), password),
        "SubEventType": SubEventType(convert_int(excel_instance.SubEventTypeField(), password)).name,
        "SubEvent": bool(excel_instance.SubEventField()),
        "EventItemId": convert_int(excel_instance.EventItemIdField(), password),
        "MainEventId": convert_int(excel_instance.MainEventIdField(), password),
        "EventChangeOpenCondition": convert_int(excel_instance.EventChangeOpenConditionField(), password),
        "BeforehandExposedTime": convert_string(excel_instance.BeforehandExposedTimeField(), password),
        "EventContentOpenTime": convert_string(excel_instance.EventContentOpenTimeField(), password),
        "EventContentCloseNoteTime": convert_string(excel_instance.EventContentCloseNoteTimeField(), password),
        "EventContentCloseTime": convert_string(excel_instance.EventContentCloseTimeField(), password),
        "ExtensionTime": convert_string(excel_instance.ExtensionTimeField(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPathField(), password),
        "SubIconParcelPath": convert_string(excel_instance.SubIconParcelPathField(), password),
        "BeforehandBgImagePath": convert_string(excel_instance.BeforehandBgImagePathField(), password),
        "MinigamePrologScenarioGroupId": convert_int(excel_instance.MinigamePrologScenarioGroupIdField(), password),
        "BeforehandScenarioGroupId": [convert_int(excel_instance.BeforehandScenarioGroupIdField(j), password) for j in range(excel_instance.BeforehandScenarioGroupIdFieldLength())],
        "MainBannerImagePath": convert_string(excel_instance.MainBannerImagePathField(), password),
        "MainBgImagePath": convert_string(excel_instance.MainBgImagePathField(), password),
        "ShiftTriggerStageId": convert_int(excel_instance.ShiftTriggerStageIdField(), password),
        "ShiftMainBgImagePath": convert_string(excel_instance.ShiftMainBgImagePathField(), password),
        "MinigameLobbyPrefabName": convert_string(excel_instance.MinigameLobbyPrefabNameField(), password),
        "MinigameVictoryPrefabName": convert_string(excel_instance.MinigameVictoryPrefabNameField(), password),
        "MinigameMissionBgPrefabName": convert_string(excel_instance.MinigameMissionBgPrefabNameField(), password),
        "MinigameMissionBgImagePath": convert_string(excel_instance.MinigameMissionBgImagePathField(), password),
        "CardBgImagePath": convert_string(excel_instance.CardBgImagePathField(), password),
        "EventAssist": bool(excel_instance.EventAssistField()),
        "EventContentReleaseType": EventContentReleaseType(convert_int(excel_instance.EventContentReleaseTypeField(), password)).name,
        "EventContentStageRewardIdPermanent": convert_int(excel_instance.EventContentStageRewardIdPermanentField(), password),
        "RewardTagPermanent": convert_float(excel_instance.RewardTagPermanentField(), password),
        "MiniEventShortCutScenarioModeId": convert_int(excel_instance.MiniEventShortCutScenarioModeIdField(), password),
        "ScenarioContentCollectionGroupId": convert_int(excel_instance.ScenarioContentCollectionGroupIdField(), password),
    }

def dump_ExcelDB_EventContentShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "GoodsId": [convert_int(excel_instance.GoodsIdField(j), password) for j in range(excel_instance.GoodsIdFieldLength())],
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFromField(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodToField(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMinField(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetTypeField(), password)).name,
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventNameField(), password),
        "RestrictBuyWhenInventoryFull": bool(excel_instance.RestrictBuyWhenInventoryFullField()),
    }

def dump_ExcelDB_EventContentShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "LocalizeCode": convert_uint(excel_instance.LocalizeCodeField(), password),
        "CostParcelType": [ParcelType(convert_int(excel_instance.CostParcelTypeField(j), password)).name for j in range(excel_instance.CostParcelTypeFieldLength())],
        "CostParcelId": [convert_int(excel_instance.CostParcelIdField(j), password) for j in range(excel_instance.CostParcelIdFieldLength())],
        "IsRefresh": bool(excel_instance.IsRefreshField()),
        "IsSoldOutDimmed": bool(excel_instance.IsSoldOutDimmedField()),
        "AutoRefreshCoolTime": convert_int(excel_instance.AutoRefreshCoolTimeField(), password),
        "RefreshAbleCount": convert_int(excel_instance.RefreshAbleCountField(), password),
        "GoodsId": [convert_int(excel_instance.GoodsIdField(j), password) for j in range(excel_instance.GoodsIdFieldLength())],
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFromField(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodToField(), password),
        "ShopProductUpdateDate": convert_string(excel_instance.ShopProductUpdateDateField(), password),
    }

def dump_ExcelDB_EventContentShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "GoodsId": convert_int(excel_instance.GoodsIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "RefreshGroup": convert_int(excel_instance.RefreshGroupField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventNameField(), password),
        "ProductUpdateTime": convert_string(excel_instance.ProductUpdateTimeField(), password),
    }

def dump_ExcelDB_EventContentSpecialOperationsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "PointItemId": convert_int(excel_instance.PointItemIdField(), password),
    }

def dump_ExcelDB_EventContentSpineDialogOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentTypeField(), password)).name,
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "SpineOffsetX": convert_float(excel_instance.SpineOffsetXField(), password),
        "SpineOffsetY": convert_float(excel_instance.SpineOffsetYField(), password),
        "DialogOffsetX": convert_float(excel_instance.DialogOffsetXField(), password),
        "DialogOffsetY": convert_float(excel_instance.DialogOffsetYField(), password),
    }

def dump_ExcelDB_EventContentSpineDisplayPeriodExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategoryField(), password)).name,
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "ShowPeriodFrom": convert_string(excel_instance.ShowPeriodFromField(), password),
        "ShowPeriodTo": convert_string(excel_instance.ShowPeriodToField(), password),
        "ShowWorldRaidConditionIDFrom": convert_int(excel_instance.ShowWorldRaidConditionIDFromField(), password),
        "ShowWorldRaidConditionIDTo": convert_int(excel_instance.ShowWorldRaidConditionIDToField(), password),
    }

def dump_ExcelDB_EventContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitleField(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescriptionField(), password),
        "PopupType": SpoilerPopupType(convert_int(excel_instance.PopupTypeField(), password)).name,
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeIdField(), password),
    }

def dump_ExcelDB_EventContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficultyField(), password)).name,
        "StageNumber": convert_string(excel_instance.StageNumberField(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplayField(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageIdField(), password),
        "OpenDate": convert_int(excel_instance.OpenDateField(), password),
        "OpenEventPoint": convert_int(excel_instance.OpenEventPointField(), password),
        "OpenConditionScenarioPermanentSubEventId": convert_int(excel_instance.OpenConditionScenarioPermanentSubEventIdField(), password),
        "PrevStageSubEventId": convert_int(excel_instance.PrevStageSubEventIdField(), password),
        "OpenConditionScenarioId": convert_int(excel_instance.OpenConditionScenarioIdField(), password),
        "OpenConditionContentType": EventContentType(convert_int(excel_instance.OpenConditionContentTypeField(), password)).name,
        "OpenConditionContentId": convert_int(excel_instance.OpenConditionContentIdField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostTypeField(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostIdField(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmountField(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCountField(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCountField(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCountField(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupIdField(j), password) for j in range(excel_instance.EnterScenarioGroupIdFieldLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupIdField(j), password) for j in range(excel_instance.ClearScenarioGroupIdFieldLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMapField(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBGField(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardIdField(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurnField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "BgmId": convert_int(excel_instance.BgmIdField(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironmentField(), password)).name,
        "GroundID": convert_int(excel_instance.GroundIDField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "InstantClear": bool(excel_instance.InstantClearField()),
        "BuffContentId": convert_int(excel_instance.BuffContentIdField(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "ChallengeDisplay": bool(excel_instance.ChallengeDisplayField()),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoalField(j), password)).name for j in range(excel_instance.StarGoalFieldLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmountField(j), password) for j in range(excel_instance.StarGoalAmountFieldLength())],
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattleField()),
        "StageHint": convert_uint(excel_instance.StageHintField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_EventContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "RewardProb": convert_int(excel_instance.RewardProbField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_ExcelDB_EventContentStageTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "RequiredEventItemAmount": convert_int(excel_instance.RequiredEventItemAmountField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentTreasureCellRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeIDField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EventContentTreasureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "TitleLocalize": convert_string(excel_instance.TitleLocalizeField(), password),
        "LoopRound": convert_int(excel_instance.LoopRoundField(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabNameField(), password),
        "TreasureBGImagePath": convert_string(excel_instance.TreasureBGImagePathField(), password),
    }

def dump_ExcelDB_EventContentTreasureRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeIDField(), password),
        "CellUnderImageWidth": convert_int(excel_instance.CellUnderImageWidthField(), password),
        "CellUnderImageHeight": convert_int(excel_instance.CellUnderImageHeightField(), password),
        "HiddenImage": bool(excel_instance.HiddenImageField()),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
        "CellUnderImagePath": convert_string(excel_instance.CellUnderImagePathField(), password),
        "TreasureSmallImagePath": convert_string(excel_instance.TreasureSmallImagePathField(), password),
        "TreasureSizeIconPath": convert_string(excel_instance.TreasureSizeIconPathField(), password),
    }

def dump_ExcelDB_EventContentTreasureRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "TreasureRound": convert_int(excel_instance.TreasureRoundField(), password),
        "TreasureRoundSize": [convert_int(excel_instance.TreasureRoundSizeField(j), password) for j in range(excel_instance.TreasureRoundSizeFieldLength())],
        "CellVisualSortUnstructed": bool(excel_instance.CellVisualSortUnstructedField()),
        "CellCheckGoodsId": convert_int(excel_instance.CellCheckGoodsIdField(), password),
        "CellRewardId": convert_int(excel_instance.CellRewardIdField(), password),
        "RewardID": [convert_int(excel_instance.RewardIDField(j), password) for j in range(excel_instance.RewardIDFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
        "TreasureCellImagePath": convert_string(excel_instance.TreasureCellImagePathField(), password),
    }

def dump_ExcelDB_EventContentZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "OriginalZoneId": convert_int(excel_instance.OriginalZoneIdField(), password),
        "LocationId": convert_int(excel_instance.LocationIdField(), password),
        "LocationRank": convert_int(excel_instance.LocationRankField(), password),
        "EventPointForLocationRank": convert_int(excel_instance.EventPointForLocationRankField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "StudentVisitProb": [convert_int(excel_instance.StudentVisitProbField(j), password) for j in range(excel_instance.StudentVisitProbFieldLength())],
        "RewardGroupId": convert_int(excel_instance.RewardGroupIdField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
        "WhiteListTags": [Tag(convert_int(excel_instance.WhiteListTagsField(j), password)).name for j in range(excel_instance.WhiteListTagsFieldLength())],
    }

def dump_ExcelDB_EventContentZoneVisitRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentLocationId": convert_int(excel_instance.EventContentLocationIdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "CharacterDevName": convert_string(excel_instance.CharacterDevNameField(), password),
        "VisitRewardParcelType": [ParcelType(convert_int(excel_instance.VisitRewardParcelTypeField(j), password)).name for j in range(excel_instance.VisitRewardParcelTypeFieldLength())],
        "VisitRewardParcelId": [convert_int(excel_instance.VisitRewardParcelIdField(j), password) for j in range(excel_instance.VisitRewardParcelIdFieldLength())],
        "VisitRewardAmount": [convert_int(excel_instance.VisitRewardAmountField(j), password) for j in range(excel_instance.VisitRewardAmountFieldLength())],
        "VisitRewardProb": [convert_int(excel_instance.VisitRewardProbField(j), password) for j in range(excel_instance.VisitRewardProbFieldLength())],
    }

def dump_ExcelDB_FarmingDungeonLocationManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FarmingDungeonLocationId": convert_int(excel_instance.FarmingDungeonLocationIdField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "WeekDungeonType": convert_float(excel_instance.WeekDungeonTypeField(), password),
        "SchoolDungeonType": SchoolDungeonType(convert_int(excel_instance.SchoolDungeonTypeField(), password)).name,
        "Order": convert_int(excel_instance.OrderField(), password),
        "OpenStartDateTime": convert_string(excel_instance.OpenStartDateTimeField(), password),
        "OpenEndDateTime": convert_string(excel_instance.OpenEndDateTimeField(), password),
        "LocationButtonImagePath": convert_string(excel_instance.LocationButtonImagePathField(), password),
        "LocalizeCodeTitle": convert_uint(excel_instance.LocalizeCodeTitleField(), password),
        "LocalizeCodeInfo": convert_uint(excel_instance.LocalizeCodeInfoField(), password),
    }

def dump_ExcelDB_FavorLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "ExpType": [convert_int(excel_instance.ExpTypeField(j), password) for j in range(excel_instance.ExpTypeFieldLength())],
    }

def dump_ExcelDB_FavorLevelRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "FavorLevel": convert_int(excel_instance.FavorLevelField(), password),
        "StatType": [EquipmentOptionType(convert_int(excel_instance.StatTypeField(j), password)).name for j in range(excel_instance.StatTypeFieldLength())],
        "StatValue": [convert_int(excel_instance.StatValueField(j), password) for j in range(excel_instance.StatValueFieldLength())],
    }

def dump_ExcelDB_FieldQuestGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SkipFromInteractionId": convert_int(excel_instance.SkipFromInteractionIdField(), password),
        "SkipToInteractionId": convert_int(excel_instance.SkipToInteractionIdField(), password),
        "NextSceneId": convert_int(excel_instance.NextSceneIdField(), password),
        "SkipResultUI": bool(excel_instance.SkipResultUIField()),
    }

def dump_ExcelDB_FieldSNSInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "InteractionGroupId": convert_int(excel_instance.InteractionGroupIdField(), password),
        "SNSStateType": FieldSNSStateType(convert_int(excel_instance.SNSStateTypeField(), password)).name,
        "StateLocalizeKey": convert_uint(excel_instance.StateLocalizeKeyField(), password),
        "DescLocalizeKey": convert_uint(excel_instance.DescLocalizeKeyField(), password),
    }

def dump_ExcelDB_FieldSNSPostExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupInteractionId": convert_int(excel_instance.GroupInteractionIdField(), password),
        "PostType": FieldSNSPostType(convert_int(excel_instance.PostTypeField(), password)).name,
        "SNSPostId": convert_int(excel_instance.SNSPostIdField(), password),
        "IsSequence": bool(excel_instance.IsSequenceField()),
        "Order": convert_int(excel_instance.OrderField(), password),
        "DelayTime": convert_int(excel_instance.DelayTimeField(), password),
        "RepostMinNum": convert_int(excel_instance.RepostMinNumField(), password),
        "RepostMaxNum": convert_int(excel_instance.RepostMaxNumField(), password),
        "FavorMinNum": convert_int(excel_instance.FavorMinNumField(), password),
        "FavorMaxNum": convert_int(excel_instance.FavorMaxNumField(), password),
    }

def dump_ExcelDB_FieldWarpExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "CurrentSceneId": convert_int(excel_instance.CurrentSceneIdField(), password),
        "ResultSceneId": convert_int(excel_instance.ResultSceneIdField(), password),
        "ResultSceneNameKey": convert_uint(excel_instance.ResultSceneNameKeyField(), password),
        "ResultSceneImagePath": convert_string(excel_instance.ResultSceneImagePathField(), password),
    }

def dump_ExcelDB_FixedEchelonSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FixedEchelonID": convert_int(excel_instance.FixedEchelonIDField(), password),
        "EchelonSceneSkip": bool(excel_instance.EchelonSceneSkipField()),
        "MainLeaderSlot": convert_int(excel_instance.MainLeaderSlotField(), password),
        "MainCharacterID": [convert_int(excel_instance.MainCharacterIDField(j), password) for j in range(excel_instance.MainCharacterIDFieldLength())],
        "MainLevel": [convert_int(excel_instance.MainLevelField(j), password) for j in range(excel_instance.MainLevelFieldLength())],
        "MainGrade": [convert_int(excel_instance.MainGradeField(j), password) for j in range(excel_instance.MainGradeFieldLength())],
        "MainExSkillLevel": [convert_int(excel_instance.MainExSkillLevelField(j), password) for j in range(excel_instance.MainExSkillLevelFieldLength())],
        "MainNoneExSkillLevel": [convert_int(excel_instance.MainNoneExSkillLevelField(j), password) for j in range(excel_instance.MainNoneExSkillLevelFieldLength())],
        "MainEquipment1Tier": [convert_int(excel_instance.MainEquipment1TierField(j), password) for j in range(excel_instance.MainEquipment1TierFieldLength())],
        "MainEquipment1Level": [convert_int(excel_instance.MainEquipment1LevelField(j), password) for j in range(excel_instance.MainEquipment1LevelFieldLength())],
        "MainEquipment2Tier": [convert_int(excel_instance.MainEquipment2TierField(j), password) for j in range(excel_instance.MainEquipment2TierFieldLength())],
        "MainEquipment2Level": [convert_int(excel_instance.MainEquipment2LevelField(j), password) for j in range(excel_instance.MainEquipment2LevelFieldLength())],
        "MainEquipment3Tier": [convert_int(excel_instance.MainEquipment3TierField(j), password) for j in range(excel_instance.MainEquipment3TierFieldLength())],
        "MainEquipment3Level": [convert_int(excel_instance.MainEquipment3LevelField(j), password) for j in range(excel_instance.MainEquipment3LevelFieldLength())],
        "MainCharacterWeaponGrade": [convert_int(excel_instance.MainCharacterWeaponGradeField(j), password) for j in range(excel_instance.MainCharacterWeaponGradeFieldLength())],
        "MainCharacterWeaponLevel": [convert_int(excel_instance.MainCharacterWeaponLevelField(j), password) for j in range(excel_instance.MainCharacterWeaponLevelFieldLength())],
        "MainCharacterGearTier": [convert_int(excel_instance.MainCharacterGearTierField(j), password) for j in range(excel_instance.MainCharacterGearTierFieldLength())],
        "MainCharacterGearLevel": [convert_int(excel_instance.MainCharacterGearLevelField(j), password) for j in range(excel_instance.MainCharacterGearLevelFieldLength())],
        "SupportCharacterID": [convert_int(excel_instance.SupportCharacterIDField(j), password) for j in range(excel_instance.SupportCharacterIDFieldLength())],
        "SupportLevel": [convert_int(excel_instance.SupportLevelField(j), password) for j in range(excel_instance.SupportLevelFieldLength())],
        "SupportGrade": [convert_int(excel_instance.SupportGradeField(j), password) for j in range(excel_instance.SupportGradeFieldLength())],
        "SupportExSkillLevel": [convert_int(excel_instance.SupportExSkillLevelField(j), password) for j in range(excel_instance.SupportExSkillLevelFieldLength())],
        "SupportNoneExSkillLevel": [convert_int(excel_instance.SupportNoneExSkillLevelField(j), password) for j in range(excel_instance.SupportNoneExSkillLevelFieldLength())],
        "SupportEquipment1Tier": [convert_int(excel_instance.SupportEquipment1TierField(j), password) for j in range(excel_instance.SupportEquipment1TierFieldLength())],
        "SupportEquipment1Level": [convert_int(excel_instance.SupportEquipment1LevelField(j), password) for j in range(excel_instance.SupportEquipment1LevelFieldLength())],
        "SupportEquipment2Tier": [convert_int(excel_instance.SupportEquipment2TierField(j), password) for j in range(excel_instance.SupportEquipment2TierFieldLength())],
        "SupportEquipment2Level": [convert_int(excel_instance.SupportEquipment2LevelField(j), password) for j in range(excel_instance.SupportEquipment2LevelFieldLength())],
        "SupportEquipment3Tier": [convert_int(excel_instance.SupportEquipment3TierField(j), password) for j in range(excel_instance.SupportEquipment3TierFieldLength())],
        "SupportEquipment3Level": [convert_int(excel_instance.SupportEquipment3LevelField(j), password) for j in range(excel_instance.SupportEquipment3LevelFieldLength())],
        "SupportCharacterWeaponGrade": [convert_int(excel_instance.SupportCharacterWeaponGradeField(j), password) for j in range(excel_instance.SupportCharacterWeaponGradeFieldLength())],
        "SupportCharacterWeaponLevel": [convert_int(excel_instance.SupportCharacterWeaponLevelField(j), password) for j in range(excel_instance.SupportCharacterWeaponLevelFieldLength())],
        "SupportCharacterGearTier": [convert_int(excel_instance.SupportCharacterGearTierField(j), password) for j in range(excel_instance.SupportCharacterGearTierFieldLength())],
        "SupportCharacterGearLevel": [convert_int(excel_instance.SupportCharacterGearLevelField(j), password) for j in range(excel_instance.SupportCharacterGearLevelFieldLength())],
        "InteractionTSCharacterId": convert_int(excel_instance.InteractionTSCharacterIdField(), password),
    }

def dump_ExcelDB_FixedStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "StageEnterEchelon01FixedEchelonId": convert_int(excel_instance.StageEnterEchelon01FixedEchelonIdField(), password),
        "StageEnterEchelon01Starttile": convert_int(excel_instance.StageEnterEchelon01StarttileField(), password),
        "StageEnterEchelon02FixedEchelonId": convert_int(excel_instance.StageEnterEchelon02FixedEchelonIdField(), password),
        "StageEnterEchelon02Starttile": convert_int(excel_instance.StageEnterEchelon02StarttileField(), password),
        "StageEnterEchelon03FixedEchelonId": convert_int(excel_instance.StageEnterEchelon03FixedEchelonIdField(), password),
        "StageEnterEchelon03Starttile": convert_int(excel_instance.StageEnterEchelon03StarttileField(), password),
        "StageEnterEchelon04FixedEchelonId": convert_int(excel_instance.StageEnterEchelon04FixedEchelonIdField(), password),
        "StageEnterEchelon04Starttile": convert_int(excel_instance.StageEnterEchelon04StarttileField(), password),
    }

def dump_ExcelDB_FloaterCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityTypeField(), password)).name,
        "FloaterOffsetPosX": convert_int(excel_instance.FloaterOffsetPosXField(), password),
        "FloaterOffsetPosY": convert_int(excel_instance.FloaterOffsetPosYField(), password),
        "FloaterRandomPosRangeX": convert_int(excel_instance.FloaterRandomPosRangeXField(), password),
        "FloaterRandomPosRangeY": convert_int(excel_instance.FloaterRandomPosRangeYField(), password),
    }

def dump_ExcelDB_FormationLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupID": convert_int(excel_instance.GroupIDField(), password),
        "SlotZ": [convert_float(excel_instance.SlotZField(j), password) for j in range(excel_instance.SlotZFieldLength())],
        "SlotX": [convert_float(excel_instance.SlotXField(j), password) for j in range(excel_instance.SlotXFieldLength())],
    }

def dump_ExcelDB_FurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "Category": FurnitureCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "SubCategory": FurnitureSubCategory(convert_int(excel_instance.SubCategoryField(), password)).name,
        "CheckFloorDecoration": bool(excel_instance.CheckFloorDecorationField()),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "StarGradeInit": convert_int(excel_instance.StarGradeInitField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
        "SizeWidth": convert_int(excel_instance.SizeWidthField(), password),
        "SizeHeight": convert_int(excel_instance.SizeHeightField(), password),
        "OtherSize": convert_int(excel_instance.OtherSizeField(), password),
        "ExpandWidth": convert_int(excel_instance.ExpandWidthField(), password),
        "Enable": bool(excel_instance.EnableField()),
        "ReverseRotation": bool(excel_instance.ReverseRotationField()),
        "Prefab": convert_string(excel_instance.PrefabField(), password),
        "PrefabExpand": convert_string(excel_instance.PrefabExpandField(), password),
        "SubPrefab": convert_string(excel_instance.SubPrefabField(), password),
        "SubExpandPrefab": convert_string(excel_instance.SubExpandPrefabField(), password),
        "CornerPrefab": convert_string(excel_instance.CornerPrefabField(), password),
        "StackableMax": convert_int(excel_instance.StackableMaxField(), password),
        "RecipeCraftId": convert_int(excel_instance.RecipeCraftIdField(), password),
        "SetGroudpId": convert_int(excel_instance.SetGroudpIdField(), password),
        "ComfortBonus": convert_int(excel_instance.ComfortBonusField(), password),
        "VisitOperationType": convert_int(excel_instance.VisitOperationTypeField(), password),
        "VisitBonusOperationType": convert_int(excel_instance.VisitBonusOperationTypeField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0Field(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1Field(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2Field(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQualityField(), password),
        "FurnitureFunctionType": FurnitureFunctionType(convert_int(excel_instance.FurnitureFunctionTypeField(), password)).name,
        "FurnitureFunctionParameter": [convert_int(excel_instance.FurnitureFunctionParameterField(j), password) for j in range(excel_instance.FurnitureFunctionParameterFieldLength())],
        "VideoId": convert_int(excel_instance.VideoIdField(), password),
        "EventCollectionId": convert_int(excel_instance.EventCollectionIdField(), password),
        "FurnitureBubbleOffsetX": convert_int(excel_instance.FurnitureBubbleOffsetXField(), password),
        "FurnitureBubbleOffsetY": convert_int(excel_instance.FurnitureBubbleOffsetYField(), password),
        "CafeCharacterStateReq": [convert_string(excel_instance.CafeCharacterStateReqField(j), password) for j in range(excel_instance.CafeCharacterStateReqFieldLength())],
        "CafeCharacterStateAdd": [convert_string(excel_instance.CafeCharacterStateAddField(j), password) for j in range(excel_instance.CafeCharacterStateAddFieldLength())],
        "CafeCharacterStateMake": [convert_string(excel_instance.CafeCharacterStateMakeField(j), password) for j in range(excel_instance.CafeCharacterStateMakeFieldLength())],
        "CafeCharacterStateOnly": [convert_string(excel_instance.CafeCharacterStateOnlyField(j), password) for j in range(excel_instance.CafeCharacterStateOnlyFieldLength())],
        "HideCraftShortcut": bool(excel_instance.HideCraftShortcutField()),
    }

def dump_ExcelDB_FurnitureGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupNameLocalize": convert_uint(excel_instance.GroupNameLocalizeField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "RequiredFurnitureCount": [convert_int(excel_instance.RequiredFurnitureCountField(j), password) for j in range(excel_instance.RequiredFurnitureCountFieldLength())],
        "ComfortBonus": [convert_int(excel_instance.ComfortBonusField(j), password) for j in range(excel_instance.ComfortBonusFieldLength())],
    }

def dump_ExcelDB_FurnitureTemplateElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_int(excel_instance.FurnitureTemplateIdField(), password),
        "FurnitureId": convert_int(excel_instance.FurnitureIdField(), password),
        "Location": FurnitureLocation(convert_int(excel_instance.LocationField(), password)).name,
        "PositionX": convert_float(excel_instance.PositionXField(), password),
        "PositionY": convert_float(excel_instance.PositionYField(), password),
        "Rotation": convert_float(excel_instance.RotationField(), password),
        "Order": convert_int(excel_instance.OrderField(), password),
    }

def dump_ExcelDB_FurnitureTemplateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_int(excel_instance.FurnitureTemplateIdField(), password),
        "FunitureTemplateTitle": convert_uint(excel_instance.FunitureTemplateTitleField(), password),
        "ThumbnailImagePath": convert_string(excel_instance.ThumbnailImagePathField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
    }

def dump_ExcelDB_GachaCombinedCostExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "Priority": convert_int(excel_instance.PriorityField(), password),
        "ConsumeGachaTicketType": GachaTicketType(convert_int(excel_instance.ConsumeGachaTicketTypeField(), password)).name,
        "ConsumeGachaTicketTypeAmount": convert_int(excel_instance.ConsumeGachaTicketTypeAmountField(), password),
        "ConsumeParcelType": ParcelType(convert_int(excel_instance.ConsumeParcelTypeField(), password)).name,
        "ConsumeParcelId": convert_int(excel_instance.ConsumeParcelIdField(), password),
        "ConsumeParcelAmount": convert_int(excel_instance.ConsumeParcelAmountField(), password),
    }

def dump_ExcelDB_GachaCraftNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "QuickCraftNodeDisplayOrder": convert_int(excel_instance.QuickCraftNodeDisplayOrderField(), password),
        "NodeQuality": convert_int(excel_instance.NodeQualityField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
        "LocalizeKey": convert_uint(excel_instance.LocalizeKeyField(), password),
        "Property": convert_int(excel_instance.PropertyField(), password),
    }

def dump_ExcelDB_GachaCraftNodeGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NodeId": convert_int(excel_instance.NodeIdField(), password),
        "GachaGroupId": convert_int(excel_instance.GachaGroupIdField(), password),
        "ProbWeight": convert_int(excel_instance.ProbWeightField(), password),
    }

def dump_ExcelDB_GachaCraftOpenTagExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NodeTier": convert_int(excel_instance.NodeTierField(), password),
        "Tag": [Tag(convert_int(excel_instance.TagField(j), password)).name for j in range(excel_instance.TagFieldLength())],
    }

def dump_ExcelDB_GachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupIDField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelID": convert_int(excel_instance.ParcelIDField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMinField(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMaxField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "State": convert_int(excel_instance.StateField(), password),
    }

def dump_ExcelDB_GachaElementRecursiveExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupIDField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelID": convert_int(excel_instance.ParcelIDField(), password),
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMinField(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMaxField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "State": convert_int(excel_instance.StateField(), password),
    }

def dump_ExcelDB_GachaGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "NameKr": convert_string(excel_instance.NameKrField(), password),
        "IsRecursive": bool(excel_instance.IsRecursiveField()),
        "GroupType": GachaGroupType(convert_int(excel_instance.GroupTypeField(), password)).name,
    }

def dump_ExcelDB_GachaSelectPickupGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GachaGroupId": convert_int(excel_instance.GachaGroupIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
    }

def dump_ExcelDB_GoodsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Type": convert_int(excel_instance.TypeField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "ConsumeParcelType": [ParcelType(convert_int(excel_instance.ConsumeParcelTypeField(j), password)).name for j in range(excel_instance.ConsumeParcelTypeFieldLength())],
        "ConsumeParcelId": [convert_int(excel_instance.ConsumeParcelIdField(j), password) for j in range(excel_instance.ConsumeParcelIdFieldLength())],
        "ConsumeParcelAmount": [convert_int(excel_instance.ConsumeParcelAmountField(j), password) for j in range(excel_instance.ConsumeParcelAmountFieldLength())],
        "ConsumeCondition": [ConsumeCondition(convert_int(excel_instance.ConsumeConditionField(j), password)).name for j in range(excel_instance.ConsumeConditionFieldLength())],
        "ConsumeGachaTicketType": [GachaTicketType(convert_int(excel_instance.ConsumeGachaTicketTypeField(j), password)).name for j in range(excel_instance.ConsumeGachaTicketTypeFieldLength())],
        "ConsumeGachaTicketTypeAmount": [convert_int(excel_instance.ConsumeGachaTicketTypeAmountField(j), password) for j in range(excel_instance.ConsumeGachaTicketTypeAmountFieldLength())],
        "CombinedGachaCostId": convert_int(excel_instance.CombinedGachaCostIdField(), password),
        "ProductIdAOS": convert_int(excel_instance.ProductIdAOSField(), password),
        "ProductIdiOS": convert_int(excel_instance.ProductIdiOSField(), password),
        "ProductIdONE": convert_int(excel_instance.ProductIdONEField(), password),
        "ProductIdSGS": convert_int(excel_instance.ProductIdSGSField(), password),
        "ProductIdSTEAM": convert_int(excel_instance.ProductIdSTEAMField(), password),
        "ConsumeExtraStep": [convert_int(excel_instance.ConsumeExtraStepField(j), password) for j in range(excel_instance.ConsumeExtraStepFieldLength())],
        "ConsumeExtraAmount": [convert_int(excel_instance.ConsumeExtraAmountField(j), password) for j in range(excel_instance.ConsumeExtraAmountFieldLength())],
        "State": convert_int(excel_instance.StateField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
    }

def dump_ExcelDB_GooglePlayAchievementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ConditionType": ConditionType(convert_int(excel_instance.ConditionTypeField(), password)).name,
        "ConditionValue": convert_int(excel_instance.ConditionValueField(), password),
        "GooglePlayId": convert_string(excel_instance.GooglePlayIdField(), password),
        "AchievementType": AchievementType(convert_int(excel_instance.AchievementTypeField(), password)).name,
    }

def dump_ExcelDB_GroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "StageFileName": [convert_string(excel_instance.StageFileNameField(j), password) for j in range(excel_instance.StageFileNameFieldLength())],
        "GroundSceneName": convert_string(excel_instance.GroundSceneNameField(), password),
        "FormationGroupId": convert_int(excel_instance.FormationGroupIdField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "EnemyBulletType": BulletType(convert_int(excel_instance.EnemyBulletTypeField(), password)).name,
        "EnemyArmorType": ArmorType(convert_int(excel_instance.EnemyArmorTypeField(), password)).name,
        "EnemySubArmorType": ArmorType(convert_int(excel_instance.EnemySubArmorTypeField(), password)).name,
        "LevelNPC": convert_int(excel_instance.LevelNPCField(), password),
        "LevelMinion": convert_int(excel_instance.LevelMinionField(), password),
        "LevelElite": convert_int(excel_instance.LevelEliteField(), password),
        "LevelChampion": convert_int(excel_instance.LevelChampionField(), password),
        "LevelBoss": convert_int(excel_instance.LevelBossField(), password),
        "ObstacleLevel": convert_int(excel_instance.ObstacleLevelField(), password),
        "GradeNPC": convert_int(excel_instance.GradeNPCField(), password),
        "GradeMinion": convert_int(excel_instance.GradeMinionField(), password),
        "GradeElite": convert_int(excel_instance.GradeEliteField(), password),
        "GradeChampion": convert_int(excel_instance.GradeChampionField(), password),
        "GradeBoss": convert_int(excel_instance.GradeBossField(), password),
        "PlayerSightPointAdd": convert_int(excel_instance.PlayerSightPointAddField(), password),
        "PlayerSightPointRate": convert_int(excel_instance.PlayerSightPointRateField(), password),
        "PlayerAttackRangeAdd": convert_int(excel_instance.PlayerAttackRangeAddField(), password),
        "PlayerAttackRangeRate": convert_int(excel_instance.PlayerAttackRangeRateField(), password),
        "EnemySightPointAdd": convert_int(excel_instance.EnemySightPointAddField(), password),
        "EnemySightPointRate": convert_int(excel_instance.EnemySightPointRateField(), password),
        "EnemyAttackRangeAdd": convert_int(excel_instance.EnemyAttackRangeAddField(), password),
        "EnemyAttackRangeRate": convert_int(excel_instance.EnemyAttackRangeRateField(), password),
        "PlayerSkillRangeAdd": convert_int(excel_instance.PlayerSkillRangeAddField(), password),
        "PlayerSkillRangeRate": convert_int(excel_instance.PlayerSkillRangeRateField(), password),
        "EnemySkillRangeAdd": convert_int(excel_instance.EnemySkillRangeAddField(), password),
        "EnemySkillRangeRate": convert_int(excel_instance.EnemySkillRangeRateField(), password),
        "PlayerMinimumPositionGapRate": convert_int(excel_instance.PlayerMinimumPositionGapRateField(), password),
        "EnemyMinimumPositionGapRate": convert_int(excel_instance.EnemyMinimumPositionGapRateField(), password),
        "PlayerSightRangeMax": bool(excel_instance.PlayerSightRangeMaxField()),
        "EnemySightRangeMax": bool(excel_instance.EnemySightRangeMaxField()),
        "TSSAirUnitHeight": convert_int(excel_instance.TSSAirUnitHeightField(), password),
        "IsPhaseBGM": bool(excel_instance.IsPhaseBGMField()),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "WarningUI": bool(excel_instance.WarningUIField()),
        "TSSHatchOpen": bool(excel_instance.TSSHatchOpenField()),
        "ForcedTacticSpeed": TacticSpeed(convert_int(excel_instance.ForcedTacticSpeedField(), password)).name,
        "ForcedSkillUse": TacticSkillUse(convert_int(excel_instance.ForcedSkillUseField(), password)).name,
        "ShowNPCSkillCutIn": ShowSkillCutIn(convert_int(excel_instance.ShowNPCSkillCutInField(), password)).name,
        "ImmuneHitBeforeTimeOutEnd": bool(excel_instance.ImmuneHitBeforeTimeOutEndField()),
        "UIBattleHideFromScratch": bool(excel_instance.UIBattleHideFromScratchField()),
        "UIEnemyCount": UIEnemyCountType(convert_int(excel_instance.UIEnemyCountField(), password)).name,
        "BattleReadyTimelinePath": convert_string(excel_instance.BattleReadyTimelinePathField(), password),
        "BeforeVictoryTimelinePath": convert_string(excel_instance.BeforeVictoryTimelinePathField(), password),
        "SkipBattleEnd": bool(excel_instance.SkipBattleEndField()),
        "HideNPCWhenBattleEnd": bool(excel_instance.HideNPCWhenBattleEndField()),
        "CoverPointOff": bool(excel_instance.CoverPointOffField()),
        "UIHpScale": convert_float(excel_instance.UIHpScaleField(), password),
        "UIEmojiScale": convert_float(excel_instance.UIEmojiScaleField(), password),
        "UISkillMainLogScale": convert_float(excel_instance.UISkillMainLogScaleField(), password),
        "EffectCountLimit": convert_int(excel_instance.EffectCountLimitField(), password),
        "CarrierSkillGroupId": convert_int(excel_instance.CarrierSkillGroupIdField(), password),
        "AllyPassiveSkillId": [convert_string(excel_instance.AllyPassiveSkillIdField(j), password) for j in range(excel_instance.AllyPassiveSkillIdFieldLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevelField(j), password) for j in range(excel_instance.AllyPassiveSkillLevelFieldLength())],
        "EnemyPassiveSkillId": [convert_string(excel_instance.EnemyPassiveSkillIdField(j), password) for j in range(excel_instance.EnemyPassiveSkillIdFieldLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevelField(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelFieldLength())],
    }

def dump_ExcelDB_GroundModuleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_uint(excel_instance.GroupIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbabilityField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPathField(), password),
    }

def dump_ExcelDB_GrowthScoreCalculationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "IncludeGrowthFactor": GrowthFactor(convert_int(excel_instance.IncludeGrowthFactorField(), password)).name,
        "ConversionCoefficient": convert_int(excel_instance.ConversionCoefficientField(), password),
    }

def dump_ExcelDB_GuideMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "Category": MissionCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "TabNumber": convert_int(excel_instance.TabNumberField(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionIdField(j), password) for j in range(excel_instance.PreMissionIdFieldLength())],
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayTypeField(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePathField(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUIField(j), password) for j in range(excel_instance.ShortcutUIFieldLength())],
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionTypeField(), password)).name,
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCountField(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameterField(j), password) for j in range(excel_instance.CompleteConditionParameterFieldLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTagField(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagFieldLength())],
        "IsAutoClearForScenario": bool(excel_instance.IsAutoClearForScenarioField()),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelTypeField(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeFieldLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelIdField(j), password) for j in range(excel_instance.MissionRewardParcelIdFieldLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmountField(j), password) for j in range(excel_instance.MissionRewardAmountFieldLength())],
    }

def dump_ExcelDB_GuideMissionOpenStageConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "OrderNumber": convert_int(excel_instance.OrderNumberField(), password),
        "TabLocalizeCode": convert_string(excel_instance.TabLocalizeCodeField(), password),
        "ClearScenarioModeId": convert_int(excel_instance.ClearScenarioModeIdField(), password),
        "LockScenarioTextLocailzeCode": convert_string(excel_instance.LockScenarioTextLocailzeCodeField(), password),
        "ShortcutScenarioUI": convert_string(excel_instance.ShortcutScenarioUIField(), password),
        "ClearStageId": convert_int(excel_instance.ClearStageIdField(), password),
        "LockStageTextLocailzeCode": convert_string(excel_instance.LockStageTextLocailzeCodeField(), password),
        "ShortcutStageUI": convert_string(excel_instance.ShortcutStageUIField(), password),
    }

def dump_ExcelDB_GuideMissionSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TitleLocalizeCode": convert_string(excel_instance.TitleLocalizeCodeField(), password),
        "PermanentInfomationLocalizeCode": convert_string(excel_instance.PermanentInfomationLocalizeCodeField(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCodeField(), password),
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "Enabled": bool(excel_instance.EnabledField()),
        "BannerOpenDate": convert_string(excel_instance.BannerOpenDateField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "CloseBannerAfterCompletion": bool(excel_instance.CloseBannerAfterCompletionField()),
        "MaximumLoginCount": convert_int(excel_instance.MaximumLoginCountField(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDateField(), password),
        "IconOrder": convert_int(excel_instance.IconOrderField(), password),
        "SpineCharacterId": convert_int(excel_instance.SpineCharacterIdField(), password),
        "RequirementParcelImage": convert_string(excel_instance.RequirementParcelImageField(), password),
        "RewardImage": convert_string(excel_instance.RewardImageField(), password),
        "LobbyBannerImage": convert_string(excel_instance.LobbyBannerImageField(), password),
        "BackgroundImage": convert_string(excel_instance.BackgroundImageField(), password),
        "TitleImage": convert_string(excel_instance.TitleImageField(), password),
        "RequirementParcelType": ParcelType(convert_int(excel_instance.RequirementParcelTypeField(), password)).name,
        "RequirementParcelId": convert_int(excel_instance.RequirementParcelIdField(), password),
        "RequirementParcelAmount": convert_int(excel_instance.RequirementParcelAmountField(), password),
        "TabType": GuideMissionTabType(convert_int(excel_instance.TabTypeField(), password)).name,
        "IsPermanent": bool(excel_instance.IsPermanentField()),
        "PreSeasonId": convert_int(excel_instance.PreSeasonIdField(), password),
    }

def dump_ExcelDB_HpBarAbbreviationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MonsterLv": convert_int(excel_instance.MonsterLvField(), password),
        "StandardHpBar": convert_int(excel_instance.StandardHpBarField(), password),
        "RaidBossHpBar": convert_int(excel_instance.RaidBossHpBarField(), password),
    }

def dump_ExcelDB_IAWorldRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfoField()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProbField(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelTypeField(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueIDField(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueNameField(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmountField(), password),
    }

def dump_ExcelDB_IdCardBackgroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "IsDefault": bool(excel_instance.IsDefaultField()),
        "BgPath": convert_string(excel_instance.BgPathField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
    }

def dump_ExcelDB_InformationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupID": convert_int(excel_instance.GroupIDField(), password),
        "PageName": convert_string(excel_instance.PageNameField(), password),
        "IsPcBuild": bool(excel_instance.IsPcBuildField()),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeIdField(), password),
        "TutorialParentName": [convert_string(excel_instance.TutorialParentNameField(j), password) for j in range(excel_instance.TutorialParentNameFieldLength())],
        "UIName": [convert_string(excel_instance.UINameField(j), password) for j in range(excel_instance.UINameFieldLength())],
    }

def dump_ExcelDB_InformationStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "StageId": convert_int(excel_instance.StageIdField(), password),
        "PageName": convert_string(excel_instance.PageNameField(), password),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeIdField(), password),
    }

def dump_ExcelDB_InteractiveWorldRaidArcadeMachineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "MiniGameType": [EventContentType(convert_int(excel_instance.MiniGameTypeField(j), password)).name for j in range(excel_instance.MiniGameTypeFieldLength())],
        "MiniGameCostItemId": [convert_int(excel_instance.MiniGameCostItemIdField(j), password) for j in range(excel_instance.MiniGameCostItemIdFieldLength())],
        "MiniGameCostItemAmount": [convert_int(excel_instance.MiniGameCostItemAmountField(j), password) for j in range(excel_instance.MiniGameCostItemAmountFieldLength())],
        "MiniGameSoftLimitItemId": [convert_string(excel_instance.MiniGameSoftLimitItemIdField(j), password) for j in range(excel_instance.MiniGameSoftLimitItemIdFieldLength())],
        "MiniGameSoftLimitItemAmount": [convert_string(excel_instance.MiniGameSoftLimitItemAmountField(j), password) for j in range(excel_instance.MiniGameSoftLimitItemAmountFieldLength())],
        "MiniGameImage": [convert_string(excel_instance.MiniGameImageField(j), password) for j in range(excel_instance.MiniGameImageFieldLength())],
        "LocalizeTitle": [convert_uint(excel_instance.LocalizeTitleField(j), password) for j in range(excel_instance.LocalizeTitleFieldLength())],
        "LocalizeDesc": [convert_uint(excel_instance.LocalizeDescField(j), password) for j in range(excel_instance.LocalizeDescFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidBossGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupIdField(), password),
        "WorldBossHPLinkGroup": convert_int(excel_instance.WorldBossHPLinkGroupField(), password),
        "WorldBossName": convert_string(excel_instance.WorldBossNameField(), password),
        "WorldBossPopupPortrait": convert_string(excel_instance.WorldBossPopupPortraitField(), password),
        "WorldBossPopupNameTexture": convert_string(excel_instance.WorldBossPopupNameTextureField(), password),
        "WorldBossPopupBG": convert_string(excel_instance.WorldBossPopupBGField(), password),
        "WorldBossParcelPortrait": convert_string(excel_instance.WorldBossParcelPortraitField(), password),
        "WorldBossListParcel": convert_string(excel_instance.WorldBossListParcelField(), password),
        "WorldBossHP": convert_int(excel_instance.WorldBossHPField(), password),
        "WorldBossHPTw": convert_int(excel_instance.WorldBossHPTwField(), password),
        "WorldBossHPAsia": convert_int(excel_instance.WorldBossHPAsiaField(), password),
        "WorldBossHPNa": convert_int(excel_instance.WorldBossHPNaField(), password),
        "WorldBossHPGlobal": convert_int(excel_instance.WorldBossHPGlobalField(), password),
        "UIHideBeforeSpawn": bool(excel_instance.UIHideBeforeSpawnField()),
        "HideAnotherBossKilled": bool(excel_instance.HideAnotherBossKilledField()),
        "WorldBossClearRewardGroupId": convert_int(excel_instance.WorldBossClearRewardGroupIdField(), password),
        "AnotherBossKilled": [convert_int(excel_instance.AnotherBossKilledField(j), password) for j in range(excel_instance.AnotherBossKilledFieldLength())],
        "EchelonConstraintGroupId": convert_int(excel_instance.EchelonConstraintGroupIdField(), password),
        "ExclusiveOperatorBossSpawn": convert_string(excel_instance.ExclusiveOperatorBossSpawnField(), password),
        "ExclusiveOperatorBossKill": convert_string(excel_instance.ExclusiveOperatorBossKillField(), password),
        "ExclusiveOperatorScenarioBattle": convert_string(excel_instance.ExclusiveOperatorScenarioBattleField(), password),
        "ExclusiveOperatorBossDamaged": convert_string(excel_instance.ExclusiveOperatorBossDamagedField(), password),
        "BossGroupOpenCondition": convert_int(excel_instance.BossGroupOpenConditionField(), password),
        "RaidScenarioBattleLocalizeKey": convert_string(excel_instance.RaidScenarioBattleLocalizeKeyField(), password),
        "IsSeasonFinalBoss": bool(excel_instance.IsSeasonFinalBossField()),
    }

def dump_ExcelDB_InteractiveWorldRaidCarrierExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CarrierSkillListGroupId": convert_int(excel_instance.CarrierSkillListGroupIdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "CharacterLevel": convert_int(excel_instance.CharacterLevelField(), password),
        "CharacterGrade": convert_int(excel_instance.CharacterGradeField(), password),
        "ExSkillGroupId": [convert_string(excel_instance.ExSkillGroupIdField(j), password) for j in range(excel_instance.ExSkillGroupIdFieldLength())],
        "ExSkillCardTexture": [convert_string(excel_instance.ExSkillCardTextureField(j), password) for j in range(excel_instance.ExSkillCardTextureFieldLength())],
        "FixedExSkillLevel": [convert_int(excel_instance.FixedExSkillLevelField(j), password) for j in range(excel_instance.FixedExSkillLevelFieldLength())],
        "PassiveSkillGroupId": [convert_string(excel_instance.PassiveSkillGroupIdField(j), password) for j in range(excel_instance.PassiveSkillGroupIdFieldLength())],
        "PassiveSkillCardTexture": [convert_string(excel_instance.PassiveSkillCardTextureField(j), password) for j in range(excel_instance.PassiveSkillCardTextureFieldLength())],
        "FixedPassiveSkillLevel": [convert_int(excel_instance.FixedPassiveSkillLevelField(j), password) for j in range(excel_instance.FixedPassiveSkillLevelFieldLength())],
        "ExtraPassiveSkillGroupId": [convert_string(excel_instance.ExtraPassiveSkillGroupIdField(j), password) for j in range(excel_instance.ExtraPassiveSkillGroupIdFieldLength())],
        "ExtraPassiveSkillCardTexture": [convert_string(excel_instance.ExtraPassiveSkillCardTextureField(j), password) for j in range(excel_instance.ExtraPassiveSkillCardTextureFieldLength())],
        "FixedExtraPassiveSkillLevel": [convert_int(excel_instance.FixedExtraPassiveSkillLevelField(j), password) for j in range(excel_instance.FixedExtraPassiveSkillLevelFieldLength())],
        "HiddenPassiveSkillGroupId": [convert_string(excel_instance.HiddenPassiveSkillGroupIdField(j), password) for j in range(excel_instance.HiddenPassiveSkillGroupIdFieldLength())],
        "HiddenPassiveSkillCardTexture": [convert_string(excel_instance.HiddenPassiveSkillCardTextureField(j), password) for j in range(excel_instance.HiddenPassiveSkillCardTextureFieldLength())],
        "FixedHiddenPassiveSkillLevel": [convert_int(excel_instance.FixedHiddenPassiveSkillLevelField(j), password) for j in range(excel_instance.FixedHiddenPassiveSkillLevelFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidCarrierMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ConditionId": convert_int(excel_instance.ConditionIdField(), password),
        "WorldRaidSeasonId": convert_int(excel_instance.WorldRaidSeasonIdField(), password),
        "WorldRaidPhaseId": convert_int(excel_instance.WorldRaidPhaseIdField(), password),
        "ReplaySeasonGroupId": convert_int(excel_instance.ReplaySeasonGroupIdField(), password),
        "ReplaySeasonOriginalPhaseId": convert_int(excel_instance.ReplaySeasonOriginalPhaseIdField(), password),
        "RecentClearBossGroupId": convert_int(excel_instance.RecentClearBossGroupIdField(), password),
        "RecentClearEventStageId": convert_int(excel_instance.RecentClearEventStageIdField(), password),
        "ChangeTarget": WorldRaidMapType(convert_int(excel_instance.ChangeTargetField(), password)).name,
        "Priority": convert_int(excel_instance.PriorityField(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPathField(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPathField(), password),
        "BridgeBGM": convert_int(excel_instance.BridgeBGMField(), password),
        "HangarBGM": convert_int(excel_instance.HangarBGMField(), password),
        "LobbyBGM": convert_int(excel_instance.LobbyBGMField(), password),
        "WorldMapBGM": convert_int(excel_instance.WorldMapBGMField(), password),
        "InformationGroupIdWorldMap": convert_int(excel_instance.InformationGroupIdWorldMapField(), password),
        "InformationGroupIdUCPopup": convert_int(excel_instance.InformationGroupIdUCPopupField(), password),
        "InformationGroupIdBridge": convert_int(excel_instance.InformationGroupIdBridgeField(), password),
        "InformationGroupIdHangar": convert_int(excel_instance.InformationGroupIdHangarField(), password),
        "InformationGroupIdLobby": convert_int(excel_instance.InformationGroupIdLobbyField(), password),
    }

def dump_ExcelDB_InteractiveWorldRaidCarrierRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SkillId": convert_int(excel_instance.SkillIdField(), password),
        "SkillSlot": convert_string(excel_instance.SkillSlotField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "RecipeIngredientId": [convert_int(excel_instance.RecipeIngredientIdField(j), password) for j in range(excel_instance.RecipeIngredientIdFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "WorldRaidSeasonId": convert_int(excel_instance.WorldRaidSeasonIdField(), password),
        "WorldRaidPhaseId": convert_int(excel_instance.WorldRaidPhaseIdField(), password),
        "Priority": convert_int(excel_instance.PriorityField(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckTypeField(), password)).name,
        "MultipleConditionCheckParameter": convert_int(excel_instance.MultipleConditionCheckParameterField(), password),
        "ConditionType": [WorldRaidConditionType(convert_int(excel_instance.ConditionTypeField(j), password)).name for j in range(excel_instance.ConditionTypeFieldLength())],
        "ConditionValue": [convert_int(excel_instance.ConditionValueField(j), password) for j in range(excel_instance.ConditionValueFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "PhaseId": convert_int(excel_instance.PhaseIdField(), password),
        "PhaseStartCondition": convert_int(excel_instance.PhaseStartConditionField(), password),
        "IsReplaySeason": bool(excel_instance.IsReplaySeasonField()),
        "EnterTicket": CurrencyTypes(convert_int(excel_instance.EnterTicketField(), password)).name,
        "PhaseStartTime": convert_string(excel_instance.PhaseStartTimeField(), password),
        "PhaseEndTime": convert_string(excel_instance.PhaseEndTimeField(), password),
        "WorldRaidLobbyScene": convert_string(excel_instance.WorldRaidLobbySceneField(), password),
        "WorldRaidLobbyBanner": convert_string(excel_instance.WorldRaidLobbyBannerField(), password),
        "WorldRaidLobbyBG": convert_string(excel_instance.WorldRaidLobbyBGField(), password),
        "WorldRaidLobbyBannerShow": bool(excel_instance.WorldRaidLobbyBannerShowField()),
        "SeasonOpenCondition": convert_int(excel_instance.SeasonOpenConditionField(), password),
        "WorldRaidLobbyEnterScenario": convert_int(excel_instance.WorldRaidLobbyEnterScenarioField(), password),
        "CanPlayNotSeasonTime": bool(excel_instance.CanPlayNotSeasonTimeField()),
        "WorldRaidUniqueThemeLobbyUI": bool(excel_instance.WorldRaidUniqueThemeLobbyUIField()),
        "WorldRaidUniqueThemeName": convert_string(excel_instance.WorldRaidUniqueThemeNameField(), password),
        "CanWorldRaidGemEnter": bool(excel_instance.CanWorldRaidGemEnterField()),
        "HideWorldRaidTicketUI": bool(excel_instance.HideWorldRaidTicketUIField()),
        "HideWorldRaidBossCompleteRewardUI": bool(excel_instance.HideWorldRaidBossCompleteRewardUIField()),
        "UseWorldRaidCommonToast": bool(excel_instance.UseWorldRaidCommonToastField()),
        "OpenRaidBossGroupId": [convert_int(excel_instance.OpenRaidBossGroupIdField(j), password) for j in range(excel_instance.OpenRaidBossGroupIdFieldLength())],
        "BossSpawnTime": [convert_string(excel_instance.BossSpawnTimeField(j), password) for j in range(excel_instance.BossSpawnTimeFieldLength())],
        "EliminateTime": [convert_string(excel_instance.EliminateTimeField(j), password) for j in range(excel_instance.EliminateTimeFieldLength())],
        "ScenarioOutputConditionId": [convert_int(excel_instance.ScenarioOutputConditionIdField(j), password) for j in range(excel_instance.ScenarioOutputConditionIdFieldLength())],
        "ConditionScenarioGroupid": [convert_int(excel_instance.ConditionScenarioGroupidField(j), password) for j in range(excel_instance.ConditionScenarioGroupidFieldLength())],
        "CarrierSkillGroupId": convert_int(excel_instance.CarrierSkillGroupIdField(), password),
        "WorldRaidMapEnterOperator": convert_string(excel_instance.WorldRaidMapEnterOperatorField(), password),
        "UseFavorRankBuff": bool(excel_instance.UseFavorRankBuffField()),
    }

def dump_ExcelDB_InteractiveWorldRaidSkillDescriptionListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SkillParcelEchelonType": EchelonExtensionType(convert_int(excel_instance.SkillParcelEchelonTypeField(), password)).name,
        "GlobalSkillGroupId": [convert_string(excel_instance.GlobalSkillGroupIdField(j), password) for j in range(excel_instance.GlobalSkillGroupIdFieldLength())],
        "GlobalSkillRemoveCondition": [convert_int(excel_instance.GlobalSkillRemoveConditionField(j), password) for j in range(excel_instance.GlobalSkillRemoveConditionFieldLength())],
        "GlobalSkillShowSkillSlot": [SkillSlotShowType(convert_int(excel_instance.GlobalSkillShowSkillSlotField(j), password)).name for j in range(excel_instance.GlobalSkillShowSkillSlotFieldLength())],
        "GlobalSkillHighlightResource": [SkillSlotHighLightType(convert_int(excel_instance.GlobalSkillHighlightResourceField(j), password)).name for j in range(excel_instance.GlobalSkillHighlightResourceFieldLength())],
        "SkillGroupId": [convert_string(excel_instance.SkillGroupIdField(j), password) for j in range(excel_instance.SkillGroupIdFieldLength())],
        "ShowSkillSlot": [SkillSlotShowType(convert_int(excel_instance.ShowSkillSlotField(j), password)).name for j in range(excel_instance.ShowSkillSlotFieldLength())],
        "HighlightResource": [SkillSlotHighLightType(convert_int(excel_instance.HighlightResourceField(j), password)).name for j in range(excel_instance.HighlightResourceFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndexField()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSyncField()),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupIdField(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPathField(), password),
        "BGPath": convert_string(excel_instance.BGPathField(), password),
        "RaidSkillDescriptionListId": convert_int(excel_instance.RaidSkillDescriptionListIdField(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterIdField(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterIdField(j), password) for j in range(excel_instance.BossCharacterIdFieldLength())],
        "AssistCharacterLimitCount": convert_int(excel_instance.AssistCharacterLimitCountField(), password),
        "WorldRaidDifficulty": WorldRaidDifficulty(convert_int(excel_instance.WorldRaidDifficultyField(), password)).name,
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenConditionField()),
        "RaidEnterAmount": convert_int(excel_instance.RaidEnterAmountField(), password),
        "ReEnterAmount": convert_int(excel_instance.ReEnterAmountField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "RaidBattleEndRewardGroupId": convert_int(excel_instance.RaidBattleEndRewardGroupIdField(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupIdField(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePathField(j), password) for j in range(excel_instance.BattleReadyTimelinePathFieldLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStartField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartFieldLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEndField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndFieldLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePathField(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePathField(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhaseField(), password),
        "EnterScenarioKey": convert_int(excel_instance.EnterScenarioKeyField(), password),
        "ClearScenarioKey": convert_int(excel_instance.ClearScenarioKeyField(), password),
        "UseFixedEchelon": bool(excel_instance.UseFixedEchelonField()),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "IsRaidScenarioBattle": bool(excel_instance.IsRaidScenarioBattleField()),
        "ShowSkillCard": bool(excel_instance.ShowSkillCardField()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKeyField(), password),
        "DamageToWorldBoss": convert_int(excel_instance.DamageToWorldBossField(), password),
        "AllyPassiveSkill": [convert_string(excel_instance.AllyPassiveSkillField(j), password) for j in range(excel_instance.AllyPassiveSkillFieldLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevelField(j), password) for j in range(excel_instance.AllyPassiveSkillLevelFieldLength())],
        "AllyPassiveSkillRemoveCondition": [convert_int(excel_instance.AllyPassiveSkillRemoveConditionField(j), password) for j in range(excel_instance.AllyPassiveSkillRemoveConditionFieldLength())],
        "EnemyPassiveSkill": [convert_string(excel_instance.EnemyPassiveSkillField(j), password) for j in range(excel_instance.EnemyPassiveSkillFieldLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevelField(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelFieldLength())],
        "EnemyPassiveSkillRemoveCondition": [convert_int(excel_instance.EnemyPassiveSkillRemoveConditionField(j), password) for j in range(excel_instance.EnemyPassiveSkillRemoveConditionFieldLength())],
        "SaveCurrentLocalBossHP": bool(excel_instance.SaveCurrentLocalBossHPField()),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_InteractiveWorldRaidStatusPresetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "WorldRaidSeasonId": convert_int(excel_instance.WorldRaidSeasonIdField(), password),
        "WorldRaidPhaseId": convert_int(excel_instance.WorldRaidPhaseIdField(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeIdField(), password),
        "IAWorldRaidGroupId": [convert_int(excel_instance.IAWorldRaidGroupIdField(j), password) for j in range(excel_instance.IAWorldRaidGroupIdFieldLength())],
        "EventContentStageId": [convert_int(excel_instance.EventContentStageIdField(j), password) for j in range(excel_instance.EventContentStageIdFieldLength())],
        "EventContentScenarioId": [convert_int(excel_instance.EventContentScenarioIdField(j), password) for j in range(excel_instance.EventContentScenarioIdFieldLength())],
    }

def dump_ExcelDB_ItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "Rarity": Rarity(convert_int(excel_instance.RarityField(), password)).name,
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "ItemCategory": ItemCategory(convert_int(excel_instance.ItemCategoryField(), password)).name,
        "Quality": convert_int(excel_instance.QualityField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
        "SpriteName": convert_string(excel_instance.SpriteNameField(), password),
        "StackableMax": convert_int(excel_instance.StackableMaxField(), password),
        "StackableFunction": convert_int(excel_instance.StackableFunctionField(), password),
        "ImmediateUse": bool(excel_instance.ImmediateUseField()),
        "UsingResultParcelType": ParcelType(convert_int(excel_instance.UsingResultParcelTypeField(), password)).name,
        "UsingResultId": convert_int(excel_instance.UsingResultIdField(), password),
        "UsingResultAmount": convert_int(excel_instance.UsingResultAmountField(), password),
        "MailType": MailType(convert_int(excel_instance.MailTypeField(), password)).name,
        "ExpiryChangeParcelType": ParcelType(convert_int(excel_instance.ExpiryChangeParcelTypeField(), password)).name,
        "ExpiryChangeId": convert_int(excel_instance.ExpiryChangeIdField(), password),
        "ExpiryChangeAmount": convert_int(excel_instance.ExpiryChangeAmountField(), password),
        "CanTierUpgrade": bool(excel_instance.CanTierUpgradeField()),
        "TierUpgradeRecipeCraftId": convert_int(excel_instance.TierUpgradeRecipeCraftIdField(), password),
        "Tags": [Tag(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
        "IsCollaboration": bool(excel_instance.IsCollaborationField()),
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0Field(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1Field(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2Field(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQualityField(), password),
        "MaxGiftTags": convert_int(excel_instance.MaxGiftTagsField(), password),
        "ShopCategory": [convert_float(excel_instance.ShopCategoryField(j), password) for j in range(excel_instance.ShopCategoryFieldLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTimeField(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateInField(), password),
        "IsOverrideExpiration": bool(excel_instance.IsOverrideExpirationField()),
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeIdField(), password),
        "GachaTicket": GachaTicketType(convert_int(excel_instance.GachaTicketField(), password)).name,
        "AlertPopupId": convert_int(excel_instance.AlertPopupIdField(), password),
        "ShiftingCraftRecipe": convert_int(excel_instance.ShiftingCraftRecipeField(), password),
    }

def dump_ExcelDB_KeyControllerImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerKeyCode": convert_string(excel_instance.ControllerKeyCodeField(), password),
        "PSIconName": convert_string(excel_instance.PSIconNameField(), password),
        "XBoxIconName": convert_string(excel_instance.XBoxIconNameField(), password),
        "SteamDeckIconName": convert_string(excel_instance.SteamDeckIconNameField(), password),
    }

def dump_ExcelDB_KeyMappingDisplayInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "KeyMappingKeyCode": convert_string(excel_instance.KeyMappingKeyCodeField(), password),
        "KeyMappingDisplayName": convert_string(excel_instance.KeyMappingDisplayNameField(), password),
    }

def dump_ExcelDB_KeyMappingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_string(excel_instance.IdField(), password),
        "DisplayGroupType": DisplayGroupType(convert_int(excel_instance.DisplayGroupTypeField(), password)).name,
        "GroupId": convert_string(excel_instance.GroupIdField(), password),
        "EnableCustomMapping": bool(excel_instance.EnableCustomMappingField()),
        "DisplayCustomMapping": bool(excel_instance.DisplayCustomMappingField()),
        "LocalizeKeyMappingId": convert_uint(excel_instance.LocalizeKeyMappingIdField(), password),
        "TargetKeyCode": convert_string(excel_instance.TargetKeyCodeField(), password),
        "ControllerCursorFocus": bool(excel_instance.ControllerCursorFocusField()),
        "ControllerKeyCode": convert_string(excel_instance.ControllerKeyCodeField(), password),
        "IsDisplay": bool(excel_instance.IsDisplayField()),
        "IsDisplayController": bool(excel_instance.IsDisplayControllerField()),
        "IsUsed": bool(excel_instance.IsUsedField()),
        "IsUsedController": bool(excel_instance.IsUsedControllerField()),
        "IsLongPress": bool(excel_instance.IsLongPressField()),
        "IgnorePosCheck": bool(excel_instance.IgnorePosCheckField()),
        "IconPositionX": convert_float(excel_instance.IconPositionXField(), password),
        "IconPositionY": convert_float(excel_instance.IconPositionYField(), password),
        "IconScaleX": convert_float(excel_instance.IconScaleXField(), password),
        "IconScaleY": convert_float(excel_instance.IconScaleYField(), password),
        "ControllerIconPositionX": convert_float(excel_instance.ControllerIconPositionXField(), password),
        "ControllerIconPositionY": convert_float(excel_instance.ControllerIconPositionYField(), password),
        "ControllerIconScaleX": convert_float(excel_instance.ControllerIconScaleXField(), password),
        "ControllerIconScaleY": convert_float(excel_instance.ControllerIconScaleYField(), password),
        "KeymappingIconBGName": convert_string(excel_instance.KeymappingIconBGNameField(), password),
    }

def dump_ExcelDB_KeyMappingGroupInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DisplayGroupType": DisplayGroupType(convert_int(excel_instance.DisplayGroupTypeField(), password)).name,
        "LocalizeKeyMappingDisplayGroupId": convert_uint(excel_instance.LocalizeKeyMappingDisplayGroupIdField(), password),
    }

def dump_ExcelDB_KeyMappingPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "ButtonName": [convert_string(excel_instance.ButtonNameField(j), password) for j in range(excel_instance.ButtonNameFieldLength())],
        "KeyMappingId": [convert_string(excel_instance.KeyMappingIdField(j), password) for j in range(excel_instance.KeyMappingIdFieldLength())],
    }

def dump_ExcelDB_KeyMappingPopupNoneFocusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "ButtonName": convert_string(excel_instance.ButtonNameField(), password),
    }

def dump_ExcelDB_KeyMappingTabExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_string(excel_instance.IdField(), password),
        "LeftArrowKey": convert_string(excel_instance.LeftArrowKeyField(), password),
        "RightArrowKey": convert_string(excel_instance.RightArrowKeyField(), password),
        "LeftIconPositionX": convert_float(excel_instance.LeftIconPositionXField(), password),
        "LeftIconPositionY": convert_float(excel_instance.LeftIconPositionYField(), password),
        "LeftIconScaleX": convert_float(excel_instance.LeftIconScaleXField(), password),
        "LeftIconScaleY": convert_float(excel_instance.LeftIconScaleYField(), password),
        "RightIconPositionX": convert_float(excel_instance.RightIconPositionXField(), password),
        "RightIconPositionY": convert_float(excel_instance.RightIconPositionYField(), password),
        "RightIconScaleX": convert_float(excel_instance.RightIconScaleXField(), password),
        "RightIconScaleY": convert_float(excel_instance.RightIconScaleYField(), password),
    }

def dump_ExcelDB_LevelExpMasterCoinExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "MinLevel": convert_int(excel_instance.MinLevelField(), password),
        "MaxLevel": convert_int(excel_instance.MaxLevelField(), password),
        "Ratio": convert_int(excel_instance.RatioField(), password),
    }

def dump_ExcelDB_LoadingImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKrField(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJpField(), password),
        "DisplayWeight": convert_int(excel_instance.DisplayWeightField(), password),
        "ImagePathTh": convert_string(excel_instance.ImagePathThField(), password),
        "ImagePathTw": convert_string(excel_instance.ImagePathTwField(), password),
        "ImagePathEn": convert_string(excel_instance.ImagePathEnField(), password),
    }

def dump_ExcelDB_LocalizeCharProfileChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeIdField(), password),
        "ChangeCharacterID": convert_int(excel_instance.ChangeCharacterIDField(), password),
        "OverrideClub": bool(excel_instance.OverrideClubField()),
    }

def dump_ExcelDB_LocalizeCharProfileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "StatusMessageKr": convert_string(excel_instance.StatusMessageKrField(), password),
        "StatusMessageJp": convert_string(excel_instance.StatusMessageJpField(), password),
        "StatusMessageTh": convert_string(excel_instance.StatusMessageThField(), password),
        "StatusMessageTw": convert_string(excel_instance.StatusMessageTwField(), password),
        "StatusMessageEn": convert_string(excel_instance.StatusMessageEnField(), password),
        "FullNameKr": convert_string(excel_instance.FullNameKrField(), password),
        "FullNameJp": convert_string(excel_instance.FullNameJpField(), password),
        "FullNameTh": convert_string(excel_instance.FullNameThField(), password),
        "FullNameTw": convert_string(excel_instance.FullNameTwField(), password),
        "FullNameEn": convert_string(excel_instance.FullNameEnField(), password),
        "FamilyNameKr": convert_string(excel_instance.FamilyNameKrField(), password),
        "FamilyNameRubyKr": convert_string(excel_instance.FamilyNameRubyKrField(), password),
        "PersonalNameKr": convert_string(excel_instance.PersonalNameKrField(), password),
        "PersonalNameRubyKr": convert_string(excel_instance.PersonalNameRubyKrField(), password),
        "FamilyNameJp": convert_string(excel_instance.FamilyNameJpField(), password),
        "FamilyNameRubyJp": convert_string(excel_instance.FamilyNameRubyJpField(), password),
        "PersonalNameJp": convert_string(excel_instance.PersonalNameJpField(), password),
        "PersonalNameRubyJp": convert_string(excel_instance.PersonalNameRubyJpField(), password),
        "FamilyNameTh": convert_string(excel_instance.FamilyNameThField(), password),
        "FamilyNameRubyTh": convert_string(excel_instance.FamilyNameRubyThField(), password),
        "PersonalNameTh": convert_string(excel_instance.PersonalNameThField(), password),
        "PersonalNameRubyTh": convert_string(excel_instance.PersonalNameRubyThField(), password),
        "FamilyNameTw": convert_string(excel_instance.FamilyNameTwField(), password),
        "FamilyNameRubyTw": convert_string(excel_instance.FamilyNameRubyTwField(), password),
        "PersonalNameTw": convert_string(excel_instance.PersonalNameTwField(), password),
        "PersonalNameRubyTw": convert_string(excel_instance.PersonalNameRubyTwField(), password),
        "FamilyNameEn": convert_string(excel_instance.FamilyNameEnField(), password),
        "FamilyNameRubyEn": convert_string(excel_instance.FamilyNameRubyEnField(), password),
        "PersonalNameEn": convert_string(excel_instance.PersonalNameEnField(), password),
        "PersonalNameRubyEn": convert_string(excel_instance.PersonalNameRubyEnField(), password),
        "Club": Club(convert_int(excel_instance.ClubField(), password)).name,
        "ClubNameForGachaKr": convert_string(excel_instance.ClubNameForGachaKrField(), password),
        "ClubNameForGachaJp": convert_string(excel_instance.ClubNameForGachaJpField(), password),
        "ClubNameForGachaTh": convert_string(excel_instance.ClubNameForGachaThField(), password),
        "ClubNameForGachaTw": convert_string(excel_instance.ClubNameForGachaTwField(), password),
        "ClubNameForGachaEn": convert_string(excel_instance.ClubNameForGachaEnField(), password),
        "SchoolYearKr": convert_string(excel_instance.SchoolYearKrField(), password),
        "SchoolYearJp": convert_string(excel_instance.SchoolYearJpField(), password),
        "SchoolYearTh": convert_string(excel_instance.SchoolYearThField(), password),
        "SchoolYearTw": convert_string(excel_instance.SchoolYearTwField(), password),
        "SchoolYearEn": convert_string(excel_instance.SchoolYearEnField(), password),
        "CharacterAgeKr": convert_string(excel_instance.CharacterAgeKrField(), password),
        "CharacterAgeJp": convert_string(excel_instance.CharacterAgeJpField(), password),
        "CharacterAgeTh": convert_string(excel_instance.CharacterAgeThField(), password),
        "CharacterAgeTw": convert_string(excel_instance.CharacterAgeTwField(), password),
        "CharacterAgeEn": convert_string(excel_instance.CharacterAgeEnField(), password),
        "BirthDay": convert_string(excel_instance.BirthDayField(), password),
        "BirthdayKr": convert_string(excel_instance.BirthdayKrField(), password),
        "BirthdayJp": convert_string(excel_instance.BirthdayJpField(), password),
        "BirthdayTh": convert_string(excel_instance.BirthdayThField(), password),
        "BirthdayTw": convert_string(excel_instance.BirthdayTwField(), password),
        "BirthdayEn": convert_string(excel_instance.BirthdayEnField(), password),
        "CharHeightKr": convert_string(excel_instance.CharHeightKrField(), password),
        "CharHeightJp": convert_string(excel_instance.CharHeightJpField(), password),
        "CharHeightTh": convert_string(excel_instance.CharHeightThField(), password),
        "CharHeightTw": convert_string(excel_instance.CharHeightTwField(), password),
        "CharHeightEn": convert_string(excel_instance.CharHeightEnField(), password),
        "DesignerNameKr": convert_string(excel_instance.DesignerNameKrField(), password),
        "DesignerNameJp": convert_string(excel_instance.DesignerNameJpField(), password),
        "DesignerNameTh": convert_string(excel_instance.DesignerNameThField(), password),
        "DesignerNameTw": convert_string(excel_instance.DesignerNameTwField(), password),
        "DesignerNameEn": convert_string(excel_instance.DesignerNameEnField(), password),
        "IllustratorNameKr": convert_string(excel_instance.IllustratorNameKrField(), password),
        "IllustratorNameJp": convert_string(excel_instance.IllustratorNameJpField(), password),
        "IllustratorNameTh": convert_string(excel_instance.IllustratorNameThField(), password),
        "IllustratorNameTw": convert_string(excel_instance.IllustratorNameTwField(), password),
        "IllustratorNameEn": convert_string(excel_instance.IllustratorNameEnField(), password),
        "CharacterVoiceKr": convert_string(excel_instance.CharacterVoiceKrField(), password),
        "CharacterVoiceJp": convert_string(excel_instance.CharacterVoiceJpField(), password),
        "CharacterVoiceTh": convert_string(excel_instance.CharacterVoiceThField(), password),
        "CharacterVoiceTw": convert_string(excel_instance.CharacterVoiceTwField(), password),
        "CharacterVoiceEn": convert_string(excel_instance.CharacterVoiceEnField(), password),
        "KRCharacterVoiceKr": convert_string(excel_instance.KRCharacterVoiceKrField(), password),
        "KRCharacterVoiceTh": convert_string(excel_instance.KRCharacterVoiceThField(), password),
        "KRCharacterVoiceTw": convert_string(excel_instance.KRCharacterVoiceTwField(), password),
        "KRCharacterVoiceEn": convert_string(excel_instance.KRCharacterVoiceEnField(), password),
        "HobbyKr": convert_string(excel_instance.HobbyKrField(), password),
        "HobbyJp": convert_string(excel_instance.HobbyJpField(), password),
        "HobbyTh": convert_string(excel_instance.HobbyThField(), password),
        "HobbyTw": convert_string(excel_instance.HobbyTwField(), password),
        "HobbyEn": convert_string(excel_instance.HobbyEnField(), password),
        "WeaponNameKr": convert_string(excel_instance.WeaponNameKrField(), password),
        "WeaponDescKr": convert_string(excel_instance.WeaponDescKrField(), password),
        "WeaponNameJp": convert_string(excel_instance.WeaponNameJpField(), password),
        "WeaponDescJp": convert_string(excel_instance.WeaponDescJpField(), password),
        "WeaponNameTh": convert_string(excel_instance.WeaponNameThField(), password),
        "WeaponDescTh": convert_string(excel_instance.WeaponDescThField(), password),
        "WeaponNameTw": convert_string(excel_instance.WeaponNameTwField(), password),
        "WeaponDescTw": convert_string(excel_instance.WeaponDescTwField(), password),
        "WeaponNameEn": convert_string(excel_instance.WeaponNameEnField(), password),
        "WeaponDescEn": convert_string(excel_instance.WeaponDescEnField(), password),
        "ProfileIntroductionKr": convert_string(excel_instance.ProfileIntroductionKrField(), password),
        "ProfileIntroductionJp": convert_string(excel_instance.ProfileIntroductionJpField(), password),
        "ProfileIntroductionTh": convert_string(excel_instance.ProfileIntroductionThField(), password),
        "ProfileIntroductionTw": convert_string(excel_instance.ProfileIntroductionTwField(), password),
        "ProfileIntroductionEn": convert_string(excel_instance.ProfileIntroductionEnField(), password),
        "CharacterSSRNewKr": convert_string(excel_instance.CharacterSSRNewKrField(), password),
        "CharacterSSRNewJp": convert_string(excel_instance.CharacterSSRNewJpField(), password),
        "CharacterSSRNewTh": convert_string(excel_instance.CharacterSSRNewThField(), password),
        "CharacterSSRNewTw": convert_string(excel_instance.CharacterSSRNewTwField(), password),
        "CharacterSSRNewEn": convert_string(excel_instance.CharacterSSRNewEnField(), password),
    }

def dump_ExcelDB_LocalizeCodeInBuildExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
        "Th": convert_string(excel_instance.ThField(), password),
        "Tw": convert_string(excel_instance.TwField(), password),
        "En": convert_string(excel_instance.EnField(), password),
    }

def dump_ExcelDB_LocalizeErrorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "ErrorLevel": WebAPIErrorLevel(convert_int(excel_instance.ErrorLevelField(), password)).name,
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
        "Th": convert_string(excel_instance.ThField(), password),
        "Tw": convert_string(excel_instance.TwField(), password),
        "En": convert_string(excel_instance.EnField(), password),
    }

def dump_ExcelDB_LocalizeEtcExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "NameKr": convert_string(excel_instance.NameKrField(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKrField(), password),
        "NameJp": convert_string(excel_instance.NameJpField(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJpField(), password),
        "NameTh": convert_string(excel_instance.NameThField(), password),
        "DescriptionTh": convert_string(excel_instance.DescriptionThField(), password),
        "NameTw": convert_string(excel_instance.NameTwField(), password),
        "DescriptionTw": convert_string(excel_instance.DescriptionTwField(), password),
        "NameEn": convert_string(excel_instance.NameEnField(), password),
        "DescriptionEn": convert_string(excel_instance.DescriptionEnField(), password),
    }

def dump_ExcelDB_LocalizeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
        "Th": convert_string(excel_instance.ThField(), password),
        "Tw": convert_string(excel_instance.TwField(), password),
        "En": convert_string(excel_instance.EnField(), password),
    }

def dump_ExcelDB_LocalizeGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GachaShopId": convert_int(excel_instance.GachaShopIdField(), password),
        "TabNameKr": convert_string(excel_instance.TabNameKrField(), password),
        "TabNameJp": convert_string(excel_instance.TabNameJpField(), password),
        "TabNameTh": convert_string(excel_instance.TabNameThField(), password),
        "TabNameTw": convert_string(excel_instance.TabNameTwField(), password),
        "TabNameEn": convert_string(excel_instance.TabNameEnField(), password),
        "TitleNameKr": convert_string(excel_instance.TitleNameKrField(), password),
        "TitleNameJp": convert_string(excel_instance.TitleNameJpField(), password),
        "TitleNameTh": convert_string(excel_instance.TitleNameThField(), password),
        "TitleNameTw": convert_string(excel_instance.TitleNameTwField(), password),
        "TitleNameEn": convert_string(excel_instance.TitleNameEnField(), password),
        "SubTitleKr": convert_string(excel_instance.SubTitleKrField(), password),
        "SubTitleJp": convert_string(excel_instance.SubTitleJpField(), password),
        "SubTitleTh": convert_string(excel_instance.SubTitleThField(), password),
        "SubTitleTw": convert_string(excel_instance.SubTitleTwField(), password),
        "SubTitleEn": convert_string(excel_instance.SubTitleEnField(), password),
        "GachaDescriptionKr": convert_string(excel_instance.GachaDescriptionKrField(), password),
        "GachaDescriptionJp": convert_string(excel_instance.GachaDescriptionJpField(), password),
        "GachaDescriptionTh": convert_string(excel_instance.GachaDescriptionThField(), password),
        "GachaDescriptionTw": convert_string(excel_instance.GachaDescriptionTwField(), password),
        "GachaDescriptionEn": convert_string(excel_instance.GachaDescriptionEnField(), password),
    }

def dump_ExcelDB_LocalizeSkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "NameKr": convert_string(excel_instance.NameKrField(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKrField(), password),
        "SkillInvokeLocalizeKr": convert_string(excel_instance.SkillInvokeLocalizeKrField(), password),
        "NameJp": convert_string(excel_instance.NameJpField(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJpField(), password),
        "SkillInvokeLocalizeJp": convert_string(excel_instance.SkillInvokeLocalizeJpField(), password),
        "NameTh": convert_string(excel_instance.NameThField(), password),
        "DescriptionTh": convert_string(excel_instance.DescriptionThField(), password),
        "SkillInvokeLocalizeTh": convert_string(excel_instance.SkillInvokeLocalizeThField(), password),
        "NameTw": convert_string(excel_instance.NameTwField(), password),
        "DescriptionTw": convert_string(excel_instance.DescriptionTwField(), password),
        "SkillInvokeLocalizeTw": convert_string(excel_instance.SkillInvokeLocalizeTwField(), password),
        "NameEn": convert_string(excel_instance.NameEnField(), password),
        "DescriptionEn": convert_string(excel_instance.DescriptionEnField(), password),
        "SkillInvokeLocalizeEn": convert_string(excel_instance.SkillInvokeLocalizeEnField(), password),
    }

def dump_ExcelDB_LogicEffectCommonVisualExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringIDField(), password),
        "IconSpriteName": convert_string(excel_instance.IconSpriteNameField(), password),
        "IconDispelColor": [convert_float(excel_instance.IconDispelColorField(j), password) for j in range(excel_instance.IconDispelColorFieldLength())],
        "ParticleEnterPath": convert_string(excel_instance.ParticleEnterPathField(), password),
        "ParticleEnterSocket": EffectBone(convert_int(excel_instance.ParticleEnterSocketField(), password)).name,
        "ParticleLoopPath": convert_string(excel_instance.ParticleLoopPathField(), password),
        "ParticleLoopSocket": EffectBone(convert_int(excel_instance.ParticleLoopSocketField(), password)).name,
        "ParticleEndPath": convert_string(excel_instance.ParticleEndPathField(), password),
        "ParticleEndSocket": EffectBone(convert_int(excel_instance.ParticleEndSocketField(), password)).name,
        "ParticleApplyPath": convert_string(excel_instance.ParticleApplyPathField(), password),
        "ParticleApplySocket": EffectBone(convert_int(excel_instance.ParticleApplySocketField(), password)).name,
        "ParticleRemovedPath": convert_string(excel_instance.ParticleRemovedPathField(), password),
        "ParticleRemovedSocket": EffectBone(convert_int(excel_instance.ParticleRemovedSocketField(), password)).name,
    }

def dump_ExcelDB_MemoryLobbyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "MemoryLobbyCategory": MemoryLobbyCategory(convert_int(excel_instance.MemoryLobbyCategoryField(), password)).name,
        "SlotTextureName": convert_string(excel_instance.SlotTextureNameField(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureNameField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "AudioClipJp": convert_string(excel_instance.AudioClipJpField(), password),
        "AudioClipKr": convert_string(excel_instance.AudioClipKrField(), password),
        "AudioClipTh": convert_string(excel_instance.AudioClipThField(), password),
        "AudioClipTw": convert_string(excel_instance.AudioClipTwField(), password),
        "AudioClipEn": convert_string(excel_instance.AudioClipEnField(), password),
    }

def dump_ExcelDB_MemoryLobby_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "PrefabNameKr": convert_string(excel_instance.PrefabNameKrField(), password),
        "PrefabNameTw": convert_string(excel_instance.PrefabNameTwField(), password),
        "PrefabNameAsia": convert_string(excel_instance.PrefabNameAsiaField(), password),
        "PrefabNameNa": convert_string(excel_instance.PrefabNameNaField(), password),
        "PrefabNameGlobal": convert_string(excel_instance.PrefabNameGlobalField(), password),
        "PrefabNameTeen": convert_string(excel_instance.PrefabNameTeenField(), password),
    }

def dump_ExcelDB_MessagePopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringId": convert_uint(excel_instance.StringIdField(), password),
        "MessagePopupLayout": MessagePopupLayout(convert_int(excel_instance.MessagePopupLayoutField(), password)).name,
        "OrderType": MessagePopupImagePositionType(convert_int(excel_instance.OrderTypeField(), password)).name,
        "Image": convert_string(excel_instance.ImageField(), password),
        "TitleText": convert_uint(excel_instance.TitleTextField(), password),
        "SubTitleText": convert_uint(excel_instance.SubTitleTextField(), password),
        "MessageText": convert_uint(excel_instance.MessageTextField(), password),
        "ConditionText": [convert_uint(excel_instance.ConditionTextField(j), password) for j in range(excel_instance.ConditionTextFieldLength())],
        "DisplayXButton": bool(excel_instance.DisplayXButtonField()),
        "Button": [MessagePopupButtonType(convert_int(excel_instance.ButtonField(j), password)).name for j in range(excel_instance.ButtonFieldLength())],
        "ButtonText": [convert_uint(excel_instance.ButtonTextField(j), password) for j in range(excel_instance.ButtonTextFieldLength())],
        "ButtonCommand": [convert_string(excel_instance.ButtonCommandField(j), password) for j in range(excel_instance.ButtonCommandFieldLength())],
        "ButtonParameter": [convert_string(excel_instance.ButtonParameterField(j), password) for j in range(excel_instance.ButtonParameterFieldLength())],
    }

def dump_ExcelDB_MiniGameAudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHashField(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefixField(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHashField(), password),
        "StateName": convert_string(excel_instance.StateNameField(), password),
        "IgnoreInterruptDelay": bool(excel_instance.IgnoreInterruptDelayField()),
        "IgnoreInterruptPlay": bool(excel_instance.IgnoreInterruptPlayField()),
        "Volume": convert_float(excel_instance.VolumeField(), password),
        "Delay": convert_float(excel_instance.DelayField(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriorityField(), password),
        "AudioClipPath": [convert_string(excel_instance.AudioClipPathField(j), password) for j in range(excel_instance.AudioClipPathFieldLength())],
        "VoiceHash": [convert_uint(excel_instance.VoiceHashField(j), password) for j in range(excel_instance.VoiceHashFieldLength())],
    }

def dump_ExcelDB_MinigameCCGCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Type": CCGCardType(convert_int(excel_instance.TypeField(), password)).name,
        "IsDisposal": bool(excel_instance.IsDisposalField()),
        "ActiveSkillId": convert_int(excel_instance.ActiveSkillIdField(), password),
        "ActiveSkillCost": convert_int(excel_instance.ActiveSkillCostField(), password),
        "ActiveSkilleCostVisible": bool(excel_instance.ActiveSkilleCostVisibleField()),
        "PassiveSkillId": [convert_int(excel_instance.PassiveSkillIdField(j), password) for j in range(excel_instance.PassiveSkillIdFieldLength())],
        "PassiveActivateCount": convert_int(excel_instance.PassiveActivateCountField(), password),
        "Name": convert_uint(excel_instance.NameField(), password),
        "Description": convert_string(excel_instance.DescriptionField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
        "UIImagePath": convert_string(excel_instance.UIImagePathField(), password),
        "Tags": [CCGTagType(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
    }

def dump_ExcelDB_MinigameCCGCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Type": CCGCharacterType(convert_int(excel_instance.TypeField(), password)).name,
        "ActiveSkillId": convert_int(excel_instance.ActiveSkillIdField(), password),
        "ActiveSkillCost": convert_int(excel_instance.ActiveSkillCostField(), password),
        "ActiveSkilleCostVisible": bool(excel_instance.ActiveSkilleCostVisibleField()),
        "ActiveSkillCooldown": convert_int(excel_instance.ActiveSkillCooldownField(), password),
        "MaxHealth": convert_int(excel_instance.MaxHealthField(), password),
        "PassiveSkillId": [convert_int(excel_instance.PassiveSkillIdField(j), password) for j in range(excel_instance.PassiveSkillIdFieldLength())],
        "Name": convert_uint(excel_instance.NameField(), password),
        "Description": convert_string(excel_instance.DescriptionField(), password),
        "ImagePath": convert_string(excel_instance.ImagePathField(), password),
        "UIImagePath": convert_string(excel_instance.UIImagePathField(), password),
        "Tags": [CCGTagType(convert_int(excel_instance.TagsField(j), password)).name for j in range(excel_instance.TagsFieldLength())],
    }

def dump_ExcelDB_MinigameCCGEnemyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "CharacterType": CCGCharacterType(convert_int(excel_instance.CharacterTypeField(), password)).name,
        "Order": convert_int(excel_instance.OrderField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
    }

def dump_ExcelDB_MinigameCCGEnemyGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "EnemyAI": convert_string(excel_instance.EnemyAIField(), password),
        "EnemyBGM": convert_int(excel_instance.EnemyBGMField(), password),
        "LocalizeEnemyGroupName": convert_uint(excel_instance.LocalizeEnemyGroupNameField(), password),
        "LocalizeEnemyGroupDesc": convert_uint(excel_instance.LocalizeEnemyGroupDescField(), password),
    }

def dump_ExcelDB_MinigameCCGInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CCGId": convert_int(excel_instance.CCGIdField(), password),
        "CostParcelType": ParcelType(convert_int(excel_instance.CostParcelTypeField(), password)).name,
        "CostParcelId": convert_int(excel_instance.CostParcelIdField(), password),
        "CostParcelAmount": convert_int(excel_instance.CostParcelAmountField(), password),
        "CardBackPath": convert_string(excel_instance.CardBackPathField(), password),
        "PerkCostParcelType": ParcelType(convert_int(excel_instance.PerkCostParcelTypeField(), password)).name,
        "PerkCostParcelId": convert_int(excel_instance.PerkCostParcelIdField(), password),
    }

def dump_ExcelDB_MinigameCCGLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelId": convert_int(excel_instance.LevelIdField(), password),
        "CCGId": convert_int(excel_instance.CCGIdField(), password),
        "FloorIndex": convert_int(excel_instance.FloorIndexField(), password),
        "BackgroundPath": convert_string(excel_instance.BackgroundPathField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
    }

def dump_ExcelDB_MinigameCCGLevelNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelId": convert_int(excel_instance.LevelIdField(), password),
        "NodeId": convert_int(excel_instance.NodeIdField(), password),
        "NodeIcon": CCGLevelNodeIcon(convert_int(excel_instance.NodeIconField(), password)).name,
        "StageGroupId": convert_int(excel_instance.StageGroupIdField(), password),
        "NextNodeId": [convert_int(excel_instance.NextNodeIdField(j), password) for j in range(excel_instance.NextNodeIdFieldLength())],
    }

def dump_ExcelDB_MinigameCCGLevelStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "EnemyGroupId": [convert_int(excel_instance.EnemyGroupIdField(j), password) for j in range(excel_instance.EnemyGroupIdFieldLength())],
        "StageType": CCGStageType(convert_int(excel_instance.StageTypeField(), password)).name,
        "CampDiscardCardCount": convert_int(excel_instance.CampDiscardCardCountField(), password),
        "CampSprPath": convert_string(excel_instance.CampSprPathField(), password),
        "CampBackgroundPath": convert_string(excel_instance.CampBackgroundPathField(), password),
        "RewardType": CCGStageRewardType(convert_int(excel_instance.RewardTypeField(), password)).name,
        "RewardCount": convert_int(excel_instance.RewardCountField(), password),
        "RewardCardGroupId": convert_int(excel_instance.RewardCardGroupIdField(), password),
        "CardRarityGroupId": convert_int(excel_instance.CardRarityGroupIdField(), password),
        "IsSkipIntroScenario": bool(excel_instance.IsSkipIntroScenarioField()),
        "IntroScenarioGroupId": convert_int(excel_instance.IntroScenarioGroupIdField(), password),
        "IsSkipOutroScenario": bool(excel_instance.IsSkipOutroScenarioField()),
        "OutroScenarioGroupId": convert_int(excel_instance.OutroScenarioGroupIdField(), password),
    }

def dump_ExcelDB_MinigameCCGLogicEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DataLoadPath": convert_string(excel_instance.DataLoadPathField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
    }

def dump_ExcelDB_MinigameCCGOpenDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DialogId": convert_int(excel_instance.DialogIdField(), password),
        "PlayOrder": convert_int(excel_instance.PlayOrderField(), password),
        "ConditionCard": convert_int(excel_instance.ConditionCardField(), password),
        "Dialog": convert_uint(excel_instance.DialogField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationKr": convert_int(excel_instance.DurationKrField(), password),
        "Voice": convert_uint(excel_instance.VoiceField(), password),
    }

def dump_ExcelDB_MinigameCCGPerkExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CCGId": convert_int(excel_instance.CCGIdField(), password),
        "CostParcelAmount": convert_int(excel_instance.CostParcelAmountField(), password),
        "RerollPoint": convert_int(excel_instance.RerollPointField(), password),
        "DiscardPoint": convert_int(excel_instance.DiscardPointField(), password),
        "EnvironmentLogicEffectId": [convert_int(excel_instance.EnvironmentLogicEffectIdField(j), password) for j in range(excel_instance.EnvironmentLogicEffectIdFieldLength())],
        "RequiredPerkId": [convert_int(excel_instance.RequiredPerkIdField(j), password) for j in range(excel_instance.RequiredPerkIdFieldLength())],
        "ShopOrder": convert_int(excel_instance.ShopOrderField(), password),
        "ShopIcon": convert_string(excel_instance.ShopIconField(), password),
        "ShopLocalizeTitle": convert_uint(excel_instance.ShopLocalizeTitleField(), password),
        "ShopLocalizeDesc": convert_uint(excel_instance.ShopLocalizeDescField(), password),
    }

def dump_ExcelDB_MinigameCCGRewardCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "EntityType": CCGEntityType(convert_int(excel_instance.EntityTypeField(), password)).name,
        "CardId": convert_int(excel_instance.CardIdField(), password),
        "CardRarity": convert_int(excel_instance.CardRarityField(), password),
    }

def dump_ExcelDB_MinigameCCGRewardCardRateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RarityGroupId": convert_int(excel_instance.RarityGroupIdField(), password),
        "CardRarity": convert_int(excel_instance.CardRarityField(), password),
        "Rate": convert_int(excel_instance.RateField(), password),
    }

def dump_ExcelDB_MinigameCCGRewardItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CCGId": convert_int(excel_instance.CCGIdField(), password),
        "MinPoint": convert_int(excel_instance.MinPointField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
    }

def dump_ExcelDB_MinigameCCGSkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SkillType": convert_string(excel_instance.SkillTypeField(), password),
        "DataLoadPath": convert_string(excel_instance.DataLoadPathField(), password),
        "Name": convert_uint(excel_instance.NameField(), password),
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "SkillIcon": convert_string(excel_instance.SkillIconField(), password),
    }

def dump_ExcelDB_MinigameCCGStartDeckCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CCGId": convert_int(excel_instance.CCGIdField(), password),
        "CardId": convert_int(excel_instance.CardIdField(), password),
    }

def dump_ExcelDB_MinigameCCGStartDeckCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CCGId": convert_int(excel_instance.CCGIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
    }

def dump_ExcelDB_MiniGameDefenseCharacterBanExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
    }

def dump_ExcelDB_MiniGameDefenseFixedStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MinigameDefenseFixedStatId": convert_int(excel_instance.MinigameDefenseFixedStatIdField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "Grade": convert_int(excel_instance.GradeField(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevelField(), password),
        "NoneExSkillLevel": convert_int(excel_instance.NoneExSkillLevelField(), password),
        "Equipment1Tier": convert_int(excel_instance.Equipment1TierField(), password),
        "Equipment1Level": convert_int(excel_instance.Equipment1LevelField(), password),
        "Equipment2Tier": convert_int(excel_instance.Equipment2TierField(), password),
        "Equipment2Level": convert_int(excel_instance.Equipment2LevelField(), password),
        "Equipment3Tier": convert_int(excel_instance.Equipment3TierField(), password),
        "Equipment3Level": convert_int(excel_instance.Equipment3LevelField(), password),
        "CharacterWeaponGrade": convert_int(excel_instance.CharacterWeaponGradeField(), password),
        "CharacterWeaponLevel": convert_int(excel_instance.CharacterWeaponLevelField(), password),
        "CharacterGearTier": convert_int(excel_instance.CharacterGearTierField(), password),
        "CharacterGearLevel": convert_int(excel_instance.CharacterGearLevelField(), password),
    }

def dump_ExcelDB_MiniGameDefenseInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DefenseBattleParcelType": ParcelType(convert_int(excel_instance.DefenseBattleParcelTypeField(), password)).name,
        "DefenseBattleParcelId": convert_int(excel_instance.DefenseBattleParcelIdField(), password),
        "DefenseBattleMultiplierMax": convert_int(excel_instance.DefenseBattleMultiplierMaxField(), password),
        "DisableRootMotion": bool(excel_instance.DisableRootMotionField()),
    }

def dump_ExcelDB_MiniGameDefenseStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficultyField(), password)).name,
        "StageDifficultyLocalize": convert_uint(excel_instance.StageDifficultyLocalizeField(), password),
        "StageNumber": convert_int(excel_instance.StageNumberField(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplayField(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageIdField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostTypeField(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostIdField(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmountField(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardIdField(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupIdField(j), password) for j in range(excel_instance.EnterScenarioGroupIdFieldLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupIdField(j), password) for j in range(excel_instance.ClearScenarioGroupIdFieldLength())],
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "GroundID": convert_int(excel_instance.GroundIDField(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoalField(j), password)).name for j in range(excel_instance.StarGoalFieldLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmountField(j), password) for j in range(excel_instance.StarGoalAmountFieldLength())],
        "DefenseFormationBGPrefab": convert_string(excel_instance.DefenseFormationBGPrefabField(), password),
        "DefenseFormationBGPrefabScale": convert_float(excel_instance.DefenseFormationBGPrefabScaleField(), password),
        "FixedEchelon": convert_int(excel_instance.FixedEchelonField(), password),
        "MininageDefenseFixedStatId": convert_int(excel_instance.MininageDefenseFixedStatIdField(), password),
        "StageHint": convert_uint(excel_instance.StageHintField(), password),
    }

def dump_ExcelDB_MiniGameDreamCollectionScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "IsSkip": bool(excel_instance.IsSkipField()),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "Parameter": [DreamMakerParameterType(convert_int(excel_instance.ParameterField(j), password)).name for j in range(excel_instance.ParameterFieldLength())],
        "ParameterAmount": [convert_int(excel_instance.ParameterAmountField(j), password) for j in range(excel_instance.ParameterAmountFieldLength())],
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
    }

def dump_ExcelDB_MiniGameDreamDailyPointExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "TotalParameterMin": convert_int(excel_instance.TotalParameterMinField(), password),
        "TotalParameterMax": convert_int(excel_instance.TotalParameterMaxField(), password),
        "DailyPointCoefficient": convert_int(excel_instance.DailyPointCoefficientField(), password),
        "DailyPointCorrectionValue": convert_int(excel_instance.DailyPointCorrectionValueField(), password),
    }

def dump_ExcelDB_MiniGameDreamEndingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EndingId": convert_int(excel_instance.EndingIdField(), password),
        "DreamMakerEndingType": DreamMakerEndingType(convert_int(excel_instance.DreamMakerEndingTypeField(), password)).name,
        "Order": convert_int(excel_instance.OrderField(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
        "EndingCondition": [DreamMakerEndingCondition(convert_int(excel_instance.EndingConditionField(j), password)).name for j in range(excel_instance.EndingConditionFieldLength())],
        "EndingConditionValue": [convert_int(excel_instance.EndingConditionValueField(j), password) for j in range(excel_instance.EndingConditionValueFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamEndingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EndingId": convert_int(excel_instance.EndingIdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "DreamMakerEndingRewardType": DreamMakerEndingRewardType(convert_int(excel_instance.DreamMakerEndingRewardTypeField(), password)).name,
        "DreamMakerEndingType": DreamMakerEndingType(convert_int(excel_instance.DreamMakerEndingTypeField(), password)).name,
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DreamMakerMultiplierCondition": DreamMakerMultiplierCondition(convert_int(excel_instance.DreamMakerMultiplierConditionField(), password)).name,
        "DreamMakerMultiplierConditionValue": convert_int(excel_instance.DreamMakerMultiplierConditionValueField(), password),
        "DreamMakerMultiplierMax": convert_int(excel_instance.DreamMakerMultiplierMaxField(), password),
        "DreamMakerDays": convert_int(excel_instance.DreamMakerDaysField(), password),
        "DreamMakerActionPoint": convert_int(excel_instance.DreamMakerActionPointField(), password),
        "DreamMakerParcelType": ParcelType(convert_int(excel_instance.DreamMakerParcelTypeField(), password)).name,
        "DreamMakerParcelId": convert_int(excel_instance.DreamMakerParcelIdField(), password),
        "DreamMakerDailyPointParcelType": ParcelType(convert_int(excel_instance.DreamMakerDailyPointParcelTypeField(), password)).name,
        "DreamMakerDailyPointId": convert_int(excel_instance.DreamMakerDailyPointIdField(), password),
        "DreamMakerParameterTransfer": convert_int(excel_instance.DreamMakerParameterTransferField(), password),
        "ScheduleCostGoodsId": convert_int(excel_instance.ScheduleCostGoodsIdField(), password),
        "LobbyBGMChangeScenarioId": convert_int(excel_instance.LobbyBGMChangeScenarioIdField(), password),
    }

def dump_ExcelDB_MiniGameDreamParameterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ParameterType": DreamMakerParameterType(convert_int(excel_instance.ParameterTypeField(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "ParameterBase": convert_int(excel_instance.ParameterBaseField(), password),
        "ParameterBaseMax": convert_int(excel_instance.ParameterBaseMaxField(), password),
        "ParameterMin": convert_int(excel_instance.ParameterMinField(), password),
        "ParameterMax": convert_int(excel_instance.ParameterMaxField(), password),
    }

def dump_ExcelDB_MiniGameDreamReplayScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
        "Order": convert_int(excel_instance.OrderField(), password),
        "ReplaySummaryTitleLocalize": convert_uint(excel_instance.ReplaySummaryTitleLocalizeField(), password),
        "ReplaySummaryLocalizeScenarioId": convert_uint(excel_instance.ReplaySummaryLocalizeScenarioIdField(), password),
        "ReplayScenarioResource": convert_string(excel_instance.ReplayScenarioResourceField(), password),
        "IsReplayScenarioHorizon": bool(excel_instance.IsReplayScenarioHorizonField()),
    }

def dump_ExcelDB_MiniGameDreamScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DreamMakerScheduleGroupId": convert_int(excel_instance.DreamMakerScheduleGroupIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "LoadingResource01": convert_string(excel_instance.LoadingResource01Field(), password),
        "LoadingResource02": convert_string(excel_instance.LoadingResource02Field(), password),
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
    }

def dump_ExcelDB_MiniGameDreamScheduleResultExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "DreamMakerResult": DreamMakerResult(convert_int(excel_instance.DreamMakerResultField(), password)).name,
        "DreamMakerScheduleGroup": convert_int(excel_instance.DreamMakerScheduleGroupField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "RewardParameter": [DreamMakerParameterType(convert_int(excel_instance.RewardParameterField(j), password)).name for j in range(excel_instance.RewardParameterFieldLength())],
        "RewardParameterOperationType": [DreamMakerParamOperationType(convert_int(excel_instance.RewardParameterOperationTypeField(j), password)).name for j in range(excel_instance.RewardParameterOperationTypeFieldLength())],
        "RewardParameterAmount": [convert_int(excel_instance.RewardParameterAmountField(j), password) for j in range(excel_instance.RewardParameterAmountFieldLength())],
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_MiniGameDreamTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "DreamMakerDays": convert_int(excel_instance.DreamMakerDaysField(), password),
        "DreamMakerActionPoint": convert_int(excel_instance.DreamMakerActionPointField(), password),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupIdField(), password),
        "Bgm": convert_int(excel_instance.BgmField(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPathField(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPathField(), password),
    }

def dump_ExcelDB_MinigameDreamVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "VoiceCondition": DreamMakerVoiceCondition(convert_int(excel_instance.VoiceConditionField(), password)).name,
        "VoiceClip": convert_uint(excel_instance.VoiceClipField(), password),
    }

def dump_ExcelDB_MiniGameMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "GroupName": convert_string(excel_instance.GroupNameField(), password),
        "Category": MissionCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetTypeField(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayTypeField(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePathField(), password),
        "ViewFlag": bool(excel_instance.ViewFlagField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionIdField(j), password) for j in range(excel_instance.PreMissionIdFieldLength())],
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "AccountLevel": convert_int(excel_instance.AccountLevelField(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUIField(j), password) for j in range(excel_instance.ShortcutUIFieldLength())],
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionTypeField(), password)).name,
        "IsCompleteExtensionTime": bool(excel_instance.IsCompleteExtensionTimeField()),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCountField(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameterField(j), password) for j in range(excel_instance.CompleteConditionParameterFieldLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTagField(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagFieldLength())],
        "RewardIcon": convert_string(excel_instance.RewardIconField(), password),
        "CompleteConditionMissionId": [convert_int(excel_instance.CompleteConditionMissionIdField(j), password) for j in range(excel_instance.CompleteConditionMissionIdFieldLength())],
        "CompleteConditionMissionCount": convert_int(excel_instance.CompleteConditionMissionCountField(), password),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelTypeField(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeFieldLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelIdField(j), password) for j in range(excel_instance.MissionRewardParcelIdFieldLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmountField(j), password) for j in range(excel_instance.MissionRewardAmountFieldLength())],
        "ConditionRewardParcelType": [ParcelType(convert_int(excel_instance.ConditionRewardParcelTypeField(j), password)).name for j in range(excel_instance.ConditionRewardParcelTypeFieldLength())],
        "ConditionRewardParcelId": [convert_int(excel_instance.ConditionRewardParcelIdField(j), password) for j in range(excel_instance.ConditionRewardParcelIdFieldLength())],
        "ConditionRewardAmount": [convert_int(excel_instance.ConditionRewardAmountField(j), password) for j in range(excel_instance.ConditionRewardAmountFieldLength())],
    }

def dump_ExcelDB_MiniGamePlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "MiniGameType": EventContentType(convert_int(excel_instance.MiniGameTypeField(), password)).name,
        "IsPcBuild": bool(excel_instance.IsPcBuildField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitleField(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePathField(), password),
        "GuideText": convert_string(excel_instance.GuideTextField(), password),
    }

def dump_ExcelDB_MiniGameRhythmBgmExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RhythmBgmId": convert_int(excel_instance.RhythmBgmIdField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "StageSelectImagePath": convert_string(excel_instance.StageSelectImagePathField(), password),
        "Bpm": convert_int(excel_instance.BpmField(), password),
        "Bgm": convert_int(excel_instance.BgmField(), password),
        "BgmNameText": convert_string(excel_instance.BgmNameTextField(), password),
        "BgmArtistText": convert_string(excel_instance.BgmArtistTextField(), password),
        "HasLyricist": bool(excel_instance.HasLyricistField()),
        "BgmComposerText": convert_string(excel_instance.BgmComposerTextField(), password),
        "BgmLength": convert_int(excel_instance.BgmLengthField(), password),
    }

def dump_ExcelDB_MiniGameRhythmExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "RhythmBgmId": convert_int(excel_instance.RhythmBgmIdField(), password),
        "PresetName": convert_string(excel_instance.PresetNameField(), password),
        "StageDifficulty": Difficulty(convert_int(excel_instance.StageDifficultyField(), password)).name,
        "IsSpecial": bool(excel_instance.IsSpecialField()),
        "OpenStageScoreAmount": convert_int(excel_instance.OpenStageScoreAmountField(), password),
        "MaxHp": convert_int(excel_instance.MaxHpField(), password),
        "MissDamage": convert_int(excel_instance.MissDamageField(), password),
        "CriticalHPRestoreValue": convert_int(excel_instance.CriticalHPRestoreValueField(), password),
        "MaxScore": convert_int(excel_instance.MaxScoreField(), password),
        "FeverScoreRate": convert_int(excel_instance.FeverScoreRateField(), password),
        "NoteScoreRate": convert_int(excel_instance.NoteScoreRateField(), password),
        "ComboScoreRate": convert_int(excel_instance.ComboScoreRateField(), password),
        "AttackScoreRate": convert_int(excel_instance.AttackScoreRateField(), password),
        "FeverCriticalRate": convert_float(excel_instance.FeverCriticalRateField(), password),
        "FeverAttackRate": convert_float(excel_instance.FeverAttackRateField(), password),
        "MaxHpScore": convert_int(excel_instance.MaxHpScoreField(), password),
        "RhythmFileName": convert_string(excel_instance.RhythmFileNameField(), password),
        "ArtLevelSceneName": convert_string(excel_instance.ArtLevelSceneNameField(), password),
        "ComboImagePath": convert_string(excel_instance.ComboImagePathField(), password),
    }

def dump_ExcelDB_MiniGameRoadPuzzleAdditionalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_MiniGameRoadPuzzleInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventUseCostType": ParcelType(convert_int(excel_instance.EventUseCostTypeField(), password)).name,
        "EventUseCostId": convert_int(excel_instance.EventUseCostIdField(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsIdField(), password),
        "RailSetRewardId": convert_int(excel_instance.RailSetRewardIdField(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRoundField(), password),
    }

def dump_ExcelDB_MinigameRoadPuzzleMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "MapGroupId": convert_int(excel_instance.MapGroupIdField(), password),
        "Map": convert_string(excel_instance.MapField(), password),
        "MapBG": convert_string(excel_instance.MapBGField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "AvailableRailTile": [convert_int(excel_instance.AvailableRailTileField(j), password) for j in range(excel_instance.AvailableRailTileFieldLength())],
        "AvailableRailTileAmount": [convert_int(excel_instance.AvailableRailTileAmountField(j), password) for j in range(excel_instance.AvailableRailTileAmountFieldLength())],
        "OriginalTileCount": [convert_int(excel_instance.OriginalTileCountField(j), password) for j in range(excel_instance.OriginalTileCountFieldLength())],
        "TrainSpeed": convert_float(excel_instance.TrainSpeedField(), password),
    }

def dump_ExcelDB_MinigameRoadPuzzleMapTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "MapTileType": RoadPuzzleMapTileType(convert_int(excel_instance.MapTileTypeField(), password)).name,
    }

def dump_ExcelDB_MiniGameRoadPuzzleRailSetRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "LocalizePrefabID": convert_string(excel_instance.LocalizePrefabIDField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_MinigameRoadPuzzleRailTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "OriginalTile": bool(excel_instance.OriginalTileField()),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "RailTileType": RoadPuzzleRailTileType(convert_int(excel_instance.RailTileTypeField(), password)).name,
    }

def dump_ExcelDB_MiniGameRoadPuzzleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_MinigameRoadPuzzleRoadRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "Round": convert_int(excel_instance.RoundField(), password),
        "IsLoop": bool(excel_instance.IsLoopField()),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupIdField(), password),
        "EndScenarioGroupId": convert_int(excel_instance.EndScenarioGroupIdField(), password),
        "MapGroupId": convert_int(excel_instance.MapGroupIdField(), password),
        "RoundReward": convert_int(excel_instance.RoundRewardField(), password),
        "AdditionalRewardID": [convert_int(excel_instance.AdditionalRewardIDField(j), password) for j in range(excel_instance.AdditionalRewardIDFieldLength())],
        "AdditionalRewardAmount": [convert_int(excel_instance.AdditionalRewardAmountField(j), password) for j in range(excel_instance.AdditionalRewardAmountFieldLength())],
    }

def dump_ExcelDB_MiniGameRoadPuzzleVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "VoiceCondition": RoadPuzzleVoiceCondition(convert_int(excel_instance.VoiceConditionField(), password)).name,
        "VoiceClip": convert_uint(excel_instance.VoiceClipField(), password),
    }

def dump_ExcelDB_MiniGameShootingCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceNameField(), password),
        "BodyRadius": convert_float(excel_instance.BodyRadiusField(), password),
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabNameField(), password),
        "NormalAttackSkillData": convert_string(excel_instance.NormalAttackSkillDataField(), password),
        "PublicSkillData": [convert_string(excel_instance.PublicSkillDataField(j), password) for j in range(excel_instance.PublicSkillDataFieldLength())],
        "DeathSkillData": convert_string(excel_instance.DeathSkillDataField(), password),
        "MaxHP": convert_int(excel_instance.MaxHPField(), password),
        "AttackPower": convert_int(excel_instance.AttackPowerField(), password),
        "DefensePower": convert_int(excel_instance.DefensePowerField(), password),
        "CriticalRate": convert_int(excel_instance.CriticalRateField(), password),
        "CriticalDamageRate": convert_int(excel_instance.CriticalDamageRateField(), password),
        "AttackRange": convert_int(excel_instance.AttackRangeField(), password),
        "MoveSpeed": convert_int(excel_instance.MoveSpeedField(), password),
        "ShotTime": convert_int(excel_instance.ShotTimeField(), password),
        "IsBoss": bool(excel_instance.IsBossField()),
        "Scale": convert_float(excel_instance.ScaleField(), password),
        "IgnoreObstacleCheck": bool(excel_instance.IgnoreObstacleCheckField()),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupIdField(), password),
    }

def dump_ExcelDB_MiniGameShootingGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "GeasType": Geas(convert_int(excel_instance.GeasTypeField(), password)).name,
        "Icon": convert_string(excel_instance.IconField(), password),
        "Probability": convert_int(excel_instance.ProbabilityField(), password),
        "MaxOverlapCount": convert_int(excel_instance.MaxOverlapCountField(), password),
        "GeasData": convert_string(excel_instance.GeasDataField(), password),
        "NeedGeasId": convert_int(excel_instance.NeedGeasIdField(), password),
        "HideInPausePopup": bool(excel_instance.HideInPausePopupField()),
    }

def dump_ExcelDB_MiniGameShootingStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "BgmId": [convert_int(excel_instance.BgmIdField(j), password) for j in range(excel_instance.BgmIdFieldLength())],
        "CostGoodsId": convert_int(excel_instance.CostGoodsIdField(), password),
        "Difficulty": Difficulty(convert_int(excel_instance.DifficultyField(), password)).name,
        "DesignLevel": convert_string(excel_instance.DesignLevelField(), password),
        "ArtLevel": convert_string(excel_instance.ArtLevelField(), password),
        "StartBattleDuration": convert_int(excel_instance.StartBattleDurationField(), password),
        "DefaultBattleDuration": convert_int(excel_instance.DefaultBattleDurationField(), password),
        "DefaultLogicEffect": convert_string(excel_instance.DefaultLogicEffectField(), password),
        "CameraSizeRate": convert_float(excel_instance.CameraSizeRateField(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardIdField(), password),
    }

def dump_ExcelDB_MiniGameShootingStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "ClearSection": convert_int(excel_instance.ClearSectionField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_MinigameTBGDiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "DiceGroup": convert_int(excel_instance.DiceGroupField(), password),
        "DiceResult": convert_int(excel_instance.DiceResultField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "ProbModifyCondition": [TBGProbModifyCondition(convert_int(excel_instance.ProbModifyConditionField(j), password)).name for j in range(excel_instance.ProbModifyConditionFieldLength())],
        "ProbModifyValue": [convert_int(excel_instance.ProbModifyValueField(j), password) for j in range(excel_instance.ProbModifyValueFieldLength())],
        "ProbModifyLimit": [convert_int(excel_instance.ProbModifyLimitField(j), password) for j in range(excel_instance.ProbModifyLimitFieldLength())],
    }

def dump_ExcelDB_MinigameTBGEncounterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "AllThema": bool(excel_instance.AllThemaField()),
        "ThemaIndex": convert_int(excel_instance.ThemaIndexField(), password),
        "ThemaType": TBGThemaType(convert_int(excel_instance.ThemaTypeField(), password)).name,
        "ObjectType": TBGObjectType(convert_int(excel_instance.ObjectTypeField(), password)).name,
        "EnemyImagePath": convert_string(excel_instance.EnemyImagePathField(), password),
        "EnemyPrefabName": convert_string(excel_instance.EnemyPrefabNameField(), password),
        "EnemyNameLocalize": convert_string(excel_instance.EnemyNameLocalizeField(), password),
        "OptionGroupId": convert_int(excel_instance.OptionGroupIdField(), password),
        "RewardHide": bool(excel_instance.RewardHideField()),
        "EncounterTitleLocalize": convert_string(excel_instance.EncounterTitleLocalizeField(), password),
        "StoryImagePath": convert_string(excel_instance.StoryImagePathField(), password),
        "BeforeStoryLocalize": convert_string(excel_instance.BeforeStoryLocalizeField(), password),
        "BeforeStoryOption1Localize": convert_string(excel_instance.BeforeStoryOption1LocalizeField(), password),
        "BeforeStoryOption2Localize": convert_string(excel_instance.BeforeStoryOption2LocalizeField(), password),
        "BeforeStoryOption3Localize": convert_string(excel_instance.BeforeStoryOption3LocalizeField(), password),
        "AllyAttackLocalize": convert_string(excel_instance.AllyAttackLocalizeField(), password),
        "EnemyAttackLocalize": convert_string(excel_instance.EnemyAttackLocalizeField(), password),
        "AttackDefenceLocalize": convert_string(excel_instance.AttackDefenceLocalizeField(), password),
        "ClearStoryLocalize": convert_string(excel_instance.ClearStoryLocalizeField(), password),
        "DefeatStoryLocalize": convert_string(excel_instance.DefeatStoryLocalizeField(), password),
        "RunawayStoryLocalize": convert_string(excel_instance.RunawayStoryLocalizeField(), password),
    }

def dump_ExcelDB_MinigameTBGEncounterOptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OptionGroupId": convert_int(excel_instance.OptionGroupIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "SlotIndex": convert_int(excel_instance.SlotIndexField(), password),
        "OptionTitleLocalize": convert_string(excel_instance.OptionTitleLocalizeField(), password),
        "OptionSuccessLocalize": convert_string(excel_instance.OptionSuccessLocalizeField(), password),
        "OptionSuccessRewardGroupId": convert_int(excel_instance.OptionSuccessRewardGroupIdField(), password),
        "OptionSuccessOrHigherDiceCount": convert_int(excel_instance.OptionSuccessOrHigherDiceCountField(), password),
        "OptionGreatSuccessOrHigherDiceCount": convert_int(excel_instance.OptionGreatSuccessOrHigherDiceCountField(), password),
        "OptionFailLocalize": convert_string(excel_instance.OptionFailLocalizeField(), password),
        "OptionFailLessDiceCount": convert_int(excel_instance.OptionFailLessDiceCountField(), password),
        "RunawayOrHigherDiceCount": convert_int(excel_instance.RunawayOrHigherDiceCountField(), password),
        "RewardHide": bool(excel_instance.RewardHideField()),
    }

def dump_ExcelDB_MinigameTBGEncounterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "TBGOptionSuccessType": TBGOptionSuccessType(convert_int(excel_instance.TBGOptionSuccessTypeField(), password)).name,
        "Paremeter": convert_int(excel_instance.ParemeterField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelIdField(), password),
        "Amount": convert_int(excel_instance.AmountField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
    }

def dump_ExcelDB_MinigameTBGItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "ItemType": TBGItemType(convert_int(excel_instance.ItemTypeField(), password)).name,
        "TBGItemEffectType": TBGItemEffectType(convert_int(excel_instance.TBGItemEffectTypeField(), password)).name,
        "ItemParameter": convert_int(excel_instance.ItemParameterField(), password),
        "LocalizeETCId": convert_string(excel_instance.LocalizeETCIdField(), password),
        "Icon": convert_string(excel_instance.IconField(), password),
        "BuffIcon": convert_string(excel_instance.BuffIconField(), password),
        "EncounterCount": convert_int(excel_instance.EncounterCountField(), password),
        "DiceEffectAniClip": convert_string(excel_instance.DiceEffectAniClipField(), password),
        "BuffIconHUDVisible": bool(excel_instance.BuffIconHUDVisibleField()),
    }

def dump_ExcelDB_MinigameTBGObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "Key": convert_string(excel_instance.KeyField(), password),
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "ObjectType": TBGObjectType(convert_int(excel_instance.ObjectTypeField(), password)).name,
        "ObjectCostType": ParcelType(convert_int(excel_instance.ObjectCostTypeField(), password)).name,
        "ObjectCostId": convert_int(excel_instance.ObjectCostIdField(), password),
        "ObjectCostAmount": convert_int(excel_instance.ObjectCostAmountField(), password),
        "Disposable": bool(excel_instance.DisposableField()),
        "ReEncounterCost": bool(excel_instance.ReEncounterCostField()),
    }

def dump_ExcelDB_MinigameTBGSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ItemSlot": convert_int(excel_instance.ItemSlotField(), password),
        "DefaultEchelonHp": convert_int(excel_instance.DefaultEchelonHpField(), password),
        "DefaultItemDiceId": convert_int(excel_instance.DefaultItemDiceIdField(), password),
        "EchelonSlot1CharacterId": convert_int(excel_instance.EchelonSlot1CharacterIdField(), password),
        "EchelonSlot2CharacterId": convert_int(excel_instance.EchelonSlot2CharacterIdField(), password),
        "EchelonSlot3CharacterId": convert_int(excel_instance.EchelonSlot3CharacterIdField(), password),
        "EchelonSlot4CharacterId": convert_int(excel_instance.EchelonSlot4CharacterIdField(), password),
        "EchelonSlot1Portrait": convert_string(excel_instance.EchelonSlot1PortraitField(), password),
        "EchelonSlot2Portrait": convert_string(excel_instance.EchelonSlot2PortraitField(), password),
        "EchelonSlot3Portrait": convert_string(excel_instance.EchelonSlot3PortraitField(), password),
        "EchelonSlot4Portrait": convert_string(excel_instance.EchelonSlot4PortraitField(), password),
        "EventUseCostType": ParcelType(convert_int(excel_instance.EventUseCostTypeField(), password)).name,
        "EventUseCostId": convert_int(excel_instance.EventUseCostIdField(), password),
        "EchelonRevivalCostType": ParcelType(convert_int(excel_instance.EchelonRevivalCostTypeField(), password)).name,
        "EchelonRevivalCostId": convert_int(excel_instance.EchelonRevivalCostIdField(), password),
        "EchelonRevivalCostAmount": convert_int(excel_instance.EchelonRevivalCostAmountField(), password),
        "EnemyBossHP": convert_int(excel_instance.EnemyBossHPField(), password),
        "EnemyMinionHP": convert_int(excel_instance.EnemyMinionHPField(), password),
        "AttackDamage": convert_int(excel_instance.AttackDamageField(), password),
        "CriticalAttackDamage": convert_int(excel_instance.CriticalAttackDamageField(), password),
        "RoundItemSelectLimit": convert_int(excel_instance.RoundItemSelectLimitField(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRoundField(), password),
        "MaxHp": convert_int(excel_instance.MaxHpField(), password),
        "MapImagePath": convert_string(excel_instance.MapImagePathField(), password),
        "MapNameLocalize": convert_string(excel_instance.MapNameLocalizeField(), password),
        "StartThemaIndex": convert_int(excel_instance.StartThemaIndexField(), password),
        "LoopThemaIndex": convert_int(excel_instance.LoopThemaIndexField(), password),
        "MaxDicePlus": convert_int(excel_instance.MaxDicePlusField(), password),
    }

def dump_ExcelDB_MinigameTBGThemaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "ThemaIndex": convert_int(excel_instance.ThemaIndexField(), password),
        "ThemaType": TBGThemaType(convert_int(excel_instance.ThemaTypeField(), password)).name,
        "ThemaMap": convert_string(excel_instance.ThemaMapField(), password),
        "ThemaMapBG": convert_string(excel_instance.ThemaMapBGField(), password),
        "PortalCondition": [TBGPortalCondition(convert_int(excel_instance.PortalConditionField(j), password)).name for j in range(excel_instance.PortalConditionFieldLength())],
        "PortalConditionParameter": [convert_string(excel_instance.PortalConditionParameterField(j), password) for j in range(excel_instance.PortalConditionParameterFieldLength())],
        "ThemaNameLocalize": convert_string(excel_instance.ThemaNameLocalizeField(), password),
        "ThemaLoadingImage": convert_string(excel_instance.ThemaLoadingImageField(), password),
        "ThemaPlayerPrefab": convert_string(excel_instance.ThemaPlayerPrefabField(), password),
        "ThemaLeaderId": convert_int(excel_instance.ThemaLeaderIdField(), password),
        "ThemaGoalLocalize": convert_string(excel_instance.ThemaGoalLocalizeField(), password),
        "InstantClearCostAmount": convert_int(excel_instance.InstantClearCostAmountField(), password),
        "IsTutorial": bool(excel_instance.IsTutorialField()),
    }

def dump_ExcelDB_MiniGameTBGThemaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "ThemaRound": convert_int(excel_instance.ThemaRoundField(), password),
        "ThemaUniqueId": convert_int(excel_instance.ThemaUniqueIdField(), password),
        "IsLoop": bool(excel_instance.IsLoopField()),
        "MiniGameTBGThemaRewardType": MiniGameTBGThemaRewardType(convert_int(excel_instance.MiniGameTBGThemaRewardTypeField(), password)).name,
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_MinigameTBGVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "VoiceCondition": TBGVoiceCondition(convert_int(excel_instance.VoiceConditionField(), password)).name,
        "VoiceId": convert_uint(excel_instance.VoiceIdField(), password),
    }

def dump_ExcelDB_MissionEmergencyCompleteExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MissionId": convert_int(excel_instance.MissionIdField(), password),
        "EmergencyComplete": bool(excel_instance.EmergencyCompleteField()),
    }

def dump_ExcelDB_MissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Category": MissionCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetTypeField(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayTypeField(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePathField(), password),
        "ViewFlag": bool(excel_instance.ViewFlagField()),
        "Limit": bool(excel_instance.LimitField()),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "EndDay": convert_int(excel_instance.EndDayField(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDateField(), password),
        "DateAutoRefer": ContentType(convert_int(excel_instance.DateAutoReferField(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionIdField(j), password) for j in range(excel_instance.PreMissionIdFieldLength())],
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "AccountLevel": convert_int(excel_instance.AccountLevelField(), password),
        "ContentTags": [SuddenMissionContentType(convert_int(excel_instance.ContentTagsField(j), password)).name for j in range(excel_instance.ContentTagsFieldLength())],
        "ShortcutUI": [convert_string(excel_instance.ShortcutUIField(j), password) for j in range(excel_instance.ShortcutUIFieldLength())],
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcutField(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionTypeField(), password)).name,
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCountField(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameterField(j), password) for j in range(excel_instance.CompleteConditionParameterFieldLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTagField(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagFieldLength())],
        "RewardIcon": convert_string(excel_instance.RewardIconField(), password),
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelTypeField(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeFieldLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelIdField(j), password) for j in range(excel_instance.MissionRewardParcelIdFieldLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmountField(j), password) for j in range(excel_instance.MissionRewardAmountFieldLength())],
    }

def dump_ExcelDB_MomotalkScheduleSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleIdField(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitleField(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescriptionField(), password),
        "PopupType": SpoilerPopupType(convert_int(excel_instance.PopupTypeField(), password)).name,
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeIdField(), password),
    }

def dump_ExcelDB_MultiFloorRaidRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RewardGroupId": convert_int(excel_instance.RewardGroupIdField(), password),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProbField(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelTypeField(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueIDField(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmountField(), password),
    }

def dump_ExcelDB_MultiFloorRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "LobbyEnterScenario": convert_uint(excel_instance.LobbyEnterScenarioField(), password),
        "ShowLobbyBanner": bool(excel_instance.ShowLobbyBannerField()),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDateField(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDateField(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDateField(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDateField(), password),
        "OpenRaidBossGroupId": convert_string(excel_instance.OpenRaidBossGroupIdField(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKeyField(), password),
        "LobbyImgPath": convert_string(excel_instance.LobbyImgPathField(), password),
        "LevelImgPath": convert_string(excel_instance.LevelImgPathField(), password),
        "PlayTip": convert_string(excel_instance.PlayTipField(), password),
    }

def dump_ExcelDB_MultiFloorRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
        "BossGroupId": convert_string(excel_instance.BossGroupIdField(), password),
        "AssistSlot": convert_int(excel_instance.AssistSlotField(), password),
        "StageOpenCondition": convert_int(excel_instance.StageOpenConditionField(), password),
        "FloorListSection": bool(excel_instance.FloorListSectionField()),
        "FloorListSectionOpenCondition": convert_int(excel_instance.FloorListSectionOpenConditionField(), password),
        "FloorListSectionLabel": convert_uint(excel_instance.FloorListSectionLabelField(), password),
        "Difficulty": convert_int(excel_instance.DifficultyField(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndexField()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSyncField()),
        "FloorListImgPath": convert_string(excel_instance.FloorListImgPathField(), password),
        "FloorImgPath": convert_string(excel_instance.FloorImgPathField(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterIdField(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterIdField(j), password) for j in range(excel_instance.BossCharacterIdFieldLength())],
        "StatChangeId": [convert_int(excel_instance.StatChangeIdField(j), password) for j in range(excel_instance.StatChangeIdFieldLength())],
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevelField(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupIdField(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePathField(j), password) for j in range(excel_instance.BattleReadyTimelinePathFieldLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStartField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartFieldLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEndField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndFieldLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePathField(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCardField()),
    }

def dump_ExcelDB_MultiFloorRaidStatChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StatChangeId": convert_int(excel_instance.StatChangeIdField(), password),
        "StatType": [StatType(convert_int(excel_instance.StatTypeField(j), password)).name for j in range(excel_instance.StatTypeFieldLength())],
        "StatAdd": [convert_int(excel_instance.StatAddField(j), password) for j in range(excel_instance.StatAddFieldLength())],
        "StatMultiply": [convert_int(excel_instance.StatMultiplyField(j), password) for j in range(excel_instance.StatMultiplyFieldLength())],
        "ApplyCharacterId": [convert_int(excel_instance.ApplyCharacterIdField(j), password) for j in range(excel_instance.ApplyCharacterIdFieldLength())],
    }

def dump_ExcelDB_ObstacleFireLineCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MyObstacleFireLineCheck": bool(excel_instance.MyObstacleFireLineCheckField()),
        "AllyObstacleFireLineCheck": bool(excel_instance.AllyObstacleFireLineCheckField()),
        "EnemyObstacleFireLineCheck": bool(excel_instance.EnemyObstacleFireLineCheckField()),
        "EmptyObstacleFireLineCheck": bool(excel_instance.EmptyObstacleFireLineCheckField()),
    }

def dump_ExcelDB_ObstacleStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringIDField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "MaxHP1": convert_int(excel_instance.MaxHP1Field(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100Field(), password),
        "BlockRate": convert_int(excel_instance.BlockRateField(), password),
        "Dodge": convert_int(excel_instance.DodgeField(), password),
        "CanNotStandRange": convert_int(excel_instance.CanNotStandRangeField(), password),
        "HighlightFloaterHeight": convert_float(excel_instance.HighlightFloaterHeightField(), password),
        "EnhanceLightArmorRate": convert_int(excel_instance.EnhanceLightArmorRateField(), password),
        "EnhanceHeavyArmorRate": convert_int(excel_instance.EnhanceHeavyArmorRateField(), password),
        "EnhanceUnarmedRate": convert_int(excel_instance.EnhanceUnarmedRateField(), password),
        "EnhanceElasticArmorRate": convert_int(excel_instance.EnhanceElasticArmorRateField(), password),
        "EnhanceCompositeArmorRate": convert_int(excel_instance.EnhanceCompositeArmorRateField(), password),
        "EnhanceStructureRate": convert_int(excel_instance.EnhanceStructureRateField(), password),
        "EnhanceNormalArmorRate": convert_int(excel_instance.EnhanceNormalArmorRateField(), password),
        "ReduceExDamagedRate": convert_int(excel_instance.ReduceExDamagedRateField(), password),
        "ReduceBasicsDamagedRate": convert_int(excel_instance.ReduceBasicsDamagedRateField(), password),
        "ReduceWeakDamagedRate": convert_int(excel_instance.ReduceWeakDamagedRateField(), password),
        "WeakDamagedRatio": convert_int(excel_instance.WeakDamagedRatioField(), password),
        "EffectiveDamagedRatio": convert_int(excel_instance.EffectiveDamagedRatioField(), password),
        "NormalDamagedRatio": convert_int(excel_instance.NormalDamagedRatioField(), password),
        "ResistDamagedRatio": convert_int(excel_instance.ResistDamagedRatioField(), password),
    }

def dump_ExcelDB_OpenConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OpenConditionContentType": OpenConditionContent(convert_int(excel_instance.OpenConditionContentTypeField(), password)).name,
        "LockUI": [convert_string(excel_instance.LockUIField(j), password) for j in range(excel_instance.LockUIFieldLength())],
        "ShortcutPopupPriority": convert_int(excel_instance.ShortcutPopupPriorityField(), password),
        "ShortcutUIName": [convert_string(excel_instance.ShortcutUINameField(j), password) for j in range(excel_instance.ShortcutUINameFieldLength())],
        "ShortcutParam": convert_int(excel_instance.ShortcutParamField(), password),
        "Scene": convert_string(excel_instance.SceneField(), password),
        "HideWhenLocked": bool(excel_instance.HideWhenLockedField()),
        "AccountLevel": convert_int(excel_instance.AccountLevelField(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeIdField(), password),
        "CampaignStageId": convert_int(excel_instance.CampaignStageIdField(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckTypeField(), password)).name,
        "OpenDayOfWeek": WeekDay(convert_int(excel_instance.OpenDayOfWeekField(), password)).name,
        "OpenHour": convert_int(excel_instance.OpenHourField(), password),
        "CloseDayOfWeek": WeekDay(convert_int(excel_instance.CloseDayOfWeekField(), password)).name,
        "CloseHour": convert_int(excel_instance.CloseHourField(), password),
        "OpenedCafeId": convert_int(excel_instance.OpenedCafeIdField(), password),
        "CafeIdforCafeRank": convert_int(excel_instance.CafeIdforCafeRankField(), password),
        "CafeRank": convert_int(excel_instance.CafeRankField(), password),
        "ContentsOpenShow": bool(excel_instance.ContentsOpenShowField()),
        "ContentsOpenShortcutUI": convert_string(excel_instance.ContentsOpenShortcutUIField(), password),
    }

def dump_ExcelDB_OperatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "GroupId": convert_string(excel_instance.GroupIdField(), password),
        "OperatorCondition": OperatorCondition(convert_int(excel_instance.OperatorConditionField(), password)).name,
        "OutputSequence": convert_int(excel_instance.OutputSequenceField(), password),
        "RandomWeight": convert_int(excel_instance.RandomWeightField(), password),
        "OutputDelay": convert_int(excel_instance.OutputDelayField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "OperatorOutputPriority": convert_int(excel_instance.OperatorOutputPriorityField(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPathField(), password),
        "TextLocalizeKey": convert_string(excel_instance.TextLocalizeKeyField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "OperatorWaitQueue": bool(excel_instance.OperatorWaitQueueField()),
        "CharacterVoiceOverridePriority": CharacterVoiceOverridePriority(convert_int(excel_instance.CharacterVoiceOverridePriorityField(), password)).name,
    }

def dump_ExcelDB_ParcelAutoSynthExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RequireParcelType": ParcelType(convert_int(excel_instance.RequireParcelTypeField(), password)).name,
        "RequireParcelId": convert_int(excel_instance.RequireParcelIdField(), password),
        "RequireParcelAmount": convert_int(excel_instance.RequireParcelAmountField(), password),
        "SynthStartAmount": convert_int(excel_instance.SynthStartAmountField(), password),
        "SynthEndAmount": convert_int(excel_instance.SynthEndAmountField(), password),
        "SynthMaxItem": bool(excel_instance.SynthMaxItemField()),
        "ResultParcelType": ParcelType(convert_int(excel_instance.ResultParcelTypeField(), password)).name,
        "ResultParcelId": convert_int(excel_instance.ResultParcelIdField(), password),
        "ResultParcelAmount": convert_int(excel_instance.ResultParcelAmountField(), password),
    }

def dump_ExcelDB_PermanentRaidManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Type": RaidBossGroupType(convert_int(excel_instance.TypeField(), password)).name,
        "OpenRaidBossGroup": [convert_string(excel_instance.OpenRaidBossGroupField(j), password) for j in range(excel_instance.OpenRaidBossGroupFieldLength())],
        "HideDifficulty": [convert_string(excel_instance.HideDifficultyField(j), password) for j in range(excel_instance.HideDifficultyFieldLength())],
        "OpenDate": convert_string(excel_instance.OpenDateField(), password),
    }

def dump_ExcelDB_PersonalityExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
    }

def dump_ExcelDB_PickupDuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ShopCategoryType": convert_float(excel_instance.ShopCategoryTypeField(), password),
        "ShopId": convert_int(excel_instance.ShopIdField(), password),
        "PickupCharacterId": convert_int(excel_instance.PickupCharacterIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_PickupFirstGetBonus2Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ShopRecruitId": convert_int(excel_instance.ShopRecruitIdField(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopIdField(), password),
        "PickupCharacterId": convert_int(excel_instance.PickupCharacterIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_PickupFirstGetBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ShopRecruitId": convert_int(excel_instance.ShopRecruitIdField(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopIdField(), password),
        "PickupCharacterId": convert_int(excel_instance.PickupCharacterIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
    }

def dump_ExcelDB_PossessionCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "DefaultParcelType": ParcelType(convert_int(excel_instance.DefaultParcelTypeField(), password)).name,
        "DefaultParcelId": convert_int(excel_instance.DefaultParcelIdField(), password),
        "DefaultParcelAmount": convert_int(excel_instance.DefaultParcelAmountField(), password),
        "ReplaceParcelType": ParcelType(convert_int(excel_instance.ReplaceParcelTypeField(), password)).name,
        "ReplaceParcelId": convert_int(excel_instance.ReplaceParcelIdField(), password),
        "ReplaceParcelAmount": convert_int(excel_instance.ReplaceParcelAmountField(), password),
    }

def dump_ExcelDB_PresetCharacterGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PresetCharacterGroupId": convert_int(excel_instance.PresetCharacterGroupIdField(), password),
        "GetPresetType": convert_string(excel_instance.GetPresetTypeField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "Exp": convert_int(excel_instance.ExpField(), password),
        "FavorExp": convert_int(excel_instance.FavorExpField(), password),
        "FavorRank": convert_int(excel_instance.FavorRankField(), password),
        "StarGrade": convert_int(excel_instance.StarGradeField(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevelField(), password),
        "PassiveSkillLevel": convert_int(excel_instance.PassiveSkillLevelField(), password),
        "ExtraPassiveSkillLevel": convert_int(excel_instance.ExtraPassiveSkillLevelField(), password),
        "CommonSkillLevel": convert_int(excel_instance.CommonSkillLevelField(), password),
        "LeaderSkillLevel": convert_int(excel_instance.LeaderSkillLevelField(), password),
        "EquipSlot01": bool(excel_instance.EquipSlot01Field()),
        "EquipSlotTier01": convert_int(excel_instance.EquipSlotTier01Field(), password),
        "EquipSlotLevel01": convert_int(excel_instance.EquipSlotLevel01Field(), password),
        "EquipSlot02": bool(excel_instance.EquipSlot02Field()),
        "EquipSlotTier02": convert_int(excel_instance.EquipSlotTier02Field(), password),
        "EquipSlotLevel02": convert_int(excel_instance.EquipSlotLevel02Field(), password),
        "EquipSlot03": bool(excel_instance.EquipSlot03Field()),
        "EquipSlotTier03": convert_int(excel_instance.EquipSlotTier03Field(), password),
        "EquipSlotLevel03": convert_int(excel_instance.EquipSlotLevel03Field(), password),
        "EquipCharacterWeapon": bool(excel_instance.EquipCharacterWeaponField()),
        "EquipCharacterWeaponTier": convert_int(excel_instance.EquipCharacterWeaponTierField(), password),
        "EquipCharacterWeaponLevel": convert_int(excel_instance.EquipCharacterWeaponLevelField(), password),
        "EquipCharacterGear": bool(excel_instance.EquipCharacterGearField()),
        "EquipCharacterGearTier": convert_int(excel_instance.EquipCharacterGearTierField(), password),
        "EquipCharacterGearLevel": convert_int(excel_instance.EquipCharacterGearLevelField(), password),
        "PotentialType01": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType01Field(), password)).name,
        "PotentialLevel01": convert_int(excel_instance.PotentialLevel01Field(), password),
        "PotentialType02": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType02Field(), password)).name,
        "PotentialLevel02": convert_int(excel_instance.PotentialLevel02Field(), password),
        "PotentialType03": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType03Field(), password)).name,
        "PotentialLevel03": convert_int(excel_instance.PotentialLevel03Field(), password),
    }

def dump_ExcelDB_PresetCharacterGroupSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "ArenaSimulatorFixed": bool(excel_instance.ArenaSimulatorFixedField()),
        "PresetType": [convert_string(excel_instance.PresetTypeField(j), password) for j in range(excel_instance.PresetTypeFieldLength())],
    }

def dump_ExcelDB_PresetParcelsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelIdField(), password),
        "PresetGroupId": convert_int(excel_instance.PresetGroupIdField(), password),
        "ParcelAmount": convert_int(excel_instance.ParcelAmountField(), password),
    }

def dump_ExcelDB_ProductAutoSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ProductAutoSelectionGroupId": convert_int(excel_instance.ProductAutoSelectionGroupIdField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "ResultAmount": [convert_int(excel_instance.ResultAmountField(j), password) for j in range(excel_instance.ResultAmountFieldLength())],
        "ConditionParcelType": ParcelType(convert_int(excel_instance.ConditionParcelTypeField(), password)).name,
        "ConditionParcelId": convert_int(excel_instance.ConditionParcelIdField(), password),
    }

def dump_ExcelDB_ProductBattlePassExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductIdField(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreTypeField(), password)).name,
        "Price": convert_int(excel_instance.PriceField(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "BattlePassProductGroupId": convert_int(excel_instance.BattlePassProductGroupIdField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
    }

def dump_ExcelDB_ProductDailyRecordExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductIdField(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreTypeField(), password)).name,
        "Price": convert_int(excel_instance.PriceField(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
        "TitleImagePath": convert_string(excel_instance.TitleImagePathField(), password),
    }

def dump_ExcelDB_ProductDailyRecordInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DaySize": convert_int(excel_instance.DaySizeField(), password),
        "ExpirationDate": convert_string(excel_instance.ExpirationDateField(), password),
    }

def dump_ExcelDB_ProductDailyRecordRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Day": convert_int(excel_instance.DayField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardId": [convert_int(excel_instance.RewardIdField(j), password) for j in range(excel_instance.RewardIdFieldLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmountField(j), password) for j in range(excel_instance.RewardAmountFieldLength())],
    }

def dump_ExcelDB_ProductExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductIdField(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreTypeField(), password)).name,
        "Price": convert_int(excel_instance.PriceField(), password),
        "PriceReference": convert_string(excel_instance.PriceReferenceField(), password),
        "PurchasePeriodType": PurchasePeriodType(convert_int(excel_instance.PurchasePeriodTypeField(), password)).name,
        "PurchasePeriodLimit": convert_int(excel_instance.PurchasePeriodLimitField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
    }

def dump_ExcelDB_ProductMonthlyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductIdField(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreTypeField(), password)).name,
        "Price": convert_int(excel_instance.PriceField(), password),
        "PriceReference": convert_string(excel_instance.PriceReferenceField(), password),
        "ProductTagType": ProductTagType(convert_int(excel_instance.ProductTagTypeField(), password)).name,
        "MonthlyDays": convert_int(excel_instance.MonthlyDaysField(), password),
        "UseMonthlyProductCheck": bool(excel_instance.UseMonthlyProductCheckField()),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
        "EnterCostReduceGroupId": convert_int(excel_instance.EnterCostReduceGroupIdField(), password),
        "DailyParcelType": [ParcelType(convert_int(excel_instance.DailyParcelTypeField(j), password)).name for j in range(excel_instance.DailyParcelTypeFieldLength())],
        "DailyParcelId": [convert_int(excel_instance.DailyParcelIdField(j), password) for j in range(excel_instance.DailyParcelIdFieldLength())],
        "DailyParcelAmount": [convert_int(excel_instance.DailyParcelAmountField(j), password) for j in range(excel_instance.DailyParcelAmountFieldLength())],
    }

def dump_ExcelDB_ProductSelectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductSelectSubType": ProductSelectSubType(convert_int(excel_instance.ProductSelectSubTypeField(), password)).name,
        "AutoSelectPopupType": AutoSelectPopupType(convert_int(excel_instance.AutoSelectPopupTypeField(), password)).name,
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductIdField(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreTypeField(), password)).name,
        "Price": convert_int(excel_instance.PriceField(), password),
        "PriceReference": convert_string(excel_instance.PriceReferenceField(), password),
        "PurchasePeriodType": PurchasePeriodType(convert_int(excel_instance.PurchasePeriodTypeField(), password)).name,
        "PurchasePeriodLimit": convert_int(excel_instance.PurchasePeriodLimitField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
        "ProductSelectionSlot": [convert_int(excel_instance.ProductSelectionSlotField(j), password) for j in range(excel_instance.ProductSelectionSlotFieldLength())],
    }

def dump_ExcelDB_ProductSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ProductSelectionGroupId": convert_int(excel_instance.ProductSelectionGroupIdField(), password),
        "ProductSelectionGroupComponentId": convert_int(excel_instance.ProductSelectionGroupComponentIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelIdField(), password),
        "ResultAmount": convert_int(excel_instance.ResultAmountField(), password),
        "ConditionParcelType": ParcelType(convert_int(excel_instance.ConditionParcelTypeField(), password)).name,
        "ConditionParcelId": convert_int(excel_instance.ConditionParcelIdField(), password),
    }

def dump_ExcelDB_RaidContentPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RaidBossGroupType": RaidBossGroupType(convert_int(excel_instance.RaidBossGroupTypeField(), password)).name,
        "IsPCBuild": bool(excel_instance.IsPCBuildField()),
        "IdExport": bool(excel_instance.IdExportField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "GuideTitle": convert_uint(excel_instance.GuideTitleField(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePathField(), password),
        "GuideText": convert_uint(excel_instance.GuideTextField(), password),
    }

def dump_ExcelDB_RaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "RankStart": convert_int(excel_instance.RankStartField(), password),
        "RankEnd": convert_int(excel_instance.RankEndField(), password),
        "RankStartTw": convert_int(excel_instance.RankStartTwField(), password),
        "RankEndTw": convert_int(excel_instance.RankEndTwField(), password),
        "RankStartAsia": convert_int(excel_instance.RankStartAsiaField(), password),
        "RankEndAsia": convert_int(excel_instance.RankEndAsiaField(), password),
        "RankStartNa": convert_int(excel_instance.RankStartNaField(), password),
        "RankEndNa": convert_int(excel_instance.RankEndNaField(), password),
        "RankStartGlobal": convert_int(excel_instance.RankStartGlobalField(), password),
        "RankEndGlobal": convert_int(excel_instance.RankEndGlobalField(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStartField(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEndField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_RaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "SeasonDisplay": convert_int(excel_instance.SeasonDisplayField(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartDataField(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDateField(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndDataField(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDateField(), password),
        "OpenRaidBossGroup": [convert_string(excel_instance.OpenRaidBossGroupField(j), password) for j in range(excel_instance.OpenRaidBossGroupFieldLength())],
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupIdField(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauageField(), password),
        "StackedSeasonRewardGauge": [convert_int(excel_instance.StackedSeasonRewardGaugeField(j), password) for j in range(excel_instance.StackedSeasonRewardGaugeFieldLength())],
        "SeasonRewardId": [convert_int(excel_instance.SeasonRewardIdField(j), password) for j in range(excel_instance.SeasonRewardIdFieldLength())],
    }

def dump_ExcelDB_RaidSkillDescriptionListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BossGroup": convert_string(excel_instance.BossGroupField(), password),
        "Difficulty": convert_string(excel_instance.DifficultyField(), password),
        "PhaseNameOverrideKey": convert_string(excel_instance.PhaseNameOverrideKeyField(), password),
        "SkillGroupId": [convert_string(excel_instance.SkillGroupIdField(j), password) for j in range(excel_instance.SkillGroupIdFieldLength())],
        "SkillUsePhase": [convert_int(excel_instance.SkillUsePhaseField(j), password) for j in range(excel_instance.SkillUsePhaseFieldLength())],
        "ShowSkillSlot": [SkillSlotShowType(convert_int(excel_instance.ShowSkillSlotField(j), password)).name for j in range(excel_instance.ShowSkillSlotFieldLength())],
        "HighlightResource": [SkillSlotHighLightType(convert_int(excel_instance.HighlightResourceField(j), password)).name for j in range(excel_instance.HighlightResourceFieldLength())],
    }

def dump_ExcelDB_RaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndexField()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSyncField()),
        "RaidBossGroup": convert_string(excel_instance.RaidBossGroupField(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPathField(), password),
        "BGPath": convert_string(excel_instance.BGPathField(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterIdField(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterIdField(j), password) for j in range(excel_instance.BossCharacterIdFieldLength())],
        "Difficulty": Difficulty(convert_int(excel_instance.DifficultyField(), password)).name,
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenConditionField()),
        "MaxPlayerCount": convert_int(excel_instance.MaxPlayerCountField(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTimeField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "RaidBossGroupType": RaidBossGroupType(convert_int(excel_instance.RaidBossGroupTypeField(), password)).name,
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLineField(), password),
        "TacticEnvironment": TacticEnvironment(convert_int(excel_instance.TacticEnvironmentField(), password)).name,
        "DefaultClearScore": convert_int(excel_instance.DefaultClearScoreField(), password),
        "MaximumScore": convert_int(excel_instance.MaximumScoreField(), password),
        "PerSecondMinusScore": convert_int(excel_instance.PerSecondMinusScoreField(), password),
        "HPPercentScore": convert_int(excel_instance.HPPercentScoreField(), password),
        "MinimumAcquisitionScore": convert_int(excel_instance.MinimumAcquisitionScoreField(), password),
        "MaximumAcquisitionScore": convert_int(excel_instance.MaximumAcquisitionScoreField(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupIdField(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePathField(j), password) for j in range(excel_instance.BattleReadyTimelinePathFieldLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStartField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartFieldLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEndField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndFieldLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePathField(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePathField(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhaseField(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKeyField(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKeyField(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCardField()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKeyField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_RaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfoField()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProbField(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelTypeField(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueIDField(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmountField(), password),
    }

def dump_ExcelDB_RaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_int(excel_instance.SeasonRewardIdField(), password),
        "SeasonRewardParcelType": [ParcelType(convert_int(excel_instance.SeasonRewardParcelTypeField(j), password)).name for j in range(excel_instance.SeasonRewardParcelTypeFieldLength())],
        "SeasonRewardParcelUniqueId": [convert_int(excel_instance.SeasonRewardParcelUniqueIdField(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueIdFieldLength())],
        "SeasonRewardAmount": [convert_int(excel_instance.SeasonRewardAmountField(j), password) for j in range(excel_instance.SeasonRewardAmountFieldLength())],
    }

def dump_ExcelDB_RecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeTypeField(), password)).name,
        "RecipeIngredientId": convert_int(excel_instance.RecipeIngredientIdField(), password),
        "RecipeSelectionGroupId": convert_int(excel_instance.RecipeSelectionGroupIdField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ResultAmountMin": [convert_int(excel_instance.ResultAmountMinField(j), password) for j in range(excel_instance.ResultAmountMinFieldLength())],
        "ResultAmountMax": [convert_int(excel_instance.ResultAmountMaxField(j), password) for j in range(excel_instance.ResultAmountMaxFieldLength())],
    }

def dump_ExcelDB_RecipeIngredientExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeTypeField(), password)).name,
        "CostParcelType": [ParcelType(convert_int(excel_instance.CostParcelTypeField(j), password)).name for j in range(excel_instance.CostParcelTypeFieldLength())],
        "CostId": [convert_int(excel_instance.CostIdField(j), password) for j in range(excel_instance.CostIdFieldLength())],
        "CostAmount": [convert_int(excel_instance.CostAmountField(j), password) for j in range(excel_instance.CostAmountFieldLength())],
        "IngredientParcelType": [ParcelType(convert_int(excel_instance.IngredientParcelTypeField(j), password)).name for j in range(excel_instance.IngredientParcelTypeFieldLength())],
        "IngredientId": [convert_int(excel_instance.IngredientIdField(j), password) for j in range(excel_instance.IngredientIdFieldLength())],
        "IngredientAmount": [convert_int(excel_instance.IngredientAmountField(j), password) for j in range(excel_instance.IngredientAmountFieldLength())],
        "CostTimeInSecond": convert_int(excel_instance.CostTimeInSecondField(), password),
    }

def dump_ExcelDB_RecipeSelectionAutoUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "TargetItemId": convert_int(excel_instance.TargetItemIdField(), password),
        "Priority": [convert_int(excel_instance.PriorityField(j), password) for j in range(excel_instance.PriorityFieldLength())],
    }

def dump_ExcelDB_RecipeSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RecipeSelectionGroupId": convert_int(excel_instance.RecipeSelectionGroupIdField(), password),
        "RecipeSelectionGroupComponentId": convert_int(excel_instance.RecipeSelectionGroupComponentIdField(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelTypeField(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelIdField(), password),
        "ResultAmountMin": convert_int(excel_instance.ResultAmountMinField(), password),
        "ResultAmountMax": convert_int(excel_instance.ResultAmountMaxField(), password),
    }

def dump_ExcelDB_ScenarioBGEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.NameField(), password),
        "Effect": convert_string(excel_instance.EffectField(), password),
        "Effect2": convert_string(excel_instance.Effect2Field(), password),
        "Scroll": ScenarioBGScroll(convert_int(excel_instance.ScrollField(), password)).name,
        "ScrollTime": convert_int(excel_instance.ScrollTimeField(), password),
        "ScrollFrom": convert_int(excel_instance.ScrollFromField(), password),
        "ScrollTo": convert_int(excel_instance.ScrollToField(), password),
    }

def dump_ExcelDB_ScenarioBGNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.NameField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "BGFileName": convert_string(excel_instance.BGFileNameField(), password),
        "BGType": ScenarioBGType(convert_int(excel_instance.BGTypeField(), password)).name,
        "AnimationRoot": convert_string(excel_instance.AnimationRootField(), password),
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "SpineScale": convert_float(excel_instance.SpineScaleField(), password),
        "SpineLocalPosX": convert_int(excel_instance.SpineLocalPosXField(), password),
        "SpineLocalPosY": convert_int(excel_instance.SpineLocalPosYField(), password),
    }

def dump_ExcelDB_ScenarioBGName_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupName": convert_uint(excel_instance.GroupNameField(), password),
        "NameKr": convert_uint(excel_instance.NameKrField(), password),
        "NameTw": convert_uint(excel_instance.NameTwField(), password),
        "NameAsia": convert_uint(excel_instance.NameAsiaField(), password),
        "NameNa": convert_uint(excel_instance.NameNaField(), password),
        "NameGlobal": convert_uint(excel_instance.NameGlobalField(), password),
        "NameTeen": convert_uint(excel_instance.NameTeenField(), password),
    }

def dump_ExcelDB_ScenarioCharacterEmotionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EmoticonName": convert_string(excel_instance.EmoticonNameField(), password),
        "Name": convert_uint(excel_instance.NameField(), password),
    }

def dump_ExcelDB_ScenarioCharacterNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterName": convert_uint(excel_instance.CharacterNameField(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStepField(), password)).name,
        "NameKR": convert_string(excel_instance.NameKRField(), password),
        "NicknameKR": convert_string(excel_instance.NicknameKRField(), password),
        "NameJP": convert_string(excel_instance.NameJPField(), password),
        "NicknameJP": convert_string(excel_instance.NicknameJPField(), password),
        "NameTH": convert_string(excel_instance.NameTHField(), password),
        "NicknameTH": convert_string(excel_instance.NicknameTHField(), password),
        "NameTW": convert_string(excel_instance.NameTWField(), password),
        "NicknameTW": convert_string(excel_instance.NicknameTWField(), password),
        "NameEN": convert_string(excel_instance.NameENField(), password),
        "NicknameEN": convert_string(excel_instance.NicknameENField(), password),
        "Shape": ScenarioCharacterShapes(convert_int(excel_instance.ShapeField(), password)).name,
        "SpinePrefabName": convert_string(excel_instance.SpinePrefabNameField(), password),
        "SmallPortrait": convert_string(excel_instance.SmallPortraitField(), password),
    }

def dump_ExcelDB_ScenarioCharacterSituationSetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.NameField(), password),
        "Face": convert_string(excel_instance.FaceField(), password),
        "Behavior": convert_string(excel_instance.BehaviorField(), password),
        "Action": convert_string(excel_instance.ActionField(), password),
        "Shape": convert_string(excel_instance.ShapeField(), password),
        "Effect": convert_uint(excel_instance.EffectField(), password),
        "Emotion": convert_uint(excel_instance.EmotionField(), password),
    }

def dump_ExcelDB_ScenarioContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "UnlockConditionType": CollectionUnlockType(convert_int(excel_instance.UnlockConditionTypeField(), password)).name,
        "UnlockConditionParameter": [convert_int(excel_instance.UnlockConditionParameterField(j), password) for j in range(excel_instance.UnlockConditionParameterFieldLength())],
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckTypeField(), password)).name,
        "UnlockConditionCount": convert_int(excel_instance.UnlockConditionCountField(), password),
        "IsObject": bool(excel_instance.IsObjectField()),
        "IsHorizon": bool(excel_instance.IsHorizonField()),
        "EmblemResource": convert_string(excel_instance.EmblemResourceField(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResourceField(), password),
        "FullResource": convert_string(excel_instance.FullResourceField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeIdField(), password),
    }

def dump_ExcelDB_ScenarioEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EffectName": convert_string(excel_instance.EffectNameField(), password),
        "Name": convert_uint(excel_instance.NameField(), password),
    }

def dump_ExcelDB_ScenarioModeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_int(excel_instance.ModeIdField(), password),
        "ModeType": ScenarioModeTypes(convert_int(excel_instance.ModeTypeField(), password)).name,
        "SubType": ScenarioModeSubTypes(convert_int(excel_instance.SubTypeField(), password)).name,
        "DisplayVolumeId": convert_string(excel_instance.DisplayVolumeIdField(), password),
        "VolumeId": convert_int(excel_instance.VolumeIdField(), password),
        "ChapterId": convert_int(excel_instance.ChapterIdField(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeIdField(), password),
        "ExposedTime": convert_string(excel_instance.ExposedTimeField(), password),
        "Hide": bool(excel_instance.HideField()),
        "Open": bool(excel_instance.OpenField()),
        "ScenarioOpenDate": convert_string(excel_instance.ScenarioOpenDateField(), password),
        "ScenarioCloseDate": convert_string(excel_instance.ScenarioCloseDateField(), password),
        "IsContinue": bool(excel_instance.IsContinueField()),
        "EpisodeContinueModeId": convert_int(excel_instance.EpisodeContinueModeIdField(), password),
        "FrontScenarioGroupId": [convert_int(excel_instance.FrontScenarioGroupIdField(j), password) for j in range(excel_instance.FrontScenarioGroupIdFieldLength())],
        "StrategyId": convert_int(excel_instance.StrategyIdField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattleField()),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "FieldDateId": convert_int(excel_instance.FieldDateIdField(), password),
        "BackScenarioGroupId": [convert_int(excel_instance.BackScenarioGroupIdField(j), password) for j in range(excel_instance.BackScenarioGroupIdFieldLength())],
        "ClearedModeId": [convert_int(excel_instance.ClearedModeIdField(j), password) for j in range(excel_instance.ClearedModeIdFieldLength())],
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardIdField(), password),
        "IsScenarioSpecialReward": bool(excel_instance.IsScenarioSpecialRewardField()),
        "SpecialRewardPrefabName": convert_string(excel_instance.SpecialRewardPrefabNameField(), password),
        "SpecialRewardLogOut": bool(excel_instance.SpecialRewardLogOutField()),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimitField(), password),
        "ClearedStageId": convert_int(excel_instance.ClearedStageIdField(), password),
        "NeedClub": Club(convert_int(excel_instance.NeedClubField(), password)).name,
        "NeedClubStudentCount": convert_int(excel_instance.NeedClubStudentCountField(), password),
        "EventContentId": convert_int(excel_instance.EventContentIdField(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentTypeField(), password)).name,
        "EventContentCondition": convert_int(excel_instance.EventContentConditionField(), password),
        "EventContentConditionGroup": convert_int(excel_instance.EventContentConditionGroupField(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficultyField(), password)).name,
        "StepIndex": convert_int(excel_instance.StepIndexField(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevelField(), password),
        "EventIconParcelPath": convert_string(excel_instance.EventIconParcelPathField(), password),
        "EventBannerTitle": convert_uint(excel_instance.EventBannerTitleField(), password),
        "Lof": bool(excel_instance.LofField()),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "CompleteReportEventName": convert_string(excel_instance.CompleteReportEventNameField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
        "CollectionGroupId": convert_int(excel_instance.CollectionGroupIdField(), password),
        "FirstClearFunnelMessage": convert_string(excel_instance.FirstClearFunnelMessageField(), password),
    }

def dump_ExcelDB_ScenarioModeRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardIdField(), password),
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "RewardProb": convert_int(excel_instance.RewardProbField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_ExcelDB_ScenarioModeSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeType": ScenarioModeTypes(convert_int(excel_instance.ModeTypeField(), password)).name,
        "SubType": ScenarioModeSubTypes(convert_int(excel_instance.SubTypeField(), password)).name,
        "VolumeId": convert_int(excel_instance.VolumeIdField(), password),
        "ChapterId": convert_int(excel_instance.ChapterIdField(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitleField(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescriptionField(), password),
        "PopupType": SpoilerPopupType(convert_int(excel_instance.PopupTypeField(), password)).name,
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeIdField(), password),
    }

def dump_ExcelDB_ScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeIdField(), password),
        "PriorityOrder": convert_int(excel_instance.PriorityOrderField(), password),
        "PVDisplayOrder": convert_int(excel_instance.PVDisplayOrderField(), password),
        "VideoId": convert_int(excel_instance.VideoIdField(), password),
        "BgmId": convert_int(excel_instance.BgmIdField(), password),
        "AudioName": convert_string(excel_instance.AudioNameField(), password),
        "SpinePath": convert_string(excel_instance.SpinePathField(), password),
        "Ratio": convert_int(excel_instance.RatioField(), password),
        "LobbyAniPath": convert_string(excel_instance.LobbyAniPathField(), password),
        "MovieCGPath": convert_string(excel_instance.MovieCGPathField(), password),
        "ScenarioForceEnter": ScenarioModeSubTypes(convert_int(excel_instance.ScenarioForceEnterField(), password)).name,
        "LocalizeId": convert_uint(excel_instance.LocalizeIdField(), password),
        "AcademyLobbyCharacterId": [convert_int(excel_instance.AcademyLobbyCharacterIdField(j), password) for j in range(excel_instance.AcademyLobbyCharacterIdFieldLength())],
        "SweepAnimation": [convert_string(excel_instance.SweepAnimationField(j), password) for j in range(excel_instance.SweepAnimationFieldLength())],
    }

def dump_ExcelDB_ScenarioScriptExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "SelectionGroup": convert_int(excel_instance.SelectionGroupField(), password),
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "Sound": convert_string(excel_instance.SoundField(), password),
        "Transition": convert_uint(excel_instance.TransitionField(), password),
        "BGName": convert_uint(excel_instance.BGNameField(), password),
        "BGEffect": convert_uint(excel_instance.BGEffectField(), password),
        "PopupFileName": convert_string(excel_instance.PopupFileNameField(), password),
        "ScriptKr": convert_string(excel_instance.ScriptKrField(), password),
        "TextJp": convert_string(excel_instance.TextJpField(), password),
        "TextTh": convert_string(excel_instance.TextThField(), password),
        "TextTw": convert_string(excel_instance.TextTwField(), password),
        "TextEn": convert_string(excel_instance.TextEnField(), password),
        "VoiceId": convert_uint(excel_instance.VoiceIdField(), password),
        "TeenMode": bool(excel_instance.TeenModeField()),
    }

def dump_ExcelDB_ScenarioScriptFunnelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "Index": convert_int(excel_instance.IndexField(), password),
        "FunnelId": convert_string(excel_instance.FunnelIdField(), password),
    }

def dump_ExcelDB_ScenarioTransitionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.NameField(), password),
        "TransitionOut": convert_string(excel_instance.TransitionOutField(), password),
        "TransitionOutDuration": convert_int(excel_instance.TransitionOutDurationField(), password),
        "TransitionOutResource": convert_string(excel_instance.TransitionOutResourceField(), password),
        "TransitionIn": convert_string(excel_instance.TransitionInField(), password),
        "TransitionInDuration": convert_int(excel_instance.TransitionInDurationField(), password),
        "TransitionInResource": convert_string(excel_instance.TransitionInResourceField(), password),
    }

def dump_ExcelDB_SchoolDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "DungeonType": SchoolDungeonType(convert_int(excel_instance.DungeonTypeField(), password)).name,
        "RewardTag": convert_float(excel_instance.RewardTagField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbabilityField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
    }

def dump_ExcelDB_SchoolDungeonStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageIdField(), password),
        "DungeonType": SchoolDungeonType(convert_int(excel_instance.DungeonTypeField(), password)).name,
        "Difficulty": convert_int(excel_instance.DifficultyField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageIdField(), password),
        "StageEnterCostType": [ParcelType(convert_int(excel_instance.StageEnterCostTypeField(j), password)).name for j in range(excel_instance.StageEnterCostTypeFieldLength())],
        "StageEnterCostId": [convert_int(excel_instance.StageEnterCostIdField(j), password) for j in range(excel_instance.StageEnterCostIdFieldLength())],
        "StageEnterCostAmount": [convert_int(excel_instance.StageEnterCostAmountField(j), password) for j in range(excel_instance.StageEnterCostAmountFieldLength())],
        "StageEnterCostMinimumAmount": [convert_int(excel_instance.StageEnterCostMinimumAmountField(j), password) for j in range(excel_instance.StageEnterCostMinimumAmountFieldLength())],
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoalField(j), password)).name for j in range(excel_instance.StarGoalFieldLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmountField(j), password) for j in range(excel_instance.StarGoalAmountFieldLength())],
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardIdField(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSecondsField(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_ServiceActionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ServiceActionType": ServiceActionType(convert_int(excel_instance.ServiceActionTypeField(), password)).name,
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "GoodsId": convert_int(excel_instance.GoodsIdField(), password),
    }

def dump_ExcelDB_ShiftingCraftRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "NotificationId": convert_int(excel_instance.NotificationIdField(), password),
        "ResultParcel": ParcelType(convert_int(excel_instance.ResultParcelField(), password)).name,
        "ResultId": convert_int(excel_instance.ResultIdField(), password),
        "ResultAmount": convert_int(excel_instance.ResultAmountField(), password),
        "RequireItemId": convert_int(excel_instance.RequireItemIdField(), password),
        "RequireItemAmount": convert_int(excel_instance.RequireItemAmountField(), password),
        "RequireGold": convert_int(excel_instance.RequireGoldField(), password),
        "AdditionalCostParcelType": ParcelType(convert_int(excel_instance.AdditionalCostParcelTypeField(), password)).name,
        "AdditionalCostParcelId": convert_int(excel_instance.AdditionalCostParcelIdField(), password),
        "AdditionalCostParcelAmount": convert_int(excel_instance.AdditionalCostParcelAmountField(), password),
        "IngredientTag": [Tag(convert_int(excel_instance.IngredientTagField(j), password)).name for j in range(excel_instance.IngredientTagFieldLength())],
        "IngredientExp": convert_int(excel_instance.IngredientExpField(), password),
        "RecipeDisplayOptions": RecipeDisplayOptions(convert_int(excel_instance.RecipeDisplayOptionsField(), password)).name,
    }

def dump_ExcelDB_ShopCashExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CashProductId": convert_int(excel_instance.CashProductIdField(), password),
        "PackageType": PurchaseSourceType(convert_int(excel_instance.PackageTypeField(), password)).name,
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "InMailPurchaseLock": bool(excel_instance.InMailPurchaseLockField()),
        "UseMailParcel": bool(excel_instance.UseMailParcelField()),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "RenewalDisplayOrder": convert_int(excel_instance.RenewalDisplayOrderField(), password),
        "CategoryType": ProductCategory(convert_int(excel_instance.CategoryTypeField(), password)).name,
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTagField(), password)).name,
        "ProductSaleType": ProductSaleType(convert_int(excel_instance.ProductSaleTypeField(), password)).name,
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFromField(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodToField(), password),
        "ProductSaleDay": convert_int(excel_instance.ProductSaleDayField(), password),
        "PeriodTag": bool(excel_instance.PeriodTagField()),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimitField(), password),
        "AccountLevelHide": bool(excel_instance.AccountLevelHideField()),
        "ClearMissionLimit": convert_int(excel_instance.ClearMissionLimitField(), password),
        "ClearMissionHide": bool(excel_instance.ClearMissionHideField()),
        "PurchaseReportEventName": convert_string(excel_instance.PurchaseReportEventNameField(), password),
        "PackageClientType": PurchaseSourceType(convert_int(excel_instance.PackageClientTypeField(), password)).name,
        "IsStartDash": bool(excel_instance.IsStartDashField()),
        "ViewFlag": bool(excel_instance.ViewFlagField()),
    }

def dump_ExcelDB_ShopCashScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioResrouceInfoId": convert_int(excel_instance.ScenarioResrouceInfoIdField(), password),
        "ShopCashId": convert_int(excel_instance.ShopCashIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
    }

def dump_ExcelDB_ShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "UseBigPopup": bool(excel_instance.UseBigPopupField()),
        "GoodsId": [convert_int(excel_instance.GoodsIdField(j), password) for j in range(excel_instance.GoodsIdFieldLength())],
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFromField(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodToField(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMinField(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetTypeField(), password)).name,
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventNameField(), password),
        "RestrictBuyWhenInventoryFull": bool(excel_instance.RestrictBuyWhenInventoryFullField()),
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTagField(), password)).name,
        "ShopUpdateGroupId": convert_int(excel_instance.ShopUpdateGroupIdField(), password),
    }

def dump_ExcelDB_ShopFilterClassifiedExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "ConsumeParcelType": ParcelType(convert_int(excel_instance.ConsumeParcelTypeField(), password)).name,
        "ConsumeParcelId": convert_int(excel_instance.ConsumeParcelIdField(), password),
        "ShopFilterType": ShopFilterType(convert_int(excel_instance.ShopFilterTypeField(), password)).name,
        "GoodsId": convert_int(excel_instance.GoodsIdField(), password),
    }

def dump_ExcelDB_ShopFreeRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "FreeRecruitPeriodFrom": convert_string(excel_instance.FreeRecruitPeriodFromField(), password),
        "FreeRecruitPeriodTo": convert_string(excel_instance.FreeRecruitPeriodToField(), password),
        "FreeRecruitType": ShopFreeRecruitType(convert_int(excel_instance.FreeRecruitTypeField(), password)).name,
        "FreeRecruitDecorationImagePath": convert_string(excel_instance.FreeRecruitDecorationImagePathField(), password),
        "TenRecruitCountOnly": bool(excel_instance.TenRecruitCountOnlyField()),
        "ShopRecruitId": [convert_int(excel_instance.ShopRecruitIdField(j), password) for j in range(excel_instance.ShopRecruitIdFieldLength())],
    }

def dump_ExcelDB_ShopFreeRecruitPeriodExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ShopFreeRecruitId": convert_int(excel_instance.ShopFreeRecruitIdField(), password),
        "ShopFreeRecruitIntervalId": convert_int(excel_instance.ShopFreeRecruitIntervalIdField(), password),
        "IntervalDate": convert_string(excel_instance.IntervalDateField(), password),
        "FreeRecruitCount": convert_int(excel_instance.FreeRecruitCountField(), password),
    }

def dump_ExcelDB_ShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "IsRefresh": bool(excel_instance.IsRefreshField()),
        "IsSoldOutDimmed": bool(excel_instance.IsSoldOutDimmedField()),
        "CostParcelType": [ParcelType(convert_int(excel_instance.CostParcelTypeField(j), password)).name for j in range(excel_instance.CostParcelTypeFieldLength())],
        "CostParcelId": [convert_int(excel_instance.CostParcelIdField(j), password) for j in range(excel_instance.CostParcelIdFieldLength())],
        "AutoRefreshCoolTime": convert_int(excel_instance.AutoRefreshCoolTimeField(), password),
        "ShopRefresherType": ShopRefresherType(convert_int(excel_instance.ShopRefresherTypeField(), password)).name,
        "ShopRefreshPeriodType": ShopRefreshPeriodType(convert_int(excel_instance.ShopRefreshPeriodTypeField(), password)).name,
        "RefreshAbleCount": convert_int(excel_instance.RefreshAbleCountField(), password),
        "GoodsId": [convert_int(excel_instance.GoodsIdField(j), password) for j in range(excel_instance.GoodsIdFieldLength())],
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFromField(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodToField(), password),
        "RefreshPeriodBaseTime": convert_string(excel_instance.RefreshPeriodBaseTimeField(), password),
        "ShopProductUpdateTime": convert_string(excel_instance.ShopProductUpdateTimeField(), password),
        "DisplayParcelType": ParcelType(convert_int(excel_instance.DisplayParcelTypeField(), password)).name,
        "DisplayParcelId": convert_int(excel_instance.DisplayParcelIdField(), password),
        "IsShopVisible": bool(excel_instance.IsShopVisibleField()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ShopUpdateDate": convert_int(excel_instance.ShopUpdateDateField(), password),
        "ShopUpdateGroupId1": convert_int(excel_instance.ShopUpdateGroupId1Field(), password),
        "ShopUpdateGroupId2": convert_int(excel_instance.ShopUpdateGroupId2Field(), password),
        "ShopUpdateGroupId3": convert_int(excel_instance.ShopUpdateGroupId3Field(), password),
        "ShopUpdateGroupId4": convert_int(excel_instance.ShopUpdateGroupId4Field(), password),
        "ShopUpdateGroupId5": convert_int(excel_instance.ShopUpdateGroupId5Field(), password),
        "ShopUpdateGroupId6": convert_int(excel_instance.ShopUpdateGroupId6Field(), password),
        "ShopUpdateGroupId7": convert_int(excel_instance.ShopUpdateGroupId7Field(), password),
        "ShopUpdateGroupId8": convert_int(excel_instance.ShopUpdateGroupId8Field(), password),
        "ShopUpdateGroupId9": convert_int(excel_instance.ShopUpdateGroupId9Field(), password),
        "ShopUpdateGroupId10": convert_int(excel_instance.ShopUpdateGroupId10Field(), password),
        "ShopUpdateGroupId11": convert_int(excel_instance.ShopUpdateGroupId11Field(), password),
        "ShopUpdateGroupId12": convert_int(excel_instance.ShopUpdateGroupId12Field(), password),
    }

def dump_ExcelDB_ShopRecruitDirectingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Path": convert_string(excel_instance.PathField(), password),
        "Phase": GachaPhase(convert_int(excel_instance.PhaseField(), password)).name,
        "GachaAmount": convert_int(excel_instance.GachaAmountField(), password),
        "IsSSR": bool(excel_instance.IsSSRField()),
        "Character": DirectingCharacter(convert_int(excel_instance.CharacterField(), password)).name,
    }

def dump_ExcelDB_ShopRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "OneGachaGoodsId": convert_int(excel_instance.OneGachaGoodsIdField(), password),
        "TenGachaGoodsId": convert_int(excel_instance.TenGachaGoodsIdField(), password),
        "GoodsDevName": convert_string(excel_instance.GoodsDevNameField(), password),
        "DisplayTag": GachaDisplayTag(convert_int(excel_instance.DisplayTagField(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "GachaBannerPath": convert_string(excel_instance.GachaBannerPathField(), password),
        "VideoId": [convert_int(excel_instance.VideoIdField(j), password) for j in range(excel_instance.VideoIdFieldLength())],
        "LinkedRobbyBannerId": convert_int(excel_instance.LinkedRobbyBannerIdField(), password),
        "InfoCharacterId": [convert_int(excel_instance.InfoCharacterIdField(j), password) for j in range(excel_instance.InfoCharacterIdFieldLength())],
        "SalePeriodVisible": bool(excel_instance.SalePeriodVisibleField()),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFromField(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodToField(), password),
        "RecruitCoinId": convert_int(excel_instance.RecruitCoinIdField(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopIdField(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMinField(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetTypeField(), password)).name,
        "SalePeriodDayParameter": convert_int(excel_instance.SalePeriodDayParameterField(), password),
        "IsOverrideSalePeriodTo": bool(excel_instance.IsOverrideSalePeriodToField()),
        "IsNewbie": bool(excel_instance.IsNewbieField()),
        "IsSelectRecruit": bool(excel_instance.IsSelectRecruitField()),
        "DirectPayInvisibleTokenId": convert_int(excel_instance.DirectPayInvisibleTokenIdField(), password),
        "DirectPayProductId": convert_string(excel_instance.DirectPayProductIdField(), password),
        "DirectPayAndroidShopCashId": convert_int(excel_instance.DirectPayAndroidShopCashIdField(), password),
        "DirectPayAppleShopCashId": convert_int(excel_instance.DirectPayAppleShopCashIdField(), password),
        "SelectAbleGachaGroupId": convert_int(excel_instance.SelectAbleGachaGroupIdField(), password),
        "MaxSelectCharacterNum": convert_int(excel_instance.MaxSelectCharacterNumField(), password),
        "DirectPayOneStoreShopCashId": convert_int(excel_instance.DirectPayOneStoreShopCashIdField(), password),
        "ProbabilityUrlDev": convert_string(excel_instance.ProbabilityUrlDevField(), password),
        "ProbabilityUrlLive": convert_string(excel_instance.ProbabilityUrlLiveField(), password),
    }

def dump_ExcelDB_ShopRecruitSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RecruitChangeScenarioModeID": convert_int(excel_instance.RecruitChangeScenarioModeIDField(), password),
        "PriorityOrder": convert_int(excel_instance.PriorityOrderField(), password),
        "TogetherPercentage": convert_int(excel_instance.TogetherPercentageField(), password),
        "AnotherPercentage": convert_int(excel_instance.AnotherPercentageField(), password),
        "TwistPercentage": convert_int(excel_instance.TwistPercentageField(), password),
        "RecruitChangeIcon": convert_string(excel_instance.RecruitChangeIconField(), password),
        "SeriesForceEnter": ScenarioModeSubTypes(convert_int(excel_instance.SeriesForceEnterField(), password)).name,
    }

def dump_ExcelDB_ShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcIdField(), password),
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "GoodsId": convert_int(excel_instance.GoodsIdField(), password),
        "IsBundle": bool(excel_instance.IsBundleField()),
        "ShopPurchasePopupType": ShopPurchasePopupType(convert_int(excel_instance.ShopPurchasePopupTypeField(), password)).name,
        "VisibleAmount": convert_int(excel_instance.VisibleAmountField(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimitField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "CategoryType": convert_float(excel_instance.CategoryTypeField(), password),
        "RefreshGroup": convert_int(excel_instance.RefreshGroupField(), password),
        "Prob": convert_int(excel_instance.ProbField(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventNameField(), password),
        "ProductUpdateTime": convert_string(excel_instance.ProductUpdateTimeField(), password),
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTagField(), password)).name,
    }

def dump_ExcelDB_ShopTabGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ShopGroupType": ShopGroupType(convert_int(excel_instance.ShopGroupTypeField(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ShopCategoryTypes": [convert_float(excel_instance.ShopCategoryTypesField(j), password) for j in range(excel_instance.ShopCategoryTypesFieldLength())],
    }

def dump_ExcelDB_ShortcutTypeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "IsAscending": bool(excel_instance.IsAscendingField()),
        "ContentType": [ShortcutContentType(convert_int(excel_instance.ContentTypeField(j), password)).name for j in range(excel_instance.ContentTypeFieldLength())],
    }

def dump_ExcelDB_SkillAdditionalTooltipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "AdditionalSkillGroupId": convert_string(excel_instance.AdditionalSkillGroupIdField(), password),
        "ShowSkillSlot": convert_string(excel_instance.ShowSkillSlotField(), password),
        "DisplayIconBg": bool(excel_instance.DisplayIconBgField()),
    }

def dump_ExcelDB_SkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LocalizeSkillId": convert_uint(excel_instance.LocalizeSkillIdField(), password),
        "GroupId": convert_string(excel_instance.GroupIdField(), password),
        "SkillDataKey": convert_string(excel_instance.SkillDataKeyField(), password),
        "VisualDataKey": convert_string(excel_instance.VisualDataKeyField(), password),
        "Level": convert_int(excel_instance.LevelField(), password),
        "SkillCost": convert_int(excel_instance.SkillCostField(), password),
        "ExtraSkillCost": convert_int(excel_instance.ExtraSkillCostField(), password),
        "EnemySkillCost": convert_int(excel_instance.EnemySkillCostField(), password),
        "ExtraEnemySkillCost": convert_int(excel_instance.ExtraEnemySkillCostField(), password),
        "NPCSkillCost": convert_int(excel_instance.NPCSkillCostField(), password),
        "ExtraNPCSkillCost": convert_int(excel_instance.ExtraNPCSkillCostField(), password),
        "BulletType": BulletType(convert_int(excel_instance.BulletTypeField(), password)).name,
        "StartCoolTime": convert_int(excel_instance.StartCoolTimeField(), password),
        "CoolTime": convert_int(excel_instance.CoolTimeField(), password),
        "EnemyStartCoolTime": convert_int(excel_instance.EnemyStartCoolTimeField(), password),
        "EnemyCoolTime": convert_int(excel_instance.EnemyCoolTimeField(), password),
        "NPCStartCoolTime": convert_int(excel_instance.NPCStartCoolTimeField(), password),
        "NPCCoolTime": convert_int(excel_instance.NPCCoolTimeField(), password),
        "UseAtg": convert_int(excel_instance.UseAtgField(), password),
        "RequireCharacterLevel": convert_int(excel_instance.RequireCharacterLevelField(), password),
        "RequireLevelUpMaterial": convert_int(excel_instance.RequireLevelUpMaterialField(), password),
        "IconName": convert_string(excel_instance.IconNameField(), password),
        "IsShowInfo": bool(excel_instance.IsShowInfoField()),
        "IsShowSpeechbubble": bool(excel_instance.IsShowSpeechbubbleField()),
        "PublicSpeechDuration": convert_int(excel_instance.PublicSpeechDurationField(), password),
        "AdditionalToolTipId": convert_int(excel_instance.AdditionalToolTipIdField(), password),
        "SelectExSkillToolTipId": convert_int(excel_instance.SelectExSkillToolTipIdField(), password),
        "TextureSkillCardForFormConversion": convert_string(excel_instance.TextureSkillCardForFormConversionField(), password),
        "SkillCardLabelPath": convert_string(excel_instance.SkillCardLabelPathField(), password),
    }

def dump_ExcelDB_SkillSelectExTooltipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "SelectableExSkillGroupId": convert_string(excel_instance.SelectableExSkillGroupIdField(), password),
        "SkillUseConditionLocalizeId": convert_string(excel_instance.SkillUseConditionLocalizeIdField(), password),
    }

def dump_ExcelDB_SNSInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "OpenScenarioModeId": convert_int(excel_instance.OpenScenarioModeIdField(), password),
        "CloseScenarioModeId": convert_int(excel_instance.CloseScenarioModeIdField(), password),
        "OpenTitleLocalizeKey": convert_uint(excel_instance.OpenTitleLocalizeKeyField(), password),
        "CloseTitleLocalizeKey": convert_uint(excel_instance.CloseTitleLocalizeKeyField(), password),
        "OpenDescLocalizeKey": convert_uint(excel_instance.OpenDescLocalizeKeyField(), password),
        "CloseDescLocalizeKey": convert_uint(excel_instance.CloseDescLocalizeKeyField(), password),
    }

def dump_ExcelDB_SNSPostExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SNSInfoId": convert_int(excel_instance.SNSInfoIdField(), password),
        "MasterPostId": convert_int(excel_instance.MasterPostIdField(), password),
        "RepostSNSProfileId": convert_int(excel_instance.RepostSNSProfileIdField(), password),
        "SNSProfileId": convert_int(excel_instance.SNSProfileIdField(), password),
        "PostTextLocalizeKey": convert_uint(excel_instance.PostTextLocalizeKeyField(), password),
        "PostImagePath": [convert_string(excel_instance.PostImagePathField(j), password) for j in range(excel_instance.PostImagePathFieldLength())],
        "RepostMinNum": convert_int(excel_instance.RepostMinNumField(), password),
        "RepostMaxNum": convert_int(excel_instance.RepostMaxNumField(), password),
        "FavorMinNum": convert_int(excel_instance.FavorMinNumField(), password),
        "FavorMaxNum": convert_int(excel_instance.FavorMaxNumField(), password),
    }

def dump_ExcelDB_SNSProfileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "DevName": convert_string(excel_instance.DevNameField(), password),
        "ProfileImagePath": convert_string(excel_instance.ProfileImagePathField(), password),
        "NameLocalizeKey": convert_uint(excel_instance.NameLocalizeKeyField(), password),
        "IdLocalizeKey": convert_uint(excel_instance.IdLocalizeKeyField(), password),
        "MarkIconVisible": bool(excel_instance.MarkIconVisibleField()),
    }

def dump_ExcelDB_SoundUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "SoundUniqueId": convert_string(excel_instance.SoundUniqueIdField(), password),
        "Path": convert_string(excel_instance.PathField(), password),
    }

def dump_ExcelDB_SpineLipsyncExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceId": convert_uint(excel_instance.VoiceIdField(), password),
        "AnimJson": convert_string(excel_instance.AnimJsonField(), password),
        "AnimJsonKr": convert_string(excel_instance.AnimJsonKrField(), password),
    }

def dump_ExcelDB_StageFileRefreshSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "ForceSave": bool(excel_instance.ForceSaveField()),
    }

def dump_ExcelDB_StatLevelInterpolationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.LevelField(), password),
        "StatTypeIndex": [convert_int(excel_instance.StatTypeIndexField(j), password) for j in range(excel_instance.StatTypeIndexFieldLength())],
    }

def dump_ExcelDB_StickerGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Layout": convert_string(excel_instance.LayoutField(), password),
        "UniqueLayoutPath": convert_string(excel_instance.UniqueLayoutPathField(), password),
        "StickerGroupIconpath": convert_string(excel_instance.StickerGroupIconpathField(), password),
        "PageCompleteSlot": convert_int(excel_instance.PageCompleteSlotField(), password),
        "PageCompleteRewardParcelType": ParcelType(convert_int(excel_instance.PageCompleteRewardParcelTypeField(), password)).name,
        "PageCompleteRewardParcelId": convert_int(excel_instance.PageCompleteRewardParcelIdField(), password),
        "PageCompleteRewardAmount": convert_int(excel_instance.PageCompleteRewardAmountField(), password),
        "LocalizeTitle": convert_uint(excel_instance.LocalizeTitleField(), password),
        "LocalizeDescription": convert_uint(excel_instance.LocalizeDescriptionField(), password),
        "StickerGroupCoverpath": convert_string(excel_instance.StickerGroupCoverpathField(), password),
    }

def dump_ExcelDB_StickerPageContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "StickerGroupId": convert_int(excel_instance.StickerGroupIdField(), password),
        "StickerPageId": convert_int(excel_instance.StickerPageIdField(), password),
        "StickerSlot": convert_int(excel_instance.StickerSlotField(), password),
        "StickerGetConditionType": StickerGetConditionType(convert_int(excel_instance.StickerGetConditionTypeField(), password)).name,
        "StickerCheckPassType": StickerCheckPassType(convert_int(excel_instance.StickerCheckPassTypeField(), password)).name,
        "GetStickerConditionType": GetStickerConditionType(convert_int(excel_instance.GetStickerConditionTypeField(), password)).name,
        "StickerGetConditionCount": convert_int(excel_instance.StickerGetConditionCountField(), password),
        "StickerGetConditionParameter": [convert_int(excel_instance.StickerGetConditionParameterField(j), password) for j in range(excel_instance.StickerGetConditionParameterFieldLength())],
        "StickerGetConditionParameterTag": [Tag(convert_int(excel_instance.StickerGetConditionParameterTagField(j), password)).name for j in range(excel_instance.StickerGetConditionParameterTagFieldLength())],
        "PackedStickerIconLocalizeEtcId": convert_uint(excel_instance.PackedStickerIconLocalizeEtcIdField(), password),
        "PackedStickerIconPath": convert_string(excel_instance.PackedStickerIconPathField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "StickerDetailPath": convert_string(excel_instance.StickerDetailPathField(), password),
    }

def dump_ExcelDB_StoryStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Name": convert_string(excel_instance.NameField(), password),
        "Localize": convert_string(excel_instance.LocalizeField(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCountField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "WhiteListId": convert_int(excel_instance.WhiteListIdField(), password),
        "StrategyMap": convert_string(excel_instance.StrategyMapField(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBGField(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurnField(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironmentField(), password)).name,
        "ContentType": ContentType(convert_int(excel_instance.ContentTypeField(), password)).name,
        "BGMId": convert_int(excel_instance.BGMIdField(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventNameField(), password),
    }

def dump_ExcelDB_StrategyObjectBuffDefineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StrategyObjectBuffID": convert_int(excel_instance.StrategyObjectBuffIDField(), password),
        "StrategyObjectTurn": convert_int(excel_instance.StrategyObjectTurnField(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupIdField(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
    }

def dump_ExcelDB_TacticalSupportSystemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SummonedTime": convert_int(excel_instance.SummonedTimeField(), password),
        "DefaultPersonalityId": convert_int(excel_instance.DefaultPersonalityIdField(), password),
        "CanTargeting": bool(excel_instance.CanTargetingField()),
        "CanCover": bool(excel_instance.CanCoverField()),
        "ObstacleUniqueName": convert_string(excel_instance.ObstacleUniqueNameField(), password),
        "ObstacleCoverRange": convert_int(excel_instance.ObstacleCoverRangeField(), password),
        "SummonSkilllGroupId": convert_string(excel_instance.SummonSkilllGroupIdField(), password),
        "CrashObstacleOBBWidth": convert_int(excel_instance.CrashObstacleOBBWidthField(), password),
        "CrashObstacleOBBHeight": convert_int(excel_instance.CrashObstacleOBBHeightField(), password),
        "IsTSSBlockedNodeCheck": bool(excel_instance.IsTSSBlockedNodeCheckField()),
        "NumberOfUses": convert_int(excel_instance.NumberOfUsesField(), password),
        "InventoryOffsetX": convert_float(excel_instance.InventoryOffsetXField(), password),
        "InventoryOffsetY": convert_float(excel_instance.InventoryOffsetYField(), password),
        "InventoryOffsetZ": convert_float(excel_instance.InventoryOffsetZField(), password),
        "InteractionChar": convert_int(excel_instance.InteractionCharField(), password),
        "CharacterInteractionStartDelay": convert_int(excel_instance.CharacterInteractionStartDelayField(), password),
        "GetOnStartEffectPath": convert_string(excel_instance.GetOnStartEffectPathField(), password),
        "GetOnEndEffectPath": convert_string(excel_instance.GetOnEndEffectPathField(), password),
        "SummonerCharacterId": convert_int(excel_instance.SummonerCharacterIdField(), password),
        "InteractionFrame": convert_int(excel_instance.InteractionFrameField(), password),
        "TSAInteractionAddDuration": convert_int(excel_instance.TSAInteractionAddDurationField(), password),
        "InteractionStudentExSkillGroupId": convert_string(excel_instance.InteractionStudentExSkillGroupIdField(), password),
        "InteractionSkillCardTexture": convert_string(excel_instance.InteractionSkillCardTextureField(), password),
        "InteractionSkillSpine": convert_string(excel_instance.InteractionSkillSpineField(), password),
        "RetreatFrame": convert_int(excel_instance.RetreatFrameField(), password),
        "DestroyFrame": convert_int(excel_instance.DestroyFrameField(), password),
    }

def dump_ExcelDB_TacticEntityEffectFilterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TargetEffectName": convert_string(excel_instance.TargetEffectNameField(), password),
        "ShowEffectToVehicle": bool(excel_instance.ShowEffectToVehicleField()),
        "ShowEffectToBoss": bool(excel_instance.ShowEffectToBossField()),
    }

def dump_ExcelDB_TacticSkipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiffField(), password),
        "HPResult": convert_int(excel_instance.HPResultField(), password),
    }

def dump_ExcelDB_TerrainAdaptationFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TerrainAdaptation": StageTopography(convert_int(excel_instance.TerrainAdaptationField(), password)).name,
        "TerrainAdaptationStat": TerrainAdaptationStat(convert_int(excel_instance.TerrainAdaptationStatField(), password)).name,
        "ShotFactor": convert_int(excel_instance.ShotFactorField(), password),
        "BlockFactor": convert_int(excel_instance.BlockFactorField(), password),
        "AccuracyFactor": convert_int(excel_instance.AccuracyFactorField(), password),
        "DodgeFactor": convert_int(excel_instance.DodgeFactorField(), password),
        "AttackPowerFactor": convert_int(excel_instance.AttackPowerFactorField(), password),
        "TerrainFactorDescription": convert_string(excel_instance.TerrainFactorDescriptionField(), password),
    }

def dump_ExcelDB_TimeAttackDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TimeAttackDungeonType": TimeAttackDungeonType(convert_int(excel_instance.TimeAttackDungeonTypeField(), password)).name,
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKeyField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "InformationGroupID": convert_int(excel_instance.InformationGroupIDField(), password),
    }

def dump_ExcelDB_TimeAttackDungeonGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TimeAttackDungeonType": TimeAttackDungeonType(convert_int(excel_instance.TimeAttackDungeonTypeField(), password)).name,
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKeyField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "ClearDefaultPoint": convert_int(excel_instance.ClearDefaultPointField(), password),
        "ClearTimeWeightPoint": convert_int(excel_instance.ClearTimeWeightPointField(), password),
        "TimeWeightConst": convert_int(excel_instance.TimeWeightConstField(), password),
        "Difficulty": convert_int(excel_instance.DifficultyField(), password),
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "AllyPassiveSkillId": [convert_string(excel_instance.AllyPassiveSkillIdField(j), password) for j in range(excel_instance.AllyPassiveSkillIdFieldLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevelField(j), password) for j in range(excel_instance.AllyPassiveSkillLevelFieldLength())],
        "EnemyPassiveSkillId": [convert_string(excel_instance.EnemyPassiveSkillIdField(j), password) for j in range(excel_instance.EnemyPassiveSkillIdFieldLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevelField(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelFieldLength())],
        "GeasIconPath": [convert_string(excel_instance.GeasIconPathField(j), password) for j in range(excel_instance.GeasIconPathFieldLength())],
        "GeasLocalizeEtcKey": [convert_uint(excel_instance.GeasLocalizeEtcKeyField(j), password) for j in range(excel_instance.GeasLocalizeEtcKeyFieldLength())],
    }

def dump_ExcelDB_TimeAttackDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "RewardMaxPoint": convert_int(excel_instance.RewardMaxPointField(), password),
        "RewardType": [TimeAttackDungeonRewardType(convert_int(excel_instance.RewardTypeField(j), password)).name for j in range(excel_instance.RewardTypeFieldLength())],
        "RewardMinPoint": [convert_int(excel_instance.RewardMinPointField(j), password) for j in range(excel_instance.RewardMinPointFieldLength())],
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelDefaultAmount": [convert_int(excel_instance.RewardParcelDefaultAmountField(j), password) for j in range(excel_instance.RewardParcelDefaultAmountFieldLength())],
        "RewardParcelMaxAmount": [convert_int(excel_instance.RewardParcelMaxAmountField(j), password) for j in range(excel_instance.RewardParcelMaxAmountFieldLength())],
    }

def dump_ExcelDB_TimeAttackDungeonSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "UISlot": convert_int(excel_instance.UISlotField(), password),
        "DungeonId": convert_int(excel_instance.DungeonIdField(), password),
        "DifficultyGeas": [convert_int(excel_instance.DifficultyGeasField(j), password) for j in range(excel_instance.DifficultyGeasFieldLength())],
        "TimeAttackDungeonRewardId": convert_int(excel_instance.TimeAttackDungeonRewardIdField(), password),
        "RoomLifeTimeInSeconds": convert_int(excel_instance.RoomLifeTimeInSecondsField(), password),
    }

def dump_ExcelDB_ToastExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.IdField(), password),
        "ToastType": ToastType(convert_int(excel_instance.ToastTypeField(), password)).name,
        "MissionId": convert_uint(excel_instance.MissionIdField(), password),
        "TextId": convert_uint(excel_instance.TextIdField(), password),
        "LifeTime": convert_int(excel_instance.LifeTimeField(), password),
    }

def dump_ExcelDB_TrophyCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeIdField(), password),
        "FurnitureId": [convert_int(excel_instance.FurnitureIdField(j), password) for j in range(excel_instance.FurnitureIdFieldLength())],
    }

def dump_ExcelDB_TutorialCharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TalkId": convert_int(excel_instance.TalkIdField(), password),
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTHField(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTWField(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeENField(), password),
        "VoiceId": convert_uint(excel_instance.VoiceIdField(), password),
    }

def dump_ExcelDB_TutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "CompletionReportEventName": convert_string(excel_instance.CompletionReportEventNameField(), password),
        "CompulsoryTutorial": bool(excel_instance.CompulsoryTutorialField()),
        "DescriptionTutorial": bool(excel_instance.DescriptionTutorialField()),
        "TutorialStageId": convert_int(excel_instance.TutorialStageIdField(), password),
        "UIName": [convert_string(excel_instance.UINameField(j), password) for j in range(excel_instance.UINameFieldLength())],
        "TutorialParentName": [convert_string(excel_instance.TutorialParentNameField(j), password) for j in range(excel_instance.TutorialParentNameFieldLength())],
    }

def dump_ExcelDB_TutorialFailureImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Contents": TutorialFailureContentType(convert_int(excel_instance.ContentsField(), password)).name,
        "Type": convert_string(excel_instance.TypeField(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKrField(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJpField(), password),
        "ImagePathTh": convert_string(excel_instance.ImagePathThField(), password),
        "ImagePathTw": convert_string(excel_instance.ImagePathTwField(), password),
        "ImagePathEn": convert_string(excel_instance.ImagePathEnField(), password),
        "ReplaceLocalizeKey": convert_string(excel_instance.ReplaceLocalizeKeyField(), password),
    }

def dump_ExcelDB_UnderCoverStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "StageNameFile": convert_string(excel_instance.StageNameFileField(), password),
        "StageTryCount": convert_int(excel_instance.StageTryCountField(), password),
        "ApplySkip": bool(excel_instance.ApplySkipField()),
        "SkipCount": convert_int(excel_instance.SkipCountField(), password),
        "ShowClearScene": bool(excel_instance.ShowClearSceneField()),
        "StageTips": convert_uint(excel_instance.StageTipsField(), password),
        "StageName": convert_uint(excel_instance.StageNameField(), password),
    }

def dump_ExcelDB_VideoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Nation": [Nation(convert_int(excel_instance.NationField(j), password)).name for j in range(excel_instance.NationFieldLength())],
        "VideoPath": [convert_string(excel_instance.VideoPathField(j), password) for j in range(excel_instance.VideoPathFieldLength())],
        "VideoTeenPath": [convert_string(excel_instance.VideoTeenPathField(j), password) for j in range(excel_instance.VideoTeenPathFieldLength())],
        "SoundPath": [convert_string(excel_instance.SoundPathField(j), password) for j in range(excel_instance.SoundPathFieldLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolumeField(j), password) for j in range(excel_instance.SoundVolumeFieldLength())],
    }

def dump_ExcelDB_Video_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VideoId": convert_int(excel_instance.VideoIdField(), password),
        "VideoPathKr": convert_string(excel_instance.VideoPathKrField(), password),
        "VideoTeenPathKr": convert_string(excel_instance.VideoTeenPathKrField(), password),
        "VideoPathTh": convert_string(excel_instance.VideoPathThField(), password),
        "VideoTeenPathTh": convert_string(excel_instance.VideoTeenPathThField(), password),
        "VideoPathTw": convert_string(excel_instance.VideoPathTwField(), password),
        "VideoTeenPathTw": convert_string(excel_instance.VideoTeenPathTwField(), password),
        "VideoPathEn": convert_string(excel_instance.VideoPathEnField(), password),
        "VideoTeenPathEn": convert_string(excel_instance.VideoTeenPathEnField(), password),
    }

def dump_ExcelDB_VoiceCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceEvent": VoiceEvent(convert_int(excel_instance.VoiceEventField(), password)).name,
        "Rate": convert_int(excel_instance.RateField(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHashField(j), password) for j in range(excel_instance.VoiceHashFieldLength())],
    }

def dump_ExcelDB_VoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "Id": convert_uint(excel_instance.IdField(), password),
        "Nation": [Nation(convert_int(excel_instance.NationField(j), password)).name for j in range(excel_instance.NationFieldLength())],
        "Path": [convert_string(excel_instance.PathField(j), password) for j in range(excel_instance.PathFieldLength())],
        "Volume": [convert_float(excel_instance.VolumeField(j), password) for j in range(excel_instance.VolumeFieldLength())],
    }

def dump_ExcelDB_VoiceLogicEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LogicEffectNameHash": convert_uint(excel_instance.LogicEffectNameHashField(), password),
        "Self": bool(excel_instance.SelfField()),
        "Priority": convert_int(excel_instance.PriorityField(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHashField(j), password) for j in range(excel_instance.VoiceHashFieldLength())],
        "VoiceId": convert_uint(excel_instance.VoiceIdField(), password),
    }

def dump_ExcelDB_VoiceRoomExceptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueIdField(), password),
        "LinkedCharacterVoicePrintType": CVPrintType(convert_int(excel_instance.LinkedCharacterVoicePrintTypeField(), password)).name,
        "LinkedCostumeUniqueId": convert_int(excel_instance.LinkedCostumeUniqueIdField(), password),
    }

def dump_ExcelDB_VoiceSpineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "Id": convert_uint(excel_instance.IdField(), password),
        "Nation": [Nation(convert_int(excel_instance.NationField(j), password)).name for j in range(excel_instance.NationFieldLength())],
        "Path": [convert_string(excel_instance.PathField(j), password) for j in range(excel_instance.PathFieldLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolumeField(j), password) for j in range(excel_instance.SoundVolumeFieldLength())],
    }

def dump_ExcelDB_VoiceTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueIdField(), password),
        "Id": convert_uint(excel_instance.IdField(), password),
        "Nation": [Nation(convert_int(excel_instance.NationField(j), password)).name for j in range(excel_instance.NationFieldLength())],
        "Path": [convert_string(excel_instance.PathField(j), password) for j in range(excel_instance.PathFieldLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolumeField(j), password) for j in range(excel_instance.SoundVolumeFieldLength())],
    }

def dump_ExcelDB_WebEventSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "Enabled": bool(excel_instance.EnabledField()),
        "IconOrder": convert_int(excel_instance.IconOrderField(), password),
        "WebEventId": [convert_int(excel_instance.WebEventIdField(j), password) for j in range(excel_instance.WebEventIdFieldLength())],
        "IsFull": bool(excel_instance.IsFullField()),
        "UseExternalBrowser": bool(excel_instance.UseExternalBrowserField()),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "LobbyBannerImage": convert_string(excel_instance.LobbyBannerImageField(), password),
        "PopupTitleLocalizeKey": convert_string(excel_instance.PopupTitleLocalizeKeyField(), password),
        "StageEventUrl": convert_string(excel_instance.StageEventUrlField(), password),
        "LiveEventUrl": convert_string(excel_instance.LiveEventUrlField(), password),
    }

def dump_ExcelDB_WeekDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageIdField(), password),
        "WeekDungeonType": convert_float(excel_instance.WeekDungeonTypeField(), password),
        "Difficulty": convert_int(excel_instance.DifficultyField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageIdField(), password),
        "StageEnterCostType": [ParcelType(convert_int(excel_instance.StageEnterCostTypeField(j), password)).name for j in range(excel_instance.StageEnterCostTypeFieldLength())],
        "StageEnterCostId": [convert_int(excel_instance.StageEnterCostIdField(j), password) for j in range(excel_instance.StageEnterCostIdFieldLength())],
        "StageEnterCostAmount": [convert_int(excel_instance.StageEnterCostAmountField(j), password) for j in range(excel_instance.StageEnterCostAmountFieldLength())],
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "StarGoal": [StarGoalType(convert_int(excel_instance.StarGoalField(j), password)).name for j in range(excel_instance.StarGoalFieldLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmountField(j), password) for j in range(excel_instance.StarGoalAmountFieldLength())],
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopographyField(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevelField(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardIdField(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSecondsField(), password),
        "BattleRewardExp": convert_int(excel_instance.BattleRewardExpField(), password),
        "BattleRewardPlayerExp": convert_int(excel_instance.BattleRewardPlayerExpField(), password),
        "GroupBuffID": [convert_int(excel_instance.GroupBuffIDField(j), password) for j in range(excel_instance.GroupBuffIDFieldLength())],
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_WeekDungeonGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDungeonBuffId": convert_int(excel_instance.WeekDungeonBuffIdField(), password),
        "School": School(convert_int(excel_instance.SchoolField(), password)).name,
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcIdField(), password),
        "FormationLocalizeEtcId": convert_uint(excel_instance.FormationLocalizeEtcIdField(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupIdField(), password),
    }

def dump_ExcelDB_WeekDungeonOpenScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDay": WeekDay(convert_int(excel_instance.WeekDayField(), password)).name,
        "Open": [convert_float(excel_instance.OpenField(j), password) for j in range(excel_instance.OpenFieldLength())],
    }

def dump_ExcelDB_WeekDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "DungeonType": convert_float(excel_instance.DungeonTypeField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelIdField(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmountField(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbabilityField(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayedField()),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPathField(), password),
    }

def dump_ExcelDB_WelcomeCampaignAttendanceRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "CountCheckType": WelcomeCampaignAttendanceType(convert_int(excel_instance.CountCheckTypeField(), password)).name,
        "Day": convert_int(excel_instance.DayField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardId": convert_int(excel_instance.RewardIdField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
    }

def dump_ExcelDB_WelcomeCampaignEnterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelTypeField(), password)).name,
        "RewardParcelUniqueID": convert_int(excel_instance.RewardParcelUniqueIDField(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmountField(), password),
    }

def dump_ExcelDB_WelcomeCampaignMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "Category": MissionCategory(convert_int(excel_instance.CategoryField(), password)).name,
        "IsLegacy": bool(excel_instance.IsLegacyField()),
        "Day": convert_int(excel_instance.DayField(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionIdField(j), password) for j in range(excel_instance.PreMissionIdFieldLength())],
        "Description": convert_uint(excel_instance.DescriptionField(), password),
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayTypeField(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePathField(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUIField(j), password) for j in range(excel_instance.ShortcutUIFieldLength())],
        "CompleteConditionDayBlock": bool(excel_instance.CompleteConditionDayBlockField()),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionTypeField(), password)).name,
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCountField(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameterField(j), password) for j in range(excel_instance.CompleteConditionParameterFieldLength())],
        "CompleteConditionParameterTag": [Tag(convert_int(excel_instance.CompleteConditionParameterTagField(j), password)).name for j in range(excel_instance.CompleteConditionParameterTagFieldLength())],
        "CompleteConditionParameterUIPrefabType": MissionCompleteUIPrefabType(convert_int(excel_instance.CompleteConditionParameterUIPrefabTypeField(), password)).name,
        "MissionRewardParcelType": [ParcelType(convert_int(excel_instance.MissionRewardParcelTypeField(j), password)).name for j in range(excel_instance.MissionRewardParcelTypeFieldLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelIdField(j), password) for j in range(excel_instance.MissionRewardParcelIdFieldLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmountField(j), password) for j in range(excel_instance.MissionRewardAmountFieldLength())],
    }

def dump_ExcelDB_WelcomeCampaignRewardIncreaseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeIdField(), password),
        "IconPath": convert_string(excel_instance.IconPathField(), password),
        "EventTargetType": EventTargetType(convert_int(excel_instance.EventTargetTypeField(), password)).name,
        "IncreaseRatio": convert_int(excel_instance.IncreaseRatioField(), password),
        "ShortcutEventTargetType": EventTargetType(convert_int(excel_instance.ShortcutEventTargetTypeField(), password)).name,
    }

def dump_ExcelDB_WelcomeCampaignSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TitleLocalizeCode": convert_uint(excel_instance.TitleLocalizeCodeField(), password),
        "TargetGroup": TargetGroup(convert_int(excel_instance.TargetGroupField(), password)).name,
        "ActiveOrder": convert_int(excel_instance.ActiveOrderField(), password),
        "StartDate": convert_string(excel_instance.StartDateField(), password),
        "EndDate": convert_string(excel_instance.EndDateField(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDateField(), password),
        "EnterIconImage": convert_string(excel_instance.EnterIconImageField(), password),
        "BackgroundImage": convert_string(excel_instance.BackgroundImageField(), password),
        "TitleImage": convert_string(excel_instance.TitleImageField(), password),
        "EnterRewardGroupId": convert_int(excel_instance.EnterRewardGroupIdField(), password),
        "RewardIncreaseId": convert_int(excel_instance.RewardIncreaseIdField(), password),
        "MaximumLoginCount": convert_int(excel_instance.MaximumLoginCountField(), password),
        "AttendanceBookSize": convert_int(excel_instance.AttendanceBookSizeField(), password),
        "ContinuousAttendance": bool(excel_instance.ContinuousAttendanceField()),
    }

def dump_ExcelDB_WorldRaidBossGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupIdField(), password),
        "WorldBossName": convert_string(excel_instance.WorldBossNameField(), password),
        "WorldBossPopupPortrait": convert_string(excel_instance.WorldBossPopupPortraitField(), password),
        "WorldBossPopupBG": convert_string(excel_instance.WorldBossPopupBGField(), password),
        "WorldBossParcelPortrait": convert_string(excel_instance.WorldBossParcelPortraitField(), password),
        "WorldBossListParcel": convert_string(excel_instance.WorldBossListParcelField(), password),
        "WorldBossHP": convert_int(excel_instance.WorldBossHPField(), password),
        "WorldBossHPTw": convert_int(excel_instance.WorldBossHPTwField(), password),
        "WorldBossHPAsia": convert_int(excel_instance.WorldBossHPAsiaField(), password),
        "WorldBossHPNa": convert_int(excel_instance.WorldBossHPNaField(), password),
        "WorldBossHPGlobal": convert_int(excel_instance.WorldBossHPGlobalField(), password),
        "UIHideBeforeSpawn": bool(excel_instance.UIHideBeforeSpawnField()),
        "HideAnotherBossKilled": bool(excel_instance.HideAnotherBossKilledField()),
        "WorldBossClearRewardGroupId": convert_int(excel_instance.WorldBossClearRewardGroupIdField(), password),
        "AnotherBossKilled": [convert_int(excel_instance.AnotherBossKilledField(j), password) for j in range(excel_instance.AnotherBossKilledFieldLength())],
        "EchelonConstraintGroupId": convert_int(excel_instance.EchelonConstraintGroupIdField(), password),
        "ExclusiveOperatorBossSpawn": convert_string(excel_instance.ExclusiveOperatorBossSpawnField(), password),
        "ExclusiveOperatorBossKill": convert_string(excel_instance.ExclusiveOperatorBossKillField(), password),
        "ExclusiveOperatorScenarioBattle": convert_string(excel_instance.ExclusiveOperatorScenarioBattleField(), password),
        "ExclusiveOperatorBossDamaged": convert_string(excel_instance.ExclusiveOperatorBossDamagedField(), password),
        "BossGroupOpenCondition": convert_int(excel_instance.BossGroupOpenConditionField(), password),
    }

def dump_ExcelDB_WorldRaidConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "LockUI": [convert_string(excel_instance.LockUIField(j), password) for j in range(excel_instance.LockUIFieldLength())],
        "HideWhenLocked": bool(excel_instance.HideWhenLockedField()),
        "AccountLevel": convert_int(excel_instance.AccountLevelField(), password),
        "ScenarioModeId": [convert_int(excel_instance.ScenarioModeIdField(j), password) for j in range(excel_instance.ScenarioModeIdFieldLength())],
        "CampaignStageID": [convert_int(excel_instance.CampaignStageIDField(j), password) for j in range(excel_instance.CampaignStageIDFieldLength())],
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckTypeField(), password)).name,
        "AfterWhenDate": convert_string(excel_instance.AfterWhenDateField(), password),
        "WorldRaidBossKill": [convert_int(excel_instance.WorldRaidBossKillField(j), password) for j in range(excel_instance.WorldRaidBossKillFieldLength())],
    }

def dump_ExcelDB_WorldRaidFavorBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WorldRaidFavorRank": convert_int(excel_instance.WorldRaidFavorRankField(), password),
        "WorldRaidFavorRankBonus": convert_int(excel_instance.WorldRaidFavorRankBonusField(), password),
    }

def dump_ExcelDB_WorldRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonIdField(), password),
        "PhaseId": convert_int(excel_instance.PhaseIdField(), password),
        "EnterTicket": CurrencyTypes(convert_int(excel_instance.EnterTicketField(), password)).name,
        "WorldRaidLobbyScene": convert_string(excel_instance.WorldRaidLobbySceneField(), password),
        "WorldRaidLobbyBanner": convert_string(excel_instance.WorldRaidLobbyBannerField(), password),
        "WorldRaidLobbyBG": convert_string(excel_instance.WorldRaidLobbyBGField(), password),
        "WorldRaidLobbyBannerShow": bool(excel_instance.WorldRaidLobbyBannerShowField()),
        "SeasonOpenCondition": convert_int(excel_instance.SeasonOpenConditionField(), password),
        "WorldRaidLobbyEnterScenario": convert_int(excel_instance.WorldRaidLobbyEnterScenarioField(), password),
        "CanPlayNotSeasonTime": bool(excel_instance.CanPlayNotSeasonTimeField()),
        "WorldRaidUniqueThemeLobbyUI": bool(excel_instance.WorldRaidUniqueThemeLobbyUIField()),
        "WorldRaidUniqueThemeName": convert_string(excel_instance.WorldRaidUniqueThemeNameField(), password),
        "CanWorldRaidGemEnter": bool(excel_instance.CanWorldRaidGemEnterField()),
        "HideWorldRaidTicketUI": bool(excel_instance.HideWorldRaidTicketUIField()),
        "HideWorldRaidBossCompleteRewardUI": bool(excel_instance.HideWorldRaidBossCompleteRewardUIField()),
        "UseWorldRaidCommonToast": bool(excel_instance.UseWorldRaidCommonToastField()),
        "OpenRaidBossGroupId": [convert_int(excel_instance.OpenRaidBossGroupIdField(j), password) for j in range(excel_instance.OpenRaidBossGroupIdFieldLength())],
        "BossSpawnTime": [convert_string(excel_instance.BossSpawnTimeField(j), password) for j in range(excel_instance.BossSpawnTimeFieldLength())],
        "EliminateTime": [convert_string(excel_instance.EliminateTimeField(j), password) for j in range(excel_instance.EliminateTimeFieldLength())],
        "ScenarioOutputConditionId": [convert_int(excel_instance.ScenarioOutputConditionIdField(j), password) for j in range(excel_instance.ScenarioOutputConditionIdFieldLength())],
        "ConditionScenarioGroupid": [convert_int(excel_instance.ConditionScenarioGroupidField(j), password) for j in range(excel_instance.ConditionScenarioGroupidFieldLength())],
        "WorldRaidMapEnterOperator": convert_string(excel_instance.WorldRaidMapEnterOperatorField(), password),
        "UseFavorRankBuff": bool(excel_instance.UseFavorRankBuffField()),
    }

def dump_ExcelDB_WorldRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndexField()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSyncField()),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupIdField(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPathField(), password),
        "BGPath": convert_string(excel_instance.BGPathField(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterIdField(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterIdField(j), password) for j in range(excel_instance.BossCharacterIdFieldLength())],
        "AssistCharacterLimitCount": convert_int(excel_instance.AssistCharacterLimitCountField(), password),
        "WorldRaidDifficulty": WorldRaidDifficulty(convert_int(excel_instance.WorldRaidDifficultyField(), password)).name,
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenConditionField()),
        "RaidEnterAmount": convert_int(excel_instance.RaidEnterAmountField(), password),
        "ReEnterAmount": convert_int(excel_instance.ReEnterAmountField(), password),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "RaidBattleEndRewardGroupId": convert_int(excel_instance.RaidBattleEndRewardGroupIdField(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupIdField(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePathField(j), password) for j in range(excel_instance.BattleReadyTimelinePathFieldLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStartField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartFieldLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEndField(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndFieldLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePathField(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePathField(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhaseField(), password),
        "EnterScenarioKey": convert_int(excel_instance.EnterScenarioKeyField(), password),
        "ClearScenarioKey": convert_int(excel_instance.ClearScenarioKeyField(), password),
        "UseFixedEchelon": bool(excel_instance.UseFixedEchelonField()),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonIdField(), password),
        "IsRaidScenarioBattle": bool(excel_instance.IsRaidScenarioBattleField()),
        "ShowSkillCard": bool(excel_instance.ShowSkillCardField()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKeyField(), password),
        "DamageToWorldBoss": convert_int(excel_instance.DamageToWorldBossField(), password),
        "AllyPassiveSkill": [convert_string(excel_instance.AllyPassiveSkillField(j), password) for j in range(excel_instance.AllyPassiveSkillFieldLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevelField(j), password) for j in range(excel_instance.AllyPassiveSkillLevelFieldLength())],
        "SaveCurrentLocalBossHP": bool(excel_instance.SaveCurrentLocalBossHPField()),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionTypeField(), password)).name,
    }

def dump_ExcelDB_WorldRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfoField()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProbField(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelTypeField(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueIDField(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmountField(), password),
    }

def dump_Excel_AddressableBlackListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_AddressableBlackListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_AddressableWhiteListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_AddressableWhiteListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_BattleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_BattleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_BossPhaseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_BossPhaseExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_BuffParticleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_BuffParticleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_CharacterDialogFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_CharacterDialogFieldExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_CheatCodeListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_CheatCodeListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ClearDeckRuleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ClearDeckRuleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConquestStepExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConquestStepExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstArenaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstArenaExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstAudioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstAudioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstCombatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstCombatExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstCommonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstConquestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstConquestExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstContentsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstContentsExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstEventCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstEventCommonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstFieldExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstKeyMappingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstKeyMappingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstMinigameCCGExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstMinigameCCGExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstMinigameRoadPuzzleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstMinigameRoadPuzzleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstMiniGameShootingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstMiniGameShootingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstMinigameTBGExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstMinigameTBGExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstNewbieContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstNewbieContentExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ConstStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ConstStrategyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_CouponStuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_CouponStuffExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_CumulativeTimeRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_CumulativeTimeRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_DefaultCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_DefaultCharacterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_DefaultEchelonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_DefaultEchelonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_DefaultFurnitureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_DefaultFurnitureExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_DefaultMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_DefaultMailExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_DefaultParcelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_DefaultParcelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_EmoticonSpecialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_EmoticonSpecialExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_EventContentBoxGachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_EventContentBoxGachaElementExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_EventContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_EventContentExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldContentStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldContentStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldContentStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldContentStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldCurtainCallFreeModeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldCurtainCallFreeModeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldDateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldDateExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldEvidenceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldEvidenceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldInteractionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldKeywordExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldKeywordExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldMasteryExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldMasteryExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldMasteryLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldMasteryLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldMasteryManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldMasteryManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldQuestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldQuestExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldSceneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldSceneExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldStoryStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldStoryStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldTutorialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldTutorialExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_FieldWorldMapZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_FieldWorldMapZoneExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_KatakanaConvertExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_KatakanaConvertExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_KnockBackExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_KnockBackExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_LimitedStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_LimitedStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_LimitedStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_LimitedStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_LimitedStageSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_LimitedStageSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_MinigameCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_MinigameCardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_MinigameRoadExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_MinigameRoadExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_NormalSkillTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_NormalSkillTemplateExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ObstacleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ObstacleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ProtocolSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ProtocolSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_RecipeCraftExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_RecipeCraftExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ScenarioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ScenarioReplayExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ScenarioReplayExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_SpecialLobbyIllustExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_SpecialLobbyIllustExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_StringTestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_StringTestExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_SystemMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_SystemMailExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_TacticArenaSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_TacticArenaSimulatorSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_TacticDamageSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_TacticDamageSimulatorSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_TacticSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_TacticSimulatorSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_TacticTimeAttackSimulatorConfigExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_TacticTimeAttackSimulatorConfigExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_TagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_TagExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_TranscendenceRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_TranscendenceRecipeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_VoiceSkillUseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_VoiceSkillUseExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_WeekDungeonFindGiftRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_WeekDungeonFindGiftRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyFavorScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyFavorScheduleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyLocationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyLocationRankExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyLocationRankExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyMessangerExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyMessangerExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyTicketExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyTicketExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AcademyZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AcademyZoneExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AccountLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AccountLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AccountLevelRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AccountLevelRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AlertPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AlertPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ArenaLevelSectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ArenaLevelSectionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ArenaMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ArenaMapExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ArenaNPCExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ArenaNPCExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ArenaRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ArenaRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ArenaSeasonCloseRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ArenaSeasonCloseRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ArenaSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ArenaSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AssistEchelonTypeConvertExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AssistEchelonTypeConvertExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AssistRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AssistRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AssistSlotExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AssistSlotExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AttendanceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AttendanceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AttendanceRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AttendanceRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_AudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_AudioAnimatorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattleLevelFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattleLevelFactorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattlePassExpLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattlePassExpLimitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattlePassFlavorTextExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattlePassFlavorTextExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattlePassInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattlePassInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattlePassLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattlePassLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattlePassMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattlePassMissionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BattlePassRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BattlePassRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BGMExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BGMExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BGMRaidExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BGMRaidExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BGMUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BGMUIExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BGM_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BGM_GlobalExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BossExternalBTExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BossExternalBTExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_BulletArmorDamageFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_BulletArmorDamageFactorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CafeInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CafeInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CafeInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CafeInteractionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CafeProductionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CafeProductionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CafeRankExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CafeRankExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CameraExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CameraExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CampaignChapterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CampaignChapterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CampaignChapterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CampaignChapterRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CampaignStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CampaignStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CampaignStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CampaignStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CampaignStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CampaignStrategyObjectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CampaignUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CampaignUnitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterAcademyTagsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterAcademyTagsExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterAIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterAIExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterCalculationLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterCalculationLimitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterCombatSkinExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterCombatSkinExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterDialogBattlePassExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterDialogBattlePassExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterDialogEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterDialogEmojiExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterDialogEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterDialogEventExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterDialogExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterDialogSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterDialogSubtitleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterGearExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterGearExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterGearLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterGearLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterIllustCoordinateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterIllustCoordinateExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterLevelStatFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterLevelStatFactorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterPotentialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterPotentialExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterPotentialRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterPotentialRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterPotentialStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterPotentialStatExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterSkillListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterSkillListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterStatExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterStatLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterStatLimitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterStatsDetailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterStatsDetailExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterStatsTransExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterStatsTransExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterTranscendenceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterTranscendenceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterVictoryInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterVictoryInteractionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterVoiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterVoiceSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterVoiceSubtitleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterWeaponExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterWeaponExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterWeaponExpBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterWeaponExpBonusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CharacterWeaponLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CharacterWeaponLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ClanChattingEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ClanChattingEmojiExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ClanRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ClanRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CombatEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CombatEmojiExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestCalculateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestCalculateExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestCameraSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestCameraSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestErosionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestErosionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestErosionUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestErosionUnitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestEventExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestGroupBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestGroupBonusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestGroupBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestGroupBuffExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestMapExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestObjectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestPlayGuideExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestProgressResourceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestProgressResourceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestTileExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestUnexpectedEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestUnexpectedEventExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ConquestUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ConquestUnitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ContentEnterCostReduceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ContentEnterCostReduceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ContentsFeverExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ContentsFeverExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ContentSpoilerPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ContentsScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ContentsScenarioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ContentsShortcutExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ContentsShortcutExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ContentTargetGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ContentTargetGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CostumeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CostumeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_CurrencyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CurrencyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_DuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_DuplicateBonusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EchelonConstraintExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EchelonConstraintExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EliminateRaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidRankingRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EliminateRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EliminateRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EliminateRaidStageLimitedRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidStageLimitedRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EliminateRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EliminateRaidStageSeasonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidStageSeasonRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EmblemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EmblemExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EquipmentChangePieceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EquipmentChangePieceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EquipmentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EquipmentExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EquipmentLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EquipmentLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EquipmentStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EquipmentStatExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentArchiveBannerOffsetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentArchiveBannerOffsetExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentBoxGachaManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentBoxGachaManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentBoxGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentBoxGachaShopExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentBuffExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentBuffGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentBuffGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentCardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentCardShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentCardShopExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentCardShopModifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentCardShopModifyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentChangeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentChangeScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentChangeScenarioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentCharacterBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentCharacterBonusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentClueExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentClueExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentClueSearchExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentClueSearchExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentClueSearchRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentClueSearchRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentClueSearchRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentClueSearchRoundExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentCollectionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentConcentrationCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentConcentrationCardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentConcentrationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentConcentrationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentConcentrationRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentConcentrationRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentConcentrationVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentConcentrationVoiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentCurrencyItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentCurrencyItemExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentDebuffRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentDebuffRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentDiceRaceEffectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentDiceRaceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentDiceRaceNodeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceProbExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentDiceRaceProbExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentDiceRaceTotalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentDiceRaceTotalRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentFortuneGachaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentFortuneGachaExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentFortuneGachaModifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentFortuneGachaModifyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentFortuneGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentFortuneGachaShopExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentLobbyMenuExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentLobbyMenuExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentLocationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentLocationRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentLocationRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentMeetupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentMeetupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentMeetupInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentMeetupInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentMiniEventShortCutExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentMiniEventShortCutExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentMiniEventTokenExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentMiniEventTokenExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentMissionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentNotifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentNotifyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentPlayGuideExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentScenarioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentShopExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentShopInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentShopInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentShopRefreshExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentSpecialOperationsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentSpecialOperationsExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentSpineDialogOffsetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentSpineDialogOffsetExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentSpineDisplayPeriodExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentSpineDisplayPeriodExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentSpoilerPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentStageTotalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentStageTotalRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentTreasureCellRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentTreasureCellRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentTreasureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentTreasureExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentTreasureRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentTreasureRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentTreasureRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentTreasureRoundExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentZoneExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_EventContentZoneVisitRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EventContentZoneVisitRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FarmingDungeonLocationManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FarmingDungeonLocationManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FavorLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FavorLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FavorLevelRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FavorLevelRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FieldQuestGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FieldQuestGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FieldSNSInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FieldSNSInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FieldSNSPostExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FieldSNSPostExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FieldWarpExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FieldWarpExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FixedEchelonSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FixedEchelonSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FixedStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FixedStrategyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FloaterCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FloaterCommonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FormationLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FormationLocationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FurnitureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FurnitureExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FurnitureGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FurnitureGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FurnitureTemplateElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FurnitureTemplateElementExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_FurnitureTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_FurnitureTemplateExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaCombinedCostExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaCombinedCostExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaCraftNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaCraftNodeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaCraftNodeGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaCraftNodeGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaCraftOpenTagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaCraftOpenTagExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaElementExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaElementRecursiveExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaElementRecursiveExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GachaSelectPickupGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GachaSelectPickupGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GoodsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GoodsExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GooglePlayAchievementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GooglePlayAchievementExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GroundExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GroundModuleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GroundModuleRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GrowthScoreCalculationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GrowthScoreCalculationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GuideMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GuideMissionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GuideMissionOpenStageConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GuideMissionOpenStageConditionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_GuideMissionSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_GuideMissionSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_HpBarAbbreviationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_HpBarAbbreviationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_IAWorldRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_IAWorldRaidStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_IdCardBackgroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_IdCardBackgroundExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InformationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InformationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InformationStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InformationStrategyObjectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidArcadeMachineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidArcadeMachineExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidBossGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidBossGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidCarrierExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidCarrierExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidCarrierMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidCarrierMapExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidCarrierRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidCarrierRecipeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidConditionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidSkillDescriptionListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidSkillDescriptionListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_InteractiveWorldRaidStatusPresetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_InteractiveWorldRaidStatusPresetExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ItemExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyControllerImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyControllerImageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingDisplayInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingDisplayInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingGroupInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingGroupInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingPopupNoneFocusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingPopupNoneFocusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingTabExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingTabExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LevelExpMasterCoinExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LevelExpMasterCoinExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LoadingImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LoadingImageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeCharProfileChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeCharProfileChangeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeCharProfileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeCharProfileExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeCodeInBuildExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeCodeInBuildExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeErrorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeErrorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeEtcExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeEtcExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeGachaShopExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LocalizeSkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LocalizeSkillExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_LogicEffectCommonVisualExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_LogicEffectCommonVisualExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MemoryLobbyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MemoryLobbyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MemoryLobby_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MemoryLobby_GlobalExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MessagePopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MessagePopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameAudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameAudioAnimatorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGCardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGCharacterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGEnemyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGEnemyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGEnemyGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGEnemyGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGLevelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGLevelNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGLevelNodeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGLevelStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGLevelStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGLogicEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGLogicEffectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGOpenDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGOpenDialogExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGPerkExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGPerkExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGRewardCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGRewardCardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGRewardCardRateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGRewardCardRateExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGRewardItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGRewardItemExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGSkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGSkillExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGStartDeckCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGStartDeckCardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameCCGStartDeckCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameCCGStartDeckCharacterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDefenseCharacterBanExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDefenseCharacterBanExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDefenseFixedStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDefenseFixedStatExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDefenseInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDefenseInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDefenseStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDefenseStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamCollectionScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamCollectionScenarioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamDailyPointExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamDailyPointExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamEndingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamEndingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamEndingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamEndingRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamParameterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamParameterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamReplayScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamReplayScenarioExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamScheduleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamScheduleResultExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamScheduleResultExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameDreamTimelineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameDreamTimelineExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameDreamVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameDreamVoiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameMissionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGamePlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGamePlayGuideExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRhythmBgmExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRhythmBgmExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRhythmExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRhythmExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRoadPuzzleAdditionalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRoadPuzzleAdditionalRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRoadPuzzleInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRoadPuzzleInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameRoadPuzzleMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameRoadPuzzleMapExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameRoadPuzzleMapTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameRoadPuzzleMapTileExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRoadPuzzleRailSetRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRoadPuzzleRailSetRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameRoadPuzzleRailTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameRoadPuzzleRailTileExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRoadPuzzleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRoadPuzzleRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameRoadPuzzleRoadRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameRoadPuzzleRoadRoundExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameRoadPuzzleVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameRoadPuzzleVoiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameShootingCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameShootingCharacterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameShootingGeasExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameShootingGeasExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameShootingStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameShootingStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameShootingStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameShootingStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGDiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGDiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGEncounterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGEncounterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGEncounterOptionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGEncounterOptionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGEncounterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGEncounterRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGItemExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGObjectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGThemaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGThemaExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MiniGameTBGThemaRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MiniGameTBGThemaRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MinigameTBGVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MinigameTBGVoiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MissionEmergencyCompleteExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MissionEmergencyCompleteExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MissionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MomotalkScheduleSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MomotalkScheduleSpoilerPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MultiFloorRaidRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MultiFloorRaidRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MultiFloorRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MultiFloorRaidSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MultiFloorRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MultiFloorRaidStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_MultiFloorRaidStatChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_MultiFloorRaidStatChangeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ObstacleFireLineCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ObstacleFireLineCheckExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ObstacleStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ObstacleStatExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_OpenConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_OpenConditionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_OperatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_OperatorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ParcelAutoSynthExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ParcelAutoSynthExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PermanentRaidManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PermanentRaidManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PersonalityExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PersonalityExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PickupDuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PickupDuplicateBonusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PickupFirstGetBonus2ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PickupFirstGetBonus2Excel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PickupFirstGetBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PickupFirstGetBonusExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PossessionCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PossessionCheckExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PresetCharacterGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PresetCharacterGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PresetCharacterGroupSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PresetCharacterGroupSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_PresetParcelsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_PresetParcelsExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductAutoSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductAutoSelectionGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductBattlePassExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductBattlePassExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductDailyRecordExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductDailyRecordExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductDailyRecordInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductDailyRecordInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductDailyRecordRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductDailyRecordRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductMonthlyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductMonthlyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductSelectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductSelectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ProductSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ProductSelectionGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidContentPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidContentPlayGuideExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidRankingRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidSkillDescriptionListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidSkillDescriptionListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidStageSeasonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidStageSeasonRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RecipeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RecipeIngredientExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RecipeIngredientExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RecipeSelectionAutoUseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RecipeSelectionAutoUseExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RecipeSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RecipeSelectionGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioBGEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioBGEffectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioBGNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioBGNameExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioBGName_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioBGName_GlobalExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioCharacterEmotionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioCharacterEmotionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioCharacterNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioCharacterNameExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioCharacterSituationSetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioCharacterSituationSetExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioContentCollectionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioEffectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioModeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioModeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioModeRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioModeRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioModeSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioModeSpoilerPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioResourceInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioScriptExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioScriptExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioScriptFunnelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioScriptFunnelExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ScenarioTransitionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ScenarioTransitionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SchoolDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SchoolDungeonRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SchoolDungeonStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SchoolDungeonStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ServiceActionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ServiceActionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShiftingCraftRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShiftingCraftRecipeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopCashExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopCashExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopCashScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopCashScenarioResourceInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopFilterClassifiedExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopFilterClassifiedExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopFreeRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopFreeRecruitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopFreeRecruitPeriodExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopFreeRecruitPeriodExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopRecruitDirectingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopRecruitDirectingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopRecruitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopRecruitSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopRecruitSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopRefreshExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShopTabGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopTabGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ShortcutTypeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShortcutTypeExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SkillAdditionalTooltipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SkillAdditionalTooltipExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SkillExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SkillSelectExTooltipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SkillSelectExTooltipExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SNSInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SNSInfoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SNSPostExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SNSPostExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SNSProfileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SNSProfileExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SoundUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SoundUIExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SpineLipsyncExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SpineLipsyncExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_StageFileRefreshSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_StageFileRefreshSettingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_StatLevelInterpolationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_StatLevelInterpolationExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_StickerGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_StickerGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_StickerPageContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_StickerPageContentExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_StoryStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_StoryStrategyExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_StrategyObjectBuffDefineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_StrategyObjectBuffDefineExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TacticalSupportSystemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TacticalSupportSystemExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TacticEntityEffectFilterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TacticEntityEffectFilterExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TacticSkipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TacticSkipExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TerrainAdaptationFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TerrainAdaptationFactorExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TimeAttackDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TimeAttackDungeonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TimeAttackDungeonGeasExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TimeAttackDungeonGeasExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TimeAttackDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TimeAttackDungeonRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TimeAttackDungeonSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TimeAttackDungeonSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_ToastExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ToastExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TrophyCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TrophyCollectionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TutorialCharacterDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TutorialCharacterDialogExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TutorialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TutorialExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_TutorialFailureImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_TutorialFailureImageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_UnderCoverStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_UnderCoverStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VideoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VideoExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_Video_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_Video_GlobalExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VoiceCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VoiceCommonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VoiceExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VoiceLogicEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VoiceLogicEffectExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VoiceRoomExceptionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VoiceRoomExceptionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VoiceSpineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VoiceSpineExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_VoiceTimelineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_VoiceTimelineExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WebEventSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WebEventSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WeekDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WeekDungeonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WeekDungeonGroupBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WeekDungeonGroupBuffExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WeekDungeonOpenScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WeekDungeonOpenScheduleExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WeekDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WeekDungeonRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WelcomeCampaignAttendanceRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WelcomeCampaignAttendanceRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WelcomeCampaignEnterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WelcomeCampaignEnterRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WelcomeCampaignMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WelcomeCampaignMissionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WelcomeCampaignRewardIncreaseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WelcomeCampaignRewardIncreaseExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WelcomeCampaignSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WelcomeCampaignSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WorldRaidBossGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WorldRaidBossGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WorldRaidConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WorldRaidConditionExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WorldRaidFavorBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WorldRaidFavorBuffExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WorldRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WorldRaidSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WorldRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WorldRaidStageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_WorldRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WorldRaidStageRewardExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }
