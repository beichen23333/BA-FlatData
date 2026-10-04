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
    Max = 89

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
    Browser = 44
    Webview = 45
    Survey = 46
    Browser_Arg = 47
    Webview_Arg = 48

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
    SelectRecruit = 6
    PackagePropertyThreeStar = 7
    Temp_1 = 8
    PackageAcademyThreeStar = 9
    SelectPickup = 10
    SelectPickupOnce = 11
    PackageLimitedThreeStar = 12
    PackageThreeStar_R88_Explosion = 13
    PackageThreeStar_R88_Mystic = 14
    PackageThreeStar_R88_Pierce = 15
    PackageThreeStar_R88_Sonic = 16

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

class ItemCategory(IntEnum):
    Coin = 0
    CharacterExpGrowth = 1
    SecretStone = 2
    Material = 3
    Consumable = 4
    Collectible = 5
    Favor = 6
    RecruitCoin = 7
    InvisibleToken = 8

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
    AttendanceImmediately = 15
    WeeklyProductReward = 16
    BiweeklyProductReward = 17
    Temp_1 = 18
    Temp_2 = 19
    Temp_3 = 20
    CouponCompleteReward = 21
    BirthdayGift = 22
    SurveyReward = 23
    CbtRechargeReward = 24
    FromCS = 25
    ExpiryChangeCurrency = 26
    ExpiryBattlePassItem = 27
    FreeProductReward = 28
    Temp_4 = 29
    Temp_5 = 30
    Temp_6 = 31
    ProductGooglePointReward = 32
    PaymentCenterProduct = 33
    PaymentCenterMonthly = 34
    PaymentCenterBattlePass = 35
    PaymentCenterDailyRecord = 36
    ExpiryProductDailyRecordItem = 37

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
    CharacterGear = 18
    IdCardBackground = 19
    Emblem = 20
    Sticker = 21
    Costume = 22
    PossessionCheck = 23
    BattlePassExp = 24
    SelectedCharacter = 25
    UnSelectedCharacter = 26

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
    Temp_1 = 59
    Temp_2 = 60
    Temp_3 = 61
    Temp_4 = 62
    Temp_5 = 63
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
    Harmony = 3
    OneStore = 4
    MicrosoftStore = 5
    GalaxyStore = 6
    STEAM = 7
    FreeProduct = 8
    Twitch = 9
    Chzzk = 10
    PaymentCenter = 11
    PCStore = 12

class PurchasePeriodType(IntEnum):
    None_ = 0
    Day = 1
    Week = 2
    Month = 3
    day21 = 4

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
    GachaDirect = 4
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
    BundleMonthly = 3

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
    Furniture = 0
    MovieMania = 1
    Scientific = 2
    Military = 3
    Machine = 4
    Gamer = 5
    Cook = 6
    Farmer = 7
    Sociable = 8
    Officer = 9
    Eerie = 10
    Intellectual = 11
    Healthy = 12
    Gourmet = 13
    TreasureHunter = 14
    CraftItem = 15
    CDItem = 16
    ExpItem = 17
    SecretStone = 18
    BookItem = 19
    FavorItem = 20
    MaterialItem = 21
    Item = 22
    CraftCommitment = 23
    ExpendableItem = 24
    Equipment = 25
    EnemyLarge = 26
    Decagram = 27
    EnemySmall = 28
    EnemyMedium = 29
    EnemyXLarge = 30
    Gehenna = 31
    Millennium = 32
    Valkyrie = 33
    Hyakkiyako = 34
    RedWinter = 35
    Shanhaijing = 36
    Abydos = 37
    Trinity = 38
    Hanger = 39
    StudyRoom = 40
    ClassRoom = 41
    Library = 42
    Lobby = 43
    ShootingRange = 44
    Office = 45
    SchaleResidence = 46
    SchaleOffice = 47
    Restaurant = 48
    Laboratory = 49
    AVRoom = 50
    ArcadeCenter = 51
    Gym = 52
    Garden = 53
    Convenience = 54
    Soldiery = 55
    Lounge = 56
    SchoolBuilding = 57
    Club = 58
    Campus = 59
    SchoolYard = 60
    Plaza = 61
    StudentCouncilOffice = 62
    ClosedBuilding = 63
    Annex = 64
    Pool = 65
    AllySmall = 66
    AllyMedium = 67
    AllyLarge = 68
    AllyXLarge = 69
    Dessert = 70
    Sports = 71
    Bedding = 72
    Curios = 73
    Electronic = 74
    Toy = 75
    Reservation = 76
    Household = 77
    Horticulture = 78
    Fashion = 79
    Functional = 80
    Delicious = 81
    Freakish = 82
    MomoFriends = 83
    Music = 84
    LoveStory = 85
    Game = 86
    Girlish = 87
    Beauty = 88
    Army = 89
    Humanities = 90
    Observational = 91
    Jellyz = 92
    Detective = 93
    Roman = 94
    CuriousFellow = 95
    Mystery = 96
    Doll = 97
    Movie = 98
    Art = 99
    PureLiterature = 100
    Food = 101
    Smart = 102
    BigMeal = 103
    Simplicity = 104
    Specialized = 105
    Books = 106
    Cosmetics = 107
    Gift1 = 108
    Gift2 = 109
    F_Aru = 110
    F_Eimi = 111
    F_Haruna = 112
    F_Hihumi = 113
    F_Hina = 114
    F_Hoshino = 115
    F_Iori = 116
    F_Maki = 117
    F_Neru = 118
    F_Izumi = 119
    F_Shiroko = 120
    F_Shun = 121
    F_Sumire = 122
    F_Tsurugi = 123
    F_Akane = 124
    F_Chise = 125
    F_Akari = 126
    F_Hasumi = 127
    F_Nonomi = 128
    F_Kayoko = 129
    F_Mutsuki = 130
    F_Zunko = 131
    F_Serika = 132
    F_Tsubaki = 133
    F_Yuuka = 134
    F_Haruka = 135
    F_Asuna = 136
    F_Kotori = 137
    F_Suzumi = 138
    F_Pina = 139
    F_Aris = 140
    F_Azusa = 141
    F_Cherino = 142
    TagName0004 = 143
    TagName0005 = 144
    F_Koharu = 145
    F_Hanako = 146
    F_Midori = 147
    F_Momoi = 148
    F_Hibiki = 149
    F_Karin = 150
    F_Saya = 151
    F_Mashiro = 152
    F_Airi = 153
    F_Fuuka = 154
    F_Hanae = 155
    F_Hare = 156
    F_Utaha = 157
    F_Ayane = 158
    F_Chinatsu = 159
    F_Kotama = 160
    F_Juri = 161
    F_Serina = 162
    F_Shimiko = 163
    F_Yoshimi = 164
    TagName0009 = 165
    F_Shizuko = 166
    F_Izuna = 167
    F_Nodoka = 168
    F_Yuzu = 169
    Shield = 170
    Helmet = 171
    RedHelmet = 172
    Helicopter = 173
    RangeAttack = 174
    MeleeAttack = 175
    Sweeper = 176
    Blackmarket = 177
    Yoheki = 178
    Kaiserpmc = 179
    Crusader = 180
    Goliath = 181
    Drone = 182
    Piece = 183
    ChampionHeavyArmor = 184
    Sukeban = 185
    Arius = 186
    EnemyKotori = 187
    EnemyYuuka = 188
    KaiserpmcHeavyArmor = 189
    BlackmarketHeavyArmor = 190
    YohekiHeavyArmor = 191
    SweeperBlack = 192
    SweeperYellow = 193
    GasMaskLightArmor = 194
    GehennaFuuki = 195
    ChampionAutomata = 196
    YohekiAutomata = 197
    Automata = 198
    EnemyIori = 199
    EnemyAkari = 200
    NewAutomata = 201
    NewAutomataBlack = 202
    NewAutomataYellow = 203
    Hat = 204
    Gloves = 205
    Shoes = 206
    Bag = 207
    Badge = 208
    Hairpin = 209
    Charm = 210
    Watch = 211
    Necklace = 212
    Cafe = 213
    GameCenter = 214
    ChocolateCafe = 215
    Main = 216
    Support = 217
    Explosion = 218
    Pierce = 219
    Mystic = 220
    LightArmor = 221
    HeavyArmor = 222
    Unarmed = 223
    Cover = 224
    Uncover = 225
    AR = 226
    SR = 227
    DSG = 228
    SMG = 229
    MG = 230
    HG = 231
    GL = 232
    SG = 233
    MT = 234
    RG = 235
    Front = 236
    Middle = 237
    Back = 238
    StreetBattle_Over_A = 239
    OutdoorBattle_Over_A = 240
    IndoorBattle_Over_A = 241
    StreetBattle_Under_B = 242
    OutdoorBattle_Under_B = 243
    IndoorBattle_Under_B = 244
    Kaitenranger = 245
    Transport = 246
    Itcenter = 247
    Powerplant = 248
    SukebanSwim_SMG = 249
    SukebanSwim_MG = 250
    SukebanSwim_SR = 251
    SukebanSwim_Champion = 252
    Token_S6 = 253
    Swimsuit = 254
    WaterPlay = 255
    F_Hihumi_Swimsuit = 256
    F_Azusa_Swimsuit = 257
    F_Tsurugi_Swimsuit = 258
    F_Mashiro_Swimsuit = 259
    F_Hina_swimsuit = 260
    F_Iori_swimsuit = 261
    F_Izumi_swimsuit = 262
    F_Shiroko_RidingSuit = 263
    Church = 264
    Stronghold = 265
    Gallery = 266
    MusicRoom = 267
    Emotional = 268
    F_Shun_Kid = 269
    F_Kirino_default = 270
    F_Saya_Casual = 271
    F_Neru_BunnyGirl = 272
    F_Karin_BunnyGirl = 273
    F_Asuna_BunnyGirl = 274
    DecagrammatonSPO = 275
    Justice = 276
    F_Natsu = 277
    F_Miku = 278
    F_Ako = 279
    F_Mari = 280
    F_Chinatsu_Onsen = 281
    F_Tomoe = 282
    F_Cherino_Onsen = 283
    F_Nodoka_Onsen = 284
    F_Aru_Newyear = 285
    F_Mutsuki_Newyear = 286
    F_Serika_Newyear = 287
    Boss = 288
    F_Wakamo = 289
    F_Sena = 290
    F_Chihiro = 291
    F_Fubuki = 292
    F_Mimori = 293
    SkillBookUltimatePieace = 294
    MaterialItemN = 295
    MaterialItemR = 296
    MaterialItemSR = 297
    MaterialItemSSR = 298
    CDItemN = 299
    CDItemR = 300
    CDItemSR = 301
    CDItemSSR = 302
    BookItemN = 303
    BookItemR = 304
    BookItemSR = 305
    BookItemSSR = 306
    ShiftingCraftMaterial_Furniture = 307
    TrophyBronzeGroup001 = 308
    TrophySilverGroup001 = 309
    TrophyGoldGroup001 = 310
    TrophyPlatinumGroup001 = 311
    ShiftingCraftCategory_CommonMaterial = 312
    ShiftingCraftCategory_CDItem = 313
    ShiftingCraftCategory_BookItem = 314
    ShiftingCraftCategory_Furniture = 315
    Token_S14 = 316
    F_Ui = 317
    F_Hinata = 318
    F_Marina = 319
    SRT = 320
    F_Miyako = 321
    F_Miyu = 322
    F_Saki = 323
    Ninja = 324
    F_Tsukuyo = 325
    F_Michiru = 326
    F_Kaede = 327
    F_Iroha = 328
    F_Misaki = 329
    F_Atsuko = 330
    F_Hiyori = 331
    F_Wakamo_Swimsuit = 332
    F_Nonomi_Swimsuit = 333
    F_Ayane_Swimsuit = 334
    CraftMaterial_SecretStone = 335
    CraftMaterial_FurnitureN = 336
    CraftMaterial_FurnitureR = 337
    CraftMaterial_FurnitureSR = 338
    CraftMaterial_FurnitureSSR = 339
    ExpEquip = 340
    WeaponExpEquip = 341
    TheSeminar = 342
    Fuuki = 343
    Kohshinjo68 = 344
    GameDev = 345
    Countermeasure = 346
    CleanNClearing = 347
    GourmetClub = 348
    F_Hoshino_Swimsuit = 349
    F_Izuna_Swimsuit = 350
    F_Chise_Swimsuit = 351
    F_Shizuko_Swimsuit = 352
    F_Saori = 353
    CraftMaterial_FavorItemSR = 354
    CraftMaterial_FavorItemSSR = 355
    ShiftingCraftCategory_FavorItem = 356
    F_Akari2 = 357
    F_Aris2 = 358
    F_Asuna2 = 359
    F_Asuna_BunnyGirl2 = 360
    F_Atsuko2 = 361
    F_Ayane_Swimsuit2 = 362
    F_Azusa_Swimsuit2 = 363
    F_Cherino_Onsen2 = 364
    F_Chinatsu2 = 365
    F_Hare2 = 366
    F_Haruna2 = 367
    F_Hihumi2 = 368
    F_Hihumi_Swimsuit2 = 369
    F_Hina2 = 370
    F_Hina_swimsuit2 = 371
    F_Hinata2 = 372
    F_Hoshino2 = 373
    F_Hoshino_Swimsuit2 = 374
    F_Juri2 = 375
    F_Karin2 = 376
    F_Karin_BunnyGirl2 = 377
    F_Kirino_default2 = 378
    F_Kotori2 = 379
    F_Mashiro2 = 380
    F_Mashiro_Swimsuit2 = 381
    F_Midori2 = 382
    F_Misaki2 = 383
    F_Miyako2 = 384
    F_Miyu2 = 385
    F_Momoi2 = 386
    F_Neru_BunnyGirl2 = 387
    F_Pina2 = 388
    F_Saya_Casual2 = 389
    F_Sena2 = 390
    F_Serina2 = 391
    F_Suzumi2 = 392
    F_Tomoe2 = 393
    F_Tsubaki2 = 394
    F_Tsurugi2 = 395
    F_Tsurugi_Swimsuit2 = 396
    F_Ui2 = 397
    F_Utaha2 = 398
    F_Wakamo2 = 399
    F_Wakamo_Swimsuit2 = 400
    F_Yuuka2 = 401
    CraftMaterial_Furniture = 402
    TrophyBronzeGroup002 = 403
    TrophySilverGroup002 = 404
    TrophyGoldGroup002 = 405
    TrophyPlatinumGroup002 = 406
    F_Kazusa = 407
    F_Kokona = 408
    F_Moe = 409
    F_Kokona2 = 410
    AtsukoOriginal = 411
    FromAriusSquad = 412
    EventChallenge_ExplosionTarget = 413
    F_Utaha_Cheerleader = 414
    F_Hibiki_Cheerleader = 415
    F_Akane_BunnyGirl = 416
    F_Noa = 417
    F_Utaha_Cheerleader2 = 418
    F_Hibiki_Cheerleader2 = 419
    F_Akane_BunnyGirl2 = 420
    F_Yuuka_Track = 421
    F_Mari_Track = 422
    F_Hasumi_Track = 423
    F_Himari = 424
    F_Mari_Track2 = 425
    F_Hasumi_Track2 = 426
    F_Himari2 = 427
    Veritas = 428
    SPTF = 429
    Engineer = 430
    F_Shigure = 431
    F_Serina_Holiday = 432
    F_Hanae_Holiday = 433
    F_Shigure2 = 434
    F_Serina_Holiday2 = 435
    F_Hanae_Holiday2 = 436
    Holiday = 437
    Perorozilla_MiddleSize = 438
    Perorozilla_SmallSize = 439
    F_Haruna_Newyear = 440
    F_Haruna_Newyear2 = 441
    F_Mine = 442
    F_Mine2 = 443
    F_Junko_Newyear = 444
    F_Junko_Newyear2 = 445
    F_Fuuka_Newyear = 446
    F_Fuuka_Newyear2 = 447
    F_Megu = 448
    F_Megu2 = 449
    F_Sakurako = 450
    F_Sakurako2 = 451
    F_Kanna = 452
    F_Kanna2 = 453
    F_Mika = 454
    F_Mika2 = 455
    UnNamedGuardianMiddle = 456
    F_Toki = 457
    F_Toki2 = 458
    F_Koyuki = 459
    F_Koyuki2 = 460
    F_Nagisa = 461
    F_Nagisa2 = 462
    F_Kayoko_Newyear = 463
    F_Kayoko_Newyear2 = 464
    F_Haruka_Newyear = 465
    F_Haruka_Newyear2 = 466
    F_Kaho = 467
    F_Kaho2 = 468
    DUArea = 469
    F_Aris_Maid = 470
    F_Aris_Maid2 = 471
    F_Yuzu_Maid = 472
    F_Yuzu_Maid2 = 473
    F_Toki_BunnyGirl = 474
    F_Toki_BunnyGirl2 = 475
    F_Reisa = 476
    F_Reisa2 = 477
    Genryumon = 478
    BlackTortoisePromenade = 479
    LaborParty = 480
    F_Rumi = 481
    F_Rumi2 = 482
    F_Mina = 483
    F_Mina2 = 484
    F_Minori = 485
    F_Minori2 = 486
    ValkyrieCD = 487
    ValkyrieBook = 488
    F_Miyako_Swimsuit = 489
    F_Miyako_Swimsuit2 = 490
    F_Saki_Swimsuit = 491
    F_Saki_Swimsuit2 = 492
    F_Miyu_Swimsuit = 493
    F_Miyu_Swimsuit2 = 494
    F_Shiroko_Swimsuit = 495
    F_Shiroko_Swimsuit2 = 496
    EN0005_CenterPipe = 497
    F_Koharu_Swimsuit = 498
    F_Koharu_Swimsuit2 = 499
    F_Ui_Swimsuit = 500
    F_Ui_Swimsuit2 = 501
    F_Hanako_Swimsuit = 502
    F_Hanako_Swimsuit2 = 503
    F_Hinata_Swimsuit = 504
    F_Hinata_Swimsuit2 = 505
    F_Mimori_Swimsuit = 506
    F_Mimori_Swimsuit2 = 507
    Hostage = 508
    HoverMissile = 509
    HoverObject = 510
    HoverGuidedDevice = 511
    HoverStealthMissile = 512
    Gift3 = 513
    HoverResort = 514
    Raid_Normal = 515
    Raid_Hard = 516
    Raid_VeryHard = 517
    Raid_HardCore = 518
    Raid_Extreme = 519
    Raid_Insane = 520
    Raid_Torment = 521
    KnowledgeLiberationFront = 522
    SummerRemedialClass = 523
    F_Momiji = 524
    F_Momiji2 = 525
    F_Meru = 526
    F_Meru2 = 527
    F_Kotori_Cheerleader = 528
    F_Kotori_Cheerleader2 = 529
    F_Haruna_Track = 530
    F_Haruna_Track2 = 531
    F_Ichika = 532
    F_Ichika2 = 533
    F_Kasumi = 534
    F_Kasumi2 = 535
    F_Shigure_Onsen = 536
    F_Shigure_Onsen2 = 537
    Highlander = 538
    SentryGun = 539
    Token_S32 = 540
    Tier2Piece = 541
    Tier3Piece = 542
    Tier4Piece = 543
    Tier5Piece = 544
    Sticker_102_Tag_01 = 545
    Sticker_102_Tag_02 = 546
    F_Misaka_Mikoto = 547
    F_Shokuho_Misaki = 548
    F_Saten_Ruiko = 549
    F_Yukari = 550
    F_Misaka_Mikoto2 = 551
    F_Shokuho_Misaki2 = 552
    F_Saten_Ruiko2 = 553
    F_Yukari2 = 554
    StreetGhostes = 555
    F_Renge = 556
    F_Renge2 = 557
    F_Kikyo = 558
    F_Kikyo2 = 559
    F_Eimi_Swimsuit = 560
    F_Eimi_Swimsuit2 = 561
    Hyakkayouran = 562
    Totem701 = 563
    MatsuriOffice = 564
    Shugyobu = 565
    Onmyobu = 566
    NinpoKenkyubu = 567
    Kurokage_Scenario = 568
    F_Kotama_Camping = 569
    F_Kotama_Camping2 = 570
    F_Hare_Camping = 571
    F_Hare_Camping2 = 572
    Hina_Dress = 573
    F_Hina_Dress = 574
    F_Hina_Dress2 = 575
    F_Ako_Dress = 576
    F_Ako_Dress2 = 577
    F_Ibuki = 578
    F_Ibuki2 = 579
    F_Makoto = 580
    F_Makoto2 = 581
    Avantgardekun_Escort_TimeAttack = 582
    F_Kayoko_Dress = 583
    F_Kayoko_Dress2 = 584
    F_Aru_Dress = 585
    F_Aru_Dress2 = 586
    F_Akari_Newyear = 587
    F_Akari_Newyear2 = 588
    RemedialClass = 589
    Meihuayuan = 590
    TrainingClub = 591
    RedwinterSecretary = 592
    HoukagoDessert = 593
    BookClub = 594
    SisterHood = 595
    RabbitPlatoon = 596
    Class227 = 597
    KnightsHospitaller = 598
    TeaParty = 599
    HotSpringsDepartment = 600
    TrinityVigilance = 601
    anzenkyoku = 602
    PandemoniumSociety = 603
    Endanbou = 604
    Emergentology = 605
    FoodService = 606
    PublicPeaceBureau = 607
    F_Umika = 608
    F_Umika2 = 609
    F_Tsubaki_Guide = 610
    F_Tsubaki_Guide2 = 611
    EventChallenge_Turret = 612
    HyakkiyakoMatsuriScore = 613
    AbydosCD = 614
    AbydosBook = 615
    FireworkFireDevice = 616
    FireworkFireDeviceMaster = 617
    F_Kazusa_Band = 618
    F_Kazusa_Band2 = 619
    F_Yoshimi_Band = 620
    F_Yoshimi_Band2 = 621
    F_Airi_Band = 622
    F_Airi_Band2 = 623
    F_Kirara = 624
    F_Kirara2 = 625
    ShinySparkleSociety = 626
    F_Momoi_Maid = 627
    F_Momoi_Maid2 = 628
    F_Midori_Maid = 629
    F_Midori_Maid2 = 630
    F_Serika_Swimsuit = 631
    F_Serika_Swimsuit2 = 632
    F_Kanna_Swimsuit = 633
    F_Kanna_Swimsuit2 = 634
    F_Moe_Swimsuit = 635
    F_Moe_Swimsuit2 = 636
    F_Fubuki_Swimsuit = 637
    F_Fubuki_Swimsuit2 = 638
    F_Kirino_Swimsuit = 639
    F_Kirino_Swimsuit2 = 640
    F_Hoshino_HWS = 641
    F_Hoshino_HWS2 = 642
    F_Shiroko_Terror = 643
    F_Shiroko_Terror2 = 644
    F_Saori_Swimsuit = 645
    F_Saori_Swimsuit2 = 646
    F_Hiyori_Swimsuit = 647
    F_Hiyori_Swimsuit2 = 648
    F_Atsuko_Swimsuit = 649
    F_Atsuko_Swimsuit2 = 650
    AbydosStudentCouncil = 651
    F_Marina_Qipao = 652
    F_Marina_Qipao2 = 653
    F_Tomoe_Qipao = 654
    F_Tomoe_Qipao2 = 655
    Haruhabara = 656
    ObjectA = 657
    ObjectB = 658
    F_Reizyo = 659
    F_Reizyo2 = 660
    F_Kisaki = 661
    F_Kisaki2 = 662
    F_Mari_Idol = 663
    F_Mari_Idol2 = 664
    F_Sakurako_Idol = 665
    F_Sakurako_Idol2 = 666
    F_Mine_Idol = 667
    F_Mine_Idol2 = 668
    En0009_Section01 = 669
    En0009_Section02 = 670
    En0009_Section03 = 671
    En0009_Section04 = 672
    En0009_Section05 = 673
    AntiqueSeraphim = 674
    F_CH0238_1 = 675
    F_CH0238_2 = 676
    F_CH0080_1 = 677
    F_CH0080_2 = 678
    F_CH0284_1 = 679
    F_CH0284_2 = 680
    F_CH0285_1 = 681
    F_CH0285_2 = 682
    En0010_Heater = 683
    F_CH0070_1 = 684
    F_CH0281_1 = 685
    F_CH0282_1 = 686
    F_CH0158_1 = 687
    F_CH0280_1 = 688
    F_CH0235_1 = 689
    F_CH0070_2 = 690
    F_CH0281_2 = 691
    F_CH0282_2 = 692
    F_CH0158_2 = 693
    F_CH0280_2 = 694
    F_CH0235_2 = 695
    Raid_Lunatic = 696
    F_CH0082_1 = 697
    F_CH0082_2 = 698
    F_CH0286_1 = 699
    F_CH0286_2 = 700
    F_CH0197_1 = 701
    F_CH0197_2 = 702
    F_CH0245_1 = 703
    F_CH0245_2 = 704
    F_CH0259_1 = 705
    F_CH0259_2 = 706
    F_CH0287_1 = 707
    F_CH0287_2 = 708
    EN0011_Section01 = 709
    EN0011_Section02 = 710
    EN0011_Section03 = 711
    EN0011_Section04 = 712
    EN0011_Section05 = 713
    EN0011_Boss = 714
    EN0011_SubCoreBlue = 715
    EN0011_SubCoreRed = 716
    EN0011_SubCoreYellow = 717
    EN0011_Summoned = 718
    EN0011_Path = 719
    EN0011_SubCore = 720
    EN0011_Dummy = 721
    CentralControlCenter = 722
    FreightLogisticsDepartment = 723
    F_CH0242_1 = 724
    F_CH0242_2 = 725
    F_CH0243_1 = 726
    F_CH0243_2 = 727
    F_CH0288_1 = 728
    F_CH0288_2 = 729
    F_CH0257_1 = 730
    F_CH0257_2 = 731
    CCCTwins = 732
    HyakkiyakoCD = 733
    HyakkiyakoBook = 734
    F_CH0221_1 = 735
    F_CH0221_2 = 736
    F_CH0109_1 = 737
    F_CH0109_2 = 738
    F_CH0222_1 = 739
    F_CH0222_2 = 740
    F_CH0301_1 = 741
    F_CH0301_2 = 742
    F_CH0302_1 = 743
    F_CH0302_2 = 744
    F_CH0300_1 = 745
    F_CH0300_2 = 746
    Momoi = 747
    F_CH0294_1 = 748
    F_CH0294_2 = 749
    F_CH0295_1 = 750
    F_CH0295_2 = 751
    F_CH0291_1 = 752
    F_CH0291_2 = 753
    F_CH0293_1 = 754
    F_CH0293_2 = 755
    F_CH0292_1 = 756
    F_CH0292_2 = 757
    Wildhunt = 758
    OccultClub = 759
    PrefectBrigade = 760
    F_CH0304_1 = 761
    F_CH0304_2 = 762
    F_CH0306_1 = 763
    F_CH0306_2 = 764
    F_CH0268_1 = 765
    F_CH0268_2 = 766
    FreeTradeCartel = 767
    F_CH0317_1 = 768
    F_CH0317_2 = 769
    F_CH0318_1 = 770
    F_CH0318_2 = 771
    F_CH0319_1 = 772
    F_CH0319_2 = 773
    CraftMaterialItem = 774
    EtcItem = 775
    NicomediasTroop = 776
    AriusSquad = 777
    ReisaMagical = 778
    F_CH0325_1 = 779
    F_CH0325_2 = 780
    F_CH0309_1 = 781
    F_CH0309_2 = 782
    F_CH0166_1 = 783
    F_CH0166_2 = 784
    F_CH0326_1 = 785
    F_CH0326_2 = 786
    EN0013_Block = 787
    EN0013_Reset = 788
    EN0013_RealBoss = 789
    EN0013_GrayCore = 790
    EN0013_BlackCore = 791
    EN0013_DroneSlot1 = 792
    EN0013_DroneSlot2 = 793
    EN0013_DroneSlot3 = 794
    EN0013_DroneSlot4 = 795
    PublishingDepartment = 796
    FrenapatisCard = 797
    RabuHelmet = 798
    F_CH0228_1 = 799
    F_CH0228_2 = 800
    F_CH0229_1 = 801
    F_CH0229_2 = 802
    F_CH0296_1 = 803
    F_CH0296_2 = 804
    F_CH0297_1 = 805
    F_CH0297_2 = 806
    WorldRaid_01 = 807
    WorldRaid_02 = 808
    WorldRaid_03 = 809
    WorldRaid_04 = 810
    F_CH0331_1 = 811
    F_CH0331_2 = 812
    F_CH0334_1 = 813
    F_CH0334_2 = 814
    F_CH0335_1 = 815
    F_CH0335_2 = 816
    F_CH0333_1 = 817
    F_CH0333_2 = 818
    F_CH0332_1 = 819
    F_CH0332_2 = 820
    EN0020_SpawnDummy = 821
    EN0020_Visual = 822
    EN0020_Jyaco = 823
    EN0020_Gauge = 824
    WorldRaid_A = 825
    WorldRaid_B = 826
    WorldRaid_C = 827
    WorldRaid_D = 828
    F_CH0337_1 = 829
    F_CH0337_2 = 830
    F_CH0336_1 = 831
    F_CH0336_2 = 832
    F_CH0310_1 = 833
    F_CH0310_2 = 834
    TagName0833 = 835
    TagName0834 = 836
    TagName0835 = 837
    TagName0836 = 838
    TagName0837 = 839
    TagName0838 = 840
    TagName0839 = 841
    TagName0840 = 842
    TagName0841 = 843
    TagName0842 = 844
    TagName0843 = 845
    TagName0844 = 846
    TagName0845 = 847
    TagName0846 = 848
    TagName0847 = 849
    TagName0848 = 850
    TagName0849 = 851
    TagName0850 = 852
    TagName0851 = 853
    TagName0852 = 854
    TagName0853 = 855
    TagName0854 = 856
    TagName0855 = 857
    TagName0856 = 858
    TagName0857 = 859
    TagName0858 = 860
    TagName0859 = 861
    TagName0860 = 862
    TagName0861 = 863
    TagName0862 = 864
    TagName0863 = 865
    TagName0864 = 866
    TagName0865 = 867
    TagName0866 = 868
    TagName0867 = 869
    TagName0868 = 870
    TagName0869 = 871
    TagName0870 = 872
    TagName0871 = 873
    TagName0872 = 874
    TagName0873 = 875
    TagName0874 = 876
    TagName0875 = 877
    TagName0876 = 878
    TagName0877 = 879
    TagName0878 = 880
    TagName0879 = 881
    TagName0880 = 882
    TagName0881 = 883
    TagName0882 = 884
    TagName0883 = 885
    TagName0884 = 886
    TagName0885 = 887
    TagName0886 = 888
    TagName0887 = 889
    TagName0888 = 890
    TagName0889 = 891
    TagName0890 = 892
    TagName0891 = 893
    TagName0892 = 894
    TagName0893 = 895
    TagName0894 = 896
    TagName0895 = 897
    TagName0896 = 898
    TagName0897 = 899
    TagName0898 = 900
    TagName0899 = 901
    TagName0900 = 902
    TagName0901 = 903
    TagName0902 = 904
    TagName0903 = 905
    TagName0904 = 906
    TagName0905 = 907
    TagName0906 = 908
    TagName0907 = 909
    TagName0908 = 910
    TagName0909 = 911
    TagName0910 = 912
    TagName0911 = 913
    TagName0912 = 914
    TagName0913 = 915
    TagName0914 = 916
    TagName0915 = 917
    TagName0916 = 918
    TagName0917 = 919
    TagName0918 = 920
    TagName0919 = 921
    TagName0920 = 922
    TagName0921 = 923
    TagName0922 = 924
    TagName0923 = 925
    TagName0924 = 926
    TagName0925 = 927
    TagName0926 = 928
    TagName0927 = 929
    TagName0928 = 930
    TagName0929 = 931
    TagName0930 = 932
    TagName0931 = 933
    TagName0932 = 934
    TagName0933 = 935
    TagName0934 = 936
    TagName0935 = 937
    TagName0936 = 938
    TagName0937 = 939
    TagName0938 = 940
    TagName0939 = 941
    TagName0940 = 942
    TagName0941 = 943
    TagName0942 = 944
    TagName0943 = 945
    TagName0944 = 946
    TagName0945 = 947
    TagName0946 = 948
    TagName0947 = 949
    TagName0948 = 950
    TagName0949 = 951
    TagName0950 = 952
    TagName0951 = 953
    TagName0952 = 954
    TagName0953 = 955
    TagName0954 = 956
    TagName0955 = 957
    TagName0956 = 958
    TagName0957 = 959
    TagName0958 = 960
    TagName0959 = 961
    TagName0960 = 962
    TagName0961 = 963
    TagName0962 = 964
    TagName0963 = 965
    TagName0964 = 966
    TagName0965 = 967
    TagName0966 = 968
    TagName0967 = 969
    TagName0968 = 970
    TagName0969 = 971
    TagName0970 = 972
    TagName0971 = 973
    TagName0972 = 974
    TagName0973 = 975
    TagName0974 = 976
    TagName0975 = 977
    TagName0976 = 978
    TagName0977 = 979
    TagName0978 = 980
    TagName0979 = 981
    TagName0980 = 982
    TagName0981 = 983
    TagName0982 = 984
    TagName0983 = 985
    TagName0984 = 986
    TagName0985 = 987
    TagName0986 = 988
    TagName0987 = 989
    TagName0988 = 990
    TagName0989 = 991
    TagName0990 = 992
    TagName0991 = 993
    TagName0992 = 994
    TagName0993 = 995
    TagName0994 = 996
    TagName0995 = 997
    TagName0996 = 998
    TagName0997 = 999
    TagName0998 = 1000
    TagName0999 = 1001
    TagName1000 = 1002
    TagName1001 = 1003
    TagName1002 = 1004
    TagName1003 = 1005
    TagName1004 = 1006
    TagName1005 = 1007
    TagName1006 = 1008
    TagName1007 = 1009
    TagName1008 = 1010
    TagName1009 = 1011
    TagName1010 = 1012
    TagName1011 = 1013
    TagName1012 = 1014
    TagName1013 = 1015
    TagName1014 = 1016
    TagName1015 = 1017
    TagName1016 = 1018
    TagName1017 = 1019
    TagName1018 = 1020
    TagName1019 = 1021
    TagName1020 = 1022
    TagName1021 = 1023
    TagName1022 = 1024
    TagName1023 = 1025
    TagName1024 = 1026
    TagName1025 = 1027
    TagName1026 = 1028
    TagName1027 = 1029
    TagName1028 = 1030
    TagName1029 = 1031
    TagName1030 = 1032
    TagName1031 = 1033
    TagName1032 = 1034
    TagName1033 = 1035
    TagName1034 = 1036
    TagName1035 = 1037
    TagName1036 = 1038
    TagName1037 = 1039
    TagName1038 = 1040
    TagName1039 = 1041
    TagName1040 = 1042
    TagName1041 = 1043
    TagName1042 = 1044
    TagName1043 = 1045
    TagName1044 = 1046
    TagName1045 = 1047
    TagName1046 = 1048
    TagName1047 = 1049
    TagName1048 = 1050
    TagName1049 = 1051
    TagName1050 = 1052
    TagName1051 = 1053
    TagName1052 = 1054
    TagName1053 = 1055
    TagName1054 = 1056
    TagName1055 = 1057
    TagName1056 = 1058
    TagName1057 = 1059
    TagName1058 = 1060
    TagName1059 = 1061
    TagName1060 = 1062
    TagName1061 = 1063
    TagName1062 = 1064
    TagName1063 = 1065
    TagName1064 = 1066
    TagName1065 = 1067
    TagName1066 = 1068
    TagName1067 = 1069
    TagName1068 = 1070
    TagName1069 = 1071
    TagName1070 = 1072
    TagName1071 = 1073
    TagName1072 = 1074
    TagName1073 = 1075
    TagName1074 = 1076
    TagName1075 = 1077
    TagName1076 = 1078
    TagName1077 = 1079
    TagName1078 = 1080
    TagName1079 = 1081
    TagName1080 = 1082
    TagName1081 = 1083
    TagName1082 = 1084
    TagName1083 = 1085
    TagName1084 = 1086
    TagName1085 = 1087
    TagName1086 = 1088
    TagName1087 = 1089
    TagName1088 = 1090
    TagName1089 = 1091
    TagName1090 = 1092
    TagName1091 = 1093
    TagName1092 = 1094
    TagName1093 = 1095
    TagName1094 = 1096
    TagName1095 = 1097
    TagName1096 = 1098
    TagName1097 = 1099
    TagName1098 = 1100
    TagName1099 = 1101
    TagName1100 = 1102
    TagName1101 = 1103
    TagName1102 = 1104
    TagName1103 = 1105
    TagName1104 = 1106
    TagName1105 = 1107
    TagName1106 = 1108
    TagName1107 = 1109
    TagName1108 = 1110
    TagName1109 = 1111
    TagName1110 = 1112
    TagName1111 = 1113
    TagName1112 = 1114
    TagName1113 = 1115
    TagName1114 = 1116
    TagName1115 = 1117
    TagName1116 = 1118
    TagName1117 = 1119
    TagName1118 = 1120
    TagName1119 = 1121
    TagName1120 = 1122
    TagName1121 = 1123
    TagName1122 = 1124
    TagName1123 = 1125
    TagName1124 = 1126
    TagName1125 = 1127
    TagName1126 = 1128
    TagName1127 = 1129
    TagName1128 = 1130
    TagName1129 = 1131
    TagName1130 = 1132
    TagName1131 = 1133
    TagName1132 = 1134
    TagName1133 = 1135
    TagName1134 = 1136
    TagName1135 = 1137
    TagName1136 = 1138
    TagName1137 = 1139
    TagName1138 = 1140
    TagName1139 = 1141
    TagName1140 = 1142
    TagName1141 = 1143
    TagName1142 = 1144
    TagName1143 = 1145
    TagName1144 = 1146
    TagName1145 = 1147
    TagName1146 = 1148
    TagName1147 = 1149
    TagName1148 = 1150
    TagName1149 = 1151
    TagName1150 = 1152
    TagName1151 = 1153
    TagName1152 = 1154
    TagName1153 = 1155
    TagName1154 = 1156
    TagName1155 = 1157
    TagName1156 = 1158
    TagName1157 = 1159
    TagName1158 = 1160
    TagName1159 = 1161
    TagName1160 = 1162
    TagName1161 = 1163
    TagName1162 = 1164
    TagName1163 = 1165
    TagName1164 = 1166
    TagName1165 = 1167
    TagName1166 = 1168
    TagName1167 = 1169
    TagName1168 = 1170
    TagName1169 = 1171
    TagName1170 = 1172
    TagName1171 = 1173
    TagName1172 = 1174
    TagName1173 = 1175
    TagName1174 = 1176
    TagName1175 = 1177
    TagName1176 = 1178
    TagName1177 = 1179
    TagName1178 = 1180
    TagName1179 = 1181
    TagName1180 = 1182
    TagName1181 = 1183
    TagName1182 = 1184
    TagName1183 = 1185
    TagName1184 = 1186
    TagName1185 = 1187
    TagName1186 = 1188
    TagName1187 = 1189
    TagName1188 = 1190
    TagName1189 = 1191
    TagName1190 = 1192
    TagName1191 = 1193
    TagName1192 = 1194
    TagName1193 = 1195
    TagName1194 = 1196
    TagName1195 = 1197
    TagName1196 = 1198
    TagName1197 = 1199
    TagName1198 = 1200
    TagName1199 = 1201
    TagName1200 = 1202
    TagName1201 = 1203
    TagName1202 = 1204
    TagName1203 = 1205
    TagName1204 = 1206
    TagName1205 = 1207
    TagName1206 = 1208
    TagName1207 = 1209
    TagName1208 = 1210
    TagName1209 = 1211
    TagName1210 = 1212
    TagName1211 = 1213
    TagName1212 = 1214
    TagName1213 = 1215
    TagName1214 = 1216
    TagName1215 = 1217
    TagName1216 = 1218
    TagName1217 = 1219
    TagName1218 = 1220
    TagName1219 = 1221
    TagName1220 = 1222
    TagName1221 = 1223
    TagName1222 = 1224
    TagName1223 = 1225
    TagName1224 = 1226
    TagName1225 = 1227
    TagName1226 = 1228
    TagName1227 = 1229
    TagName1228 = 1230
    TagName1229 = 1231
    TagName1230 = 1232
    TagName1231 = 1233
    TagName1232 = 1234
    TagName1233 = 1235
    TagName1234 = 1236
    TagName1235 = 1237
    TagName1236 = 1238
    TagName1237 = 1239
    TagName1238 = 1240
    TagName1239 = 1241
    TagName1240 = 1242
    TagName1241 = 1243
    TagName1242 = 1244
    TagName1243 = 1245
    TagName1244 = 1246
    TagName1245 = 1247
    TagName1246 = 1248
    TagName1247 = 1249
    TagName1248 = 1250
    TagName1249 = 1251
    TagName1250 = 1252
    TagName1251 = 1253
    TagName1252 = 1254
    TagName1253 = 1255
    TagName1254 = 1256
    TagName1255 = 1257
    TagName1256 = 1258
    TagName1257 = 1259
    TagName1258 = 1260
    TagName1259 = 1261
    TagName1260 = 1262
    TagName1261 = 1263
    TagName1262 = 1264
    TagName1263 = 1265
    TagName1264 = 1266
    TagName1265 = 1267
    TagName1266 = 1268
    TagName1267 = 1269
    TagName1268 = 1270
    TagName1269 = 1271
    TagName1270 = 1272
    TagName1271 = 1273
    TagName1272 = 1274
    TagName1273 = 1275
    TagName1274 = 1276
    TagName1275 = 1277
    TagName1276 = 1278
    TagName1277 = 1279
    TagName1278 = 1280
    TagName1279 = 1281
    TagName1280 = 1282
    TagName1281 = 1283
    TagName1282 = 1284
    TagName1283 = 1285
    TagName1284 = 1286
    TagName1285 = 1287
    TagName1286 = 1288
    TagName1287 = 1289
    TagName1288 = 1290
    TagName1289 = 1291
    TagName1290 = 1292
    TagName1291 = 1293
    TagName1292 = 1294
    TagName1293 = 1295
    TagName1294 = 1296
    TagName1295 = 1297
    TagName1296 = 1298
    TagName1297 = 1299
    TagName1298 = 1300
    TagName1299 = 1301
    TagName1300 = 1302
    TagName1301 = 1303
    TagName1302 = 1304
    TagName1303 = 1305
    TagName1304 = 1306
    TagName1305 = 1307
    TagName1306 = 1308
    TagName1307 = 1309
    TagName1308 = 1310
    TagName1309 = 1311
    TagName1310 = 1312
    TagName1311 = 1313
    TagName1312 = 1314
    TagName1313 = 1315
    TagName1314 = 1316
    TagName1315 = 1317
    TagName1316 = 1318
    TagName1317 = 1319
    TagName1318 = 1320
    TagName1319 = 1321
    TagName1320 = 1322
    TagName1321 = 1323
    TagName1322 = 1324
    TagName1323 = 1325
    TagName1324 = 1326
    TagName1325 = 1327
    TagName1326 = 1328
    TagName1327 = 1329
    TagName1328 = 1330
    TagName1329 = 1331
    TagName1330 = 1332
    TagName1331 = 1333
    TagName1332 = 1334
    TagName1333 = 1335
    TagName1334 = 1336
    TagName1335 = 1337
    TagName1336 = 1338
    TagName1337 = 1339
    TagName1338 = 1340
    TagName1339 = 1341
    TagName1340 = 1342
    TagName1341 = 1343
    TagName1342 = 1344
    TagName1343 = 1345
    TagName1344 = 1346
    TagName1345 = 1347
    TagName1346 = 1348
    TagName1347 = 1349
    TagName1348 = 1350
    TagName1349 = 1351
    TagName1350 = 1352
    TagName1351 = 1353
    TagName1352 = 1354
    TagName1353 = 1355
    TagName1354 = 1356
    TagName1355 = 1357
    TagName1356 = 1358
    TagName1357 = 1359
    TagName1358 = 1360
    TagName1359 = 1361
    TagName1360 = 1362
    TagName1361 = 1363
    TagName1362 = 1364
    TagName1363 = 1365
    TagName1364 = 1366
    TagName1365 = 1367
    TagName1366 = 1368
    TagName1367 = 1369
    TagName1368 = 1370
    TagName1369 = 1371
    TagName1370 = 1372
    TagName1371 = 1373
    TagName1372 = 1374
    TagName1373 = 1375
    TagName1374 = 1376
    TagName1375 = 1377
    TagName1376 = 1378
    TagName1377 = 1379
    TagName1378 = 1380
    TagName1379 = 1381
    TagName1380 = 1382
    TagName1381 = 1383
    TagName1382 = 1384
    TagName1383 = 1385
    TagName1384 = 1386
    TagName1385 = 1387
    TagName1386 = 1388
    TagName1387 = 1389
    TagName1388 = 1390
    TagName1389 = 1391
    TagName1390 = 1392
    TagName1391 = 1393
    TagName1392 = 1394
    TagName1393 = 1395
    TagName1394 = 1396
    TagName1395 = 1397
    TagName1396 = 1398
    TagName1397 = 1399
    TagName1398 = 1400
    TagName1399 = 1401
    TagName1400 = 1402
    TagName1401 = 1403
    TagName1402 = 1404
    TagName1403 = 1405
    TagName1404 = 1406
    TagName1405 = 1407
    TagName1406 = 1408
    TagName1407 = 1409
    TagName1408 = 1410
    TagName1409 = 1411
    TagName1410 = 1412
    TagName1411 = 1413
    TagName1412 = 1414
    TagName1413 = 1415
    TagName1414 = 1416
    TagName1415 = 1417
    TagName1416 = 1418
    TagName1417 = 1419
    TagName1418 = 1420
    TagName1419 = 1421
    TagName1420 = 1422
    TagName1421 = 1423
    TagName1422 = 1424
    TagName1423 = 1425
    TagName1424 = 1426
    TagName1425 = 1427
    TagName1426 = 1428
    TagName1427 = 1429
    TagName1428 = 1430
    TagName1429 = 1431
    TagName1430 = 1432
    TagName1431 = 1433
    TagName1432 = 1434
    TagName1433 = 1435
    TagName1434 = 1436
    TagName1435 = 1437
    TagName1436 = 1438
    TagName1437 = 1439
    TagName1438 = 1440
    TagName1439 = 1441
    TagName1440 = 1442
    TagName1441 = 1443
    TagName1442 = 1444
    TagName1443 = 1445
    TagName1444 = 1446
    TagName1445 = 1447
    TagName1446 = 1448
    TagName1447 = 1449
    TagName1448 = 1450
    TagName1449 = 1451
    TagName1450 = 1452
    TagName1451 = 1453
    TagName1452 = 1454
    TagName1453 = 1455
    TagName1454 = 1456
    TagName1455 = 1457
    TagName1456 = 1458
    TagName1457 = 1459
    TagName1458 = 1460
    TagName1459 = 1461
    TagName1460 = 1462
    TagName1461 = 1463
    TagName1462 = 1464
    TagName1463 = 1465
    TagName1464 = 1466
    TagName1465 = 1467
    TagName1466 = 1468
    TagName1467 = 1469
    TagName1468 = 1470
    TagName1469 = 1471
    TagName1470 = 1472
    TagName1471 = 1473
    TagName1472 = 1474
    TagName1473 = 1475
    TagName1474 = 1476
    TagName1475 = 1477
    TagName1476 = 1478
    TagName1477 = 1479
    TagName1478 = 1480
    TagName1479 = 1481
    TagName1480 = 1482
    TagName1481 = 1483
    TagName1482 = 1484
    TagName1483 = 1485
    TagName1484 = 1486
    TagName1485 = 1487
    TagName1486 = 1488
    TagName1487 = 1489
    TagName1488 = 1490
    TagName1489 = 1491
    TagName1490 = 1492
    TagName1491 = 1493
    TagName1492 = 1494
    TagName1493 = 1495
    TagName1494 = 1496
    TagName1495 = 1497
    TagName1496 = 1498
    TagName1497 = 1499
    TagName1498 = 1500
    TagName1499 = 1501
    TagName1500 = 1502
    TagName1501 = 1503
    TagName1502 = 1504
    TagName1503 = 1505
    TagName1504 = 1506
    TagName1505 = 1507
    TagName1506 = 1508
    TagName1507 = 1509
    TagName1508 = 1510
    TagName1509 = 1511
    TagName1510 = 1512
    TagName1511 = 1513
    TagName1512 = 1514
    TagName1513 = 1515
    TagName1514 = 1516
    TagName1515 = 1517
    TagName1516 = 1518
    TagName1517 = 1519
    TagName1518 = 1520
    TagName1519 = 1521
    TagName1520 = 1522
    TagName1521 = 1523
    TagName1522 = 1524
    TagName1523 = 1525
    TagName1524 = 1526
    TagName1525 = 1527
    TagName1526 = 1528
    TagName1527 = 1529
    TagName1528 = 1530
    TagName1529 = 1531
    TagName1530 = 1532
    TagName1531 = 1533
    TagName1532 = 1534
    TagName1533 = 1535
    TagName1534 = 1536
    TagName1535 = 1537
    TagName1536 = 1538
    TagName1537 = 1539
    TagName1538 = 1540
    TagName1539 = 1541
    TagName1540 = 1542
    TagName1541 = 1543
    TagName1542 = 1544
    TagName1543 = 1545
    TagName1544 = 1546
    TagName1545 = 1547
    TagName1546 = 1548
    TagName1547 = 1549
    TagName1548 = 1550
    TagName1549 = 1551
    TagName1550 = 1552
    TagName1551 = 1553
    TagName1552 = 1554
    TagName1553 = 1555
    TagName1554 = 1556
    TagName1555 = 1557
    TagName1556 = 1558
    TagName1557 = 1559
    TagName1558 = 1560
    TagName1559 = 1561
    TagName1560 = 1562
    TagName1561 = 1563
    TagName1562 = 1564
    TagName1563 = 1565
    TagName1564 = 1566
    TagName1565 = 1567
    TagName1566 = 1568
    TagName1567 = 1569
    TagName1568 = 1570
    TagName1569 = 1571
    TagName1570 = 1572
    TagName1571 = 1573
    TagName1572 = 1574
    TagName1573 = 1575
    TagName1574 = 1576
    TagName1575 = 1577
    TagName1576 = 1578
    TagName1577 = 1579
    TagName1578 = 1580
    TagName1579 = 1581
    TagName1580 = 1582
    TagName1581 = 1583
    TagName1582 = 1584
    TagName1583 = 1585
    TagName1584 = 1586
    TagName1585 = 1587
    TagName1586 = 1588
    TagName1587 = 1589
    TagName1588 = 1590
    TagName1589 = 1591
    TagName1590 = 1592
    TagName1591 = 1593
    TagName1592 = 1594
    TagName1593 = 1595
    TagName1594 = 1596
    TagName1595 = 1597
    TagName1596 = 1598
    TagName1597 = 1599
    TagName1598 = 1600
    TagName1599 = 1601
    TagName1600 = 1602
    TagName1601 = 1603
    TagName1602 = 1604
    TagName1603 = 1605
    TagName1604 = 1606
    TagName1605 = 1607
    TagName1606 = 1608
    TagName1607 = 1609
    TagName1608 = 1610
    TagName1609 = 1611
    TagName1610 = 1612
    TagName1611 = 1613
    TagName1612 = 1614
    TagName1613 = 1615
    TagName1614 = 1616
    TagName1615 = 1617
    TagName1616 = 1618
    TagName1617 = 1619
    TagName1618 = 1620
    TagName1619 = 1621
    TagName1620 = 1622
    TagName1621 = 1623
    TagName1622 = 1624
    TagName1623 = 1625
    TagName1624 = 1626
    TagName1625 = 1627
    TagName1626 = 1628
    TagName1627 = 1629
    TagName1628 = 1630
    TagName1629 = 1631
    TagName1630 = 1632
    TagName1631 = 1633
    TagName1632 = 1634
    TagName1633 = 1635
    TagName1634 = 1636
    TagName1635 = 1637
    TagName1636 = 1638
    TagName1637 = 1639
    TagName1638 = 1640
    TagName1639 = 1641
    TagName1640 = 1642
    TagName1641 = 1643
    TagName1642 = 1644
    TagName1643 = 1645
    TagName1644 = 1646
    TagName1645 = 1647
    TagName1646 = 1648
    TagName1647 = 1649
    TagName1648 = 1650
    TagName1649 = 1651
    TagName1650 = 1652
    TagName1651 = 1653
    TagName1652 = 1654
    TagName1653 = 1655
    TagName1654 = 1656
    TagName1655 = 1657
    TagName1656 = 1658
    TagName1657 = 1659
    TagName1658 = 1660
    TagName1659 = 1661
    TagName1660 = 1662
    TagName1661 = 1663
    TagName1662 = 1664
    TagName1663 = 1665
    TagName1664 = 1666
    TagName1665 = 1667
    TagName1666 = 1668
    TagName1667 = 1669
    TagName1668 = 1670
    TagName1669 = 1671
    TagName1670 = 1672
    TagName1671 = 1673
    TagName1672 = 1674
    TagName1673 = 1675
    TagName1674 = 1676
    TagName1675 = 1677
    TagName1676 = 1678
    TagName1677 = 1679
    TagName1678 = 1680
    TagName1679 = 1681
    TagName1680 = 1682
    TagName1681 = 1683
    TagName1682 = 1684
    TagName1683 = 1685
    TagName1684 = 1686
    TagName1685 = 1687
    TagName1686 = 1688
    TagName1687 = 1689
    TagName1688 = 1690
    TagName1689 = 1691
    TagName1690 = 1692
    TagName1691 = 1693
    TagName1692 = 1694
    TagName1693 = 1695
    TagName1694 = 1696
    TagName1695 = 1697
    TagName1696 = 1698
    TagName1697 = 1699
    TagName1698 = 1700
    TagName1699 = 1701
    TagName1700 = 1702
    TagName1701 = 1703
    TagName1702 = 1704
    TagName1703 = 1705
    TagName1704 = 1706
    TagName1705 = 1707
    TagName1706 = 1708
    TagName1707 = 1709
    TagName1708 = 1710
    TagName1709 = 1711
    TagName1710 = 1712
    TagName1711 = 1713
    TagName1712 = 1714
    TagName1713 = 1715
    TagName1714 = 1716
    TagName1715 = 1717
    TagName1716 = 1718
    TagName1717 = 1719
    TagName1718 = 1720
    TagName1719 = 1721
    TagName1720 = 1722
    TagName1721 = 1723
    TagName1722 = 1724
    TagName1723 = 1725
    TagName1724 = 1726
    TagName1725 = 1727
    TagName1726 = 1728
    TagName1727 = 1729
    TagName1728 = 1730
    TagName1729 = 1731
    TagName1730 = 1732
    TagName1731 = 1733
    TagName1732 = 1734
    TagName1733 = 1735
    TagName1734 = 1736
    TagName1735 = 1737
    TagName1736 = 1738
    TagName1737 = 1739
    TagName1738 = 1740
    TagName1739 = 1741
    TagName1740 = 1742
    TagName1741 = 1743
    TagName1742 = 1744
    TagName1743 = 1745
    TagName1744 = 1746
    TagName1745 = 1747
    TagName1746 = 1748
    TagName1747 = 1749
    TagName1748 = 1750
    TagName1749 = 1751
    TagName1750 = 1752
    TagName1751 = 1753
    TagName1752 = 1754
    TagName1753 = 1755
    TagName1754 = 1756
    TagName1755 = 1757
    TagName1756 = 1758
    TagName1757 = 1759
    TagName1758 = 1760
    TagName1759 = 1761
    TagName1760 = 1762
    TagName1761 = 1763
    TagName1762 = 1764
    TagName1763 = 1765
    TagName1764 = 1766
    TagName1765 = 1767
    TagName1766 = 1768
    TagName1767 = 1769
    TagName1768 = 1770
    TagName1769 = 1771
    TagName1770 = 1772
    TagName1771 = 1773
    TagName1772 = 1774
    TagName1773 = 1775
    TagName1774 = 1776
    TagName1775 = 1777
    TagName1776 = 1778
    TagName1777 = 1779
    TagName1778 = 1780
    TagName1779 = 1781
    TagName1780 = 1782
    TagName1781 = 1783
    TagName1782 = 1784
    TagName1783 = 1785
    TagName1784 = 1786
    TagName1785 = 1787
    TagName1786 = 1788
    TagName1787 = 1789
    TagName1788 = 1790
    TagName1789 = 1791
    TagName1790 = 1792
    TagName1791 = 1793
    TagName1792 = 1794
    TagName1793 = 1795
    TagName1794 = 1796
    TagName1795 = 1797
    TagName1796 = 1798
    TagName1797 = 1799
    TagName1798 = 1800
    TagName1799 = 1801
    TagName1800 = 1802
    TagName1801 = 1803
    TagName1802 = 1804
    TagName1803 = 1805
    TagName1804 = 1806
    TagName1805 = 1807
    TagName1806 = 1808
    TagName1807 = 1809
    TagName1808 = 1810
    TagName1809 = 1811
    TagName1810 = 1812
    TagName1811 = 1813
    TagName1812 = 1814
    TagName1813 = 1815
    TagName1814 = 1816
    TagName1815 = 1817
    TagName1816 = 1818
    TagName1817 = 1819
    TagName1818 = 1820
    TagName1819 = 1821
    TagName1820 = 1822
    TagName1821 = 1823
    TagName1822 = 1824
    TagName1823 = 1825
    TagName1824 = 1826
    TagName1825 = 1827
    TagName1826 = 1828
    TagName1827 = 1829
    TagName1828 = 1830
    TagName1829 = 1831
    TagName1830 = 1832
    TagName1831 = 1833
    TagName1832 = 1834
    TagName1833 = 1835
    TagName1834 = 1836
    TagName1835 = 1837
    TagName1836 = 1838
    TagName1837 = 1839
    TagName1838 = 1840
    TagName1839 = 1841
    TagName1840 = 1842
    TagName1841 = 1843
    TagName1842 = 1844
    TagName1843 = 1845
    TagName1844 = 1846
    TagName1845 = 1847
    TagName1846 = 1848
    TagName1847 = 1849
    TagName1848 = 1850
    TagName1849 = 1851
    TagName1850 = 1852
    TagName1851 = 1853
    TagName1852 = 1854
    TagName1853 = 1855
    TagName1854 = 1856
    TagName1855 = 1857
    TagName1856 = 1858
    TagName1857 = 1859
    TagName1858 = 1860
    TagName1859 = 1861
    TagName1860 = 1862
    TagName1861 = 1863
    TagName1862 = 1864
    TagName1863 = 1865
    TagName1864 = 1866
    TagName1865 = 1867
    TagName1866 = 1868
    TagName1867 = 1869
    TagName1868 = 1870
    TagName1869 = 1871
    TagName1870 = 1872
    TagName1871 = 1873
    TagName1872 = 1874
    TagName1873 = 1875
    TagName1874 = 1876
    TagName1875 = 1877
    TagName1876 = 1878
    TagName1877 = 1879
    TagName1878 = 1880
    TagName1879 = 1881
    TagName1880 = 1882
    TagName1881 = 1883
    TagName1882 = 1884
    TagName1883 = 1885
    TagName1884 = 1886
    TagName1885 = 1887
    TagName1886 = 1888
    TagName1887 = 1889
    TagName1888 = 1890
    TagName1889 = 1891
    TagName1890 = 1892
    TagName1891 = 1893
    TagName1892 = 1894
    TagName1893 = 1895
    TagName1894 = 1896
    TagName1895 = 1897
    TagName1896 = 1898
    TagName1897 = 1899
    TagName1898 = 1900
    TagName1899 = 1901
    TagName1900 = 1902
    TagName1901 = 1903
    TagName1902 = 1904
    TagName1903 = 1905
    TagName1904 = 1906
    TagName1905 = 1907
    TagName1906 = 1908
    TagName1907 = 1909
    TagName1908 = 1910
    TagName1909 = 1911
    TagName1910 = 1912
    TagName1911 = 1913
    TagName1912 = 1914
    TagName1913 = 1915
    TagName1914 = 1916
    TagName1915 = 1917
    TagName1916 = 1918
    TagName1917 = 1919
    TagName1918 = 1920
    TagName1919 = 1921
    TagName1920 = 1922
    TagName1921 = 1923
    TagName1922 = 1924
    TagName1923 = 1925
    TagName1924 = 1926
    TagName1925 = 1927
    TagName1926 = 1928
    TagName1927 = 1929
    TagName1928 = 1930
    TagName1929 = 1931
    TagName1930 = 1932
    TagName1931 = 1933
    TagName1932 = 1934
    TagName1933 = 1935
    TagName1934 = 1936
    TagName1935 = 1937
    TagName1936 = 1938
    TagName1937 = 1939
    TagName1938 = 1940
    TagName1939 = 1941
    TagName1940 = 1942
    TagName1941 = 1943
    TagName1942 = 1944
    TagName1943 = 1945
    TagName1944 = 1946
    TagName1945 = 1947
    TagName1946 = 1948
    TagName1947 = 1949
    TagName1948 = 1950
    TagName1949 = 1951
    TagName1950 = 1952
    TagName1951 = 1953
    TagName1952 = 1954
    TagName1953 = 1955
    TagName1954 = 1956
    TagName1955 = 1957
    TagName1956 = 1958
    TagName1957 = 1959
    TagName1958 = 1960
    TagName1959 = 1961
    TagName1960 = 1962
    TagName1961 = 1963
    TagName1962 = 1964
    TagName1963 = 1965
    TagName1964 = 1966
    TagName1965 = 1967
    TagName1966 = 1968
    TagName1967 = 1969
    TagName1968 = 1970
    TagName1969 = 1971
    TagName1970 = 1972
    TagName1971 = 1973
    TagName1972 = 1974
    TagName1973 = 1975
    TagName1974 = 1976
    TagName1975 = 1977
    TagName1976 = 1978
    TagName1977 = 1979
    TagName1978 = 1980
    TagName1979 = 1981
    TagName1980 = 1982
    TagName1981 = 1983
    TagName1982 = 1984
    TagName1983 = 1985
    TagName1984 = 1986
    TagName1985 = 1987
    TagName1986 = 1988
    TagName1987 = 1989
    TagName1988 = 1990
    TagName1989 = 1991
    TagName1990 = 1992
    TagName1991 = 1993
    TagName1992 = 1994
    TagName1993 = 1995
    TagName1994 = 1996
    TagName1995 = 1997
    TagName1996 = 1998
    TagName1997 = 1999
    TagName1998 = 2000
    TagName1999 = 2001
    TagName2000 = 2002
    TagName2001 = 2003
    TagName2002 = 2004
    TagName2003 = 2005
    TagName2004 = 2006
    TagName2005 = 2007
    TagName2006 = 2008
    TagName2007 = 2009
    TagName2008 = 2010
    TagName2009 = 2011
    TagName2010 = 2012
    TagName2011 = 2013
    TagName2012 = 2014
    TagName2013 = 2015
    TagName2014 = 2016
    TagName2015 = 2017
    TagName2016 = 2018
    TagName2017 = 2019
    TagName2018 = 2020
    TagName2019 = 2021
    TagName2020 = 2022
    TagName2021 = 2023
    TagName2022 = 2024
    TagName2023 = 2025
    TagName2024 = 2026
    TagName2025 = 2027
    TagName2026 = 2028
    TagName2027 = 2029
    TagName2028 = 2030
    TagName2029 = 2031
    TagName2030 = 2032
    TagName2031 = 2033
    TagName2032 = 2034
    TagName2033 = 2035
    TagName2034 = 2036
    TagName2035 = 2037
    TagName2036 = 2038
    TagName2037 = 2039
    TagName2038 = 2040
    TagName2039 = 2041
    TagName2040 = 2042
    TagName2041 = 2043
    TagName2042 = 2044
    TagName2043 = 2045
    TagName2044 = 2046
    TagName2045 = 2047
    TagName2046 = 2048
    TagName2047 = 2049
    TagName2048 = 2050
    TagName2049 = 2051
    TagName2050 = 2052
    TagName2051 = 2053
    TagName2052 = 2054
    TagName2053 = 2055
    TagName2054 = 2056
    TagName2055 = 2057
    TagName2056 = 2058
    TagName2057 = 2059
    TagName2058 = 2060
    TagName2059 = 2061
    TagName2060 = 2062
    TagName2061 = 2063
    TagName2062 = 2064
    TagName2063 = 2065
    TagName2064 = 2066
    TagName2065 = 2067
    TagName2066 = 2068
    TagName2067 = 2069
    TagName2068 = 2070
    TagName2069 = 2071
    TagName2070 = 2072
    TagName2071 = 2073
    TagName2072 = 2074
    TagName2073 = 2075
    TagName2074 = 2076
    TagName2075 = 2077
    TagName2076 = 2078
    TagName2077 = 2079
    TagName2078 = 2080
    TagName2079 = 2081
    TagName2080 = 2082
    TagName2081 = 2083
    TagName2082 = 2084
    TagName2083 = 2085
    TagName2084 = 2086
    TagName2085 = 2087
    TagName2086 = 2088
    TagName2087 = 2089
    TagName2088 = 2090
    TagName2089 = 2091
    TagName2090 = 2092
    TagName2091 = 2093
    TagName2092 = 2094
    TagName2093 = 2095
    TagName2094 = 2096
    TagName2095 = 2097
    TagName2096 = 2098
    TagName2097 = 2099
    TagName2098 = 2100
    TagName2099 = 2101
    TagName2100 = 2102
    TagName2101 = 2103
    TagName2102 = 2104
    TagName2103 = 2105
    TagName2104 = 2106
    TagName2105 = 2107
    TagName2106 = 2108
    TagName2107 = 2109
    TagName2108 = 2110
    TagName2109 = 2111
    TagName2110 = 2112
    TagName2111 = 2113
    TagName2112 = 2114
    TagName2113 = 2115
    TagName2114 = 2116
    TagName2115 = 2117
    TagName2116 = 2118
    TagName2117 = 2119
    TagName2118 = 2120
    TagName2119 = 2121
    TagName2120 = 2122
    TagName2121 = 2123
    TagName2122 = 2124
    TagName2123 = 2125
    TagName2124 = 2126
    TagName2125 = 2127
    TagName2126 = 2128
    TagName2127 = 2129
    TagName2128 = 2130
    TagName2129 = 2131
    TagName2130 = 2132
    TagName2131 = 2133
    TagName2132 = 2134
    TagName2133 = 2135
    TagName2134 = 2136
    TagName2135 = 2137
    TagName2136 = 2138
    TagName2137 = 2139
    TagName2138 = 2140
    TagName2139 = 2141
    TagName2140 = 2142
    TagName2141 = 2143
    TagName2142 = 2144
    TagName2143 = 2145
    TagName2144 = 2146
    TagName2145 = 2147
    TagName2146 = 2148
    TagName2147 = 2149
    TagName2148 = 2150
    TagName2149 = 2151
    TagName2150 = 2152
    TagName2151 = 2153
    TagName2152 = 2154
    TagName2153 = 2155
    TagName2154 = 2156
    TagName2155 = 2157
    TagName2156 = 2158
    TagName2157 = 2159
    TagName2158 = 2160
    TagName2159 = 2161
    TagName2160 = 2162
    TagName2161 = 2163
    TagName2162 = 2164
    TagName2163 = 2165
    TagName2164 = 2166
    TagName2165 = 2167
    TagName2166 = 2168
    TagName2167 = 2169
    TagName2168 = 2170
    TagName2169 = 2171
    TagName2170 = 2172
    TagName2171 = 2173
    TagName2172 = 2174
    TagName2173 = 2175
    TagName2174 = 2176
    TagName2175 = 2177
    TagName2176 = 2178
    TagName2177 = 2179
    TagName2178 = 2180
    TagName2179 = 2181
    TagName2180 = 2182
    TagName2181 = 2183
    TagName2182 = 2184
    TagName2183 = 2185
    TagName2184 = 2186
    TagName2185 = 2187
    TagName2186 = 2188
    TagName2187 = 2189
    TagName2188 = 2190
    TagName2189 = 2191
    TagName2190 = 2192
    TagName2191 = 2193
    TagName2192 = 2194
    TagName2193 = 2195
    TagName2194 = 2196
    TagName2195 = 2197
    TagName2196 = 2198
    TagName2197 = 2199
    TagName2198 = 2200
    TagName2199 = 2201
    TagName2200 = 2202
    TagName2201 = 2203
    TagName2202 = 2204
    TagName2203 = 2205
    TagName2204 = 2206
    TagName2205 = 2207
    TagName2206 = 2208
    TagName2207 = 2209
    TagName2208 = 2210
    TagName2209 = 2211
    TagName2210 = 2212
    TagName2211 = 2213
    TagName2212 = 2214
    TagName2213 = 2215
    TagName2214 = 2216
    TagName2215 = 2217
    TagName2216 = 2218
    TagName2217 = 2219
    TagName2218 = 2220
    TagName2219 = 2221
    TagName2220 = 2222
    TagName2221 = 2223
    TagName2222 = 2224
    TagName2223 = 2225
    TagName2224 = 2226
    TagName2225 = 2227
    TagName2226 = 2228
    TagName2227 = 2229
    TagName2228 = 2230
    TagName2229 = 2231
    TagName2230 = 2232
    TagName2231 = 2233
    TagName2232 = 2234
    TagName2233 = 2235
    TagName2234 = 2236
    TagName2235 = 2237
    TagName2236 = 2238
    TagName2237 = 2239
    TagName2238 = 2240
    TagName2239 = 2241
    TagName2240 = 2242
    TagName2241 = 2243
    TagName2242 = 2244
    TagName2243 = 2245
    TagName2244 = 2246
    TagName2245 = 2247
    TagName2246 = 2248
    TagName2247 = 2249
    TagName2248 = 2250
    TagName2249 = 2251
    TagName2250 = 2252
    TagName2251 = 2253
    TagName2252 = 2254
    TagName2253 = 2255
    TagName2254 = 2256
    TagName2255 = 2257
    TagName2256 = 2258
    TagName2257 = 2259
    TagName2258 = 2260
    TagName2259 = 2261
    TagName2260 = 2262
    TagName2261 = 2263
    TagName2262 = 2264
    TagName2263 = 2265
    TagName2264 = 2266
    TagName2265 = 2267
    TagName2266 = 2268
    TagName2267 = 2269
    TagName2268 = 2270
    TagName2269 = 2271
    TagName2270 = 2272
    TagName2271 = 2273
    TagName2272 = 2274
    TagName2273 = 2275
    TagName2274 = 2276
    TagName2275 = 2277
    TagName2276 = 2278
    TagName2277 = 2279
    TagName2278 = 2280
    TagName2279 = 2281
    TagName2280 = 2282
    TagName2281 = 2283
    TagName2282 = 2284
    TagName2283 = 2285
    TagName2284 = 2286
    TagName2285 = 2287
    TagName2286 = 2288
    TagName2287 = 2289
    TagName2288 = 2290
    TagName2289 = 2291
    TagName2290 = 2292
    TagName2291 = 2293
    TagName2292 = 2294
    TagName2293 = 2295
    TagName2294 = 2296
    TagName2295 = 2297
    TagName2296 = 2298
    TagName2297 = 2299
    TagName2298 = 2300
    TagName2299 = 2301
    TagName2300 = 2302
    TagName2301 = 2303
    TagName2302 = 2304
    TagName2303 = 2305
    TagName2304 = 2306
    TagName2305 = 2307
    TagName2306 = 2308
    TagName2307 = 2309
    TagName2308 = 2310
    TagName2309 = 2311
    TagName2310 = 2312
    TagName2311 = 2313
    TagName2312 = 2314
    TagName2313 = 2315
    TagName2314 = 2316
    TagName2315 = 2317
    TagName2316 = 2318
    TagName2317 = 2319
    TagName2318 = 2320
    TagName2319 = 2321
    TagName2320 = 2322
    TagName2321 = 2323
    TagName2322 = 2324
    TagName2323 = 2325
    TagName2324 = 2326
    TagName2325 = 2327
    TagName2326 = 2328
    TagName2327 = 2329
    TagName2328 = 2330
    TagName2329 = 2331
    TagName2330 = 2332
    TagName2331 = 2333
    TagName2332 = 2334
    TagName2333 = 2335
    TagName2334 = 2336
    TagName2335 = 2337
    TagName2336 = 2338
    TagName2337 = 2339
    TagName2338 = 2340
    TagName2339 = 2341
    TagName2340 = 2342
    TagName2341 = 2343
    TagName2342 = 2344
    TagName2343 = 2345
    TagName2344 = 2346
    TagName2345 = 2347
    TagName2346 = 2348
    TagName2347 = 2349
    TagName2348 = 2350
    TagName2349 = 2351
    TagName2350 = 2352
    TagName2351 = 2353
    TagName2352 = 2354
    TagName2353 = 2355
    TagName2354 = 2356
    TagName2355 = 2357
    TagName2356 = 2358
    TagName2357 = 2359
    TagName2358 = 2360
    TagName2359 = 2361
    TagName2360 = 2362
    TagName2361 = 2363
    TagName2362 = 2364
    TagName2363 = 2365
    TagName2364 = 2366
    TagName2365 = 2367
    TagName2366 = 2368
    TagName2367 = 2369
    TagName2368 = 2370
    TagName2369 = 2371
    TagName2370 = 2372
    TagName2371 = 2373
    TagName2372 = 2374
    TagName2373 = 2375
    TagName2374 = 2376
    TagName2375 = 2377
    TagName2376 = 2378
    TagName2377 = 2379
    TagName2378 = 2380
    TagName2379 = 2381
    TagName2380 = 2382
    TagName2381 = 2383
    TagName2382 = 2384
    TagName2383 = 2385
    TagName2384 = 2386
    TagName2385 = 2387
    TagName2386 = 2388
    TagName2387 = 2389
    TagName2388 = 2390
    TagName2389 = 2391
    TagName2390 = 2392
    TagName2391 = 2393
    TagName2392 = 2394
    TagName2393 = 2395
    TagName2394 = 2396
    TagName2395 = 2397
    TagName2396 = 2398
    TagName2397 = 2399
    TagName2398 = 2400
    TagName2399 = 2401
    TagName2400 = 2402
    TagName2401 = 2403
    TagName2402 = 2404
    TagName2403 = 2405
    TagName2404 = 2406
    TagName2405 = 2407
    TagName2406 = 2408
    TagName2407 = 2409
    TagName2408 = 2410
    TagName2409 = 2411
    TagName2410 = 2412
    TagName2411 = 2413
    TagName2412 = 2414
    TagName2413 = 2415
    TagName2414 = 2416
    TagName2415 = 2417
    TagName2416 = 2418
    TagName2417 = 2419
    TagName2418 = 2420
    TagName2419 = 2421
    TagName2420 = 2422
    TagName2421 = 2423
    TagName2422 = 2424
    TagName2423 = 2425
    TagName2424 = 2426
    TagName2425 = 2427
    TagName2426 = 2428
    TagName2427 = 2429
    TagName2428 = 2430
    TagName2429 = 2431
    TagName2430 = 2432
    TagName2431 = 2433
    TagName2432 = 2434
    TagName2433 = 2435
    TagName2434 = 2436
    TagName2435 = 2437
    TagName2436 = 2438
    TagName2437 = 2439
    TagName2438 = 2440
    TagName2439 = 2441
    TagName2440 = 2442
    TagName2441 = 2443
    TagName2442 = 2444
    TagName2443 = 2445
    TagName2444 = 2446
    TagName2445 = 2447
    TagName2446 = 2448
    TagName2447 = 2449
    TagName2448 = 2450
    TagName2449 = 2451
    TagName2450 = 2452
    TagName2451 = 2453
    TagName2452 = 2454
    TagName2453 = 2455
    TagName2454 = 2456
    TagName2455 = 2457
    TagName2456 = 2458
    TagName2457 = 2459
    TagName2458 = 2460
    TagName2459 = 2461
    TagName2460 = 2462
    TagName2461 = 2463
    TagName2462 = 2464
    TagName2463 = 2465
    TagName2464 = 2466
    TagName2465 = 2467
    TagName2466 = 2468
    TagName2467 = 2469
    TagName2468 = 2470
    TagName2469 = 2471
    TagName2470 = 2472
    TagName2471 = 2473
    TagName2472 = 2474
    TagName2473 = 2475
    TagName2474 = 2476
    TagName2475 = 2477
    TagName2476 = 2478
    TagName2477 = 2479
    TagName2478 = 2480
    TagName2479 = 2481
    TagName2480 = 2482
    TagName2481 = 2483
    TagName2482 = 2484
    TagName2483 = 2485
    TagName2484 = 2486
    TagName2485 = 2487
    TagName2486 = 2488
    TagName2487 = 2489
    TagName2488 = 2490
    TagName2489 = 2491
    TagName2490 = 2492
    TagName2491 = 2493
    TagName2492 = 2494
    TagName2493 = 2495
    TagName2494 = 2496
    TagName2495 = 2497
    TagName2496 = 2498
    TagName2497 = 2499
    TagName2498 = 2500
    TagName2499 = 2501
    TagName2500 = 2502
    TagName2501 = 2503
    TagName2502 = 2504
    TagName2503 = 2505
    TagName2504 = 2506
    TagName2505 = 2507
    TagName2506 = 2508
    TagName2507 = 2509
    TagName2508 = 2510
    TagName2509 = 2511
    TagName2510 = 2512
    TagName2511 = 2513
    TagName2512 = 2514
    TagName2513 = 2515
    TagName2514 = 2516
    TagName2515 = 2517
    TagName2516 = 2518
    TagName2517 = 2519
    TagName2518 = 2520
    TagName2519 = 2521
    TagName2520 = 2522
    TagName2521 = 2523
    TagName2522 = 2524
    TagName2523 = 2525
    TagName2524 = 2526
    TagName2525 = 2527
    TagName2526 = 2528
    TagName2527 = 2529
    TagName2528 = 2530
    TagName2529 = 2531
    TagName2530 = 2532
    TagName2531 = 2533
    TagName2532 = 2534
    TagName2533 = 2535
    TagName2534 = 2536
    TagName2535 = 2537
    TagName2536 = 2538
    TagName2537 = 2539
    TagName2538 = 2540
    TagName2539 = 2541
    TagName2540 = 2542
    TagName2541 = 2543
    TagName2542 = 2544
    TagName2543 = 2545
    TagName2544 = 2546
    TagName2545 = 2547
    TagName2546 = 2548
    TagName2547 = 2549
    TagName2548 = 2550
    TagName2549 = 2551
    TagName2550 = 2552
    TagName2551 = 2553
    TagName2552 = 2554
    TagName2553 = 2555
    TagName2554 = 2556
    TagName2555 = 2557
    TagName2556 = 2558
    TagName2557 = 2559
    TagName2558 = 2560
    TagName2559 = 2561
    TagName2560 = 2562
    TagName2561 = 2563
    TagName2562 = 2564
    TagName2563 = 2565
    TagName2564 = 2566
    TagName2565 = 2567
    TagName2566 = 2568
    TagName2567 = 2569
    TagName2568 = 2570
    TagName2569 = 2571
    TagName2570 = 2572
    TagName2571 = 2573
    TagName2572 = 2574
    TagName2573 = 2575
    TagName2574 = 2576
    TagName2575 = 2577
    TagName2576 = 2578
    TagName2577 = 2579
    TagName2578 = 2580
    TagName2579 = 2581
    TagName2580 = 2582
    TagName2581 = 2583
    TagName2582 = 2584
    TagName2583 = 2585
    TagName2584 = 2586
    TagName2585 = 2587
    TagName2586 = 2588
    TagName2587 = 2589
    TagName2588 = 2590
    TagName2589 = 2591
    TagName2590 = 2592
    TagName2591 = 2593
    TagName2592 = 2594
    TagName2593 = 2595
    TagName2594 = 2596
    TagName2595 = 2597
    TagName2596 = 2598
    TagName2597 = 2599
    TagName2598 = 2600
    TagName2599 = 2601
    TagName2600 = 2602
    TagName2601 = 2603
    TagName2602 = 2604
    TagName2603 = 2605
    TagName2604 = 2606
    TagName2605 = 2607
    TagName2606 = 2608
    TagName2607 = 2609
    TagName2608 = 2610
    TagName2609 = 2611
    TagName2610 = 2612
    TagName2611 = 2613
    TagName2612 = 2614
    TagName2613 = 2615
    TagName2614 = 2616
    TagName2615 = 2617
    TagName2616 = 2618
    TagName2617 = 2619
    TagName2618 = 2620
    TagName2619 = 2621
    TagName2620 = 2622
    TagName2621 = 2623
    TagName2622 = 2624
    TagName2623 = 2625
    TagName2624 = 2626
    TagName2625 = 2627
    TagName2626 = 2628
    TagName2627 = 2629
    TagName2628 = 2630
    TagName2629 = 2631
    TagName2630 = 2632
    TagName2631 = 2633
    TagName2632 = 2634
    TagName2633 = 2635
    TagName2634 = 2636
    TagName2635 = 2637
    TagName2636 = 2638
    TagName2637 = 2639
    TagName2638 = 2640
    TagName2639 = 2641
    TagName2640 = 2642
    TagName2641 = 2643
    TagName2642 = 2644
    TagName2643 = 2645
    TagName2644 = 2646
    TagName2645 = 2647
    TagName2646 = 2648
    TagName2647 = 2649
    TagName2648 = 2650
    TagName2649 = 2651
    TagName2650 = 2652
    TagName2651 = 2653
    TagName2652 = 2654
    TagName2653 = 2655
    TagName2654 = 2656
    TagName2655 = 2657
    TagName2656 = 2658
    TagName2657 = 2659
    TagName2658 = 2660
    TagName2659 = 2661
    TagName2660 = 2662
    TagName2661 = 2663
    TagName2662 = 2664
    TagName2663 = 2665
    TagName2664 = 2666
    TagName2665 = 2667
    TagName2666 = 2668
    TagName2667 = 2669
    TagName2668 = 2670
    TagName2669 = 2671
    TagName2670 = 2672
    TagName2671 = 2673
    TagName2672 = 2674
    TagName2673 = 2675
    TagName2674 = 2676
    TagName2675 = 2677
    TagName2676 = 2678
    TagName2677 = 2679
    TagName2678 = 2680
    TagName2679 = 2681
    TagName2680 = 2682
    TagName2681 = 2683
    TagName2682 = 2684
    TagName2683 = 2685
    TagName2684 = 2686
    TagName2685 = 2687
    TagName2686 = 2688
    TagName2687 = 2689
    TagName2688 = 2690
    TagName2689 = 2691
    TagName2690 = 2692
    TagName2691 = 2693
    TagName2692 = 2694
    TagName2693 = 2695
    TagName2694 = 2696
    TagName2695 = 2697
    TagName2696 = 2698
    TagName2697 = 2699
    TagName2698 = 2700
    TagName2699 = 2701
    TagName2700 = 2702
    TagName2701 = 2703
    TagName2702 = 2704
    TagName2703 = 2705
    TagName2704 = 2706
    TagName2705 = 2707
    TagName2706 = 2708
    TagName2707 = 2709
    TagName2708 = 2710
    TagName2709 = 2711
    TagName2710 = 2712
    TagName2711 = 2713
    TagName2712 = 2714
    TagName2713 = 2715
    TagName2714 = 2716
    TagName2715 = 2717
    TagName2716 = 2718
    TagName2717 = 2719
    TagName2718 = 2720
    TagName2719 = 2721
    TagName2720 = 2722
    TagName2721 = 2723
    TagName2722 = 2724
    TagName2723 = 2725
    TagName2724 = 2726
    TagName2725 = 2727
    TagName2726 = 2728
    TagName2727 = 2729
    TagName2728 = 2730
    TagName2729 = 2731
    TagName2730 = 2732
    TagName2731 = 2733
    TagName2732 = 2734
    TagName2733 = 2735
    TagName2734 = 2736
    TagName2735 = 2737
    TagName2736 = 2738
    TagName2737 = 2739
    TagName2738 = 2740
    TagName2739 = 2741
    TagName2740 = 2742
    TagName2741 = 2743
    TagName2742 = 2744
    TagName2743 = 2745
    TagName2744 = 2746
    TagName2745 = 2747
    TagName2746 = 2748
    TagName2747 = 2749
    TagName2748 = 2750
    TagName2749 = 2751
    TagName2750 = 2752
    TagName2751 = 2753
    TagName2752 = 2754
    TagName2753 = 2755
    TagName2754 = 2756
    TagName2755 = 2757
    TagName2756 = 2758
    TagName2757 = 2759
    TagName2758 = 2760
    TagName2759 = 2761
    TagName2760 = 2762
    TagName2761 = 2763
    TagName2762 = 2764
    TagName2763 = 2765
    TagName2764 = 2766
    TagName2765 = 2767
    TagName2766 = 2768
    TagName2767 = 2769
    TagName2768 = 2770
    TagName2769 = 2771
    TagName2770 = 2772
    TagName2771 = 2773
    TagName2772 = 2774
    TagName2773 = 2775
    TagName2774 = 2776
    TagName2775 = 2777
    TagName2776 = 2778
    TagName2777 = 2779
    TagName2778 = 2780
    TagName2779 = 2781
    TagName2780 = 2782
    TagName2781 = 2783
    TagName2782 = 2784
    TagName2783 = 2785
    TagName2784 = 2786
    TagName2785 = 2787
    TagName2786 = 2788
    TagName2787 = 2789
    TagName2788 = 2790
    TagName2789 = 2791
    TagName2790 = 2792
    TagName2791 = 2793
    TagName2792 = 2794
    TagName2793 = 2795
    TagName2794 = 2796
    TagName2795 = 2797
    TagName2796 = 2798
    TagName2797 = 2799
    TagName2798 = 2800
    TagName2799 = 2801
    TagName2800 = 2802
    TagName2801 = 2803
    TagName2802 = 2804
    TagName2803 = 2805
    TagName2804 = 2806
    TagName2805 = 2807
    TagName2806 = 2808
    TagName2807 = 2809
    TagName2808 = 2810
    TagName2809 = 2811
    TagName2810 = 2812
    TagName2811 = 2813
    TagName2812 = 2814
    TagName2813 = 2815
    TagName2814 = 2816
    TagName2815 = 2817
    TagName2816 = 2818
    TagName2817 = 2819
    TagName2818 = 2820
    TagName2819 = 2821
    TagName2820 = 2822
    TagName2821 = 2823
    TagName2822 = 2824
    TagName2823 = 2825
    TagName2824 = 2826
    TagName2825 = 2827
    TagName2826 = 2828
    TagName2827 = 2829
    TagName2828 = 2830
    TagName2829 = 2831
    TagName2830 = 2832
    TagName2831 = 2833
    TagName2832 = 2834
    TagName2833 = 2835
    TagName2834 = 2836
    TagName2835 = 2837
    TagName2836 = 2838
    TagName2837 = 2839
    TagName2838 = 2840
    TagName2839 = 2841
    TagName2840 = 2842
    TagName2841 = 2843
    TagName2842 = 2844
    TagName2843 = 2845
    TagName2844 = 2846
    TagName2845 = 2847
    TagName2846 = 2848
    TagName2847 = 2849
    TagName2848 = 2850
    TagName2849 = 2851
    TagName2850 = 2852
    TagName2851 = 2853
    TagName2852 = 2854
    TagName2853 = 2855
    TagName2854 = 2856
    TagName2855 = 2857
    TagName2856 = 2858
    TagName2857 = 2859
    TagName2858 = 2860
    TagName2859 = 2861
    TagName2860 = 2862
    TagName2861 = 2863
    TagName2862 = 2864
    TagName2863 = 2865
    TagName2864 = 2866
    TagName2865 = 2867
    TagName2866 = 2868
    TagName2867 = 2869
    TagName2868 = 2870
    TagName2869 = 2871
    TagName2870 = 2872
    TagName2871 = 2873
    TagName2872 = 2874
    TagName2873 = 2875
    TagName2874 = 2876
    TagName2875 = 2877
    TagName2876 = 2878
    TagName2877 = 2879
    TagName2878 = 2880
    TagName2879 = 2881
    TagName2880 = 2882
    TagName2881 = 2883
    TagName2882 = 2884
    TagName2883 = 2885
    TagName2884 = 2886
    TagName2885 = 2887
    TagName2886 = 2888
    TagName2887 = 2889
    TagName2888 = 2890
    TagName2889 = 2891
    TagName2890 = 2892
    TagName2891 = 2893
    TagName2892 = 2894
    TagName2893 = 2895
    TagName2894 = 2896
    TagName2895 = 2897
    TagName2896 = 2898
    TagName2897 = 2899
    TagName2898 = 2900
    TagName2899 = 2901
    TagName2900 = 2902
    TagName2901 = 2903
    TagName2902 = 2904
    TagName2903 = 2905
    TagName2904 = 2906
    TagName2905 = 2907
    TagName2906 = 2908
    TagName2907 = 2909
    TagName2908 = 2910
    TagName2909 = 2911
    TagName2910 = 2912
    TagName2911 = 2913
    TagName2912 = 2914
    TagName2913 = 2915
    TagName2914 = 2916
    TagName2915 = 2917
    TagName2916 = 2918
    TagName2917 = 2919
    TagName2918 = 2920
    TagName2919 = 2921
    TagName2920 = 2922
    TagName2921 = 2923
    TagName2922 = 2924
    TagName2923 = 2925
    TagName2924 = 2926
    TagName2925 = 2927
    TagName2926 = 2928
    TagName2927 = 2929
    TagName2928 = 2930
    TagName2929 = 2931
    TagName2930 = 2932
    TagName2931 = 2933
    TagName2932 = 2934
    TagName2933 = 2935
    TagName2934 = 2936
    TagName2935 = 2937
    TagName2936 = 2938
    TagName2937 = 2939
    TagName2938 = 2940
    TagName2939 = 2941
    TagName2940 = 2942
    TagName2941 = 2943
    TagName2942 = 2944
    TagName2943 = 2945
    TagName2944 = 2946
    TagName2945 = 2947
    TagName2946 = 2948
    TagName2947 = 2949
    TagName2948 = 2950
    TagName2949 = 2951
    TagName2950 = 2952
    TagName2951 = 2953
    TagName2952 = 2954
    TagName2953 = 2955
    TagName2954 = 2956
    TagName2955 = 2957
    TagName2956 = 2958
    TagName2957 = 2959
    TagName2958 = 2960
    TagName2959 = 2961
    TagName2960 = 2962
    TagName2961 = 2963
    TagName2962 = 2964
    TagName2963 = 2965
    TagName2964 = 2966
    TagName2965 = 2967
    TagName2966 = 2968
    TagName2967 = 2969
    TagName2968 = 2970
    TagName2969 = 2971
    TagName2970 = 2972
    TagName2971 = 2973
    TagName2972 = 2974
    TagName2973 = 2975
    TagName2974 = 2976
    TagName2975 = 2977
    TagName2976 = 2978
    TagName2977 = 2979
    TagName2978 = 2980
    TagName2979 = 2981
    TagName2980 = 2982
    TagName2981 = 2983
    TagName2982 = 2984
    TagName2983 = 2985
    TagName2984 = 2986
    TagName2985 = 2987
    TagName2986 = 2988
    TagName2987 = 2989
    TagName2988 = 2990
    TagName2989 = 2991
    TagName2990 = 2992
    TagName2991 = 2993
    TagName2992 = 2994
    TagName2993 = 2995
    TagName2994 = 2996
    TagName2995 = 2997
    TagName2996 = 2998
    TagName2997 = 2999
    TagName2998 = 3000
    TagName2999 = 3001
    TagName3000 = 3002
    TagName3001 = 3003

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

def dump_Excel_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndexField(), password),
        "DialogType": convert_string(excel_instance.DialogTypeField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "HideUI": bool(excel_instance.HideUIField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
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
        "WORLDBOSSBATTLEMIDDLE": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLEField(), password),
        "WORLDBOSSBATTLEHIGH": convert_int(excel_instance.WORLDBOSSBATTLEHIGHField(), password),
        "WORLDBOSSBATTLEVERYHIGH": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHField(), password),
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
        "CharProfileRowIntervalJp": convert_int(excel_instance.CharProfileRowIntervalJpField(), password),
        "CharProfilePopupRowIntervalKr": convert_int(excel_instance.CharProfilePopupRowIntervalKrField(), password),
        "CharProfilePopupRowIntervalJp": convert_int(excel_instance.CharProfilePopupRowIntervalJpField(), password),
        "BeforehandGachaCount": convert_int(excel_instance.BeforehandGachaCountField(), password),
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
        "TTSVCN02": convert_string(excel_instance.TTSVCN02Field(), password),
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
        "ScrollWheelFactor": convert_float(excel_instance.ScrollWheelFactorField(), password),
        "RemoveKeycodeWord": convert_string(excel_instance.RemoveKeycodeWordField(), password),
        "TutorialDialogTouchKey": convert_string(excel_instance.TutorialDialogTouchKeyField(), password),
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

def dump_Excel_GachaSelectPickupGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "NameKr": convert_string(excel_instance.NameKrField(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupIDField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
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

def dump_Excel_IAWorldRaidSkillDescriptionListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "GlobalSkillGroupId": [convert_string(excel_instance.GlobalSkillGroupIdField(j), password) for j in range(excel_instance.GlobalSkillGroupIdFieldLength())],
        "GlobalSkillRemoveCondition": [convert_int(excel_instance.GlobalSkillRemoveConditionField(j), password) for j in range(excel_instance.GlobalSkillRemoveConditionFieldLength())],
        "GlobalSkillHighlightResource": [SkillSlotHighLightType(convert_int(excel_instance.GlobalSkillHighlightResourceField(j), password)).name for j in range(excel_instance.GlobalSkillHighlightResourceFieldLength())],
        "SkillGroupId": [convert_string(excel_instance.SkillGroupIdField(j), password) for j in range(excel_instance.SkillGroupIdFieldLength())],
        "HighlightResource": [SkillSlotHighLightType(convert_int(excel_instance.HighlightResourceField(j), password)).name for j in range(excel_instance.HighlightResourceFieldLength())],
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

def dump_Excel_LocalizeCCGExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
    }

def dump_Excel_LocalizeFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
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

def dump_Excel_ScenarioScriptField1Excel(excel_instance, password: bytes = b"") -> dict:
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
        "VoiceJp": convert_string(excel_instance.VoiceJpField(), password),
    }

def dump_Excel_ScenarioScriptTestExcel(excel_instance, password: bytes = b"") -> dict:
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
        "VoiceId": convert_string(excel_instance.VoiceIdField(), password),
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
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "UnlockBattlePassId": convert_int(excel_instance.UnlockBattlePassIdField(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "DurationCN": convert_int(excel_instance.DurationCNField(), password),
    }

def dump_ExcelDB_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndexField(), password),
        "DialogType": convert_string(excel_instance.DialogTypeField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "DurationAdd": convert_int(excel_instance.DurationAddField(), password),
        "HideUI": bool(excel_instance.HideUIField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
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
        "DurationCN": convert_int(excel_instance.DurationCNField(), password),
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
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "CVUnlockScenarioType": CVUnlockScenarioType(convert_int(excel_instance.CVUnlockScenarioTypeField(), password)).name,
        "UnlockEventSeason": convert_int(excel_instance.UnlockEventSeasonField(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupIdField(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "ScenarioCharacterShapes": ScenarioCharacterShapes(convert_int(excel_instance.ScenarioCharacterShapesField(), password)).name,
        "DurationCN": convert_int(excel_instance.DurationCNField(), password),
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
        "AnimationName": convert_string(excel_instance.AnimationNameField(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceIdField(j), password) for j in range(excel_instance.VoiceIdFieldLength())],
        "ApplyPosition": bool(excel_instance.ApplyPositionField()),
        "PosX": convert_float(excel_instance.PosXField(), password),
        "PosY": convert_float(excel_instance.PosYField(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisibleField()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionTypeField(), password)).name,
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRankField(), password),
        "UnlockEquipWeapon": bool(excel_instance.UnlockEquipWeaponField()),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "DurationCN": convert_int(excel_instance.DurationCNField(), password),
    }

def dump_ExcelDB_CharacterDialogSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroupField(), password),
        "CharacterId": convert_int(excel_instance.CharacterIdField(), password),
        "Duration": convert_int(excel_instance.DurationField(), password),
        "Separate": bool(excel_instance.SeparateField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "DurationCN": convert_int(excel_instance.DurationCNField(), password),
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
        "ScenarioCharacter": convert_string(excel_instance.ScenarioCharacterField(), password),
        "SpawnTemplateId": convert_uint(excel_instance.SpawnTemplateIdField(), password),
        "FavorLevelupType": convert_int(excel_instance.FavorLevelupTypeField(), password),
        "EquipmentSlot": [EquipmentCategory(convert_int(excel_instance.EquipmentSlotField(j), password)).name for j in range(excel_instance.EquipmentSlotFieldLength())],
        "WeaponLocalizeId": convert_uint(excel_instance.WeaponLocalizeIdField(), password),
        "DisplayEnemyInfo": bool(excel_instance.DisplayEnemyInfoField()),
        "BodyRadius": convert_int(excel_instance.BodyRadiusField(), password),
        "RandomEffectRadius": convert_int(excel_instance.RandomEffectRadiusField(), password),
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
        "Duration": convert_int(excel_instance.DurationField(), password),
        "Separate": bool(excel_instance.SeparateField()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKRField(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJPField(), password),
        "DurationCN": convert_int(excel_instance.DurationCNField(), password),
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

def dump_ExcelDB_CheatCodeListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "CheatCode": [convert_string(excel_instance.CheatCodeField(j), password) for j in range(excel_instance.CheatCodeFieldLength())],
        "InputTitle": [convert_string(excel_instance.InputTitleField(j), password) for j in range(excel_instance.InputTitleFieldLength())],
        "Desc": convert_string(excel_instance.DescField(), password),
    }

def dump_ExcelDB_ClanChattingEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "TabGroupId": convert_int(excel_instance.TabGroupIdField(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrderField(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKrField(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJpField(), password),
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

def dump_ExcelDB_CouponCompleteExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupIdField(), password),
        "GiftId": [convert_int(excel_instance.GiftIdField(j), password) for j in range(excel_instance.GiftIdFieldLength())],
        "Comment": convert_string(excel_instance.CommentField(), password),
        "ExpiredDay": convert_int(excel_instance.ExpiredDayField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelIdField(j), password) for j in range(excel_instance.RewardParcelIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
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
        "PercentRankStart": convert_int(excel_instance.PercentRankStartField(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEndField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_EliminateRaidRankingRewardUOExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "RankStart": convert_int(excel_instance.RankStartField(), password),
        "RankEnd": convert_int(excel_instance.RankEndField(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStartField(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEndField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
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
        "EmblemEffectPath": convert_string(excel_instance.EmblemEffectPathField(), password),
        "DisplayType": EmblemDisplayType(convert_int(excel_instance.DisplayTypeField(), password)).name,
        "DisplayStartDate": convert_string(excel_instance.DisplayStartDateField(), password),
        "DisplayEndDate": convert_string(excel_instance.DisplayEndDateField(), password),
        "DislpayFavorLevel": convert_int(excel_instance.DislpayFavorLevelField(), password),
        "CheckPassType": EmblemCheckPassType(convert_int(excel_instance.CheckPassTypeField(), password)).name,
        "EmblemParameter": convert_int(excel_instance.EmblemParameterField(), password),
        "CheckPassCount": convert_int(excel_instance.CheckPassCountField(), password),
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
        "ProductIdHarmony": convert_int(excel_instance.ProductIdHarmonyField(), password),
        "ConsumeExtraStep": [convert_int(excel_instance.ConsumeExtraStepField(j), password) for j in range(excel_instance.ConsumeExtraStepFieldLength())],
        "ConsumeExtraAmount": [convert_int(excel_instance.ConsumeExtraAmountField(j), password) for j in range(excel_instance.ConsumeExtraAmountFieldLength())],
        "State": convert_int(excel_instance.StateField(), password),
        "ParcelType": [ParcelType(convert_int(excel_instance.ParcelTypeField(j), password)).name for j in range(excel_instance.ParcelTypeFieldLength())],
        "ParcelId": [convert_int(excel_instance.ParcelIdField(j), password) for j in range(excel_instance.ParcelIdFieldLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmountField(j), password) for j in range(excel_instance.ParcelAmountFieldLength())],
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
        "WorldBossHPUO": convert_int(excel_instance.WorldBossHPUOField(), password),
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
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0Field(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1Field(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2Field(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQualityField(), password),
        "MaxGiftTags": convert_int(excel_instance.MaxGiftTagsField(), password),
        "ShopCategory": [convert_float(excel_instance.ShopCategoryField(j), password) for j in range(excel_instance.ShopCategoryFieldLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTimeField(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateInField(), password),
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeIdField(), password),
        "GachaTicket": GachaTicketType(convert_int(excel_instance.GachaTicketField(), password)).name,
        "AlertPopupId": convert_int(excel_instance.AlertPopupIdField(), password),
        "ShiftingCraftRecipe": convert_int(excel_instance.ShiftingCraftRecipeField(), password),
    }

def dump_ExcelDB_KeyMappingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_string(excel_instance.IdField(), password),
        "TargetKeyCode": convert_string(excel_instance.TargetKeyCodeField(), password),
        "IsDisplay": bool(excel_instance.IsDisplayField()),
        "IsUsed": bool(excel_instance.IsUsedField()),
        "IsLongPress": bool(excel_instance.IsLongPressField()),
        "IgnorePosCheck": bool(excel_instance.IgnorePosCheckField()),
        "IconPositionX": convert_float(excel_instance.IconPositionXField(), password),
        "IconPositionY": convert_float(excel_instance.IconPositionYField(), password),
        "IconScaleX": convert_float(excel_instance.IconScaleXField(), password),
        "IconScaleY": convert_float(excel_instance.IconScaleYField(), password),
    }

def dump_ExcelDB_KeyMappingPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PrefabName": convert_string(excel_instance.PrefabNameField(), password),
        "ButtonName": [convert_string(excel_instance.ButtonNameField(j), password) for j in range(excel_instance.ButtonNameFieldLength())],
        "KeyMappingId": [convert_string(excel_instance.KeyMappingIdField(j), password) for j in range(excel_instance.KeyMappingIdFieldLength())],
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
        "FullNameKr": convert_string(excel_instance.FullNameKrField(), password),
        "FullNameJp": convert_string(excel_instance.FullNameJpField(), password),
        "FamilyNameKr": convert_string(excel_instance.FamilyNameKrField(), password),
        "FamilyNameRubyKr": convert_string(excel_instance.FamilyNameRubyKrField(), password),
        "PersonalNameKr": convert_string(excel_instance.PersonalNameKrField(), password),
        "PersonalNameRubyKr": convert_string(excel_instance.PersonalNameRubyKrField(), password),
        "FamilyNameJp": convert_string(excel_instance.FamilyNameJpField(), password),
        "FamilyNameRubyJp": convert_string(excel_instance.FamilyNameRubyJpField(), password),
        "PersonalNameJp": convert_string(excel_instance.PersonalNameJpField(), password),
        "PersonalNameRubyJp": convert_string(excel_instance.PersonalNameRubyJpField(), password),
        "Club": Club(convert_int(excel_instance.ClubField(), password)).name,
        "SchoolYearKr": convert_string(excel_instance.SchoolYearKrField(), password),
        "SchoolYearJp": convert_string(excel_instance.SchoolYearJpField(), password),
        "CharacterAgeKr": convert_string(excel_instance.CharacterAgeKrField(), password),
        "CharacterAgeJp": convert_string(excel_instance.CharacterAgeJpField(), password),
        "BirthDay": convert_string(excel_instance.BirthDayField(), password),
        "BirthdayKr": convert_string(excel_instance.BirthdayKrField(), password),
        "BirthdayJp": convert_string(excel_instance.BirthdayJpField(), password),
        "CharHeightKr": convert_string(excel_instance.CharHeightKrField(), password),
        "CharHeightJp": convert_string(excel_instance.CharHeightJpField(), password),
        "DesignerNameKr": convert_string(excel_instance.DesignerNameKrField(), password),
        "DesignerNameJp": convert_string(excel_instance.DesignerNameJpField(), password),
        "IllustratorNameKr": convert_string(excel_instance.IllustratorNameKrField(), password),
        "IllustratorNameJp": convert_string(excel_instance.IllustratorNameJpField(), password),
        "CharacterVoiceKr": convert_string(excel_instance.CharacterVoiceKrField(), password),
        "CharacterVoiceJp": convert_string(excel_instance.CharacterVoiceJpField(), password),
        "HobbyKr": convert_string(excel_instance.HobbyKrField(), password),
        "HobbyJp": convert_string(excel_instance.HobbyJpField(), password),
        "WeaponNameKr": convert_string(excel_instance.WeaponNameKrField(), password),
        "WeaponDescKr": convert_string(excel_instance.WeaponDescKrField(), password),
        "WeaponNameJp": convert_string(excel_instance.WeaponNameJpField(), password),
        "WeaponDescJp": convert_string(excel_instance.WeaponDescJpField(), password),
        "ProfileIntroductionKr": convert_string(excel_instance.ProfileIntroductionKrField(), password),
        "ProfileIntroductionJp": convert_string(excel_instance.ProfileIntroductionJpField(), password),
        "CharacterSSRNewKr": convert_string(excel_instance.CharacterSSRNewKrField(), password),
        "CharacterSSRNewJp": convert_string(excel_instance.CharacterSSRNewJpField(), password),
    }

def dump_ExcelDB_LocalizeCodeInBuildExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
    }

def dump_ExcelDB_LocalizeErrorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "ErrorLevel": WebAPIErrorLevel(convert_int(excel_instance.ErrorLevelField(), password)).name,
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
    }

def dump_ExcelDB_LocalizeEtcExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "NameKr": convert_string(excel_instance.NameKrField(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKrField(), password),
        "NameJp": convert_string(excel_instance.NameJpField(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJpField(), password),
    }

def dump_ExcelDB_LocalizeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.KeyField(), password),
        "Kr": convert_string(excel_instance.KrField(), password),
        "Jp": convert_string(excel_instance.JpField(), password),
    }

def dump_ExcelDB_LocalizeGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GachaShopId": convert_int(excel_instance.GachaShopIdField(), password),
        "TabNameKr": convert_string(excel_instance.TabNameKrField(), password),
        "TabNameJp": convert_string(excel_instance.TabNameJpField(), password),
        "TitleNameKr": convert_string(excel_instance.TitleNameKrField(), password),
        "TitleNameJp": convert_string(excel_instance.TitleNameJpField(), password),
        "SubTitleKr": convert_string(excel_instance.SubTitleKrField(), password),
        "SubTitleJp": convert_string(excel_instance.SubTitleJpField(), password),
        "GachaDescriptionKr": convert_string(excel_instance.GachaDescriptionKrField(), password),
        "GachaDescriptionJp": convert_string(excel_instance.GachaDescriptionJpField(), password),
        "GachaPeriodCN": convert_string(excel_instance.GachaPeriodCNField(), password),
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

def dump_ExcelDB_ProductBattlePassExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.IdField(), password),
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
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
        "ProductId": convert_string(excel_instance.ProductIdField(), password),
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
        "PercentRankStart": convert_int(excel_instance.PercentRankStartField(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEndField(), password),
        "Tier": convert_int(excel_instance.TierField(), password),
        "RewardParcelType": [ParcelType(convert_int(excel_instance.RewardParcelTypeField(j), password)).name for j in range(excel_instance.RewardParcelTypeFieldLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueIdField(j), password) for j in range(excel_instance.RewardParcelUniqueIdFieldLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmountField(j), password) for j in range(excel_instance.RewardParcelAmountFieldLength())],
    }

def dump_ExcelDB_RaidRankingRewardUOExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupIdField(), password),
        "Id": convert_int(excel_instance.IdField(), password),
        "RankStart": convert_int(excel_instance.RankStartField(), password),
        "RankEnd": convert_int(excel_instance.RankEndField(), password),
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
        "VolumeId": convert_int(excel_instance.VolumeIdField(), password),
        "ChapterId": convert_int(excel_instance.ChapterIdField(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeIdField(), password),
        "ExposedTime": convert_string(excel_instance.ExposedTimeField(), password),
        "Hide": bool(excel_instance.HideField()),
        "Open": bool(excel_instance.OpenField()),
        "IsContinue": bool(excel_instance.IsContinueField()),
        "EpisodeContinueModeId": convert_int(excel_instance.EpisodeContinueModeIdField(), password),
        "FrontScenarioGroupId": [convert_int(excel_instance.FrontScenarioGroupIdField(j), password) for j in range(excel_instance.FrontScenarioGroupIdFieldLength())],
        "StrategyId": convert_int(excel_instance.StrategyIdField(), password),
        "GroundId": convert_int(excel_instance.GroundIdField(), password),
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattleField()),
        "BattleDuration": convert_int(excel_instance.BattleDurationField(), password),
        "BackScenarioGroupId": [convert_int(excel_instance.BackScenarioGroupIdField(j), password) for j in range(excel_instance.BackScenarioGroupIdFieldLength())],
        "ClearedModeId": [convert_int(excel_instance.ClearedModeIdField(j), password) for j in range(excel_instance.ClearedModeIdFieldLength())],
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardIdField(), password),
        "IsScenarioSpecialReward": bool(excel_instance.IsScenarioSpecialRewardField()),
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
        "LocalizeId": convert_uint(excel_instance.LocalizeIdField(), password),
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
        "VoiceId": convert_string(excel_instance.VoiceIdField(), password),
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
        "IsNewbie": bool(excel_instance.IsNewbieField()),
        "IsSelectRecruit": bool(excel_instance.IsSelectRecruitField()),
        "DirectPayInvisibleTokenId": convert_int(excel_instance.DirectPayInvisibleTokenIdField(), password),
        "DirectPayAndroidShopCashId": convert_int(excel_instance.DirectPayAndroidShopCashIdField(), password),
        "DirectPayAppleShopCashId": convert_int(excel_instance.DirectPayAppleShopCashIdField(), password),
        "DirectPayHarmonyShopCashId": convert_int(excel_instance.DirectPayHarmonyShopCashIdField(), password),
        "SelectAbleGachaGroupId": convert_int(excel_instance.SelectAbleGachaGroupIdField(), password),
        "MaxSelectCharacterNum": convert_int(excel_instance.MaxSelectCharacterNumField(), password),
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

def dump_ExcelDB_SoundUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.IDField(), password),
        "SoundUniqueId": convert_string(excel_instance.SoundUniqueIdField(), password),
        "Path": convert_string(excel_instance.PathField(), password),
    }

def dump_ExcelDB_SpineLipsyncExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceId": convert_uint(excel_instance.VoiceIdField(), password),
        "VoiceStringId": convert_string(excel_instance.VoiceStringIdField(), password),
        "AnimJson": convert_string(excel_instance.AnimJsonField(), password),
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
        "SoundPath": [convert_string(excel_instance.SoundPathField(j), password) for j in range(excel_instance.SoundPathFieldLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolumeField(j), password) for j in range(excel_instance.SoundVolumeFieldLength())],
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

def dump_ExcelDB_WebSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WebId": convert_int(excel_instance.WebIdField(), password),
        "OpenTime": convert_string(excel_instance.OpenTimeField(), password),
        "CloseTime": convert_string(excel_instance.CloseTimeField(), password),
        "Type": convert_int(excel_instance.TypeField(), password),
        "MailExpiredDay": convert_int(excel_instance.MailExpiredDayField(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPathField(), password),
        "BannerType": EventContentType(convert_int(excel_instance.BannerTypeField(), password)).name,
        "IconOrder": convert_int(excel_instance.IconOrderField(), password),
        "Url": convert_string(excel_instance.UrlField(), password),
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
        "WorldBossHPUO": convert_int(excel_instance.WorldBossHPUOField(), password),
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

def dump_Excel_CharacterDialogEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_CharacterDialogEmojiExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_CharacterDialogFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_CharacterDialogFieldExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_Excel_GachaSelectPickupGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_GachaSelectPickupGroupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_IAWorldRaidSkillDescriptionListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_IAWorldRaidSkillDescriptionListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_Excel_LocalizeCCGExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_LocalizeCCGExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_LocalizeFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_LocalizeFieldExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_Excel_ScenarioScriptField1ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ScenarioScriptField1Excel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_Excel_ScenarioScriptTestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [Excel_ScenarioScriptTestExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_CheatCodeListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CheatCodeListExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_CouponCompleteExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_CouponCompleteExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_EliminateRaidRankingRewardUOExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_EliminateRaidRankingRewardUOExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_KeyMappingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_KeyMappingPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_KeyMappingPopupExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_RaidRankingRewardUOExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidRankingRewardUOExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_RaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_RaidSeasonManageExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_ShopRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_ShopRecruitExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_SoundUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SoundUIExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
    }

def dump_ExcelDB_SpineLipsyncExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_SpineLipsyncExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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

def dump_ExcelDB_WebSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [ExcelDB_WebSeasonExcel(excel_instance.DataListField(j), password) for j in range(excel_instance.DataListFieldLength())],
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
