from enum import IntEnum
from lib.encryption import convert_short, convert_ushort, convert_int, convert_long, convert_float, convert_double, convert_string, convert_uint, convert_ulong, create_key
import inspect

def dump_table(table_instance) -> list:
    excel_name = table_instance.__class__.__name__.removesuffix("Table")
    current_module = inspect.getmodule(inspect.currentframe())
    dump_func = next(
        f
        for n, f in inspect.getmembers(current_module, inspect.isfunction)
        if n.removeprefix("dump_") == excel_name
    )
    password = create_key(excel_name.removesuffix("Excel"))
    return [dump_func(table_instance.DataList(j), password) for j in range(table_instance.DataListLength())]

class State(IntEnum):
    Normal = 0
    Hover = 1
    Pressed = 2
    Disabled = 3

class Trigger(IntEnum):
    OnClick = 0
    OnMouseOver = 1
    OnMouseOut = 2
    OnPress = 3
    OnRelease = 4
    OnDoubleClick = 5

class Restriction(IntEnum):
    None_ = 0
    Horizontal = 1
    Vertical = 2
    PressAndHold = 3

class DragEffect(IntEnum):
    None_ = 0
    Momentum = 1
    MomentumAndSpring = 2

class Arrangement(IntEnum):
    Horizontal = 0
    Vertical = 1
    CellSnap = 2

class Sorting(IntEnum):
    None_ = 0
    Alphabetic = 1
    Horizontal = 2
    Vertical = 3
    Custom = 4

class Action(IntEnum):
    PressAndClick = 0
    Select = 1
    All = 2

class Modifier(IntEnum):
    Any = 0
    Shift = 1
    Ctrl = 2
    Alt = 3
    None_ = 4

class Constraint(IntEnum):
    None_ = 0
    Vertical = 1
    Horizontal = 2
    Explicit = 3

class Trigger(IntEnum):
    OnClick = 0
    OnMouseOver = 1
    OnMouseOut = 2
    OnPress = 3
    OnRelease = 4
    Custom = 5
    OnEnable = 6
    OnDisable = 7

class Position(IntEnum):
    Auto = 0
    Above = 1
    Below = 2

class Selection(IntEnum):
    OnPress = 0
    OnClick = 1

class OpenOn(IntEnum):
    ClickOrTap = 0
    RightClick = 1
    DoubleClick = 2
    Manual = 3

class FillDirection(IntEnum):
    LeftToRight = 0
    RightToLeft = 1
    BottomToTop = 2
    TopToBottom = 3

class Movement(IntEnum):
    Horizontal = 0
    Vertical = 1
    Unrestricted = 2
    Custom = 3

class DragEffect(IntEnum):
    None_ = 0
    Momentum = 1
    MomentumAndSpring = 2

class ShowCondition(IntEnum):
    Always = 0
    OnlyIfNeeded = 1
    WhenDragging = 2

class Direction(IntEnum):
    Down = 0
    Up = 1

class Sorting(IntEnum):
    None_ = 0
    Alphabetic = 1
    Horizontal = 2
    Vertical = 3
    Custom = 4

class Alignment(IntEnum):
    Automatic = 0
    Left = 1
    Center = 2
    Right = 3
    Justified = 4

class SymbolStyle(IntEnum):
    None_ = 0
    Normal = 1
    Colored = 2
    NoOutline = 3

class UpdateCondition(IntEnum):
    OnStart = 0
    OnUpdate = 1
    OnLateUpdate = 2
    OnFixedUpdate = 3

class Direction(IntEnum):
    SourceUpdatesTarget = 0
    TargetUpdatesSource = 1
    BiDirectional = 2

class Type(IntEnum):
    Simple = 0
    Sliced = 1
    Tiled = 2
    Filled = 3
    Advanced = 4

class FillDirection(IntEnum):
    Horizontal = 0
    Vertical = 1
    Radial90 = 2
    Radial180 = 3
    Radial360 = 4

class AdvancedType(IntEnum):
    Invisible = 0
    Sliced = 1
    Tiled = 2

class Flip(IntEnum):
    Nothing = 0
    Horizontally = 1
    Vertically = 2
    Both = 3

class Clipping(IntEnum):
    None_ = 0
    TextureMask = 1
    SoftClip = 2
    ConstrainButDontClip = 3

class ShadowMode(IntEnum):
    None_ = 0
    Receive = 1
    CastAndReceive = 2

class AnchorUpdate(IntEnum):
    OnEnable = 0
    OnUpdate = 1
    OnStart = 2

class Pivot(IntEnum):
    TopLeft = 0
    Top = 1
    TopRight = 2
    Left = 3
    Center = 4
    Right = 5
    BottomLeft = 6
    Bottom = 7
    BottomRight = 8

class AspectRatioSource(IntEnum):
    Free = 0
    BasedOnWidth = 1
    BasedOnHeight = 2

class AnimationLetterOrder(IntEnum):
    Forward = 0
    Reverse = 1
    Random = 2

class Method(IntEnum):
    Linear = 0
    EaseIn = 1
    EaseOut = 2
    EaseInOut = 3
    BounceIn = 4
    BounceOut = 5

class Style(IntEnum):
    Once = 0
    Loop = 1
    PingPong = 2

class Side(IntEnum):
    BottomLeft = 0
    Left = 1
    TopLeft = 2
    Top = 3
    TopRight = 4
    Right = 5
    BottomRight = 6
    Bottom = 7
    Center = 8

class ControlScheme(IntEnum):
    Mouse = 0
    Touch = 1
    Controller = 2

class ClickNotification(IntEnum):
    None_ = 0
    Always = 1
    BasedOnDelta = 2

class EventType(IntEnum):
    World_3D = 0
    UI_3D = 1
    World_2D = 2
    UI_2D = 3

class ProcessEventsIn(IntEnum):
    Update = 0
    LateUpdate = 1

class InputType(IntEnum):
    Standard = 0
    AutoCorrect = 1
    Password = 2

class Validation(IntEnum):
    None_ = 0
    Integer = 1
    Float = 2
    Alphanumeric = 3
    Username = 4
    Name = 5
    Filename = 6

class KeyboardType(IntEnum):
    Default = 0
    ASCIICapable = 1
    NumbersAndPunctuation = 2
    URL = 3
    NumberPad = 4
    PhonePad = 5
    NamePhonePad = 6
    EmailAddress = 7

class OnReturnKey(IntEnum):
    Default = 0
    Submit = 1
    NewLine = 2

class Effect(IntEnum):
    None_ = 0
    Shadow = 1
    Outline = 2
    Outline8 = 3
    OutlineShadow1 = 4
    OutlineShadow = 5

class Overflow(IntEnum):
    ShrinkContent = 0
    ClampContent = 1
    ResizeFreely = 2
    ResizeHeight = 3

class Crispness(IntEnum):
    Never = 0
    OnDesktop = 1
    Always = 2

class Modifier(IntEnum):
    None_ = 0
    ToUppercase = 1
    ToLowercase = 2
    Custom = 3

class RenderQueue(IntEnum):
    Automatic = 0
    StartAt = 1
    Explicit = 2

class Scaling(IntEnum):
    Flexible = 0
    Constrained = 1
    ConstrainedOnMobiles = 2

class Constraint(IntEnum):
    Fit = 0
    Fill = 1
    FitWidth = 2
    FitHeight = 3

class Style(IntEnum):
    None_ = 0
    Horizontal = 1
    Vertical = 2
    Both = 3
    BasedOnHeight = 4
    FillKeepingRatio = 5
    FitInternalKeepingRatio = 6

class Style(IntEnum):
    Text = 0
    Chat = 1

class ComparerType(IntEnum):
    GREATER = 0
    LessOrEqual = 1

class OperatorType(IntEnum):
    AND = 0
    OR = 1

class SoP(IntEnum):
    SingleEvent = 0
    PersistentEvent = 1

class NoteLine(IntEnum):
    Left = 0
    Right = 1
    Both = 2

class NoteType(IntEnum):
    Normal = 0
    Long = 1
    Boom = 2

class NoteProperty(IntEnum):
    Flick = 0
    LongEnd = 1
    Normal = 2

class BattleResultType(IntEnum):
    Victory = 0
    Defeat = 1

class ShakerType(IntEnum):
    Default = 0
    GroundCommand = 1

class AnimatorStateName(IntEnum):
    Idle = 0
    AttackStart = 1
    AttackIng = 2
    AttackDelay = 3
    AttackEnd = 4
    Reload = 5
    Callsign = 6
    MoveEnd = 7
    MoveIng = 8
    MoveJump = 9
    MoveCallsign = 10
    RearrangeStart = 11
    RearrangeIdle = 12
    RearrangeReaction = 13
    VitalPanic = 14
    VitalDyingIng = 15
    VitalReatreat = 16
    VitalDeath = 17
    VictoryStart = 18
    VictoryEnd = 19
    Exs1 = 20
    MoveIngStart = 21
    MoveIngEnd = 22
    MoveEndRootMotion = 23
    MoveAttack = 24
    AttackReadyStart = 25
    AttackReadyEnd = 26
    Appear = 27
    Exs2 = 28
    Exs3 = 29
    PublicSkill1 = 30
    PublicSkill2 = 31
    PublicSkill3 = 32
    TSSInteractIdle = 33
    TSSInteractAttack = 34
    VitalDeathGroggy = 35
    VitalHit = 36
    MoveLeft = 37
    MoveRight = 38
    Exs4 = 39
    Exs5 = 40
    Exs6 = 41
    Exs7 = 42
    Exs8 = 43
    Exs9 = 44
    Exs10 = 45
    PublicSkill4 = 46
    PublicSkill5 = 47
    PublicSkill6 = 48
    PublicSkill7 = 49
    PublicSkill8 = 50
    PublicSkill9 = 51
    PublicSkill10 = 52
    TSSInteract = 53

class Shape(IntEnum):
    Unknown = 0
    Rect = 1
    Circle = 2
    Fan = 3
    Donut = 4
    Custom = 5

class PlayableAssetSelectionType(IntEnum):
    Ordered = 0
    Random = 1

class ForwardVector(IntEnum):
    Forward = 0
    Right = 1
    Up = 2
    Back = 3
    Left = 4
    Down = 5

class HeliState(IntEnum):
    None_ = 0
    Ready = 1
    Appear = 2
    Idle = 3
    Disappear = 4
    Max = 5

class AttendResultProcess(IntEnum):
    Progress = 0
    LocationRank = 1
    FavorGrowth = 2
    Rewards = 3

class EquipType(IntEnum):
    Account = 0
    IDCard = 1

class CommonEventType(IntEnum):
    TileConquer = 0
    TileUpgrade = 1
    BossOpen = 2
    StepComplete = 3
    MassErosion = 4
    Erosion = 5
    ErosionRemove = 6
    UnexpectedEvent = 7
    TileConquerReward = 8

class AttendResultProcess(IntEnum):
    Progress = 0
    LocationRank = 1
    FavorGrowth = 2

class FriendBlockListType(IntEnum):
    None_ = 0
    Friend = 1
    Block = 2

class FurnitureTimelineType(IntEnum):
    Idle = 0
    Req = 1
    Add = 2
    Make = 3
    Only = 4
    InteractionBGM = 5

class ScenarioCharacterTarget(IntEnum):
    Invalid = 0
    Front1 = 1
    Front2 = 2
    Front3 = 3
    Front4 = 4
    Front5 = 5
    Back1 = 6
    Back2 = 7
    Back3 = 8
    All_Front = 9
    All_Back = 10
    All = 11

class ScenarioTitleType(IntEnum):
    None_ = 0
    Default = 1
    Trailer = 2

class ScenarioEndingType(IntEnum):
    None_ = 0
    Finish = 1
    ToBeContinue = 2

class TextType(IntEnum):
    Normal = 0
    FadeIn = 1
    TypeWriter = 2

class LabelAlign(IntEnum):
    Left = 0
    Center = 1
    Right = 2

class StickerHasInfo(IntEnum):
    None_ = 0
    CanUnlock = 1
    Unlock = 2

class BossAppearState(IntEnum):
    Ready = 0
    World = 1
    Scenario = 2
    Clear = 3

class FromUIScene(IntEnum):
    Lobby = 0
    Work = 1
    ScenarioMode = 2

class SyncType(IntEnum):
    None_ = 0
    Manual = 1
    Auto = 2

class CharacterMemorialFilterType(IntEnum):
    None_ = 0
    One = 1
    OverOne = 2

class CharacterGearFilterType(IntEnum):
    DoesntExist = 0
    NotEquipped = 1
    Equipped = 2

class CharacterObscurationFilterType(IntEnum):
    Able = 0
    Unable = 1

class CharacterGearType(IntEnum):
    DoesntExist = 0
    NotEquipped = 1
    Tier1 = 2
    Tier2 = 3

class ContentBlockType(IntEnum):
    MinusGem = 0

class MemoryUnitType(IntEnum):
    B = 0
    KB = 1
    MB = 2
    GB = 3
    TB = 4

class MemorySpaceType(IntEnum):
    FreeSpace = 0
    BusySpace = 1
    TotalSpace = 2

class InputLayer(IntEnum):
    Network = 0
    Login = 1
    UIOpen = 2
    FadeInOrOut = 3
    Animation = 4
    BattleLoad = 5
    BattleUnLoad = 6
    Temp1 = 7
    Temp2 = 8
    Temp3 = 9
    Temp4 = 10
    BattleResult = 11
    PlatformService = 12
    CashShop = 13
    HexaPlayerMove = 14
    ArenaSimulation = 15
    UIDirector = 16
    CampaignEnter = 17
    InitEchelon = 18
    UIGetAsync = 19
    Transition = 20
    MailCheck = 21
    RuntimeHierarchy = 22
    TTS = 23

class SortingRule(IntEnum):
    StarGrade = 0
    Rarity = 1
    Level = 2
    FavorLevel = 3
    School = 4
    Name = 5
    ExSkillLevel = 6
    StreetBattleAdaptation = 7
    OutdoorBattleAdaptation = 8
    IndoorBattleAdaptation = 9
    ArmorType = 10
    WeaponType = 11
    GetTime = 12
    AttackPower = 13
    DefensePower = 14
    MaxHP = 15
    AttackRange = 16
    UniqueId = 17
    Count = 18
    ComfortBonus = 19
    SetGroudpId = 20
    BulletType = 21
    ExpirationTime = 22
    EventItem = 23
    EventToken1 = 24
    EventToken2 = 25
    EventToken3 = 26
    EventToken4 = 27
    EventToken5 = 28
    TacticRole = 29
    SkillLevel = 30
    Interaction = 31
    DisplayOrder = 32
    BirthDay = 33
    Favorite = 34
    ConquestStep = 35
    ConquestBaseLevel = 36
    ConquestTileId = 37
    EventArchive_Default = 38
    EventArchive_Name = 39
    EventArchive_Incomplete = 40
    PotentialMaxHp = 41
    PotentialAttackPower = 42
    PotentialHealPower = 43
    WeaponGrade = 44
    AccountLevel = 45
    LastConnectTime = 46
    Gear = 47
    ExSkillCost = 48
    HealPower = 49

class ChatSortingRule(IntEnum):
    DateTime = 0
    Unread = 1
    Name = 2
    FavorLevel = 3
    Favorite = 4

class SortingOrder(IntEnum):
    Ascending = 0
    Descending = 1

class MultiSweepFilterOption(IntEnum):
    None_ = 0
    SecretStone = 1
    Equipment = 2
    Material = 3

class MultiSweepStageDifficultyFilterOption(IntEnum):
    None_ = 0
    Normal = 1
    Hard = 2

class MultiSweepStageFilterOption(IntEnum):
    None_ = 0
    Possible = 1
    Impossible = 2

class CraftFilterOption(IntEnum):
    None_ = 0
    Equipment = 1
    Furniture = 2
    Decoration = 3
    Interior = 4
    SecretStone = 5
    Coin = 6
    Material = 7
    Favor = 8

class ShiftingCraftFilterOption(IntEnum):
    None_ = 0
    ShiftingCraftCategory_CommonMaterial = 1
    ShiftingCraftCategory_CDItem = 2
    ShiftingCraftCategory_BookItem = 3
    ShiftingCraftCategory_Furniture = 4
    ShiftingCraftCategory_FavorItem = 5

class ItemFilter(IntEnum):
    None_ = 0
    SecretStone = 1
    Coin = 2
    Material = 3
    Consumable = 4
    Favor = 5
    Collectible = 6
    All = 7

class EquipmentFilter(IntEnum):
    All = 0

class MultiSweepFilter(IntEnum):
    None_ = 0
    SecretStone = 1
    Equipment = 2
    Material = 3

class MultiSweepStageDifficultyFilter(IntEnum):
    None_ = 0
    Normal = 1
    Hard = 2

class MultiSweepStageFilter(IntEnum):
    None_ = 0
    Possible = 1
    Impossible = 2

class CraftFilter(IntEnum):
    None_ = 0
    Equipment = 1
    Furniture = 2
    Decoration = 3
    Interior = 4
    SecretStone = 5
    Coin = 6
    Material = 7
    Favor = 8
    All = 9

class ShiftingCraftRecipeFilter(IntEnum):
    None_ = 0
    ShiftingCraftCategory_CommonMaterial = 1
    ShiftingCraftCategory_CDItem = 2
    ShiftingCraftCategory_BookItem = 3
    ShiftingCraftCategory_Furniture = 4
    ShiftingCraftCategory_FavorItem = 5
    All = 6

class ClanJoinFilter(IntEnum):
    Free = 0
    Permission = 1
    All = 2

class ShopFilter(IntEnum):
    Resource1 = 0
    Resource2 = 1
    All = 2

class TBGState(IntEnum):
    Move = 0
    Dead = 1
    Encounter = 2

class AudioType(IntEnum):
    SFX = 0
    Voice = 1

class Character(IntEnum):
    Main = 0
    Sub = 1

class Type(IntEnum):
    Start = 0
    End = 1

class Trigger(IntEnum):
    OnClick = 0
    LongPress = 1
    OnPress = 2
    Count = 3

class MXToggleState(IntEnum):
    On = 0
    Off = 1
    Disable = 2

class Axis(IntEnum):
    None_ = 0
    X = 1
    Y = 2
    Z = 3

class Axis(IntEnum):
    X = 0
    Y = 1
    Z = 2

class Bound(IntEnum):
    OUTSIDE = 0
    INSIDE = 1

class LifeType(IntEnum):
    ParticleStopAction = 0
    ScaledTimer = 1
    UnscaledTimer = 2
    SyncParentTimeline = 3
    ParentTimelineTimer = 4

class ResizeType(IntEnum):
    Off = 0
    FullScreen = 1
    Relative = 2
    FitWithFixedRatio = 3

class MaterialPropertyType(IntEnum):
    VALUE = 0
    COLOR = 1

class CurveType(IntEnum):
    IncreaseLinear = 0
    IncreaseEaseIn = 1
    IncreaseEaseOut = 2
    IncreaseEaseInOut = 3
    DecreaseLinear = 4
    DecreaseEaseIn = 5
    DecreaseEaseOut = 6
    DecreaseEaseInOut = 7
    Constant = 8

class Trigger(IntEnum):
    BattleEnd = 0

class CameraFindType(IntEnum):
    None_ = 0
    MainCameraTag = 1
    FxCameraTag = 2
    Parent = 3
    Child = 4
    GameMain = 5
    Current = 6
    UICamera = 7

class eAmbientType(IntEnum):
    Skybox = 0
    Gradient = 1
    Color = 2

class ScenarioCharacterFade(IntEnum):
    NONE = 0
    FADE_IN = 1
    FADE_OUT = 2

class BehaviorType(IntEnum):
    BaseTrack = 0
    Masked = 1
    MaskedRandomTiming = 2

class FinishType(IntEnum):
    DoNothing = 0
    PlayIdle = 1
    FinishMask = 2
    PlayNext = 3

class PreDelayType(IntEnum):
    Immediate = 0
    Random = 1
    DelayedRandom = 2

class LockScreenDisplay(IntEnum):
    Secret = 0
    Private = 1
    Public = 2

class NotificationStyle(IntEnum):
    None_ = 0
    NoSound = 1
    Default = 2
    Popup = 3

class SplitDownloadType(IntEnum):
    Direct = 0
    Scene = 1
    Scenario = 2

class LanguageTypeYostar(IntEnum):
    CN = 0
    EN = 1
    JP = 2
    KR = 3

class LoginMethod(IntEnum):
    None_ = 0
    Device = 1
    MigrationCode = 2
    PublisherPlatform = 3
    Twitter = 4
    FaceBook = 5
    Google = 6
    GooglePlay = 7
    Apple = 8
    Amazon = 9
    Nintendo = 10

class Platform(IntEnum):
    None_ = 0
    Yostar = 1
    YostarWhitGooglePlayGames = 2

class PlatformServiceState(IntEnum):
    Default = 0
    WaitInitResponded = 1
    Ready = 2
    InitFailed = 3
    NeedReInit = 4

class PurchaseServerTagYostar(IntEnum):
    STANDBY2 = 0
    STANDBY1 = 1
    MAJOR = 2
    MINOR = 3
    TEST = 4
    TEST_IN = 5
    AUDIT = 6
    PRE_AUDIT = 7
    PRODUCTION = 8
    HOTFIX = 9

class ResultCodeYostar(IntEnum):
    Unknown = 0
    OK = 1
    DEVICE_ID_BLOCKED = 2
    UID_OR_TOKEN_INVALIDCERT = 3
    ACCOUNT_CREATE_FAILED = 4
    ACCOUNT_BIND_FAILED_12 = 5
    ACCOUNT_BIND_FAILED_13 = 6
    ACCOUNT_BIND_FAILED_14 = 7
    ACCOUNT_BIND_FAILED_15 = 8
    ACCOUNT_BIND_FAILED_16 = 9
    LOGIN_PARAM_MISS = 10
    IP_BLOCKED = 11
    UID_BLOCKED = 12
    ACCESSTOKEN_INVALIDCERT = 13
    MIGRATIONCODE_INVALIDCERT = 14
    BIRTHSET_ALREADYSET = 15
    BIRTHSET_INVALIDFMT = 16
    SOCIAL_ACCOUNT_NOT_LINK = 17
    SOCIAL_ACCOUNT_PARAM_INVALIDCERT = 18
    SOCIAL_ACCOUNT_ALREADY_LINK = 19
    PLAY_GAME_ACCOUNT_LINK_OTHER_UID_ALREADY = 20
    UID_LINK_OTHER_PLAY_GAME_ACCOUNT_ALREADY = 21
    UID_AND_PLAY_GAME_ACCOUNT_ALL_LINKED_OTHER = 22
    PLAY_GAME_ACCOUNT_CAN_NOT_LINK_GUEST = 23
    UID_HAVE_NOT_LINK_PLAY_GAME_ACCOUNT = 24
    UID_LINK_PLAY_GAME_ACCOUNT_SUCCESS = 25
    GOOGLE_PLAY_GAME_TOKEN_AUTH_FAIL = 26
    PLAY_GAME_ACCOUNT_UNLNK_WARN = 27
    SOCIAL_ACCOUNT_UID_INVALIDCERT = 28
    LINK_PLATFORM_ERROR = 29
    UNLINK_PLATFORM_ERROR = 30
    UNLINK_ATLEAST_HAVE_ONE_ACCOUNT = 31
    FB_LOGIN_CANCEL = 32
    FB_AUTHORIZATION_CANCEL = 33
    TW_AUTHORIZATION_CANCEL = 34
    ERROR_GOOGLE_FAILE = 35
    GOOGLE_SIGN_IN_CANCELLED = 36
    GOOGLE_PLAY_INVALD = 37
    GOOGLE_SIGN_IN_CURRENTLY_IN_PROGRESS = 38
    GOOGLE_SIGN_IN_FAILED = 39
    USER_DELETE_ACCOUNT = 40
    INIT_FAILED = 41
    YOSTAR_EMAIL_ERROR = 42
    YOSTAR_EMAIL_DOUBLE_CHK_ERROR = 43
    VERIFICATION_CODE_REQ_FAST = 44
    VERIFICATION_CODE_OVERDUE_1 = 45
    VERIFICATION_CODE_OVERDUE_2 = 46
    ACCOUNT_HAS_BEEN_FREEZE = 47
    VERIFICATION_CODE_NULL = 48
    GEETEST_FAIL = 49
    GEETEST_VERIFICATION_FAIL = 50
    HTTPERROR = 51
    PAY_BIRTH_NOTSET = 52
    PAY_OVER_LIMIT = 53
    PAY_PRODUCT_INVALID = 54
    PAY_STORE_INVALID = 55
    PAY_SERVERTAG_INVALID = 56
    PAY_ILLEGAL_CURRENCY = 57
    PAY_VERIFY_ERROR = 58
    PAY_AIRIPLATFORM_INVALID_REQUEST = 59
    PAY_GAMESERVER_INVALID_REQUEST = 60
    PAY_HOLDON = 61
    PAY_INVALID_ORDERID = 62
    PAY_TIMEOUT = 63
    PAY_INVALID_PRODUCT_IN_STORE = 64
    PAY_STORE_FAILURE = 65
    PAY_CANCELED = 66
    PAY_CANCELED_OR_FAIL = 67
    PAY_NOT_SUPORT = 68
    GOOGLE_BILLING_UNAVAILABLE = 69
    GOOGLE_DEVELOPER_ERROR = 70
    GOOGLE_FATAL_ERROR = 71
    GOOGLE_FEATURE_NOT_SUPPORTED = 72
    GOOGLE_ITEM_ALREADY_OWNED = 73
    GOOGLE_ITEM_NOT_OWNED = 74
    GOOGLE_ITEM_UNAVAILABLE = 75
    GOOGLE_SERVICE_DISCONNECTED = 76
    GOOGLE_SERVICE_TIMEOUT = 77
    GOOGLE_SERVICE_UNAVAILABLE = 78
    GOOGLE_USER_CANCELED = 79
    SDK_GETSKUS_FAILED = 80
    GOOGLE_CONNECT_FAILED = 81
    APPSTORE_BILL_UNFINISH = 82
    SAMSUNG_CONSUME_QUERY_ERROR = 83
    SYSTEM_SHARE_FAILED = 84
    SHARE_NOT_SUPORT = 85
    SHARE_APP_NOT_INSTALL = 86
    ERROR_HAD_DELETE = 87
    ERROR_REBORN_FAILED = 88
    ERROR_REBORN_FAILED_NO_DELETE = 89
    ERROR_LOGIN_FAILED_DELETE = 90
    ERROR_LOGIN_FAILED_CANT_LOGIN = 91
    ERROR_CRETAE_OREDER_REPEAT = 92
    ERROR_NEED_CONFIRM_AGREMENT = 93
    ERROR_ONE_STORE_NEED_LOGIN = 94
    ERROR_NO_NEED_KMC_CERT = 95
    ERROR_NEED_KMC_CERT = 96
    ERROR_KMC_CERT_EXPIRE = 97
    NINTENDO_AUTH_CANCEL = 98
    NINTENDO_AUTH_FAIL = 99
    NINTENDO_USER_NOT_EXIST = 100
    NINTENDO_ACCOUNT_UNAVAILABLE = 101
    NINTENDO_ACCOUNT_UNLINK_UID = 102
    NINTENDO_LOGIN_AUTH_FAIL = 103
    YOSTAR_ACCOUNT_NOT_EXIST = 104
    YOSTAR_ACCOUNT_LINKED_NINTENDO_ALREADY = 105
    YOSTAR_ACCOUNT_UNLINKED_NINTENDO = 106
    NINTENDO_ACCOUNT_LINKED_YOSTAR_ALREADY = 107
    Error_Survey_Not_Found = 108
    Error_Survey_Notify = 109
    ERROOR_PARAMS = 110
    ERROR_Not_Support_TwitterBind = 111
    ERROR_Not_Support_TwitterOverrideBind = 112
    ERROR_Not_SupportTwitterRegist = 113
    ERROR_Not_SupportTwitterLogin = 114

class ShopAgreementTypeYostar(IntEnum):
    SHOP_AGREEMENT_1 = 0
    SHOP_AGREEMENT_2 = 1

class PatchGroupType(IntEnum):
    None_ = 0
    Catalog = 1
    Preload = 2
    GameData = 3

class CafeInputState(IntEnum):
    Default = 0
    GiveGift = 1
    EditReady = 2
    Edit = 3

class TweenType(IntEnum):
    LinearTween = 0
    EaseInQuad = 1
    EaseOutQuad = 2
    EaseInOutQuad = 3
    EaseInCubic = 4
    EaseOutCubic = 5
    EaseInOutCubic = 6
    EaseInQuart = 7
    EaseOutQuart = 8
    EaseInOutQuart = 9
    EaseInQuint = 10
    EaseOutQuint = 11
    EaseInOutQuint = 12
    EaseInSine = 13
    EaseOutSine = 14
    EaseInOutSine = 15
    EaseInExpo = 16
    EaseOutExpo = 17
    EaseInOutExpo = 18
    EaseInCirc = 19
    EaseOutCirc = 20
    EaseInOutCirc = 21

class StatFeature(IntEnum):
    NotSupported = 0
    Fixed = 1
    Leveling = 2

class EventRewardRealType(IntEnum):
    ItemCampaignNormal = 0
    ItemCampaignHard = 1
    ItemChaser = 2
    ItemFindGift = 3
    ItemBlood = 4
    ItemSchoolDungeon = 5
    ItemAcademy = 6
    ItemTimeAttack = 7
    ItemRaid = 8
    ExpAccount = 9

class UISiblingPriority(IntEnum):
    VeryLow = 0
    Low = 1
    Normal = 2
    High = 3
    VeryHigh = 4

class MessangerDisplayType(IntEnum):
    Student = 0
    Chat = 1

class TimerType(IntEnum):
    None_ = 0
    ArenaLobby = 1
    ArenaEntry = 2
    ArenaFormation = 3

class TabType(IntEnum):
    Battle = 0
    Time = 1
    Daily = 2
    Season = 3
    NewRecord = 4

class ArenaRecordType(IntEnum):
    Season = 0
    AllTime = 1

class SwipeDir(IntEnum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class UITargetFPS(IntEnum):
    DontCare = 0
    FPS15 = 1
    FPS20 = 2
    FPS30 = 3

class CountDisplayType(IntEnum):
    Normal = 0
    None_ = 1
    Wave = 2
    FindGift = 3

class UseType(IntEnum):
    CanUse = 0
    CanNotUse = 1
    NotEnoughCost = 2
    InvalidStatus = 3
    OnTSS = 4

class BattleResultType(IntEnum):
    Victory = 0
    Defeat = 1

class CafeTemplateElementCountState(IntEnum):
    Enough = 0
    NotEnough = 1
    None_ = 2

class SocialList(IntEnum):
    Friend = 0
    Clan = 1

class UIType(IntEnum):
    Start = 0
    Story = 1
    Enemy = 2
    Player = 3

class CharacterDetailDisplayState(IntEnum):
    None_ = 0
    HasCharacter = 1
    DefaultInfo = 2
    ExchangeCharacterByGoods = 3

class TileState(IntEnum):
    Conquested = 0
    Conquestable = 1
    Enemy = 2
    TreasureBox = 3
    Operating = 4

class Damage(IntEnum):
    Damage = 0
    Damaged = 1
    Heal = 2
    Max = 3

class Target(IntEnum):
    All = 0
    Obstacle = 1
    Character = 2
    Max = 3

class Path(IntEnum):
    All = 0
    Normal = 1
    Ex = 2
    Public = 3
    Passive = 4
    ExtraPassive = 5
    Max = 6

class PopupType(IntEnum):
    None_ = 0
    Rank = 1
    MissionFailed = 2
    LevelUp = 3
    Refund = 4
    Reward = 5
    TutorialFailure = 6
    EventResult = 7
    Max = 8

class DiceAnimatorState(IntEnum):
    DiceRace_Idle = 0
    DiceRace_Run = 1
    DiceRace_Run_End = 2
    DiceRace_Finish = 3
    DiceRace_Reward = 4
    None_ = 5

class CharacterState(IntEnum):
    Buff = 0
    Possesion = 1
    NotHeld = 2

class CGOrientation(IntEnum):
    Landscape = 0
    Portrait = 1

class UITreasureObjectRotationType(IntEnum):
    None_ = 0
    Clockwise = 1
    CounterClockwise = 2

class FormationSupportStatChange(IntEnum):
    None_ = 0
    Up = 1
    Down = 2

class From(IntEnum):
    Campaign = 0
    EventContent = 1
    Raid = 2
    WeekDungeonChaserA = 3
    WeekDungeonChaserB = 4
    WeekDungeonChaserC = 5
    ArenaOffense = 6
    ArenaDefense = 7
    Scenario = 8
    SubStage = 9
    EventSubStage = 10
    Lobby = 11
    WeekDungeonBlood = 12
    WeekDungeonFindGift = 13
    TutorialStage = 14
    SchoolDungeonA = 15
    SchoolDungeonB = 16
    SchoolDungeonC = 17
    TimeAttackDungeon = 18
    WorldRaid = 19
    Conquest = 20
    StoryStrategy = 21
    EliminateRaid = 22
    Field = 23
    MultiFloorRaid = 24
    CampaignStrategySkip = 25
    MinigameDefense = 26

class TouchState(IntEnum):
    None_ = 0
    Down = 1
    Press = 2
    Drag = 3
    Up = 4

class NoticePrefabType(IntEnum):
    None_ = 0
    Import = 1
    Overwrite = 2
    EditName = 3

class FriendTab(IntEnum):
    MyFriend = 0
    RequestSent = 1
    RequestReceived = 2
    Search = 3

class FriendShowToggleFlag(IntEnum):
    AccountLevel = 0
    FriendCode = 1
    RaidRanking = 2
    EliminateRaidRanking = 3
    ArenaRanking = 4
    All = 5

class UIUserInfoTab(IntEnum):
    Profile = 0
    Record = 1
    Support = 2

class ShowDirectingType(IntEnum):
    None_ = 0
    Normal = 1
    SSR = 2
    FakeSSR = 3

class IconType(IntEnum):
    None_ = 0
    Stat = 1
    Status = 2
    Dot = 3
    Max = 4

class AnimationEnableFlag(IntEnum):
    New = 0
    NewRefresh = 1
    NearEnd = 2
    Dispel = 3
    DispelRefresh = 4
    All = 5
    None_ = 6

class GaugeAttachType(IntEnum):
    HPBar = 0
    BottomUI = 1

class GaugeType(IntEnum):
    ProgressBar = 0
    Dial = 1

class ActionType(IntEnum):
    SetActive = 0
    ChangeColor = 1
    TextureChange = 2
    PlayAnimation = 3
    MaterialChange = 4
    BoolValueChange = 5

class TriggerType(IntEnum):
    UIType = 0
    GaugeEqual = 1
    GaugeEqualOver = 2
    GaugeEqualUnder = 3
    FormIndex = 4

class InvisibleFlag(IntEnum):
    None_ = 0
    EmojiPlay = 1
    HideUI = 2
    Timeline = 3
    Dead = 4
    All = 5

class InvisibleFlag(IntEnum):
    None_ = 0
    HideUI = 1
    HPBarHideExcel = 2
    HideHPBarComponent = 3
    BulletTime = 4
    ConfrontationGauge = 5
    Dead = 6
    Timeline = 7
    LogicEffectHide = 8
    All = 9

class UISiblingPriority(IntEnum):
    VeryLow = 0
    Low = 1
    Normal = 2
    High = 3
    VeryHigh = 4

class UIOpenType(IntEnum):
    FromLobby = 0
    FromFloor = 1
    MoveAnimation = 2

class TooltipType(IntEnum):
    None_ = 0
    Description = 1
    Parcel = 2
    ParcelCannotUseShortcut = 3
    ShortcutOnly = 4
    Stat = 5
    Max = 6
    SkillInfo = 7

class ButtonLayout(IntEnum):
    NoButton = 0
    OneButton = 1
    TwoButton = 2
    MAX_BUTTON_LAYOUT = 3

class State(IntEnum):
    Download = 0
    Complete = 1

class AgreementType(IntEnum):
    None_ = 0
    UserAgreement = 1
    PrivacyPolicy = 2
    FundSettlement = 3
    SpecificCommerce = 4

class InputType(IntEnum):
    Nickname = 0
    Callname = 1
    Comment = 2

class UIPopup_Input_CommentMode(IntEnum):
    None_ = 0
    Account = 1
    IdCard = 2

class RaidRewardSubTab(IntEnum):
    Ranking = 0
    Point = 1
    Limited = 2

class RaidRewardTab(IntEnum):
    RewardEnd = 0
    RewardSeason = 1

class RedDotRaidType(IntEnum):
    Raid = 0
    EliminateRaid = 1
    Playing = 2

class BeforehandGachaSelectResultType(IntEnum):
    SAVE = 0
    CURRENT = 1

class CategoryShopParcelDisplayType(IntEnum):
    None_ = 0
    ByCost = 1
    ByCategoryToCurrency = 2

class GachaCountType(IntEnum):
    ONE = 0
    TEN = 1

class BeforehandGachaPopupOpenType(IntEnum):
    SAVE = 0
    SAVEINFO = 1
    SELECT = 2

class WidgetDisplayType(IntEnum):
    Accumulate = 0
    Each = 1

class SortUIType(IntEnum):
    CharStar = 0
    Label = 1
    Event = 2

class ItemState(IntEnum):
    IS_NORMAL = 0
    IS_DISABLE = 1
    END = 2

class AssetDataClearType(IntEnum):
    None_ = 0
    RESTORE = 1
    CACHE_CLEAR = 2
    CACHE_CLEAR_ALL = 3
    INIT_GAMESETTING = 4

class PopupType(IntEnum):
    None_ = 0
    Rank = 1
    StageClear = 2
    LevelUp = 3
    StageMission = 4
    Reward = 5
    EventResult = 6
    Max = 7

class CanNotTouchTypes(IntEnum):
    None_ = 0
    Never = 1
    TouchableByMode = 2

class FitType(IntEnum):
    Fullscreen = 0
    FitWidth = 1
    FitHeight = 2

class ConnectState(IntEnum):
    Prepare = 0
    Connecting = 1
    Success = 2
    Fail = 3

class StateResultCode(IntEnum):
    Maintain = 0
    Normal = 1
    AppUpdate = 2

class DataHashException(IntEnum):
    GET_LOCAL_DATAHASH_STORE = 0
    SAVE_LOCAL_DATAHASH = 1
    SAVE_LOADL_DATAHASH_DICTIONARY = 2
    GET_LOCAL_DATAHASH = 3
    DELETE_LOCAL_DATAHASH = 4
    DELETE_LOCAL_DATAHASH_BY_LIST = 5
    DELETE_ALL_LOCAL_DATAHASH = 6
    GET_ALL_LOCAL_DATAHASH_PATTERN = 7

class SensitiveCheckType(IntEnum):
    CallName = 0
    Name = 1
    SelfIntroduction = 2
    ClanIntroduction = 3
    ClanChat = 4
    BirthDay = 5

class SensitiveResultType(IntEnum):
    Success = 0
    NullValue = 1
    OnlyCN = 2
    OnlyCNAZ09 = 3
    OnlyCNAZ09Sign = 4
    Only09 = 5
    NumLimit = 6
    Sensitive = 7
    BirthDayLimit = 8

class UCBTNodeTag(IntEnum):
    Begin = 0
    GetNextPath = 1
    MovePath = 2
    AfterMovePath = 3
    GuardMode = 4
    IsStunned = 5
    IsStunnedReady = 6
    IsConfused_UNUSED = 7
    Stun = 8
    StunReady = 9
    FindNoiseMaker = 10
    LookAtNoiseMaker = 11
    CustomAnimation = 12
    End = 13

class UCEntityTypes(IntEnum):
    Plain = 0
    Player = 1
    NPC = 2
    Boss = 3
    Obstacle = 4
    Projectile = 5
    Particle = 6
    Prop = 7

class UCEntityStatus(IntEnum):
    None_ = 0
    StunReady = 1
    Stun = 2

class DebugLogType(IntEnum):
    Debug = 0
    Warning = 1
    Error = 2

class UCPersonalityType(IntEnum):
    None_ = 0
    All = 1
    CH0070 = 2
    CH0280 = 3

class UIButtonBindType(IntEnum):
    None_ = 0
    SkillButton_1 = 1
    SkillButton_2 = 2
    ItemButton = 3

class UIItemQuickSlotBindType(IntEnum):
    None_ = 0
    ItemQuickSlot_1 = 1
    ItemQuickSlot_2 = 2
    ItemQuickSlot_3 = 3

class Type(IntEnum):
    LeftStick = 0

class Clockwise(IntEnum):
    DontCare = 0
    Clockwise = 1
    CounterClockwise = 2

class RefreshEventType(IntEnum):
    None_ = 0
    DisableAll = 1
    ByQuickSlot = 2
    ByPolymorph = 3
    ByHide = 4
    BySwitch = 5
    ByActionButtonEffect = 6

class UCRuntimeObjectType(IntEnum):
    Common = 0
    Skill_NoiseMaker = 1

class States(IntEnum):
    Initialize = 0
    Playing = 1
    Detected = 2
    LoadingSavePoint = 3
    EnterStageAction = 4
    GameOver = 5
    ClearStage = 6

class UCButtonStateFlags(IntEnum):
    None_ = 0
    Press = 1
    Drag = 2
    DragOut = 3

class UCButtonVisualState(IntEnum):
    Empty = 0
    Enable = 1
    Disable = 2
    Cooltime = 3
    InBox = 4
    InCabinet = 5

class CommandMode(IntEnum):
    MoveImmediately = 0
    MovePosition = 1
    MovePositionDelta = 2
    RotateImmediately = 3

class UCNPCAnimations(IntEnum):
    Enter = 0
    IdleAndMove_01 = 1
    CatchPlayer = 2
    EX_01 = 3
    Panic_01 = 4
    Exit = 5

class UCPlayerAnimations(IntEnum):
    Enter = 0
    Idle = 1
    IdleAndMoveMixer_01 = 2
    RotateRun = 3
    UseSkill_01 = 4
    UseSkill_02 = 5
    GetItem_01 = 6
    UseItem_Self_01 = 7
    UseItem_Throw_01 = 8
    UseItem_Shot_01 = 9
    Interaction_Use_01 = 10
    Interaction_Use_WalkiTalkie_01 = 11
    Panic_01 = 12
    Exit = 13

class UCPropAnimations(IntEnum):
    Enter = 0
    Idle = 1
    IdleAndMoveMixer = 2
    Open = 3
    Close = 4
    Off = 5
    Interation_01 = 6
    Interation_02 = 7
    Interation_03 = 8
    Interation_04 = 9
    CatchPlayer = 10
    Exit = 11

class ErrorCode(IntEnum):
    PROCESS_TIMEOUT = 0
    APPLICATION_SUSPEND = 1
    HTTP_CLIENT_ERROR = 2
    HTTP_SERVER_ERROR = 3
    NETWORK_ERROR = 4
    FILESYSTEM_ERROR = 5
    APPLICATION_ERROR = 6
    CONSISTENCY_ERROR = 7

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
    FurnitureEtc = 4
    FurnitureSubCategory1 = 5
    Prop = 6
    HomeAppliance = 7
    WallDecoration = 8
    FloorDecoration = 9
    DecorationEtc = 10
    DecorationSubCategory1 = 11
    Floor = 12
    Background = 13
    Wallpaper = 14
    InteriorsSubCategory1 = 15
    All = 16

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

class TargetingCellType(IntEnum):
    None_ = 0
    Near = 1
    Far = 2

class TargetingUnitType(IntEnum):
    None_ = 0
    Near = 1
    Far = 2
    MinHp = 3
    MaxHp = 4
    Random = 5

class ProjectileAction(IntEnum):
    None_ = 0
    Damage = 1
    Heal = 2

class FontType(IntEnum):
    None_ = 0
    Damage = 1
    Block = 2
    Heal = 3
    Miss = 4
    Critical = 5
    Skill = 6
    Immune = 7
    DamageResist = 8
    DamageWeak = 9
    CriticalResist = 10
    CriticalWeak = 11
    Effective = 12
    CriticalEffective = 13

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

class DamageType(IntEnum):
    Normal = 0
    Critical = 1
    IgnoreDefence = 2

class FormationLine(IntEnum):
    Students = 0
    TSS = 1

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

class TacticEntityType(IntEnum):
    None_ = 0
    Student = 1
    Minion = 2
    Elite = 3
    Champion = 4
    Boss = 5
    Obstacle = 6
    Servant = 7
    Vehicle = 8
    Summoned = 9
    Hallucination = 10
    DestructibleProjectile = 11

class BuffIconType(IntEnum):
    None_ = 0
    Debuff_DyingPenalty = 1
    CC_MindControl = 2
    CC_Inoperative = 3
    CC_Confusion = 4
    CC_Provoke = 5
    CC_Silence = 6
    CC_Blind = 7
    Dot_Damage = 8
    Dot_Heal = 9
    Buff_AttackPower = 10
    Buff_CriticalChance = 11
    Buff_CriticalDamage = 12
    Buff_DefensePower = 13
    Buff_Dodge = 14
    Buff_Hit = 15
    Buff_WeaponRange = 16
    Buff_SightRange = 17
    Buff_MoveSpeed = 18
    Buff_Mind = 19
    Debuf_AttackPower = 20
    Debuff_CriticalChance = 21
    Debuff_CriticalDamage = 22
    Debuff_DefensePower = 23
    Debuff_Dodge = 24
    Debuff_Hit = 25
    Debuff_WeaponRange = 26
    Debuff_SightRange = 27
    Debuff_MoveSpeed = 28
    Debuff_Mind = 29
    Buff_AttackTime = 30
    Debuff_AttackTime = 31
    Buff_MaxHp = 32
    Debuff_MaxHp = 33
    Buff_MaxBulletCount = 34
    Debuff_MaxBulletCount = 35
    Debuff_SuppliesCondition = 36
    Buff_HealEffectivenessRate = 37
    Debuff_HealEffectivenessRate = 38
    Buff_HealPower = 39
    Debuff_HealPower = 40
    Buff_CriticalChanceResistPoint = 41
    Debuff_CriticalChanceResistPoint = 42
    CC_Stunned = 43
    Debuff_ConcentratedTarget = 44
    Buff_Immortal = 45
    Max = 46

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

class ObstacleClass(IntEnum):
    MAIN = 0
    SUB = 1

class ObstacleDestroyType(IntEnum):
    Remain = 0
    Remove = 1

class ObstacleHeightType(IntEnum):
    Low = 0
    Middle = 1
    High = 2

class ObstacleCoverType(IntEnum):
    None_ = 0
    Cover = 1
    Shelter = 2

class SkillCategory(IntEnum):
    None_ = 0

class LogicEffectCategory(IntEnum):
    None_ = 0
    Attack = 1
    Heal = 2
    Buff = 3
    Debuff = 4
    CrowdControl = 5
    Boss = 6
    Dummy = 7

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

class SkillPriorityCheckCondition(IntEnum):
    None_ = 0
    HPRateUnder = 1
    DebuffCountOver = 2
    BuffCountOver = 3
    CrowdControlOver = 4

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

class AmplifyDoTRemoveCondition(IntEnum):
    None_ = 0
    ApplyCount = 1

class LogicEffectSound(IntEnum):
    None_ = 0
    Damage = 1
    Heal = 2
    Knockback = 3

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

class ClearCheck(IntEnum):
    None_ = 0
    Success_Play = 1
    Success_Sweep = 2
    Fail_Timeout = 3
    Fail_PlayerGiveUp = 4
    Fail_Annihilation = 5

class BuffType(IntEnum):
    None_ = 0
    Buff_AttackPower = 1
    Buff_CriticalChance = 2
    Buff_CriticalDamage = 3
    Buff_DefensePower = 4
    Buff_Dodge = 5
    Buff_Hit = 6
    Buff_WeaponRange = 7
    Buff_SightRange = 8
    Buff_MoveSpeed = 9
    Buff_AttackTime = 10
    Buff_MaxHp = 11
    Buff_MaxBulletCount = 12
    DeBuff_AttackPower = 13
    DeBuff_CriticalChance = 14
    DeBuff_CriticalDamage = 15
    DeBuff_DefensePower = 16
    DeBuff_Dodge = 17
    DeBuff_Hit = 18
    DeBuff_WeaponRange = 19
    DeBuff_SightRange = 20
    DeBuff_MoveSpeed = 21
    DeBuff_AttackTime = 22
    DeBuff_MaxHp = 23
    DeBuff_MaxBulletCount = 24

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

class StatLevelUpType(IntEnum):
    Standard = 0
    Premature = 1
    LateBloom = 2
    Obstacle = 3
    TimeAttack = 4

class GrowthCategory(IntEnum):
    None_ = 0
    LevelUp = 1
    Transcend = 2
    SkillLevelUp = 3

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
    HealRate = 69
    HealLightArmorRate = 70
    HealHeavyArmorRate = 71
    HealUnarmedRate = 72
    HealElasticArmorRate = 73
    HealNormalArmorRate = 74
    HealedExplosionRate = 75
    HealedPierceRate = 76
    HealedMysticRate = 77
    HealedSonicRate = 78
    HealedNormalRate = 79
    Max = 80

class ProductionStep(IntEnum):
    ToDo = 0
    Doing = 1
    Complete = 2
    Release = 3

class TacticRole(IntEnum):
    None_ = 0
    DamageDealer = 1
    Tanker = 2
    Supporter = 3
    Healer = 4
    Vehicle = 5

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

class CVExceptionTarget(IntEnum):
    CharacterId = 0
    SquadType = 1

class PotentialStatBonusRateType(IntEnum):
    None_ = 0
    MaxHP = 1
    AttackPower = 2
    HealPower = 3

class ClanSocialGrade(IntEnum):
    None_ = 0
    President = 1
    Manager = 2
    Member = 3
    Applicant = 4
    Refused = 5
    Kicked = 6
    Quit = 7
    VicePredisident = 8

class ClanJoinOption(IntEnum):
    Free = 0
    Permission = 1
    All = 2

class ClanSearchOption(IntEnum):
    Name = 0
    Id = 1

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

class ConquestItemType(IntEnum):
    None_ = 0
    EventPoint = 1
    EventToken1 = 2
    EventToken2 = 3
    EventToken3 = 4
    EventToken4 = 5
    EventToken5 = 6

class ConquestProgressType(IntEnum):
    None_ = 0
    Upgrade = 1
    Manage = 2

class TileState(IntEnum):
    None_ = 0
    PartiallyConquested = 1
    FullyConquested = 2

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
    Browser = 39
    Webview = 40
    Survey = 41
    Browser_Arg = 42
    Webview_Arg = 43

class OpenCondition(IntEnum):
    Hide = 0
    Lock = 1
    Open = 2

class ResetContentType(IntEnum):
    None_ = 0
    HardStagePlay = 1
    StarategyMapHeal = 2
    ShopRefresh = 3
    ArenaDefenseVictoryReward = 4
    WeeklyMasterCoin = 5
    WorldRaidGemEnterCount = 6
    ConquestDailyErosionCheck = 7
    MiniEventToken = 8

class WeekDungeonType(IntEnum):
    None_ = 0
    ChaserA = 1
    ChaserB = 2
    ChaserC = 3
    FindGift = 4
    Blood = 5

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

class ContentLockType(IntEnum):
    None_ = 0
    NotUseControlledByOtherSetting = 1
    Academy = 2
    MultiFloorRaid = 3
    EventContent = 4
    EventNotice = 5
    GuideMission = 6
    Campaign = 7
    Story = 8
    WeekDungeon_Chase = 9
    WeekDungeon = 10
    SchoolDungeon = 11
    Raid = 12
    EliminateRaid = 13
    TimeAttackDungeon = 14
    Arena = 15
    Cafe = 16
    GemShop = 17
    Gacha = 18
    Craft = 19
    MomoTalk = 20

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

class ContentResultType(IntEnum):
    Failure = 0
    Success = 1

class EventContentItemType(IntEnum):
    EventPoint = 0
    EventToken1 = 1
    EventToken2 = 2
    EventToken3 = 3
    EventToken4 = 4
    EventToken5 = 5
    EventMeetUpTicket = 6
    EventEtcItem = 7

class RaidSeasonType(IntEnum):
    None_ = 0
    Open = 1
    Close = 2
    Settlement = 3

class BuffConditionType(IntEnum):
    All = 0
    Character = 1
    School = 2
    Weapon = 3

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

class JudgeGrade(IntEnum):
    None_ = 0
    Miss = 1
    Attack = 2
    Critical = 3

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

class ContentsChangeType(IntEnum):
    None_ = 0
    WorldRaidBossDamageRatio = 1
    WorldRaidBossGroupDate = 2

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

class RankingSearchType(IntEnum):
    None_ = 0
    Rank = 1
    Score = 2

class EventContentReleaseType(IntEnum):
    None_ = 0
    Permanent = 1
    MainStory = 2
    PermanentSpecialOperate = 3
    PermanentConquest = 4

class CraftSlotIndex(IntEnum):
    Slot00 = 0
    Slot01 = 1
    Slot02 = 2
    Max = 3

class CraftNodeTier(IntEnum):
    Base = 0
    Node01 = 1
    Node02 = 2
    Node03 = 3
    Max = 4

class SubEventType(IntEnum):
    None_ = 0
    SubEvent = 1
    SubEventPermanent = 2

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

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1

class Language(IntEnum):
    Kr = 0
    Jp = 1
    Th = 2
    Tw = 3
    En = 4

class SoundType(IntEnum):
    UI = 0
    BGM = 1
    FX = 2

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

class EchelonExtensionType(IntEnum):
    Base = 0
    Extension = 1

class NoticeType(IntEnum):
    None_ = 0
    Notice = 1
    Event = 2

class RewardTag(IntEnum):
    Default = 0
    FirstClear = 1
    StrategyObject = 2
    Event = 3
    ThreeStar = 4
    ProductMonthly = 5
    Rare = 6
    EventBonus = 7
    TimeWeight = 8
    ProductWeekly = 9
    ProductBiweekly = 10
    EventPermanentReward = 11
    ConquestManageEvent = 12
    ConquestManageDefault = 13
    ConquestCalculateDefault = 14
    ConquestCalculateLevel2 = 15
    ConquestCalculateLevel3 = 16
    ConquestFootholdUpgrade2 = 17
    ConquestFootholdUpgrade3 = 18
    ConquestErosionPenalty = 19
    GemBonus = 20
    GemPaid = 21
    ConquestTileConquer = 22

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

class RaidStatus(IntEnum):
    None_ = 0
    Playing = 1
    Clear = 2
    Close = 3

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

class EventChangeType(IntEnum):
    MainSub = 0
    SubMain = 1

class CafeCharacterState(IntEnum):
    None_ = 0
    Idle = 1
    Walk = 2
    Reaction = 3
    Interaction = 4
    Max = 5

class FurnitureFunctionType(IntEnum):
    None_ = 0
    EventCollection = 1
    VideoPlay = 2
    TrophyCollection = 3
    InteractionBGMPlay = 4

class NotificationEventReddot(IntEnum):
    StagePointReward = 0
    MissionComplete = 1
    MiniGameMissionComplete = 2
    WorldRaidReward = 3
    ConquestCalculateReward = 4
    DiceRaceLapReward = 5

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

class FilterCategory(IntEnum):
    Character = 0
    Equipment = 1
    Item = 2
    Craft = 3
    ShiftCraft = 4
    Shop = 5
    MemoryLobby = 6
    Trophy = 7
    Emblem = 8

class FilterIcon(IntEnum):
    TextOnly = 0
    TextWithIcon = 1
    Pin = 2
    Role = 3
    CharacterStar = 4
    WeaponStar = 5
    Attack = 6
    Defense = 7
    Range = 8
    MemoryLobby = 9
    Obscuration = 10

class CVUnlockScenarioType(IntEnum):
    Main = 0
    Event = 1
    SpecialOperation = 2

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

class FriendSearchLevelOption(IntEnum):
    Recommend = 0
    All = 1
    Level1To30 = 2
    Level31To40 = 3
    Level41To50 = 4
    Level51To60 = 5
    Level61To70 = 6
    Level71To80 = 7
    Level81To90 = 8
    Level91To100 = 9

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

class TBGTileType(IntEnum):
    None_ = 0
    Start = 1
    Movable = 2
    UnMovable = 3

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
    Reset_EquipmentAtSpecificTierUpCount = 25
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

class AccountAchievementType(IntEnum):
    TotalLoginCount = 0
    TotalGetClearStarCount = 1
    TotalCharacterLevelUpCount = 2
    TotalCharacterSkillLevelUpCount = 3
    TotalClearCampaignStageCount = 4
    TotalClearChaserDungeonCount = 5
    TotalClearFindGiftAndBloodDungeonCount = 6
    TotalEquipmentLevelUpCount = 7
    TotalEquipmentTierUpCount = 8
    MaxComfortPoint = 9
    TotalGetGold = 10
    TotalUseGold = 11
    TotalJoinArenaCount = 12
    TotalJoinRaidCount = 13
    TotalClearSchoolDungeonCount = 14
    TotalGetWeaponCount = 15
    TotalWeaponLevelUpCount = 16
    TotalWeaponTranscendenceCount = 17
    KillEnemyWithDecagrammatonSPOTagCount = 18
    EventPoint = 19
    ConquestCalculateReward = 20
    TotalJoinEliminateRaidCount = 21
    Cafe2MaxComfortPoint = 22
    TotalRaidTicketUseCount = 23
    TotalEliminateTicketUseCount = 24
    TotalCharacterPotentialUpCount = 25

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

class Rarity(IntEnum):
    N = 0
    R = 1
    SR = 2
    SSR = 3

class Tier(IntEnum):
    T1 = 0
    T2 = 1
    T3 = 2
    T4 = 3

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
    Max = 28

class SortingTarget(IntEnum):
    None_ = 0
    Rarity = 1
    Level = 2
    StarGrade = 3
    Tier = 4

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

class ParcelChangeReason(IntEnum):
    None_ = 0
    Acquire_NewAccount = 1
    Acquire_PlayReward = 2
    Acquire_ChapterReward = 3
    Acquire_LoginReward = 4
    Acquire_EventReward = 5
    Acquire_GMPush = 6
    Acquire_ShopBuy = 7
    Acquire_GachaBuy = 8
    Acquire_CurrencyBuy = 9
    Equipment_Equip = 10
    Equipment_Unequip = 11
    Equipment_Levelup = 12
    Equipment_LimitBreak = 13
    Equipment_Transcendence = 14
    Equipment_Enchant = 15
    Item_Use = 16
    Item_Lock = 17
    Item_CharacterGrowthMaterial = 18
    Item_Change = 19
    Item_Delete = 20
    Item_Consume = 21
    Item_SelectTicket = 22
    Character_ExpGrowth = 23
    Character_Transcendence = 24
    Character_SkillLevelUp = 25
    Character_FavorGrowth = 26
    Furniture_CafeSet = 27
    Furniture_CafeRecall = 28
    Academy_AttendSchedule = 29
    Academy_MessageList = 30
    Adventure_EnterMainStage = 31
    Adventure_EnterSubStage = 32
    Adventure_MainStageBattleResult = 33
    Adventure_SubStageBattleResult = 34
    Adventure_ChapterClearReward = 35
    Adventure_Retreat = 36
    Adventure_PurchasePlayCountHardStage = 37
    Adventure_TutorialStage = 38
    Adventure_TutorialStageBattleResult = 39
    ContentSweep_Sweep = 40
    Arena_TimeReward = 41
    Arena_DailyReward = 42
    Arena_EnterBattle = 43
    Arena_BattleResult = 44
    Cafe_Interact = 45
    Cafe_Production = 46
    Cafe_RankUp = 47
    Cafe_GiveGift = 48
    WeekDungeon_BattleResult = 49
    WeekDungeon_EnterBattle = 50
    WeekDungeon_Retreat = 51
    Mission_Clear = 52
    Shop_Refresh = 53
    Shop_BuyEligma = 54
    Shop_BuyMerchandise = 55
    Shop_BuyGacha = 56
    Scenario_Clear = 57
    Recipe_Craft = 58
    Raid_Failed = 59
    Raid_Reward = 60
    Raid_SeasonReward = 61
    Raid_CreateBattle = 62
    CumulativeTimeReward_Reward = 63
    Mail_Receive = 64
    MomoTalk_FavorSchedule = 65
    WeekDungeon_EnterBlood = 66
    WeekDungeon_EnterGift = 67
    Acquire_ActionPoint = 68
    Acquire_ArenaTicket = 69
    EventContent_TotalReward = 70
    Craft_UpdateNode = 71
    Craft_CompleteProcess = 72
    Craft_Reward = 73
    EventContent_BattleResult = 74
    Adventure_Sweep = 75
    EventContent_Sweep = 76
    WeekDungeon_Sweep = 77
    Acquire_MonthlyProduct = 78
    Acquire_DailyReward = 79
    Billing_PurchaseProduct = 80
    EventContent_EnterMainStage = 81
    EventContent_EnterSubStage = 82
    EventContent_MainStageResult = 83
    EventContent_SubStageResult = 84
    EventContent_Retreat = 85
    WeekDungeon_BloodResult = 86
    WeekDungeon_GiftResult = 87
    WeekDungeon_EnterChaserA = 88
    WeekDungeon_EnterChaserB = 89
    WeekDungeon_EnterChaserC = 90
    WeekDungeon_ChaserAResult = 91
    WeekDungeon_ChaserBResult = 92
    WeekDungeon_ChaserCResult = 93
    EventContent_BoxGacha = 94
    Raid_Sweep = 95
    Clan_AssistReward = 96
    EventContent_CardShop = 97
    CharacterWeapon_ExpGrowth = 98
    CharacterWeapon_Transcendence = 99
    MiniGameMission_Clear = 100
    SchoolDungeon_EnterSchoolA = 101
    SchoolDungeon_EnterSchoolB = 102
    SchoolDungeon_EnterSchoolC = 103
    SchoolDungeon_SchoolAResult = 104
    SchoolDungeon_SchoolBResult = 105
    SchoolDungeon_SchoolCResult = 106
    TimeAttackDungeon_CreateBattle = 107
    TimeAttackDungeon_EndBattle = 108
    TimeAttackDungeon_Reward = 109
    Clan_Create = 110
    Arena_SeasonReward = 111
    Arena_OverallReward = 112
    EventContent_AttendSchedule = 113
    EventContent_BuyFortuneGacha = 114
    Equipment_BatchGrowth = 115
    EventContent_EnterStoryStage = 116
    EventContent_StoryStageResult = 117
    WorldRaid_EndBattle = 118
    WorldRaid_Reward = 119
    Conquest_EnterBattle = 120
    Conquest_EnterUnExpectBattle = 121
    Conquest_BattleResult = 122
    Conquest_UnExpectBattleResult = 123
    Conquest_UpgradeBase = 124
    Conquest_ManageBase = 125
    Conquest_CalculatedReward = 126
    Conquest_TakeEventBoxObject = 127
    Conquest_ConquerNormalTile = 128
    Item_SelectRecruit = 129
    Adventure_EnterExtraStage = 130
    Adventure_ExtraStageBattleResult = 131
    Scenario_EnterMainStage = 132
    Scenario_MainStageResult = 133
    Scenario_RetreatMainStage = 134
    EventContent_DiceRaceRollReward = 135
    EventContent_DiceRaceLapReward = 136
    ShiftingCraft_BeginProcess = 137
    ShiftingCraft_CompleteProcess = 138
    ShiftingCraft_Reward = 139
    MiniGame_ShootingBattleResult = 140
    MiniGame_ShootingSweep = 141
    EliminateRaid_Failed = 142
    EliminateRaid_Reward = 143
    EliminateRaid_SeasonReward = 144
    EliminateRaid_CreateBattle = 145
    EliminateRaid_Sweep = 146
    Item_AutoSynth = 147
    ContentSweep_MultiSweep = 148
    Emblem_Acquire = 149
    MiniGame_TBGMove = 150
    MiniGame_TBGEncounterInput = 151
    MiniGame_TBGResurrect = 152
    MiniGame_TBGSweep = 153
    Shop_BeforehandGacha = 154
    EliminateRaid_LimitedReward = 155
    Craft_AutoBeginProcess = 156
    Craft_CompleteProcessAll = 157
    Craft_RewardAll = 158
    ShiftingCraft_CompleteProcessAll = 159
    ShiftingCraft_RewardAll = 160
    Temp_1 = 161
    Temp_2 = 162
    Temp_3 = 163
    Temp_4 = 164
    EventContent_Treasure = 165
    Field_EnterStage = 166
    Field_StageResult = 167
    Field_Interaction = 168
    Field_Quest = 169
    Character_PotentialGrowth = 170
    MultiFloorRaid_EndBattle = 171
    MultiFloorRaid_Reward = 172
    MiniGame_DreamSchedule = 173
    MiniGame_DreamDailyClosing = 174
    MiniGame_DreamEnding = 175
    Item_ExpireChange = 176
    MiniGame_DefenseBattleResult = 177
    Raid_FailCompensateReward = 178
    EliminateRaid_FailCompensateReward = 179
    Currency_ExpireChange = 180
    Conquest_ErosionBattleResult = 181
    Conquest_EnterErosionBattle = 182

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

class ScenarioType(IntEnum):
    None_ = 0
    Title = 1
    Place = 2

class ScenarioTypes(IntEnum):
    None_ = 0
    Title = 1
    Place = 2

class ScenarioCharacterAction(IntEnum):
    Idle = 0
    Shake = 1
    Greeting = 2
    FalldownLeft = 3
    FalldownRight = 4
    Stiff = 5
    Hophop = 6
    Jump = 7

class ScenarioCharacterBehaviors(IntEnum):
    None_ = 0
    Appear = 1
    Disappear = 2
    AppearToLeft = 3
    ApperToRight = 4
    DisappearToLeft = 5
    DisappearToRight = 6
    MoveToTarget = 7

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

class DialogConditionDetail(IntEnum):
    None_ = 0
    Day = 1
    Close = 2
    MiniGameDreamMakerDay = 3

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

class EtcSchool(IntEnum):
    None_ = 0
    ETC = 1
    Tokiwadai = 2
    Sakugawa = 3
    Max = 4

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

class ScenarioEffectDepth(IntEnum):
    None_ = 0
    AboveBg = 1
    AboveCharacter = 2
    AboveAll = 3

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

class ShopCategoryType(IntEnum):
    General = 0
    SecretStone = 1
    Raid = 2
    Gold = 3
    Ap = 4
    PickupGacha = 5
    NormalGacha = 6
    PointGacha = 7
    EventGacha = 8
    ArenaTicket = 9
    Arena = 10
    TutoGacha = 11
    RecruitSellection = 12
    EventContent_0 = 13
    EventContent_1 = 14
    EventContent_2 = 15
    EventContent_3 = 16
    EventContent_4 = 17
    _Obsolete = 18
    LimitedGacha = 19
    MasterCoin = 20
    SecretStoneGrowth = 21
    TicketGacha = 22
    DirectPayGacha = 23
    FesGacha = 24
    TimeAttack = 25
    Chaser = 26
    ChaserTicket = 27
    SchoolDungeonTicket = 28
    AcademyTicket = 29
    Special = 30
    Care = 31
    BeforehandGacha = 32
    EliminateRaid = 33
    GlobalSpecialGacha = 34

class PurchaseServerTag(IntEnum):
    Audit = 0
    PreAudit = 1
    Production = 2
    Hotfix = 3
    Standby2 = 4
    Standby1 = 5
    Major = 6
    Minor = 7
    Temp = 8
    Test = 9
    TestIn = 10

class PurchaseStatusCode(IntEnum):
    None_ = 0
    Start = 1
    PublishSuccess = 2
    End = 3
    Error = 4
    DuplicateOrder = 5
    Refund = 6

class StoreType(IntEnum):
    None_ = 0
    GooglePlay = 1
    AppStore = 2
    Harmony = 3
    OneStore = 4
    MicrosoftStore = 5
    GalaxyStore = 6

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

class ProductCategory(IntEnum):
    None_ = 0
    Gem = 1
    Monthly = 2
    Package = 3
    GachaDirect = 4
    TimeLimit = 5

class ProductDisplayTag(IntEnum):
    None_ = 0
    New = 1
    Hot = 2
    Sale = 3
    Limited = 4

class ProductTagType(IntEnum):
    Monthly = 0
    Weekly = 1
    Biweekly = 2
    BundleMonthly = 3

class BillingTransactionEndType(IntEnum):
    None_ = 0
    Success = 1
    Cancel = 2

class GachaRewardType(IntEnum):
    None_ = 0
    Eligma = 1
    Eleph = 2

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
    SRT = 24
    Event = 25
    ChaserTotalTicket = 26
    SchoolTotalTicket = 27
    ShopFilterDUMMY_1 = 28
    ShopFilterDUMMY_2 = 29
    ShopFilterDUMMY_3 = 30
    ShopFilterDUMMY_4 = 31
    ShopFilterDUMMY_5 = 32
    ShopFilterDUMMY_6 = 33
    ShopFilterDUMMY_7 = 34
    ETC = 35
    Bundle = 36

class SocialMode(IntEnum):
    TITLE = 0
    LOBBY = 1
    FORMATION = 2
    STAGE_SELECT = 3
    BATTLE = 4
    POPUP = 5
    BATTLE_RESULT = 6
    BATTLE_RESULT_VICTORY = 7
    BATTLE_RESULT_DEFEAT = 8
    INVALID = 9
    TACTIC = 10
    STRATEGY = 11
    ACCONT = 12
    CAMPAIGN_STORY = 13
    CAMPAIGN_STAGE = 14
    TACTICREADY = 15

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
    TagName0701 = 703
    TagName0702 = 704
    TagName0703 = 705
    TagName0704 = 706
    TagName0705 = 707
    TagName0706 = 708
    TagName0707 = 709
    TagName0708 = 710
    TagName0709 = 711
    TagName0710 = 712
    TagName0711 = 713
    TagName0712 = 714
    TagName0713 = 715
    TagName0714 = 716
    TagName0715 = 717
    TagName0716 = 718
    TagName0717 = 719
    TagName0718 = 720
    TagName0719 = 721
    TagName0720 = 722
    TagName0721 = 723
    TagName0722 = 724
    TagName0723 = 725
    TagName0724 = 726
    TagName0725 = 727
    TagName0726 = 728
    TagName0727 = 729
    TagName0728 = 730
    TagName0729 = 731
    TagName0730 = 732
    TagName0731 = 733
    TagName0732 = 734
    TagName0733 = 735
    TagName0734 = 736
    TagName0735 = 737
    TagName0736 = 738
    TagName0737 = 739
    TagName0738 = 740
    TagName0739 = 741
    TagName0740 = 742
    TagName0741 = 743
    TagName0742 = 744
    TagName0743 = 745
    TagName0744 = 746
    TagName0745 = 747
    TagName0746 = 748
    TagName0747 = 749
    TagName0748 = 750
    TagName0749 = 751
    TagName0750 = 752
    TagName0751 = 753
    TagName0752 = 754
    TagName0753 = 755
    TagName0754 = 756
    TagName0755 = 757
    TagName0756 = 758
    TagName0757 = 759
    TagName0758 = 760
    TagName0759 = 761
    TagName0760 = 762
    TagName0761 = 763
    TagName0762 = 764
    TagName0763 = 765
    TagName0764 = 766
    TagName0765 = 767
    TagName0766 = 768
    TagName0767 = 769
    TagName0768 = 770
    TagName0769 = 771
    TagName0770 = 772
    TagName0771 = 773
    TagName0772 = 774
    TagName0773 = 775
    TagName0774 = 776
    TagName0775 = 777
    TagName0776 = 778
    TagName0777 = 779
    TagName0778 = 780
    TagName0779 = 781
    TagName0780 = 782
    TagName0781 = 783
    TagName0782 = 784
    TagName0783 = 785
    TagName0784 = 786
    TagName0785 = 787
    TagName0786 = 788
    TagName0787 = 789
    TagName0788 = 790
    TagName0789 = 791
    TagName0790 = 792
    TagName0791 = 793
    TagName0792 = 794
    TagName0793 = 795
    TagName0794 = 796
    TagName0795 = 797
    TagName0796 = 798
    TagName0797 = 799
    TagName0798 = 800
    TagName0799 = 801
    TagName0800 = 802
    TagName0801 = 803
    TagName0802 = 804
    TagName0803 = 805
    TagName0804 = 806
    TagName0805 = 807
    TagName0806 = 808
    TagName0807 = 809
    TagName0808 = 810
    TagName0809 = 811
    TagName0810 = 812
    TagName0811 = 813
    TagName0812 = 814
    TagName0813 = 815
    TagName0814 = 816
    TagName0815 = 817
    TagName0816 = 818
    TagName0817 = 819
    TagName0818 = 820
    TagName0819 = 821
    TagName0820 = 822
    TagName0821 = 823
    TagName0822 = 824
    TagName0823 = 825
    TagName0824 = 826
    TagName0825 = 827
    TagName0826 = 828
    TagName0827 = 829
    TagName0828 = 830
    TagName0829 = 831
    TagName0830 = 832
    TagName0831 = 833
    TagName0832 = 834
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

class UnderCoverItemCategory(IntEnum):
    Consumable = 0
    Interaction = 1
    Skill = 2
    Collection = 3

class CharacterLogType(IntEnum):
    Targeting = 0
    Pathfinding = 1
    Debug = 2

class DrawType(IntEnum):
    Debug = 0
    Gizmo = 1

class NotifyCollectionChangedAction(IntEnum):
    Add = 0
    Remove = 1
    Replace = 2
    Move = 3
    Reset = 4

class MediaType(IntEnum):
    none = 0
    ogg = 1
    mp4 = 2
    jpg = 3
    png = 4
    acb = 5
    awb = 6

class MediaManifestCollumnType(IntEnum):
    key = 0
    hash = 1
    mediaType = 2
    size = 3

class FocusingType(IntEnum):
    Distance = 0
    Object = 1
    Owner = 2

class TimelineEntityIndex(IntEnum):
    MainFirst = 0
    MainSecond = 1
    MainThird = 2
    MainFourth = 3
    SupportFirst = 4
    SupportSecond = 5
    MainFifth = 6
    MainSixth = 7
    SupportThird = 8
    SupportFourth = 9

class TimelineType(IntEnum):
    Default = 0
    Victory = 1

class FinishType(IntEnum):
    Return = 0
    ReturnAndDisable = 1
    ReturnAndDestroy = 2
    Hold = 3
    ManualDestroy = 4

class ProcessedErrorAction(IntEnum):
    None_ = 0
    WebAPIError = 1
    CustomError = 2
    DefaultError = 3

class GameObjectLifecycle(IntEnum):
    None_ = 0
    Game = 1
    Scene = 2

class SessionState(IntEnum):
    NONE = 0
    WAITING_SERVER_RESPONSE = 1
    RECEIVED_SERVER_RESPONSE = 2
    FILE_NOT_FOUND = 3
    FAILED = 4
    SUCCESS = 5
    CLIENT_NETWORK_NOT_REACHABLE = 6
    SERVER_RESPONSE_ERROR = 7
    SERVER_NOT_RESPONSE = 8

class HttpMethodType(IntEnum):
    GET = 0
    POST = 1

class IrcState(IntEnum):
    None_ = 0
    Initialized = 1
    Connected = 2
    ConnectFailed = 3
    Disconnected = 4
    Registered = 5
    Kicked = 6

class IrcUserMode(IntEnum):
    Away = 0
    Invisible = 1
    Wallops = 2
    Restricted = 3
    Operator = 4
    LocalOperator = 5
    Notices = 6

class ReplyCode(IntEnum):
    NONE = 0
    RPL_NONE = 1
    RPL_WELCOME = 2
    RPL_YOURHOST = 3
    RPL_CREATED = 4
    RPL_MYINFO = 5
    RPL_MAP = 6
    RPL_ENDOFMAP = 7
    RPL_MOTDSTART = 8
    RPL_MOTD = 9
    RPL_MOTDALT = 10
    RPL_MOTDALT2 = 11
    RPL_MOTDEND = 12
    RPL_UMODEIS = 13
    RPL_USERHOST = 14
    RPL_ISON = 15
    RPL_AWAY = 16
    RPL_UNAWAY = 17
    RPL_NOWAWAY = 18
    RPL_WHOISHELPER = 19
    RPL_WHOISUSER = 20
    RPL_WHOISSERVER = 21
    RPL_WHOISOPERATOR = 22
    RPL_WHOISIDLE = 23
    RPL_ENDOFWHOIS = 24
    RPL_WHOISCHANNEL = 25
    RPL_WHOWASUSER = 26
    RPL_ENDOFWHOWAS = 27
    RPL_WHOREPLY = 28
    RPL_ENDOFWHO = 29
    RPL_USERIPS = 30
    RPL_USERIP = 31
    RPL_LISTSTART = 32
    RPL_LIST = 33
    RPL_LISTEND = 34
    RPL_LINKS = 35
    RPL_ENDOFLINKS = 36
    RPL_UNIQOPIS = 37
    RPL_CHANNELMODEIS = 38
    RPL_CHANNELURL = 39
    RPL_CHANNELCREATED = 40
    RPL_NOTOPIC = 41
    RPL_TOPIC = 42
    RPL_TOPICSETBY = 43
    RPL_NAMEREPLY = 44
    RPL_ENDOFNAMES = 45
    RPL_INVITING = 46
    RPL_SUMMONING = 47
    RPL_INVITELIST = 48
    RPL_ENDOFINVITELIST = 49
    RPL_EXCEPTLIST = 50
    RPL_ENDOFEXCEPTLIST = 51
    RPL_BANLIST = 52
    RPL_ENDOFBANLIST = 53
    RPL_VERSION = 54
    RPL_INFO = 55
    RPL_ENDOFINFO = 56
    RPL_YOUREOPER = 57
    RPL_REHASHING = 58
    RPL_YOURESERVICE = 59
    RPL_TIME = 60
    RPL_USERSSTART = 61
    RPL_USERS = 62
    RPL_ENDOFUSERS = 63
    RPL_NOUSERS = 64
    RPL_SERVLIST = 65
    RPL_SERVLISTEND = 66
    RPL_ADMINME = 67
    RPL_ADMINLOC1 = 68
    RPL_ADMINLOC2 = 69
    RPL_ADMINEMAIL = 70
    RPL_TRYAGAIN = 71
    RPL_TRACELINK = 72
    RPL_TRACECONNECTING = 73
    RPL_TRACEHANDSHAKE = 74
    RPL_TRACEUNKNOWN = 75
    RPL_TRACEOPERATOR = 76
    RPL_TRACEUSER = 77
    RPL_TRACESERVER = 78
    RPL_TRACESERVICE = 79
    RPL_TRACENEWTYPE = 80
    RPL_TRACECLASS = 81
    RPL_TRACERECONNECT = 82
    RPL_TRACELOG = 83
    RPL_TRACEEND = 84
    RPL_STATSLINKINFO = 85
    RPL_STATSCOMMANDS = 86
    RPL_STATSCLINE = 87
    RPL_STATSNLINE = 88
    RPL_STATSILINE = 89
    RPL_STATSKLINE = 90
    RplStatsPLine = 91
    RplStatsQLine = 92
    RplStatsELine = 93
    RplStatsDLine = 94
    RplStatsLLine = 95
    RplStatsuLine = 96
    RplStatsoLine = 97
    RplStatsHLine = 98
    RplStatsGLine = 99
    RplStatsULine = 100
    RplStatsZLine = 101
    RplStatsYLine = 102
    RPL_ENDOFSTATS = 103
    RPL_STATSUPTIME = 104
    RPL_STATSPING = 105
    RPL_STATSDLINE = 106
    RplGLineList = 107
    RplEndOfGLineList = 108
    RplSilenceList = 109
    RplEndOfSilenceList = 110
    RPL_LUSERCLIENT = 111
    RPL_LUSEROP = 112
    RPL_LUSERUNKNOWN = 113
    RPL_LUSERCHANNELS = 114
    RPL_LUSERME = 115
    RplLUserLocalUser = 116
    RplLUserGlobalUser = 117
    ERR_NOSUCHNICK = 118
    ERR_NOSUCHSERVER = 119
    ERR_NOSUCHCHANNEL = 120
    ERR_CANNOTSENDTOCHAN = 121
    ERR_TOOMANYCHANNELS = 122
    ERR_WASNOSUCHNICK = 123
    ERR_TOOMANYTARGETS = 124
    ERR_NOSUCHSERVICE = 125
    ERR_NOORIGIN = 126
    ERR_NORECIPIENT = 127
    ERR_NOTEXTTOSEND = 128
    ERR_NOTOPLEVEL = 129
    ERR_WILDTOPLEVEL = 130
    ERR_BADMASK = 131
    ErrTooMuchInfo = 132
    ERR_UNKNOWNCOMMAND = 133
    ERR_NOMOTD = 134
    ERR_NOADMININFO = 135
    ERR_FILEERROR = 136
    ERR_NONICKNAMEGIVEN = 137
    ERR_ERRONEUSNICKNAME = 138
    ERR_NICKNAMEINUSE = 139
    ERR_NICKCOLLISION = 140
    ERR_UNAVAILRESOURCE = 141
    ErrNickTooFast = 142
    ErrTargetTooFast = 143
    ERR_USERNOTINCHANNEL = 144
    ERR_NOTONCHANNEL = 145
    ERR_USERONCHANNEL = 146
    ERR_NOLOGIN = 147
    ERR_SUMMONDISABLED = 148
    ERR_USERSDISABLED = 149
    ERR_NOTREGISTERED = 150
    ERR_NEEDMOREPARAMS = 151
    ERR_ALREADYREGISTRED = 152
    ERR_NOPERMFORHOST = 153
    ERR_PASSWDMISMATCH = 154
    ERR_YOUREBANNEDCREEP = 155
    ERR_YOUWILLBEBANNED = 156
    ERR_KEYSET = 157
    ErrServerCanChange = 158
    ERR_CHANNELISFULL = 159
    ERR_UNKNOWNMODE = 160
    ERR_INVITEONLYCHAN = 161
    ERR_BANNEDFROMCHAN = 162
    ERR_BADCHANNELKEY = 163
    ERR_BADCHANMASK = 164
    ERR_NOCHANMODES = 165
    ERR_BANLISTFULL = 166
    ERR_NOPRIVILEGES = 167
    ERR_CHANOPRIVSNEEDED = 168
    ERR_CANTKILLSERVER = 169
    ERR_RESTRICTED = 170
    ERR_UNIQOPPRIVSNEEDED = 171
    ERR_NOOPERHOST = 172
    ERR_UMODEUNKNOWNFLAG = 173
    ERR_USERSDONTMATCH = 174
    ErrSilenceListFull = 175

class TBGPreBattleOption(IntEnum):
    Attack = 0
    RunAway = 1

class TBGPostBattleOption(IntEnum):
    Retry = 0
    Retreat = 1

class TBGBattleEncounterStage(IntEnum):
    None_ = 0
    BeforeStoryOption = 1
    PreBattlePhase = 2
    InBattlePhase = 3
    PostBattlePhase = 4
    ExitRunAway = 5
    ExitBattleVictory = 6
    EncounterRewardOption = 7
    ExitBattleRetreat = 8

class TBGEncounterState(IntEnum):
    None_ = 0
    Active = 1
    Disposing = 2

class TBGFacilityEncounterStage(IntEnum):
    None_ = 0
    EncounterOption = 1
    EncounterRewardOption = 2
    Exit = 3

class TBGHexaObjectSpawnRule(IntEnum):
    Nothing = 0
    ObjectId = 1
    ObjectType = 2

class TBGObjectInteractionType(IntEnum):
    None_ = 0
    Encounter = 1
    Portal = 2

class TBGRandomEncounterStage(IntEnum):
    None_ = 0
    BeforeStoryOption = 1
    EncounterOption = 2
    EncounterRewardOption = 3
    Exit = 4

class TBGTreasureEncounterStage(IntEnum):
    None_ = 0
    PreReceiveReward = 1
    PostReceiveReward = 2
    ExitTreasureFake = 3
    ExitToClearThema = 4
    ExitToContinue = 5

class TBGDiceRollResult(IntEnum):
    Failure = 0
    Success = 1
    CriticalSuccess = 2

class Protocol(IntEnum):
    Common_Cheat = 0
    Error = 1
    None_ = 2
    System_Version = 3
    Session_Info = 4
    NetworkTime_Sync = 5
    NetworkTime_SyncReply = 6
    Audit_GachaStatistics = 7
    Account_Create = 8
    Account_Nickname = 9
    Account_Auth = 10
    Account_CurrencySync = 11
    Account_SetRepresentCharacterAndComment = 12
    Account_GetTutorial = 13
    Account_SetTutorial = 14
    Account_PassCheck = 15
    Account_VerifyForYostar = 16
    Account_CheckYostar = 17
    Account_CallName = 18
    Account_BirthDay = 19
    Account_Auth2 = 20
    Account_LinkReward = 21
    Account_ReportXignCodeCheater = 22
    Account_DismissRepurchasablePopup = 23
    Account_InvalidateToken = 24
    Account_LoginSync = 25
    Account_Reset = 26
    Account_RequestBirthdayMail = 27
    Character_List = 28
    Character_Transcendence = 29
    Character_ExpGrowth = 30
    Character_FavorGrowth = 31
    Character_UpdateSkillLevel = 32
    Character_UnlockWeapon = 33
    Character_WeaponExpGrowth = 34
    Character_WeaponTranscendence = 35
    Character_SetFavorites = 36
    Character_SetCostume = 37
    Character_BatchSkillLevelUpdate = 38
    Character_PotentialGrowth = 39
    Equipment_List = 40
    Equipment_Sell = 41
    Equipment_Equip = 42
    Equipment_LevelUp = 43
    Equipment_TierUp = 44
    Equipment_Lock = 45
    Equipment_BatchGrowth = 46
    Item_List = 47
    Item_Sell = 48
    Item_Consume = 49
    Item_Lock = 50
    Item_BulkConsume = 51
    Item_SelectTicket = 52
    Item_AutoSynth = 53
    Echelon_List = 54
    Echelon_Save = 55
    Echelon_PresetList = 56
    Echelon_PresetSave = 57
    Echelon_PresetGroupRename = 58
    Campaign_List = 59
    Campaign_EnterMainStage = 60
    Campaign_ConfirmMainStage = 61
    Campaign_DeployEchelon = 62
    Campaign_WithdrawEchelon = 63
    Campaign_MapMove = 64
    Campaign_EndTurn = 65
    Campaign_EnterTactic = 66
    Campaign_TacticResult = 67
    Campaign_Retreat = 68
    Campaign_ChapterClearReward = 69
    Campaign_Heal = 70
    Campaign_EnterSubStage = 71
    Campaign_SubStageResult = 72
    Campaign_Portal = 73
    Campaign_ConfirmTutorialStage = 74
    Campaign_PurchasePlayCountHardStage = 75
    Campaign_EnterTutorialStage = 76
    Campaign_TutorialStageResult = 77
    Campaign_RestartMainStage = 78
    Campaign_EnterMainStageStrategySkip = 79
    Campaign_MainStageStrategySkipResult = 80
    Mail_List = 81
    Mail_Check = 82
    Mail_Receive = 83
    Mission_List = 84
    Mission_Reward = 85
    Mission_MultipleReward = 86
    Mission_GuideReward = 87
    Mission_MultipleGuideReward = 88
    Mission_Sync = 89
    Mission_GuideMissionSeasonList = 90
    Attendance_List = 91
    Attendance_Check = 92
    Attendance_Reward = 93
    Shop_BuyMerchandise = 94
    Shop_BuyGacha = 95
    Shop_List = 96
    Shop_Refresh = 97
    Shop_BuyEligma = 98
    Shop_BuyGacha2 = 99
    Shop_GachaRecruitList = 100
    Shop_BuyRefreshMerchandise = 101
    Shop_BuyGacha3 = 102
    Shop_BuyAP = 103
    Shop_BeforehandGachaGet = 104
    Shop_BeforehandGachaRun = 105
    Shop_BeforehandGachaSave = 106
    Shop_BeforehandGachaPick = 107
    Recipe_Craft = 108
    MemoryLobby_List = 109
    MemoryLobby_SetMain = 110
    MemoryLobby_UpdateLobbyMode = 111
    MemoryLobby_Interact = 112
    CumulativeTimeReward_List = 113
    CumulativeTimeReward_Reward = 114
    OpenCondition_List = 115
    OpenCondition_Set = 116
    OpenCondition_EventList = 117
    Toast_List = 118
    Raid_List = 119
    Raid_CompleteList = 120
    Raid_Detail = 121
    Raid_Search = 122
    Raid_CreateBattle = 123
    Raid_EnterBattle = 124
    Raid_BattleUpdate = 125
    Raid_EndBattle = 126
    Raid_Reward = 127
    Raid_RewardAll = 128
    Raid_Revive = 129
    Raid_Share = 130
    Raid_SeasonInfo = 131
    Raid_SeasonReward = 132
    Raid_Lobby = 133
    Raid_GiveUp = 134
    Raid_OpponentList = 135
    Raid_RankingReward = 136
    Raid_Login = 137
    Raid_Sweep = 138
    Raid_GetBestTeam = 139
    SkipHistory_List = 140
    SkipHistory_Save = 141
    Scenario_List = 142
    Scenario_Clear = 143
    Scenario_GroupHistoryUpdate = 144
    Scenario_Skip = 145
    Scenario_Select = 146
    Scenario_AccountStudentChange = 147
    Scenario_LobbyStudentChange = 148
    Scenario_SpecialLobbyChange = 149
    Scenario_Enter = 150
    Scenario_EnterMainStage = 151
    Scenario_ConfirmMainStage = 152
    Scenario_DeployEchelon = 153
    Scenario_WithdrawEchelon = 154
    Scenario_MapMove = 155
    Scenario_EndTurn = 156
    Scenario_EnterTactic = 157
    Scenario_TacticResult = 158
    Scenario_Retreat = 159
    Scenario_Portal = 160
    Scenario_RestartMainStage = 161
    Scenario_SkipMainStage = 162
    Cafe_Get = 163
    Cafe_Ack = 164
    Cafe_Deploy = 165
    Cafe_Relocate = 166
    Cafe_Remove = 167
    Cafe_RemoveAll = 168
    Cafe_Interact = 169
    Cafe_ListPreset = 170
    Cafe_RenamePreset = 171
    Cafe_ClearPreset = 172
    Cafe_UpdatePresetFurniture = 173
    Cafe_ApplyPreset = 174
    Cafe_RankUp = 175
    Cafe_ReceiveCurrency = 176
    Cafe_GiveGift = 177
    Cafe_SummonCharacter = 178
    Cafe_TrophyHistory = 179
    Cafe_ApplyTemplate = 180
    Cafe_Open = 181
    Cafe_Travel = 182
    Craft_List = 183
    Craft_SelectNode = 184
    Craft_UpdateNodeLevel = 185
    Craft_BeginProcess = 186
    Craft_CompleteProcess = 187
    Craft_Reward = 188
    Craft_HistoryList = 189
    Craft_ShiftingBeginProcess = 190
    Craft_ShiftingCompleteProcess = 191
    Craft_ShiftingReward = 192
    Craft_AutoBeginProcess = 193
    Craft_CompleteProcessAll = 194
    Craft_RewardAll = 195
    Craft_ShiftingCompleteProcessAll = 196
    Craft_ShiftingRewardAll = 197
    Arena_EnterLobby = 198
    Arena_Login = 199
    Arena_SettingChange = 200
    Arena_OpponentList = 201
    Arena_EnterBattle = 202
    Arena_EnterBattlePart1 = 203
    Arena_EnterBattlePart2 = 204
    Arena_BattleResult = 205
    Arena_CumulativeTimeReward = 206
    Arena_DailyReward = 207
    Arena_RankList = 208
    Arena_History = 209
    Arena_RecordSync = 210
    Arena_TicketPurchase = 211
    Arena_DamageReport = 212
    Arena_CheckSeasonCloseReward = 213
    Arena_SyncEchelonSettingTime = 214
    WeekDungeon_List = 215
    WeekDungeon_EnterBattle = 216
    WeekDungeon_BattleResult = 217
    WeekDungeon_Retreat = 218
    Academy_GetInfo = 219
    Academy_AttendSchedule = 220
    Academy_AttendFavorSchedule = 221
    Event_GetList = 222
    Event_GetImage = 223
    Event_UseCoupon = 224
    Event_RewardIncrease = 225
    ContentSave_Get = 226
    ContentSave_Discard = 227
    ContentSweep_Request = 228
    ContentSweep_MultiSweep = 229
    ContentSweep_MultiSweepPresetList = 230
    ContentSweep_SetMultiSweepPreset = 231
    ContentSweep_SetMultiSweepPresetName = 232
    Clan_Lobby = 233
    Clan_Login = 234
    Clan_Search = 235
    Clan_Create = 236
    Clan_Member = 237
    Clan_Applicant = 238
    Clan_Join = 239
    Clan_Quit = 240
    Clan_Permit = 241
    Clan_Kick = 242
    Clan_Setting = 243
    Clan_Confer = 244
    Clan_Dismiss = 245
    Clan_AutoJoin = 246
    Clan_MemberList = 247
    Clan_CancelApply = 248
    Clan_MyAssistList = 249
    Clan_SetAssist = 250
    Clan_ChatLog = 251
    Clan_Check = 252
    Clan_AllAssistList = 253
    Billing_TransactionStartByYostar = 254
    Billing_TransactionEndByYostar = 255
    Billing_PurchaseListByYostar = 256
    EventContent_AdventureList = 257
    EventContent_EnterMainStage = 258
    EventContent_ConfirmMainStage = 259
    EventContent_EnterTactic = 260
    EventContent_TacticResult = 261
    EventContent_EnterSubStage = 262
    EventContent_SubStageResult = 263
    EventContent_DeployEchelon = 264
    EventContent_WithdrawEchelon = 265
    EventContent_MapMove = 266
    EventContent_EndTurn = 267
    EventContent_Retreat = 268
    EventContent_Portal = 269
    EventContent_PurchasePlayCountHardStage = 270
    EventContent_ShopList = 271
    EventContent_ShopRefresh = 272
    EventContent_ReceiveStageTotalReward = 273
    EventContent_EnterMainGroundStage = 274
    EventContent_MainGroundStageResult = 275
    EventContent_ShopBuyMerchandise = 276
    EventContent_ShopBuyRefreshMerchandise = 277
    EventContent_SelectBuff = 278
    EventContent_BoxGachaShopList = 279
    EventContent_BoxGachaShopPurchase = 280
    EventContent_BoxGachaShopRefresh = 281
    EventContent_CollectionList = 282
    EventContent_CollectionForMission = 283
    EventContent_ScenarioGroupHistoryUpdate = 284
    EventContent_CardShopList = 285
    EventContent_CardShopShuffle = 286
    EventContent_CardShopPurchase = 287
    EventContent_RestartMainStage = 288
    EventContent_LocationGetInfo = 289
    EventContent_LocationAttendSchedule = 290
    EventContent_FortuneGachaPurchase = 291
    EventContent_SubEventLobby = 292
    EventContent_EnterStoryStage = 293
    EventContent_StoryStageResult = 294
    EventContent_DiceRaceLobby = 295
    EventContent_DiceRaceRoll = 296
    EventContent_DiceRaceLapReward = 297
    EventContent_PermanentList = 298
    EventContent_DiceRaceUseItem = 299
    EventContent_CardShopPurchaseAll = 300
    EventContent_TreasureLobby = 301
    EventContent_TreasureFlip = 302
    EventContent_TreasureNextRound = 303
    TTS_GetFile = 304
    ContentLog_UIOpenStatistics = 305
    MomoTalk_OutLine = 306
    MomoTalk_MessageList = 307
    MomoTalk_Read = 308
    MomoTalk_Reply = 309
    MomoTalk_FavorSchedule = 310
    ClearDeck_List = 311
    MiniGame_StageList = 312
    MiniGame_EnterStage = 313
    MiniGame_Result = 314
    MiniGame_MissionList = 315
    MiniGame_MissionReward = 316
    MiniGame_MissionMultipleReward = 317
    MiniGame_ShootingLobby = 318
    MiniGame_ShootingBattleEnter = 319
    MiniGame_ShootingBattleResult = 320
    MiniGame_ShootingSweep = 321
    MiniGame_TableBoardSync = 322
    MiniGame_TableBoardMove = 323
    MiniGame_TableBoardEncounterInput = 324
    MiniGame_TableBoardBattleEncounter = 325
    MiniGame_TableBoardBattleRunAway = 326
    MiniGame_TableBoardClearThema = 327
    MiniGame_TableBoardUseItem = 328
    MiniGame_TableBoardResurrect = 329
    MiniGame_TableBoardSweep = 330
    MiniGame_TableBoardMoveThema = 331
    MiniGame_DreamMakerGetInfo = 332
    MiniGame_DreamMakerNewGame = 333
    MiniGame_DreamMakerRestart = 334
    MiniGame_DreamMakerAttendSchedule = 335
    MiniGame_DreamMakerDailyClosing = 336
    MiniGame_DreamMakerEnding = 337
    MiniGame_DefenseGetInfo = 338
    MiniGame_DefenseEnterBattle = 339
    MiniGame_DefenseBattleResult = 340
    Notification_LobbyCheck = 341
    Notification_EventContentReddotCheck = 342
    ProofToken_RequestQuestion = 343
    ProofToken_Submit = 344
    SchoolDungeon_List = 345
    SchoolDungeon_EnterBattle = 346
    SchoolDungeon_BattleResult = 347
    SchoolDungeon_Retreat = 348
    TimeAttackDungeon_Lobby = 349
    TimeAttackDungeon_CreateBattle = 350
    TimeAttackDungeon_EnterBattle = 351
    TimeAttackDungeon_EndBattle = 352
    TimeAttackDungeon_Sweep = 353
    TimeAttackDungeon_GiveUp = 354
    TimeAttackDungeon_Login = 355
    WorldRaid_Lobby = 356
    WorldRaid_BossList = 357
    WorldRaid_EnterBattle = 358
    WorldRaid_BattleResult = 359
    WorldRaid_ReceiveReward = 360
    ResetableContent_Get = 361
    Conquest_GetInfo = 362
    Conquest_Conquer = 363
    Conquest_ConquerWithBattleStart = 364
    Conquest_ConquerWithBattleResult = 365
    Conquest_DeployEchelon = 366
    Conquest_ManageBase = 367
    Conquest_UpgradeBase = 368
    Conquest_TakeEventObject = 369
    Conquest_EventObjectBattleStart = 370
    Conquest_EventObjectBattleResult = 371
    Conquest_ReceiveCalculateRewards = 372
    Conquest_NormalizeEchelon = 373
    Conquest_Check = 374
    Conquest_ErosionBattleStart = 375
    Conquest_ErosionBattleResult = 376
    Conquest_MainStoryGetInfo = 377
    Conquest_MainStoryConquer = 378
    Conquest_MainStoryConquerWithBattleStart = 379
    Conquest_MainStoryConquerWithBattleResult = 380
    Conquest_MainStoryCheck = 381
    Friend_List = 382
    Friend_Remove = 383
    Friend_GetFriendDetailedInfo = 384
    Friend_GetIdCard = 385
    Friend_SetIdCard = 386
    Friend_Search = 387
    Friend_SendFriendRequest = 388
    Friend_AcceptFriendRequest = 389
    Friend_DeclineFriendRequest = 390
    Friend_CancelFriendRequest = 391
    Friend_Check = 392
    Friend_ListByIds = 393
    Friend_Block = 394
    Friend_Unblock = 395
    CharacterGear_List = 396
    CharacterGear_Unlock = 397
    CharacterGear_TierUp = 398
    EliminateRaid_Login = 399
    EliminateRaid_Lobby = 400
    EliminateRaid_OpponentList = 401
    EliminateRaid_GetBestTeam = 402
    EliminateRaid_CreateBattle = 403
    EliminateRaid_EnterBattle = 404
    EliminateRaid_EndBattle = 405
    EliminateRaid_GiveUp = 406
    EliminateRaid_Sweep = 407
    EliminateRaid_SeasonReward = 408
    EliminateRaid_RankingReward = 409
    EliminateRaid_LimitedReward = 410
    Attachment_Get = 411
    Attachment_EmblemList = 412
    Attachment_EmblemAcquire = 413
    Attachment_EmblemAttach = 414
    Sticker_Login = 415
    Sticker_Lobby = 416
    Sticker_UseSticker = 417
    Field_Sync = 418
    Field_Interaction = 419
    Field_QuestClear = 420
    Field_SceneChanged = 421
    Field_EndDate = 422
    Field_EnterStage = 423
    Field_StageResult = 424
    MultiFloorRaid_Sync = 425
    MultiFloorRaid_EnterBattle = 426
    MultiFloorRaid_EndBattle = 427
    MultiFloorRaid_ReceiveReward = 428
    Queuing_GetTicket = 429
    Log_TestBattleCheckAsync = 430
    Log_TestBattleCheckSync = 431
    Log_TestBattleCheckSyncWithBattleSetting = 432
    Management_Data = 433
    Order_Notify = 434
    Battle_Notify = 435
    Survey_Notify = 436
    Web_Notify = 437
    Clan_Chat_Records = 438
    Clan_Send_Chat = 439
    Shop_ListTutorialGacha = 440
    Shop_BuyTutorialGacha = 441
    Shop_SaveTutorialGacha = 442
    Shop_ConfirmTutorialGacha = 443

class ServerNotificationFlag(IntEnum):
    None_ = 0
    NewMailArrived = 1
    HasUnreadMail = 2
    NewToastDetected = 3
    CanReceiveArenaDailyReward = 4
    CanReceiveRaidReward = 5
    ServerMaintenance = 6
    CannotReceiveMail = 7
    InventoryFullRewardMail = 8
    CanReceiveClanAttendanceReward = 9
    HasClanApplicant = 10
    HasFriendRequest = 11
    CheckConquest = 12
    CanReceiveEliminateRaidReward = 13
    CanReceiveMultiFloorRaidReward = 14

class CampaignState(IntEnum):
    BeforeStart = 0
    BeginPlayerPhase = 1
    PlayerPhase = 2
    EndPlayerPhase = 3
    BeginEnemyPhase = 4
    EnemyPhase = 5
    EndEnemyPhase = 6
    Win = 7
    Lose = 8
    StrategySkip = 9

class CampaignEndBattle(IntEnum):
    None_ = 0
    Win = 1
    Lose = 2

class CheatFlags(IntEnum):
    None_ = 0
    Conquest = 1
    Mission = 2

class RaidRoomSortOption(IntEnum):
    HPHigh = 0
    HPLow = 1
    RemainTimeHigh = 2
    RemainTimeLow = 3

class WebAPIErrorCode(IntEnum):
    None_ = 0
    InvalidPacket = 1
    InvalidProtocol = 2
    InvalidSession = 3
    InvalidVersion = 4
    InternalServerError = 5
    DBError = 6
    InvalidToken = 7
    FailedToLockAccount = 8
    InvalidCheatError = 9
    AccountCurrencyCannotAffordCost = 10
    ExceedTranscendenceCountLimit = 11
    MailBoxFull = 12
    InventoryAlreadyFull = 13
    AccountNotFound = 14
    DataClassNotFound = 15
    DataEntityNotFound = 16
    AccountGemPaidCannotAffordCost = 17
    AccountGemBonusCannotAffordCost = 18
    AccountItemCannotAffordCost = 19
    APITimeoutError = 20
    FunctionTimeoutError = 21
    DBDistributeTransactionError = 22
    OccasionalJobError = 23
    FailedToConsumeParcel = 24
    InvalidString = 25
    InvalidStringLength = 26
    EmptyString = 27
    SpecialSymbolNotAllowed = 28
    InvalidDate = 29
    CoolTimeRemain = 30
    TimeElapseError = 31
    ClientSendBadRequest = 32
    ClientSendTooManyRequest = 33
    ClientSuspectedAsCheater = 34
    CombatVerificationFailedInDev = 35
    ServerFailedToHandleRequest = 36
    DocumentDBFailedToHandleRequest = 37
    ServerCacheFailedToHandleRequest = 38
    ReconnectBundleUpdateRequired = 39
    GatewayMakeStandbyNotSupport = 40
    GatewayPassCheckNotSupport = 41
    GatewayWaitingTicketTimeOut = 42
    ClientUpdateRequire = 43
    AccountCreateNoDevId = 44
    AccountCreateDuplicatedDevId = 45
    AccountAuthEmptyDevId = 46
    AccountAuthNotCreated = 47
    AccountAccessControlWithoutPermission = 48
    AccountNicknameEmptyString = 49
    AccountNicknameSameName = 50
    AccountNicknameWithInvalidString = 51
    AccountNicknameWithInvalidLength = 52
    YostarServerNotSuccessStatusCode = 53
    YostarNetworkException = 54
    YostarException = 55
    AccoountPassCheckNotSupportCheat = 56
    AccountCreateFail = 57
    AccountAddPubliserAccountFail = 58
    AccountAddDevIdFail = 59
    AccountCreateAlreadyPublisherAccoundId = 60
    AccountUpdateStateFail = 61
    YostarCheckFail = 62
    EnterTicketInvalid = 63
    EnterTicketTimeOut = 64
    EnterTicketUsed = 65
    AccountCommentLengthOverLimit = 66
    AccountUpdateBirthdayFailed = 67
    AccountLoginError = 68
    AccountCurrencySyncError = 69
    InvalidClientCookie = 70
    InappositeNicknameRestricted = 71
    InappositeCommentRestricted = 72
    InappositeCallnameRestricted = 73
    CharacterNotFound = 74
    CharacterLocked = 75
    CharacterAlreadyHas = 76
    CharacterAssignedEchelon = 77
    CharacterFavorDownException = 78
    CharacterFavorMaxLevelExceed = 79
    CannotLevelUpSkill = 80
    CharacterLevelAlreadyMax = 81
    InvalidCharacterExpGrowthRequest = 82
    CharacterWeaponDataNotFound = 83
    CharacterWeaponNotFound = 84
    CharacterWeaponAlreadyUnlocked = 85
    CharacterWeaponUnlockConditionFail = 86
    CharacterWeaponExpGrowthNotValidItem = 87
    InvalidCharacterWeaponExpGrowthRequest = 88
    CharacterWeaponTranscendenceRecipeNotFound = 89
    CharacterWeaponTranscendenceConditionFail = 90
    CharacterWeaponUpdateFail = 91
    CharacterGearNotFound = 92
    CharacterGearAlreadyEquiped = 93
    CharacterGearCannotTierUp = 94
    CharacterGearCannotUnlock = 95
    CharacterCostumeNotFound = 96
    CharacterCostumeAlreadySet = 97
    CharacterCannotEquipCostume = 98
    InvalidCharacterSkillLevelUpdateRequest = 99
    InvalidCharacterPotentialGrowthRequest = 100
    CharacterPotentialGrowthDataNotFound = 101
    EquipmentNotFound = 102
    InvalidEquipmentExpGrowthRequest = 103
    EquipmentNotMatchingSlotItemCategory = 104
    EquipmentLocked = 105
    EquipmentAlreadyEquiped = 106
    EquipmentConsumeItemLimitCountOver = 107
    EquipmentNotEquiped = 108
    EquipmentCanNotEquip = 109
    EquipmentIngredientEmtpy = 110
    EquipmentCannotLevelUp = 111
    EquipmentCannotTierUp = 112
    EquipmentGearCannotUnlock = 113
    EquipmentBatchGrowthNotValid = 114
    ItemNotFound = 115
    ItemLocked = 116
    ItemCreateWithoutStackCount = 117
    ItemCreateStackCountFull = 118
    ItemNotUsingType = 119
    ItemEnchantIngredientFail = 120
    ItemInvalidConsumeRequest = 121
    ItemInsufficientStackCount = 122
    ItemOverExpirationDateTime = 123
    ItemCannotAutoSynth = 124
    EchelonEmptyLeader = 125
    EchelonNotFound = 126
    EchelonNotDeployed = 127
    EchelonSlotOverMaxCount = 128
    EchelonAssignCharacterOnOtherEchelon = 129
    EchelonTypeNotAcceptable = 130
    EchelonEmptyNotAcceptable = 131
    EchelonPresetInvalidSave = 132
    EchelonPresetLabelLengthInvalid = 133
    CampaignStageNotOpen = 134
    CampaignStagePlayLimit = 135
    CampaignStageEnterFail = 136
    CampaignStageInvalidSaveData = 137
    CampaignStageNotPlayerTurn = 138
    CampaignStageStageNotFound = 139
    CampaignStageHistoryNotFound = 140
    CampaignStageChapterNotFound = 141
    CampaignStageEchelonNotFound = 142
    CampaignStageWithdrawedCannotReUse = 143
    CampaignStageChapterRewardInvalidReward = 144
    CampaignStageChapterRewardAlreadyReceived = 145
    CampaignStageTacticWinnerInvalid = 146
    CampaignStageActionCountZero = 147
    CampaignStageHealNotAcceptable = 148
    CampaignStageHealLimit = 149
    CampaignStageLocationCanNotEngage = 150
    CampaignEncounterWaitingCannotEndTurn = 151
    CampaignTacticResultEmpty = 152
    CampaignPortalExitNotFound = 153
    CampaignCannotReachDestination = 154
    CampaignChapterRewardConditionNotSatisfied = 155
    CampaignStageDataInvalid = 156
    ContentSweepNotOpened = 157
    CampaignTacticSkipFailed = 158
    CampaignUnableToRemoveFixedEchelon = 159
    CampaignCharacterIsNotWhitelist = 160
    CampaignFailedToSkipStrategy = 161
    InvalidSweepRequest = 162
    MailReceiveRequestInvalid = 163
    MissionCannotComplete = 164
    MissionRewardInvalid = 165
    AttendanceInvalid = 166
    ShopExcelNotFound = 167
    ShopAndGoodsNotMatched = 168
    ShopGoodsNotFound = 169
    ShopExceedPurchaseCountLimit = 170
    ShopCannotRefresh = 171
    ShopInfoNotFound = 172
    ShopCannotPurchaseActionPointLimitOver = 173
    ShopNotOpened = 174
    ShopInvalidGoods = 175
    ShopInvalidCostOrReward = 176
    ShopEligmaOverPurchase = 177
    ShopFreeRecruitInvalid = 178
    ShopNewbieGachaInvalid = 179
    ShopCannotNewGoodsRefresh = 180
    GachaCostNotValid = 181
    ShopRestrictBuyWhenInventoryFull = 182
    BeforehandGachaMetadataNotFound = 183
    BeforehandGachaCandidateNotFound = 184
    BeforehandGachaInvalidLastIndex = 185
    BeforehandGachaInvalidSaveIndex = 186
    BeforehandGachaInvalidPickIndex = 187
    BeforehandGachaDuplicatedResults = 188
    RecipeCraftNoData = 189
    RecipeCraftInsufficientIngredients = 190
    RecipeCraftDataError = 191
    MemoryLobbyNotFound = 192
    LobbyModeChangeFailed = 193
    CumulativeTimeRewardNotFound = 194
    CumulativeTimeRewardAlreadyReceipt = 195
    CumulativeTimeRewardInsufficientConnectionTime = 196
    OpenConditionClosed = 197
    OpenConditionSetNotSupport = 198
    CafeNotFound = 199
    CafeFurnitureNotFound = 200
    CafeDeployFail = 201
    CafeRelocateFail = 202
    CafeInteractionNotFound = 203
    CafeProductionEmpty = 204
    CafeRankUpFail = 205
    CafePresetNotFound = 206
    CafeRenamePresetFail = 207
    CafeClearPresetFail = 208
    CafeUpdatePresetFurnitureFail = 209
    CafeReservePresetActivationTimeFail = 210
    CafePresetApplyFail = 211
    CafePresetIsEmpty = 212
    CafeAlreadyVisitCharacter = 213
    CafeCannotSummonCharacter = 214
    CafeCanRefreshVisitCharacter = 215
    CafeAlreadyInteraction = 216
    CafeTemplateNotFound = 217
    CafeAlreadyOpened = 218
    CafeNoPlaceToTravel = 219
    CafeCannotTravelToOwnCafe = 220
    CafeCannotTravel = 221
    CafeCannotTravel_CafeLock = 222
    ScenarioMode_Fail = 223
    ScenarioMode_DuplicatedScenarioModeId = 224
    ScenarioMode_LimitClearedScenario = 225
    ScenarioMode_LimitAccountLevel = 226
    ScenarioMode_LimitClearedStage = 227
    ScenarioMode_LimitClubStudent = 228
    ScenarioMode_FailInDBProcess = 229
    ScenarioGroup_DuplicatedScenarioGroupId = 230
    ScenarioGroup_FailInDBProcess = 231
    ScenarioGroup_DataNotFound = 232
    ScenarioGroup_MeetupConditionFail = 233
    CraftInfoNotFound = 234
    CraftCanNotCreateNode = 235
    CraftCanNotUpdateNode = 236
    CraftCanNotBeginProcess = 237
    CraftNodeDepthError = 238
    CraftAlreadyProcessing = 239
    CraftCanNotCompleteProcess = 240
    CraftProcessNotComplete = 241
    CraftInvalidIngredient = 242
    CraftError = 243
    CraftInvalidData = 244
    CraftNotAvailableToCafePresets = 245
    CraftNotEnoughEmptySlotCount = 246
    CraftInvalidPresetSlotDB = 247
    RaidExcelDataNotFound = 248
    RaidSeasonNotOpen = 249
    RaidDBDataNotFound = 250
    RaidBattleNotFound = 251
    RaidBattleUpdateFail = 252
    RaidCompleteListEmpty = 253
    RaidRoomCanNotCreate = 254
    RaidActionPointZero = 255
    RaidTicketZero = 256
    RaidRoomCanNotJoin = 257
    RaidRoomMaxPlayer = 258
    RaidRewardDataNotFound = 259
    RaidSeasonRewardNotFound = 260
    RaidSeasonAlreadyReceiveReward = 261
    RaidSeasonAddRewardPointError = 262
    RaidSeasonRewardNotUpdate = 263
    RaidSeasonReceiveRewardFail = 264
    RaidSearchNotFound = 265
    RaidShareNotFound = 266
    RaidEndRewardFlagError = 267
    RaidCanNotFoundPlayer = 268
    RaidAlreadyParticipateCharacters = 269
    RaidClearHistoryNotSave = 270
    RaidBattleAlreadyEnd = 271
    RaidEchelonNotFound = 272
    RaidSeasonOpen = 273
    RaidRoomIsAlreadyClose = 274
    RaidRankingNotFound = 275
    WeekDungeonInfoNotFound = 276
    WeekDungeonNotOpenToday = 277
    WeekDungeonBattleWinnerInvalid = 278
    WeekDungeonInvalidSaveData = 279
    FindGiftRewardNotFound = 280
    FindGiftRewardAlreadyAcquired = 281
    FindGiftClearCountOverTotalCount = 282
    ArenaInfoNotFound = 283
    ArenaGroupNotFound = 284
    ArenaRankHistoryNotFound = 285
    ArenaRankInvalid = 286
    ArenaBattleFail = 287
    ArenaDailyRewardAlreadyBeenReceived = 288
    ArenaNoSeasonAvailable = 289
    ArenaAttackCoolTime = 290
    ArenaOpponentAlreadyBeenAttacked = 291
    ArenaOpponentRankInvalid = 292
    ArenaNeedFormationSetting = 293
    ArenaNoHistory = 294
    ArenaInvalidRequest = 295
    ArenaInvalidIndex = 296
    ArenaNotFoundBattle = 297
    ArenaBattleTimeOver = 298
    ArenaRefreshTimeOver = 299
    ArenaEchelonSettingTimeOver = 300
    ArenaCannotReceiveReward = 301
    ArenaRewardNotExist = 302
    ArenaCannotSetMap = 303
    ArenaDefenderRankChange = 304
    AcademyNotFound = 305
    AcademyScheduleTableNotFound = 306
    AcademyScheduleOperationNotFound = 307
    AcademyAlreadyAttendedSchedule = 308
    AcademyAlreadyAttendedFavorSchedule = 309
    AcademyRewardCharacterNotFound = 310
    AcademyScheduleCanNotAttend = 311
    AcademyTicketZero = 312
    AcademyMessageCanNotSend = 313
    ContentSaveDBNotFound = 314
    ContentSaveDBEntranceFeeEmpty = 315
    AccountBanned = 316
    ServerNowLoadingProhibitedWord = 317
    ServerIsUnderMaintenance = 318
    ServerMaintenanceSoon = 319
    AccountIsNotInWhiteList = 320
    ServerContentsLockUpdating = 321
    ServerContentsLock = 322
    CouponIsEmpty = 323
    CouponIsInvalid = 324
    UseCouponUsedListReadFail = 325
    UseCouponUsedCoupon = 326
    UseCouponNotFoundSerials = 327
    UseCouponDeleteSerials = 328
    UseCouponUnapprovedSerials = 329
    UseCouponExpiredSerials = 330
    UseCouponMaximumSerials = 331
    UseCouponNotFoundMeta = 332
    UseCouponDuplicateUseCoupon = 333
    UseCouponDuplicateUseSerial = 334
    BillingStartShopCashIdNotFound = 335
    BillingStartNotServiceTime = 336
    BillingStartUseConditionCheckError = 337
    BillingStartSmallLevel = 338
    BillingStartMaxPurchaseCount = 339
    BillingStartFailAddOrder = 340
    BillingStartExistPurchase = 341
    BillingEndFailGetOrder = 342
    BillingEndShopCashIdNotFound = 343
    BillingEndProductIdNotFound = 344
    BillingEndMonthlyProductIdNotFound = 345
    BillingEndInvalidState = 346
    BillingEndFailUpdteState = 347
    BillingEndFailSendMail = 348
    BillingEndInvalidAccount = 349
    BillingEndNotFoundPurchaseCount = 350
    BillingEndFailUpdteMonthlyProduct = 351
    BillingStartMailFull = 352
    BillingStartInventoryAndMailFull = 353
    BillingEndRecvedErrorMonthlyProduct = 354
    MonthlyProductNotOutdated = 355
    ClanNotFound = 356
    ClanSearchFailed = 357
    ClanEmptySearchString = 358
    ClanAccountAlreadyJoinedClan = 359
    ClanAccountAlreadyQuitClan = 360
    ClanCreateFailed = 361
    ClanMemberExceedCapacity = 362
    ClanDoesNotHavePermission = 363
    ClanTargetAccountIsNotApplicant = 364
    ClanMemberNotFound = 365
    ClanCanNotKick = 366
    ClanCanNotDismiss = 367
    ClanCanNotQuit = 368
    ClanRejoinCoolOff = 369
    ClanChangeMemberGradeFailed = 370
    ClanHasBeenDisMissed = 371
    ClanCannotChangeJoinOption = 372
    ClanExceedConferCountLimit = 373
    ClanBusy = 374
    ClanNameEmptyString = 375
    ClanNameWithInvalidLength = 376
    ClanAssistCharacterAlreadyDeployed = 377
    ClanAssistNotValidUse = 378
    ClanAssistCharacterChanged = 379
    ClanAssistCoolTime = 380
    ClanAssistAlreadyUsedInRaidRoom = 381
    ClanAssistAlreadyUsedInTimeAttackDungeonRoom = 382
    ClanAssistEchelonHasAssistOnly = 383
    PaymentInvalidSign = 384
    PaymentInvalidSeed1 = 385
    PaymentInvalidSeed2 = 386
    PaymentInvalidInput = 387
    PaymentNotFoundPurchase = 388
    PaymentGetPurchaseOrderNotZero = 389
    PaymentSetPurchaseOrderNotZero = 390
    PaymentException = 391
    PaymentInvalidState = 392
    SessionNotFound = 393
    SessionParseFail = 394
    SessionInvalidInput = 395
    SessionNotAuth = 396
    SessionDuplicateLogin = 397
    SessionTimeOver = 398
    SessionInvalidVersion = 399
    SessionChangeDate = 400
    CallName_RenameCoolTime = 401
    CallName_EmptyString = 402
    CallName_InvalidString = 403
    CallName_TTSServerIsNotAvailable = 404
    CouchbaseInvalidCas = 405
    CouchbaseOperationFailed = 406
    CouchbaseRollBackFailed = 407
    EventContentCannotSelectBuff = 408
    EventContentNoBuffGroupAvailable = 409
    EventContentBuffGroupIdDuplicated = 410
    EventContentNotOpen = 411
    EventContentNoTotalRewardAvailable = 412
    EventContentBoxGachaPurchaseFailed = 413
    EventContentBoxGachaCannotRefresh = 414
    EventContentCardShopCannotShuffle = 415
    EventContentElementDoesNotExist = 416
    EventContentElementAlreadyPurchased = 417
    EventContentLocationNotFound = 418
    EventContentLocationScheduleCanNotAttend = 419
    EventContentDiceRaceDataNotFound = 420
    EventContentDiceRaceAlreadyReceiveLapRewardAll = 421
    EventContentDiceRaceInvalidDiceRaceResultType = 422
    EventContentTreasureDataNotFound = 423
    EventContentTreasureNotComplete = 424
    EventContentTreasureFlipFailed = 425
    MiniGameStageIsNotOpen = 426
    MiniGameStageInvalidResult = 427
    MiniGameShootingStageInvlid = 428
    MiniGameShootingCannotSweep = 429
    MiniGameTableBoardSaveNotExist = 430
    MiniGameTableBoardPlayerCannotMove = 431
    MiniGameTableBoardNoActiveEncounter = 432
    MiniGameTableBoardInvalidEncounterRequest = 433
    MiniGameTableBoardProcessEncounterFailed = 434
    MiniGameTableBoardItemNotExist = 435
    MiniGameTableBoardInvalidItemUse = 436
    MiniGameTableBoardInvalidClearThemaRequest = 437
    MiniGameTableBoardInvalidSeason = 438
    MiniGameTableBoardInvalidResurrectRequest = 439
    MiniGameTableBoardSweepConditionFail = 440
    MiniGameTableBoardInvalidData = 441
    MiniGameDreamCannotStartNewGame = 442
    MiniGameDreamCannotApplyMultiplier = 443
    MiniGameDreamCannotReset = 444
    MiniGameDreamNotEnoughActionCount = 445
    MiniGameDreamSaveNotExist = 446
    MiniGameDreamActionCountRemain = 447
    MiniGameDreamRoundNotComplete = 448
    MiniGameDreamRewardAlreadyReceived = 449
    MiniGameDreamRoundCompleted = 450
    MiniGameShouldReceiveEndingReward = 451
    MiniGameDefenseCannotUseCharacter = 452
    MiniGameDefenseNotOpenStage = 453
    MiniGameDefenseCannotApplyMultiplier = 454
    ProofTokenNotSubmitted = 455
    SchoolDungeonInfoNotFound = 456
    SchoolDungeonNotOpened = 457
    SchoolDungeonInvalidSaveData = 458
    SchoolDungeonBattleWinnerInvalid = 459
    SchoolDungeonInvalidReward = 460
    TimeAttackDungeonDataNotFound = 461
    TimeAttackDungeonNotOpen = 462
    TimeAttackDungeonRoomTimeOut = 463
    TimeAttackDungeonRoomPlayCountOver = 464
    TimeAttackDungeonRoomAlreadyExists = 465
    TimeAttackDungeonRoomAlreadyClosed = 466
    TimeAttackDungeonRoomNotExist = 467
    TimeAttackDungeonInvalidRequest = 468
    TimeAttackDungeonInvalidData = 469
    WorldRaidDataNotFound = 470
    WorldRaidSeasonNotOpen = 471
    WorldRaidBossGroupNotOpen = 472
    WorldRaidInvalidOpenCondition = 473
    WorldRaidDifficultyNotOpen = 474
    WorldRaidAssistCharacterLimitOver = 475
    WorldRaidContainBlackListCharacter = 476
    WorldRaidValidFixedEchelonSetting = 477
    WorldRaidAlredayReceiveRewardAll = 478
    WorldRaidCannotReceiveReward = 479
    WorldRaidBossAlreadyDead = 480
    WorldRaidNotAnotherBossKilled = 481
    WorldRaidBattleResultUpdateFailed = 482
    WorldRaidGemEnterCountLimitOver = 483
    WorldRaidCannotGemEnter = 484
    WorldRaidNeedClearScenarioBoss = 485
    WorldRaidBossIsAlive = 486
    ConquestDataNotFound = 487
    ConquestAlreadyConquested = 488
    ConquestNotFullyConquested = 489
    ConquestStepNotOpened = 490
    ConquestUnableToReach = 491
    ConquestUnableToAttack = 492
    ConquestEchelonChangedCountMax = 493
    ConquestEchelonNotFound = 494
    ConquestCharacterAlreadyDeployed = 495
    ConquestMaxUpgrade = 496
    ConquestUnitNotFound = 497
    ConquestObjectNotFound = 498
    ConquestCalculateRewardNotFound = 499
    ConquestInvalidTileType = 500
    ConquestInvalidObjectType = 501
    ConquestInvalidSaveData = 502
    ConquestMaxAssistCountReached = 503
    ConquestErosionConditionNotSatisfied = 504
    ConquestAdditionalContentNotInUse = 505
    ConquestCannotUseManageEchelon = 506
    FriendUserIsNotFriend = 507
    FriendFailedToCreateFriendIdCard = 508
    FriendRequestNotFound = 509
    FriendInvalidFriendCode = 510
    FriendAlreadyFriend = 511
    FriendMaxSentRequestReached = 512
    FriendMaxReceivedRequestReached = 513
    FriendCannotRequestMaxFriendCountReached = 514
    FriendCannotAcceptMaxFriendCountReached = 515
    FriendOpponentMaxFriendCountReached = 516
    FriendTargetIsBusy = 517
    FriendRequestTargetIsYourself = 518
    FriendSearchTargetIsYourself = 519
    FriendInvalidBackgroundId = 520
    FriendIdCardCommentLengthOverLimit = 521
    FriendBackgroundNotOwned = 522
    FriendBlockTargetIsYourself = 523
    FriendBlockTargetIsAlreadyBlocked = 524
    FriendBlockTargetIsExceedMaxCount = 525
    FriendBlockUserCannotOpenProfile = 526
    FriendBlockUserCannotSendRequest = 527
    EliminateStageIsNotOpened = 528
    MultiSweepPresetDocumentNotFound = 529
    MultiSweepPresetNameEmpty = 530
    MultiSweepPresetInvalidStageId = 531
    MultiSweepPresetInvalidId = 532
    MultiSweepPresetNameInvalidLength = 533
    MultiSweepPresetTooManySelectStageId = 534
    MultiSweepPresetInvalidSweepCount = 535
    MultiSweepPresetTooManySelectParcelId = 536
    EmblemDataNotFound = 537
    EmblemAttachFailed = 538
    EmblemCannotReceive = 539
    EmblemPassCheckEmblemIsEmpty = 540
    StickerDataNotFound = 541
    StickerNotAcquired = 542
    StickerDocumentNotFound = 543
    StickerAlreadyUsed = 544
    ClearDeckInvalidKey = 545
    ClearDeckOutOfDate = 546
    FieldDataNotFound = 547
    FieldInteracionFailed = 548
    FieldQuestClearFailed = 549
    FieldInvalidSceneChangedRequest = 550
    FieldInvalidEndDateRequest = 551
    FieldCreateDailyQuestFailed = 552
    FieldResetReplayFailed = 553
    FieldIncreaseMasteryFailed = 554
    FieldStageDataInvalid = 555
    FieldStageEnterFail = 556
    FieldContentIsClosed = 557
    FieldEventStageNotCleared = 558
    MultiFloorRaidSeasonNotOpened = 559
    MultiFloorRaidDataNotFound = 560
    MultiFloorRaidAssistCharacterLimitOver = 561
    MultiFloorRaidStageOpenConditionFail = 562
    MultiFloorRaidInvalidSummary = 563
    MultiFloorRaidInvalidRewardRequest = 564
    BattleServerError = 565
    ServerBusy = 566
    UseCopuonDuplicateUseCoupon = 567
    ClanNotHaveApplication = 568
    ClanBeKickedOut = 569
    SessionCrossDay = 570
    AppUpdate = 571
    ResourceUpdate = 572
    GachaDailyPurchaseLimit = 573
    ClanCantConferInactivePlayer = 574
    FeatureSuspendedNotice = 575
    CouponAreaNotMatch = 576
    UseCouponFrequentRequests = 577
    UseCouponExceededLimit = 578

class StepState(IntEnum):
    Default = 0
    StandBy = 1
    Eroding = 2
    Complete = 3

class OpenConditionLockReason(IntEnum):
    None_ = 0
    Level = 1
    StageClear = 2
    Time = 3
    Day = 4
    CafeRank = 5
    ScenarioModeClear = 6
    CafeOpen = 7

class SweepSortingOrder(IntEnum):
    None_ = 0
    Item_Coin = 1
    Item_SceretStone = 2
    Equipment = 3
    Item_CharacterExpGrowth = 4
    Item_Material = 5
    Currency = 6

class ProhibitWordType(IntEnum):
    BlackList = 0
    WhiteList = 1

class NarrowOrWide(IntEnum):
    None_ = 0
    Narrow = 1
    Wide = 2

class ResetableContentBandWidth(IntEnum):
    MiniEventToken = 0

class ParcelProcessActionType(IntEnum):
    None_ = 0
    Cost = 1
    Reward = 2

class ParcelChangeType(IntEnum):
    NoChange = 0
    Terminated = 1
    MailSend = 2
    Converted = 3

class UserType(IntEnum):
    None_ = 0
    GM = 1
    Tester = 2
    Bot = 3

class LogCode(IntEnum):
    None_ = 0
    AccountLogin = 1
    AccountLogOut = 2
    AccountStatusChange = 3
    AccountCharacterChange = 4
    AccountEquipmentChange = 5
    AccountItemChange = 6
    AccountFurnitureChange = 7
    AccountCharacterWeaponChange = 8
    AccountCurrency = 9
    AccountCurrencyChange = 10
    AccountApCurrencyCharge = 11
    AccountGemCurrencyCharge = 12
    AccountTicketChange = 13
    AccountMonthlyProductFix = 14
    Adventure_Default = 15
    Adventure_Squad = 16
    Adventure_Detail = 17
    Adventure_Ground = 18
    Adventure_Reward = 19
    Adventure_Hero = 20
    Adventure_Supporter = 21
    Adventure_Deck = 22
    Raid_Default = 23
    Raid_Squad = 24
    Raid_Detail = 25
    Raid_Reward = 26
    Raid_SeasonReward = 27
    Raid_BestRecord = 28
    WeekDungeon_Default = 29
    WeekDungeon_Squad = 30
    WeekDungeon_Detail = 31
    WeekDungeon_Reward = 32
    Arena_Default = 33
    Arena_Squad = 34
    Arena_Detail = 35
    Arena_Reward = 36
    Arena_Performance = 37
    SchoolDungeon_Default = 38
    SchoolDungeon_Squad = 39
    SchoolDungeon_Detail = 40
    SchoolDungeon_Reward = 41
    Battle_Character = 42
    Student_FavorRankChange = 43
    Parcel_CharacterChange = 44
    Parcel_EquipmentChange = 45
    Parcel_ItemChange = 46
    Parcel_Item = 47
    Parcel_MemoryLobby = 48
    Parcel_Furniture = 49
    Scenario_Default = 50
    Scenario_Skip = 51
    Scenario_Select = 52
    Scenario_AccountStudent = 53
    Scenario_LobbyStudent = 54
    Scenario_SpecialLobby = 55
    Scenario_AccountStudentChange = 56
    Scenario_LobbyStudentChange = 57
    Scenario_SpecialLobbyChange = 58
    Scenario_Schedule = 59
    Scene_Default = 60
    Cafe_Default = 61
    Cafe_Character = 62
    Cafe_ChangeFurniture = 63
    Cafe_FurnitureInfo = 64
    Goods_Gacha = 65
    Goods_Shop = 66
    Goods_UseGold = 67
    Mission_Default = 68
    ItemInfo_Default = 69
    ProofToken_Default = 70
    ProofToken_QuestionSent = 71
    ProofToken_WrongProtocolEncoding = 72
    FortuneGacha_Default = 73
    TimeAttackDungeon_Default = 74
    TimeAttackDungeon_Reward = 75
    TimeAttackDungeon_Sweep = 76
    Conquest_Default = 77
    Conquest_Squad = 78
    Conquest_Detail = 79
    Conquest_Reward = 80
    WorldRaid_Default = 81
    WorldRaid_Detail = 82
    WorldRaid_Squad = 83
    Craft_PreReward = 84
    Friend_SendRequest = 85
    Friend_RequestAccept = 86
    Friend_RequestDecline = 87
    Friend_Remove = 88
    Friend_IdCardBackgroundChange = 89
    EliminateRaid_Default = 90
    EliminateRaid_Squad = 91
    EliminateRaid_Detail = 92
    EliminateRaid_Reward = 93
    EliminateRaid_SeasonReward = 94
    EliminateRaid_BestRecord = 95
    EliminateRaid_LimitedReward = 96
    AccountAttachment_Emblem = 97
    MiniGameShooting_Default = 98
    MiniGameShooting_Sweep = 99
    MultiFloorRaid_Default = 100
    MultiFloorRaid_Detail = 101
    MultiFloorRaid_Squad = 102
    MultiFloorRaid_Reward = 103
    Clan_Transfer = 104
    ClientSetting_Default = 105
    Issue_Default = 106

class AssistRelation(IntEnum):
    None_ = 0
    Clan = 1
    Friend = 2
    Cheat = 3
    Stranger = 4

class ShopCashBlockType(IntEnum):
    All = 0
    AppStore = 1
    GooglePlay = 2
    None_ = 3

class CraftProcessCompleteType(IntEnum):
    None_ = 0
    ByTimeElapse = 1
    ByPlayer = 2

class CraftState(IntEnum):
    None_ = 0
    BaseNode = 1
    NodeSelecting = 2
    Crafting = 3
    Complete = 4

class EchelonStatusFlag(IntEnum):
    None_ = 0
    BeforeDeploy = 1
    OnDuty = 2

class IssueAlertTypeCode(IntEnum):
    All = 0
    File_Target = 1
    AllButFile_Exception = 2

class ShopProductType(IntEnum):
    None_ = 0
    General = 1
    Refresh = 2

class IrcMessageType(IntEnum):
    None_ = 0
    Notice = 1
    Sticker = 2
    Chat = 3
    HistoryCount = 4

class IrcNoticeType(IntEnum):
    None_ = 0
    Apply = 1
    Join = 2
    Confer = 3
    Leave = 4
    Dismiss = 5

class RotationType(IntEnum):
    None_ = 0
    Clockwise = 1
    CounterClockwise = 2

class ShapeType(IntEnum):
    None_ = 0
    Circle = 1
    Donut = 2
    Fan = 3
    LineSegment = 4
    OBB = 5

class DiffOperatorType(IntEnum):
    None_ = 0
    GreaterOrEqual = 1
    LessOrEqual = 2
    Equal = 3
    NotEqual = 4

class TransitionType(IntEnum):
    None_ = 0
    Linear = 1
    EaseIn = 2
    EaseOut = 3
    EaseInSine = 4
    EaseOutSine = 5
    EaseInOutSine = 6
    EaseInQuad = 7
    EaseOutQuad = 8
    EaseInOutQuad = 9
    EaseInCubic = 10
    EaseOutCubic = 11
    EaseInOutCubic = 12
    EaseInQuart = 13
    EaseOutQuart = 14
    EaseInOutQuart = 15
    EaseInQuint = 16
    EaseOutQuint = 17
    EaseInOutQuint = 18
    EaseInExpo = 19
    EaseOutExpo = 20
    EaseInOutExpo = 21
    EaseInCirc = 22
    EaseOutCirc = 23
    EaseInOutCirc = 24
    EaseInBack = 25
    EaseOutBack = 26
    EaseInOutBack = 27
    EaseInElastic = 28
    EaseOutElastic = 29
    EaseInOutElastic = 30
    EaseInBounce = 31
    EaseOutBounce = 32
    EaseInOutBounce = 33

class CRCResult(IntEnum):
    None_ = 0
    FileNotExists = 1
    Valid = 2
    Invalid = 3

class MissingFieldAction(IntEnum):
    ParseError = 0
    ReplaceByEmpty = 1
    ReplaceByNull = 2

class ParseErrorAction(IntEnum):
    RaiseEvent = 0
    AdvanceToNextLine = 1
    ThrowException = 2

class ValueTrimmingOptions(IntEnum):
    None_ = 0
    UnquotedOnly = 1
    QuotedOnly = 2
    All = 3

class EvaluateOptions(IntEnum):
    None_ = 0
    IgnoreCase = 1
    NoCache = 2
    IterateParameters = 3
    RoundAwayFromZero = 4

class BinaryExpressionType(IntEnum):
    And = 0
    Or = 1
    NotEqual = 2
    LesserOrEqual = 3
    GreaterOrEqual = 4
    Lesser = 5
    Greater = 6
    Equal = 7
    Minus = 8
    Plus = 9
    Modulo = 10
    Div = 11
    Times = 12
    BitwiseOr = 13
    BitwiseAnd = 14
    BitwiseXOr = 15
    LeftShift = 16
    RightShift = 17
    Unknown = 18

class FunctionType(IntEnum):
    Invalid = 0
    Abs = 1
    Acos = 2
    Asin = 3
    Atan = 4
    Ceiling = 5
    Cos = 6
    Exp = 7
    Floor = 8
    IEEERemainder = 9
    Log = 10
    Log10 = 11
    Pow = 12
    Round = 13
    Sign = 14
    Sin = 15
    Sqrt = 16
    Tan = 17
    Truncate = 18
    Max = 19
    Min = 20
    If = 21
    In = 22
    GetCurrentFrame = 23
    GroggyGaugeRate = 24
    MaxHpCapGaugeValue = 25
    GetHPRate = 26
    GetBossAIPhase = 27
    GetHPInteger = 28
    GetCurrentBehavior = 29
    IsReloading = 30
    HasCrowdControl = 31
    GetActiveParts = 32
    HasLogicEffectTemplate = 33
    StatGaugeRate = 34
    GetFormIndex = 35

class UnaryExpressionType(IntEnum):
    Not = 0
    Negate = 1
    BitwiseNot = 2

class ValueType(IntEnum):
    Integer = 0
    String = 1
    DateTime = 2
    Float = 3
    Boolean = 4

class EquipSlot(IntEnum):
    None_ = 0
    Weapon = 1
    Helmet = 2
    Armor = 3
    Shoes = 4
    Accessory = 5

class CompareOperator(IntEnum):
    Less = 0
    LessOrEqual = 1
    Equal = 2
    GreatorOrEqual = 3
    Greator = 4
    NotEqual = 5

class TimeSpanAccuracyType(IntEnum):
    Seconds = 0
    MillisecondThreeDigit = 1

class ActionProgress(IntEnum):
    None_ = 0
    Running = 1
    Finished = 2

class ActionState(IntEnum):
    Default = 0
    Phase01 = 1
    Phase02 = 2
    Phase03 = 3
    Phase04 = 4
    Phase05 = 5
    Phase06 = 6
    Phase07 = 7
    Phase08 = 8
    Phase09 = 9
    None_ = 10

class TSAInteractionState(IntEnum):
    NotInteracting = 0
    Interacting = 1
    TSADying = 2

class LogicEffectEndCondition(IntEnum):
    None_ = 0
    Duration = 1
    ReloadCount = 2
    AmmoCount = 3
    AmmoHit = 4
    UseExSkillCount = 5

class ObstacleState(IntEnum):
    Pre = 0
    Idle = 1
    Destroy = 2
    Retreat = 3
    Remain = 4
    Remove = 5

class TargetSortOrder(IntEnum):
    None_ = 0
    Highest = 1
    Lowest = 2
    Random = 3

class BattleEntityType(IntEnum):
    None_ = 0
    Character = 1
    SkillActor = 2
    Obstacle = 3
    Point = 4
    Projectile = 5
    EffectArea = 6
    Supporter = 7
    BattleItem = 8

class BehaviorType(IntEnum):
    None_ = 0
    NormalAttack01 = 1
    NormalAttack02 = 2
    NormalAttack03 = 3
    NormalAttack04 = 4
    NormalAttack05 = 5
    NormalAttack06 = 6
    NormalAttack07 = 7
    NormalAttack08 = 8
    NormalAttack09 = 9
    NormalAttack10 = 10
    UseExSkill01 = 11
    UseExSkill02 = 12
    UseExSkill03 = 13
    UseExSkill04 = 14
    UseExSkill05 = 15
    UseExSkill06 = 16
    UseExSkill07 = 17
    UseExSkill08 = 18
    UseExSkill09 = 19
    UseExSkill10 = 20
    UsePublicSkill01 = 21
    UsePublicSkill02 = 22
    UsePublicSkill03 = 23
    UsePublicSkill04 = 24
    UsePublicSkill05 = 25
    UsePublicSkill06 = 26
    UsePublicSkill07 = 27
    UsePublicSkill08 = 28
    UsePublicSkill09 = 29
    UsePublicSkill10 = 30
    Dead = 31
    Dying = 32
    Retreat = 33
    EnterGround = 34
    TSSInteract = 35
    Idle = 36
    Stunned = 37
    Hit = 38
    Knockback = 39
    Panic = 40
    Paralysis = 41
    Emp = 42
    Purify = 43
    Groggy = 44
    GroggyDead = 45
    Frozen = 46
    Move = 47
    MoveToFormationBeacon = 48
    MoveLeft = 49
    MoveRight = 50
    MoveAttack = 51
    ReleaseFormConversion = 52
    Walk = 53
    Stop = 54
    Seek = 55
    Flee = 56
    Evade = 57
    Wander = 58
    SeekPosition = 59
    Feared = 60
    Airborn = 61
    Charmed = 62
    Pulling = 63
    Stasis = 64
    Following = 65
    MetamorphNormalAttack01 = 66

class HeroStatus(IntEnum):
    None_ = 0
    Dead = 1
    Dying = 2
    Exiled = 3
    Suppressed = 4
    Stasis = 5
    Knockback = 6
    Pulling = 7
    Airborn = 8
    Stoned = 9
    Stunned = 10
    Paralysis = 11
    Emp = 12
    Purify = 13
    Groggy = 14
    Hit = 15
    Frozen = 16
    Panic = 17
    Charmed = 18
    Fear = 19
    Polymorph = 20
    ForcedIdle = 21
    Taunted = 22
    ConcentratedTarget = 23
    Confusion = 24
    MindControlled = 25
    Silence = 26
    Blind = 27
    Entangle = 28
    Slow = 29
    Immortal = 30
    Indestructible = 31
    DisableNormalAttack = 32
    DisableExSkill = 33
    DisablePassiveSkill = 34
    DisablePublicSkill = 35
    ImmuneDamageAttack = 36
    ImmuneDamageAll = 37
    ImmuneDamageBySkillType = 38
    ImmuneDead = 39
    ImmuneStoned = 40
    ImmuneKnockback = 41
    ImmunePulling = 42
    ImmuneAirborn = 43
    ImmuneStunned = 44
    ImmuneCharmed = 45
    ImmuneFear = 46
    ImmunePolymorph = 47
    ImmuneForcedIdle = 48
    ImmuneMindControl = 49
    ImmuneSilence = 50
    ImmuneBlind = 51
    ImmuneParalysis = 52
    ImmuneEmp = 53
    ImmunePurify = 54
    ImmuneGroggy = 55
    ImmuneConcentratedTarget = 56
    ImmuneConfusion = 57
    ImmuneCrowdControl = 58
    ImmuneGroggyGaugeAdd = 59
    Rage = 60
    Untargetable = 61
    Metamorph = 62
    Thorns = 63
    All = 64

class HeroSummaryDetailFlag(IntEnum):
    None_ = 0
    BattleProperty = 1
    BattleStatistics = 2
    NumericLogs = 3
    StatSnapshot = 4
    Default = 5
    All = 6

class SkillActionType(IntEnum):
    None_ = 0
    NormalAttackSkill = 1
    TargetSkill = 2
    MultipleTargetSkill = 3
    ProjectileSkill = 4
    MultipleProjectileSkill = 5
    AreaSkill = 6
    MultipleAreaSkill = 7
    SummonObstacleSkill = 8
    SummonCharacterSkill = 9
    SummonBattleItem = 10
    TimelineSkill = 11
    PassiveSkill = 12

class ComparisonOperator(IntEnum):
    None_ = 0
    Equal = 1
    NotEqual = 2
    Less = 3
    LessOrEqual = 4
    Greater = 5
    GreaterOrEqual = 6

class SkillSlot(IntEnum):
    None_ = 0
    NormalAttack01 = 1
    NormalAttack02 = 2
    NormalAttack03 = 3
    NormalAttack04 = 4
    NormalAttack05 = 5
    NormalAttack06 = 6
    NormalAttack07 = 7
    NormalAttack08 = 8
    NormalAttack09 = 9
    NormalAttack10 = 10
    ExSkill01 = 11
    ExSkill02 = 12
    ExSkill03 = 13
    ExSkill04 = 14
    ExSkill05 = 15
    ExSkill06 = 16
    ExSkill07 = 17
    ExSkill08 = 18
    ExSkill09 = 19
    ExSkill10 = 20
    Passive01 = 21
    Passive02 = 22
    Passive03 = 23
    Passive04 = 24
    Passive05 = 25
    Passive06 = 26
    Passive07 = 27
    Passive08 = 28
    Passive09 = 29
    Passive10 = 30
    ExtraPassive01 = 31
    ExtraPassive02 = 32
    ExtraPassive03 = 33
    ExtraPassive04 = 34
    ExtraPassive05 = 35
    ExtraPassive06 = 36
    ExtraPassive07 = 37
    ExtraPassive08 = 38
    ExtraPassive09 = 39
    ExtraPassive10 = 40
    Support01 = 41
    Support02 = 42
    Support03 = 43
    Support04 = 44
    Support05 = 45
    Support06 = 46
    Support07 = 47
    Support08 = 48
    Support09 = 49
    Support10 = 50
    EnterBattleGround = 51
    LeaderSkill01 = 52
    LeaderSkill02 = 53
    LeaderSkill03 = 54
    LeaderSkill04 = 55
    LeaderSkill05 = 56
    LeaderSkill06 = 57
    LeaderSkill07 = 58
    LeaderSkill08 = 59
    LeaderSkill09 = 60
    LeaderSkill10 = 61
    Equipment01 = 62
    Equipment02 = 63
    Equipment03 = 64
    Equipment04 = 65
    Equipment05 = 66
    Equipment06 = 67
    Equipment07 = 68
    Equipment08 = 69
    Equipment09 = 70
    Equipment10 = 71
    PublicSkill01 = 72
    PublicSkill02 = 73
    PublicSkill03 = 74
    PublicSkill04 = 75
    PublicSkill05 = 76
    PublicSkill06 = 77
    PublicSkill07 = 78
    PublicSkill08 = 79
    PublicSkill09 = 80
    PublicSkill10 = 81
    GroupBuff01 = 82
    HexaBuff01 = 83
    EventBuff01 = 84
    EventBuff02 = 85
    EventBuff03 = 86
    MoveAttack01 = 87
    MetamorphNormalAttack = 88
    GroundPassive01 = 89
    GroundPassive02 = 90
    GroundPassive03 = 91
    GroundPassive04 = 92
    GroundPassive05 = 93
    GroundPassive06 = 94
    GroundPassive07 = 95
    GroundPassive08 = 96
    GroundPassive09 = 97
    GroundPassive10 = 98
    HiddenPassive01 = 99
    HiddenPassive02 = 100
    HiddenPassive03 = 101
    HiddenPassive04 = 102
    HiddenPassive05 = 103
    HiddenPassive06 = 104
    HiddenPassive07 = 105
    HiddenPassive08 = 106
    HiddenPassive09 = 107
    HiddenPassive10 = 108
    Count = 109

class ComparisonOperator(IntEnum):
    Equal = 0
    NotEqual = 1
    Less = 2
    LessOrEqual = 3
    Greater = 4
    GreaterOrEqual = 5

class CheckConditionOperator(IntEnum):
    And = 0
    Or = 1

class BaseEntityType(IntEnum):
    Caster = 0
    Target = 1

class BattleTypes(IntEnum):
    None_ = 0
    Adventure = 1
    ScenarioMode = 2
    WeekDungeonChaserA = 3
    WeekDungeonBlood = 4
    WeekDungeonChaserB = 5
    WeekDungeonChaserC = 6
    WeekDungeonFindGift = 7
    EventContent = 8
    TutorialAdventure = 9
    Profiling = 10
    SingleRaid = 11
    MultiRaid = 12
    PracticeRaid = 13
    EliminateRaid = 14
    MultiFloorRaid = 15
    MinigameDefense = 16
    Arena = 17
    TimeAttack = 18
    SchoolDungeonA = 19
    SchoolDungeonB = 20
    SchoolDungeonC = 21
    WorldRaid = 22
    Conquest = 23
    FieldStory = 24
    FieldContent = 25
    PvE = 26
    WeekDungeon = 27
    SchoolDungeon = 28
    Raid = 29
    PvP = 30
    All = 31

class IncludeType(IntEnum):
    None_ = 0
    Include = 1
    Exclude = 2

class HPRateConstraintType(IntEnum):
    None_ = 0
    HPOver = 1
    HPUnder = 2

class ChangeSkillCardCostBaseType(IntEnum):
    Target = 0
    Caster = 1
    None_ = 2

class DamageByHitRemoveCondition(IntEnum):
    None_ = 0
    HpRateOver = 1
    HpRateUnder = 2
    TriggerCountOver = 3

class DamageByHitTriggerType(IntEnum):
    None_ = 0
    Damaged = 1
    Healed = 2

class DamageOverTimeRemoveCondition(IntEnum):
    None_ = 0
    HpRateOver = 1
    HpRateUnder = 2

class GaugeChargeConditionType(IntEnum):
    None_ = 0
    Period = 1
    UseSkill = 2

class HealByHitRemoveCondition(IntEnum):
    None_ = 0
    HpRateOver = 1
    HpRateUnder = 2
    TriggerCountOver = 3

class HealByHitTriggerType(IntEnum):
    None_ = 0
    Damaged = 1
    Healed = 2

class SkillCardCopyEndCondition(IntEnum):
    TriggerCount = 0
    None_ = 1

class NormalAttackPhaseName(IntEnum):
    AttackEnter = 0
    Reload = 1
    AttackStart = 2
    AttackIng = 3
    AttackBurstDelay = 4
    AttackFinish = 5
    MountWeapon = 6
    UnmountWeapon = 7
    SearchNewTarget = 8
    ExitNormalAttack = 9

class NormalAttackCondition(IntEnum):
    None_ = 0
    IsWeaponMounted = 1
    MoveEndRequired = 2
    TargetNotAvailable = 3
    ForceMoveCommandExists = 4
    BulletEmpty = 5
    BurstRoundOver = 6
    PublicSkillEnabled = 7
    FormConversionRequired = 8
    IsOrderByRandom = 9

class PassiveTriggerEvent(IntEnum):
    None_ = 0
    BattleEntity_NormalAttack = 1
    BattleEntity_UseSkillStart = 2
    BattleEntity_Attack = 3
    BattleEntity_Damaged = 4
    BattleEntity_Polling = 5
    BattleEntity_Heal = 6
    BattleEntity_Healed = 7
    BattleEntity_Dying = 8
    BattleEntity_Attacked = 9
    BattleEntity_Dodged = 10
    BattleEntity_AttackCritical = 11
    BattleEntity_Died = 12
    BattleEntity_KillEnemy = 13
    BattleEntity_Reload = 14
    BattleEntity_UseSkillEnd = 15
    BattleEntity_AddLogicEffectTemplate = 16
    BattleEntity_CoverStart = 17
    BattleEntity_CoverEnd = 18
    BattleEntity_DamageHit = 19
    BattleEntity_RemoveLogicEffectTemplate = 20
    BattleEntity_AddLogicEffectCategory = 21
    BattleEntity_AddLogicEffectGroupId = 22
    BattleEntity_RemoveLogicEffectGroupId = 23
    BattleEntity_KillAlly = 24
    BattleEntity_CountLogicEffectCategory = 25
    BattleEntity_UseExSkillCost = 26
    BattleEntity_AppliedLogicEffectCategory = 27
    BattleEntity_AppliedLogicEffectGroupId = 28
    BattleEntity_AppliedLogicEffectTemplate = 29
    BattleEntity_AppliedLogicEffectData = 30
    Immediate = 31
    Battle_Periodic = 32
    Battle_Polling = 33
    BattleEntityState_OnOff = 34
    BattleEntityState_NotMoving = 35
    BattleEntityState_Reloading = 36
    BattleEntityState_Moving = 37

class SkillLogicType(IntEnum):
    None_ = 0
    Active = 1
    Passive = 2
    Manual = 3

class SameAuraCheckCondition(IntEnum):
    None_ = 0
    SameInvokerEntityId = 1
    SameInvokerTeam = 2
    SameSkillId = 3
    SameSkillEntityName = 4
    All = 5

class BarrierShape(IntEnum):
    Circle = 0
    Square = 1

class BeamPhase(IntEnum):
    Expansion = 0
    Keeping = 1
    Extinction = 2

class OverLimitBehavior(IntEnum):
    None_ = 0
    Kill = 1
    Retreat = 2
    OverLimitAbility = 3
    ApplyAbilityAndRemoveFromGroup = 4

class BounceConditionCheckTiming(IntEnum):
    Defualt = 0
    AfterHitAbilities = 1
    AfterFixedDelay = 2

class NontargetBounceCondition(IntEnum):
    None_ = 0
    Obstacle = 1
    Boss = 2
    Shield = 3

class HighlightOption(IntEnum):
    None_ = 0
    Highlight = 1
    HighlightAndFactor = 2

class TransformDecideTiming(IntEnum):
    SkillStart = 0
    EntitySpawn = 1

class AreaTransformTypes(IntEnum):
    None_ = 0
    RadiusIncrement = 1
    RadiusDecrement = 2
    ObbCenterIncrement = 3
    ObbCenterDecrement = 4
    FanClockWise = 5
    FanCounterClockWise = 6
    FanClockwiseRound = 7
    FanCounterClockwiseRound = 8

class ForceMoveType(IntEnum):
    None_ = 0
    ToTarget = 1
    FromTarget = 2
    EntityDirection = 3
    TeamDirection = 4
    InvokerDirection = 5

class ModifierCheckTarget(IntEnum):
    Caster = 0
    Target = 1
    CasterAlly = 2
    CasterEnemy = 3
    All = 4
    CasterAllyExceptCaster = 5

class BattleLogicState(IntEnum):
    None_ = 0
    Preparing = 1
    InProgress = 2
    Finished = 3
    Paused = 4

class BattleEndType(IntEnum):
    None_ = 0
    AllNearlyDead = 1
    TimeOut = 2
    EscortFailed = 3
    Clear = 4

class AttackLogicEffectType(IntEnum):
    Damage = 0
    DeadlyAttack = 1
    TransferredDamage = 2
    DamageOverTime = 3
    ChangeDamageOverTime = 4
    DamageByHit = 5
    ExtraStatDamage = 6
    AccumulateDamage = 7
    MaxHPCapGauge = 8

class HitResultTypes(IntEnum):
    None_ = 0
    NormalHit = 1
    CriticalHit = 2
    Block = 3
    Dodge = 4
    Immune = 5
    All = 6

class ComparisonOperator(IntEnum):
    Equal = 0
    NotEqual = 1
    Less = 2
    LessOrEqual = 3
    Greater = 4
    GreaterOrEqual = 5

class Side(IntEnum):
    Default = 0
    Left = 1
    Right = 2

class PlayStartPointType(IntEnum):
    Start = 0
    LoopStart = 1

class PlayEndPointType(IntEnum):
    End = 0
    LoopEnd = 1

class AllClearCondition(IntEnum):
    LastWaveClear = 0
    AllSpawnedEnemyDied = 1

class ShapeType(IntEnum):
    Rect = 0
    Circle = 1

class TargetType(IntEnum):
    Player = 0
    Enemy = 1
    Anyone = 2
    EnemySpawnTemplateId = 3
    PlayerAll = 4
    PlayerSpawnTemplateId = 5

class TriggerType(IntEnum):
    Enter = 0
    Stay = 1
    Exit = 2

class ShapeType(IntEnum):
    Rect = 0
    Circle = 1

class TargetType(IntEnum):
    Player = 0
    Enemy = 1
    Anyone = 2
    EnemySpawnTemplateId = 3
    PlayerAll = 4
    PlayerSpawnTemplateId = 5

class TriggerType(IntEnum):
    Enter = 0
    Stay = 1
    Exit = 2

class DeadCheckType(IntEnum):
    SpawnedCharacterDead = 0
    All = 1

class CompareType(IntEnum):
    LessThanOrEqual = 0
    GreaterThanOrEqual = 1

class OperatorType(IntEnum):
    AND = 0
    OR = 1

class UpdateEvent(IntEnum):
    New = 0
    Modify = 1
    Dispell = 2
    Remove = 3

class SkillCardState(IntEnum):
    None_ = 0
    InHand = 1
    InDeck = 2
    Used = 3
    Cast = 4
    InputReceived = 5
    CoolTime = 6
    CoolTimeComplete = 7
    Disabled = 8
    Waiting = 9
    Switched = 10

class GroupStatTypes(IntEnum):
    None_ = 0
    MaxHitPoint = 1
    CurrentHitPoint = 2
    PhysicalAttack = 3
    AliveHeroes = 4
    DeadHeroes = 5
    KillCount = 6
    BestCondition = 7
    GradeSum = 8
    LevelSum = 9
    CardCastCount = 10

class GroupTag(IntEnum):
    None_ = 0
    Group01 = 1
    Group02 = 2
    Group03 = 3
    Group04 = 4
    Group05 = 5
    Group06 = 6
    Group07 = 7
    Group08 = 8
    Group09 = 9
    Group10 = 10
    Group11 = 11
    Group12 = 12
    Group13 = 13
    Group14 = 14
    Group15 = 15
    Group16 = 16

class BattleLogActionType(IntEnum):
    None_ = 0
    Given = 1
    Taken = 2

class BattleLogCategory(IntEnum):
    None_ = 0
    Damage = 1
    Heal = 2

class BattleLogSourceType(IntEnum):
    None_ = 0
    Normal = 1
    Ex = 2
    Public = 3
    Passive = 4
    ExtraPassive = 5
    Etc = 6

class CardStatus(IntEnum):
    None_ = 0
    NotCasted = 1
    Castable = 2
    Casting = 3
    Applied = 4
    Cancelled = 5
    Fizzled = 6

class SteeringTypes(IntEnum):
    None_ = 0
    Seek = 1
    Flee = 2
    Forward = 3
    Backward = 4
    Wander = 5
    Separation = 6
    Alignment = 7
    Cohesion = 8
    AvoidObstacle = 9
    AvoidWall = 10
    Pursuit = 11
    Evade = 12
    Arrive = 13
    InterPose = 14
    Breakthrough = 15
    Stop = 16
    All = 17

class BehaviorResult(IntEnum):
    Failure = 0
    Success = 1
    Running = 2

class TriggerType(IntEnum):
    None_ = 0
    TargetEnter = 1
    TargetExit = 2
    AuraDuration = 3

class ConditionType(IntEnum):
    None_ = 0
    LogicEffectTemplate = 1
    LogicEffectGroupId = 2
    LogicEffectCategory = 3

class CommandType(IntEnum):
    None_ = 0
    AuraCancel = 1
    SpawnSkillEntity = 2

class AbilityActivateTag(IntEnum):
    None_ = 0
    ActionStart = 1
    ActionRelease = 2
    ActionEnd = 3

class TriggerType(IntEnum):
    None_ = 0
    TargetEnter = 1
    TargetExit = 2
    AuraDuration = 3

class ConditionType(IntEnum):
    None_ = 0
    LogicEffectTemplate = 1
    LogicEffectGroupId = 2
    LogicEffectCategory = 3

class CommandType(IntEnum):
    None_ = 0
    AuraCancel = 1
    SpawnSkillEntity = 2

class AutoUseConditionType(IntEnum):
    None_ = 0
    Interval = 1
    HpUnder = 2
    HasLogicEffectCategory = 3
    AmmoCountUnder = 4
    OnAttackIng = 5
    KillTarget = 6
    GainBattleItem = 7
    HitLogicEffectCategory = 8
    HpOver = 9
    CriticalAttack = 10
    CriticalAttacked = 11
    Healed = 12
    Dodged = 13
    Blocked = 14
    CoverTime = 15
    UseSkill = 16
    HitLogicEffectGroupId = 17
    HitLogicEffectTemplateId = 18
    Attacked = 19
    RemoveLogicEffectTemplateId = 20

class ExtraStatType(IntEnum):
    None_ = 0
    InvokerCurrentHP = 1
    TargetCurrentHP = 2
    InvokerMaxHP = 3
    TargetMaxHP = 4
    InvokerLostHP = 5
    TargetLostHP = 6
    InvokerMaxHPCapGaugeValue = 7
    TargetMaxHPCapGaugeValue = 8
    InvokerDefaultDefense = 9
    TargetDefaultDefense = 10
    InvokerCurrentDefense = 11
    TargetCurrentDefense = 12

class MovingAreaOptions(IntEnum):
    None_ = 0
    FixedAim = 1
    CheckSpawnPositionOutOfMovingArea = 2

class ProjectileTypes(IntEnum):
    None_ = 0
    TargetCharacter = 1
    TargetPosition = 2
    Nontarget = 3
    Max = 4

class DamageCriticalType(IntEnum):
    None_ = 0
    Never = 1
    Check = 2
    Always = 3

class LifeGainType(IntEnum):
    None_ = 0
    Heal = 1
    Recover = 2

class SkillApplyType(IntEnum):
    None_ = 0
    Direct = 1
    Hitscan = 2
    AlwaysBlocked = 3

class SkillProperty(IntEnum):
    None_ = 0
    ReuseCoolTime = 1
    CoolTime = 2
    CoolTimeAndStartCoolTime = 3
    ProjectileRange = 4
    TargetingRange = 5
    Invalid = 6

class SkillToTargetDistributeType(IntEnum):
    None_ = 0
    EachToEachTarget = 1
    AllToOneTarget = 2
    OneToAllTarget = 3

class SkillType(IntEnum):
    None_ = 0
    Ex = 1
    Passive = 2
    Leader = 3
    Normal = 4
    ExtraPassive = 5
    Public = 6
    GroupBuff = 7
    HexaBuff = 8
    EventBuff = 9
    TimeAttackGeasPassive = 10
    HiddenPassive = 11

class EntitySpawnRule(IntEnum):
    SpawnAll = 0
    SpawnOnlyOne = 1
    SpawnOnlyOnePerFrame = 2

class EntitySpawnCondition(IntEnum):
    None_ = 0
    HPRateUnder = 1
    HPRateOver = 2
    IncludeLogicEffectTemplateId = 3
    ExcludeLogicEffectTemplateId = 4
    Rate = 5
    IncludeArmorType = 6
    ExcludeArmorType = 7
    SkillLevel = 8
    IncludeTag = 9
    ExcludeTag = 10

class EntitySpawnConditionCheckTarget(IntEnum):
    Caster = 0
    Target = 1
    SpawnEntityTarget = 2

class SpawnDirectionTypes(IntEnum):
    None_ = 0
    Invoker = 1
    Input = 2
    ToTarget = 3
    AllyToEnemy = 4
    EnemyToAlly = 5
    AliveAllyCenter = 6
    AliveEnemyCenter = 7
    WorldPosition = 8
    CasterToTarget = 9
    TargetToCaster = 10

class SpawnPositionTypes(IntEnum):
    None_ = 0
    Invoker = 1
    InputPosition = 2
    InputBattleEntity = 3
    AliveAllyCenter = 4
    AliveEnemyCenter = 5
    GroundCenter = 6
    BattleEntity = 7
    WorldPosition = 8
    SkillCommandSelectedTarget = 9
    SkillCommandSelectedPosition = 10
    ProcedureTriggeredTarget = 11
    ProcedureTriggeredPosition = 12

class AliveState(IntEnum):
    None_ = 0
    Alive = 1
    Dying = 2
    Dead = 3
    AliveOrDying = 4
    AliveOrDead = 5
    DeadOrDying = 6
    All = 7

class CoverState(IntEnum):
    None_ = 0
    NotCovered = 1
    Covered = 2

class TargetEntityType(IntEnum):
    None_ = 0
    Character = 1
    Character_Except_TSS = 2
    TSS = 3
    Supporter = 4
    Obstacle = 5

class TargetingType(IntEnum):
    None_ = 0
    Target = 1
    Position = 2

class TargetSideId(IntEnum):
    None_ = 0
    Self = 1
    Ally_Except_Self = 2
    Enemy = 3
    Neutral = 4
    Ally = 5
    Self_or_Enemy = 6
    Self_or_Neutral = 7
    Ally_or_Enemy = 8
    Ally_or_Neutral = 9
    Enemy_or_Neutral = 10
    All_Except_Self = 11
    ALL = 12

class TargetSortCriteria(IntEnum):
    None_ = 0
    CurrentHP = 1
    MaxHP = 2
    HPRate = 3
    Distance = 4
    AttackPower = 5
    DefensePower = 6
    BuffCount = 7
    DebuffCount = 8
    CrowdControlCount = 9
    LogicEffectTemplateCount = 10
    Stat = 11
    SummonedTime = 12
    All = 13

class PassiveSkillTargetType(IntEnum):
    None_ = 0
    UseTriggerSource = 1
    UseTriggerTarget = 2
    UseSkillEntityTargetingRule = 3
    UseTriggerTargetExceptSelf = 4

class ManualSkillTypes(IntEnum):
    None_ = 0
    GroupBuff = 1
    StrategyBuff = 2
    EventBuff = 3

class AccumulateCheckType(IntEnum):
    Damage = 0
    Heal = 1

class ExecuteCondition(IntEnum):
    OverAccumulateAmount = 0
    OverDuration = 1

class GaugeTraceType(IntEnum):
    None_ = 0
    HPRate = 1

class ApplyType(IntEnum):
    Default = 0
    IncludeImmune = 1

class DamageSourceType(IntEnum):
    None_ = 0
    DamageOverTime = 1
    ChangeDamageOverTime = 2
    DamageByHit = 3
    ExtraStatDamage = 4

class StatEvalType(IntEnum):
    None_ = 0
    Base = 1
    Coefficient = 2

class ResolvePriority(IntEnum):
    Dispel = 0
    StatChange = 1
    LifeGain = 2
    StatusRemove = 3
    Normal = 4
    CrowdControlStatusAdd = 5
    StatusAdd = 6
    Damage = 7

class LogicEffectType(IntEnum):
    None_ = 0
    Damage = 1
    Heal = 2
    StatChange = 3
    StatusChange = 4
    KnockBack = 5
    StatusRemove = 6
    ModifyCoolTime = 7
    Revive = 8

class ConquestCommandType(IntEnum):
    None_ = 0
    PropAnimation = 1
    Operator = 2
    TileConquer = 3
    TileUpgrade = 4
    BossOpen = 5
    StepComplete = 6
    MassErosion = 7
    Erosion = 8
    ErosionRemove = 9
    StepOpen = 10
    BossClear = 11
    HideConquestUI = 12
    ShowConquestUI = 13
    HideHexaUI = 14
    ShowHexaUI = 15
    StepObjectComplete = 16
    CameraSetting = 17
    PropAnimationHold = 18
    CheckTileErosion = 19
    PlayMapEnterScenario = 20
    UnexpectedEvent = 21
    TileConquerReward = 22

class ConquestConditionType(IntEnum):
    None_ = 0
    TileFriendlyTerritory = 1
    StepTileComplete = 2
    StepBossDead = 3
    StepOpen = 4
    DeadUnitLeader = 5
    TileUniqueId = 6
    UnitOpen = 7
    StepObjectComplete = 8

class ConquestDisplayType(IntEnum):
    None_ = 0
    TileConquered = 1
    TileUpgraded = 2
    UnexpectedEvent = 3
    BossOpen = 4
    PropAnimation = 5
    PropAnimationAndBlock = 6
    PropAnimationHoldAndPlay = 7
    Operator = 8
    StepComplete = 9
    MassErosion = 10
    Erosion = 11
    ErosionRemove = 12
    CheckTileErosion = 13
    StepOpen = 14
    BossClear = 15
    HideConquestUI = 16
    ShowConquestUI = 17
    HideHexaUI = 18
    ShowHexaUI = 19
    StepObjectComplete = 20
    CameraSetting = 21
    PlayMapEnterScenario = 22
    ShowTileConquerReward = 23

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1

class CommonEventType(IntEnum):
    Invalid = 0
    TileConquer = 1
    TileUpgrade = 2
    BossOpen = 3
    StepComplete = 4
    MassErosion = 5
    Erosion = 6
    ErosionRemove = 7
    UnexpectedEvent = 8
    TileConquerReward = 9

class ConquestTriggerType(IntEnum):
    None_ = 0
    TileConquer = 1
    TileUpgrade = 2
    MapEnter = 3
    SyncState = 4
    AcquireCalculateReward = 5
    UnexpectedEvent = 6
    MassErosion = 7
    MassErosionEnd = 8
    TileErosion = 9
    TileErosionEnd = 10

class ClearCondition(IntEnum):
    EnemyAllDead = 0
    BossKill = 1

class HexaTileMapCommandType(IntEnum):
    PlayScenario = 0
    SpawnUnitInTile = 1
    SpawnStrategyObjectInTile = 2

class HexaTileMapConditionType(IntEnum):
    PlayerTurnStart = 0
    EnemyTurnStart = 1
    UnitDead = 2
    PlayerArrivedInTileFirstTime = 3

class HexaDisplayType(IntEnum):
    None_ = 0
    EndBattle = 1
    PlayScenario = 2
    SpawnUnitFromUniqueId = 3
    StatBuff = 4
    DieUnit = 5
    HideStrategy = 6
    SpawnUnit = 7
    SpawnStrategy = 8
    SpawnTile = 9
    HideTile = 10
    ClearFogOfWar = 11
    MoveUnit = 12
    WarpUnit = 13
    SetTileMovablity = 14
    WarpUnitFromHideTile = 15
    BossExile = 16

class MultipleConditionCheckType(IntEnum):
    And = 0
    Or = 1

class HexaConditionType(IntEnum):
    None_ = 0
    StartCampaign = 1
    TurnBeginEnd = 2
    UnitDead = 3
    PlayerArrivedInTileFirstTime = 4
    AnyEnemyDead = 5
    EveryTurn = 6
    EnemyArrivedInTileFirstTime = 7
    SpecificEnemyArrivedInTileFirstTime = 8

class HexaCommandType(IntEnum):
    None_ = 0
    UnitSpawn = 1
    PlayScenario = 2
    StrategySpawn = 3
    TileSpawn = 4
    TileHide = 5
    EndBattle = 6
    WaitTurn = 7
    StrategyHide = 8
    UnitDie = 9
    UnitMove = 10
    CharacterEmoji = 11

class PatchType(IntEnum):
    Asset = 0
    Table = 1
    Media = 2

class PatchDownloadType(IntEnum):
    FULL = 0
    SPLIT = 1
    NONE = 2

class PatchStatus(IntEnum):
    None_ = 0
    ClientNetworkUnreachable = 1
    PatchServerNotRespond = 2
    InvalidUri = 3
    HashFileNotExists = 4
    PatchRequired = 5
    PatchUnnecessary = 6
    DownloadCatalogHashFailed = 7
    DownloadCatalogFailed = 8
    DownloadCatalogSuccess = 9
    NoNeedToDownloadCatalog = 10
    DownloadBundleFailed = 11
    DownloadingPatch = 12
    DownloadComplete = 13
    DownloadStart = 14
    ValidatingPatch = 15
    ValidateFailed = 16
    ProcessComplete = 17
    DiskFull = 18

class DownloadBundleStatus(IntEnum):
    None_ = 0
    DownloadAddressableCatalogFailed = 1
    DownloadCatalogSuccess = 2
    DownloadMediaCatalogFailed = 3
    DownloadTableCatalogFailed = 4
    DownloadAssetCatalogFailed = 5
    DeviceNotEnoughFreeSpace = 6
    DownloadBundleFailed = 7
    DownloadSuccess = 8
    DownloadCRCFailed = 9

class DLAssetType(IntEnum):
    Bundle = 0
    Table = 1
    Media = 2
    Dir = 3

class ConquestEventObjectType(IntEnum):
    None_ = 0
    UnexpectedEnemy = 1
    TreasureBox = 2
    Erosion = 3
    End = 4

class ServerStatus(IntEnum):
    None_ = 0
    Open = 1
    WhiteListOnly = 2
    Error = 3
    Maintenance = 4

class PopupType(IntEnum):
    Always = 0
    OneTime = 1

class BannerDisplayType(IntEnum):
    Lobby = 0
    Gacha = 1

class GuidePopupType(IntEnum):
    SurveyGuidePopup = 0
    GuidePopup = 1

class CraftType(IntEnum):
    Craft = 0
    ShiftingCraft = 1

class CharacterElephBonusType(IntEnum):
    None_ = 0
    Pickup = 1
    Bonus = 2

class LayerButtonType(IntEnum):
    InnerButton = 0
    Lobby_StudentRecord = 1
    Lobby_Social = 2

class ReddotType(IntEnum):
    Off = 0
    Yellow = 1
    Red = 2

class EmblemFromUIType(IntEnum):
    None_ = 0
    ListPopup_Select = 1
    ListPopup_Element = 2
    InfoOnly = 3
    ContentsDisplay = 4

class AnimatorState(IntEnum):
    Idle = 0
    Attack = 1
    Move = 2
    Die = 3
    PublicSkill1 = 4
    PublicSkill2 = 5
    PublicSkill3 = 6
    Delay = 7
    None_ = 8

class CharacterState(IntEnum):
    Idle = 0
    Move = 1
    Attack = 2
    Die = 3
    PublicSkill1 = 4
    PublicSkill2 = 5
    PublicSkill3 = 6
    Delay = 7

class StatType(IntEnum):
    AttackPower = 0
    DefensePower = 1
    MoveSpeed = 2
    AttackRange = 3
    CriticalRate = 4
    CriticalDamageRate = 5
    ShotTime = 6
    Hp = 7
    LifeStealRate = 8
    EvasionRate = 9

class MGSGameMode(IntEnum):
    Normal = 0
    Hard = 1
    Free = 2

class GameSpeedType(IntEnum):
    NormalSpeed = 0
    FastSpeed = 1
    SlowSpeed = 2

class RaidDifficultyFilter(IntEnum):
    All = 0
    Normal = 1
    Hard = 2
    VeryHard = 3
    HardCore = 4
    Extreme = 5
    Insane = 6
    Torment = 7
    Lunatic = 8

class Mute(IntEnum):
    On = 0
    Off = 1

class SkillCutIn(IntEnum):
    Always = 0
    OnceADay = 1
    Never = 2

class RaidRetryCutScene(IntEnum):
    Always = 0
    Never = 1

class SupplyCard(IntEnum):
    Auto = 0
    Manual = 1

class Resolution(IntEnum):
    VeryHigh = 0
    High = 1
    Normal = 2
    Low = 3

class FPS(IntEnum):
    High = 0
    Normal = 1

class ToggleValue(IntEnum):
    On = 0
    Off = 1

class LeftUIValue(IntEnum):
    Right = 0
    Left = 1

class DrawcallMode(IntEnum):
    SRPBatcher = 0
    DynamicBatching = 1
    Off = 2

class AntiAliasing(IntEnum):
    Off = 0
    Low = 1
    High = 2

class ShaderQuality(IntEnum):
    Normal = 0
    Low = 1

class MemoryLobbyAni(IntEnum):
    Always = 0
    OnceADay = 1
    Never = 2

class RandomLobby(IntEnum):
    Always = 0
    OnceADay = 1
    Never = 2

class OptionTab(IntEnum):
    None_ = 0
    Game = 1
    Graphic = 2
    Sound = 3
    Notice = 4
    Title = 5

class MinigameNoteScale(IntEnum):
    Big = 0
    Medium = 1
    Small = 2

class MinigameNoteColor(IntEnum):
    Set1 = 0
    Set2 = 1

class VoiceLang(IntEnum):
    CN = 0
    JP = 1

class OptionType(IntEnum):
    None_ = 0
    BGM = 1
    FXSound = 2
    VoiceSound = 3
    SkillCutIn = 4
    SupplyCard = 5
    Resolution = 6
    FPS = 7
    MemoryLobbyAni = 8
    RandomLobby = 9
    AllowSamePersonality = 10
    NotificationApCharge = 11
    NotificationCafeCharge = 12
    ArenaBattleSkip = 13
    LetterBoxInBattle = 14
    MemoryClearByUI = 15
    RaidRetryCutScene = 16
    TitleVideoAudio = 17
    VoiceSubtitle = 18
    HideBuffIconsPassive = 19
    HideBuffIconsSpecialStudentExtraPassive = 20
    EXSkillPinPointMyUnit = 21
    EXSkillPinPointAllyEtc = 22
    LeftUI = 23
    ShowFurnitureBubbles = 24
    DrawcallMode = 25
    AllowPostProcess = 26
    AntiAliasing = 27
    GraphicsDesc = 28
    VoiceLanguage = 29
    NoteSpeed = 30
    NoteTiming = 31
    NoteColor = 32
    NoteScale = 33
    Fever = 34
    NoteSFX = 35

class CommandType(IntEnum):
    Play = 0
    Stop = 1

class AudioSourceStates(IntEnum):
    None_ = 0
    Delay = 1
    Playing = 2
    FadeOut = 3

class EffectPositionSource(IntEnum):
    None_ = 0
    Invoker = 1
    Target = 2
    Position = 3
    AllyBack = 4
    EnemyBack = 5
    WorldPosition = 6
    ProjectileEntity = 7
    ProjectileDestination = 8

class AlignDirection(IntEnum):
    None_ = 0
    EffectBone = 1
    Target = 2
    Caster = 3
    TargetToCaster = 4
    CasterToTarget = 5
    EntityDirection = 6

class FacingTargetType(IntEnum):
    Trajectory = 0
    Target = 1
    InitDirection = 2

class BattleSceneState(IntEnum):
    None_ = 0
    Preparing = 1
    InBattle = 2
    Ending = 3
    ShowResult = 4
    Paused = 5
    SkillTargetSelect = 6
    ShowTargetPopup = 7
    AskContinue = 8
    ShowUltimate = 9
    Replicate = 10
    WaitPeer = 11
    WaitSyncTurn = 12

class BattleResultSkipType(IntEnum):
    None_ = 0
    SkipPopup = 1
    SkipTimeline = 2

class MinigameSFXType(IntEnum):
    EmptyHit = 0
    SingleHit = 1
    DoubleHit = 2
    FlickHit = 3
    LongHit = 4

class Trigger(IntEnum):
    OnClick = 0
    OnHover = 1
    OnPress = 2
    OnHoverTrue = 3
    OnHoverFalse = 4
    OnPressTrue = 5
    OnPressFalse = 6
    OnActivate = 7
    OnActivateTrue = 8
    OnActivateFalse = 9
    OnDoubleClick = 10
    OnSelect = 11
    OnSelectTrue = 12
    OnSelectFalse = 13
    Manual = 14

class Direction(IntEnum):
    Reverse = 0
    Toggle = 1
    Forward = 2

class EnableCondition(IntEnum):
    DoNothing = 0
    EnableThenPlay = 1
    IgnoreDisabledState = 2

class DisableCondition(IntEnum):
    DisableAfterReverse = 0
    DoNotDisable = 1
    DisableAfterForward = 2


def dump_GroundVector3(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Y": convert_float(excel_instance.Y(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_GroundGridFlatNew(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "StartX": convert_float(excel_instance.StartX(), password),
        "StartY": convert_float(excel_instance.StartY(), password),
        "Gap": convert_float(excel_instance.Gap(), password),
        "NodesLength": convert_int(excel_instance.NodesLength(), password),
        "Version": convert_string(excel_instance.Version(), password),
    }

def dump_GroundNodeFlatNew(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "IsCanNotUseSkill": bool(excel_instance.IsCanNotUseSkill()),
                "NodeType": GroundNodeType(convert_int(excel_instance.NodeType(), password)).name,
        "OriginalNodeType": GroundNodeType(convert_int(excel_instance.OriginalNodeType(), password)).name,
    }

def dump_GroundVector3New(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Y": convert_float(excel_instance.Y(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_AcademyFavorScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ScheduleGroupId": convert_int(excel_instance.ScheduleGroupId(), password),
        "OrderInGroup": convert_int(excel_instance.OrderInGroup(), password),
        "Location": convert_string(excel_instance.Location(), password),
        "LocalizeScenarioId": convert_uint(excel_instance.LocalizeScenarioId(), password),
        "FavorRank": convert_int(excel_instance.FavorRank(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmount(), password),
        "ScenarioSriptGroupId": convert_int(excel_instance.ScenarioSriptGroupId(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_AcademyLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPath(), password),
        "IconImagePath": convert_string(excel_instance.IconImagePath(), password),
        "OpenConditionLength": convert_int(excel_instance.OpenConditionLength(), password),
        "OpenConditionCountLength": convert_int(excel_instance.OpenConditionCountLength(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "OpenTeacherRank": convert_int(excel_instance.OpenTeacherRank(), password),
    }

def dump_AcademyLocationRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Rank": convert_int(excel_instance.Rank(), password),
        "RankExp": convert_int(excel_instance.RankExp(), password),
        "TotalExp": convert_int(excel_instance.TotalExp(), password),
    }

def dump_AcademyMessanger1Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_int(excel_instance.MessageGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_int(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_int(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_int(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_int(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_int(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyMessanger2Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_int(excel_instance.MessageGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_int(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_int(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_int(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_int(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_int(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyMessanger3Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_int(excel_instance.MessageGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_int(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_int(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_int(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_int(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_int(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyMessangerExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_int(excel_instance.MessageGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MessageCondition": AcademyMessageConditions(convert_int(excel_instance.MessageCondition(), password)).name,
        "ConditionValue": convert_int(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_int(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_int(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_int(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_int(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": AcademyMessageTypes(convert_int(excel_instance.MessageType(), password)).name,
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
    }

def dump_AcademyRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Location": convert_string(excel_instance.Location(), password),
        "ScheduleGroupId": convert_int(excel_instance.ScheduleGroupId(), password),
        "OrderInGroup": convert_int(excel_instance.OrderInGroup(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "ProgressTexture": convert_string(excel_instance.ProgressTexture(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocationRank": convert_int(excel_instance.LocationRank(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmount(), password),
        "SecretStoneProb": convert_int(excel_instance.SecretStoneProb(), password),
        "ExtraFavorExp": convert_int(excel_instance.ExtraFavorExp(), password),
        "ExtraFavorExpProb": convert_int(excel_instance.ExtraFavorExpProb(), password),
        "ExtraRewardParcelTypeLength": convert_int(excel_instance.ExtraRewardParcelTypeLength(), password),
        "ExtraRewardParcelIdLength": convert_int(excel_instance.ExtraRewardParcelIdLength(), password),
        "ExtraRewardAmountLength": convert_int(excel_instance.ExtraRewardAmountLength(), password),
        "ExtraRewardProbLength": convert_int(excel_instance.ExtraRewardProbLength(), password),
        "IsExtraRewardDisplayedLength": convert_int(excel_instance.IsExtraRewardDisplayedLength(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_AcademyTicketExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocationRankSum": convert_int(excel_instance.LocationRankSum(), password),
        "ScheduleTicktetMax": convert_int(excel_instance.ScheduleTicktetMax(), password),
    }

def dump_AcademyZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocationId": convert_int(excel_instance.LocationId(), password),
        "LocationRankForUnlock": convert_int(excel_instance.LocationRankForUnlock(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StudentVisitProbLength": convert_int(excel_instance.StudentVisitProbLength(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
    }

def dump_AddressableBlackListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FolderPathLength": convert_int(excel_instance.FolderPathLength(), password),
        "ResourcePathLength": convert_int(excel_instance.ResourcePathLength(), password),
    }

def dump_AddressableWhiteListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FolderPathLength": convert_int(excel_instance.FolderPathLength(), password),
        "ResourcePathLength": convert_int(excel_instance.ResourcePathLength(), password),
    }

def dump_AnimationBlendTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataListLength": convert_int(excel_instance.DataListLength(), password),
    }

def dump_BlendData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Type": convert_int(excel_instance.Type(), password),
        "InfoListLength": convert_int(excel_instance.InfoListLength(), password),
    }

def dump_BlendInfo(excel_instance, password: bytes = b"") -> dict:
    return {
        "From": convert_int(excel_instance.From(), password),
        "To": convert_int(excel_instance.To(), password),
        "Blend": convert_float(excel_instance.Blend(), password),
    }

def dump_AnimatorDataTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataListLength": convert_int(excel_instance.DataListLength(), password),
    }

def dump_AnimatorData(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultStateName": convert_string(excel_instance.DefaultStateName(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "DataListLength": convert_int(excel_instance.DataListLength(), password),
    }

def dump_AniStateData(excel_instance, password: bytes = b"") -> dict:
    return {
        "StateName": convert_string(excel_instance.StateName(), password),
        "StatePrefix": convert_string(excel_instance.StatePrefix(), password),
        "StateNameWithPrefix": convert_string(excel_instance.StateNameWithPrefix(), password),
        "Tag": convert_string(excel_instance.Tag(), password),
        "SpeedParameterName": convert_string(excel_instance.SpeedParameterName(), password),
        "SpeedParamter": convert_float(excel_instance.SpeedParamter(), password),
        "StateSpeed": convert_float(excel_instance.StateSpeed(), password),
        "ClipName": convert_string(excel_instance.ClipName(), password),
        "Length": convert_float(excel_instance.Length(), password),
        "FrameRate": convert_float(excel_instance.FrameRate(), password),
        "IsLooping": bool(excel_instance.IsLooping()),
        "EventsLength": convert_int(excel_instance.EventsLength(), password),
    }

def dump_AniEventData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "Time": convert_float(excel_instance.Time(), password),
        "IntParam": convert_int(excel_instance.IntParam(), password),
        "FloatParam": convert_float(excel_instance.FloatParam(), password),
        "StringParam": convert_string(excel_instance.StringParam(), password),
    }

def dump_ArenaLevelSectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ArenaSeasonId": convert_int(excel_instance.ArenaSeasonId(), password),
        "StartLevel": convert_int(excel_instance.StartLevel(), password),
        "LastLevel": convert_int(excel_instance.LastLevel(), password),
        "UserCount": convert_int(excel_instance.UserCount(), password),
    }

def dump_ArenaMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "TerrainType": convert_int(excel_instance.TerrainType(), password),
        "TerrainTypeLocalizeKey": convert_string(excel_instance.TerrainTypeLocalizeKey(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "GroundGroupId": convert_int(excel_instance.GroundGroupId(), password),
        "GroundGroupNameLocalizeKey": convert_string(excel_instance.GroundGroupNameLocalizeKey(), password),
        "StartRank": convert_int(excel_instance.StartRank(), password),
        "EndRank": convert_int(excel_instance.EndRank(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
    }

def dump_ArenaNPCExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Rank": convert_int(excel_instance.Rank(), password),
        "NPCAccountLevel": convert_int(excel_instance.NPCAccountLevel(), password),
        "NPCLevel": convert_int(excel_instance.NPCLevel(), password),
        "NPCLevelDeviation": convert_int(excel_instance.NPCLevelDeviation(), password),
        "NPCStarGrade": convert_int(excel_instance.NPCStarGrade(), password),
        "ExceptionCharacterRaritiesLength": convert_int(excel_instance.ExceptionCharacterRaritiesLength(), password),
        "ExceptionMainCharacterIdsLength": convert_int(excel_instance.ExceptionMainCharacterIdsLength(), password),
        "ExceptionSupportCharacterIdsLength": convert_int(excel_instance.ExceptionSupportCharacterIdsLength(), password),
        "ExceptionTSSIdsLength": convert_int(excel_instance.ExceptionTSSIdsLength(), password),
    }

def dump_ArenaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ArenaRewardType": ArenaRewardType(convert_int(excel_instance.ArenaRewardType(), password)).name,
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "RankIconPath": convert_string(excel_instance.RankIconPath(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelUniqueIdLength": convert_int(excel_instance.RewardParcelUniqueIdLength(), password),
        "RewardParcelUniqueNameLength": convert_int(excel_instance.RewardParcelUniqueNameLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_ArenaSeasonCloseRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelUniqueIdLength": convert_int(excel_instance.RewardParcelUniqueIdLength(), password),
        "RewardParcelUniqueNameLength": convert_int(excel_instance.RewardParcelUniqueNameLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_ArenaSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDate(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDate(), password),
        "SeasonGroupLimit": convert_int(excel_instance.SeasonGroupLimit(), password),
        "PrevSeasonId": convert_int(excel_instance.PrevSeasonId(), password),
    }

def dump_BattleLevelFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiff(), password),
        "DamageRate": convert_int(excel_instance.DamageRate(), password),
    }

def dump_BossExternalBTExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ExternalBTId": convert_int(excel_instance.ExternalBTId(), password),
        "AIPhase": convert_int(excel_instance.AIPhase(), password),
        "ExternalBTNodeType": ExternalBTNodeType(convert_int(excel_instance.ExternalBTNodeType(), password)).name,
        "ExternalBTTrigger": ExternalBTTrigger(convert_int(excel_instance.ExternalBTTrigger(), password)).name,
        "TriggerArgument": convert_string(excel_instance.TriggerArgument(), password),
        "BehaviorRate": convert_int(excel_instance.BehaviorRate(), password),
        "ExternalBehavior": ExternalBehavior(convert_int(excel_instance.ExternalBehavior(), password)).name,
        "BehaviorArgument": convert_string(excel_instance.BehaviorArgument(), password),
    }

def dump_BossPhaseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "AIPhase": convert_int(excel_instance.AIPhase(), password),
        "NormalAttackSkillUniqueName": convert_string(excel_instance.NormalAttackSkillUniqueName(), password),
        "UseExSkillLength": convert_int(excel_instance.UseExSkillLength(), password),
    }

def dump_BuffParticleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "UniqueName": convert_string(excel_instance.UniqueName(), password),
        "BuffType": convert_string(excel_instance.BuffType(), password),
        "BuffName": convert_string(excel_instance.BuffName(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePath(), password),
    }

def dump_BulletArmorDamageFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupId(), password),
        "BulletType": BulletType(convert_int(excel_instance.BulletType(), password)).name,
        "ArmorType": ArmorType(convert_int(excel_instance.ArmorType(), password)).name,
        "DamageRate": convert_int(excel_instance.DamageRate(), password),
        "DamageAttribute": DamageAttribute(convert_int(excel_instance.DamageAttribute(), password)).name,
        "MinDamageRate": convert_int(excel_instance.MinDamageRate(), password),
        "MaxDamageRate": convert_int(excel_instance.MaxDamageRate(), password),
        "ShowHighlightFloater": bool(excel_instance.ShowHighlightFloater()),
    }

def dump_CafeInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeId(), password),
        "IsDefault": bool(excel_instance.IsDefault()),
        "OpenConditionCafeId": OpenConditionContent(convert_int(excel_instance.OpenConditionCafeId(), password)).name,
        "OpenConditionCafeInvite": OpenConditionContent(convert_int(excel_instance.OpenConditionCafeInvite(), password)).name,
    }

def dump_CafeInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "IgnoreIfUnobtained": bool(excel_instance.IgnoreIfUnobtained()),
        "IgnoreIfUnobtainedStartDate": convert_string(excel_instance.IgnoreIfUnobtainedStartDate(), password),
        "IgnoreIfUnobtainedEndDate": convert_string(excel_instance.IgnoreIfUnobtainedEndDate(), password),
        "BubbleTypeLength": convert_int(excel_instance.BubbleTypeLength(), password),
        "BubbleDurationLength": convert_int(excel_instance.BubbleDurationLength(), password),
        "FavorEmoticonRewardParcelType": ParcelType(convert_int(excel_instance.FavorEmoticonRewardParcelType(), password)).name,
        "FavorEmoticonRewardId": convert_int(excel_instance.FavorEmoticonRewardId(), password),
        "FavorEmoticonRewardAmount": convert_int(excel_instance.FavorEmoticonRewardAmount(), password),
        "CafeCharacterStateLength": convert_int(excel_instance.CafeCharacterStateLength(), password),
    }

def dump_CafeProductionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeId(), password),
        "Rank": convert_int(excel_instance.Rank(), password),
        "CafeProductionParcelType": ParcelType(convert_int(excel_instance.CafeProductionParcelType(), password)).name,
        "CafeProductionParcelId": convert_int(excel_instance.CafeProductionParcelId(), password),
        "ParcelProductionCoefficient": convert_int(excel_instance.ParcelProductionCoefficient(), password),
        "ParcelProductionCorrectionValue": convert_int(excel_instance.ParcelProductionCorrectionValue(), password),
        "ParcelStorageMax": convert_int(excel_instance.ParcelStorageMax(), password),
    }

def dump_CafeRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeId(), password),
        "Rank": convert_int(excel_instance.Rank(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "ComfortMax": convert_int(excel_instance.ComfortMax(), password),
        "TagCountMax": convert_int(excel_instance.TagCountMax(), password),
        "CharacterVisitMin": convert_int(excel_instance.CharacterVisitMin(), password),
        "CharacterVisitMax": convert_int(excel_instance.CharacterVisitMax(), password),
        "CafeVisitWeightBase": convert_int(excel_instance.CafeVisitWeightBase(), password),
        "CafeVisitWeightTagBonusStepLength": convert_int(excel_instance.CafeVisitWeightTagBonusStepLength(), password),
        "CafeVisitWeightTagBonusLength": convert_int(excel_instance.CafeVisitWeightTagBonusLength(), password),
    }

def dump_CampaignChapterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "NormalImagePath": convert_string(excel_instance.NormalImagePath(), password),
        "HardImagePath": convert_string(excel_instance.HardImagePath(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "PreChapterIdLength": convert_int(excel_instance.PreChapterIdLength(), password),
        "ChapterRewardId": convert_int(excel_instance.ChapterRewardId(), password),
        "ChapterHardRewardId": convert_int(excel_instance.ChapterHardRewardId(), password),
        "ChapterVeryHardRewardId": convert_int(excel_instance.ChapterVeryHardRewardId(), password),
        "NormalCampaignStageIdLength": convert_int(excel_instance.NormalCampaignStageIdLength(), password),
        "NormalExtraStageIdLength": convert_int(excel_instance.NormalExtraStageIdLength(), password),
        "HardCampaignStageIdLength": convert_int(excel_instance.HardCampaignStageIdLength(), password),
        "VeryHardCampaignStageIdLength": convert_int(excel_instance.VeryHardCampaignStageIdLength(), password),
        "IsTacticSkip": bool(excel_instance.IsTacticSkip()),
    }

def dump_CampaignChapterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CampaignChapterStar": convert_int(excel_instance.CampaignChapterStar(), password),
        "ChapterRewardParcelTypeLength": convert_int(excel_instance.ChapterRewardParcelTypeLength(), password),
        "ChapterRewardIdLength": convert_int(excel_instance.ChapterRewardIdLength(), password),
        "ChapterRewardAmountLength": convert_int(excel_instance.ChapterRewardAmountLength(), password),
    }

def dump_CampaignStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Deprecated": bool(excel_instance.Deprecated()),
        "Name": convert_string(excel_instance.Name(), password),
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "CleardScenarioId": convert_int(excel_instance.CleardScenarioId(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupIdLength": convert_int(excel_instance.EnterScenarioGroupIdLength(), password),
        "ClearScenarioGroupIdLength": convert_int(excel_instance.ClearScenarioGroupIdLength(), password),
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "CampaignStageRewardId": convert_int(excel_instance.CampaignStageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StrategySkipGroundId": convert_int(excel_instance.StrategySkipGroundId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventName(), password),
        "TacticRewardExp": convert_int(excel_instance.TacticRewardExp(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_CampaignStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "StageRewardProb": convert_int(excel_instance.StageRewardProb(), password),
        "StageRewardParcelType": ParcelType(convert_int(excel_instance.StageRewardParcelType(), password)).name,
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "StageRewardAmount": convert_int(excel_instance.StageRewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_CampaignStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "StrategyObjectType": StrategyObjectType(convert_int(excel_instance.StrategyObjectType(), password)).name,
        "StrategyRewardParcelType": ParcelType(convert_int(excel_instance.StrategyRewardParcelType(), password)).name,
        "StrategyRewardID": convert_int(excel_instance.StrategyRewardID(), password),
        "StrategyRewardName": convert_string(excel_instance.StrategyRewardName(), password),
        "StrategyRewardAmount": convert_int(excel_instance.StrategyRewardAmount(), password),
        "StrategySightRange": convert_int(excel_instance.StrategySightRange(), password),
        "PortalId": convert_int(excel_instance.PortalId(), password),
        "HealValue": convert_int(excel_instance.HealValue(), password),
        "SwithId": convert_int(excel_instance.SwithId(), password),
        "BuffId": convert_int(excel_instance.BuffId(), password),
        "Disposable": bool(excel_instance.Disposable()),
    }

def dump_CampaignUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "StrategyPrefabName": convert_string(excel_instance.StrategyPrefabName(), password),
        "EnterScenarioGroupIdLength": convert_int(excel_instance.EnterScenarioGroupIdLength(), password),
        "ClearScenarioGroupIdLength": convert_int(excel_instance.ClearScenarioGroupIdLength(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "MoveRange": convert_int(excel_instance.MoveRange(), password),
        "AIMoveType": StrategyAIType(convert_int(excel_instance.AIMoveType(), password)).name,
        "Grade": HexaUnitGrade(convert_int(excel_instance.Grade(), password)).name,
        "EnvironmentType": TacticEnvironment(convert_int(excel_instance.EnvironmentType(), password)).name,
        "Scale": convert_float(excel_instance.Scale(), password),
        "IsTacticSkip": bool(excel_instance.IsTacticSkip()),
    }

def dump_CharacterAcademyTagsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FavorTagsLength": convert_int(excel_instance.FavorTagsLength(), password),
        "FavorItemTagsLength": convert_int(excel_instance.FavorItemTagsLength(), password),
        "FavorItemUniqueTagsLength": convert_int(excel_instance.FavorItemUniqueTagsLength(), password),
        "ForbiddenTagsLength": convert_int(excel_instance.ForbiddenTagsLength(), password),
        "ZoneWhiteListTagsLength": convert_int(excel_instance.ZoneWhiteListTagsLength(), password),
    }

def dump_CharacterAIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EngageType": EngageType(convert_int(excel_instance.EngageType(), password)).name,
        "Positioning": PositioningType(convert_int(excel_instance.Positioning(), password)).name,
        "CheckCanUseAutoSkill": bool(excel_instance.CheckCanUseAutoSkill()),
        "DistanceReduceRatioObstaclePath": convert_int(excel_instance.DistanceReduceRatioObstaclePath(), password),
        "DistanceReduceObstaclePath": convert_int(excel_instance.DistanceReduceObstaclePath(), password),
        "DistanceReduceRatioFormationPath": convert_int(excel_instance.DistanceReduceRatioFormationPath(), password),
        "DistanceReduceFormationPath": convert_int(excel_instance.DistanceReduceFormationPath(), password),
        "MinimumPositionGap": convert_int(excel_instance.MinimumPositionGap(), password),
        "CanUseObstacleOfKneelMotion": bool(excel_instance.CanUseObstacleOfKneelMotion()),
        "CanUseObstacleOfStandMotion": bool(excel_instance.CanUseObstacleOfStandMotion()),
        "HasTargetSwitchingMotion": bool(excel_instance.HasTargetSwitchingMotion()),
    }

def dump_CharacterCalculationLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "CalculationValue": BattleCalculationStat(convert_int(excel_instance.CalculationValue(), password)).name,
        "MinValue": convert_int(excel_instance.MinValue(), password),
        "MaxValue": convert_int(excel_instance.MaxValue(), password),
        "LimitStartValueLength": convert_int(excel_instance.LimitStartValueLength(), password),
        "DecreaseRateLength": convert_int(excel_instance.DecreaseRateLength(), password),
    }

def dump_CharacterCombatSkinExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePath(), password),
    }

def dump_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": convert_string(excel_instance.DialogType(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "HideUI": bool(excel_instance.HideUI()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterDialogFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Phase": convert_int(excel_instance.Phase(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": FieldDialogType(convert_int(excel_instance.DialogType(), password)).name,
        "Duration": convert_int(excel_instance.Duration(), password),
        "MotionName": convert_string(excel_instance.MotionName(), password),
        "IsInteractionDialog": bool(excel_instance.IsInteractionDialog()),
        "HideUI": bool(excel_instance.HideUI()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CostumeGroupId": convert_int(excel_instance.CostumeGroupId(), password),
        "IsPlayable": bool(excel_instance.IsPlayable()),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "ReleaseDate": convert_string(excel_instance.ReleaseDate(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDate(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDate(), password),
        "IsPlayableCharacter": bool(excel_instance.IsPlayableCharacter()),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "IsNPC": bool(excel_instance.IsNPC()),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "CanSurvive": bool(excel_instance.CanSurvive()),
        "IsDummy": bool(excel_instance.IsDummy()),
        "SubPartsCount": convert_int(excel_instance.SubPartsCount(), password),
        "TacticRole": convert_float(excel_instance.TacticRole(), password),
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponType(), password)).name,
        "TacticRange": TacticRange(convert_int(excel_instance.TacticRange(), password)).name,
        "BulletType": BulletType(convert_int(excel_instance.BulletType(), password)).name,
        "ArmorType": ArmorType(convert_int(excel_instance.ArmorType(), password)).name,
        "AimIKType": AimIKType(convert_int(excel_instance.AimIKType(), password)).name,
        "School": School(convert_int(excel_instance.School(), password)).name,
        "Club": Club(convert_int(excel_instance.Club(), password)).name,
        "DefaultStarGrade": convert_int(excel_instance.DefaultStarGrade(), password),
        "MaxStarGrade": convert_int(excel_instance.MaxStarGrade(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "SquadType": SquadType(convert_int(excel_instance.SquadType(), password)).name,
        "Jumpable": bool(excel_instance.Jumpable()),
        "PersonalityId": convert_int(excel_instance.PersonalityId(), password),
        "CharacterAIId": convert_int(excel_instance.CharacterAIId(), password),
        "ExternalBTId": convert_int(excel_instance.ExternalBTId(), password),
        "MainCombatStyleId": convert_int(excel_instance.MainCombatStyleId(), password),
        "CombatStyleIndex": convert_int(excel_instance.CombatStyleIndex(), password),
        "ScenarioCharacter": convert_string(excel_instance.ScenarioCharacter(), password),
        "SpawnTemplateId": convert_uint(excel_instance.SpawnTemplateId(), password),
        "FavorLevelupType": convert_int(excel_instance.FavorLevelupType(), password),
        "EquipmentSlotLength": convert_int(excel_instance.EquipmentSlotLength(), password),
        "WeaponLocalizeId": convert_uint(excel_instance.WeaponLocalizeId(), password),
        "DisplayEnemyInfo": bool(excel_instance.DisplayEnemyInfo()),
        "BodyRadius": convert_int(excel_instance.BodyRadius(), password),
        "RandomEffectRadius": convert_int(excel_instance.RandomEffectRadius(), password),
        "HPBarHide": bool(excel_instance.HPBarHide()),
        "HpBarHeight": convert_float(excel_instance.HpBarHeight(), password),
        "HighlightFloaterHeight": convert_float(excel_instance.HighlightFloaterHeight(), password),
        "EmojiOffsetX": convert_float(excel_instance.EmojiOffsetX(), password),
        "EmojiOffsetY": convert_float(excel_instance.EmojiOffsetY(), password),
        "MoveStartFrame": convert_int(excel_instance.MoveStartFrame(), password),
        "MoveEndFrame": convert_int(excel_instance.MoveEndFrame(), password),
        "JumpMotionFrame": convert_int(excel_instance.JumpMotionFrame(), password),
        "AppearFrame": convert_int(excel_instance.AppearFrame(), password),
        "CanMove": bool(excel_instance.CanMove()),
        "CanFix": bool(excel_instance.CanFix()),
        "CanCrowdControl": bool(excel_instance.CanCrowdControl()),
        "CanBattleItemMove": bool(excel_instance.CanBattleItemMove()),
        "IsAirUnit": bool(excel_instance.IsAirUnit()),
        "AirUnitHeight": convert_int(excel_instance.AirUnitHeight(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
        "SecretStoneItemId": convert_int(excel_instance.SecretStoneItemId(), password),
        "SecretStoneItemAmount": convert_int(excel_instance.SecretStoneItemAmount(), password),
        "CharacterPieceItemId": convert_int(excel_instance.CharacterPieceItemId(), password),
        "CharacterPieceItemAmount": convert_int(excel_instance.CharacterPieceItemAmount(), password),
        "CombineRecipeId": convert_int(excel_instance.CombineRecipeId(), password),
    }

def dump_CharacterIllustCoordinateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterBodyCenterX": convert_float(excel_instance.CharacterBodyCenterX(), password),
        "CharacterBodyCenterY": convert_float(excel_instance.CharacterBodyCenterY(), password),
        "DefaultScale": convert_float(excel_instance.DefaultScale(), password),
        "MinScale": convert_float(excel_instance.MinScale(), password),
        "MaxScale": convert_float(excel_instance.MaxScale(), password),
    }

def dump_CharacterLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "TotalExp": convert_int(excel_instance.TotalExp(), password),
    }

def dump_CharacterLevelStatFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "CriticalFactor": convert_int(excel_instance.CriticalFactor(), password),
        "StabilityFactor": convert_int(excel_instance.StabilityFactor(), password),
        "DefenceFactor": convert_int(excel_instance.DefenceFactor(), password),
        "AccuracyFactor": convert_int(excel_instance.AccuracyFactor(), password),
    }

def dump_CharacterSkillListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterSkillListGroupId": convert_int(excel_instance.CharacterSkillListGroupId(), password),
        "MinimumGradeCharacterWeapon": convert_int(excel_instance.MinimumGradeCharacterWeapon(), password),
        "MinimumTierCharacterGear": convert_int(excel_instance.MinimumTierCharacterGear(), password),
        "FormIndex": convert_int(excel_instance.FormIndex(), password),
        "IsRootMotion": bool(excel_instance.IsRootMotion()),
        "IsMoveLeftRight": bool(excel_instance.IsMoveLeftRight()),
        "UseRandomExSkillTimeline": bool(excel_instance.UseRandomExSkillTimeline()),
        "TSAInteractionId": convert_int(excel_instance.TSAInteractionId(), password),
        "NormalSkillGroupIdLength": convert_int(excel_instance.NormalSkillGroupIdLength(), password),
        "NormalSkillTimeLineIndexLength": convert_int(excel_instance.NormalSkillTimeLineIndexLength(), password),
        "ExSkillGroupIdLength": convert_int(excel_instance.ExSkillGroupIdLength(), password),
        "ExSkillCutInTimeLineIndexLength": convert_int(excel_instance.ExSkillCutInTimeLineIndexLength(), password),
        "ExSkillLevelTimeLineIndexLength": convert_int(excel_instance.ExSkillLevelTimeLineIndexLength(), password),
        "PublicSkillGroupIdLength": convert_int(excel_instance.PublicSkillGroupIdLength(), password),
        "PublicSkillTimeLineIndexLength": convert_int(excel_instance.PublicSkillTimeLineIndexLength(), password),
        "PassiveSkillGroupIdLength": convert_int(excel_instance.PassiveSkillGroupIdLength(), password),
        "LeaderSkillGroupIdLength": convert_int(excel_instance.LeaderSkillGroupIdLength(), password),
        "ExtraPassiveSkillGroupIdLength": convert_int(excel_instance.ExtraPassiveSkillGroupIdLength(), password),
        "HiddenPassiveSkillGroupIdLength": convert_int(excel_instance.HiddenPassiveSkillGroupIdLength(), password),
    }

def dump_CharacterStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "StabilityRate": convert_int(excel_instance.StabilityRate(), password),
        "StabilityPoint": convert_int(excel_instance.StabilityPoint(), password),
        "AttackPower1": convert_int(excel_instance.AttackPower1(), password),
        "AttackPower100": convert_int(excel_instance.AttackPower100(), password),
        "MaxHP1": convert_int(excel_instance.MaxHP1(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100(), password),
        "DefensePower1": convert_int(excel_instance.DefensePower1(), password),
        "DefensePower100": convert_int(excel_instance.DefensePower100(), password),
        "HealPower1": convert_int(excel_instance.HealPower1(), password),
        "HealPower100": convert_int(excel_instance.HealPower100(), password),
        "DodgePoint": convert_int(excel_instance.DodgePoint(), password),
        "AccuracyPoint": convert_int(excel_instance.AccuracyPoint(), password),
        "CriticalPoint": convert_int(excel_instance.CriticalPoint(), password),
        "CriticalResistPoint": convert_int(excel_instance.CriticalResistPoint(), password),
        "CriticalDamageRate": convert_int(excel_instance.CriticalDamageRate(), password),
        "CriticalDamageResistRate": convert_int(excel_instance.CriticalDamageResistRate(), password),
        "BlockRate": convert_int(excel_instance.BlockRate(), password),
        "HealEffectivenessRate": convert_int(excel_instance.HealEffectivenessRate(), password),
        "OppressionPower": convert_int(excel_instance.OppressionPower(), password),
        "OppressionResist": convert_int(excel_instance.OppressionResist(), password),
        "DefensePenetration1": convert_int(excel_instance.DefensePenetration1(), password),
        "DefensePenetration100": convert_int(excel_instance.DefensePenetration100(), password),
        "DefensePenetrationResist1": convert_int(excel_instance.DefensePenetrationResist1(), password),
        "DefensePenetrationResist100": convert_int(excel_instance.DefensePenetrationResist100(), password),
        "EnhanceExplosionRate": convert_int(excel_instance.EnhanceExplosionRate(), password),
        "EnhancePierceRate": convert_int(excel_instance.EnhancePierceRate(), password),
        "EnhanceMysticRate": convert_int(excel_instance.EnhanceMysticRate(), password),
        "EnhanceSonicRate": convert_int(excel_instance.EnhanceSonicRate(), password),
        "EnhanceSiegeRate": convert_int(excel_instance.EnhanceSiegeRate(), password),
        "EnhanceNormalRate": convert_int(excel_instance.EnhanceNormalRate(), password),
        "EnhanceLightArmorRate": convert_int(excel_instance.EnhanceLightArmorRate(), password),
        "EnhanceHeavyArmorRate": convert_int(excel_instance.EnhanceHeavyArmorRate(), password),
        "EnhanceUnarmedRate": convert_int(excel_instance.EnhanceUnarmedRate(), password),
        "EnhanceElasticArmorRate": convert_int(excel_instance.EnhanceElasticArmorRate(), password),
        "EnhanceStructureRate": convert_int(excel_instance.EnhanceStructureRate(), password),
        "EnhanceNormalArmorRate": convert_int(excel_instance.EnhanceNormalArmorRate(), password),
        "ExtendBuffDuration": convert_int(excel_instance.ExtendBuffDuration(), password),
        "ExtendDebuffDuration": convert_int(excel_instance.ExtendDebuffDuration(), password),
        "ExtendCrowdControlDuration": convert_int(excel_instance.ExtendCrowdControlDuration(), password),
        "AmmoCount": convert_int(excel_instance.AmmoCount(), password),
        "AmmoCost": convert_int(excel_instance.AmmoCost(), password),
        "IgnoreDelayCount": convert_int(excel_instance.IgnoreDelayCount(), password),
        "NormalAttackSpeed": convert_int(excel_instance.NormalAttackSpeed(), password),
        "Range": convert_int(excel_instance.Range(), password),
        "InitialRangeRate": convert_int(excel_instance.InitialRangeRate(), password),
        "MoveSpeed": convert_int(excel_instance.MoveSpeed(), password),
        "SightPoint": convert_int(excel_instance.SightPoint(), password),
        "ActiveGauge": convert_int(excel_instance.ActiveGauge(), password),
        "GroggyGauge": convert_int(excel_instance.GroggyGauge(), password),
        "GroggyTime": convert_int(excel_instance.GroggyTime(), password),
        "StrategyMobility": convert_int(excel_instance.StrategyMobility(), password),
        "ActionCount": convert_int(excel_instance.ActionCount(), password),
        "StrategySightRange": convert_int(excel_instance.StrategySightRange(), password),
        "DamageRatio": convert_int(excel_instance.DamageRatio(), password),
        "DamagedRatio": convert_int(excel_instance.DamagedRatio(), password),
        "DamageRatio2Increase": convert_int(excel_instance.DamageRatio2Increase(), password),
        "DamageRatio2Decrease": convert_int(excel_instance.DamageRatio2Decrease(), password),
        "DamagedRatio2Increase": convert_int(excel_instance.DamagedRatio2Increase(), password),
        "DamagedRatio2Decrease": convert_int(excel_instance.DamagedRatio2Decrease(), password),
        "ExDamagedRatioIncrease": convert_int(excel_instance.ExDamagedRatioIncrease(), password),
        "ExDamagedRatioDecrease": convert_int(excel_instance.ExDamagedRatioDecrease(), password),
        "EnhanceExDamageRate": convert_int(excel_instance.EnhanceExDamageRate(), password),
        "ReduceExDamagedRate": convert_int(excel_instance.ReduceExDamagedRate(), password),
        "HealRate": convert_int(excel_instance.HealRate(), password),
        "HealLightArmorRate": convert_int(excel_instance.HealLightArmorRate(), password),
        "HealHeavyArmorRate": convert_int(excel_instance.HealHeavyArmorRate(), password),
        "HealUnarmedRate": convert_int(excel_instance.HealUnarmedRate(), password),
        "HealElasticArmorRate": convert_int(excel_instance.HealElasticArmorRate(), password),
        "HealNormalArmorRate": convert_int(excel_instance.HealNormalArmorRate(), password),
        "HealedExplosionRate": convert_int(excel_instance.HealedExplosionRate(), password),
        "HealedPierceRate": convert_int(excel_instance.HealedPierceRate(), password),
        "HealedMysticRate": convert_int(excel_instance.HealedMysticRate(), password),
        "HealedSonicRate": convert_int(excel_instance.HealedSonicRate(), password),
        "HealedNormalRate": convert_int(excel_instance.HealedNormalRate(), password),
        "StreetBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.StreetBattleAdaptation(), password)).name,
        "OutdoorBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OutdoorBattleAdaptation(), password)).name,
        "IndoorBattleAdaptation": TerrainAdaptationStat(convert_int(excel_instance.IndoorBattleAdaptation(), password)).name,
        "RegenCost": convert_int(excel_instance.RegenCost(), password),
    }

def dump_CharacterStatLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "StatType": StatType(convert_int(excel_instance.StatType(), password)).name,
        "StatMinValue": convert_int(excel_instance.StatMinValue(), password),
        "StatMaxValue": convert_int(excel_instance.StatMaxValue(), password),
        "StatRatioMinValue": convert_int(excel_instance.StatRatioMinValue(), password),
        "StatRatioMaxValue": convert_int(excel_instance.StatRatioMaxValue(), password),
    }

def dump_CharacterStatsDetailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DetailShowStatsLength": convert_int(excel_instance.DetailShowStatsLength(), password),
        "IsStatsPercentLength": convert_int(excel_instance.IsStatsPercentLength(), password),
    }

def dump_CharacterStatsTransExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TransSupportStats": StatType(convert_int(excel_instance.TransSupportStats(), password)).name,
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "TransSupportStatsFactor": convert_int(excel_instance.TransSupportStatsFactor(), password),
        "StatTransType": StatTransType(convert_int(excel_instance.StatTransType(), password)).name,
    }

def dump_CharacterTranscendenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MaxFavorLevelLength": convert_int(excel_instance.MaxFavorLevelLength(), password),
        "StatBonusRateAttackLength": convert_int(excel_instance.StatBonusRateAttackLength(), password),
        "StatBonusRateHPLength": convert_int(excel_instance.StatBonusRateHPLength(), password),
        "StatBonusRateHealLength": convert_int(excel_instance.StatBonusRateHealLength(), password),
        "RecipeIdLength": convert_int(excel_instance.RecipeIdLength(), password),
        "SkillSlotALength": convert_int(excel_instance.SkillSlotALength(), password),
        "SkillSlotBLength": convert_int(excel_instance.SkillSlotBLength(), password),
        "SkillSlotCLength": convert_int(excel_instance.SkillSlotCLength(), password),
        "MaxlevelStarLength": convert_int(excel_instance.MaxlevelStarLength(), password),
    }

def dump_CharacterVictoryInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "InteractionId": convert_int(excel_instance.InteractionId(), password),
        "CostumeId01": convert_int(excel_instance.CostumeId01(), password),
        "PositionIndex01": convert_int(excel_instance.PositionIndex01(), password),
        "VictoryStartAnimationPath01": convert_string(excel_instance.VictoryStartAnimationPath01(), password),
        "VictoryEndAnimationPath01": convert_string(excel_instance.VictoryEndAnimationPath01(), password),
        "VoiceEvent01": VoiceEvent(convert_int(excel_instance.VoiceEvent01(), password)).name,
        "CostumeId02": convert_int(excel_instance.CostumeId02(), password),
        "PositionIndex02": convert_int(excel_instance.PositionIndex02(), password),
        "VictoryStartAnimationPath02": convert_string(excel_instance.VictoryStartAnimationPath02(), password),
        "VictoryEndAnimationPath02": convert_string(excel_instance.VictoryEndAnimationPath02(), password),
        "VoiceEvent02": VoiceEvent(convert_int(excel_instance.VoiceEvent02(), password)).name,
        "CostumeId03": convert_int(excel_instance.CostumeId03(), password),
        "PositionIndex03": convert_int(excel_instance.PositionIndex03(), password),
        "VictoryStartAnimationPath03": convert_string(excel_instance.VictoryStartAnimationPath03(), password),
        "VictoryEndAnimationPath03": convert_string(excel_instance.VictoryEndAnimationPath03(), password),
        "VoiceEvent03": VoiceEvent(convert_int(excel_instance.VoiceEvent03(), password)).name,
        "CostumeId04": convert_int(excel_instance.CostumeId04(), password),
        "PositionIndex04": convert_int(excel_instance.PositionIndex04(), password),
        "VictoryStartAnimationPath04": convert_string(excel_instance.VictoryStartAnimationPath04(), password),
        "VictoryEndAnimationPath04": convert_string(excel_instance.VictoryEndAnimationPath04(), password),
        "VoiceEvent04": VoiceEvent(convert_int(excel_instance.VoiceEvent04(), password)).name,
        "CostumeId05": convert_int(excel_instance.CostumeId05(), password),
        "PositionIndex05": convert_int(excel_instance.PositionIndex05(), password),
        "VictoryStartAnimationPath05": convert_string(excel_instance.VictoryStartAnimationPath05(), password),
        "VictoryEndAnimationPath05": convert_string(excel_instance.VictoryEndAnimationPath05(), password),
        "VoiceEvent05": VoiceEvent(convert_int(excel_instance.VoiceEvent05(), password)).name,
        "CostumeId06": convert_int(excel_instance.CostumeId06(), password),
        "PositionIndex06": convert_int(excel_instance.PositionIndex06(), password),
        "VictoryStartAnimationPath06": convert_string(excel_instance.VictoryStartAnimationPath06(), password),
        "VictoryEndAnimationPath06": convert_string(excel_instance.VictoryEndAnimationPath06(), password),
        "VoiceEvent06": VoiceEvent(convert_int(excel_instance.VoiceEvent06(), password)).name,
    }

def dump_CharacterWeaponExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "SetRecipe": convert_int(excel_instance.SetRecipe(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "AttackPower": convert_int(excel_instance.AttackPower(), password),
        "AttackPower100": convert_int(excel_instance.AttackPower100(), password),
        "MaxHP": convert_int(excel_instance.MaxHP(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100(), password),
        "HealPower": convert_int(excel_instance.HealPower(), password),
        "HealPower100": convert_int(excel_instance.HealPower100(), password),
        "UnlockLength": convert_int(excel_instance.UnlockLength(), password),
        "RecipeIdLength": convert_int(excel_instance.RecipeIdLength(), password),
        "MaxLevelLength": convert_int(excel_instance.MaxLevelLength(), password),
        "LearnSkillSlotLength": convert_int(excel_instance.LearnSkillSlotLength(), password),
        "StatTypeLength": convert_int(excel_instance.StatTypeLength(), password),
        "StatValueLength": convert_int(excel_instance.StatValueLength(), password),
    }

def dump_CharacterWeaponExpBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponType(), password)).name,
        "WeaponExpGrowthA": convert_int(excel_instance.WeaponExpGrowthA(), password),
        "WeaponExpGrowthB": convert_int(excel_instance.WeaponExpGrowthB(), password),
        "WeaponExpGrowthC": convert_int(excel_instance.WeaponExpGrowthC(), password),
        "WeaponExpGrowthZ": convert_int(excel_instance.WeaponExpGrowthZ(), password),
    }

def dump_CharacterWeaponLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "TotalExp": convert_int(excel_instance.TotalExp(), password),
    }

def dump_ClearDeckRuleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "SizeLimit": convert_int(excel_instance.SizeLimit(), password),
    }

def dump_ConquestCalculateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CalculateConditionParcelType": ParcelType(convert_int(excel_instance.CalculateConditionParcelType(), password)).name,
        "CalculateConditionParcelUniqueId": convert_int(excel_instance.CalculateConditionParcelUniqueId(), password),
        "CalculateConditionParcelAmount": convert_int(excel_instance.CalculateConditionParcelAmount(), password),
    }

def dump_ConquestCameraSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ConquestMapBoundaryOffsetLeft": convert_float(excel_instance.ConquestMapBoundaryOffsetLeft(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRight(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTop(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottom(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetX(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetY(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngle(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
    }

def dump_ConquestErosionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "ErosionType": ConquestErosionType(convert_int(excel_instance.ErosionType(), password)).name,
        "Phase": convert_int(excel_instance.Phase(), password),
        "PhaseAlarm": bool(excel_instance.PhaseAlarm()),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "PhaseStartConditionTypeLength": convert_int(excel_instance.PhaseStartConditionTypeLength(), password),
        "PhaseStartConditionParameterLength": convert_int(excel_instance.PhaseStartConditionParameterLength(), password),
        "PhaseBeforeExposeConditionTypeLength": convert_int(excel_instance.PhaseBeforeExposeConditionTypeLength(), password),
        "PhaseBeforeExposeConditionParameterLength": convert_int(excel_instance.PhaseBeforeExposeConditionParameterLength(), password),
        "ErosionBattleConditionParcelType": ParcelType(convert_int(excel_instance.ErosionBattleConditionParcelType(), password)).name,
        "ErosionBattleConditionParcelUniqueId": convert_int(excel_instance.ErosionBattleConditionParcelUniqueId(), password),
        "ErosionBattleConditionParcelAmount": convert_int(excel_instance.ErosionBattleConditionParcelAmount(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardId(), password),
    }

def dump_ConquestErosionUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TilePrefabId": convert_int(excel_instance.TilePrefabId(), password),
        "MassErosionUnitId": convert_int(excel_instance.MassErosionUnitId(), password),
        "MassErosionUnitRotationY": convert_float(excel_instance.MassErosionUnitRotationY(), password),
        "IndividualErosionUnitId": convert_int(excel_instance.IndividualErosionUnitId(), password),
        "IndividualErosionUnitRotationY": convert_float(excel_instance.IndividualErosionUnitRotationY(), password),
    }

def dump_ConquestEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "MainStoryEventContentId": convert_int(excel_instance.MainStoryEventContentId(), password),
        "ConquestEventType": ConquestEventType(convert_int(excel_instance.ConquestEventType(), password)).name,
        "UseErosion": bool(excel_instance.UseErosion()),
        "UseUnexpectedEvent": bool(excel_instance.UseUnexpectedEvent()),
        "UseCalculate": bool(excel_instance.UseCalculate()),
        "UseConquestObject": bool(excel_instance.UseConquestObject()),
        "EvnetMapGoalLocalize": convert_string(excel_instance.EvnetMapGoalLocalize(), password),
        "EvnetMapNameLocalize": convert_string(excel_instance.EvnetMapNameLocalize(), password),
        "MapEnterScenarioGroupId": convert_int(excel_instance.MapEnterScenarioGroupId(), password),
        "EvnetScenarioBG": convert_string(excel_instance.EvnetScenarioBG(), password),
        "ManageUnitChange": convert_int(excel_instance.ManageUnitChange(), password),
        "AssistCount": convert_int(excel_instance.AssistCount(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "AnimationUnitAmountMin": convert_int(excel_instance.AnimationUnitAmountMin(), password),
        "AnimationUnitAmountMax": convert_int(excel_instance.AnimationUnitAmountMax(), password),
        "AnimationUnitDelay": convert_float(excel_instance.AnimationUnitDelay(), password),
        "LocalizeUnexpected": convert_string(excel_instance.LocalizeUnexpected(), password),
        "LocalizeErosions": convert_string(excel_instance.LocalizeErosions(), password),
        "LocalizeStep": convert_string(excel_instance.LocalizeStep(), password),
        "LocalizeTile": convert_string(excel_instance.LocalizeTile(), password),
        "LocalizeMapInfo": convert_string(excel_instance.LocalizeMapInfo(), password),
        "LocalizeManage": convert_string(excel_instance.LocalizeManage(), password),
        "LocalizeUpgrade": convert_string(excel_instance.LocalizeUpgrade(), password),
        "LocalizeTreasureBox": convert_string(excel_instance.LocalizeTreasureBox(), password),
        "IndividualErosionDailyCount": convert_int(excel_instance.IndividualErosionDailyCount(), password),
    }

def dump_ConquestGroupBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBonusId": convert_int(excel_instance.ConquestBonusId(), password),
        "SchoolLength": convert_int(excel_instance.SchoolLength(), password),
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "BonusParcelTypeLength": convert_int(excel_instance.BonusParcelTypeLength(), password),
        "BonusIdLength": convert_int(excel_instance.BonusIdLength(), password),
        "BonusCharacterCount1Length": convert_int(excel_instance.BonusCharacterCount1Length(), password),
        "BonusPercentage1Length": convert_int(excel_instance.BonusPercentage1Length(), password),
        "BonusCharacterCount2Length": convert_int(excel_instance.BonusCharacterCount2Length(), password),
        "BonusPercentage2Length": convert_int(excel_instance.BonusPercentage2Length(), password),
        "BonusCharacterCount3Length": convert_int(excel_instance.BonusCharacterCount3Length(), password),
        "BonusPercentage3Length": convert_int(excel_instance.BonusPercentage3Length(), password),
    }

def dump_ConquestGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBuffId": convert_int(excel_instance.ConquestBuffId(), password),
        "SchoolLength": convert_int(excel_instance.SchoolLength(), password),
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
    }

def dump_ConquestMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficulty(), password)).name,
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "ConquestMap": convert_string(excel_instance.ConquestMap(), password),
        "StepEnterScenarioGroupId": convert_int(excel_instance.StepEnterScenarioGroupId(), password),
        "StepOpenConditionTypeLength": convert_int(excel_instance.StepOpenConditionTypeLength(), password),
        "StepOpenConditionParameterLength": convert_int(excel_instance.StepOpenConditionParameterLength(), password),
        "MapGoalLocalize": convert_string(excel_instance.MapGoalLocalize(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalize(), password),
        "StepNameLocalize": convert_string(excel_instance.StepNameLocalize(), password),
        "ConquestMapBG": convert_string(excel_instance.ConquestMapBG(), password),
        "CameraSettingId": convert_int(excel_instance.CameraSettingId(), password),
    }

def dump_ConquestObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ConquestObjectType": ConquestObjectType(convert_int(excel_instance.ConquestObjectType(), password)).name,
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ConquestRewardParcelType": ParcelType(convert_int(excel_instance.ConquestRewardParcelType(), password)).name,
        "ConquestRewardID": convert_int(excel_instance.ConquestRewardID(), password),
        "ConquestRewardAmount": convert_int(excel_instance.ConquestRewardAmount(), password),
        "Disposable": bool(excel_instance.Disposable()),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "StepObjectCount": convert_int(excel_instance.StepObjectCount(), password),
    }

def dump_ConquestPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_ConquestProgressResourceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Group": ConquestProgressType(convert_int(excel_instance.Group(), password)).name,
        "ProgressResource": convert_string(excel_instance.ProgressResource(), password),
        "VoiceIdLength": convert_int(excel_instance.VoiceIdLength(), password),
        "ProgressLocalizeCode": convert_string(excel_instance.ProgressLocalizeCode(), password),
    }

def dump_ConquestRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_ConquestStepExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficulty(), password)).name,
        "Step": convert_int(excel_instance.Step(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalize(), password),
        "StepEnterScenarioGroupId": convert_int(excel_instance.StepEnterScenarioGroupId(), password),
        "StepEnterItemType": ParcelType(convert_int(excel_instance.StepEnterItemType(), password)).name,
        "StepEnterItemUniqueId": convert_int(excel_instance.StepEnterItemUniqueId(), password),
        "StepEnterItemAmount": convert_int(excel_instance.StepEnterItemAmount(), password),
        "UnexpectedEventUnitIdLength": convert_int(excel_instance.UnexpectedEventUnitIdLength(), password),
        "UnexpectedEventPrefab": convert_string(excel_instance.UnexpectedEventPrefab(), password),
        "TreasureBoxObjectId": convert_int(excel_instance.TreasureBoxObjectId(), password),
        "TreasureBoxCountPerStepOpen": convert_int(excel_instance.TreasureBoxCountPerStepOpen(), password),
    }

def dump_ConquestTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventId": convert_int(excel_instance.EventId(), password),
        "Step": convert_int(excel_instance.Step(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "TileNameLocalize": convert_string(excel_instance.TileNameLocalize(), password),
        "TileImageName": convert_string(excel_instance.TileImageName(), password),
        "Playable": bool(excel_instance.Playable()),
        "TileType": ConquestTileType(convert_int(excel_instance.TileType(), password)).name,
        "NotMapFog": bool(excel_instance.NotMapFog()),
        "GroupBonusId": convert_int(excel_instance.GroupBonusId(), password),
        "ConquestCostType": ParcelType(convert_int(excel_instance.ConquestCostType(), password)).name,
        "ConquestCostId": convert_int(excel_instance.ConquestCostId(), password),
        "ConquestCostAmount": convert_int(excel_instance.ConquestCostAmount(), password),
        "ManageCostType": ParcelType(convert_int(excel_instance.ManageCostType(), password)).name,
        "ManageCostId": convert_int(excel_instance.ManageCostId(), password),
        "ManageCostAmount": convert_int(excel_instance.ManageCostAmount(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardId(), password),
        "MassErosionId": convert_int(excel_instance.MassErosionId(), password),
        "Upgrade2CostType": ParcelType(convert_int(excel_instance.Upgrade2CostType(), password)).name,
        "Upgrade2CostId": convert_int(excel_instance.Upgrade2CostId(), password),
        "Upgrade2CostAmount": convert_int(excel_instance.Upgrade2CostAmount(), password),
        "Upgrade3CostType": ParcelType(convert_int(excel_instance.Upgrade3CostType(), password)).name,
        "Upgrade3CostId": convert_int(excel_instance.Upgrade3CostId(), password),
        "Upgrade3CostAmount": convert_int(excel_instance.Upgrade3CostAmount(), password),
    }

def dump_ConquestUnexpectedEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UnexpectedEventConditionType": ParcelType(convert_int(excel_instance.UnexpectedEventConditionType(), password)).name,
        "UnexpectedEventConditionUniqueId": convert_int(excel_instance.UnexpectedEventConditionUniqueId(), password),
        "UnexpectedEventConditionAmount": convert_int(excel_instance.UnexpectedEventConditionAmount(), password),
        "UnexpectedEventOccurDailyLimitCount": convert_int(excel_instance.UnexpectedEventOccurDailyLimitCount(), password),
        "UnitCountPerStep": convert_int(excel_instance.UnitCountPerStep(), password),
        "UnexpectedEventPrefabLength": convert_int(excel_instance.UnexpectedEventPrefabLength(), password),
        "UnexpectedEventUnitIdLength": convert_int(excel_instance.UnexpectedEventUnitIdLength(), password),
    }

def dump_ConquestUnitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "StrategyPrefabName": convert_string(excel_instance.StrategyPrefabName(), password),
        "Scale": convert_float(excel_instance.Scale(), password),
        "ShieldEffectScale": convert_float(excel_instance.ShieldEffectScale(), password),
        "UnitFxPrefabName": convert_string(excel_instance.UnitFxPrefabName(), password),
        "PointAnimation": convert_string(excel_instance.PointAnimation(), password),
        "EnemyType": ConquestEnemyType(convert_int(excel_instance.EnemyType(), password)).name,
        "Team": ConquestTeamType(convert_int(excel_instance.Team(), password)).name,
        "UnitGroup": convert_int(excel_instance.UnitGroup(), password),
        "PrevUnitGroup": convert_int(excel_instance.PrevUnitGroup(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoalLength": convert_int(excel_instance.StarGoalLength(), password),
        "StarGoalAmountLength": convert_int(excel_instance.StarGoalAmountLength(), password),
        "GroupBuffId": convert_int(excel_instance.GroupBuffId(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "ManageEchelonStageEnterCostType": ParcelType(convert_int(excel_instance.ManageEchelonStageEnterCostType(), password)).name,
        "ManageEchelonStageEnterCostId": convert_int(excel_instance.ManageEchelonStageEnterCostId(), password),
        "ManageEchelonStageEnterCostAmount": convert_int(excel_instance.ManageEchelonStageEnterCostAmount(), password),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupId(), password),
        "ClearScenarioGroupId": convert_int(excel_instance.ClearScenarioGroupId(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardId(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "TacticRewardExp": convert_int(excel_instance.TacticRewardExp(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_ConstArenaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttackCoolTime": convert_int(excel_instance.AttackCoolTime(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "DefenseCoolTime": convert_int(excel_instance.DefenseCoolTime(), password),
        "TSSStartCoolTime": convert_int(excel_instance.TSSStartCoolTime(), password),
        "EndAlarm": convert_int(excel_instance.EndAlarm(), password),
        "TimeRewardMaxAmount": convert_int(excel_instance.TimeRewardMaxAmount(), password),
        "EnterCostType": ParcelType(convert_int(excel_instance.EnterCostType(), password)).name,
        "EnterCostId": convert_int(excel_instance.EnterCostId(), password),
        "TicketCost": convert_int(excel_instance.TicketCost(), password),
        "DailyRewardResetTime": convert_string(excel_instance.DailyRewardResetTime(), password),
        "OpenScenarioId": convert_string(excel_instance.OpenScenarioId(), password),
        "CharacterSlotHideRankLength": convert_int(excel_instance.CharacterSlotHideRankLength(), password),
        "MapSlotHideRank": convert_int(excel_instance.MapSlotHideRank(), password),
        "RelativeOpponentRankStartLength": convert_int(excel_instance.RelativeOpponentRankStartLength(), password),
        "RelativeOpponentRankEndLength": convert_int(excel_instance.RelativeOpponentRankEndLength(), password),
        "ModifiedStatTypeLength": convert_int(excel_instance.ModifiedStatTypeLength(), password),
        "StatMulFactorLength": convert_int(excel_instance.StatMulFactorLength(), password),
        "StatSumFactorLength": convert_int(excel_instance.StatSumFactorLength(), password),
        "NPCNameLength": convert_int(excel_instance.NPCNameLength(), password),
        "NPCMainCharacterCount": convert_int(excel_instance.NPCMainCharacterCount(), password),
        "NPCSupportCharacterCount": convert_int(excel_instance.NPCSupportCharacterCount(), password),
        "NPCCharacterSkillLevel": convert_int(excel_instance.NPCCharacterSkillLevel(), password),
        "TimeSpanInDaysForBattleHistory": convert_int(excel_instance.TimeSpanInDaysForBattleHistory(), password),
        "HiddenCharacterImagePath": convert_string(excel_instance.HiddenCharacterImagePath(), password),
        "DefenseVictoryRewardMaxCount": convert_int(excel_instance.DefenseVictoryRewardMaxCount(), password),
        "TopRankerCountLimit": convert_int(excel_instance.TopRankerCountLimit(), password),
        "AutoRefreshIntervalMilliSeconds": convert_int(excel_instance.AutoRefreshIntervalMilliSeconds(), password),
        "EchelonSettingIntervalMilliSeconds": convert_int(excel_instance.EchelonSettingIntervalMilliSeconds(), password),
        "SkipAllowedTimeMilliSeconds": convert_int(excel_instance.SkipAllowedTimeMilliSeconds(), password),
        "ShowSeasonChangeInfoStartTime": convert_string(excel_instance.ShowSeasonChangeInfoStartTime(), password),
        "ShowSeasonChangeInfoEndTime": convert_string(excel_instance.ShowSeasonChangeInfoEndTime(), password),
        "ShowSeasonId": convert_int(excel_instance.ShowSeasonId(), password),
        "ArenaHistoryQueryLimitDays": convert_int(excel_instance.ArenaHistoryQueryLimitDays(), password),
    }

def dump_ConstAudioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultSnapShotName": convert_string(excel_instance.DefaultSnapShotName(), password),
        "BattleSnapShotName": convert_string(excel_instance.BattleSnapShotName(), password),
        "RaidSnapShotName": convert_string(excel_instance.RaidSnapShotName(), password),
        "ExSkillCutInSnapShotName": convert_string(excel_instance.ExSkillCutInSnapShotName(), password),
    }

def dump_ConstCombatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SkillHandCount": convert_int(excel_instance.SkillHandCount(), password),
        "DyingTime": convert_int(excel_instance.DyingTime(), password),
        "BuffIconBlinkTime": convert_int(excel_instance.BuffIconBlinkTime(), password),
        "ShowBufficonEXSkill": bool(excel_instance.ShowBufficonEXSkill()),
        "ShowBufficonPassiveSkill": bool(excel_instance.ShowBufficonPassiveSkill()),
        "ShowBufficonExtraPassiveSkill": bool(excel_instance.ShowBufficonExtraPassiveSkill()),
        "ShowBufficonLeaderSkill": bool(excel_instance.ShowBufficonLeaderSkill()),
        "ShowBufficonGroundPassiveSkill": bool(excel_instance.ShowBufficonGroundPassiveSkill()),
        "SuppliesConditionStringId": convert_string(excel_instance.SuppliesConditionStringId(), password),
        "PublicSpeechBubbleOffsetX": convert_float(excel_instance.PublicSpeechBubbleOffsetX(), password),
        "PublicSpeechBubbleOffsetY": convert_float(excel_instance.PublicSpeechBubbleOffsetY(), password),
        "PublicSpeechBubbleOffsetZ": convert_float(excel_instance.PublicSpeechBubbleOffsetZ(), password),
        "ShowRaidListCount": convert_int(excel_instance.ShowRaidListCount(), password),
        "MaxRaidTicketCount": convert_int(excel_instance.MaxRaidTicketCount(), password),
        "MaxRaidBossSkillSlot": convert_int(excel_instance.MaxRaidBossSkillSlot(), password),
        "EngageTimelinePath": convert_string(excel_instance.EngageTimelinePath(), password),
        "EngageWithSupporterTimelinePath": convert_string(excel_instance.EngageWithSupporterTimelinePath(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "TimeLimitAlarm": convert_int(excel_instance.TimeLimitAlarm(), password),
        "EchelonMaxCommonCost": convert_int(excel_instance.EchelonMaxCommonCost(), password),
        "EchelonInitCommonCost": convert_int(excel_instance.EchelonInitCommonCost(), password),
        "SkillSlotCoolTime": convert_int(excel_instance.SkillSlotCoolTime(), password),
        "EnemyRegenCost": convert_int(excel_instance.EnemyRegenCost(), password),
        "ChampionRegenCost": convert_int(excel_instance.ChampionRegenCost(), password),
        "PlayerRegenCostDelay": convert_int(excel_instance.PlayerRegenCostDelay(), password),
        "CrowdControlFactor": convert_int(excel_instance.CrowdControlFactor(), password),
        "RaidOpenScenarioId": convert_string(excel_instance.RaidOpenScenarioId(), password),
        "EliminateRaidOpenScenarioId": convert_string(excel_instance.EliminateRaidOpenScenarioId(), password),
        "DefenceConstA": convert_int(excel_instance.DefenceConstA(), password),
        "DefenceConstB": convert_int(excel_instance.DefenceConstB(), password),
        "DefenceConstC": convert_int(excel_instance.DefenceConstC(), password),
        "DefenceConstD": convert_int(excel_instance.DefenceConstD(), password),
        "AccuracyConstA": convert_int(excel_instance.AccuracyConstA(), password),
        "AccuracyConstB": convert_int(excel_instance.AccuracyConstB(), password),
        "AccuracyConstC": convert_int(excel_instance.AccuracyConstC(), password),
        "AccuracyConstD": convert_int(excel_instance.AccuracyConstD(), password),
        "CriticalConstA": convert_int(excel_instance.CriticalConstA(), password),
        "CriticalConstB": convert_int(excel_instance.CriticalConstB(), password),
        "CriticalConstC": convert_int(excel_instance.CriticalConstC(), password),
        "CriticalConstD": convert_int(excel_instance.CriticalConstD(), password),
        "MaxGroupBuffLevel": convert_int(excel_instance.MaxGroupBuffLevel(), password),
        "EmojiDefaultTime": convert_int(excel_instance.EmojiDefaultTime(), password),
        "TimeLineActionRotateSpeed": convert_int(excel_instance.TimeLineActionRotateSpeed(), password),
        "BodyRotateSpeed": convert_int(excel_instance.BodyRotateSpeed(), password),
        "NormalTimeScale": convert_int(excel_instance.NormalTimeScale(), password),
        "FastTimeScale": convert_int(excel_instance.FastTimeScale(), password),
        "BulletTimeScale": convert_int(excel_instance.BulletTimeScale(), password),
        "UIDisplayDelayAfterSkillCutIn": convert_int(excel_instance.UIDisplayDelayAfterSkillCutIn(), password),
        "UseInitialRangeForCoverMove": bool(excel_instance.UseInitialRangeForCoverMove()),
        "SlowTimeScale": convert_int(excel_instance.SlowTimeScale(), password),
        "AimIKMinDegree": convert_float(excel_instance.AimIKMinDegree(), password),
        "AimIKMaxDegree": convert_float(excel_instance.AimIKMaxDegree(), password),
        "MinimumClearTime": convert_int(excel_instance.MinimumClearTime(), password),
        "MinimumClearLevelGap": convert_int(excel_instance.MinimumClearLevelGap(), password),
        "CheckCheaterMaxUseCostNonArena": convert_int(excel_instance.CheckCheaterMaxUseCostNonArena(), password),
        "CheckCheaterMaxUseCostArena": convert_int(excel_instance.CheckCheaterMaxUseCostArena(), password),
        "AllowedMaxTimeScale": convert_int(excel_instance.AllowedMaxTimeScale(), password),
        "RandomAnimationOutput": convert_int(excel_instance.RandomAnimationOutput(), password),
        "SummonedTeleportDistance": convert_int(excel_instance.SummonedTeleportDistance(), password),
        "ArenaMinimumClearTime": convert_int(excel_instance.ArenaMinimumClearTime(), password),
        "WORLDBOSSBATTLELITTLE": convert_int(excel_instance.WORLDBOSSBATTLELITTLE(), password),
        "WORLDBOSSBATTLEMIDDLE": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLE(), password),
        "WORLDBOSSBATTLEHIGH": convert_int(excel_instance.WORLDBOSSBATTLEHIGH(), password),
        "WORLDBOSSBATTLEVERYHIGH": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGH(), password),
        "WorldRaidAutoSyncTermSecond": convert_int(excel_instance.WorldRaidAutoSyncTermSecond(), password),
        "WorldRaidBossHpDecreaseTerm": convert_int(excel_instance.WorldRaidBossHpDecreaseTerm(), password),
        "WorldRaidBossParcelReactionDelay": convert_int(excel_instance.WorldRaidBossParcelReactionDelay(), password),
        "RaidRankingJumpMinimumWaitingTime": convert_int(excel_instance.RaidRankingJumpMinimumWaitingTime(), password),
        "EffectTeleportDistance": convert_float(excel_instance.EffectTeleportDistance(), password),
        "AuraExitThresholdMargin": convert_int(excel_instance.AuraExitThresholdMargin(), password),
        "TSAInteractionDamageFactor": convert_int(excel_instance.TSAInteractionDamageFactor(), password),
        "VictoryInteractionRate": convert_int(excel_instance.VictoryInteractionRate(), password),
        "EchelonExtensionEngageTimelinePath": convert_string(excel_instance.EchelonExtensionEngageTimelinePath(), password),
        "EchelonExtensionEngageWithSupporterTimelinePath": convert_string(excel_instance.EchelonExtensionEngageWithSupporterTimelinePath(), password),
        "EchelonExtensionVictoryTimelinePath": convert_string(excel_instance.EchelonExtensionVictoryTimelinePath(), password),
        "EchelonExtensionEchelonMaxCommonCost": convert_int(excel_instance.EchelonExtensionEchelonMaxCommonCost(), password),
        "EchelonExtensionEchelonInitCommonCost": convert_int(excel_instance.EchelonExtensionEchelonInitCommonCost(), password),
        "EchelonExtensionCostRegenRatio": convert_int(excel_instance.EchelonExtensionCostRegenRatio(), password),
        "CheckCheaterMaxUseCostMultiFloorRaid": convert_int(excel_instance.CheckCheaterMaxUseCostMultiFloorRaid(), password),
    }

def dump_ConstCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CampaignMainStageMaxRank": convert_int(excel_instance.CampaignMainStageMaxRank(), password),
        "CampaignMainStageBestRecord": convert_int(excel_instance.CampaignMainStageBestRecord(), password),
        "HardAdventurePlayCountRecoverDailyNumber": convert_int(excel_instance.HardAdventurePlayCountRecoverDailyNumber(), password),
        "HardStageCount": convert_int(excel_instance.HardStageCount(), password),
        "TacticRankClearTime": convert_int(excel_instance.TacticRankClearTime(), password),
        "BaseTimeScale": convert_int(excel_instance.BaseTimeScale(), password),
        "GachaPercentage": convert_int(excel_instance.GachaPercentage(), password),
        "AcademyFavorZoneId": convert_int(excel_instance.AcademyFavorZoneId(), password),
        "CafePresetSlotCount": convert_int(excel_instance.CafePresetSlotCount(), password),
        "CafeMonologueIntervalMillisec": convert_int(excel_instance.CafeMonologueIntervalMillisec(), password),
        "CafeMonologueDefaultDuration": convert_int(excel_instance.CafeMonologueDefaultDuration(), password),
        "CafeBubbleIdleDurationMilliSec": convert_int(excel_instance.CafeBubbleIdleDurationMilliSec(), password),
        "FindGiftTimeLimit": convert_int(excel_instance.FindGiftTimeLimit(), password),
        "CafeAutoChargePeriodInMsc": convert_int(excel_instance.CafeAutoChargePeriodInMsc(), password),
        "CafeProductionDecimalPosition": convert_int(excel_instance.CafeProductionDecimalPosition(), password),
        "CafeSetGroupApplyCount": convert_int(excel_instance.CafeSetGroupApplyCount(), password),
        "WeekDungeonFindGiftRewardLimitCount": convert_int(excel_instance.WeekDungeonFindGiftRewardLimitCount(), password),
        "StageFailedCurrencyRefundRate": convert_int(excel_instance.StageFailedCurrencyRefundRate(), password),
        "EnterDeposit": convert_int(excel_instance.EnterDeposit(), password),
        "AccountMaxLevel": convert_int(excel_instance.AccountMaxLevel(), password),
        "MainSquadExpBonus": convert_int(excel_instance.MainSquadExpBonus(), password),
        "SupportSquadExpBonus": convert_int(excel_instance.SupportSquadExpBonus(), password),
        "AccountExpRatio": convert_int(excel_instance.AccountExpRatio(), password),
        "MissionToastLifeTime": convert_int(excel_instance.MissionToastLifeTime(), password),
        "ExpItemInsertLimit": convert_int(excel_instance.ExpItemInsertLimit(), password),
        "ExpItemInsertAccelTime": convert_int(excel_instance.ExpItemInsertAccelTime(), password),
        "CharacterLvUpCoefficient": convert_int(excel_instance.CharacterLvUpCoefficient(), password),
        "EquipmentLvUpCoefficient": convert_int(excel_instance.EquipmentLvUpCoefficient(), password),
        "ExpEquipInsertLimit": convert_int(excel_instance.ExpEquipInsertLimit(), password),
        "EquipLvUpCoefficient": convert_int(excel_instance.EquipLvUpCoefficient(), password),
        "NicknameLength": convert_int(excel_instance.NicknameLength(), password),
        "CraftDurationLength": convert_int(excel_instance.CraftDurationLength(), password),
        "CraftLimitTime": convert_int(excel_instance.CraftLimitTime(), password),
        "ShiftingCraftDurationLength": convert_int(excel_instance.ShiftingCraftDurationLength(), password),
        "ShiftingCraftTicketConsumeAmount": convert_int(excel_instance.ShiftingCraftTicketConsumeAmount(), password),
        "ShiftingCraftSlotMaxCapacity": convert_int(excel_instance.ShiftingCraftSlotMaxCapacity(), password),
        "CraftTicketItemUniqueId": convert_int(excel_instance.CraftTicketItemUniqueId(), password),
        "CraftTicketConsumeAmount": convert_int(excel_instance.CraftTicketConsumeAmount(), password),
        "AcademyEnterCostType": ParcelType(convert_int(excel_instance.AcademyEnterCostType(), password)).name,
        "AcademyEnterCostId": convert_int(excel_instance.AcademyEnterCostId(), password),
        "AcademyTicketCost": convert_int(excel_instance.AcademyTicketCost(), password),
        "MassangerMessageExpireDay": convert_int(excel_instance.MassangerMessageExpireDay(), password),
        "CraftLeafNodeGenerateLv1Count": convert_int(excel_instance.CraftLeafNodeGenerateLv1Count(), password),
        "CraftLeafNodeGenerateLv2Count": convert_int(excel_instance.CraftLeafNodeGenerateLv2Count(), password),
        "TutorialGachaShopId": convert_int(excel_instance.TutorialGachaShopId(), password),
        "BeforehandGachaShopId": convert_int(excel_instance.BeforehandGachaShopId(), password),
        "TutorialGachaGoodsId": convert_int(excel_instance.TutorialGachaGoodsId(), password),
        "EquipmentSlotOpenLevelLength": convert_int(excel_instance.EquipmentSlotOpenLevelLength(), password),
        "ScenarioAutoDelayMillisec": convert_float(excel_instance.ScenarioAutoDelayMillisec(), password),
        "JoinOrCreateClanCoolTimeFromHour": convert_int(excel_instance.JoinOrCreateClanCoolTimeFromHour(), password),
        "ClanMaxMember": convert_int(excel_instance.ClanMaxMember(), password),
        "ClanSearchResultCount": convert_int(excel_instance.ClanSearchResultCount(), password),
        "ClanMaxApplicant": convert_int(excel_instance.ClanMaxApplicant(), password),
        "ClanRejoinCoolTimeFromSecond": convert_int(excel_instance.ClanRejoinCoolTimeFromSecond(), password),
        "ClanWordBalloonMaxCharacter": convert_int(excel_instance.ClanWordBalloonMaxCharacter(), password),
        "CallNameRenameCoolTimeFromHour": convert_int(excel_instance.CallNameRenameCoolTimeFromHour(), password),
        "CallNameMinimumLength": convert_int(excel_instance.CallNameMinimumLength(), password),
        "CallNameMaximumLength": convert_int(excel_instance.CallNameMaximumLength(), password),
        "LobbyToScreenModeWaitTime": convert_int(excel_instance.LobbyToScreenModeWaitTime(), password),
        "ScreenshotToLobbyButtonHideDelay": convert_int(excel_instance.ScreenshotToLobbyButtonHideDelay(), password),
        "PrologueScenarioID01": convert_int(excel_instance.PrologueScenarioID01(), password),
        "PrologueScenarioID02": convert_int(excel_instance.PrologueScenarioID02(), password),
        "TutorialHardStage11": convert_int(excel_instance.TutorialHardStage11(), password),
        "TutorialSpeedButtonStage": convert_int(excel_instance.TutorialSpeedButtonStage(), password),
        "TutorialCharacterDefaultCount": convert_int(excel_instance.TutorialCharacterDefaultCount(), password),
        "TutorialShopCategoryType": convert_float(excel_instance.TutorialShopCategoryType(), password),
        "AdventureStrategyPlayTimeLimitInSeconds": convert_int(excel_instance.AdventureStrategyPlayTimeLimitInSeconds(), password),
        "WeekDungoenTacticPlayTimeLimitInSeconds": convert_int(excel_instance.WeekDungoenTacticPlayTimeLimitInSeconds(), password),
        "RaidTacticPlayTimeLimitInSeconds": convert_int(excel_instance.RaidTacticPlayTimeLimitInSeconds(), password),
        "RaidOpponentListAmount": convert_int(excel_instance.RaidOpponentListAmount(), password),
        "CraftBaseGoldRequiredLength": convert_int(excel_instance.CraftBaseGoldRequiredLength(), password),
        "PostExpiredDayAttendance": convert_int(excel_instance.PostExpiredDayAttendance(), password),
        "PostExpiredDayInventoryOverflow": convert_int(excel_instance.PostExpiredDayInventoryOverflow(), password),
        "PostExpiredDayGameManager": convert_int(excel_instance.PostExpiredDayGameManager(), password),
        "UILabelCharacterWrap": convert_string(excel_instance.UILabelCharacterWrap(), password),
        "RequestTimeOut": convert_float(excel_instance.RequestTimeOut(), password),
        "MailStorageSoftCap": convert_int(excel_instance.MailStorageSoftCap(), password),
        "MailStorageHardCap": convert_int(excel_instance.MailStorageHardCap(), password),
        "ClearDeckStorageSize": convert_int(excel_instance.ClearDeckStorageSize(), password),
        "ClearDeckNoStarViewCount": convert_int(excel_instance.ClearDeckNoStarViewCount(), password),
        "ClearDeck1StarViewCount": convert_int(excel_instance.ClearDeck1StarViewCount(), password),
        "ClearDeck2StarViewCount": convert_int(excel_instance.ClearDeck2StarViewCount(), password),
        "ClearDeck3StarViewCount": convert_int(excel_instance.ClearDeck3StarViewCount(), password),
        "ExSkillLevelMax": convert_int(excel_instance.ExSkillLevelMax(), password),
        "PublicSkillLevelMax": convert_int(excel_instance.PublicSkillLevelMax(), password),
        "PassiveSkillLevelMax": convert_int(excel_instance.PassiveSkillLevelMax(), password),
        "ExtraPassiveSkillLevelMax": convert_int(excel_instance.ExtraPassiveSkillLevelMax(), password),
        "AccountCommentMaxLength": convert_int(excel_instance.AccountCommentMaxLength(), password),
        "CafeSummonCoolTimeFromHour": convert_int(excel_instance.CafeSummonCoolTimeFromHour(), password),
        "LimitedStageDailyClearCount": convert_int(excel_instance.LimitedStageDailyClearCount(), password),
        "LimitedStageEntryTimeLimit": convert_int(excel_instance.LimitedStageEntryTimeLimit(), password),
        "LimitedStageEntryTimeBuffer": convert_int(excel_instance.LimitedStageEntryTimeBuffer(), password),
        "LimitedStagePointAmount": convert_int(excel_instance.LimitedStagePointAmount(), password),
        "LimitedStagePointPerApMin": convert_int(excel_instance.LimitedStagePointPerApMin(), password),
        "LimitedStagePointPerApMax": convert_int(excel_instance.LimitedStagePointPerApMax(), password),
        "AccountLinkReward": convert_int(excel_instance.AccountLinkReward(), password),
        "MonthlyProductCheckDays": convert_int(excel_instance.MonthlyProductCheckDays(), password),
        "WeaponLvUpCoefficient": convert_int(excel_instance.WeaponLvUpCoefficient(), password),
        "ShowRaidMyListCount": convert_int(excel_instance.ShowRaidMyListCount(), password),
        "MaxLevelExpMasterCoinRatio": convert_int(excel_instance.MaxLevelExpMasterCoinRatio(), password),
        "RaidEnterCostType": ParcelType(convert_int(excel_instance.RaidEnterCostType(), password)).name,
        "RaidEnterCostId": convert_int(excel_instance.RaidEnterCostId(), password),
        "RaidTicketCost": convert_int(excel_instance.RaidTicketCost(), password),
        "TimeAttackDungeonScenarioId": convert_string(excel_instance.TimeAttackDungeonScenarioId(), password),
        "TimeAttackDungoenPlayCountPerTicket": convert_int(excel_instance.TimeAttackDungoenPlayCountPerTicket(), password),
        "TimeAttackDungeonEnterCostType": ParcelType(convert_int(excel_instance.TimeAttackDungeonEnterCostType(), password)).name,
        "TimeAttackDungeonEnterCostId": convert_int(excel_instance.TimeAttackDungeonEnterCostId(), password),
        "TimeAttackDungeonEnterCost": convert_int(excel_instance.TimeAttackDungeonEnterCost(), password),
        "ClanLeaderTransferLastLoginLimit": convert_int(excel_instance.ClanLeaderTransferLastLoginLimit(), password),
        "MonthlyProductRepurchasePopupLimit": convert_int(excel_instance.MonthlyProductRepurchasePopupLimit(), password),
        "CommonFavorItemTagsLength": convert_int(excel_instance.CommonFavorItemTagsLength(), password),
        "MaxApMasterCoinPerWeek": convert_int(excel_instance.MaxApMasterCoinPerWeek(), password),
        "CraftOpenExpTier1": convert_int(excel_instance.CraftOpenExpTier1(), password),
        "CraftOpenExpTier2": convert_int(excel_instance.CraftOpenExpTier2(), password),
        "CraftOpenExpTier3": convert_int(excel_instance.CraftOpenExpTier3(), password),
        "CharacterEquipmentGearSlot": convert_int(excel_instance.CharacterEquipmentGearSlot(), password),
        "BirthDayDDay": convert_int(excel_instance.BirthDayDDay(), password),
        "RecommendedFriendsLvDifferenceLimit": convert_int(excel_instance.RecommendedFriendsLvDifferenceLimit(), password),
        "DDosDetectCount": convert_int(excel_instance.DDosDetectCount(), password),
        "DDosCheckIntervalInSeconds": convert_int(excel_instance.DDosCheckIntervalInSeconds(), password),
        "MaxFriendsCount": convert_int(excel_instance.MaxFriendsCount(), password),
        "MaxFriendsRequest": convert_int(excel_instance.MaxFriendsRequest(), password),
        "FriendsSearchRequestCount": convert_int(excel_instance.FriendsSearchRequestCount(), password),
        "FriendsMaxApplicant": convert_int(excel_instance.FriendsMaxApplicant(), password),
        "IdCardDefaultCharacterId": convert_int(excel_instance.IdCardDefaultCharacterId(), password),
        "IdCardDefaultBgId": convert_int(excel_instance.IdCardDefaultBgId(), password),
        "WorldRaidGemEnterCost": convert_int(excel_instance.WorldRaidGemEnterCost(), password),
        "WorldRaidGemEnterAmout": convert_int(excel_instance.WorldRaidGemEnterAmout(), password),
        "FriendIdCardCommentMaxLength": convert_int(excel_instance.FriendIdCardCommentMaxLength(), password),
        "FormationPresetNumberOfEchelonTab": convert_int(excel_instance.FormationPresetNumberOfEchelonTab(), password),
        "FormationPresetNumberOfEchelon": convert_int(excel_instance.FormationPresetNumberOfEchelon(), password),
        "FormationPresetRecentNumberOfEchelon": convert_int(excel_instance.FormationPresetRecentNumberOfEchelon(), password),
        "FormationPresetEchelonTabTextLength": convert_int(excel_instance.FormationPresetEchelonTabTextLength(), password),
        "FormationPresetEchelonSlotTextLength": convert_int(excel_instance.FormationPresetEchelonSlotTextLength(), password),
        "CharProfileRowIntervalKr": convert_int(excel_instance.CharProfileRowIntervalKr(), password),
        "CharProfileRowIntervalJp": convert_int(excel_instance.CharProfileRowIntervalJp(), password),
        "CharProfilePopupRowIntervalKr": convert_int(excel_instance.CharProfilePopupRowIntervalKr(), password),
        "CharProfilePopupRowIntervalJp": convert_int(excel_instance.CharProfilePopupRowIntervalJp(), password),
        "BeforehandGachaCount": convert_int(excel_instance.BeforehandGachaCount(), password),
        "BeforehandGachaGroupId": convert_int(excel_instance.BeforehandGachaGroupId(), password),
        "RenewalDisplayOrderDay": convert_int(excel_instance.RenewalDisplayOrderDay(), password),
        "EmblemDefaultId": convert_int(excel_instance.EmblemDefaultId(), password),
        "BirthdayMailStartDate": convert_string(excel_instance.BirthdayMailStartDate(), password),
        "BirthdayMailRemainDate": convert_int(excel_instance.BirthdayMailRemainDate(), password),
        "BirthdayMailParcelType": ParcelType(convert_int(excel_instance.BirthdayMailParcelType(), password)).name,
        "BirthdayMailParcelId": convert_int(excel_instance.BirthdayMailParcelId(), password),
        "BirthdayMailParcelAmount": convert_int(excel_instance.BirthdayMailParcelAmount(), password),
        "ClearDeckAverageDeckCount": convert_int(excel_instance.ClearDeckAverageDeckCount(), password),
        "ClearDeckWorldRaidSaveConditionCoefficient": convert_int(excel_instance.ClearDeckWorldRaidSaveConditionCoefficient(), password),
        "ClearDeckShowCount": convert_int(excel_instance.ClearDeckShowCount(), password),
        "CharacterMaxLevel": convert_int(excel_instance.CharacterMaxLevel(), password),
        "PotentialBonusStatMaxLevelMaxHP": convert_int(excel_instance.PotentialBonusStatMaxLevelMaxHP(), password),
        "PotentialBonusStatMaxLevelAttackPower": convert_int(excel_instance.PotentialBonusStatMaxLevelAttackPower(), password),
        "PotentialBonusStatMaxLevelHealPower": convert_int(excel_instance.PotentialBonusStatMaxLevelHealPower(), password),
        "PotentialOpenConditionCharacterLevel": convert_int(excel_instance.PotentialOpenConditionCharacterLevel(), password),
        "AssistStrangerMinLevel": convert_int(excel_instance.AssistStrangerMinLevel(), password),
        "AssistStrangerMaxLevel": convert_int(excel_instance.AssistStrangerMaxLevel(), password),
        "MaxBlockedUserCount": convert_int(excel_instance.MaxBlockedUserCount(), password),
        "CafeRandomVisitMinComfortBonus": convert_int(excel_instance.CafeRandomVisitMinComfortBonus(), password),
        "CafeRandomVisitMinLastLogin": convert_int(excel_instance.CafeRandomVisitMinLastLogin(), password),
        "CafeTravelSyncIntervalByMillisec": convert_int(excel_instance.CafeTravelSyncIntervalByMillisec(), password),
        "TTSVCN02": convert_string(excel_instance.TTSVCN02(), password),
    }

def dump_ConstConquestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ManageUnitChange": convert_int(excel_instance.ManageUnitChange(), password),
        "AssistCount": convert_int(excel_instance.AssistCount(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "AnimationUnitAmountMin": convert_int(excel_instance.AnimationUnitAmountMin(), password),
        "AnimationUnitAmountMax": convert_int(excel_instance.AnimationUnitAmountMax(), password),
        "AnimationUnitDelay": convert_float(excel_instance.AnimationUnitDelay(), password),
    }

def dump_ConstEventCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentHardStageCount": convert_int(excel_instance.EventContentHardStageCount(), password),
        "EventStrategyPlayTimeLimitInSeconds": convert_int(excel_instance.EventStrategyPlayTimeLimitInSeconds(), password),
        "SubEventChangeLimitSeconds": convert_int(excel_instance.SubEventChangeLimitSeconds(), password),
        "SubEventInstantClear": bool(excel_instance.SubEventInstantClear()),
        "CardShopProbWeightCount": convert_int(excel_instance.CardShopProbWeightCount(), password),
        "CardShopProbWeightRarity": Rarity(convert_int(excel_instance.CardShopProbWeightRarity(), password)).name,
        "MeetupScenarioReplayResource": convert_string(excel_instance.MeetupScenarioReplayResource(), password),
        "MeetupScenarioReplayTitleLocalize": convert_string(excel_instance.MeetupScenarioReplayTitleLocalize(), password),
        "SpecialOperactionCollectionGroupId": convert_int(excel_instance.SpecialOperactionCollectionGroupId(), password),
        "TreasureNormalVariationAmount": convert_int(excel_instance.TreasureNormalVariationAmount(), password),
        "TreasureLoopVariationAmount": convert_int(excel_instance.TreasureLoopVariationAmount(), password),
        "TreasureLimitVariationLoopCount": convert_int(excel_instance.TreasureLimitVariationLoopCount(), password),
        "TreasureLimitVariationClearLoopCount": convert_int(excel_instance.TreasureLimitVariationClearLoopCount(), password),
        "EventStoryReplayHideEventContentId": convert_int(excel_instance.EventStoryReplayHideEventContentId(), password),
    }

def dump_ConstFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DialogSmoothTime": convert_int(excel_instance.DialogSmoothTime(), password),
        "TalkDialogDurationDefault": convert_int(excel_instance.TalkDialogDurationDefault(), password),
        "ThinkDialogDurationDefault": convert_int(excel_instance.ThinkDialogDurationDefault(), password),
        "IdleThinkDelayMin": convert_int(excel_instance.IdleThinkDelayMin(), password),
        "IdleThinkDelayMax": convert_int(excel_instance.IdleThinkDelayMax(), password),
    }

def dump_ConstMiniGameShootingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NormalStageId": convert_int(excel_instance.NormalStageId(), password),
        "NormalSectionCount": convert_int(excel_instance.NormalSectionCount(), password),
        "HardStageId": convert_int(excel_instance.HardStageId(), password),
        "HardSectionCount": convert_int(excel_instance.HardSectionCount(), password),
        "FreeStageId": convert_int(excel_instance.FreeStageId(), password),
        "FreeSectionCount": convert_int(excel_instance.FreeSectionCount(), password),
        "PlayerCharacterIdLength": convert_int(excel_instance.PlayerCharacterIdLength(), password),
        "HiddenPlayerCharacterId": convert_int(excel_instance.HiddenPlayerCharacterId(), password),
        "CameraSmoothTime": convert_float(excel_instance.CameraSmoothTime(), password),
        "SpawnEffectPath": convert_string(excel_instance.SpawnEffectPath(), password),
        "WaitTimeAfterSpawn": convert_float(excel_instance.WaitTimeAfterSpawn(), password),
        "FreeGearInterval": convert_int(excel_instance.FreeGearInterval(), password),
    }

def dump_ConstMinigameTBGExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestMapBoundaryOffsetLeft": convert_float(excel_instance.ConquestMapBoundaryOffsetLeft(), password),
        "ConquestMapBoundaryOffsetRight": convert_float(excel_instance.ConquestMapBoundaryOffsetRight(), password),
        "ConquestMapBoundaryOffsetTop": convert_float(excel_instance.ConquestMapBoundaryOffsetTop(), password),
        "ConquestMapBoundaryOffsetBottom": convert_float(excel_instance.ConquestMapBoundaryOffsetBottom(), password),
        "ConquestMapCenterOffsetX": convert_float(excel_instance.ConquestMapCenterOffsetX(), password),
        "ConquestMapCenterOffsetY": convert_float(excel_instance.ConquestMapCenterOffsetY(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngle(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
        "ThemaLoadingProgressTime": convert_float(excel_instance.ThemaLoadingProgressTime(), password),
        "MapAllyRotation": convert_float(excel_instance.MapAllyRotation(), password),
        "AniAllyBattleAttack": convert_string(excel_instance.AniAllyBattleAttack(), password),
        "EffectAllyBattleAttack": convert_string(excel_instance.EffectAllyBattleAttack(), password),
        "EffectAllyBattleDamage": convert_string(excel_instance.EffectAllyBattleDamage(), password),
        "AniEnemyBattleAttack": convert_string(excel_instance.AniEnemyBattleAttack(), password),
        "EffectEnemyBattleAttack": convert_string(excel_instance.EffectEnemyBattleAttack(), password),
        "EffectEnemyBattleDamage": convert_string(excel_instance.EffectEnemyBattleDamage(), password),
        "EncounterAllyRotation": convert_float(excel_instance.EncounterAllyRotation(), password),
        "EncounterEnemyRotation": convert_float(excel_instance.EncounterEnemyRotation(), password),
        "EncounterRewardReceiveIndex": convert_int(excel_instance.EncounterRewardReceiveIndex(), password),
    }

def dump_ConstNewbieContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NewbieGachaReleaseDate": convert_string(excel_instance.NewbieGachaReleaseDate(), password),
        "NewbieGachaCheckDays": convert_int(excel_instance.NewbieGachaCheckDays(), password),
        "NewbieGachaTokenGraceTime": convert_int(excel_instance.NewbieGachaTokenGraceTime(), password),
        "NewbieAttendanceReleaseDate": convert_string(excel_instance.NewbieAttendanceReleaseDate(), password),
        "NewbieAttendanceStartableEndDay": convert_int(excel_instance.NewbieAttendanceStartableEndDay(), password),
        "NewbieAttendanceEndDay": convert_int(excel_instance.NewbieAttendanceEndDay(), password),
    }

def dump_ConstStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "HexaMapBoundaryOffset": convert_float(excel_instance.HexaMapBoundaryOffset(), password),
        "HexaMapStartCameraOffset": convert_float(excel_instance.HexaMapStartCameraOffset(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
        "HealCostType": CurrencyTypes(convert_int(excel_instance.HealCostType(), password)).name,
        "HealCostAmountLength": convert_int(excel_instance.HealCostAmountLength(), password),
        "CanHealHpRate": convert_int(excel_instance.CanHealHpRate(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "AdventureEchelonCount": convert_int(excel_instance.AdventureEchelonCount(), password),
        "RaidEchelonCount": convert_int(excel_instance.RaidEchelonCount(), password),
        "DefaultEchelonCount": convert_int(excel_instance.DefaultEchelonCount(), password),
        "EventContentEchelonCount": convert_int(excel_instance.EventContentEchelonCount(), password),
        "TimeAttackDungeonEchelonCount": convert_int(excel_instance.TimeAttackDungeonEchelonCount(), password),
        "WorldRaidEchelonCount": convert_int(excel_instance.WorldRaidEchelonCount(), password),
        "TacticSkipClearTimeSeconds": convert_int(excel_instance.TacticSkipClearTimeSeconds(), password),
        "TacticSkipFramePerSecond": convert_int(excel_instance.TacticSkipFramePerSecond(), password),
        "ConquestEchelonCount": convert_int(excel_instance.ConquestEchelonCount(), password),
        "StoryEchelonCount": convert_int(excel_instance.StoryEchelonCount(), password),
        "MultiSweepPresetCount": convert_int(excel_instance.MultiSweepPresetCount(), password),
        "MultiSweepPresetNameMaxLength": convert_int(excel_instance.MultiSweepPresetNameMaxLength(), password),
        "MultiSweepPresetSelectStageMaxCount": convert_int(excel_instance.MultiSweepPresetSelectStageMaxCount(), password),
        "MultiSweepPresetMaxSweepCount": convert_int(excel_instance.MultiSweepPresetMaxSweepCount(), password),
        "MultiSweepPresetSelectParcelMaxCount": convert_int(excel_instance.MultiSweepPresetSelectParcelMaxCount(), password),
    }

def dump_ContentsFeverExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConditionContent": FeverBattleType(convert_int(excel_instance.ConditionContent(), password)).name,
        "SkillFeverCheckCondition": SkillPriorityCheckTarget(convert_int(excel_instance.SkillFeverCheckCondition(), password)).name,
        "SkillCostFever": convert_int(excel_instance.SkillCostFever(), password),
        "FeverStartTime": convert_int(excel_instance.FeverStartTime(), password),
        "FeverDurationTime": convert_int(excel_instance.FeverDurationTime(), password),
    }

def dump_CostumeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeGroupId": convert_int(excel_instance.CostumeGroupId(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "IsDefault": bool(excel_instance.IsDefault()),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "ReleaseDate": convert_string(excel_instance.ReleaseDate(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDate(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDate(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "CharacterSkillListGroupId": convert_int(excel_instance.CharacterSkillListGroupId(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceName(), password),
        "SpineResourceNameDiorama": convert_string(excel_instance.SpineResourceNameDiorama(), password),
        "SpineResourceNameDioramaForFormConversionLength": convert_int(excel_instance.SpineResourceNameDioramaForFormConversionLength(), password),
        "EntityMaterialType": EntityMaterialType(convert_int(excel_instance.EntityMaterialType(), password)).name,
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabName(), password),
        "CafeModelPrefabName": convert_string(excel_instance.CafeModelPrefabName(), password),
        "EchelonModelPrefabName": convert_string(excel_instance.EchelonModelPrefabName(), password),
        "StrategyModelPrefabName": convert_string(excel_instance.StrategyModelPrefabName(), password),
        "TextureDir": convert_string(excel_instance.TextureDir(), password),
        "CollectionTexturePath": convert_string(excel_instance.CollectionTexturePath(), password),
        "CollectionBGTexturePath": convert_string(excel_instance.CollectionBGTexturePath(), password),
        "CombatStyleTexturePath": convert_string(excel_instance.CombatStyleTexturePath(), password),
        "UseObjectHPBAR": bool(excel_instance.UseObjectHPBAR()),
        "TextureBoss": convert_string(excel_instance.TextureBoss(), password),
        "TextureSkillCardLength": convert_int(excel_instance.TextureSkillCardLength(), password),
        "InformationPacel": convert_string(excel_instance.InformationPacel(), password),
        "AnimationSSR": convert_string(excel_instance.AnimationSSR(), password),
        "EnterStrategyAnimationName": convert_string(excel_instance.EnterStrategyAnimationName(), password),
        "AnimationValidator": bool(excel_instance.AnimationValidator()),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupId(), password),
        "ShowObjectHpStatus": bool(excel_instance.ShowObjectHpStatus()),
    }

def dump_CouponCompleteExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "GiftIdLength": convert_int(excel_instance.GiftIdLength(), password),
        "Comment": convert_string(excel_instance.Comment(), password),
        "ExpiredDay": convert_int(excel_instance.ExpiredDay(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_CouponStuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StuffId": convert_int(excel_instance.StuffId(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "LimitAmount": convert_int(excel_instance.LimitAmount(), password),
        "CouponStuffNameLocalizeKey": convert_string(excel_instance.CouponStuffNameLocalizeKey(), password),
    }

def dump_CumulativeTimeRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Description": convert_string(excel_instance.Description(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "TimeConditionLength": convert_int(excel_instance.TimeConditionLength(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardIdLength": convert_int(excel_instance.RewardIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_DefaultCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "FavoriteCharacter": bool(excel_instance.FavoriteCharacter()),
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "FavorRank": convert_int(excel_instance.FavorRank(), password),
        "StarGrade": convert_int(excel_instance.StarGrade(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevel(), password),
        "PassiveSkillLevel": convert_int(excel_instance.PassiveSkillLevel(), password),
        "ExtraPassiveSkillLevel": convert_int(excel_instance.ExtraPassiveSkillLevel(), password),
        "CommonSkillLevel": convert_int(excel_instance.CommonSkillLevel(), password),
        "LeaderSkillLevel": convert_int(excel_instance.LeaderSkillLevel(), password),
    }

def dump_DefaultEchelonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EchlonId": convert_int(excel_instance.EchlonId(), password),
        "LeaderId": convert_int(excel_instance.LeaderId(), password),
        "MainIdLength": convert_int(excel_instance.MainIdLength(), password),
        "SupportIdLength": convert_int(excel_instance.SupportIdLength(), password),
        "TssId": convert_int(excel_instance.TssId(), password),
    }

def dump_DefaultFurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Location": FurnitureLocation(convert_int(excel_instance.Location(), password)).name,
        "PositionX": convert_float(excel_instance.PositionX(), password),
        "PositionY": convert_float(excel_instance.PositionY(), password),
        "Rotation": convert_float(excel_instance.Rotation(), password),
    }

def dump_DefaultMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "MailSendPeriodFrom": convert_string(excel_instance.MailSendPeriodFrom(), password),
        "MailSendPeriodTo": convert_string(excel_instance.MailSendPeriodTo(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_DefaultParcelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "ParcelAmount": convert_int(excel_instance.ParcelAmount(), password),
    }

def dump_DuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ItemCategory": ItemCategory(convert_int(excel_instance.ItemCategory(), password)).name,
        "ItemId": convert_int(excel_instance.ItemId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_EchelonConstraintExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsWhiteList": bool(excel_instance.IsWhiteList()),
        "CharacterIdLength": convert_int(excel_instance.CharacterIdLength(), password),
        "PersonalityIdLength": convert_int(excel_instance.PersonalityIdLength(), password),
        "WeaponType": WeaponType(convert_int(excel_instance.WeaponType(), password)).name,
        "School": School(convert_int(excel_instance.School(), password)).name,
        "Club": Club(convert_int(excel_instance.Club(), password)).name,
        "Role": convert_float(excel_instance.Role(), password),
    }

def dump_EliminateRaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelUniqueIdLength": convert_int(excel_instance.RewardParcelUniqueIdLength(), password),
        "RewardParcelUniqueNameLength": convert_int(excel_instance.RewardParcelUniqueNameLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EliminateRaidRankingRewardUOExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelUniqueIdLength": convert_int(excel_instance.RewardParcelUniqueIdLength(), password),
        "RewardParcelUniqueNameLength": convert_int(excel_instance.RewardParcelUniqueNameLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EliminateRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "SeasonDisplay": convert_int(excel_instance.SeasonDisplay(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartData(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndData(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "LobbyTableBGPath": convert_string(excel_instance.LobbyTableBGPath(), password),
        "LobbyScreenBGPath": convert_string(excel_instance.LobbyScreenBGPath(), password),
        "OpenRaidBossGroup01": convert_string(excel_instance.OpenRaidBossGroup01(), password),
        "OpenRaidBossGroup02": convert_string(excel_instance.OpenRaidBossGroup02(), password),
        "OpenRaidBossGroup03": convert_string(excel_instance.OpenRaidBossGroup03(), password),
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauage(), password),
        "StackedSeasonRewardGaugeLength": convert_int(excel_instance.StackedSeasonRewardGaugeLength(), password),
        "SeasonRewardIdLength": convert_int(excel_instance.SeasonRewardIdLength(), password),
        "LimitedRewardIdNormal": convert_int(excel_instance.LimitedRewardIdNormal(), password),
        "LimitedRewardIdHard": convert_int(excel_instance.LimitedRewardIdHard(), password),
        "LimitedRewardIdVeryhard": convert_int(excel_instance.LimitedRewardIdVeryhard(), password),
        "LimitedRewardIdHardcore": convert_int(excel_instance.LimitedRewardIdHardcore(), password),
        "LimitedRewardIdExtreme": convert_int(excel_instance.LimitedRewardIdExtreme(), password),
        "LimitedRewardIdInsane": convert_int(excel_instance.LimitedRewardIdInsane(), password),
        "LimitedRewardIdTorment": convert_int(excel_instance.LimitedRewardIdTorment(), password),
    }

def dump_EliminateRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndex()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSync()),
        "RaidBossGroup": convert_string(excel_instance.RaidBossGroup(), password),
        "RaidEnterCostType": ParcelType(convert_int(excel_instance.RaidEnterCostType(), password)).name,
        "RaidEnterCostId": convert_int(excel_instance.RaidEnterCostId(), password),
        "RaidEnterCostAmount": convert_int(excel_instance.RaidEnterCostAmount(), password),
        "BossSpinePath": convert_string(excel_instance.BossSpinePath(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterId(), password),
        "BossCharacterIdLength": convert_int(excel_instance.BossCharacterIdLength(), password),
        "Difficulty": Difficulty(convert_int(excel_instance.Difficulty(), password)).name,
        "IsOpen": bool(excel_instance.IsOpen()),
        "MaxPlayerCount": convert_int(excel_instance.MaxPlayerCount(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTime(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "GroundDevName": convert_string(excel_instance.GroundDevName(), password),
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLine(), password),
        "TacticEnvironment": TacticEnvironment(convert_int(excel_instance.TacticEnvironment(), password)).name,
        "DefaultClearScore": convert_int(excel_instance.DefaultClearScore(), password),
        "MaximumScore": convert_int(excel_instance.MaximumScore(), password),
        "PerSecondMinusScore": convert_int(excel_instance.PerSecondMinusScore(), password),
        "HPPercentScore": convert_int(excel_instance.HPPercentScore(), password),
        "MinimumAcquisitionScore": convert_int(excel_instance.MinimumAcquisitionScore(), password),
        "MaximumAcquisitionScore": convert_int(excel_instance.MaximumAcquisitionScore(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePathLength": convert_int(excel_instance.BattleReadyTimelinePathLength(), password),
        "BattleReadyTimelinePhaseStartLength": convert_int(excel_instance.BattleReadyTimelinePhaseStartLength(), password),
        "BattleReadyTimelinePhaseEndLength": convert_int(excel_instance.BattleReadyTimelinePhaseEndLength(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKey(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_EliminateRaidStageLimitedRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LimitedRewardId": convert_int(excel_instance.LimitedRewardId(), password),
        "LimitedRewardParcelTypeLength": convert_int(excel_instance.LimitedRewardParcelTypeLength(), password),
        "LimitedRewardParcelUniqueIdLength": convert_int(excel_instance.LimitedRewardParcelUniqueIdLength(), password),
        "LimitedRewardAmountLength": convert_int(excel_instance.LimitedRewardAmountLength(), password),
    }

def dump_EliminateRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_EliminateRaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_int(excel_instance.SeasonRewardId(), password),
        "SeasonRewardParcelTypeLength": convert_int(excel_instance.SeasonRewardParcelTypeLength(), password),
        "SeasonRewardParcelUniqueIdLength": convert_int(excel_instance.SeasonRewardParcelUniqueIdLength(), password),
        "SeasonRewardParcelUniqueNameLength": convert_int(excel_instance.SeasonRewardParcelUniqueNameLength(), password),
        "SeasonRewardAmountLength": convert_int(excel_instance.SeasonRewardAmountLength(), password),
    }

def dump_EmoticonSpecialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "CharacterUniqueId": convert_int(excel_instance.CharacterUniqueId(), password),
        "Random": convert_string(excel_instance.Random(), password),
    }

def dump_EquipmentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EquipmentCategory": EquipmentCategory(convert_int(excel_instance.EquipmentCategory(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Wear": bool(excel_instance.Wear()),
        "MaxLevel": convert_int(excel_instance.MaxLevel(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "TierInit": convert_int(excel_instance.TierInit(), password),
        "NextTierEquipment": convert_int(excel_instance.NextTierEquipment(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "ImageName": convert_string(excel_instance.ImageName(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQuality(), password),
        "ShopCategoryLength": convert_int(excel_instance.ShopCategoryLength(), password),
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeId(), password),
    }

def dump_EquipmentLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "TierLevelExpLength": convert_int(excel_instance.TierLevelExpLength(), password),
        "TotalExpLength": convert_int(excel_instance.TotalExpLength(), password),
    }

def dump_EquipmentStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EquipmentId": convert_int(excel_instance.EquipmentId(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "StatTypeLength": convert_int(excel_instance.StatTypeLength(), password),
        "MinStatLength": convert_int(excel_instance.MinStatLength(), password),
        "MaxStatLength": convert_int(excel_instance.MaxStatLength(), password),
        "LevelUpInsertLimit": convert_int(excel_instance.LevelUpInsertLimit(), password),
        "LevelUpFeedExp": convert_int(excel_instance.LevelUpFeedExp(), password),
        "LevelUpFeedCostCurrency": CurrencyTypes(convert_int(excel_instance.LevelUpFeedCostCurrency(), password)).name,
        "LevelUpFeedCostAmount": convert_int(excel_instance.LevelUpFeedCostAmount(), password),
        "EquipmentCategory": EquipmentCategory(convert_int(excel_instance.EquipmentCategory(), password)).name,
        "LevelUpFeedAddExp": convert_int(excel_instance.LevelUpFeedAddExp(), password),
        "DefaultMaxLevel": convert_int(excel_instance.DefaultMaxLevel(), password),
        "TranscendenceMax": convert_int(excel_instance.TranscendenceMax(), password),
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupId(), password),
    }

def dump_EventContentArchiveBannerOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "OffsetX": convert_float(excel_instance.OffsetX(), password),
        "OffsetY": convert_float(excel_instance.OffsetY(), password),
        "ScaleX": convert_float(excel_instance.ScaleX(), password),
        "ScaleY": convert_float(excel_instance.ScaleY(), password),
    }

def dump_EventContentBoxGachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
    }

def dump_EventContentBoxGachaManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
        "IsLoop": bool(excel_instance.IsLoop()),
    }

def dump_EventContentBoxGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "GroupElementAmount": convert_int(excel_instance.GroupElementAmount(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "IsPrize": bool(excel_instance.IsPrize()),
        "GoodsIdLength": convert_int(excel_instance.GoodsIdLength(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
    }

def dump_EventContentBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentBuffId": convert_int(excel_instance.EventContentBuffId(), password),
        "IsBuff": bool(excel_instance.IsBuff()),
        "CharacterTag": Tag(convert_int(excel_instance.CharacterTag(), password)).name,
        "EnumType": EventContentBuffFindRule(convert_int(excel_instance.EnumType(), password)).name,
        "EnumTypeValueLength": convert_int(excel_instance.EnumTypeValueLength(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "BuffDescriptionLocalizeCodeId": convert_string(excel_instance.BuffDescriptionLocalizeCodeId(), password),
    }

def dump_EventContentBuffGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "BuffContentId": convert_int(excel_instance.BuffContentId(), password),
        "BuffGroupId": convert_int(excel_instance.BuffGroupId(), password),
        "BuffGroupNameLocalizeCodeId": convert_string(excel_instance.BuffGroupNameLocalizeCodeId(), password),
        "EventContentBuffId1": convert_int(excel_instance.EventContentBuffId1(), password),
        "BuffNameLocalizeCodeId1": convert_string(excel_instance.BuffNameLocalizeCodeId1(), password),
        "BuffDescriptionIconPath1": convert_string(excel_instance.BuffDescriptionIconPath1(), password),
        "EventContentBuffId2": convert_int(excel_instance.EventContentBuffId2(), password),
        "BuffNameLocalizeCodeId2": convert_string(excel_instance.BuffNameLocalizeCodeId2(), password),
        "BuffDescriptionIconPath2": convert_string(excel_instance.BuffDescriptionIconPath2(), password),
        "EventContentDebuffId": convert_int(excel_instance.EventContentDebuffId(), password),
        "DebuffNameLocalizeCodeId": convert_string(excel_instance.DebuffNameLocalizeCodeId(), password),
        "DeBuffDescriptionIconPath": convert_string(excel_instance.DeBuffDescriptionIconPath(), password),
        "BuffGroupProb": convert_int(excel_instance.BuffGroupProb(), password),
    }

def dump_EventContentCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CardGroupId": convert_int(excel_instance.CardGroupId(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "BackIconPath": convert_string(excel_instance.BackIconPath(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
    }

def dump_EventContentCardShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "CardGroupId": convert_int(excel_instance.CardGroupId(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbWeight1": convert_int(excel_instance.ProbWeight1(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EventContentChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ChangeCount": convert_int(excel_instance.ChangeCount(), password),
        "IsLast": bool(excel_instance.IsLast()),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "ChangeCostType": ParcelType(convert_int(excel_instance.ChangeCostType(), password)).name,
        "ChangeCostId": convert_int(excel_instance.ChangeCostId(), password),
        "ChangeCostAmount": convert_int(excel_instance.ChangeCostAmount(), password),
    }

def dump_EventContentChangeScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ChangeType": EventChangeType(convert_int(excel_instance.ChangeType(), password)).name,
        "ChangeCount": convert_int(excel_instance.ChangeCount(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
    }

def dump_EventContentCharacterBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "EventContentItemTypeLength": convert_int(excel_instance.EventContentItemTypeLength(), password),
        "BonusPercentageLength": convert_int(excel_instance.BonusPercentageLength(), password),
    }

def dump_EventContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "UnlockConditionType": CollectionUnlockType(convert_int(excel_instance.UnlockConditionType(), password)).name,
        "UnlockConditionParameterLength": convert_int(excel_instance.UnlockConditionParameterLength(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "UnlockConditionCount": convert_int(excel_instance.UnlockConditionCount(), password),
        "IsObject": bool(excel_instance.IsObject()),
        "IsObjectOnFullResource": bool(excel_instance.IsObjectOnFullResource()),
        "IsHorizon": bool(excel_instance.IsHorizon()),
        "EmblemResource": convert_string(excel_instance.EmblemResource(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResource(), password),
        "FullResource": convert_string(excel_instance.FullResource(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeId(), password),
    }

def dump_EventContentCurrencyItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentItemType": EventContentItemType(convert_int(excel_instance.EventContentItemType(), password)).name,
        "ItemUniqueId": convert_int(excel_instance.ItemUniqueId(), password),
        "UseShortCutContentType": convert_string(excel_instance.UseShortCutContentType(), password),
    }

def dump_EventContentDebuffRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventStageId": convert_int(excel_instance.EventStageId(), password),
        "EventContentItemType": EventContentItemType(convert_int(excel_instance.EventContentItemType(), password)).name,
        "RewardPercentage": convert_int(excel_instance.RewardPercentage(), password),
    }

def dump_EventContentDiceRaceEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentDiceRaceResultType": EventContentDiceRaceResultType(convert_int(excel_instance.EventContentDiceRaceResultType(), password)).name,
        "IsDiceResult": bool(excel_instance.IsDiceResult()),
        "AniClip": convert_string(excel_instance.AniClip(), password),
        "VoiceIdLength": convert_int(excel_instance.VoiceIdLength(), password),
    }

def dump_EventContentDiceRaceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DiceCostGoodsId": convert_int(excel_instance.DiceCostGoodsId(), password),
        "SkipableLap": convert_int(excel_instance.SkipableLap(), password),
        "DiceRacePawnPrefab": convert_string(excel_instance.DiceRacePawnPrefab(), password),
        "IsUsingFixedDice": bool(excel_instance.IsUsingFixedDice()),
        "DiceRaceEventTypeLength": convert_int(excel_instance.DiceRaceEventTypeLength(), password),
    }

def dump_EventContentDiceRaceNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "NodeId": convert_int(excel_instance.NodeId(), password),
        "EventContentDiceRaceNodeType": EventContentDiceRaceNodeType(convert_int(excel_instance.EventContentDiceRaceNodeType(), password)).name,
        "MoveForwardTypeArg": convert_int(excel_instance.MoveForwardTypeArg(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_EventContentDiceRaceProbExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentDiceRaceResultType": EventContentDiceRaceResultType(convert_int(excel_instance.EventContentDiceRaceResultType(), password)).name,
        "CostItemId": convert_int(excel_instance.CostItemId(), password),
        "CostItemAmount": convert_int(excel_instance.CostItemAmount(), password),
        "DiceResult": convert_int(excel_instance.DiceResult(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
    }

def dump_EventContentDiceRaceTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "RewardID": convert_int(excel_instance.RewardID(), password),
        "RequiredLapFinishCount": convert_int(excel_instance.RequiredLapFinishCount(), password),
        "DisplayLapFinishCount": convert_int(excel_instance.DisplayLapFinishCount(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EventContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "BgImagePath": convert_string(excel_instance.BgImagePath(), password),
    }

def dump_EventContentFortuneGachaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
    }

def dump_EventContentFortuneGachaModifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TargetGrade": convert_int(excel_instance.TargetGrade(), password),
        "ProbModifyStartCount": convert_int(excel_instance.ProbModifyStartCount(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabName(), password),
        "BucketImagePath": convert_string(excel_instance.BucketImagePath(), password),
        "ShopBgImagePath": convert_string(excel_instance.ShopBgImagePath(), password),
        "TitleLocalizeKey": convert_string(excel_instance.TitleLocalizeKey(), password),
    }

def dump_EventContentFortuneGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Grade": convert_int(excel_instance.Grade(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupId(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbModifyValue": convert_int(excel_instance.ProbModifyValue(), password),
        "ProbModifyLimit": convert_int(excel_instance.ProbModifyLimit(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EventContentLobbyMenuExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "IconSpriteName": convert_string(excel_instance.IconSpriteName(), password),
        "ButtonText": convert_string(excel_instance.ButtonText(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "IconOffsetX": convert_float(excel_instance.IconOffsetX(), password),
        "IconOffsetY": convert_float(excel_instance.IconOffsetY(), password),
        "ReddotSpriteName": convert_string(excel_instance.ReddotSpriteName(), password),
    }

def dump_EventContentLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPath(), password),
        "LocationResetScheduleCount": convert_int(excel_instance.LocationResetScheduleCount(), password),
        "ScheduleEventPointCostParcelType": ParcelType(convert_int(excel_instance.ScheduleEventPointCostParcelType(), password)).name,
        "ScheduleEventPointCostParcelId": convert_int(excel_instance.ScheduleEventPointCostParcelId(), password),
        "ScheduleEventPointCostParcelAmount": convert_int(excel_instance.ScheduleEventPointCostParcelAmount(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "InformationGroupId": convert_int(excel_instance.InformationGroupId(), password),
    }

def dump_EventContentLocationRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Location": convert_string(excel_instance.Location(), password),
        "ScheduleGroupId": convert_int(excel_instance.ScheduleGroupId(), password),
        "OrderInGroup": convert_int(excel_instance.OrderInGroup(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "ProgressTexture": convert_string(excel_instance.ProgressTexture(), password),
        "VoiceIdLength": convert_int(excel_instance.VoiceIdLength(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocationRank": convert_int(excel_instance.LocationRank(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmount(), password),
        "SecretStoneProb": convert_int(excel_instance.SecretStoneProb(), password),
        "ExtraFavorExp": convert_int(excel_instance.ExtraFavorExp(), password),
        "ExtraFavorExpProb": convert_int(excel_instance.ExtraFavorExpProb(), password),
        "ExtraRewardParcelTypeLength": convert_int(excel_instance.ExtraRewardParcelTypeLength(), password),
        "ExtraRewardParcelIdLength": convert_int(excel_instance.ExtraRewardParcelIdLength(), password),
        "ExtraRewardAmountLength": convert_int(excel_instance.ExtraRewardAmountLength(), password),
        "ExtraRewardProbLength": convert_int(excel_instance.ExtraRewardProbLength(), password),
        "IsExtraRewardDisplayedLength": convert_int(excel_instance.IsExtraRewardDisplayedLength(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_EventContentMeetupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ConditionScenarioGroupId": convert_int(excel_instance.ConditionScenarioGroupId(), password),
        "ConditionType": MeetupConditionType(convert_int(excel_instance.ConditionType(), password)).name,
        "ConditionParameterLength": convert_int(excel_instance.ConditionParameterLength(), password),
        "ConditionPrintType": MeetupConditionPrintType(convert_int(excel_instance.ConditionPrintType(), password)).name,
    }

def dump_EventContentMeetupInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CostParcelType": ParcelType(convert_int(excel_instance.CostParcelType(), password)).name,
        "CostId": convert_int(excel_instance.CostId(), password),
        "CostAmount": convert_int(excel_instance.CostAmount(), password),
    }

def dump_EventContentMiniEventShortCutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "ShorcutContentType": EventTargetType(convert_int(excel_instance.ShorcutContentType(), password)).name,
        "ShortcutUI": convert_string(excel_instance.ShortcutUI(), password),
    }

def dump_EventContentMiniEventTokenExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ItemUniqueId": convert_int(excel_instance.ItemUniqueId(), password),
        "MaximumAmount": convert_int(excel_instance.MaximumAmount(), password),
    }

def dump_EventContentMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "GroupName": convert_string(excel_instance.GroupName(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetType(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "PreMissionIdLength": convert_int(excel_instance.PreMissionIdLength(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ShortcutUILength": convert_int(excel_instance.ShortcutUILength(), password),
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "IsCompleteExtensionTime": bool(excel_instance.IsCompleteExtensionTime()),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameterLength": convert_int(excel_instance.CompleteConditionParameterLength(), password),
        "CompleteConditionParameterTagLength": convert_int(excel_instance.CompleteConditionParameterTagLength(), password),
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "CompleteConditionMissionIdLength": convert_int(excel_instance.CompleteConditionMissionIdLength(), password),
        "CompleteConditionMissionCount": convert_int(excel_instance.CompleteConditionMissionCount(), password),
        "MissionRewardParcelTypeLength": convert_int(excel_instance.MissionRewardParcelTypeLength(), password),
        "MissionRewardParcelIdLength": convert_int(excel_instance.MissionRewardParcelIdLength(), password),
        "MissionRewardAmountLength": convert_int(excel_instance.MissionRewardAmountLength(), password),
        "ConditionRewardParcelTypeLength": convert_int(excel_instance.ConditionRewardParcelTypeLength(), password),
        "ConditionRewardParcelIdLength": convert_int(excel_instance.ConditionRewardParcelIdLength(), password),
        "ConditionRewardAmountLength": convert_int(excel_instance.ConditionRewardAmountLength(), password),
    }

def dump_EventContentPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_EventContentScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ReplayDisplayGroup": convert_int(excel_instance.ReplayDisplayGroup(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "RecollectionNumber": convert_int(excel_instance.RecollectionNumber(), password),
        "IsRecollection": bool(excel_instance.IsRecollection()),
        "IsMeetup": bool(excel_instance.IsMeetup()),
        "IsOmnibus": bool(excel_instance.IsOmnibus()),
        "ScenarioGroupIdLength": convert_int(excel_instance.ScenarioGroupIdLength(), password),
        "ScenarioConditionType": EventContentScenarioConditionType(convert_int(excel_instance.ScenarioConditionType(), password)).name,
        "ConditionAmount": convert_int(excel_instance.ConditionAmount(), password),
        "ConditionEventContentId": convert_int(excel_instance.ConditionEventContentId(), password),
        "ClearedScenarioGroupId": convert_int(excel_instance.ClearedScenarioGroupId(), password),
        "RecollectionSummaryLocalizeScenarioId": convert_uint(excel_instance.RecollectionSummaryLocalizeScenarioId(), password),
        "RecollectionResource": convert_string(excel_instance.RecollectionResource(), password),
        "IsRecollectionHorizon": bool(excel_instance.IsRecollectionHorizon()),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardIdLength": convert_int(excel_instance.RewardIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_EventContentSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "OriginalEventContentId": convert_int(excel_instance.OriginalEventContentId(), password),
        "IsReturn": bool(excel_instance.IsReturn()),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "OpenConditionContent": OpenConditionContent(convert_int(excel_instance.OpenConditionContent(), password)).name,
        "EventDisplay": bool(excel_instance.EventDisplay()),
        "IconOrder": convert_int(excel_instance.IconOrder(), password),
        "SubEventType": SubEventType(convert_int(excel_instance.SubEventType(), password)).name,
        "SubEvent": bool(excel_instance.SubEvent()),
        "EventItemId": convert_int(excel_instance.EventItemId(), password),
        "MainEventId": convert_int(excel_instance.MainEventId(), password),
        "EventChangeOpenCondition": convert_int(excel_instance.EventChangeOpenCondition(), password),
        "BeforehandExposedTime": convert_string(excel_instance.BeforehandExposedTime(), password),
        "EventContentOpenTime": convert_string(excel_instance.EventContentOpenTime(), password),
        "EventContentCloseTime": convert_string(excel_instance.EventContentCloseTime(), password),
        "ExtensionTime": convert_string(excel_instance.ExtensionTime(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPath(), password),
        "SubIconParcelPath": convert_string(excel_instance.SubIconParcelPath(), password),
        "BeforehandBgImagePath": convert_string(excel_instance.BeforehandBgImagePath(), password),
        "MinigamePrologScenarioGroupId": convert_int(excel_instance.MinigamePrologScenarioGroupId(), password),
        "BeforehandScenarioGroupIdLength": convert_int(excel_instance.BeforehandScenarioGroupIdLength(), password),
        "MainBannerImagePath": convert_string(excel_instance.MainBannerImagePath(), password),
        "MainBgImagePath": convert_string(excel_instance.MainBgImagePath(), password),
        "ShiftTriggerStageId": convert_int(excel_instance.ShiftTriggerStageId(), password),
        "ShiftMainBgImagePath": convert_string(excel_instance.ShiftMainBgImagePath(), password),
        "MinigameLobbyPrefabName": convert_string(excel_instance.MinigameLobbyPrefabName(), password),
        "MinigameVictoryPrefabName": convert_string(excel_instance.MinigameVictoryPrefabName(), password),
        "MinigameMissionBgPrefabName": convert_string(excel_instance.MinigameMissionBgPrefabName(), password),
        "MinigameMissionBgImagePath": convert_string(excel_instance.MinigameMissionBgImagePath(), password),
        "CardBgImagePath": convert_string(excel_instance.CardBgImagePath(), password),
        "EventAssist": bool(excel_instance.EventAssist()),
        "EventContentReleaseType": EventContentReleaseType(convert_int(excel_instance.EventContentReleaseType(), password)).name,
        "EventContentStageRewardIdPermanent": convert_int(excel_instance.EventContentStageRewardIdPermanent(), password),
        "RewardTagPermanent": convert_float(excel_instance.RewardTagPermanent(), password),
        "MiniEventShortCutScenarioModeId": convert_int(excel_instance.MiniEventShortCutScenarioModeId(), password),
        "ScenarioContentCollectionGroupId": convert_int(excel_instance.ScenarioContentCollectionGroupId(), password),
    }

def dump_EventContentShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsIdLength": convert_int(excel_instance.GoodsIdLength(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetType(), password)).name,
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "RestrictBuyWhenInventoryFull": bool(excel_instance.RestrictBuyWhenInventoryFull()),
    }

def dump_EventContentShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "LocalizeCode": convert_uint(excel_instance.LocalizeCode(), password),
        "CostParcelTypeLength": convert_int(excel_instance.CostParcelTypeLength(), password),
        "CostParcelIdLength": convert_int(excel_instance.CostParcelIdLength(), password),
        "IsRefresh": bool(excel_instance.IsRefresh()),
        "IsSoldOutDimmed": bool(excel_instance.IsSoldOutDimmed()),
        "AutoRefreshCoolTime": convert_int(excel_instance.AutoRefreshCoolTime(), password),
        "RefreshAbleCount": convert_int(excel_instance.RefreshAbleCount(), password),
        "GoodsIdLength": convert_int(excel_instance.GoodsIdLength(), password),
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFrom(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodTo(), password),
        "ShopProductUpdateDate": convert_string(excel_instance.ShopProductUpdateDate(), password),
    }

def dump_EventContentShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
    }

def dump_EventContentSpecialOperationsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "PointItemId": convert_int(excel_instance.PointItemId(), password),
    }

def dump_EventContentSpineDialogOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "SpineOffsetX": convert_float(excel_instance.SpineOffsetX(), password),
        "SpineOffsetY": convert_float(excel_instance.SpineOffsetY(), password),
        "DialogOffsetX": convert_float(excel_instance.DialogOffsetX(), password),
        "DialogOffsetY": convert_float(excel_instance.DialogOffsetY(), password),
    }

def dump_EventContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "OpenDate": convert_int(excel_instance.OpenDate(), password),
        "OpenEventPoint": convert_int(excel_instance.OpenEventPoint(), password),
        "OpenConditionScenarioPermanentSubEventId": convert_int(excel_instance.OpenConditionScenarioPermanentSubEventId(), password),
        "PrevStageSubEventId": convert_int(excel_instance.PrevStageSubEventId(), password),
        "OpenConditionScenarioId": convert_int(excel_instance.OpenConditionScenarioId(), password),
        "OpenConditionContentType": EventContentType(convert_int(excel_instance.OpenConditionContentType(), password)).name,
        "OpenConditionContentId": convert_int(excel_instance.OpenConditionContentId(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupIdLength": convert_int(excel_instance.EnterScenarioGroupIdLength(), password),
        "ClearScenarioGroupIdLength": convert_int(excel_instance.ClearScenarioGroupIdLength(), password),
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "InstantClear": bool(excel_instance.InstantClear()),
        "BuffContentId": convert_int(excel_instance.BuffContentId(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "ChallengeDisplay": bool(excel_instance.ChallengeDisplay()),
        "StarGoalLength": convert_int(excel_instance.StarGoalLength(), password),
        "StarGoalAmountLength": convert_int(excel_instance.StarGoalAmountLength(), password),
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattle()),
        "StageHint": convert_uint(excel_instance.StageHint(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_EventContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_EventContentStageTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "RequiredEventItemAmount": convert_int(excel_instance.RequiredEventItemAmount(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EventContentZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "OriginalZoneId": convert_int(excel_instance.OriginalZoneId(), password),
        "LocationId": convert_int(excel_instance.LocationId(), password),
        "LocationRank": convert_int(excel_instance.LocationRank(), password),
        "EventPointForLocationRank": convert_int(excel_instance.EventPointForLocationRank(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StudentVisitProbLength": convert_int(excel_instance.StudentVisitProbLength(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
        "WhiteListTagsLength": convert_int(excel_instance.WhiteListTagsLength(), password),
    }

def dump_EventContentZoneVisitRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentLocationId": convert_int(excel_instance.EventContentLocationId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "CharacterDevName": convert_string(excel_instance.CharacterDevName(), password),
        "VisitRewardParcelTypeLength": convert_int(excel_instance.VisitRewardParcelTypeLength(), password),
        "VisitRewardParcelIdLength": convert_int(excel_instance.VisitRewardParcelIdLength(), password),
        "VisitRewardAmountLength": convert_int(excel_instance.VisitRewardAmountLength(), password),
        "VisitRewardProbLength": convert_int(excel_instance.VisitRewardProbLength(), password),
    }

def dump_FieldContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "AreaId": convert_int(excel_instance.AreaId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "InstantClear": bool(excel_instance.InstantClear()),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "SkipFormationSettings": bool(excel_instance.SkipFormationSettings()),
        "DailyLastPlay": bool(excel_instance.DailyLastPlay()),
        "StarGoalLength": convert_int(excel_instance.StarGoalLength(), password),
        "StarGoalAmountLength": convert_int(excel_instance.StarGoalAmountLength(), password),
    }

def dump_FieldContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_FieldCurtainCallFreeModeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "OpenDate": convert_int(excel_instance.OpenDate(), password),
        "SetFieldDateID": convert_int(excel_instance.SetFieldDateID(), password),
        "SetFieldQuestOpenDate": convert_int(excel_instance.SetFieldQuestOpenDate(), password),
    }

def dump_FieldDateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "OpenDate": convert_int(excel_instance.OpenDate(), password),
        "DateLocalizeKey": convert_string(excel_instance.DateLocalizeKey(), password),
        "EntrySceneId": convert_int(excel_instance.EntrySceneId(), password),
        "StartConditionType": FieldConditionType(convert_int(excel_instance.StartConditionType(), password)).name,
        "StartConditionId": convert_int(excel_instance.StartConditionId(), password),
        "EndConditionType": FieldConditionType(convert_int(excel_instance.EndConditionType(), password)).name,
        "EndConditionId": convert_int(excel_instance.EndConditionId(), password),
        "EndReadyConditionType": FieldConditionType(convert_int(excel_instance.EndReadyConditionType(), password)).name,
        "EndReadyConditionId": convert_int(excel_instance.EndReadyConditionId(), password),
        "OpenConditionStage": convert_int(excel_instance.OpenConditionStage(), password),
        "CharacterIconPath": convert_string(excel_instance.CharacterIconPath(), password),
        "DateResultBGPath": convert_string(excel_instance.DateResultBGPath(), password),
        "DateResultSpinePath": convert_string(excel_instance.DateResultSpinePath(), password),
        "DateResultSpineOffsetX": convert_float(excel_instance.DateResultSpineOffsetX(), password),
    }

def dump_FieldEvidenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "NameLocalizeKey": convert_string(excel_instance.NameLocalizeKey(), password),
        "DescriptionLocalizeKey": convert_string(excel_instance.DescriptionLocalizeKey(), password),
        "DetailLocalizeKey": convert_string(excel_instance.DetailLocalizeKey(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_FieldInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeasonId": convert_long(excel_instance.FieldSeasonId(), password),
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "FieldDateId": convert_long(excel_instance.FieldDateId(), password),
        "ShowEmoji": bool(excel_instance.ShowEmoji()),
        "KeywordLocalize": convert_string(excel_instance.KeywordLocalize(), password),
        "InteractionTypeLength": convert_int(excel_instance.InteractionTypeLength(), password),
        "InteractionIdLength": convert_int(excel_instance.InteractionIdLength(), password),
        "ConditionClass": FieldConditionClass(convert_int(excel_instance.ConditionClass(), password)).name,
        "ConditionClassParametersLength": convert_int(excel_instance.ConditionClassParametersLength(), password),
        "OnceOnly": bool(excel_instance.OnceOnly()),
        "ConditionIndexLength": convert_int(excel_instance.ConditionIndexLength(), password),
        "ConditionTypeLength": convert_int(excel_instance.ConditionTypeLength(), password),
        "ConditionIdLength": convert_int(excel_instance.ConditionIdLength(), password),
        "NegateConditionLength": convert_int(excel_instance.NegateConditionLength(), password),
    }

def dump_FieldKeywordExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "NameLocalizeKey": convert_string(excel_instance.NameLocalizeKey(), password),
        "DescriptionLocalizeKey": convert_string(excel_instance.DescriptionLocalizeKey(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_FieldMasteryExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "ExpAmount": convert_int(excel_instance.ExpAmount(), password),
        "TokenType": ParcelType(convert_int(excel_instance.TokenType(), password)).name,
        "TokenId": convert_int(excel_instance.TokenId(), password),
        "TokenRequirement": convert_int(excel_instance.TokenRequirement(), password),
        "AccomplishmentConditionType": FieldConditionType(convert_int(excel_instance.AccomplishmentConditionType(), password)).name,
        "AccomplishmentConditionId": convert_int(excel_instance.AccomplishmentConditionId(), password),
    }

def dump_FieldMasteryLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "IdLength": convert_int(excel_instance.IdLength(), password),
        "ExpLength": convert_int(excel_instance.ExpLength(), password),
        "TotalExpLength": convert_int(excel_instance.TotalExpLength(), password),
        "RewardIdLength": convert_int(excel_instance.RewardIdLength(), password),
    }

def dump_FieldMasteryManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeason": convert_int(excel_instance.FieldSeason(), password),
        "LocalizeEtc": convert_uint(excel_instance.LocalizeEtc(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "LevelId": convert_int(excel_instance.LevelId(), password),
    }

def dump_FieldQuestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FieldSeasonId": convert_int(excel_instance.FieldSeasonId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "IsDaily": bool(excel_instance.IsDaily()),
        "FieldDateId": convert_int(excel_instance.FieldDateId(), password),
        "Opendate": convert_int(excel_instance.Opendate(), password),
        "AssetPath": convert_string(excel_instance.AssetPath(), password),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "QuestNamKey": convert_uint(excel_instance.QuestNamKey(), password),
        "QuestDescKey": convert_uint(excel_instance.QuestDescKey(), password),
    }

def dump_FieldRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_long(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
    }

def dump_FieldSceneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_long(excel_instance.UniqueId(), password),
        "DateId": convert_long(excel_instance.DateId(), password),
        "GroupId": convert_long(excel_instance.GroupId(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPath(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPath(), password),
        "BGMId": convert_long(excel_instance.BGMId(), password),
        "ConditionalBGMQuestIdLength": convert_int(excel_instance.ConditionalBGMQuestIdLength(), password),
        "BeginConditionalBGMScenarioGroupIdLength": convert_int(excel_instance.BeginConditionalBGMScenarioGroupIdLength(), password),
        "BeginConditionalBGMInteractionIdLength": convert_int(excel_instance.BeginConditionalBGMInteractionIdLength(), password),
        "EndConditionalBGMScenarioGroupIdLength": convert_int(excel_instance.EndConditionalBGMScenarioGroupIdLength(), password),
        "EndConditionalBGMInteractionIdLength": convert_int(excel_instance.EndConditionalBGMInteractionIdLength(), password),
        "ConditionalBGMIdLength": convert_int(excel_instance.ConditionalBGMIdLength(), password),
    }

def dump_FieldSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EntryDateId": convert_int(excel_instance.EntryDateId(), password),
        "InstantEntryDateId": convert_int(excel_instance.InstantEntryDateId(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "LobbyBGMChangeStageId": convert_int(excel_instance.LobbyBGMChangeStageId(), password),
        "FieldPrefabControlID": convert_int(excel_instance.FieldPrefabControlID(), password),
        "FieldGetKeywordCallDialogEnum": FieldDialogType(convert_int(excel_instance.FieldGetKeywordCallDialogEnum(), password)).name,
        "MasteryImagePath": convert_string(excel_instance.MasteryImagePath(), password),
        "FieldLobbyTitleImagePath": convert_string(excel_instance.FieldLobbyTitleImagePath(), password),
        "KeywordLogoImagePath": convert_string(excel_instance.KeywordLogoImagePath(), password),
    }

def dump_FieldStoryStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "SkipFormationSettings": bool(excel_instance.SkipFormationSettings()),
    }

def dump_FieldTutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "TutorialTypeLength": convert_int(excel_instance.TutorialTypeLength(), password),
        "ConditionTypeLength": convert_int(excel_instance.ConditionTypeLength(), password),
        "ConditionIdLength": convert_int(excel_instance.ConditionIdLength(), password),
    }

def dump_FieldWorldMapZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Date": convert_int(excel_instance.Date(), password),
        "OpenConditionType": FieldConditionType(convert_int(excel_instance.OpenConditionType(), password)).name,
        "OpenConditionId": convert_int(excel_instance.OpenConditionId(), password),
        "CloseConditionType": FieldConditionType(convert_int(excel_instance.CloseConditionType(), password)).name,
        "CloseConditionId": convert_int(excel_instance.CloseConditionId(), password),
        "ResultFieldScene": convert_int(excel_instance.ResultFieldScene(), password),
        "FieldStageInteractionId": convert_int(excel_instance.FieldStageInteractionId(), password),
        "WorldMapButtonType": FieldWorldMapButtonType(convert_int(excel_instance.WorldMapButtonType(), password)).name,
        "LocalizeCode": convert_uint(excel_instance.LocalizeCode(), password),
        "NewTagDisplay": bool(excel_instance.NewTagDisplay()),
    }

def dump_FixedStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StageEnterEchelon01FixedEchelonId": convert_int(excel_instance.StageEnterEchelon01FixedEchelonId(), password),
        "StageEnterEchelon01Starttile": convert_int(excel_instance.StageEnterEchelon01Starttile(), password),
        "StageEnterEchelon02FixedEchelonId": convert_int(excel_instance.StageEnterEchelon02FixedEchelonId(), password),
        "StageEnterEchelon02Starttile": convert_int(excel_instance.StageEnterEchelon02Starttile(), password),
        "StageEnterEchelon03FixedEchelonId": convert_int(excel_instance.StageEnterEchelon03FixedEchelonId(), password),
        "StageEnterEchelon03Starttile": convert_int(excel_instance.StageEnterEchelon03Starttile(), password),
        "StageEnterEchelon04FixedEchelonId": convert_int(excel_instance.StageEnterEchelon04FixedEchelonId(), password),
        "StageEnterEchelon04Starttile": convert_int(excel_instance.StageEnterEchelon04Starttile(), password),
    }

def dump_FloaterCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TacticEntityType": TacticEntityType(convert_int(excel_instance.TacticEntityType(), password)).name,
        "FloaterOffsetPosX": convert_int(excel_instance.FloaterOffsetPosX(), password),
        "FloaterOffsetPosY": convert_int(excel_instance.FloaterOffsetPosY(), password),
        "FloaterRandomPosRangeX": convert_int(excel_instance.FloaterRandomPosRangeX(), password),
        "FloaterRandomPosRangeY": convert_int(excel_instance.FloaterRandomPosRangeY(), password),
    }

def dump_FurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "Category": FurnitureCategory(convert_int(excel_instance.Category(), password)).name,
        "SubCategory": FurnitureSubCategory(convert_int(excel_instance.SubCategory(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StarGradeInit": convert_int(excel_instance.StarGradeInit(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "SizeWidth": convert_int(excel_instance.SizeWidth(), password),
        "SizeHeight": convert_int(excel_instance.SizeHeight(), password),
        "OtherSize": convert_int(excel_instance.OtherSize(), password),
        "ExpandWidth": convert_int(excel_instance.ExpandWidth(), password),
        "Enable": bool(excel_instance.Enable()),
        "ReverseRotation": bool(excel_instance.ReverseRotation()),
        "Prefab": convert_string(excel_instance.Prefab(), password),
        "PrefabExpand": convert_string(excel_instance.PrefabExpand(), password),
        "SubPrefab": convert_string(excel_instance.SubPrefab(), password),
        "SubExpandPrefab": convert_string(excel_instance.SubExpandPrefab(), password),
        "CornerPrefab": convert_string(excel_instance.CornerPrefab(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "RecipeCraftId": convert_int(excel_instance.RecipeCraftId(), password),
        "SetGroudpId": convert_int(excel_instance.SetGroudpId(), password),
        "ComfortBonus": convert_int(excel_instance.ComfortBonus(), password),
        "VisitOperationType": convert_int(excel_instance.VisitOperationType(), password),
        "VisitBonusOperationType": convert_int(excel_instance.VisitBonusOperationType(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQuality(), password),
        "FurnitureFunctionType": FurnitureFunctionType(convert_int(excel_instance.FurnitureFunctionType(), password)).name,
        "FurnitureFunctionParameterLength": convert_int(excel_instance.FurnitureFunctionParameterLength(), password),
        "VideoId": convert_int(excel_instance.VideoId(), password),
        "EventCollectionId": convert_int(excel_instance.EventCollectionId(), password),
        "FurnitureBubbleOffsetX": convert_int(excel_instance.FurnitureBubbleOffsetX(), password),
        "FurnitureBubbleOffsetY": convert_int(excel_instance.FurnitureBubbleOffsetY(), password),
        "CafeCharacterStateReqLength": convert_int(excel_instance.CafeCharacterStateReqLength(), password),
        "CafeCharacterStateAddLength": convert_int(excel_instance.CafeCharacterStateAddLength(), password),
        "CafeCharacterStateMakeLength": convert_int(excel_instance.CafeCharacterStateMakeLength(), password),
        "CafeCharacterStateOnlyLength": convert_int(excel_instance.CafeCharacterStateOnlyLength(), password),
    }

def dump_FurnitureGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupNameLocalize": convert_uint(excel_instance.GroupNameLocalize(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "RequiredFurnitureCountLength": convert_int(excel_instance.RequiredFurnitureCountLength(), password),
        "ComfortBonusLength": convert_int(excel_instance.ComfortBonusLength(), password),
    }

def dump_FurnitureTemplateElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_int(excel_instance.FurnitureTemplateId(), password),
        "FurnitureId": convert_int(excel_instance.FurnitureId(), password),
        "Location": FurnitureLocation(convert_int(excel_instance.Location(), password)).name,
        "PositionX": convert_float(excel_instance.PositionX(), password),
        "PositionY": convert_float(excel_instance.PositionY(), password),
        "Rotation": convert_float(excel_instance.Rotation(), password),
        "Order": convert_int(excel_instance.Order(), password),
    }

def dump_FurnitureTemplateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_int(excel_instance.FurnitureTemplateId(), password),
        "FunitureTemplateTitle": convert_uint(excel_instance.FunitureTemplateTitle(), password),
        "ThumbnailImagePath": convert_string(excel_instance.ThumbnailImagePath(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_GachaCraftNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "QuickCraftNodeDisplayOrder": convert_int(excel_instance.QuickCraftNodeDisplayOrder(), password),
        "NodeQuality": convert_int(excel_instance.NodeQuality(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "LocalizeKey": convert_uint(excel_instance.LocalizeKey(), password),
        "Property": convert_int(excel_instance.Property(), password),
    }

def dump_GachaCraftNodeGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NodeId": convert_int(excel_instance.NodeId(), password),
        "GachaGroupId": convert_int(excel_instance.GachaGroupId(), password),
        "ProbWeight": convert_int(excel_instance.ProbWeight(), password),
    }

def dump_GachaCraftOpenTagExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NodeTier": convert_int(excel_instance.NodeTier(), password),
        "TagLength": convert_int(excel_instance.TagLength(), password),
    }

def dump_GachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupID(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelID": convert_int(excel_instance.ParcelID(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMin(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMax(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "State": convert_int(excel_instance.State(), password),
    }

def dump_GachaElementRecursiveExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupID(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelID": convert_int(excel_instance.ParcelID(), password),
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMin(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMax(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "State": convert_int(excel_instance.State(), password),
    }

def dump_GachaGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "IsRecursive": bool(excel_instance.IsRecursive()),
        "GroupType": GachaGroupType(convert_int(excel_instance.GroupType(), password)).name,
    }

def dump_GoodsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Type": convert_int(excel_instance.Type(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "ConsumeParcelTypeLength": convert_int(excel_instance.ConsumeParcelTypeLength(), password),
        "ConsumeParcelIdLength": convert_int(excel_instance.ConsumeParcelIdLength(), password),
        "ConsumeParcelAmountLength": convert_int(excel_instance.ConsumeParcelAmountLength(), password),
        "ConsumeConditionLength": convert_int(excel_instance.ConsumeConditionLength(), password),
        "ConsumeGachaTicketType": GachaTicketType(convert_int(excel_instance.ConsumeGachaTicketType(), password)).name,
        "ConsumeGachaTicketTypeAmount": convert_int(excel_instance.ConsumeGachaTicketTypeAmount(), password),
        "ProductIdAOS": convert_int(excel_instance.ProductIdAOS(), password),
        "ProductIdiOS": convert_int(excel_instance.ProductIdiOS(), password),
        "ProductIdHarmony": convert_int(excel_instance.ProductIdHarmony(), password),
        "ConsumeExtraStepLength": convert_int(excel_instance.ConsumeExtraStepLength(), password),
        "ConsumeExtraAmountLength": convert_int(excel_instance.ConsumeExtraAmountLength(), password),
        "State": convert_int(excel_instance.State(), password),
        "ParcelTypeLength": convert_int(excel_instance.ParcelTypeLength(), password),
        "ParcelIdLength": convert_int(excel_instance.ParcelIdLength(), password),
        "ParcelAmountLength": convert_int(excel_instance.ParcelAmountLength(), password),
    }

def dump_GroundGridFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "StartX": convert_float(excel_instance.StartX(), password),
        "StartY": convert_float(excel_instance.StartY(), password),
        "Gap": convert_float(excel_instance.Gap(), password),
        "NodesLength": convert_int(excel_instance.NodesLength(), password),
        "Version": convert_string(excel_instance.Version(), password),
    }

def dump_GroundNodeFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "IsCanNotUseSkill": bool(excel_instance.IsCanNotUseSkill()),
                "NodeType": GroundNodeType(convert_int(excel_instance.NodeType(), password)).name,
        "OriginalNodeType": GroundNodeType(convert_int(excel_instance.OriginalNodeType(), password)).name,
    }

def dump_GroundNodeLayerFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "LayersLength": convert_int(excel_instance.LayersLength(), password),
    }

def dump_GuideMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "TabNumber": convert_int(excel_instance.TabNumber(), password),
        "PreMissionIdLength": convert_int(excel_instance.PreMissionIdLength(), password),
        "Description": convert_uint(excel_instance.Description(), password),
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ShortcutUILength": convert_int(excel_instance.ShortcutUILength(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameterLength": convert_int(excel_instance.CompleteConditionParameterLength(), password),
        "CompleteConditionParameterTagLength": convert_int(excel_instance.CompleteConditionParameterTagLength(), password),
        "IsAutoClearForScenario": bool(excel_instance.IsAutoClearForScenario()),
        "MissionRewardParcelTypeLength": convert_int(excel_instance.MissionRewardParcelTypeLength(), password),
        "MissionRewardParcelIdLength": convert_int(excel_instance.MissionRewardParcelIdLength(), password),
        "MissionRewardAmountLength": convert_int(excel_instance.MissionRewardAmountLength(), password),
    }

def dump_GuideMissionOpenStageConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "OrderNumber": convert_int(excel_instance.OrderNumber(), password),
        "TabLocalizeCode": convert_string(excel_instance.TabLocalizeCode(), password),
        "ClearScenarioModeId": convert_int(excel_instance.ClearScenarioModeId(), password),
        "LockScenarioTextLocailzeCode": convert_string(excel_instance.LockScenarioTextLocailzeCode(), password),
        "ShortcutScenarioUI": convert_string(excel_instance.ShortcutScenarioUI(), password),
        "ClearStageId": convert_int(excel_instance.ClearStageId(), password),
        "LockStageTextLocailzeCode": convert_string(excel_instance.LockStageTextLocailzeCode(), password),
        "ShortcutStageUI": convert_string(excel_instance.ShortcutStageUI(), password),
    }

def dump_GuideMissionSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TitleLocalizeCode": convert_string(excel_instance.TitleLocalizeCode(), password),
        "PermanentInfomationLocalizeCode": convert_string(excel_instance.PermanentInfomationLocalizeCode(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCode(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "Enabled": bool(excel_instance.Enabled()),
        "BannerOpenDate": convert_string(excel_instance.BannerOpenDate(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "CloseBannerAfterCompletion": bool(excel_instance.CloseBannerAfterCompletion()),
        "MaximumLoginCount": convert_int(excel_instance.MaximumLoginCount(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDate(), password),
        "SpineCharacterId": convert_int(excel_instance.SpineCharacterId(), password),
        "RequirementParcelImage": convert_string(excel_instance.RequirementParcelImage(), password),
        "RewardImage": convert_string(excel_instance.RewardImage(), password),
        "LobbyBannerImage": convert_string(excel_instance.LobbyBannerImage(), password),
        "BackgroundImage": convert_string(excel_instance.BackgroundImage(), password),
        "TitleImage": convert_string(excel_instance.TitleImage(), password),
        "RequirementParcelType": ParcelType(convert_int(excel_instance.RequirementParcelType(), password)).name,
        "RequirementParcelId": convert_int(excel_instance.RequirementParcelId(), password),
        "RequirementParcelAmount": convert_int(excel_instance.RequirementParcelAmount(), password),
        "TabType": GuideMissionTabType(convert_int(excel_instance.TabType(), password)).name,
        "IsPermanent": bool(excel_instance.IsPermanent()),
        "PreSeasonId": convert_int(excel_instance.PreSeasonId(), password),
    }

def dump_HpBarAbbreviationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MonsterLv": convert_int(excel_instance.MonsterLv(), password),
        "StandardHpBar": convert_int(excel_instance.StandardHpBar(), password),
        "RaidBossHpBar": convert_int(excel_instance.RaidBossHpBar(), password),
    }

def dump_InformationStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StageId": convert_int(excel_instance.StageId(), password),
        "PageName": convert_string(excel_instance.PageName(), password),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeId(), password),
    }

def dump_ItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "ItemCategory": ItemCategory(convert_int(excel_instance.ItemCategory(), password)).name,
        "Quality": convert_int(excel_instance.Quality(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "StackableFunction": convert_int(excel_instance.StackableFunction(), password),
        "ImmediateUse": bool(excel_instance.ImmediateUse()),
        "UsingResultParcelType": ParcelType(convert_int(excel_instance.UsingResultParcelType(), password)).name,
        "UsingResultId": convert_int(excel_instance.UsingResultId(), password),
        "UsingResultAmount": convert_int(excel_instance.UsingResultAmount(), password),
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "ExpiryChangeParcelType": ParcelType(convert_int(excel_instance.ExpiryChangeParcelType(), password)).name,
        "ExpiryChangeId": convert_int(excel_instance.ExpiryChangeId(), password),
        "ExpiryChangeAmount": convert_int(excel_instance.ExpiryChangeAmount(), password),
        "CanTierUpgrade": bool(excel_instance.CanTierUpgrade()),
        "TierUpgradeRecipeCraftId": convert_int(excel_instance.TierUpgradeRecipeCraftId(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQuality(), password),
        "MaxGiftTags": convert_int(excel_instance.MaxGiftTags(), password),
        "ShopCategoryLength": convert_int(excel_instance.ShopCategoryLength(), password),
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTime(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateIn(), password),
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeId(), password),
        "GachaTicket": GachaTicketType(convert_int(excel_instance.GachaTicket(), password)).name,
    }

def dump_KnockBackExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_int(excel_instance.Index(), password),
        "Dist": convert_float(excel_instance.Dist(), password),
        "Speed": convert_float(excel_instance.Speed(), password),
    }

def dump_LimitedStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "OpenDate": convert_int(excel_instance.OpenDate(), password),
        "OpenEventPoint": convert_int(excel_instance.OpenEventPoint(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupIdLength": convert_int(excel_instance.EnterScenarioGroupIdLength(), password),
        "ClearScenarioGroupIdLength": convert_int(excel_instance.ClearScenarioGroupIdLength(), password),
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "InstantClear": bool(excel_instance.InstantClear()),
        "BuffContentId": convert_int(excel_instance.BuffContentId(), password),
        "ChallengeDisplay": bool(excel_instance.ChallengeDisplay()),
    }

def dump_LimitedStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_LimitedStageSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "TypeACount": convert_int(excel_instance.TypeACount(), password),
        "TypeBCount": convert_int(excel_instance.TypeBCount(), password),
        "TypeCCount": convert_int(excel_instance.TypeCCount(), password),
    }

def dump_LocalizeCharProfileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "StatusMessageKr": convert_string(excel_instance.StatusMessageKr(), password),
        "StatusMessageJp": convert_string(excel_instance.StatusMessageJp(), password),
        "FullNameKr": convert_string(excel_instance.FullNameKr(), password),
        "FullNameJp": convert_string(excel_instance.FullNameJp(), password),
        "FamilyNameKr": convert_string(excel_instance.FamilyNameKr(), password),
        "FamilyNameRubyKr": convert_string(excel_instance.FamilyNameRubyKr(), password),
        "PersonalNameKr": convert_string(excel_instance.PersonalNameKr(), password),
        "PersonalNameRubyKr": convert_string(excel_instance.PersonalNameRubyKr(), password),
        "FamilyNameJp": convert_string(excel_instance.FamilyNameJp(), password),
        "FamilyNameRubyJp": convert_string(excel_instance.FamilyNameRubyJp(), password),
        "PersonalNameJp": convert_string(excel_instance.PersonalNameJp(), password),
        "PersonalNameRubyJp": convert_string(excel_instance.PersonalNameRubyJp(), password),
        "SchoolYearKr": convert_string(excel_instance.SchoolYearKr(), password),
        "SchoolYearJp": convert_string(excel_instance.SchoolYearJp(), password),
        "CharacterAgeKr": convert_string(excel_instance.CharacterAgeKr(), password),
        "CharacterAgeJp": convert_string(excel_instance.CharacterAgeJp(), password),
        "BirthDay": convert_string(excel_instance.BirthDay(), password),
        "BirthdayKr": convert_string(excel_instance.BirthdayKr(), password),
        "BirthdayJp": convert_string(excel_instance.BirthdayJp(), password),
        "CharHeightKr": convert_string(excel_instance.CharHeightKr(), password),
        "CharHeightJp": convert_string(excel_instance.CharHeightJp(), password),
        "DesignerNameKr": convert_string(excel_instance.DesignerNameKr(), password),
        "DesignerNameJp": convert_string(excel_instance.DesignerNameJp(), password),
        "IllustratorNameKr": convert_string(excel_instance.IllustratorNameKr(), password),
        "IllustratorNameJp": convert_string(excel_instance.IllustratorNameJp(), password),
        "CharacterVoiceKr": convert_string(excel_instance.CharacterVoiceKr(), password),
        "CharacterVoiceJp": convert_string(excel_instance.CharacterVoiceJp(), password),
        "HobbyKr": convert_string(excel_instance.HobbyKr(), password),
        "HobbyJp": convert_string(excel_instance.HobbyJp(), password),
        "WeaponNameKr": convert_string(excel_instance.WeaponNameKr(), password),
        "WeaponDescKr": convert_string(excel_instance.WeaponDescKr(), password),
        "WeaponNameJp": convert_string(excel_instance.WeaponNameJp(), password),
        "WeaponDescJp": convert_string(excel_instance.WeaponDescJp(), password),
        "ProfileIntroductionKr": convert_string(excel_instance.ProfileIntroductionKr(), password),
        "ProfileIntroductionJp": convert_string(excel_instance.ProfileIntroductionJp(), password),
        "CharacterSSRNewKr": convert_string(excel_instance.CharacterSSRNewKr(), password),
        "CharacterSSRNewJp": convert_string(excel_instance.CharacterSSRNewJp(), password),
    }

def dump_LocalizeFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GachaShopId": convert_int(excel_instance.GachaShopId(), password),
        "TabNameKr": convert_string(excel_instance.TabNameKr(), password),
        "TabNameJp": convert_string(excel_instance.TabNameJp(), password),
        "TitleNameKr": convert_string(excel_instance.TitleNameKr(), password),
        "TitleNameJp": convert_string(excel_instance.TitleNameJp(), password),
        "SubTitleKr": convert_string(excel_instance.SubTitleKr(), password),
        "SubTitleJp": convert_string(excel_instance.SubTitleJp(), password),
        "GachaDescriptionKr": convert_string(excel_instance.GachaDescriptionKr(), password),
        "GachaDescriptionJp": convert_string(excel_instance.GachaDescriptionJp(), password),
        "GachaPeriodCN": convert_string(excel_instance.GachaPeriodCN(), password),
    }

def dump_LogicEffectCommonVisualExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringID(), password),
        "IconSpriteName": convert_string(excel_instance.IconSpriteName(), password),
        "IconDispelColorLength": convert_int(excel_instance.IconDispelColorLength(), password),
        "ParticleEnterPath": convert_string(excel_instance.ParticleEnterPath(), password),
        "ParticleEnterSocket": EffectBone(convert_int(excel_instance.ParticleEnterSocket(), password)).name,
        "ParticleLoopPath": convert_string(excel_instance.ParticleLoopPath(), password),
        "ParticleLoopSocket": EffectBone(convert_int(excel_instance.ParticleLoopSocket(), password)).name,
        "ParticleEndPath": convert_string(excel_instance.ParticleEndPath(), password),
        "ParticleEndSocket": EffectBone(convert_int(excel_instance.ParticleEndSocket(), password)).name,
        "ParticleApplyPath": convert_string(excel_instance.ParticleApplyPath(), password),
        "ParticleApplySocket": EffectBone(convert_int(excel_instance.ParticleApplySocket(), password)).name,
        "ParticleRemovedPath": convert_string(excel_instance.ParticleRemovedPath(), password),
        "ParticleRemovedSocket": EffectBone(convert_int(excel_instance.ParticleRemovedSocket(), password)).name,
    }

def dump_MiniGameAudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHash(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefix(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHash(), password),
        "StateName": convert_string(excel_instance.StateName(), password),
        "IgnoreInterruptDelay": bool(excel_instance.IgnoreInterruptDelay()),
        "IgnoreInterruptPlay": bool(excel_instance.IgnoreInterruptPlay()),
        "Volume": convert_float(excel_instance.Volume(), password),
        "Delay": convert_float(excel_instance.Delay(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriority(), password),
        "AudioClipPathLength": convert_int(excel_instance.AudioClipPathLength(), password),
        "VoiceHashLength": convert_int(excel_instance.VoiceHashLength(), password),
    }

def dump_MiniGameMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "GroupName": convert_string(excel_instance.GroupName(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetType(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "PreMissionIdLength": convert_int(excel_instance.PreMissionIdLength(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ShortcutUILength": convert_int(excel_instance.ShortcutUILength(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "IsCompleteExtensionTime": bool(excel_instance.IsCompleteExtensionTime()),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameterLength": convert_int(excel_instance.CompleteConditionParameterLength(), password),
        "CompleteConditionParameterTagLength": convert_int(excel_instance.CompleteConditionParameterTagLength(), password),
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "MissionRewardParcelTypeLength": convert_int(excel_instance.MissionRewardParcelTypeLength(), password),
        "MissionRewardParcelIdLength": convert_int(excel_instance.MissionRewardParcelIdLength(), password),
        "MissionRewardAmountLength": convert_int(excel_instance.MissionRewardAmountLength(), password),
    }

def dump_MiniGamePlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_MiniGameRhythmBgmExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RhythmBgmId": convert_int(excel_instance.RhythmBgmId(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "StageSelectImagePath": convert_string(excel_instance.StageSelectImagePath(), password),
        "Bpm": convert_int(excel_instance.Bpm(), password),
        "Bgm": convert_int(excel_instance.Bgm(), password),
        "BgmNameText": convert_string(excel_instance.BgmNameText(), password),
        "BgmArtistText": convert_string(excel_instance.BgmArtistText(), password),
        "HasLyricist": bool(excel_instance.HasLyricist()),
        "BgmComposerText": convert_string(excel_instance.BgmComposerText(), password),
        "BgmLength": convert_int(excel_instance.BgmLength(), password),
    }

def dump_MiniGameRhythmExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "RhythmBgmId": convert_int(excel_instance.RhythmBgmId(), password),
        "PresetName": convert_string(excel_instance.PresetName(), password),
        "StageDifficulty": Difficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "IsSpecial": bool(excel_instance.IsSpecial()),
        "OpenStageScoreAmount": convert_int(excel_instance.OpenStageScoreAmount(), password),
        "MaxHp": convert_int(excel_instance.MaxHp(), password),
        "MissDamage": convert_int(excel_instance.MissDamage(), password),
        "CriticalHPRestoreValue": convert_int(excel_instance.CriticalHPRestoreValue(), password),
        "MaxScore": convert_int(excel_instance.MaxScore(), password),
        "FeverScoreRate": convert_int(excel_instance.FeverScoreRate(), password),
        "NoteScoreRate": convert_int(excel_instance.NoteScoreRate(), password),
        "ComboScoreRate": convert_int(excel_instance.ComboScoreRate(), password),
        "AttackScoreRate": convert_int(excel_instance.AttackScoreRate(), password),
        "FeverCriticalRate": convert_float(excel_instance.FeverCriticalRate(), password),
        "FeverAttackRate": convert_float(excel_instance.FeverAttackRate(), password),
        "MaxHpScore": convert_int(excel_instance.MaxHpScore(), password),
        "RhythmFileName": convert_string(excel_instance.RhythmFileName(), password),
        "ArtLevelSceneName": convert_string(excel_instance.ArtLevelSceneName(), password),
        "ComboImagePath": convert_string(excel_instance.ComboImagePath(), password),
    }

def dump_MiniGameShootingCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceName(), password),
        "BodyRadius": convert_float(excel_instance.BodyRadius(), password),
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabName(), password),
        "NormalAttackSkillData": convert_string(excel_instance.NormalAttackSkillData(), password),
        "PublicSkillDataLength": convert_int(excel_instance.PublicSkillDataLength(), password),
        "DeathSkillData": convert_string(excel_instance.DeathSkillData(), password),
        "MaxHP": convert_int(excel_instance.MaxHP(), password),
        "AttackPower": convert_int(excel_instance.AttackPower(), password),
        "DefensePower": convert_int(excel_instance.DefensePower(), password),
        "CriticalRate": convert_int(excel_instance.CriticalRate(), password),
        "CriticalDamageRate": convert_int(excel_instance.CriticalDamageRate(), password),
        "AttackRange": convert_int(excel_instance.AttackRange(), password),
        "MoveSpeed": convert_int(excel_instance.MoveSpeed(), password),
        "ShotTime": convert_int(excel_instance.ShotTime(), password),
        "IsBoss": bool(excel_instance.IsBoss()),
        "Scale": convert_float(excel_instance.Scale(), password),
        "IgnoreObstacleCheck": bool(excel_instance.IgnoreObstacleCheck()),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupId(), password),
    }

def dump_MiniGameShootingGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "GeasType": Geas(convert_int(excel_instance.GeasType(), password)).name,
        "Icon": convert_string(excel_instance.Icon(), password),
        "Probability": convert_int(excel_instance.Probability(), password),
        "MaxOverlapCount": convert_int(excel_instance.MaxOverlapCount(), password),
        "GeasData": convert_string(excel_instance.GeasData(), password),
        "NeedGeasId": convert_int(excel_instance.NeedGeasId(), password),
        "HideInPausePopup": bool(excel_instance.HideInPausePopup()),
    }

def dump_MiniGameShootingStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "BgmIdLength": convert_int(excel_instance.BgmIdLength(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "Difficulty": Difficulty(convert_int(excel_instance.Difficulty(), password)).name,
        "DesignLevel": convert_string(excel_instance.DesignLevel(), password),
        "ArtLevel": convert_string(excel_instance.ArtLevel(), password),
        "StartBattleDuration": convert_int(excel_instance.StartBattleDuration(), password),
        "DefaultBattleDuration": convert_int(excel_instance.DefaultBattleDuration(), password),
        "DefaultLogicEffect": convert_string(excel_instance.DefaultLogicEffect(), password),
        "CameraSizeRate": convert_float(excel_instance.CameraSizeRate(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardId(), password),
    }

def dump_MiniGameShootingStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "ClearSection": convert_int(excel_instance.ClearSection(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_MinigameTBGDiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "DiceGroup": convert_int(excel_instance.DiceGroup(), password),
        "DiceResult": convert_int(excel_instance.DiceResult(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbModifyConditionLength": convert_int(excel_instance.ProbModifyConditionLength(), password),
        "ProbModifyValueLength": convert_int(excel_instance.ProbModifyValueLength(), password),
        "ProbModifyLimitLength": convert_int(excel_instance.ProbModifyLimitLength(), password),
    }

def dump_MinigameTBGEncounterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "AllThema": bool(excel_instance.AllThema()),
        "ThemaIndex": convert_int(excel_instance.ThemaIndex(), password),
        "ThemaType": TBGThemaType(convert_int(excel_instance.ThemaType(), password)).name,
        "ObjectType": TBGObjectType(convert_int(excel_instance.ObjectType(), password)).name,
        "EnemyImagePath": convert_string(excel_instance.EnemyImagePath(), password),
        "EnemyPrefabName": convert_string(excel_instance.EnemyPrefabName(), password),
        "EnemyNameLocalize": convert_string(excel_instance.EnemyNameLocalize(), password),
        "OptionGroupId": convert_int(excel_instance.OptionGroupId(), password),
        "RewardHide": bool(excel_instance.RewardHide()),
        "EncounterTitleLocalize": convert_string(excel_instance.EncounterTitleLocalize(), password),
        "StoryImagePath": convert_string(excel_instance.StoryImagePath(), password),
        "BeforeStoryLocalize": convert_string(excel_instance.BeforeStoryLocalize(), password),
        "BeforeStoryOption1Localize": convert_string(excel_instance.BeforeStoryOption1Localize(), password),
        "BeforeStoryOption2Localize": convert_string(excel_instance.BeforeStoryOption2Localize(), password),
        "BeforeStoryOption3Localize": convert_string(excel_instance.BeforeStoryOption3Localize(), password),
        "AllyAttackLocalize": convert_string(excel_instance.AllyAttackLocalize(), password),
        "EnemyAttackLocalize": convert_string(excel_instance.EnemyAttackLocalize(), password),
        "AttackDefenceLocalize": convert_string(excel_instance.AttackDefenceLocalize(), password),
        "ClearStoryLocalize": convert_string(excel_instance.ClearStoryLocalize(), password),
        "DefeatStoryLocalize": convert_string(excel_instance.DefeatStoryLocalize(), password),
        "RunawayStoryLocalize": convert_string(excel_instance.RunawayStoryLocalize(), password),
    }

def dump_MinigameTBGEncounterOptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OptionGroupId": convert_int(excel_instance.OptionGroupId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SlotIndex": convert_int(excel_instance.SlotIndex(), password),
        "OptionTitleLocalize": convert_string(excel_instance.OptionTitleLocalize(), password),
        "OptionSuccessLocalize": convert_string(excel_instance.OptionSuccessLocalize(), password),
        "OptionSuccessRewardGroupId": convert_int(excel_instance.OptionSuccessRewardGroupId(), password),
        "OptionSuccessOrHigherDiceCount": convert_int(excel_instance.OptionSuccessOrHigherDiceCount(), password),
        "OptionGreatSuccessOrHigherDiceCount": convert_int(excel_instance.OptionGreatSuccessOrHigherDiceCount(), password),
        "OptionFailLocalize": convert_string(excel_instance.OptionFailLocalize(), password),
        "OptionFailLessDiceCount": convert_int(excel_instance.OptionFailLessDiceCount(), password),
        "RunawayOrHigherDiceCount": convert_int(excel_instance.RunawayOrHigherDiceCount(), password),
        "RewardHide": bool(excel_instance.RewardHide()),
    }

def dump_MinigameTBGEncounterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "TBGOptionSuccessType": TBGOptionSuccessType(convert_int(excel_instance.TBGOptionSuccessType(), password)).name,
        "Paremeter": convert_int(excel_instance.Paremeter(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "Amount": convert_int(excel_instance.Amount(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
    }

def dump_MinigameTBGItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ItemType": TBGItemType(convert_int(excel_instance.ItemType(), password)).name,
        "TBGItemEffectType": TBGItemEffectType(convert_int(excel_instance.TBGItemEffectType(), password)).name,
        "ItemParameter": convert_int(excel_instance.ItemParameter(), password),
        "LocalizeETCId": convert_string(excel_instance.LocalizeETCId(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "BuffIcon": convert_string(excel_instance.BuffIcon(), password),
        "EncounterCount": convert_int(excel_instance.EncounterCount(), password),
        "DiceEffectAniClip": convert_string(excel_instance.DiceEffectAniClip(), password),
        "BuffIconHUDVisible": bool(excel_instance.BuffIconHUDVisible()),
    }

def dump_MinigameTBGObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Key": convert_string(excel_instance.Key(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ObjectType": TBGObjectType(convert_int(excel_instance.ObjectType(), password)).name,
        "ObjectCostType": ParcelType(convert_int(excel_instance.ObjectCostType(), password)).name,
        "ObjectCostId": convert_int(excel_instance.ObjectCostId(), password),
        "ObjectCostAmount": convert_int(excel_instance.ObjectCostAmount(), password),
        "Disposable": bool(excel_instance.Disposable()),
        "ReEncounterCost": bool(excel_instance.ReEncounterCost()),
    }

def dump_MinigameTBGSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ItemSlot": convert_int(excel_instance.ItemSlot(), password),
        "DefaultEchelonHp": convert_int(excel_instance.DefaultEchelonHp(), password),
        "DefaultItemDiceId": convert_int(excel_instance.DefaultItemDiceId(), password),
        "EchelonSlot1CharacterId": convert_int(excel_instance.EchelonSlot1CharacterId(), password),
        "EchelonSlot2CharacterId": convert_int(excel_instance.EchelonSlot2CharacterId(), password),
        "EchelonSlot3CharacterId": convert_int(excel_instance.EchelonSlot3CharacterId(), password),
        "EchelonSlot4CharacterId": convert_int(excel_instance.EchelonSlot4CharacterId(), password),
        "EchelonSlot1Portrait": convert_string(excel_instance.EchelonSlot1Portrait(), password),
        "EchelonSlot2Portrait": convert_string(excel_instance.EchelonSlot2Portrait(), password),
        "EchelonSlot3Portrait": convert_string(excel_instance.EchelonSlot3Portrait(), password),
        "EchelonSlot4Portrait": convert_string(excel_instance.EchelonSlot4Portrait(), password),
        "EventUseCostType": ParcelType(convert_int(excel_instance.EventUseCostType(), password)).name,
        "EventUseCostId": convert_int(excel_instance.EventUseCostId(), password),
        "EchelonRevivalCostType": ParcelType(convert_int(excel_instance.EchelonRevivalCostType(), password)).name,
        "EchelonRevivalCostId": convert_int(excel_instance.EchelonRevivalCostId(), password),
        "EchelonRevivalCostAmount": convert_int(excel_instance.EchelonRevivalCostAmount(), password),
        "EnemyBossHP": convert_int(excel_instance.EnemyBossHP(), password),
        "EnemyMinionHP": convert_int(excel_instance.EnemyMinionHP(), password),
        "AttackDamage": convert_int(excel_instance.AttackDamage(), password),
        "CriticalAttackDamage": convert_int(excel_instance.CriticalAttackDamage(), password),
        "RoundItemSelectLimit": convert_int(excel_instance.RoundItemSelectLimit(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRound(), password),
        "MaxHp": convert_int(excel_instance.MaxHp(), password),
        "MapImagePath": convert_string(excel_instance.MapImagePath(), password),
        "MapNameLocalize": convert_string(excel_instance.MapNameLocalize(), password),
        "StartThemaIndex": convert_int(excel_instance.StartThemaIndex(), password),
        "LoopThemaIndex": convert_int(excel_instance.LoopThemaIndex(), password),
        "MaxDicePlus": convert_int(excel_instance.MaxDicePlus(), password),
    }

def dump_MinigameTBGThemaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ThemaIndex": convert_int(excel_instance.ThemaIndex(), password),
        "ThemaType": TBGThemaType(convert_int(excel_instance.ThemaType(), password)).name,
        "ThemaMap": convert_string(excel_instance.ThemaMap(), password),
        "ThemaMapBG": convert_string(excel_instance.ThemaMapBG(), password),
        "PortalConditionLength": convert_int(excel_instance.PortalConditionLength(), password),
        "PortalConditionParameterLength": convert_int(excel_instance.PortalConditionParameterLength(), password),
        "ThemaNameLocalize": convert_string(excel_instance.ThemaNameLocalize(), password),
        "ThemaLoadingImage": convert_string(excel_instance.ThemaLoadingImage(), password),
        "ThemaPlayerPrefab": convert_string(excel_instance.ThemaPlayerPrefab(), password),
        "ThemaLeaderId": convert_int(excel_instance.ThemaLeaderId(), password),
        "ThemaGoalLocalize": convert_string(excel_instance.ThemaGoalLocalize(), password),
        "InstantClearCostAmount": convert_int(excel_instance.InstantClearCostAmount(), password),
        "IsTutorial": bool(excel_instance.IsTutorial()),
    }

def dump_MiniGameTBGThemaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ThemaRound": convert_int(excel_instance.ThemaRound(), password),
        "ThemaUniqueId": convert_int(excel_instance.ThemaUniqueId(), password),
        "IsLoop": bool(excel_instance.IsLoop()),
        "MiniGameTBGThemaRewardType": MiniGameTBGThemaRewardType(convert_int(excel_instance.MiniGameTBGThemaRewardType(), password)).name,
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_MinigameTBGVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "VoiceCondition": TBGVoiceCondition(convert_int(excel_instance.VoiceCondition(), password)).name,
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_MissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Category": MissionCategory(convert_int(excel_instance.Category(), password)).name,
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": MissionResetType(convert_int(excel_instance.ResetType(), password)).name,
        "ToastDisplayType": MissionToastDisplayConditionType(convert_int(excel_instance.ToastDisplayType(), password)).name,
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "Limit": bool(excel_instance.Limit()),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "EndDay": convert_int(excel_instance.EndDay(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "DateAutoRefer": ContentType(convert_int(excel_instance.DateAutoRefer(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "PreMissionIdLength": convert_int(excel_instance.PreMissionIdLength(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ContentTagsLength": convert_int(excel_instance.ContentTagsLength(), password),
        "ShortcutUILength": convert_int(excel_instance.ShortcutUILength(), password),
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": MissionCompleteConditionType(convert_int(excel_instance.CompleteConditionType(), password)).name,
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameterLength": convert_int(excel_instance.CompleteConditionParameterLength(), password),
        "CompleteConditionParameterTagLength": convert_int(excel_instance.CompleteConditionParameterTagLength(), password),
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "MissionRewardParcelTypeLength": convert_int(excel_instance.MissionRewardParcelTypeLength(), password),
        "MissionRewardParcelIdLength": convert_int(excel_instance.MissionRewardParcelIdLength(), password),
        "MissionRewardAmountLength": convert_int(excel_instance.MissionRewardAmountLength(), password),
    }

def dump_NormalSkillTemplateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_int(excel_instance.Index(), password),
        "FirstCoolTime": convert_float(excel_instance.FirstCoolTime(), password),
        "CoolTime": convert_float(excel_instance.CoolTime(), password),
        "MultiAni": bool(excel_instance.MultiAni()),
    }

def dump_ObstacleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Index": convert_int(excel_instance.Index(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "JumpAble": bool(excel_instance.JumpAble()),
        "SubOffsetLength": convert_int(excel_instance.SubOffsetLength(), password),
        "X": convert_float(excel_instance.X(), password),
        "Z": convert_float(excel_instance.Z(), password),
        "Hp": convert_int(excel_instance.Hp(), password),
        "MaxHp": convert_int(excel_instance.MaxHp(), password),
        "BlockRate": convert_int(excel_instance.BlockRate(), password),
        "EvasionRate": convert_int(excel_instance.EvasionRate(), password),
        "DestroyType": ObstacleDestroyType(convert_int(excel_instance.DestroyType(), password)).name,
        "Point1OffesetLength": convert_int(excel_instance.Point1OffesetLength(), password),
        "EnemyPoint1OssetLength": convert_int(excel_instance.EnemyPoint1OssetLength(), password),
        "Point2OffesetLength": convert_int(excel_instance.Point2OffesetLength(), password),
        "EnemyPoint2OssetLength": convert_int(excel_instance.EnemyPoint2OssetLength(), password),
        "SubObstacleIDLength": convert_int(excel_instance.SubObstacleIDLength(), password),
    }

def dump_ObstacleFireLineCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MyObstacleFireLineCheck": bool(excel_instance.MyObstacleFireLineCheck()),
        "AllyObstacleFireLineCheck": bool(excel_instance.AllyObstacleFireLineCheck()),
        "EnemyObstacleFireLineCheck": bool(excel_instance.EnemyObstacleFireLineCheck()),
        "EmptyObstacleFireLineCheck": bool(excel_instance.EmptyObstacleFireLineCheck()),
    }

def dump_ParcelAutoSynthExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RequireParcelType": ParcelType(convert_int(excel_instance.RequireParcelType(), password)).name,
        "RequireParcelId": convert_int(excel_instance.RequireParcelId(), password),
        "RequireParcelAmount": convert_int(excel_instance.RequireParcelAmount(), password),
        "SynthStartAmount": convert_int(excel_instance.SynthStartAmount(), password),
        "SynthEndAmount": convert_int(excel_instance.SynthEndAmount(), password),
        "SynthMaxItem": bool(excel_instance.SynthMaxItem()),
        "ResultParcelType": ParcelType(convert_int(excel_instance.ResultParcelType(), password)).name,
        "ResultParcelId": convert_int(excel_instance.ResultParcelId(), password),
        "ResultParcelAmount": convert_int(excel_instance.ResultParcelAmount(), password),
    }

def dump_PersonalityExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
    }

def dump_PickupDuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ShopCategoryType": convert_float(excel_instance.ShopCategoryType(), password),
        "ShopId": convert_int(excel_instance.ShopId(), password),
        "PickupCharacterId": convert_int(excel_instance.PickupCharacterId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_PresetCharacterGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PresetCharacterGroupId": convert_int(excel_instance.PresetCharacterGroupId(), password),
        "GetPresetType": convert_string(excel_instance.GetPresetType(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "FavorRank": convert_int(excel_instance.FavorRank(), password),
        "StarGrade": convert_int(excel_instance.StarGrade(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevel(), password),
        "PassiveSkillLevel": convert_int(excel_instance.PassiveSkillLevel(), password),
        "ExtraPassiveSkillLevel": convert_int(excel_instance.ExtraPassiveSkillLevel(), password),
        "CommonSkillLevel": convert_int(excel_instance.CommonSkillLevel(), password),
        "LeaderSkillLevel": convert_int(excel_instance.LeaderSkillLevel(), password),
        "EquipSlot01": bool(excel_instance.EquipSlot01()),
        "EquipSlotTier01": convert_int(excel_instance.EquipSlotTier01(), password),
        "EquipSlotLevel01": convert_int(excel_instance.EquipSlotLevel01(), password),
        "EquipSlot02": bool(excel_instance.EquipSlot02()),
        "EquipSlotTier02": convert_int(excel_instance.EquipSlotTier02(), password),
        "EquipSlotLevel02": convert_int(excel_instance.EquipSlotLevel02(), password),
        "EquipSlot03": bool(excel_instance.EquipSlot03()),
        "EquipSlotTier03": convert_int(excel_instance.EquipSlotTier03(), password),
        "EquipSlotLevel03": convert_int(excel_instance.EquipSlotLevel03(), password),
        "EquipCharacterWeapon": bool(excel_instance.EquipCharacterWeapon()),
        "EquipCharacterWeaponTier": convert_int(excel_instance.EquipCharacterWeaponTier(), password),
        "EquipCharacterWeaponLevel": convert_int(excel_instance.EquipCharacterWeaponLevel(), password),
        "EquipCharacterGear": bool(excel_instance.EquipCharacterGear()),
        "EquipCharacterGearTier": convert_int(excel_instance.EquipCharacterGearTier(), password),
        "EquipCharacterGearLevel": convert_int(excel_instance.EquipCharacterGearLevel(), password),
        "PotentialType01": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType01(), password)).name,
        "PotentialLevel01": convert_int(excel_instance.PotentialLevel01(), password),
        "PotentialType02": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType02(), password)).name,
        "PotentialLevel02": convert_int(excel_instance.PotentialLevel02(), password),
        "PotentialType03": PotentialStatBonusRateType(convert_int(excel_instance.PotentialType03(), password)).name,
        "PotentialLevel03": convert_int(excel_instance.PotentialLevel03(), password),
    }

def dump_PresetCharacterGroupSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ArenaSimulatorFixed": bool(excel_instance.ArenaSimulatorFixed()),
        "PresetTypeLength": convert_int(excel_instance.PresetTypeLength(), password),
    }

def dump_PresetParcelsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "PresetGroupId": convert_int(excel_instance.PresetGroupId(), password),
        "ParcelAmount": convert_int(excel_instance.ParcelAmount(), password),
    }

def dump_ProductExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreType(), password)).name,
        "Price": convert_int(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "PurchasePeriodType": PurchasePeriodType(convert_int(excel_instance.PurchasePeriodType(), password)).name,
        "PurchasePeriodLimit": convert_int(excel_instance.PurchasePeriodLimit(), password),
        "ParcelTypeLength": convert_int(excel_instance.ParcelTypeLength(), password),
        "ParcelIdLength": convert_int(excel_instance.ParcelIdLength(), password),
        "ParcelAmountLength": convert_int(excel_instance.ParcelAmountLength(), password),
    }

def dump_ProductMonthlyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "StoreType": StoreType(convert_int(excel_instance.StoreType(), password)).name,
        "Price": convert_int(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "ProductTagType": ProductTagType(convert_int(excel_instance.ProductTagType(), password)).name,
        "MonthlyDays": convert_int(excel_instance.MonthlyDays(), password),
        "UseMonthlyProductCheck": bool(excel_instance.UseMonthlyProductCheck()),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "ParcelTypeLength": convert_int(excel_instance.ParcelTypeLength(), password),
        "ParcelIdLength": convert_int(excel_instance.ParcelIdLength(), password),
        "ParcelAmountLength": convert_int(excel_instance.ParcelAmountLength(), password),
        "EnterCostReduceGroupId": convert_int(excel_instance.EnterCostReduceGroupId(), password),
        "DailyParcelTypeLength": convert_int(excel_instance.DailyParcelTypeLength(), password),
        "DailyParcelIdLength": convert_int(excel_instance.DailyParcelIdLength(), password),
        "DailyParcelAmountLength": convert_int(excel_instance.DailyParcelAmountLength(), password),
    }

def dump_PropVector3(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Y": convert_float(excel_instance.Y(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_PropMotion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "PositionsLength": convert_int(excel_instance.PositionsLength(), password),
        "RotationsLength": convert_int(excel_instance.RotationsLength(), password),
    }

def dump_PropRootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "RootMotionsLength": convert_int(excel_instance.RootMotionsLength(), password),
    }

def dump_ProtocolSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Protocol": convert_string(excel_instance.Protocol(), password),
        "OpenConditionContent": OpenConditionContent(convert_int(excel_instance.OpenConditionContent(), password)).name,
        "Currency": bool(excel_instance.Currency()),
        "Inventory": bool(excel_instance.Inventory()),
        "Mail": bool(excel_instance.Mail()),
    }

def dump_RaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelUniqueIdLength": convert_int(excel_instance.RewardParcelUniqueIdLength(), password),
        "RewardParcelUniqueNameLength": convert_int(excel_instance.RewardParcelUniqueNameLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_RaidRankingRewardUOExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelUniqueIdLength": convert_int(excel_instance.RewardParcelUniqueIdLength(), password),
        "RewardParcelUniqueNameLength": convert_int(excel_instance.RewardParcelUniqueNameLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_RaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "SeasonDisplay": convert_int(excel_instance.SeasonDisplay(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartData(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndData(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "OpenRaidBossGroupLength": convert_int(excel_instance.OpenRaidBossGroupLength(), password),
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauage(), password),
        "StackedSeasonRewardGaugeLength": convert_int(excel_instance.StackedSeasonRewardGaugeLength(), password),
        "SeasonRewardIdLength": convert_int(excel_instance.SeasonRewardIdLength(), password),
    }

def dump_RaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndex()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSync()),
        "RaidBossGroup": convert_string(excel_instance.RaidBossGroup(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterId(), password),
        "BossCharacterIdLength": convert_int(excel_instance.BossCharacterIdLength(), password),
        "Difficulty": Difficulty(convert_int(excel_instance.Difficulty(), password)).name,
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenCondition()),
        "MaxPlayerCount": convert_int(excel_instance.MaxPlayerCount(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTime(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "GroundDevName": convert_string(excel_instance.GroundDevName(), password),
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLine(), password),
        "TacticEnvironment": TacticEnvironment(convert_int(excel_instance.TacticEnvironment(), password)).name,
        "DefaultClearScore": convert_int(excel_instance.DefaultClearScore(), password),
        "MaximumScore": convert_int(excel_instance.MaximumScore(), password),
        "PerSecondMinusScore": convert_int(excel_instance.PerSecondMinusScore(), password),
        "HPPercentScore": convert_int(excel_instance.HPPercentScore(), password),
        "MinimumAcquisitionScore": convert_int(excel_instance.MinimumAcquisitionScore(), password),
        "MaximumAcquisitionScore": convert_int(excel_instance.MaximumAcquisitionScore(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePathLength": convert_int(excel_instance.BattleReadyTimelinePathLength(), password),
        "BattleReadyTimelinePhaseStartLength": convert_int(excel_instance.BattleReadyTimelinePhaseStartLength(), password),
        "BattleReadyTimelinePhaseEndLength": convert_int(excel_instance.BattleReadyTimelinePhaseEndLength(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKey(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_RaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_RaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_int(excel_instance.SeasonRewardId(), password),
        "SeasonRewardParcelTypeLength": convert_int(excel_instance.SeasonRewardParcelTypeLength(), password),
        "SeasonRewardParcelUniqueIdLength": convert_int(excel_instance.SeasonRewardParcelUniqueIdLength(), password),
        "SeasonRewardParcelUniqueNameLength": convert_int(excel_instance.SeasonRewardParcelUniqueNameLength(), password),
        "SeasonRewardAmountLength": convert_int(excel_instance.SeasonRewardAmountLength(), password),
    }

def dump_RecipeCraftExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeType(), password)).name,
        "RecipeIngredientId": convert_int(excel_instance.RecipeIngredientId(), password),
        "RecipeIngredientDevName": convert_string(excel_instance.RecipeIngredientDevName(), password),
        "ParcelTypeLength": convert_int(excel_instance.ParcelTypeLength(), password),
        "ParcelIdLength": convert_int(excel_instance.ParcelIdLength(), password),
        "ParcelDevNameLength": convert_int(excel_instance.ParcelDevNameLength(), password),
        "ResultAmountMinLength": convert_int(excel_instance.ResultAmountMinLength(), password),
        "ResultAmountMaxLength": convert_int(excel_instance.ResultAmountMaxLength(), password),
    }

def dump_RecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeType(), password)).name,
        "RecipeIngredientId": convert_int(excel_instance.RecipeIngredientId(), password),
        "RecipeSelectionGroupId": convert_int(excel_instance.RecipeSelectionGroupId(), password),
        "ParcelTypeLength": convert_int(excel_instance.ParcelTypeLength(), password),
        "ParcelIdLength": convert_int(excel_instance.ParcelIdLength(), password),
        "ResultAmountMinLength": convert_int(excel_instance.ResultAmountMinLength(), password),
        "ResultAmountMaxLength": convert_int(excel_instance.ResultAmountMaxLength(), password),
    }

def dump_RecipeIngredientExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RecipeType": RecipeType(convert_int(excel_instance.RecipeType(), password)).name,
        "CostParcelTypeLength": convert_int(excel_instance.CostParcelTypeLength(), password),
        "CostIdLength": convert_int(excel_instance.CostIdLength(), password),
        "CostAmountLength": convert_int(excel_instance.CostAmountLength(), password),
        "IngredientParcelTypeLength": convert_int(excel_instance.IngredientParcelTypeLength(), password),
        "IngredientIdLength": convert_int(excel_instance.IngredientIdLength(), password),
        "IngredientAmountLength": convert_int(excel_instance.IngredientAmountLength(), password),
        "CostTimeInSecond": convert_int(excel_instance.CostTimeInSecond(), password),
    }

def dump_RecipeSelectionAutoUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "TargetItemId": convert_int(excel_instance.TargetItemId(), password),
        "PriorityLength": convert_int(excel_instance.PriorityLength(), password),
    }

def dump_RecipeSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RecipeSelectionGroupId": convert_int(excel_instance.RecipeSelectionGroupId(), password),
        "RecipeSelectionGroupComponentId": convert_int(excel_instance.RecipeSelectionGroupComponentId(), password),
        "ParcelType": ParcelType(convert_int(excel_instance.ParcelType(), password)).name,
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "ResultAmountMin": convert_int(excel_instance.ResultAmountMin(), password),
        "ResultAmountMax": convert_int(excel_instance.ResultAmountMax(), password),
    }

def dump_Position(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_Motion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "PositionsLength": convert_int(excel_instance.PositionsLength(), password),
    }

def dump_MoveEnd(excel_instance, password: bytes = b"") -> dict:
    return {
                            }

def dump_Form(excel_instance, password: bytes = b"") -> dict:
    return {
                    }

def dump_RootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "FormsLength": convert_int(excel_instance.FormsLength(), password),
        "ExSkillsLength": convert_int(excel_instance.ExSkillsLength(), password),
                    }

def dump_ScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NoneLength": convert_int(excel_instance.NoneLength(), password),
        "IdleLength": convert_int(excel_instance.IdleLength(), password),
        "Cafe": DialogCategory(convert_int(excel_instance.Cafe(), password)).name,
        "Talk": DialogType(convert_int(excel_instance.Talk(), password)).name,
        "Open": StoryCondition(convert_int(excel_instance.Open(), password)).name,
        "EnterConver": EmojiEvent(convert_int(excel_instance.EnterConver(), password)).name,
        "Center": ScenarioZoomAnchors(convert_int(excel_instance.Center(), password)).name,
        "Instant": ScenarioZoomType(convert_int(excel_instance.Instant(), password)).name,
        "Prologue": ScenarioContentType(convert_int(excel_instance.Prologue(), password)).name,
    }

def dump_ScenarioReplayExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_int(excel_instance.ModeId(), password),
        "VolumeId": convert_int(excel_instance.VolumeId(), password),
        "ReplayType": ScenarioModeReplayTypes(convert_int(excel_instance.ReplayType(), password)).name,
        "ChapterId": convert_int(excel_instance.ChapterId(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeId(), password),
        "FrontScenarioGroupIdLength": convert_int(excel_instance.FrontScenarioGroupIdLength(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "BackScenarioGroupIdLength": convert_int(excel_instance.BackScenarioGroupIdLength(), password),
    }

def dump_ScenarioScriptField1Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "SelectionGroup": convert_int(excel_instance.SelectionGroup(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "Sound": convert_string(excel_instance.Sound(), password),
        "Transition": convert_uint(excel_instance.Transition(), password),
        "BGName": convert_uint(excel_instance.BGName(), password),
        "BGEffect": convert_uint(excel_instance.BGEffect(), password),
        "PopupFileName": convert_string(excel_instance.PopupFileName(), password),
        "ScriptKr": convert_string(excel_instance.ScriptKr(), password),
        "TextJp": convert_string(excel_instance.TextJp(), password),
        "VoiceJp": convert_string(excel_instance.VoiceJp(), password),
    }

def dump_ScenarioScriptTestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "SelectionGroup": convert_int(excel_instance.SelectionGroup(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "Sound": convert_string(excel_instance.Sound(), password),
        "Transition": convert_uint(excel_instance.Transition(), password),
        "BGName": convert_uint(excel_instance.BGName(), password),
        "BGEffect": convert_uint(excel_instance.BGEffect(), password),
        "PopupFileName": convert_string(excel_instance.PopupFileName(), password),
        "ScriptKr": convert_string(excel_instance.ScriptKr(), password),
        "TextJp": convert_string(excel_instance.TextJp(), password),
        "VoiceId": convert_string(excel_instance.VoiceId(), password),
    }

def dump_ShiftingCraftRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "NotificationId": convert_int(excel_instance.NotificationId(), password),
        "ResultParcel": ParcelType(convert_int(excel_instance.ResultParcel(), password)).name,
        "ResultId": convert_int(excel_instance.ResultId(), password),
        "ResultAmount": convert_int(excel_instance.ResultAmount(), password),
        "RequireItemId": convert_int(excel_instance.RequireItemId(), password),
        "RequireItemAmount": convert_int(excel_instance.RequireItemAmount(), password),
        "RequireGold": convert_int(excel_instance.RequireGold(), password),
        "IngredientTagLength": convert_int(excel_instance.IngredientTagLength(), password),
        "IngredientExp": convert_int(excel_instance.IngredientExp(), password),
    }

def dump_ShopCashExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CashProductId": convert_int(excel_instance.CashProductId(), password),
        "PackageType": PurchaseSourceType(convert_int(excel_instance.PackageType(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "RenewalDisplayOrder": convert_int(excel_instance.RenewalDisplayOrder(), password),
        "CategoryType": ProductCategory(convert_int(excel_instance.CategoryType(), password)).name,
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PeriodTag": bool(excel_instance.PeriodTag()),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimit(), password),
        "AccountLevelHide": bool(excel_instance.AccountLevelHide()),
        "ClearMissionLimit": convert_int(excel_instance.ClearMissionLimit(), password),
        "ClearMissionHide": bool(excel_instance.ClearMissionHide()),
        "PurchaseReportEventName": convert_string(excel_instance.PurchaseReportEventName(), password),
    }

def dump_ShopCashScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioResrouceInfoId": convert_int(excel_instance.ScenarioResrouceInfoId(), password),
        "ShopCashId": convert_int(excel_instance.ShopCashId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
    }

def dump_ShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsIdLength": convert_int(excel_instance.GoodsIdLength(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetType(), password)).name,
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "RestrictBuyWhenInventoryFull": bool(excel_instance.RestrictBuyWhenInventoryFull()),
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
        "ShopUpdateGroupId": convert_int(excel_instance.ShopUpdateGroupId(), password),
    }

def dump_ShopFilterClassifiedExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "ConsumeParcelType": ParcelType(convert_int(excel_instance.ConsumeParcelType(), password)).name,
        "ConsumeParcelId": convert_int(excel_instance.ConsumeParcelId(), password),
        "ShopFilterType": ShopFilterType(convert_int(excel_instance.ShopFilterType(), password)).name,
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
    }

def dump_ShopFreeRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FreeRecruitPeriodFrom": convert_string(excel_instance.FreeRecruitPeriodFrom(), password),
        "FreeRecruitPeriodTo": convert_string(excel_instance.FreeRecruitPeriodTo(), password),
        "FreeRecruitType": ShopFreeRecruitType(convert_int(excel_instance.FreeRecruitType(), password)).name,
        "FreeRecruitDecorationImagePath": convert_string(excel_instance.FreeRecruitDecorationImagePath(), password),
        "ShopRecruitIdLength": convert_int(excel_instance.ShopRecruitIdLength(), password),
    }

def dump_ShopFreeRecruitPeriodExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ShopFreeRecruitId": convert_int(excel_instance.ShopFreeRecruitId(), password),
        "ShopFreeRecruitIntervalId": convert_int(excel_instance.ShopFreeRecruitIntervalId(), password),
        "IntervalDate": convert_string(excel_instance.IntervalDate(), password),
        "FreeRecruitCount": convert_int(excel_instance.FreeRecruitCount(), password),
    }

def dump_ShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "IsRefresh": bool(excel_instance.IsRefresh()),
        "IsSoldOutDimmed": bool(excel_instance.IsSoldOutDimmed()),
        "CostParcelTypeLength": convert_int(excel_instance.CostParcelTypeLength(), password),
        "CostParcelIdLength": convert_int(excel_instance.CostParcelIdLength(), password),
        "AutoRefreshCoolTime": convert_int(excel_instance.AutoRefreshCoolTime(), password),
        "RefreshAbleCount": convert_int(excel_instance.RefreshAbleCount(), password),
        "GoodsIdLength": convert_int(excel_instance.GoodsIdLength(), password),
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFrom(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodTo(), password),
        "ShopProductUpdateTime": convert_string(excel_instance.ShopProductUpdateTime(), password),
        "DisplayParcelType": ParcelType(convert_int(excel_instance.DisplayParcelType(), password)).name,
        "DisplayParcelId": convert_int(excel_instance.DisplayParcelId(), password),
        "IsShopVisible": bool(excel_instance.IsShopVisible()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ShopUpdateDate": convert_int(excel_instance.ShopUpdateDate(), password),
        "ShopUpdateGroupId1": convert_int(excel_instance.ShopUpdateGroupId1(), password),
        "ShopUpdateGroupId2": convert_int(excel_instance.ShopUpdateGroupId2(), password),
        "ShopUpdateGroupId3": convert_int(excel_instance.ShopUpdateGroupId3(), password),
        "ShopUpdateGroupId4": convert_int(excel_instance.ShopUpdateGroupId4(), password),
        "ShopUpdateGroupId5": convert_int(excel_instance.ShopUpdateGroupId5(), password),
        "ShopUpdateGroupId6": convert_int(excel_instance.ShopUpdateGroupId6(), password),
        "ShopUpdateGroupId7": convert_int(excel_instance.ShopUpdateGroupId7(), password),
        "ShopUpdateGroupId8": convert_int(excel_instance.ShopUpdateGroupId8(), password),
        "ShopUpdateGroupId9": convert_int(excel_instance.ShopUpdateGroupId9(), password),
        "ShopUpdateGroupId10": convert_int(excel_instance.ShopUpdateGroupId10(), password),
        "ShopUpdateGroupId11": convert_int(excel_instance.ShopUpdateGroupId11(), password),
        "ShopUpdateGroupId12": convert_int(excel_instance.ShopUpdateGroupId12(), password),
    }

def dump_ShopRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "OneGachaGoodsId": convert_int(excel_instance.OneGachaGoodsId(), password),
        "TenGachaGoodsId": convert_int(excel_instance.TenGachaGoodsId(), password),
        "GoodsDevName": convert_string(excel_instance.GoodsDevName(), password),
        "DisplayTag": GachaDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GachaBannerPath": convert_string(excel_instance.GachaBannerPath(), password),
        "VideoIdLength": convert_int(excel_instance.VideoIdLength(), password),
        "LinkedRobbyBannerId": convert_int(excel_instance.LinkedRobbyBannerId(), password),
        "InfoCharacterIdLength": convert_int(excel_instance.InfoCharacterIdLength(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "RecruitCoinId": convert_int(excel_instance.RecruitCoinId(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopId(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": PurchaseCountResetType(convert_int(excel_instance.PurchaseCountResetType(), password)).name,
        "IsNewbie": bool(excel_instance.IsNewbie()),
        "IsSelectRecruit": bool(excel_instance.IsSelectRecruit()),
        "DirectPayInvisibleTokenId": convert_int(excel_instance.DirectPayInvisibleTokenId(), password),
        "DirectPayAndroidShopCashId": convert_int(excel_instance.DirectPayAndroidShopCashId(), password),
        "DirectPayAppleShopCashId": convert_int(excel_instance.DirectPayAppleShopCashId(), password),
        "DirectPayHarmonyShopCashId": convert_int(excel_instance.DirectPayHarmonyShopCashId(), password),
    }

def dump_ShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
        "IsBundle": bool(excel_instance.IsBundle()),
        "VisibleAmount": convert_int(excel_instance.VisibleAmount(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "DisplayTag": ProductDisplayTag(convert_int(excel_instance.DisplayTag(), password)).name,
    }

def dump_SkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeSkillId": convert_uint(excel_instance.LocalizeSkillId(), password),
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "SkillDataKey": convert_string(excel_instance.SkillDataKey(), password),
        "VisualDataKey": convert_string(excel_instance.VisualDataKey(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "SkillCost": convert_int(excel_instance.SkillCost(), password),
        "ExtraSkillCost": convert_int(excel_instance.ExtraSkillCost(), password),
        "EnemySkillCost": convert_int(excel_instance.EnemySkillCost(), password),
        "ExtraEnemySkillCost": convert_int(excel_instance.ExtraEnemySkillCost(), password),
        "NPCSkillCost": convert_int(excel_instance.NPCSkillCost(), password),
        "ExtraNPCSkillCost": convert_int(excel_instance.ExtraNPCSkillCost(), password),
        "BulletType": BulletType(convert_int(excel_instance.BulletType(), password)).name,
        "StartCoolTime": convert_int(excel_instance.StartCoolTime(), password),
        "CoolTime": convert_int(excel_instance.CoolTime(), password),
        "EnemyStartCoolTime": convert_int(excel_instance.EnemyStartCoolTime(), password),
        "EnemyCoolTime": convert_int(excel_instance.EnemyCoolTime(), password),
        "NPCStartCoolTime": convert_int(excel_instance.NPCStartCoolTime(), password),
        "NPCCoolTime": convert_int(excel_instance.NPCCoolTime(), password),
        "UseAtg": convert_int(excel_instance.UseAtg(), password),
        "RequireCharacterLevel": convert_int(excel_instance.RequireCharacterLevel(), password),
        "RequireLevelUpMaterial": convert_int(excel_instance.RequireLevelUpMaterial(), password),
        "IconName": convert_string(excel_instance.IconName(), password),
        "IsShowInfo": bool(excel_instance.IsShowInfo()),
        "IsShowSpeechbubble": bool(excel_instance.IsShowSpeechbubble()),
        "PublicSpeechDuration": convert_int(excel_instance.PublicSpeechDuration(), password),
        "AdditionalToolTipId": convert_int(excel_instance.AdditionalToolTipId(), password),
        "TextureSkillCardForFormConversion": convert_string(excel_instance.TextureSkillCardForFormConversion(), password),
        "SkillCardLabelPath": convert_string(excel_instance.SkillCardLabelPath(), password),
    }

def dump_SpecialLobbyIllustExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CharacterCostumeUniqueId": convert_int(excel_instance.CharacterCostumeUniqueId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "SlotTextureName": convert_string(excel_instance.SlotTextureName(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureName(), password),
    }

def dump_StrategyObjectBuffDefineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StrategyObjectBuffID": convert_int(excel_instance.StrategyObjectBuffID(), password),
        "StrategyObjectTurn": convert_int(excel_instance.StrategyObjectTurn(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
    }

def dump_StringTestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringLength": convert_int(excel_instance.StringLength(), password),
        "Sentence1": convert_string(excel_instance.Sentence1(), password),
        "Script": convert_string(excel_instance.Script(), password),
    }

def dump_SystemMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "ExpiredDay": convert_int(excel_instance.ExpiredDay(), password),
        "Sender": convert_string(excel_instance.Sender(), password),
        "Comment": convert_string(excel_instance.Comment(), password),
    }

def dump_TacticalSupportSystemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SummonedTime": convert_int(excel_instance.SummonedTime(), password),
        "DefaultPersonalityId": convert_int(excel_instance.DefaultPersonalityId(), password),
        "CanTargeting": bool(excel_instance.CanTargeting()),
        "CanCover": bool(excel_instance.CanCover()),
        "ObstacleUniqueName": convert_string(excel_instance.ObstacleUniqueName(), password),
        "ObstacleCoverRange": convert_int(excel_instance.ObstacleCoverRange(), password),
        "SummonSkilllGroupId": convert_string(excel_instance.SummonSkilllGroupId(), password),
        "CrashObstacleOBBWidth": convert_int(excel_instance.CrashObstacleOBBWidth(), password),
        "CrashObstacleOBBHeight": convert_int(excel_instance.CrashObstacleOBBHeight(), password),
        "IsTSSBlockedNodeCheck": bool(excel_instance.IsTSSBlockedNodeCheck()),
        "NumberOfUses": convert_int(excel_instance.NumberOfUses(), password),
        "InventoryOffsetX": convert_float(excel_instance.InventoryOffsetX(), password),
        "InventoryOffsetY": convert_float(excel_instance.InventoryOffsetY(), password),
        "InventoryOffsetZ": convert_float(excel_instance.InventoryOffsetZ(), password),
        "InteractionChar": convert_int(excel_instance.InteractionChar(), password),
        "CharacterInteractionStartDelay": convert_int(excel_instance.CharacterInteractionStartDelay(), password),
        "GetOnStartEffectPath": convert_string(excel_instance.GetOnStartEffectPath(), password),
        "GetOnEndEffectPath": convert_string(excel_instance.GetOnEndEffectPath(), password),
        "SummonerCharacterId": convert_int(excel_instance.SummonerCharacterId(), password),
        "InteractionFrame": convert_int(excel_instance.InteractionFrame(), password),
        "TSAInteractionAddDuration": convert_int(excel_instance.TSAInteractionAddDuration(), password),
        "InteractionStudentExSkillGroupId": convert_string(excel_instance.InteractionStudentExSkillGroupId(), password),
        "InteractionSkillCardTexture": convert_string(excel_instance.InteractionSkillCardTexture(), password),
        "InteractionSkillSpine": convert_string(excel_instance.InteractionSkillSpine(), password),
        "RetreatFrame": convert_int(excel_instance.RetreatFrame(), password),
        "DestroyFrame": convert_int(excel_instance.DestroyFrame(), password),
    }

def dump_TacticArenaSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.Order(), password),
        "Repeat": convert_int(excel_instance.Repeat(), password),
        "AttackerFrom": ArenaSimulatorServer(convert_int(excel_instance.AttackerFrom(), password)).name,
        "AttackerUserArenaGroup": convert_int(excel_instance.AttackerUserArenaGroup(), password),
        "AttackerUserArenaRank": convert_int(excel_instance.AttackerUserArenaRank(), password),
        "AttackerPresetGroupId": convert_int(excel_instance.AttackerPresetGroupId(), password),
        "AttackerStrikerNum": convert_int(excel_instance.AttackerStrikerNum(), password),
        "AttackerSpecialNum": convert_int(excel_instance.AttackerSpecialNum(), password),
        "DefenderFrom": ArenaSimulatorServer(convert_int(excel_instance.DefenderFrom(), password)).name,
        "DefenderUserArenaGroup": convert_int(excel_instance.DefenderUserArenaGroup(), password),
        "DefenderUserArenaRank": convert_int(excel_instance.DefenderUserArenaRank(), password),
        "DefenderPresetGroupId": convert_int(excel_instance.DefenderPresetGroupId(), password),
        "DefenderStrikerNum": convert_int(excel_instance.DefenderStrikerNum(), password),
        "DefenderSpecialNum": convert_int(excel_instance.DefenderSpecialNum(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
    }

def dump_TacticDamageSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.Order(), password),
        "Repeat": convert_int(excel_instance.Repeat(), password),
        "TestPreset": convert_int(excel_instance.TestPreset(), password),
        "TestBattleTime": convert_int(excel_instance.TestBattleTime(), password),
        "StrikerSquard": convert_int(excel_instance.StrikerSquard(), password),
        "SpecialSquard": convert_int(excel_instance.SpecialSquard(), password),
        "ReplaceCharacterCostRegen": bool(excel_instance.ReplaceCharacterCostRegen()),
        "ReplaceCostRegenValue": convert_int(excel_instance.ReplaceCostRegenValue(), password),
        "UseAutoSkill": bool(excel_instance.UseAutoSkill()),
        "OverrideStreetAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideStreetAdaptation(), password)).name,
        "OverrideOutdoorAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideOutdoorAdaptation(), password)).name,
        "OverrideIndoorAdaptation": TerrainAdaptationStat(convert_int(excel_instance.OverrideIndoorAdaptation(), password)).name,
        "ApplyOverrideAdaptation": bool(excel_instance.ApplyOverrideAdaptation()),
        "OverrideFavorLevel": convert_int(excel_instance.OverrideFavorLevel(), password),
        "ApplyOverrideFavorLevel": bool(excel_instance.ApplyOverrideFavorLevel()),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "FixedCharacterLength": convert_int(excel_instance.FixedCharacterLength(), password),
    }

def dump_TacticEntityEffectFilterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TargetEffectName": convert_string(excel_instance.TargetEffectName(), password),
        "ShowEffectToVehicle": bool(excel_instance.ShowEffectToVehicle()),
        "ShowEffectToBoss": bool(excel_instance.ShowEffectToBoss()),
    }

def dump_TacticSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
    }

def dump_TacticSkipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiff(), password),
        "HPResult": convert_int(excel_instance.HPResult(), password),
    }

def dump_TacticTimeAttackSimulatorConfigExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.Order(), password),
        "Repeat": convert_int(excel_instance.Repeat(), password),
        "PresetGroupId": convert_int(excel_instance.PresetGroupId(), password),
        "AttackStrikerNum": convert_int(excel_instance.AttackStrikerNum(), password),
        "AttackSpecialNum": convert_int(excel_instance.AttackSpecialNum(), password),
        "GeasId": convert_int(excel_instance.GeasId(), password),
    }

def dump_TagExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Furniture": Tag(convert_int(excel_instance.Furniture(), password)).name,
        "None_": Club(convert_int(excel_instance.None_(), password)).name,
    }

def dump_TerrainAdaptationFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TerrainAdaptation": StageTopography(convert_int(excel_instance.TerrainAdaptation(), password)).name,
        "TerrainAdaptationStat": TerrainAdaptationStat(convert_int(excel_instance.TerrainAdaptationStat(), password)).name,
        "ShotFactor": convert_int(excel_instance.ShotFactor(), password),
        "BlockFactor": convert_int(excel_instance.BlockFactor(), password),
        "AccuracyFactor": convert_int(excel_instance.AccuracyFactor(), password),
        "DodgeFactor": convert_int(excel_instance.DodgeFactor(), password),
        "AttackPowerFactor": convert_int(excel_instance.AttackPowerFactor(), password),
    }

def dump_TimeAttackDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TimeAttackDungeonType": TimeAttackDungeonType(convert_int(excel_instance.TimeAttackDungeonType(), password)).name,
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKey(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "InformationGroupID": convert_int(excel_instance.InformationGroupID(), password),
    }

def dump_TimeAttackDungeonGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TimeAttackDungeonType": TimeAttackDungeonType(convert_int(excel_instance.TimeAttackDungeonType(), password)).name,
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKey(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "ClearDefaultPoint": convert_int(excel_instance.ClearDefaultPoint(), password),
        "ClearTimeWeightPoint": convert_int(excel_instance.ClearTimeWeightPoint(), password),
        "TimeWeightConst": convert_int(excel_instance.TimeWeightConst(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "AllyPassiveSkillIdLength": convert_int(excel_instance.AllyPassiveSkillIdLength(), password),
        "AllyPassiveSkillLevelLength": convert_int(excel_instance.AllyPassiveSkillLevelLength(), password),
        "EnemyPassiveSkillIdLength": convert_int(excel_instance.EnemyPassiveSkillIdLength(), password),
        "EnemyPassiveSkillLevelLength": convert_int(excel_instance.EnemyPassiveSkillLevelLength(), password),
        "GeasIconPathLength": convert_int(excel_instance.GeasIconPathLength(), password),
        "GeasLocalizeEtcKeyLength": convert_int(excel_instance.GeasLocalizeEtcKeyLength(), password),
    }

def dump_TimeAttackDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RewardMaxPoint": convert_int(excel_instance.RewardMaxPoint(), password),
        "RewardTypeLength": convert_int(excel_instance.RewardTypeLength(), password),
        "RewardMinPointLength": convert_int(excel_instance.RewardMinPointLength(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelDefaultAmountLength": convert_int(excel_instance.RewardParcelDefaultAmountLength(), password),
        "RewardParcelMaxAmountLength": convert_int(excel_instance.RewardParcelMaxAmountLength(), password),
    }

def dump_TimeAttackDungeonSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "UISlot": convert_int(excel_instance.UISlot(), password),
        "DungeonId": convert_int(excel_instance.DungeonId(), password),
        "DifficultyGeasLength": convert_int(excel_instance.DifficultyGeasLength(), password),
        "TimeAttackDungeonRewardId": convert_int(excel_instance.TimeAttackDungeonRewardId(), password),
        "RoomLifeTimeInSeconds": convert_int(excel_instance.RoomLifeTimeInSeconds(), password),
    }

def dump_TranscendenceRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CostCurrencyType": CurrencyTypes(convert_int(excel_instance.CostCurrencyType(), password)).name,
        "CostCurrencyAmount": convert_int(excel_instance.CostCurrencyAmount(), password),
        "ParcelTypeLength": convert_int(excel_instance.ParcelTypeLength(), password),
        "ParcelIdLength": convert_int(excel_instance.ParcelIdLength(), password),
        "ParcelAmountLength": convert_int(excel_instance.ParcelAmountLength(), password),
    }

def dump_TrophyCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "FurnitureIdLength": convert_int(excel_instance.FurnitureIdLength(), password),
    }

def dump_VoiceSkillUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "VoiceHashLength": convert_int(excel_instance.VoiceHashLength(), password),
    }

def dump_WebSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WebId": convert_int(excel_instance.WebId(), password),
        "OpenTime": convert_string(excel_instance.OpenTime(), password),
        "CloseTime": convert_string(excel_instance.CloseTime(), password),
        "Type": convert_int(excel_instance.Type(), password),
        "MailExpiredDay": convert_int(excel_instance.MailExpiredDay(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPath(), password),
        "BannerType": EventContentType(convert_int(excel_instance.BannerType(), password)).name,
        "IconOrder": convert_int(excel_instance.IconOrder(), password),
        "Url": convert_string(excel_instance.Url(), password),
    }

def dump_WeekDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageId(), password),
        "WeekDungeonType": convert_float(excel_instance.WeekDungeonType(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "StageEnterCostTypeLength": convert_int(excel_instance.StageEnterCostTypeLength(), password),
        "StageEnterCostIdLength": convert_int(excel_instance.StageEnterCostIdLength(), password),
        "StageEnterCostAmountLength": convert_int(excel_instance.StageEnterCostAmountLength(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoalLength": convert_int(excel_instance.StarGoalLength(), password),
        "StarGoalAmountLength": convert_int(excel_instance.StarGoalAmountLength(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "BattleRewardExp": convert_int(excel_instance.BattleRewardExp(), password),
        "BattleRewardPlayerExp": convert_int(excel_instance.BattleRewardPlayerExp(), password),
        "GroupBuffIDLength": convert_int(excel_instance.GroupBuffIDLength(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_WeekDungeonFindGiftRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
        "RewardParcelProbabilityLength": convert_int(excel_instance.RewardParcelProbabilityLength(), password),
        "DropItemModelPrefabPathLength": convert_int(excel_instance.DropItemModelPrefabPathLength(), password),
    }

def dump_WeekDungeonGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDungeonBuffId": convert_int(excel_instance.WeekDungeonBuffId(), password),
        "School": School(convert_int(excel_instance.School(), password)).name,
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "FormationLocalizeEtcId": convert_uint(excel_instance.FormationLocalizeEtcId(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
    }

def dump_WeekDungeonOpenScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDay": WeekDay(convert_int(excel_instance.WeekDay(), password)).name,
        "OpenLength": convert_int(excel_instance.OpenLength(), password),
    }

def dump_WeekDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DungeonType": convert_float(excel_instance.DungeonType(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPath(), password),
    }

def dump_WorldRaidBossGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupId(), password),
        "WorldBossName": convert_string(excel_instance.WorldBossName(), password),
        "WorldBossPopupPortrait": convert_string(excel_instance.WorldBossPopupPortrait(), password),
        "WorldBossPopupBG": convert_string(excel_instance.WorldBossPopupBG(), password),
        "WorldBossParcelPortrait": convert_string(excel_instance.WorldBossParcelPortrait(), password),
        "WorldBossListParcel": convert_string(excel_instance.WorldBossListParcel(), password),
        "WorldBossHP": convert_int(excel_instance.WorldBossHP(), password),
        "WorldBossHPUO": convert_int(excel_instance.WorldBossHPUO(), password),
        "UIHideBeforeSpawn": bool(excel_instance.UIHideBeforeSpawn()),
        "HideAnotherBossKilled": bool(excel_instance.HideAnotherBossKilled()),
        "WorldBossClearRewardGroupId": convert_int(excel_instance.WorldBossClearRewardGroupId(), password),
        "AnotherBossKilledLength": convert_int(excel_instance.AnotherBossKilledLength(), password),
        "EchelonConstraintGroupId": convert_int(excel_instance.EchelonConstraintGroupId(), password),
        "ExclusiveOperatorBossSpawn": convert_string(excel_instance.ExclusiveOperatorBossSpawn(), password),
        "ExclusiveOperatorBossKill": convert_string(excel_instance.ExclusiveOperatorBossKill(), password),
        "ExclusiveOperatorScenarioBattle": convert_string(excel_instance.ExclusiveOperatorScenarioBattle(), password),
        "ExclusiveOperatorBossDamaged": convert_string(excel_instance.ExclusiveOperatorBossDamaged(), password),
        "BossGroupOpenCondition": convert_int(excel_instance.BossGroupOpenCondition(), password),
    }

def dump_WorldRaidFavorBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WorldRaidFavorRank": convert_int(excel_instance.WorldRaidFavorRank(), password),
        "WorldRaidFavorRankBonus": convert_int(excel_instance.WorldRaidFavorRankBonus(), password),
    }

def dump_WorldRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EnterTicket": CurrencyTypes(convert_int(excel_instance.EnterTicket(), password)).name,
        "WorldRaidLobbyScene": convert_string(excel_instance.WorldRaidLobbyScene(), password),
        "WorldRaidLobbyBanner": convert_string(excel_instance.WorldRaidLobbyBanner(), password),
        "WorldRaidLobbyBG": convert_string(excel_instance.WorldRaidLobbyBG(), password),
        "WorldRaidLobbyBannerShow": bool(excel_instance.WorldRaidLobbyBannerShow()),
        "SeasonOpenCondition": convert_int(excel_instance.SeasonOpenCondition(), password),
        "WorldRaidLobbyEnterScenario": convert_int(excel_instance.WorldRaidLobbyEnterScenario(), password),
        "CanPlayNotSeasonTime": bool(excel_instance.CanPlayNotSeasonTime()),
        "WorldRaidUniqueThemeLobbyUI": bool(excel_instance.WorldRaidUniqueThemeLobbyUI()),
        "WorldRaidUniqueThemeName": convert_string(excel_instance.WorldRaidUniqueThemeName(), password),
        "CanWorldRaidGemEnter": bool(excel_instance.CanWorldRaidGemEnter()),
        "HideWorldRaidTicketUI": bool(excel_instance.HideWorldRaidTicketUI()),
        "HideWorldRaidBossCompleteRewardUI": bool(excel_instance.HideWorldRaidBossCompleteRewardUI()),
        "UseWorldRaidCommonToast": bool(excel_instance.UseWorldRaidCommonToast()),
        "OpenRaidBossGroupIdLength": convert_int(excel_instance.OpenRaidBossGroupIdLength(), password),
        "BossSpawnTimeLength": convert_int(excel_instance.BossSpawnTimeLength(), password),
        "EliminateTimeLength": convert_int(excel_instance.EliminateTimeLength(), password),
        "ScenarioOutputConditionIdLength": convert_int(excel_instance.ScenarioOutputConditionIdLength(), password),
        "ConditionScenarioGroupidLength": convert_int(excel_instance.ConditionScenarioGroupidLength(), password),
        "WorldRaidMapEnterOperator": convert_string(excel_instance.WorldRaidMapEnterOperator(), password),
        "UseFavorRankBuff": bool(excel_instance.UseFavorRankBuff()),
    }

def dump_WorldRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndex()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSync()),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupId(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterId(), password),
        "BossCharacterIdLength": convert_int(excel_instance.BossCharacterIdLength(), password),
        "AssistCharacterLimitCount": convert_int(excel_instance.AssistCharacterLimitCount(), password),
        "WorldRaidDifficulty": WorldRaidDifficulty(convert_int(excel_instance.WorldRaidDifficulty(), password)).name,
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenCondition()),
        "RaidEnterAmount": convert_int(excel_instance.RaidEnterAmount(), password),
        "ReEnterAmount": convert_int(excel_instance.ReEnterAmount(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RaidBattleEndRewardGroupId": convert_int(excel_instance.RaidBattleEndRewardGroupId(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePathLength": convert_int(excel_instance.BattleReadyTimelinePathLength(), password),
        "BattleReadyTimelinePhaseStartLength": convert_int(excel_instance.BattleReadyTimelinePhaseStartLength(), password),
        "BattleReadyTimelinePhaseEndLength": convert_int(excel_instance.BattleReadyTimelinePhaseEndLength(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_int(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_int(excel_instance.ClearScenarioKey(), password),
        "UseFixedEchelon": bool(excel_instance.UseFixedEchelon()),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "IsRaidScenarioBattle": bool(excel_instance.IsRaidScenarioBattle()),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "DamageToWorldBoss": convert_int(excel_instance.DamageToWorldBoss(), password),
        "AllyPassiveSkillLength": convert_int(excel_instance.AllyPassiveSkillLength(), password),
        "AllyPassiveSkillLevelLength": convert_int(excel_instance.AllyPassiveSkillLevelLength(), password),
        "SaveCurrentLocalBossHP": bool(excel_instance.SaveCurrentLocalBossHP()),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_WorldRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_AccountLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "Exp": convert_int(excel_instance.Exp(), password),
        "NewbieExpRatio": convert_int(excel_instance.NewbieExpRatio(), password),
        "CloseInterval": convert_int(excel_instance.CloseInterval(), password),
        "APAutoChargeMax": convert_int(excel_instance.APAutoChargeMax(), password),
        "NeedReportEvent": bool(excel_instance.NeedReportEvent()),
    }

def dump_AssistEchelonTypeConvertExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Contents": EchelonType(convert_int(excel_instance.Contents(), password)).name,
        "ConvertTo": EchelonType(convert_int(excel_instance.ConvertTo(), password)).name,
    }

def dump_AttendanceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Type": AttendanceType(convert_int(excel_instance.Type(), password)).name,
        "CountdownPrefab": convert_string(excel_instance.CountdownPrefab(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "AccountType": AccountState(convert_int(excel_instance.AccountType(), password)).name,
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimit(), password),
        "Title": convert_string(excel_instance.Title(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCode(), password),
        "CountRule": AttendanceCountRule(convert_int(excel_instance.CountRule(), password)).name,
        "CountReset": AttendanceResetType(convert_int(excel_instance.CountReset(), password)).name,
        "BookSize": convert_int(excel_instance.BookSize(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDate(), password),
        "MailType": MailType(convert_int(excel_instance.MailType(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategory(), password)).name,
        "TitleImagePath": convert_string(excel_instance.TitleImagePath(), password),
        "DecorationImagePath": convert_string(excel_instance.DecorationImagePath(), password),
        "DecorationGarlandImagePath": convert_string(excel_instance.DecorationGarlandImagePath(), password),
    }

def dump_AttendanceRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttendanceId": convert_int(excel_instance.AttendanceId(), password),
        "Day": convert_int(excel_instance.Day(), password),
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardIdLength": convert_int(excel_instance.RewardIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_AudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHash(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefix(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHash(), password),
        "StateName": convert_string(excel_instance.StateName(), password),
        "IgnoreInterruptDelay": bool(excel_instance.IgnoreInterruptDelay()),
        "IgnoreInterruptPlay": bool(excel_instance.IgnoreInterruptPlay()),
        "Volume": convert_float(excel_instance.Volume(), password),
        "Delay": convert_float(excel_instance.Delay(), password),
        "RandomPitchMin": convert_int(excel_instance.RandomPitchMin(), password),
        "RandomPitchMax": convert_int(excel_instance.RandomPitchMax(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriority(), password),
        "AudioClipPathLength": convert_int(excel_instance.AudioClipPathLength(), password),
        "VoiceHashLength": convert_int(excel_instance.VoiceHashLength(), password),
    }

def dump_BGMExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "NationLength": convert_int(excel_instance.NationLength(), password),
        "PathLength": convert_int(excel_instance.PathLength(), password),
        "VolumeLength": convert_int(excel_instance.VolumeLength(), password),
        "LoopStartTimeLength": convert_int(excel_instance.LoopStartTimeLength(), password),
        "LoopEndTimeLength": convert_int(excel_instance.LoopEndTimeLength(), password),
        "LoopTranstionTimeLength": convert_int(excel_instance.LoopTranstionTimeLength(), password),
        "LoopOffsetTimeLength": convert_int(excel_instance.LoopOffsetTimeLength(), password),
    }

def dump_BGMRaidExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageId(), password),
        "PhaseIndex": convert_int(excel_instance.PhaseIndex(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
    }

def dump_BGMUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UIPrefab": convert_uint(excel_instance.UIPrefab(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "BGMId2nd": convert_int(excel_instance.BGMId2nd(), password),
        "BGMId3rd": convert_int(excel_instance.BGMId3rd(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
    }

def dump_CameraExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "MinDistance": convert_float(excel_instance.MinDistance(), password),
        "MaxDistance": convert_float(excel_instance.MaxDistance(), password),
        "RotationX": convert_float(excel_instance.RotationX(), password),
        "RotationY": convert_float(excel_instance.RotationY(), password),
        "MoveInstantly": bool(excel_instance.MoveInstantly()),
        "MoveInstantlyRotationSave": bool(excel_instance.MoveInstantlyRotationSave()),
        "LeftMargin": convert_float(excel_instance.LeftMargin(), password),
        "BottomMargin": convert_float(excel_instance.BottomMargin(), password),
        "IgnoreEnemies": bool(excel_instance.IgnoreEnemies()),
        "UseRailPointCompensation": bool(excel_instance.UseRailPointCompensation()),
    }

def dump_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": convert_string(excel_instance.DialogType(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "HideUI": bool(excel_instance.HideUI()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterDialogEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "OriginalCharacterId": convert_int(excel_instance.OriginalCharacterId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "EventID": convert_int(excel_instance.EventID(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategory(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogCondition(), password)).name,
        "DialogConditionDetail": DialogConditionDetail(convert_int(excel_instance.DialogConditionDetail(), password)).name,
        "DialogConditionDetailValue": convert_int(excel_instance.DialogConditionDetailValue(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogType(), password)).name,
        "ActionName": convert_string(excel_instance.ActionName(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "VoiceIdLength": convert_int(excel_instance.VoiceIdLength(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionType(), password)).name,
        "CVUnlockScenarioType": CVUnlockScenarioType(convert_int(excel_instance.CVUnlockScenarioType(), password)).name,
        "UnlockEventSeason": convert_int(excel_instance.UnlockEventSeason(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "DurationCN": convert_int(excel_instance.DurationCN(), password),
    }

def dump_CharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "DialogCategory": DialogCategory(convert_int(excel_instance.DialogCategory(), password)).name,
        "DialogCondition": DialogCondition(convert_int(excel_instance.DialogCondition(), password)).name,
        "Anniversary": Anniversary(convert_int(excel_instance.Anniversary(), password)).name,
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DialogType": DialogType(convert_int(excel_instance.DialogType(), password)).name,
        "ActionName": convert_string(excel_instance.ActionName(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "VoiceIdLength": convert_int(excel_instance.VoiceIdLength(), password),
        "ApplyPosition": bool(excel_instance.ApplyPosition()),
        "PosX": convert_float(excel_instance.PosX(), password),
        "PosY": convert_float(excel_instance.PosY(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionType(), password)).name,
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRank(), password),
        "UnlockEquipWeapon": bool(excel_instance.UnlockEquipWeapon()),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "DurationCN": convert_int(excel_instance.DurationCN(), password),
    }

def dump_CharacterDialogSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "Separate": bool(excel_instance.Separate()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CharacterGearExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "StatLevelUpType": StatLevelUpType(convert_int(excel_instance.StatLevelUpType(), password)).name,
        "Tier": convert_int(excel_instance.Tier(), password),
        "NextTierEquipment": convert_int(excel_instance.NextTierEquipment(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "OpenFavorLevel": convert_int(excel_instance.OpenFavorLevel(), password),
        "MaxLevel": convert_int(excel_instance.MaxLevel(), password),
        "LearnSkillSlot": convert_string(excel_instance.LearnSkillSlot(), password),
        "StatTypeLength": convert_int(excel_instance.StatTypeLength(), password),
        "MinStatValueLength": convert_int(excel_instance.MinStatValueLength(), password),
        "MaxStatValueLength": convert_int(excel_instance.MaxStatValueLength(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "TagsLength": convert_int(excel_instance.TagsLength(), password),
    }

def dump_CharacterGearLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "TierLevelExpLength": convert_int(excel_instance.TierLevelExpLength(), password),
        "TotalExpLength": convert_int(excel_instance.TotalExpLength(), password),
    }

def dump_CharacterPotentialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "PotentialStatGroupId": convert_int(excel_instance.PotentialStatGroupId(), password),
        "PotentialStatBonusRateType": PotentialStatBonusRateType(convert_int(excel_instance.PotentialStatBonusRateType(), password)).name,
        "IsUnnecessaryStat": bool(excel_instance.IsUnnecessaryStat()),
    }

def dump_CharacterPotentialRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RequirePotentialStatTypeLength": convert_int(excel_instance.RequirePotentialStatTypeLength(), password),
        "RequirePotentialStatLevelLength": convert_int(excel_instance.RequirePotentialStatLevelLength(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
    }

def dump_CharacterPotentialStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PotentialStatGroupId": convert_int(excel_instance.PotentialStatGroupId(), password),
        "PotentialLevel": convert_int(excel_instance.PotentialLevel(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "StatBonusRate": convert_int(excel_instance.StatBonusRate(), password),
    }

def dump_CharacterVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterVoiceUniqueId": convert_int(excel_instance.CharacterVoiceUniqueId(), password),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupId(), password),
        "VoiceHash": convert_uint(excel_instance.VoiceHash(), password),
        "OnlyOne": bool(excel_instance.OnlyOne()),
        "Priority": convert_int(excel_instance.Priority(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": CVCollectionType(convert_int(excel_instance.CVCollectionType(), password)).name,
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRank(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "NationLength": convert_int(excel_instance.NationLength(), password),
        "VolumeLength": convert_int(excel_instance.VolumeLength(), password),
        "DelayLength": convert_int(excel_instance.DelayLength(), password),
        "PathLength": convert_int(excel_instance.PathLength(), password),
    }

def dump_CharacterVoiceSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupId(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "Separate": bool(excel_instance.Separate()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
    }

def dump_CheatCodeListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CheatCodeLength": convert_int(excel_instance.CheatCodeLength(), password),
        "InputTitleLength": convert_int(excel_instance.InputTitleLength(), password),
        "Desc": convert_string(excel_instance.Desc(), password),
    }

def dump_ClanAssistSlotExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SlotId": convert_int(excel_instance.SlotId(), password),
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonType(), password)).name,
        "SlotNumber": convert_int(excel_instance.SlotNumber(), password),
        "AssistTermRewardPeriodFromSec": convert_int(excel_instance.AssistTermRewardPeriodFromSec(), password),
        "AssistRewardLimit": convert_int(excel_instance.AssistRewardLimit(), password),
        "AssistRentRewardDailyMaxCount": convert_int(excel_instance.AssistRentRewardDailyMaxCount(), password),
        "AssistRentalFeeAmount": convert_int(excel_instance.AssistRentalFeeAmount(), password),
        "AssistRentalFeeAmountStranger": convert_int(excel_instance.AssistRentalFeeAmountStranger(), password),
    }

def dump_ClanChattingEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TabGroupId": convert_int(excel_instance.TabGroupId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
    }

def dump_ClanRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ClanRewardType": ClanRewardType(convert_int(excel_instance.ClanRewardType(), password)).name,
        "EchelonType": EchelonType(convert_int(excel_instance.EchelonType(), password)).name,
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_CombatEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "EmojiEvent": EmojiEvent(convert_int(excel_instance.EmojiEvent(), password)).name,
        "OrderOfPriority": convert_int(excel_instance.OrderOfPriority(), password),
        "EmojiDuration": bool(excel_instance.EmojiDuration()),
        "EmojiReversal": bool(excel_instance.EmojiReversal()),
        "EmojiTurnOn": bool(excel_instance.EmojiTurnOn()),
        "ShowEmojiDelay": convert_int(excel_instance.ShowEmojiDelay(), password),
        "ShowDefaultBG": bool(excel_instance.ShowDefaultBG()),
    }

def dump_ContentEnterCostReduceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EnterCostReduceGroupId": convert_int(excel_instance.EnterCostReduceGroupId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "StageId": convert_int(excel_instance.StageId(), password),
        "ReduceEnterCostType": ParcelType(convert_int(excel_instance.ReduceEnterCostType(), password)).name,
        "ReduceEnterCostId": convert_int(excel_instance.ReduceEnterCostId(), password),
        "ReduceAmount": convert_int(excel_instance.ReduceAmount(), password),
    }

def dump_ContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "SpoilerPopupTitle": convert_string(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_string(excel_instance.SpoilerPopupDescription(), password),
        "IsWarningPopUp": bool(excel_instance.IsWarningPopUp()),
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_ContentsScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.Id(), password),
        "LocalizeId": convert_uint(excel_instance.LocalizeId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ScenarioContentType": ScenarioContentType(convert_int(excel_instance.ScenarioContentType(), password)).name,
        "ScenarioGroupIdLength": convert_int(excel_instance.ScenarioGroupIdLength(), password),
    }

def dump_ContentsShortcutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ScenarioModeVolume": convert_int(excel_instance.ScenarioModeVolume(), password),
        "ScenarioModeChapter": convert_int(excel_instance.ScenarioModeChapter(), password),
        "ShortcutOpenTime": convert_string(excel_instance.ShortcutOpenTime(), password),
        "ShortcutCloseTime": convert_string(excel_instance.ShortcutCloseTime(), password),
        "ConditionContentId": convert_int(excel_instance.ConditionContentId(), password),
        "ConquestMapDifficulty": StageDifficulty(convert_int(excel_instance.ConquestMapDifficulty(), password)).name,
        "ConquestStepIndex": convert_int(excel_instance.ConquestStepIndex(), password),
        "ShortcutContentId": convert_int(excel_instance.ShortcutContentId(), password),
        "ShortcutUINameLength": convert_int(excel_instance.ShortcutUINameLength(), password),
        "Localize": convert_string(excel_instance.Localize(), password),
    }

def dump_CurrencyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CurrencyType": CurrencyTypes(convert_int(excel_instance.CurrencyType(), password)).name,
        "CurrencyName": convert_string(excel_instance.CurrencyName(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "AutoChargeMsc": convert_int(excel_instance.AutoChargeMsc(), password),
        "AutoChargeAmount": convert_int(excel_instance.AutoChargeAmount(), password),
        "CurrencyOverChargeType": CurrencyOverChargeType(convert_int(excel_instance.CurrencyOverChargeType(), password)).name,
        "CurrencyAdditionalChargeType": CurrencyAdditionalChargeType(convert_int(excel_instance.CurrencyAdditionalChargeType(), password)).name,
        "ChargeLimit": convert_int(excel_instance.ChargeLimit(), password),
        "OverChargeLimit": convert_int(excel_instance.OverChargeLimit(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "DailyRefillType": DailyRefillType(convert_int(excel_instance.DailyRefillType(), password)).name,
        "DailyRefillAmount": convert_int(excel_instance.DailyRefillAmount(), password),
        "DailyRefillTimeLength": convert_int(excel_instance.DailyRefillTimeLength(), password),
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTime(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateIn(), password),
        "ExpiryChangeParcelType": ParcelType(convert_int(excel_instance.ExpiryChangeParcelType(), password)).name,
        "ExpiryChangeId": convert_int(excel_instance.ExpiryChangeId(), password),
        "ExpiryChangeAmount": convert_int(excel_instance.ExpiryChangeAmount(), password),
    }

def dump_EmblemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Category": EmblemCategory(convert_int(excel_instance.Category(), password)).name,
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "UseAtLocalizeId": convert_int(excel_instance.UseAtLocalizeId(), password),
        "EmblemTextVisible": bool(excel_instance.EmblemTextVisible()),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "EmblemIconPath": convert_string(excel_instance.EmblemIconPath(), password),
        "EmblemIconNumControl": convert_int(excel_instance.EmblemIconNumControl(), password),
        "EmblemIconBGPath": convert_string(excel_instance.EmblemIconBGPath(), password),
        "EmblemBGPathJp": convert_string(excel_instance.EmblemBGPathJp(), password),
        "EmblemBGPathKr": convert_string(excel_instance.EmblemBGPathKr(), password),
        "DisplayType": EmblemDisplayType(convert_int(excel_instance.DisplayType(), password)).name,
        "DisplayStartDate": convert_string(excel_instance.DisplayStartDate(), password),
        "DisplayEndDate": convert_string(excel_instance.DisplayEndDate(), password),
        "DislpayFavorLevel": convert_int(excel_instance.DislpayFavorLevel(), password),
        "CheckPassType": EmblemCheckPassType(convert_int(excel_instance.CheckPassType(), password)).name,
        "EmblemParameter": convert_int(excel_instance.EmblemParameter(), password),
        "CheckPassCount": convert_int(excel_instance.CheckPassCount(), password),
    }

def dump_EventContentNotifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "EventNotifyType": EventNotifyType(convert_int(excel_instance.EventNotifyType(), password)).name,
        "EventTargetType": EventTargetType(convert_int(excel_instance.EventTargetType(), password)).name,
        "ShortcutEventTargetType": EventTargetType(convert_int(excel_instance.ShortcutEventTargetType(), password)).name,
        "IsShortcutEnable": bool(excel_instance.IsShortcutEnable()),
    }

def dump_EventContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "SpoilerPopupTitle": convert_string(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_string(excel_instance.SpoilerPopupDescription(), password),
        "IsWarningPopUp": bool(excel_instance.IsWarningPopUp()),
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_EventContentTreasureCellRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeID(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_EventContentTreasureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TitleLocalize": convert_string(excel_instance.TitleLocalize(), password),
        "LoopRound": convert_int(excel_instance.LoopRound(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabName(), password),
        "TreasureBGImagePath": convert_string(excel_instance.TreasureBGImagePath(), password),
    }

def dump_EventContentTreasureRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeID(), password),
        "CellUnderImageWidth": convert_int(excel_instance.CellUnderImageWidth(), password),
        "CellUnderImageHeight": convert_int(excel_instance.CellUnderImageHeight(), password),
        "HiddenImage": bool(excel_instance.HiddenImage()),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
        "CellUnderImagePath": convert_string(excel_instance.CellUnderImagePath(), password),
        "TreasureSmallImagePath": convert_string(excel_instance.TreasureSmallImagePath(), password),
        "TreasureSizeIconPath": convert_string(excel_instance.TreasureSizeIconPath(), password),
    }

def dump_EventContentTreasureRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TreasureRound": convert_int(excel_instance.TreasureRound(), password),
        "TreasureRoundSizeLength": convert_int(excel_instance.TreasureRoundSizeLength(), password),
        "CellVisualSortUnstructed": bool(excel_instance.CellVisualSortUnstructed()),
        "CellCheckGoodsId": convert_int(excel_instance.CellCheckGoodsId(), password),
        "CellRewardId": convert_int(excel_instance.CellRewardId(), password),
        "RewardIDLength": convert_int(excel_instance.RewardIDLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
        "TreasureCellImagePath": convert_string(excel_instance.TreasureCellImagePath(), password),
    }

def dump_FarmingDungeonLocationManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FarmingDungeonLocationId": convert_int(excel_instance.FarmingDungeonLocationId(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "WeekDungeonType": convert_float(excel_instance.WeekDungeonType(), password),
        "SchoolDungeonType": SchoolDungeonType(convert_int(excel_instance.SchoolDungeonType(), password)).name,
        "Order": convert_int(excel_instance.Order(), password),
        "OpenStartDateTime": convert_string(excel_instance.OpenStartDateTime(), password),
        "OpenEndDateTime": convert_string(excel_instance.OpenEndDateTime(), password),
        "LocationButtonImagePath": convert_string(excel_instance.LocationButtonImagePath(), password),
        "LocalizeCodeTitle": convert_uint(excel_instance.LocalizeCodeTitle(), password),
        "LocalizeCodeInfo": convert_uint(excel_instance.LocalizeCodeInfo(), password),
    }

def dump_FavorLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "ExpTypeLength": convert_int(excel_instance.ExpTypeLength(), password),
    }

def dump_FavorLevelRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "FavorLevel": convert_int(excel_instance.FavorLevel(), password),
        "StatTypeLength": convert_int(excel_instance.StatTypeLength(), password),
        "StatValueLength": convert_int(excel_instance.StatValueLength(), password),
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardAmountLength": convert_int(excel_instance.RewardAmountLength(), password),
    }

def dump_FixedEchelonSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FixedEchelonID": convert_int(excel_instance.FixedEchelonID(), password),
        "EchelonSceneSkip": bool(excel_instance.EchelonSceneSkip()),
        "MainLeaderSlot": convert_int(excel_instance.MainLeaderSlot(), password),
        "MainCharacterIDLength": convert_int(excel_instance.MainCharacterIDLength(), password),
        "MainLevelLength": convert_int(excel_instance.MainLevelLength(), password),
        "MainGradeLength": convert_int(excel_instance.MainGradeLength(), password),
        "MainExSkillLevelLength": convert_int(excel_instance.MainExSkillLevelLength(), password),
        "MainNoneExSkillLevelLength": convert_int(excel_instance.MainNoneExSkillLevelLength(), password),
        "MainEquipment1TierLength": convert_int(excel_instance.MainEquipment1TierLength(), password),
        "MainEquipment1LevelLength": convert_int(excel_instance.MainEquipment1LevelLength(), password),
        "MainEquipment2TierLength": convert_int(excel_instance.MainEquipment2TierLength(), password),
        "MainEquipment2LevelLength": convert_int(excel_instance.MainEquipment2LevelLength(), password),
        "MainEquipment3TierLength": convert_int(excel_instance.MainEquipment3TierLength(), password),
        "MainEquipment3LevelLength": convert_int(excel_instance.MainEquipment3LevelLength(), password),
        "MainCharacterWeaponGradeLength": convert_int(excel_instance.MainCharacterWeaponGradeLength(), password),
        "MainCharacterWeaponLevelLength": convert_int(excel_instance.MainCharacterWeaponLevelLength(), password),
        "MainCharacterGearTierLength": convert_int(excel_instance.MainCharacterGearTierLength(), password),
        "MainCharacterGearLevelLength": convert_int(excel_instance.MainCharacterGearLevelLength(), password),
        "SupportCharacterIDLength": convert_int(excel_instance.SupportCharacterIDLength(), password),
        "SupportLevelLength": convert_int(excel_instance.SupportLevelLength(), password),
        "SupportGradeLength": convert_int(excel_instance.SupportGradeLength(), password),
        "SupportExSkillLevelLength": convert_int(excel_instance.SupportExSkillLevelLength(), password),
        "SupportNoneExSkillLevelLength": convert_int(excel_instance.SupportNoneExSkillLevelLength(), password),
        "SupportEquipment1TierLength": convert_int(excel_instance.SupportEquipment1TierLength(), password),
        "SupportEquipment1LevelLength": convert_int(excel_instance.SupportEquipment1LevelLength(), password),
        "SupportEquipment2TierLength": convert_int(excel_instance.SupportEquipment2TierLength(), password),
        "SupportEquipment2LevelLength": convert_int(excel_instance.SupportEquipment2LevelLength(), password),
        "SupportEquipment3TierLength": convert_int(excel_instance.SupportEquipment3TierLength(), password),
        "SupportEquipment3LevelLength": convert_int(excel_instance.SupportEquipment3LevelLength(), password),
        "SupportCharacterWeaponGradeLength": convert_int(excel_instance.SupportCharacterWeaponGradeLength(), password),
        "SupportCharacterWeaponLevelLength": convert_int(excel_instance.SupportCharacterWeaponLevelLength(), password),
        "SupportCharacterGearTierLength": convert_int(excel_instance.SupportCharacterGearTierLength(), password),
        "SupportCharacterGearLevelLength": convert_int(excel_instance.SupportCharacterGearLevelLength(), password),
        "InteractionTSCharacterId": convert_int(excel_instance.InteractionTSCharacterId(), password),
    }

def dump_FormationLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupID": convert_int(excel_instance.GroupID(), password),
        "SlotZLength": convert_int(excel_instance.SlotZLength(), password),
        "SlotXLength": convert_int(excel_instance.SlotXLength(), password),
    }

def dump_GroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StageFileNameLength": convert_int(excel_instance.StageFileNameLength(), password),
        "GroundSceneName": convert_string(excel_instance.GroundSceneName(), password),
        "FormationGroupId": convert_int(excel_instance.FormationGroupId(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "EnemyBulletType": BulletType(convert_int(excel_instance.EnemyBulletType(), password)).name,
        "EnemyArmorType": ArmorType(convert_int(excel_instance.EnemyArmorType(), password)).name,
        "LevelNPC": convert_int(excel_instance.LevelNPC(), password),
        "LevelMinion": convert_int(excel_instance.LevelMinion(), password),
        "LevelElite": convert_int(excel_instance.LevelElite(), password),
        "LevelChampion": convert_int(excel_instance.LevelChampion(), password),
        "LevelBoss": convert_int(excel_instance.LevelBoss(), password),
        "ObstacleLevel": convert_int(excel_instance.ObstacleLevel(), password),
        "GradeNPC": convert_int(excel_instance.GradeNPC(), password),
        "GradeMinion": convert_int(excel_instance.GradeMinion(), password),
        "GradeElite": convert_int(excel_instance.GradeElite(), password),
        "GradeChampion": convert_int(excel_instance.GradeChampion(), password),
        "GradeBoss": convert_int(excel_instance.GradeBoss(), password),
        "PlayerSightPointAdd": convert_int(excel_instance.PlayerSightPointAdd(), password),
        "PlayerSightPointRate": convert_int(excel_instance.PlayerSightPointRate(), password),
        "PlayerAttackRangeAdd": convert_int(excel_instance.PlayerAttackRangeAdd(), password),
        "PlayerAttackRangeRate": convert_int(excel_instance.PlayerAttackRangeRate(), password),
        "EnemySightPointAdd": convert_int(excel_instance.EnemySightPointAdd(), password),
        "EnemySightPointRate": convert_int(excel_instance.EnemySightPointRate(), password),
        "EnemyAttackRangeAdd": convert_int(excel_instance.EnemyAttackRangeAdd(), password),
        "EnemyAttackRangeRate": convert_int(excel_instance.EnemyAttackRangeRate(), password),
        "PlayerSkillRangeAdd": convert_int(excel_instance.PlayerSkillRangeAdd(), password),
        "PlayerSkillRangeRate": convert_int(excel_instance.PlayerSkillRangeRate(), password),
        "EnemySkillRangeAdd": convert_int(excel_instance.EnemySkillRangeAdd(), password),
        "EnemySkillRangeRate": convert_int(excel_instance.EnemySkillRangeRate(), password),
        "PlayerMinimumPositionGapRate": convert_int(excel_instance.PlayerMinimumPositionGapRate(), password),
        "EnemyMinimumPositionGapRate": convert_int(excel_instance.EnemyMinimumPositionGapRate(), password),
        "PlayerSightRangeMax": bool(excel_instance.PlayerSightRangeMax()),
        "EnemySightRangeMax": bool(excel_instance.EnemySightRangeMax()),
        "TSSAirUnitHeight": convert_int(excel_instance.TSSAirUnitHeight(), password),
        "IsPhaseBGM": bool(excel_instance.IsPhaseBGM()),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "WarningUI": bool(excel_instance.WarningUI()),
        "TSSHatchOpen": bool(excel_instance.TSSHatchOpen()),
        "ForcedTacticSpeed": TacticSpeed(convert_int(excel_instance.ForcedTacticSpeed(), password)).name,
        "ForcedSkillUse": TacticSkillUse(convert_int(excel_instance.ForcedSkillUse(), password)).name,
        "ShowNPCSkillCutIn": ShowSkillCutIn(convert_int(excel_instance.ShowNPCSkillCutIn(), password)).name,
        "ImmuneHitBeforeTimeOutEnd": bool(excel_instance.ImmuneHitBeforeTimeOutEnd()),
        "UIBattleHideFromScratch": bool(excel_instance.UIBattleHideFromScratch()),
        "BattleReadyTimelinePath": convert_string(excel_instance.BattleReadyTimelinePath(), password),
        "BeforeVictoryTimelinePath": convert_string(excel_instance.BeforeVictoryTimelinePath(), password),
        "SkipBattleEnd": bool(excel_instance.SkipBattleEnd()),
        "HideNPCWhenBattleEnd": bool(excel_instance.HideNPCWhenBattleEnd()),
        "CoverPointOff": bool(excel_instance.CoverPointOff()),
        "UIHpScale": convert_float(excel_instance.UIHpScale(), password),
        "UIEmojiScale": convert_float(excel_instance.UIEmojiScale(), password),
        "UISkillMainLogScale": convert_float(excel_instance.UISkillMainLogScale(), password),
        "AllyPassiveSkillIdLength": convert_int(excel_instance.AllyPassiveSkillIdLength(), password),
        "AllyPassiveSkillLevelLength": convert_int(excel_instance.AllyPassiveSkillLevelLength(), password),
        "EnemyPassiveSkillIdLength": convert_int(excel_instance.EnemyPassiveSkillIdLength(), password),
        "EnemyPassiveSkillLevelLength": convert_int(excel_instance.EnemyPassiveSkillLevelLength(), password),
    }

def dump_GroundModuleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_uint(excel_instance.GroupId(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPath(), password),
    }

def dump_IdCardBackgroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Rarity": Rarity(convert_int(excel_instance.Rarity(), password)).name,
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "IsDefault": bool(excel_instance.IsDefault()),
        "BgPath": convert_string(excel_instance.BgPath(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
    }

def dump_InformationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupID": convert_int(excel_instance.GroupID(), password),
        "PageName": convert_string(excel_instance.PageName(), password),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeId(), password),
        "TutorialParentNameLength": convert_int(excel_instance.TutorialParentNameLength(), password),
        "UINameLength": convert_int(excel_instance.UINameLength(), password),
    }

def dump_LoadingImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
        "DisplayWeight": convert_int(excel_instance.DisplayWeight(), password),
    }

def dump_LocalizeCharProfileChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "ChangeCharacterID": convert_int(excel_instance.ChangeCharacterID(), password),
    }

def dump_LocalizeCodeInBuildExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeErrorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "ErrorLevel": WebAPIErrorLevel(convert_int(excel_instance.ErrorLevel(), password)).name,
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeEtcExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKr(), password),
        "NameJp": convert_string(excel_instance.NameJp(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJp(), password),
    }

def dump_LocalizeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
    }

def dump_LocalizeSkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKr(), password),
        "SkillInvokeLocalizeKr": convert_string(excel_instance.SkillInvokeLocalizeKr(), password),
        "NameJp": convert_string(excel_instance.NameJp(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJp(), password),
        "SkillInvokeLocalizeJp": convert_string(excel_instance.SkillInvokeLocalizeJp(), password),
    }

def dump_MemoryLobbyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "MemoryLobbyCategory": MemoryLobbyCategory(convert_int(excel_instance.MemoryLobbyCategory(), password)).name,
        "SlotTextureName": convert_string(excel_instance.SlotTextureName(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureName(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "AudioClipJp": convert_string(excel_instance.AudioClipJp(), password),
        "AudioClipKr": convert_string(excel_instance.AudioClipKr(), password),
    }

def dump_MessagePopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringId": convert_uint(excel_instance.StringId(), password),
        "MessagePopupLayout": MessagePopupLayout(convert_int(excel_instance.MessagePopupLayout(), password)).name,
        "OrderType": MessagePopupImagePositionType(convert_int(excel_instance.OrderType(), password)).name,
        "Image": convert_string(excel_instance.Image(), password),
        "TitleText": convert_uint(excel_instance.TitleText(), password),
        "SubTitleText": convert_uint(excel_instance.SubTitleText(), password),
        "MessageText": convert_uint(excel_instance.MessageText(), password),
        "ConditionTextLength": convert_int(excel_instance.ConditionTextLength(), password),
        "DisplayXButton": bool(excel_instance.DisplayXButton()),
        "ButtonLength": convert_int(excel_instance.ButtonLength(), password),
        "ButtonTextLength": convert_int(excel_instance.ButtonTextLength(), password),
        "ButtonCommandLength": convert_int(excel_instance.ButtonCommandLength(), password),
        "ButtonParameterLength": convert_int(excel_instance.ButtonParameterLength(), password),
    }

def dump_MiniGameDefenseCharacterBanExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
    }

def dump_MiniGameDefenseFixedStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MinigameDefenseFixedStatId": convert_int(excel_instance.MinigameDefenseFixedStatId(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "Grade": convert_int(excel_instance.Grade(), password),
        "ExSkillLevel": convert_int(excel_instance.ExSkillLevel(), password),
        "NoneExSkillLevel": convert_int(excel_instance.NoneExSkillLevel(), password),
        "Equipment1Tier": convert_int(excel_instance.Equipment1Tier(), password),
        "Equipment1Level": convert_int(excel_instance.Equipment1Level(), password),
        "Equipment2Tier": convert_int(excel_instance.Equipment2Tier(), password),
        "Equipment2Level": convert_int(excel_instance.Equipment2Level(), password),
        "Equipment3Tier": convert_int(excel_instance.Equipment3Tier(), password),
        "Equipment3Level": convert_int(excel_instance.Equipment3Level(), password),
        "CharacterWeaponGrade": convert_int(excel_instance.CharacterWeaponGrade(), password),
        "CharacterWeaponLevel": convert_int(excel_instance.CharacterWeaponLevel(), password),
        "CharacterGearTier": convert_int(excel_instance.CharacterGearTier(), password),
        "CharacterGearLevel": convert_int(excel_instance.CharacterGearLevel(), password),
    }

def dump_MiniGameDefenseInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DefenseBattleParcelType": ParcelType(convert_int(excel_instance.DefenseBattleParcelType(), password)).name,
        "DefenseBattleParcelId": convert_int(excel_instance.DefenseBattleParcelId(), password),
        "DefenseBattleMultiplierMax": convert_int(excel_instance.DefenseBattleMultiplierMax(), password),
        "DisableRootMotion": bool(excel_instance.DisableRootMotion()),
    }

def dump_MiniGameDefenseStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "StageDifficulty": StageDifficulty(convert_int(excel_instance.StageDifficulty(), password)).name,
        "StageDifficultyLocalize": convert_uint(excel_instance.StageDifficultyLocalize(), password),
        "StageNumber": convert_int(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": ParcelType(convert_int(excel_instance.StageEnterCostType(), password)).name,
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardId(), password),
        "EnterScenarioGroupIdLength": convert_int(excel_instance.EnterScenarioGroupIdLength(), password),
        "ClearScenarioGroupIdLength": convert_int(excel_instance.ClearScenarioGroupIdLength(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "StarGoalLength": convert_int(excel_instance.StarGoalLength(), password),
        "StarGoalAmountLength": convert_int(excel_instance.StarGoalAmountLength(), password),
        "DefenseFormationBGPrefab": convert_string(excel_instance.DefenseFormationBGPrefab(), password),
        "DefenseFormationBGPrefabScale": convert_float(excel_instance.DefenseFormationBGPrefabScale(), password),
        "FixedEchelon": convert_int(excel_instance.FixedEchelon(), password),
        "MininageDefenseFixedStatId": convert_int(excel_instance.MininageDefenseFixedStatId(), password),
        "StageHint": convert_uint(excel_instance.StageHint(), password),
    }

def dump_MiniGameDreamCollectionScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "IsSkip": bool(excel_instance.IsSkip()),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ParameterLength": convert_int(excel_instance.ParameterLength(), password),
        "ParameterAmountLength": convert_int(excel_instance.ParameterAmountLength(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
    }

def dump_MiniGameDreamDailyPointExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TotalParameterMin": convert_int(excel_instance.TotalParameterMin(), password),
        "TotalParameterMax": convert_int(excel_instance.TotalParameterMax(), password),
        "DailyPointCoefficient": convert_int(excel_instance.DailyPointCoefficient(), password),
        "DailyPointCorrectionValue": convert_int(excel_instance.DailyPointCorrectionValue(), password),
    }

def dump_MiniGameDreamEndingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EndingId": convert_int(excel_instance.EndingId(), password),
        "DreamMakerEndingType": DreamMakerEndingType(convert_int(excel_instance.DreamMakerEndingType(), password)).name,
        "Order": convert_int(excel_instance.Order(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
        "EndingConditionLength": convert_int(excel_instance.EndingConditionLength(), password),
        "EndingConditionValueLength": convert_int(excel_instance.EndingConditionValueLength(), password),
    }

def dump_MiniGameDreamEndingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EndingId": convert_int(excel_instance.EndingId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "DreamMakerEndingRewardType": DreamMakerEndingRewardType(convert_int(excel_instance.DreamMakerEndingRewardType(), password)).name,
        "DreamMakerEndingType": DreamMakerEndingType(convert_int(excel_instance.DreamMakerEndingType(), password)).name,
        "RewardParcelTypeLength": convert_int(excel_instance.RewardParcelTypeLength(), password),
        "RewardParcelIdLength": convert_int(excel_instance.RewardParcelIdLength(), password),
        "RewardParcelAmountLength": convert_int(excel_instance.RewardParcelAmountLength(), password),
    }

def dump_MiniGameDreamInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DreamMakerMultiplierCondition": DreamMakerMultiplierCondition(convert_int(excel_instance.DreamMakerMultiplierCondition(), password)).name,
        "DreamMakerMultiplierConditionValue": convert_int(excel_instance.DreamMakerMultiplierConditionValue(), password),
        "DreamMakerMultiplierMax": convert_int(excel_instance.DreamMakerMultiplierMax(), password),
        "DreamMakerDays": convert_int(excel_instance.DreamMakerDays(), password),
        "DreamMakerActionPoint": convert_int(excel_instance.DreamMakerActionPoint(), password),
        "DreamMakerParcelType": ParcelType(convert_int(excel_instance.DreamMakerParcelType(), password)).name,
        "DreamMakerParcelId": convert_int(excel_instance.DreamMakerParcelId(), password),
        "DreamMakerDailyPointParcelType": ParcelType(convert_int(excel_instance.DreamMakerDailyPointParcelType(), password)).name,
        "DreamMakerDailyPointId": convert_int(excel_instance.DreamMakerDailyPointId(), password),
        "DreamMakerParameterTransfer": convert_int(excel_instance.DreamMakerParameterTransfer(), password),
        "ScheduleCostGoodsId": convert_int(excel_instance.ScheduleCostGoodsId(), password),
        "LobbyBGMChangeScenarioId": convert_int(excel_instance.LobbyBGMChangeScenarioId(), password),
    }

def dump_MiniGameDreamParameterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ParameterType": DreamMakerParameterType(convert_int(excel_instance.ParameterType(), password)).name,
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "ParameterBase": convert_int(excel_instance.ParameterBase(), password),
        "ParameterBaseMax": convert_int(excel_instance.ParameterBaseMax(), password),
        "ParameterMin": convert_int(excel_instance.ParameterMin(), password),
        "ParameterMax": convert_int(excel_instance.ParameterMax(), password),
    }

def dump_MiniGameDreamReplayScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "ReplaySummaryTitleLocalize": convert_uint(excel_instance.ReplaySummaryTitleLocalize(), password),
        "ReplaySummaryLocalizeScenarioId": convert_uint(excel_instance.ReplaySummaryLocalizeScenarioId(), password),
        "ReplayScenarioResource": convert_string(excel_instance.ReplayScenarioResource(), password),
        "IsReplayScenarioHorizon": bool(excel_instance.IsReplayScenarioHorizon()),
    }

def dump_MiniGameDreamScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DreamMakerScheduleGroupId": convert_int(excel_instance.DreamMakerScheduleGroupId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "LoadingResource01": convert_string(excel_instance.LoadingResource01(), password),
        "LoadingResource02": convert_string(excel_instance.LoadingResource02(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
    }

def dump_MiniGameDreamScheduleResultExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DreamMakerResult": DreamMakerResult(convert_int(excel_instance.DreamMakerResult(), password)).name,
        "DreamMakerScheduleGroup": convert_int(excel_instance.DreamMakerScheduleGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "RewardParameterLength": convert_int(excel_instance.RewardParameterLength(), password),
        "RewardParameterOperationTypeLength": convert_int(excel_instance.RewardParameterOperationTypeLength(), password),
        "RewardParameterAmountLength": convert_int(excel_instance.RewardParameterAmountLength(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_MiniGameDreamTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DreamMakerDays": convert_int(excel_instance.DreamMakerDays(), password),
        "DreamMakerActionPoint": convert_int(excel_instance.DreamMakerActionPoint(), password),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupId(), password),
        "Bgm": convert_int(excel_instance.Bgm(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPath(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPath(), password),
    }

def dump_MinigameDreamVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "VoiceCondition": DreamMakerVoiceCondition(convert_int(excel_instance.VoiceCondition(), password)).name,
        "VoiceClip": convert_uint(excel_instance.VoiceClip(), password),
    }

def dump_MissionEmergencyCompleteExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MissionId": convert_int(excel_instance.MissionId(), password),
        "EmergencyComplete": bool(excel_instance.EmergencyComplete()),
    }

def dump_MultiFloorRaidRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": ParcelType(convert_int(excel_instance.ClearStageRewardParcelType(), password)).name,
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_MultiFloorRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "LobbyEnterScenario": convert_uint(excel_instance.LobbyEnterScenario(), password),
        "ShowLobbyBanner": bool(excel_instance.ShowLobbyBanner()),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDate(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDate(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "OpenRaidBossGroupId": convert_string(excel_instance.OpenRaidBossGroupId(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "LobbyImgPath": convert_string(excel_instance.LobbyImgPath(), password),
        "LevelImgPath": convert_string(excel_instance.LevelImgPath(), password),
        "PlayTip": convert_string(excel_instance.PlayTip(), password),
    }

def dump_MultiFloorRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "BossGroupId": convert_string(excel_instance.BossGroupId(), password),
        "AssistSlot": convert_int(excel_instance.AssistSlot(), password),
        "StageOpenCondition": convert_int(excel_instance.StageOpenCondition(), password),
        "FloorListSection": bool(excel_instance.FloorListSection()),
        "FloorListSectionOpenCondition": convert_int(excel_instance.FloorListSectionOpenCondition(), password),
        "FloorListSectionLabel": convert_uint(excel_instance.FloorListSectionLabel(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndex()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSync()),
        "FloorListImgPath": convert_string(excel_instance.FloorListImgPath(), password),
        "FloorImgPath": convert_string(excel_instance.FloorImgPath(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterId(), password),
        "BossCharacterIdLength": convert_int(excel_instance.BossCharacterIdLength(), password),
        "StatChangeIdLength": convert_int(excel_instance.StatChangeIdLength(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevel(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "BattleReadyTimelinePathLength": convert_int(excel_instance.BattleReadyTimelinePathLength(), password),
        "BattleReadyTimelinePhaseStartLength": convert_int(excel_instance.BattleReadyTimelinePhaseStartLength(), password),
        "BattleReadyTimelinePhaseEndLength": convert_int(excel_instance.BattleReadyTimelinePhaseEndLength(), password),
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
    }

def dump_MultiFloorRaidStatChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StatChangeId": convert_int(excel_instance.StatChangeId(), password),
        "StatTypeLength": convert_int(excel_instance.StatTypeLength(), password),
        "StatAddLength": convert_int(excel_instance.StatAddLength(), password),
        "StatMultiplyLength": convert_int(excel_instance.StatMultiplyLength(), password),
        "ApplyCharacterIdLength": convert_int(excel_instance.ApplyCharacterIdLength(), password),
    }

def dump_ObstacleStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringID(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "MaxHP1": convert_int(excel_instance.MaxHP1(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100(), password),
        "BlockRate": convert_int(excel_instance.BlockRate(), password),
        "Dodge": convert_int(excel_instance.Dodge(), password),
        "CanNotStandRange": convert_int(excel_instance.CanNotStandRange(), password),
        "HighlightFloaterHeight": convert_float(excel_instance.HighlightFloaterHeight(), password),
        "EnhanceLightArmorRate": convert_int(excel_instance.EnhanceLightArmorRate(), password),
        "EnhanceHeavyArmorRate": convert_int(excel_instance.EnhanceHeavyArmorRate(), password),
        "EnhanceUnarmedRate": convert_int(excel_instance.EnhanceUnarmedRate(), password),
        "EnhanceElasticArmorRate": convert_int(excel_instance.EnhanceElasticArmorRate(), password),
        "EnhanceStructureRate": convert_int(excel_instance.EnhanceStructureRate(), password),
        "EnhanceNormalArmorRate": convert_int(excel_instance.EnhanceNormalArmorRate(), password),
        "ReduceExDamagedRate": convert_int(excel_instance.ReduceExDamagedRate(), password),
    }

def dump_OpenConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OpenConditionContentType": OpenConditionContent(convert_int(excel_instance.OpenConditionContentType(), password)).name,
        "LockUILength": convert_int(excel_instance.LockUILength(), password),
        "ShortcutPopupPriority": convert_int(excel_instance.ShortcutPopupPriority(), password),
        "ShortcutUINameLength": convert_int(excel_instance.ShortcutUINameLength(), password),
        "ShortcutParam": convert_int(excel_instance.ShortcutParam(), password),
        "Scene": convert_string(excel_instance.Scene(), password),
        "HideWhenLocked": bool(excel_instance.HideWhenLocked()),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "CampaignStageId": convert_int(excel_instance.CampaignStageId(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "OpenDayOfWeek": WeekDay(convert_int(excel_instance.OpenDayOfWeek(), password)).name,
        "OpenHour": convert_int(excel_instance.OpenHour(), password),
        "CloseDayOfWeek": WeekDay(convert_int(excel_instance.CloseDayOfWeek(), password)).name,
        "CloseHour": convert_int(excel_instance.CloseHour(), password),
        "OpenedCafeId": convert_int(excel_instance.OpenedCafeId(), password),
        "CafeIdforCafeRank": convert_int(excel_instance.CafeIdforCafeRank(), password),
        "CafeRank": convert_int(excel_instance.CafeRank(), password),
        "ContentsOpenShow": bool(excel_instance.ContentsOpenShow()),
        "ContentsOpenShortcutUI": convert_string(excel_instance.ContentsOpenShortcutUI(), password),
    }

def dump_OperatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "OperatorCondition": OperatorCondition(convert_int(excel_instance.OperatorCondition(), password)).name,
        "OutputSequence": convert_int(excel_instance.OutputSequence(), password),
        "RandomWeight": convert_int(excel_instance.RandomWeight(), password),
        "OutputDelay": convert_int(excel_instance.OutputDelay(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "OperatorOutputPriority": convert_int(excel_instance.OperatorOutputPriority(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "TextLocalizeKey": convert_string(excel_instance.TextLocalizeKey(), password),
        "VoiceIdLength": convert_int(excel_instance.VoiceIdLength(), password),
        "OperatorWaitQueue": bool(excel_instance.OperatorWaitQueue()),
    }

def dump_ScenarioBGEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "Effect": convert_string(excel_instance.Effect(), password),
        "Effect2": convert_string(excel_instance.Effect2(), password),
        "Scroll": ScenarioBGScroll(convert_int(excel_instance.Scroll(), password)).name,
        "ScrollTime": convert_int(excel_instance.ScrollTime(), password),
        "ScrollFrom": convert_int(excel_instance.ScrollFrom(), password),
        "ScrollTo": convert_int(excel_instance.ScrollTo(), password),
    }

def dump_ScenarioBGNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "BGFileName": convert_string(excel_instance.BGFileName(), password),
        "BGType": ScenarioBGType(convert_int(excel_instance.BGType(), password)).name,
        "AnimationRoot": convert_string(excel_instance.AnimationRoot(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "SpineScale": convert_float(excel_instance.SpineScale(), password),
        "SpineLocalPosX": convert_int(excel_instance.SpineLocalPosX(), password),
        "SpineLocalPosY": convert_int(excel_instance.SpineLocalPosY(), password),
    }

def dump_ScenarioCharacterEmotionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EmoticonName": convert_string(excel_instance.EmoticonName(), password),
        "Name": convert_uint(excel_instance.Name(), password),
    }

def dump_ScenarioCharacterNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterName": convert_uint(excel_instance.CharacterName(), password),
        "ProductionStep": ProductionStep(convert_int(excel_instance.ProductionStep(), password)).name,
        "NameKR": convert_string(excel_instance.NameKR(), password),
        "NicknameKR": convert_string(excel_instance.NicknameKR(), password),
        "NameJP": convert_string(excel_instance.NameJP(), password),
        "NicknameJP": convert_string(excel_instance.NicknameJP(), password),
        "Shape": ScenarioCharacterShapes(convert_int(excel_instance.Shape(), password)).name,
        "SpinePrefabName": convert_string(excel_instance.SpinePrefabName(), password),
        "SmallPortrait": convert_string(excel_instance.SmallPortrait(), password),
    }

def dump_ScenarioCharacterSituationSetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "Face": convert_string(excel_instance.Face(), password),
        "Behavior": convert_string(excel_instance.Behavior(), password),
        "Action": convert_string(excel_instance.Action(), password),
        "Shape": convert_string(excel_instance.Shape(), password),
        "Effect": convert_uint(excel_instance.Effect(), password),
        "Emotion": convert_uint(excel_instance.Emotion(), password),
    }

def dump_ScenarioContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "UnlockConditionType": CollectionUnlockType(convert_int(excel_instance.UnlockConditionType(), password)).name,
        "UnlockConditionParameterLength": convert_int(excel_instance.UnlockConditionParameterLength(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "UnlockConditionCount": convert_int(excel_instance.UnlockConditionCount(), password),
        "IsObject": bool(excel_instance.IsObject()),
        "IsHorizon": bool(excel_instance.IsHorizon()),
        "EmblemResource": convert_string(excel_instance.EmblemResource(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResource(), password),
        "FullResource": convert_string(excel_instance.FullResource(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeId(), password),
    }

def dump_ScenarioEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EffectName": convert_string(excel_instance.EffectName(), password),
        "Name": convert_uint(excel_instance.Name(), password),
    }

def dump_ScenarioModeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_int(excel_instance.ModeId(), password),
        "ModeType": ScenarioModeTypes(convert_int(excel_instance.ModeType(), password)).name,
        "SubType": ScenarioModeSubTypes(convert_int(excel_instance.SubType(), password)).name,
        "VolumeId": convert_int(excel_instance.VolumeId(), password),
        "ChapterId": convert_int(excel_instance.ChapterId(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeId(), password),
        "ExposedTime": convert_string(excel_instance.ExposedTime(), password),
        "Hide": bool(excel_instance.Hide()),
        "Open": bool(excel_instance.Open()),
        "IsContinue": bool(excel_instance.IsContinue()),
        "EpisodeContinueModeId": convert_int(excel_instance.EpisodeContinueModeId(), password),
        "FrontScenarioGroupIdLength": convert_int(excel_instance.FrontScenarioGroupIdLength(), password),
        "StrategyId": convert_int(excel_instance.StrategyId(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattle()),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "BackScenarioGroupIdLength": convert_int(excel_instance.BackScenarioGroupIdLength(), password),
        "ClearedModeIdLength": convert_int(excel_instance.ClearedModeIdLength(), password),
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardId(), password),
        "IsScenarioSpecialReward": bool(excel_instance.IsScenarioSpecialReward()),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimit(), password),
        "ClearedStageId": convert_int(excel_instance.ClearedStageId(), password),
        "NeedClub": Club(convert_int(excel_instance.NeedClub(), password)).name,
        "NeedClubStudentCount": convert_int(excel_instance.NeedClubStudentCount(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentType": EventContentType(convert_int(excel_instance.EventContentType(), password)).name,
        "EventContentCondition": convert_int(excel_instance.EventContentCondition(), password),
        "EventContentConditionGroup": convert_int(excel_instance.EventContentConditionGroup(), password),
        "MapDifficulty": StageDifficulty(convert_int(excel_instance.MapDifficulty(), password)).name,
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevel(), password),
        "EventIconParcelPath": convert_string(excel_instance.EventIconParcelPath(), password),
        "EventBannerTitle": convert_uint(excel_instance.EventBannerTitle(), password),
        "Lof": bool(excel_instance.Lof()),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "CompleteReportEventName": convert_string(excel_instance.CompleteReportEventName(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
        "CollectionGroupId": convert_int(excel_instance.CollectionGroupId(), password),
    }

def dump_ScenarioModeRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_ScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "VideoId": convert_int(excel_instance.VideoId(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "AudioName": convert_string(excel_instance.AudioName(), password),
        "SpinePath": convert_string(excel_instance.SpinePath(), password),
        "Ratio": convert_int(excel_instance.Ratio(), password),
        "LobbyAniPath": convert_string(excel_instance.LobbyAniPath(), password),
        "MovieCGPath": convert_string(excel_instance.MovieCGPath(), password),
        "LocalizeId": convert_uint(excel_instance.LocalizeId(), password),
    }

def dump_ScenarioScriptExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "SelectionGroup": convert_int(excel_instance.SelectionGroup(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "Sound": convert_string(excel_instance.Sound(), password),
        "Transition": convert_uint(excel_instance.Transition(), password),
        "BGName": convert_uint(excel_instance.BGName(), password),
        "BGEffect": convert_uint(excel_instance.BGEffect(), password),
        "PopupFileName": convert_string(excel_instance.PopupFileName(), password),
        "ScriptKr": convert_string(excel_instance.ScriptKr(), password),
        "TextJp": convert_string(excel_instance.TextJp(), password),
        "VoiceId": convert_string(excel_instance.VoiceId(), password),
    }

def dump_ScenarioTransitionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "TransitionOut": convert_string(excel_instance.TransitionOut(), password),
        "TransitionOutDuration": convert_int(excel_instance.TransitionOutDuration(), password),
        "TransitionOutResource": convert_string(excel_instance.TransitionOutResource(), password),
        "TransitionIn": convert_string(excel_instance.TransitionIn(), password),
        "TransitionInDuration": convert_int(excel_instance.TransitionInDuration(), password),
        "TransitionInResource": convert_string(excel_instance.TransitionInResource(), password),
    }

def dump_SchoolDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DungeonType": SchoolDungeonType(convert_int(excel_instance.DungeonType(), password)).name,
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardParcelType": ParcelType(convert_int(excel_instance.RewardParcelType(), password)).name,
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_SchoolDungeonStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageId(), password),
        "DungeonType": SchoolDungeonType(convert_int(excel_instance.DungeonType(), password)).name,
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "StageEnterCostTypeLength": convert_int(excel_instance.StageEnterCostTypeLength(), password),
        "StageEnterCostIdLength": convert_int(excel_instance.StageEnterCostIdLength(), password),
        "StageEnterCostAmountLength": convert_int(excel_instance.StageEnterCostAmountLength(), password),
        "StageEnterCostMinimumAmountLength": convert_int(excel_instance.StageEnterCostMinimumAmountLength(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoalLength": convert_int(excel_instance.StarGoalLength(), password),
        "StarGoalAmountLength": convert_int(excel_instance.StarGoalAmountLength(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "EchelonExtensionType": EchelonExtensionType(convert_int(excel_instance.EchelonExtensionType(), password)).name,
    }

def dump_ServiceActionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ServiceActionType": ServiceActionType(convert_int(excel_instance.ServiceActionType(), password)).name,
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
    }

def dump_ShortcutTypeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "IsAscending": bool(excel_instance.IsAscending()),
        "ContentTypeLength": convert_int(excel_instance.ContentTypeLength(), password),
    }

def dump_SkillAdditionalTooltipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "AdditionalSkillGroupId": convert_string(excel_instance.AdditionalSkillGroupId(), password),
        "ShowSkillSlot": convert_string(excel_instance.ShowSkillSlot(), password),
    }

def dump_SoundUIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "SoundUniqueId": convert_string(excel_instance.SoundUniqueId(), password),
        "Path": convert_string(excel_instance.Path(), password),
    }

def dump_SpineLipsyncExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
        "VoiceStringId": convert_string(excel_instance.VoiceStringId(), password),
        "AnimJson": convert_string(excel_instance.AnimJson(), password),
    }

def dump_StatLevelInterpolationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "StatTypeIndexLength": convert_int(excel_instance.StatTypeIndexLength(), password),
    }

def dump_StickerGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Layout": convert_string(excel_instance.Layout(), password),
        "UniqueLayoutPath": convert_string(excel_instance.UniqueLayoutPath(), password),
        "StickerGroupIconpath": convert_string(excel_instance.StickerGroupIconpath(), password),
        "PageCompleteSlot": convert_int(excel_instance.PageCompleteSlot(), password),
        "PageCompleteRewardParcelType": ParcelType(convert_int(excel_instance.PageCompleteRewardParcelType(), password)).name,
        "PageCompleteRewardParcelId": convert_int(excel_instance.PageCompleteRewardParcelId(), password),
        "PageCompleteRewardAmount": convert_int(excel_instance.PageCompleteRewardAmount(), password),
        "LocalizeTitle": convert_uint(excel_instance.LocalizeTitle(), password),
        "LocalizeDescription": convert_uint(excel_instance.LocalizeDescription(), password),
        "StickerGroupCoverpath": convert_string(excel_instance.StickerGroupCoverpath(), password),
    }

def dump_StickerPageContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StickerGroupId": convert_int(excel_instance.StickerGroupId(), password),
        "StickerPageId": convert_int(excel_instance.StickerPageId(), password),
        "StickerSlot": convert_int(excel_instance.StickerSlot(), password),
        "StickerGetConditionType": StickerGetConditionType(convert_int(excel_instance.StickerGetConditionType(), password)).name,
        "StickerCheckPassType": StickerCheckPassType(convert_int(excel_instance.StickerCheckPassType(), password)).name,
        "GetStickerConditionType": GetStickerConditionType(convert_int(excel_instance.GetStickerConditionType(), password)).name,
        "StickerGetConditionCount": convert_int(excel_instance.StickerGetConditionCount(), password),
        "StickerGetConditionParameterLength": convert_int(excel_instance.StickerGetConditionParameterLength(), password),
        "StickerGetConditionParameterTagLength": convert_int(excel_instance.StickerGetConditionParameterTagLength(), password),
        "PackedStickerIconLocalizeEtcId": convert_uint(excel_instance.PackedStickerIconLocalizeEtcId(), password),
        "PackedStickerIconPath": convert_string(excel_instance.PackedStickerIconPath(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "StickerDetailPath": convert_string(excel_instance.StickerDetailPath(), password),
    }

def dump_StoryStrategyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "Localize": convert_string(excel_instance.Localize(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "WhiteListId": convert_int(excel_instance.WhiteListId(), password),
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": StageTopography(convert_int(excel_instance.StageTopography(), password)).name,
        "StrategyEnvironment": StrategyEnvironment(convert_int(excel_instance.StrategyEnvironment(), password)).name,
        "ContentType": ContentType(convert_int(excel_instance.ContentType(), password)).name,
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventName(), password),
    }

def dump_ToastExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.Id(), password),
        "ToastType": ToastType(convert_int(excel_instance.ToastType(), password)).name,
        "MissionId": convert_uint(excel_instance.MissionId(), password),
        "TextId": convert_uint(excel_instance.TextId(), password),
        "LifeTime": convert_int(excel_instance.LifeTime(), password),
    }

def dump_TutorialCharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TalkId": convert_int(excel_instance.TalkId(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_TutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "CompletionReportEventName": convert_string(excel_instance.CompletionReportEventName(), password),
        "CompulsoryTutorial": bool(excel_instance.CompulsoryTutorial()),
        "DescriptionTutorial": bool(excel_instance.DescriptionTutorial()),
        "TutorialStageId": convert_int(excel_instance.TutorialStageId(), password),
        "UINameLength": convert_int(excel_instance.UINameLength(), password),
        "TutorialParentNameLength": convert_int(excel_instance.TutorialParentNameLength(), password),
    }

def dump_TutorialFailureImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Contents": TutorialFailureContentType(convert_int(excel_instance.Contents(), password)).name,
        "Type": convert_string(excel_instance.Type(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
    }

def dump_UnderCoverStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "StageNameFile": convert_string(excel_instance.StageNameFile(), password),
        "StageTryCount": convert_int(excel_instance.StageTryCount(), password),
        "ApplySkip": bool(excel_instance.ApplySkip()),
        "SkipCount": convert_int(excel_instance.SkipCount(), password),
        "ShowClearScene": bool(excel_instance.ShowClearScene()),
        "StageTips": convert_uint(excel_instance.StageTips(), password),
        "StageName": convert_uint(excel_instance.StageName(), password),
    }

def dump_VideoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "NationLength": convert_int(excel_instance.NationLength(), password),
        "VideoPathLength": convert_int(excel_instance.VideoPathLength(), password),
        "SoundPathLength": convert_int(excel_instance.SoundPathLength(), password),
        "SoundVolumeLength": convert_int(excel_instance.SoundVolumeLength(), password),
    }

def dump_VoiceCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceEvent": VoiceEvent(convert_int(excel_instance.VoiceEvent(), password)).name,
        "Rate": convert_int(excel_instance.Rate(), password),
        "VoiceHashLength": convert_int(excel_instance.VoiceHashLength(), password),
    }

def dump_VoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "NationLength": convert_int(excel_instance.NationLength(), password),
        "PathLength": convert_int(excel_instance.PathLength(), password),
        "VolumeLength": convert_int(excel_instance.VolumeLength(), password),
    }

def dump_VoiceLogicEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LogicEffectNameHash": convert_uint(excel_instance.LogicEffectNameHash(), password),
        "Self": bool(excel_instance.Self()),
        "Priority": convert_int(excel_instance.Priority(), password),
        "VoiceHashLength": convert_int(excel_instance.VoiceHashLength(), password),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_VoiceRoomExceptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "LinkedCharacterVoicePrintType": CVPrintType(convert_int(excel_instance.LinkedCharacterVoicePrintType(), password)).name,
        "LinkedCostumeUniqueId": convert_int(excel_instance.LinkedCostumeUniqueId(), password),
    }

def dump_VoiceSpineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "NationLength": convert_int(excel_instance.NationLength(), password),
        "PathLength": convert_int(excel_instance.PathLength(), password),
        "SoundVolumeLength": convert_int(excel_instance.SoundVolumeLength(), password),
    }

def dump_VoiceTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "NationLength": convert_int(excel_instance.NationLength(), password),
        "PathLength": convert_int(excel_instance.PathLength(), password),
        "SoundVolumeLength": convert_int(excel_instance.SoundVolumeLength(), password),
    }

def dump_WorldRaidConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LockUILength": convert_int(excel_instance.LockUILength(), password),
        "HideWhenLocked": bool(excel_instance.HideWhenLocked()),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ScenarioModeIdLength": convert_int(excel_instance.ScenarioModeIdLength(), password),
        "CampaignStageIDLength": convert_int(excel_instance.CampaignStageIDLength(), password),
        "MultipleConditionCheckType": MultipleConditionCheckType(convert_int(excel_instance.MultipleConditionCheckType(), password)).name,
        "AfterWhenDate": convert_string(excel_instance.AfterWhenDate(), password),
        "WorldRaidBossKillLength": convert_int(excel_instance.WorldRaidBossKillLength(), password),
    }

def dump_AcademyFavorScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyFavorScheduleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyLocationRankExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyLocationRankExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessanger1ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessanger1Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessanger2ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessanger2Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessanger3ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessanger3Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyMessangerExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyMessangerExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyTicketExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyTicketExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AcademyZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AcademyZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AddressableBlackListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AddressableBlackListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AddressableWhiteListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AddressableWhiteListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaLevelSectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaLevelSectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaNPCExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaNPCExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaSeasonCloseRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaSeasonCloseRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ArenaSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ArenaSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattleLevelFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattleLevelFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BossExternalBTExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BossExternalBTExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BossPhaseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BossPhaseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BuffParticleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BuffParticleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BulletArmorDamageFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BulletArmorDamageFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeInteractionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeProductionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeProductionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CafeRankExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CafeRankExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignChapterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignChapterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignChapterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignChapterRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignStrategyObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CampaignUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CampaignUnitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterAcademyTagsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterAcademyTagsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterAIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterAIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterCalculationLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterCalculationLimitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterCombatSkinExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterCombatSkinExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterIllustCoordinateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterIllustCoordinateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterLevelStatFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterLevelStatFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterSkillListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterSkillListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatLimitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatsDetailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatsDetailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterStatsTransExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterStatsTransExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterTranscendenceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterTranscendenceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVictoryInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVictoryInteractionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterWeaponExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterWeaponExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterWeaponExpBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterWeaponExpBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterWeaponLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterWeaponLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClearDeckRuleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClearDeckRuleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestCalculateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestCalculateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestCameraSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestCameraSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestErosionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestErosionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestErosionUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestErosionUnitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestEventExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestGroupBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestGroupBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestGroupBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestGroupBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestPlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestProgressResourceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestProgressResourceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestStepExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestStepExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestTileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestUnexpectedEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestUnexpectedEventExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestUnitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestUnitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstArenaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstArenaExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstAudioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstAudioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstCombatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstCombatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstConquestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstConquestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstEventCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstEventCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMiniGameShootingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMiniGameShootingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMinigameTBGExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMinigameTBGExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstNewbieContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstNewbieContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsFeverExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsFeverExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CostumeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CostumeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CouponCompleteExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CouponCompleteExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CouponStuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CouponStuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CumulativeTimeRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CumulativeTimeRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultCharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultEchelonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultEchelonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultFurnitureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultFurnitureExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultMailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DefaultParcelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DefaultParcelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_DuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_DuplicateBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EchelonConstraintExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EchelonConstraintExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidRankingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidRankingRewardUOExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidRankingRewardUOExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageLimitedRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageLimitedRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EliminateRaidStageSeasonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EliminateRaidStageSeasonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EmoticonSpecialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EmoticonSpecialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentArchiveBannerOffsetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentArchiveBannerOffsetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBuffGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBuffGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCardShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCardShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentChangeScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentChangeScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCharacterBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCharacterBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCurrencyItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCurrencyItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDebuffRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDebuffRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceNodeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceProbExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceProbExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentDiceRaceTotalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentDiceRaceTotalRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentFortuneGachaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentFortuneGachaExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentFortuneGachaModifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentFortuneGachaModifyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentFortuneGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentFortuneGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentLobbyMenuExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentLobbyMenuExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentLocationRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentLocationRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMeetupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMeetupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMeetupInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMeetupInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMiniEventShortCutExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMiniEventShortCutExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMiniEventTokenExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMiniEventTokenExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentPlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentShopInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentShopInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentShopRefreshExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpecialOperationsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpecialOperationsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpineDialogOffsetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpineDialogOffsetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentStageTotalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentStageTotalRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentZoneVisitRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentZoneVisitRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldContentStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldContentStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldContentStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldContentStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldCurtainCallFreeModeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldCurtainCallFreeModeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldDateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldDateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldEvidenceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldEvidenceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldInteractionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldInteractionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldKeywordExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldKeywordExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldMasteryExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldMasteryExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldMasteryLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldMasteryLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldMasteryManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldMasteryManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldQuestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldQuestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldSceneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldSceneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldStoryStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldStoryStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldTutorialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldTutorialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldWorldMapZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldWorldMapZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FixedStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FixedStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FloaterCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FloaterCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureTemplateElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureTemplateElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FurnitureTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FurnitureTemplateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaCraftNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCraftNodeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaCraftNodeGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCraftNodeGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaCraftOpenTagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCraftOpenTagExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaElementRecursiveExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaElementRecursiveExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GachaGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GoodsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GoodsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GuideMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GuideMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GuideMissionOpenStageConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GuideMissionOpenStageConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GuideMissionSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GuideMissionSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_HpBarAbbreviationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_HpBarAbbreviationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InformationStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InformationStrategyObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KnockBackExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KnockBackExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LimitedStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LimitedStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LimitedStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LimitedStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LimitedStageSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LimitedStageSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCharProfileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCharProfileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LogicEffectCommonVisualExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LogicEffectCommonVisualExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameAudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameAudioAnimatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGamePlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGamePlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRhythmBgmExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRhythmBgmExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRhythmExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRhythmExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingCharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingGeasExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingGeasExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameShootingStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameShootingStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGDiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGDiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGEncounterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGEncounterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGEncounterOptionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGEncounterOptionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGEncounterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGEncounterRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGThemaExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGThemaExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameTBGThemaRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameTBGThemaRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameTBGVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameTBGVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_NormalSkillTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_NormalSkillTemplateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleFireLineCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleFireLineCheckExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ParcelAutoSynthExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ParcelAutoSynthExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PersonalityExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PersonalityExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PickupDuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PickupDuplicateBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PresetCharacterGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PresetCharacterGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PresetCharacterGroupSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PresetCharacterGroupSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PresetParcelsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PresetParcelsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductMonthlyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductMonthlyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProtocolSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProtocolSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidRankingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidRankingRewardUOExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidRankingRewardUOExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidStageSeasonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidStageSeasonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeCraftExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeCraftExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeIngredientExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeIngredientExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeSelectionAutoUseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeSelectionAutoUseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeSelectionGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioReplayExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioReplayExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptField1ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptField1Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptTestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptTestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShiftingCraftRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShiftingCraftRecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopCashExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopCashExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopCashScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopCashScenarioResourceInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopFilterClassifiedExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopFilterClassifiedExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopFreeRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopFreeRecruitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopFreeRecruitPeriodExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopFreeRecruitPeriodExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRecruitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRefreshExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SpecialLobbyIllustExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SpecialLobbyIllustExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StrategyObjectBuffDefineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StrategyObjectBuffDefineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StringTestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StringTestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SystemMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SystemMailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticalSupportSystemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticalSupportSystemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticArenaSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticArenaSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticDamageSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticDamageSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticEntityEffectFilterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticEntityEffectFilterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticSkipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticSkipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticTimeAttackSimulatorConfigExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticTimeAttackSimulatorConfigExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TagExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TerrainAdaptationFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TerrainAdaptationFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonGeasExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonGeasExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TimeAttackDungeonSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TimeAttackDungeonSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TranscendenceRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TranscendenceRecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TrophyCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TrophyCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceSkillUseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceSkillUseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WebSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WebSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonFindGiftRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonFindGiftRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonGroupBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonGroupBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonOpenScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonOpenScheduleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidBossGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidBossGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidFavorBuffExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidFavorBuffExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AccountLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AccountLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AssistEchelonTypeConvertExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AssistEchelonTypeConvertExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AttendanceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AttendanceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AttendanceRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AttendanceRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AudioAnimatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BGMExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGMExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BGMRaidExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGMRaidExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BGMUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGMUIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CameraExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CameraExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogEventExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogEventExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogSubtitleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterGearExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterGearExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterGearLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterGearLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterPotentialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterPotentialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterPotentialRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterPotentialRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterPotentialStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterPotentialStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVoiceSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVoiceSubtitleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CheatCodeListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CheatCodeListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClanAssistSlotExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClanAssistSlotExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClanChattingEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClanChattingEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClanRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClanRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CombatEmojiExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CombatEmojiExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentEnterCostReduceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentEnterCostReduceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsShortcutExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsShortcutExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CurrencyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CurrencyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EmblemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EmblemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentNotifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentNotifyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureCellRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureCellRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentTreasureRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentTreasureRoundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FarmingDungeonLocationManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FarmingDungeonLocationManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FavorLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FavorLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FavorLevelRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FavorLevelRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FixedEchelonSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FixedEchelonSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FormationLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FormationLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GroundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GroundModuleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GroundModuleRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_IdCardBackgroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_IdCardBackgroundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InformationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InformationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LoadingImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LoadingImageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCharProfileChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCharProfileChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCodeInBuildExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCodeInBuildExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeErrorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeErrorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeEtcExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeEtcExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeSkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeSkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MemoryLobbyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MemoryLobbyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MessagePopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MessagePopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseCharacterBanExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseCharacterBanExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseFixedStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseFixedStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDefenseStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDefenseStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamCollectionScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamCollectionScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamDailyPointExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamDailyPointExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamEndingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamEndingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamEndingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamEndingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamParameterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamParameterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamReplayScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamReplayScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamScheduleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamScheduleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamScheduleResultExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamScheduleResultExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameDreamTimelineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameDreamTimelineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameDreamVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameDreamVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MissionEmergencyCompleteExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MissionEmergencyCompleteExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MultiFloorRaidStatChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MultiFloorRaidStatChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleStatExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleStatExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_OpenConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_OpenConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_OperatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_OperatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioBGEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioBGNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGNameExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioCharacterEmotionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioCharacterEmotionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioCharacterNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioCharacterNameExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioCharacterSituationSetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioCharacterSituationSetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioContentCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioModeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioModeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioModeRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioModeRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioResourceInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioTransitionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioTransitionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SchoolDungeonRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SchoolDungeonRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SchoolDungeonStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SchoolDungeonStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ServiceActionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ServiceActionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShortcutTypeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShortcutTypeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillAdditionalTooltipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillAdditionalTooltipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SoundUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SoundUIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SpineLipsyncExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SpineLipsyncExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StatLevelInterpolationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StatLevelInterpolationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StickerGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StickerGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StickerPageContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StickerPageContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StoryStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StoryStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ToastExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ToastExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TutorialCharacterDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TutorialCharacterDialogExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TutorialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TutorialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TutorialFailureImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TutorialFailureImageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_UnderCoverStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_UnderCoverStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VideoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VideoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceLogicEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceLogicEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceRoomExceptionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceRoomExceptionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceSpineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceSpineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceTimelineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceTimelineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }
