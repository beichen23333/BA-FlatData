from enum import IntEnum
from utils.encryption import convert_short, convert_ushort, convert_int, convert_long, convert_float, convert_double, convert_string, convert_uint, convert_ulong, create_key
import inspect

def dump_table(table_instance) -> list:
    excel_name = table_instance.__class__.__name__.removesuffix("Table")
    current_module = inspect.getmodule(inspect.currentframe())
    dump_func = next(f for n, f in inspect.getmembers(current_module, inspect.isfunction) if n.removeprefix("dump_") == excel_name)
    password = create_key(excel_name.removesuffix("Excel"))
    return [dump_func(table_instance.DataList(j), password) for j in range(table_instance.DataListLength())]


def dump_GroundVector3(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Y": convert_float(excel_instance.Y(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_AddressableBlackListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FolderPath": [convert_string(excel_instance.FolderPath(j), password) for j in range(excel_instance.FolderPathLength())],
        "ResourcePath": [convert_string(excel_instance.ResourcePath(j), password) for j in range(excel_instance.ResourcePathLength())],
    }

def dump_AddressableWhiteListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FolderPath": [convert_string(excel_instance.FolderPath(j), password) for j in range(excel_instance.FolderPathLength())],
        "ResourcePath": [convert_string(excel_instance.ResourcePath(j), password) for j in range(excel_instance.ResourcePathLength())],
    }

def dump_AnimationBlendTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataListLength": convert_int(excel_instance.DataListLength(), password),
    }

def dump_BlendData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Type": convert_int(excel_instance.Type(), password),
        "InfoList": [excel_instance.InfoList(j) for j in range(excel_instance.InfoListLength())],
    }

def dump_BlendInfo(excel_instance, password: bytes = b"") -> dict:
    return {
        "From": convert_int(excel_instance.From(), password),
        "To": convert_int(excel_instance.To(), password),
        "Blend": convert_float(excel_instance.Blend(), password),
    }

def dump_AnimatorDataTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AnimatorData(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AnimatorData(excel_instance, password: bytes = b"") -> dict:
    return {
        "DefaultStateName": convert_string(excel_instance.DefaultStateName(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "DataList": [excel_instance.DataList(j) for j in range(excel_instance.DataListLength())],
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
        "Events": [excel_instance.Events(j) for j in range(excel_instance.EventsLength())],
    }

def dump_AniEventData(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "Time": convert_float(excel_instance.Time(), password),
        "IntParam": convert_int(excel_instance.IntParam(), password),
        "FloatParam": convert_float(excel_instance.FloatParam(), password),
        "StringParam": convert_string(excel_instance.StringParam(), password),
    }

def dump_BattleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [excel_instance.None_(j) for j in range(excel_instance.None_Length())],
        "Single": excel_instance.Single(),
        "Guided": excel_instance.Guided(),
        "Blue": excel_instance.Blue(),
        "CoverEnter": excel_instance.CoverEnter(),
        "Normal": [excel_instance.Normal(j) for j in range(excel_instance.NormalLength())],
        "Crush": excel_instance.Crush(),
        "Able": excel_instance.Able(),
        "AllySelf": excel_instance.AllySelf(),
        "LightArmor": excel_instance.LightArmor(),
        "Wood": excel_instance.Wood(),
        "All": [excel_instance.All(j) for j in range(excel_instance.AllLength())],
        "DISTANCE": excel_instance.DISTANCE(),
        "CloseToObstacle": excel_instance.CloseToObstacle(),
        "Students": [excel_instance.Students(j) for j in range(excel_instance.StudentsLength())],
        "Sequence": excel_instance.Sequence(),
        "UseNextExSkill": excel_instance.UseNextExSkill(),
        "Student": excel_instance.Student(),
        "SearchAndMove": excel_instance.SearchAndMove(),
        "Position": excel_instance.Position(),
        "Street": excel_instance.Street(),
        "D": excel_instance.D(),
        "MAIN": excel_instance.MAIN(),
        "Remain": excel_instance.Remain(),
        "Low": excel_instance.Low(),
        "Resist": excel_instance.Resist(),
        "Ally": excel_instance.Ally(),
        "Main": excel_instance.Main(),
        "TargetToCaster": excel_instance.TargetToCaster(),
        "Duration": excel_instance.Duration(),
        "Preset": excel_instance.Preset(),
        "FinalDamage": excel_instance.FinalDamage(),
        "SpecialTransStat": excel_instance.SpecialTransStat(),
        "Talk": excel_instance.Talk(),
    }

def dump_BossPhaseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "AIPhase": convert_int(excel_instance.AIPhase(), password),
        "NormalAttackSkillUniqueName": convert_string(excel_instance.NormalAttackSkillUniqueName(), password),
        "UseExSkill": [bool(excel_instance.UseExSkill(j)) for j in range(excel_instance.UseExSkillLength())],
    }

def dump_BuffParticleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "UniqueName": convert_string(excel_instance.UniqueName(), password),
        "BuffType": convert_string(excel_instance.BuffType(), password),
        "BuffName": convert_string(excel_instance.BuffName(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePath(), password),
    }

def dump_CharacterDialogFieldExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Phase": convert_int(excel_instance.Phase(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": excel_instance.DialogType(),
        "Duration": convert_int(excel_instance.Duration(), password),
        "MotionName": convert_string(excel_instance.MotionName(), password),
        "IsInteractionDialog": bool(excel_instance.IsInteractionDialog()),
        "HideUI": bool(excel_instance.HideUI()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
    }

def dump_CheatCodeListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CheatCode": [convert_string(excel_instance.CheatCode(j), password) for j in range(excel_instance.CheatCodeLength())],
        "InputTitle": [convert_string(excel_instance.InputTitle(j), password) for j in range(excel_instance.InputTitleLength())],
        "Desc": convert_string(excel_instance.Desc(), password),
    }

def dump_ClearDeckRuleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": excel_instance.ContentType(),
        "SizeLimit": convert_int(excel_instance.SizeLimit(), password),
    }

def dump_ConquestStepExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "MapDifficulty": excel_instance.MapDifficulty(),
        "Step": convert_int(excel_instance.Step(), password),
        "StepGoalLocalize": convert_string(excel_instance.StepGoalLocalize(), password),
        "StepEnterScenarioGroupId": convert_int(excel_instance.StepEnterScenarioGroupId(), password),
        "StepEnterItemType": excel_instance.StepEnterItemType(),
        "StepEnterItemUniqueId": convert_int(excel_instance.StepEnterItemUniqueId(), password),
        "StepEnterItemAmount": convert_int(excel_instance.StepEnterItemAmount(), password),
        "UnexpectedEventUnitId": [convert_int(excel_instance.UnexpectedEventUnitId(j), password) for j in range(excel_instance.UnexpectedEventUnitIdLength())],
        "UnexpectedEventPrefab": convert_string(excel_instance.UnexpectedEventPrefab(), password),
        "TreasureBoxObjectId": convert_int(excel_instance.TreasureBoxObjectId(), password),
        "TreasureBoxCountPerStepOpen": convert_int(excel_instance.TreasureBoxCountPerStepOpen(), password),
    }

def dump_ConstArenaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttackCoolTime": convert_int(excel_instance.AttackCoolTime(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "DefenseCoolTime": convert_int(excel_instance.DefenseCoolTime(), password),
        "TSSStartCoolTime": convert_int(excel_instance.TSSStartCoolTime(), password),
        "EndAlarm": convert_int(excel_instance.EndAlarm(), password),
        "TimeRewardMaxAmount": convert_int(excel_instance.TimeRewardMaxAmount(), password),
        "EnterCostType": excel_instance.EnterCostType(),
        "EnterCostId": convert_int(excel_instance.EnterCostId(), password),
        "TicketCost": convert_int(excel_instance.TicketCost(), password),
        "DailyRewardResetTime": convert_string(excel_instance.DailyRewardResetTime(), password),
        "OpenScenarioId": convert_string(excel_instance.OpenScenarioId(), password),
        "CharacterSlotHideRank": [convert_int(excel_instance.CharacterSlotHideRank(j), password) for j in range(excel_instance.CharacterSlotHideRankLength())],
        "MapSlotHideRank": convert_int(excel_instance.MapSlotHideRank(), password),
        "RelativeOpponentRankStart": [convert_int(excel_instance.RelativeOpponentRankStart(j), password) for j in range(excel_instance.RelativeOpponentRankStartLength())],
        "RelativeOpponentRankEnd": [convert_int(excel_instance.RelativeOpponentRankEnd(j), password) for j in range(excel_instance.RelativeOpponentRankEndLength())],
        "ModifiedStatType": [excel_instance.ModifiedStatType(j) for j in range(excel_instance.ModifiedStatTypeLength())],
        "StatMulFactor": [convert_int(excel_instance.StatMulFactor(j), password) for j in range(excel_instance.StatMulFactorLength())],
        "StatSumFactor": [convert_int(excel_instance.StatSumFactor(j), password) for j in range(excel_instance.StatSumFactorLength())],
        "NPCName": [convert_string(excel_instance.NPCName(j), password) for j in range(excel_instance.NPCNameLength())],
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
        "WORLDBOSSBATTLELITTLETw": convert_int(excel_instance.WORLDBOSSBATTLELITTLETw(), password),
        "WORLDBOSSBATTLELITTLEAsia": convert_int(excel_instance.WORLDBOSSBATTLELITTLEAsia(), password),
        "WORLDBOSSBATTLELITTLENa": convert_int(excel_instance.WORLDBOSSBATTLELITTLENa(), password),
        "WORLDBOSSBATTLELITTLEGlobal": convert_int(excel_instance.WORLDBOSSBATTLELITTLEGlobal(), password),
        "WORLDBOSSBATTLEMIDDLE": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLE(), password),
        "WORLDBOSSBATTLEMIDDLETw": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLETw(), password),
        "WORLDBOSSBATTLEMIDDLEAsia": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLEAsia(), password),
        "WORLDBOSSBATTLEMIDDLENa": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLENa(), password),
        "WORLDBOSSBATTLEMIDDLEGlobal": convert_int(excel_instance.WORLDBOSSBATTLEMIDDLEGlobal(), password),
        "WORLDBOSSBATTLEHIGH": convert_int(excel_instance.WORLDBOSSBATTLEHIGH(), password),
        "WORLDBOSSBATTLEHIGHTw": convert_int(excel_instance.WORLDBOSSBATTLEHIGHTw(), password),
        "WORLDBOSSBATTLEHIGHAsia": convert_int(excel_instance.WORLDBOSSBATTLEHIGHAsia(), password),
        "WORLDBOSSBATTLEHIGHNa": convert_int(excel_instance.WORLDBOSSBATTLEHIGHNa(), password),
        "WORLDBOSSBATTLEHIGHGlobal": convert_int(excel_instance.WORLDBOSSBATTLEHIGHGlobal(), password),
        "WORLDBOSSBATTLEVERYHIGH": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGH(), password),
        "WORLDBOSSBATTLEVERYHIGHTw": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHTw(), password),
        "WORLDBOSSBATTLEVERYHIGHAsia": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHAsia(), password),
        "WORLDBOSSBATTLEVERYHIGHNa": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHNa(), password),
        "WORLDBOSSBATTLEVERYHIGHGlobal": convert_int(excel_instance.WORLDBOSSBATTLEVERYHIGHGlobal(), password),
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
        "EchelonMaxOverloadCost": convert_int(excel_instance.EchelonMaxOverloadCost(), password),
        "EchelonExtensionMaxOverloadCost": convert_int(excel_instance.EchelonExtensionMaxOverloadCost(), password),
        "EchelonExtensionEchelonInitCommonCost": convert_int(excel_instance.EchelonExtensionEchelonInitCommonCost(), password),
        "EchelonExtensionCostRegenRatio": convert_int(excel_instance.EchelonExtensionCostRegenRatio(), password),
        "EchelonOverloadCostRegenRatio": convert_int(excel_instance.EchelonOverloadCostRegenRatio(), password),
        "EchelonExtensionOverloadCostRegenRatio": convert_int(excel_instance.EchelonExtensionOverloadCostRegenRatio(), password),
        "CheckCheaterMaxUseCostMultiFloorRaid": convert_int(excel_instance.CheckCheaterMaxUseCostMultiFloorRaid(), password),
        "ExcessiveTouchCheckTime": convert_float(excel_instance.ExcessiveTouchCheckTime(), password),
        "ExcessiveTouchCheckCount": convert_int(excel_instance.ExcessiveTouchCheckCount(), password),
        "CampaignAlertPopupLevelGap": convert_int(excel_instance.CampaignAlertPopupLevelGap(), password),
        "MoveCorrectionSkipRatio": convert_int(excel_instance.MoveCorrectionSkipRatio(), password),
        "ObstacleColliderHeightJumpable": convert_float(excel_instance.ObstacleColliderHeightJumpable(), password),
        "ObstacleColliderHeightNotJumpable": convert_float(excel_instance.ObstacleColliderHeightNotJumpable(), password),
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
        "CraftDuration": [convert_int(excel_instance.CraftDuration(j), password) for j in range(excel_instance.CraftDurationLength())],
        "CraftLimitTime": convert_int(excel_instance.CraftLimitTime(), password),
        "ShiftingCraftDuration": [convert_int(excel_instance.ShiftingCraftDuration(j), password) for j in range(excel_instance.ShiftingCraftDurationLength())],
        "ShiftingCraftTicketConsumeAmount": convert_int(excel_instance.ShiftingCraftTicketConsumeAmount(), password),
        "ShiftingCraftSlotMaxCapacity": convert_int(excel_instance.ShiftingCraftSlotMaxCapacity(), password),
        "CraftTicketItemUniqueId": convert_int(excel_instance.CraftTicketItemUniqueId(), password),
        "CraftTicketConsumeAmount": convert_int(excel_instance.CraftTicketConsumeAmount(), password),
        "AcademyEnterCostType": excel_instance.AcademyEnterCostType(),
        "AcademyEnterCostId": convert_int(excel_instance.AcademyEnterCostId(), password),
        "AcademyTicketCost": convert_int(excel_instance.AcademyTicketCost(), password),
        "MassangerMessageExpireDay": convert_int(excel_instance.MassangerMessageExpireDay(), password),
        "CraftLeafNodeGenerateLv1Count": convert_int(excel_instance.CraftLeafNodeGenerateLv1Count(), password),
        "CraftLeafNodeGenerateLv2Count": convert_int(excel_instance.CraftLeafNodeGenerateLv2Count(), password),
        "TutorialGachaShopId": convert_int(excel_instance.TutorialGachaShopId(), password),
        "BeforehandGachaShopId": convert_int(excel_instance.BeforehandGachaShopId(), password),
        "TutorialGachaGoodsId": convert_int(excel_instance.TutorialGachaGoodsId(), password),
        "EquipmentSlotOpenLevel": [convert_int(excel_instance.EquipmentSlotOpenLevel(j), password) for j in range(excel_instance.EquipmentSlotOpenLevelLength())],
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
        "CraftBaseGoldRequired": [convert_int(excel_instance.CraftBaseGoldRequired(j), password) for j in range(excel_instance.CraftBaseGoldRequiredLength())],
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
        "RaidEnterCostType": excel_instance.RaidEnterCostType(),
        "RaidEnterCostId": convert_int(excel_instance.RaidEnterCostId(), password),
        "RaidTicketCost": convert_int(excel_instance.RaidTicketCost(), password),
        "TimeAttackDungeonScenarioId": convert_string(excel_instance.TimeAttackDungeonScenarioId(), password),
        "TimeAttackDungoenPlayCountPerTicket": convert_int(excel_instance.TimeAttackDungoenPlayCountPerTicket(), password),
        "TimeAttackDungeonEnterCostType": excel_instance.TimeAttackDungeonEnterCostType(),
        "TimeAttackDungeonEnterCostId": convert_int(excel_instance.TimeAttackDungeonEnterCostId(), password),
        "TimeAttackDungeonEnterCost": convert_int(excel_instance.TimeAttackDungeonEnterCost(), password),
        "ClanLeaderTransferLastLoginLimit": convert_int(excel_instance.ClanLeaderTransferLastLoginLimit(), password),
        "MonthlyProductRepurchasePopupLimit": convert_int(excel_instance.MonthlyProductRepurchasePopupLimit(), password),
        "CommonFavorItemTags": [excel_instance.CommonFavorItemTags(j) for j in range(excel_instance.CommonFavorItemTagsLength())],
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
        "CallnameLengthEn": convert_int(excel_instance.CallnameLengthEn(), password),
        "CallnameLengthKr": convert_int(excel_instance.CallnameLengthKr(), password),
        "NicknameLengthKr": convert_int(excel_instance.NicknameLengthKr(), password),
        "ClanNameLength": convert_int(excel_instance.ClanNameLength(), password),
        "CafePresetEditNameLength": convert_int(excel_instance.CafePresetEditNameLength(), password),
        "FormationPresetEchelonTabTextLengthKr": convert_int(excel_instance.FormationPresetEchelonTabTextLengthKr(), password),
        "FormationPresetEchelonSlotTextLengthKr": convert_int(excel_instance.FormationPresetEchelonSlotTextLengthKr(), password),
        "CharProfileRowIntervalJp": convert_int(excel_instance.CharProfileRowIntervalJp(), password),
        "CharProfilePopupRowIntervalKr": convert_int(excel_instance.CharProfilePopupRowIntervalKr(), password),
        "CharProfilePopupRowIntervalJp": convert_int(excel_instance.CharProfilePopupRowIntervalJp(), password),
        "BeforehandGachaCount": convert_int(excel_instance.BeforehandGachaCount(), password),
        "LowMemorySizeGL": convert_int(excel_instance.LowMemorySizeGL(), password),
        "BeforehandGachaGroupId": convert_int(excel_instance.BeforehandGachaGroupId(), password),
        "RenewalDisplayOrderDay": convert_int(excel_instance.RenewalDisplayOrderDay(), password),
        "EmblemDefaultId": convert_int(excel_instance.EmblemDefaultId(), password),
        "BirthdayMailStartDate": convert_string(excel_instance.BirthdayMailStartDate(), password),
        "BirthdayMailRemainDate": convert_int(excel_instance.BirthdayMailRemainDate(), password),
        "BirthdayMailParcelType": excel_instance.BirthdayMailParcelType(),
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
        "ClanChattingNoticeCautionDelay": convert_float(excel_instance.ClanChattingNoticeCautionDelay(), password),
        "CallNameWaitTimeGL": convert_float(excel_instance.CallNameWaitTimeGL(), password),
        "AssistStrangerMaxLevel": convert_int(excel_instance.AssistStrangerMaxLevel(), password),
        "MaxBlockedUserCount": convert_int(excel_instance.MaxBlockedUserCount(), password),
        "CafeRandomVisitMinComfortBonus": convert_int(excel_instance.CafeRandomVisitMinComfortBonus(), password),
        "CafeRandomVisitMinLastLogin": convert_int(excel_instance.CafeRandomVisitMinLastLogin(), password),
        "CafeTravelSyncIntervalByMillisec": convert_int(excel_instance.CafeTravelSyncIntervalByMillisec(), password),
        "RankBracketPercentage1": convert_int(excel_instance.RankBracketPercentage1(), password),
        "RankBracketPercentage2": convert_int(excel_instance.RankBracketPercentage2(), password),
        "RankBracketPercentage3": convert_int(excel_instance.RankBracketPercentage3(), password),
        "RankBracketPercentage4": convert_int(excel_instance.RankBracketPercentage4(), password),
        "RankBracketPercentage5": convert_int(excel_instance.RankBracketPercentage5(), password),
        "RankBracketPercentage6": convert_int(excel_instance.RankBracketPercentage6(), password),
        "RankBracketPercentage7": convert_int(excel_instance.RankBracketPercentage7(), password),
        "ExpiryBattlePassItemReceiveDay": convert_int(excel_instance.ExpiryBattlePassItemReceiveDay(), password),
        "BattlePassFlavorTextIdleDurationMilliSec": convert_int(excel_instance.BattlePassFlavorTextIdleDurationMilliSec(), password),
        "BattlePassEndImminentDay": convert_int(excel_instance.BattlePassEndImminentDay(), password),
        "BattlePassExpIconPath": convert_string(excel_instance.BattlePassExpIconPath(), password),
        "CafeCameraDragThreshold": convert_float(excel_instance.CafeCameraDragThreshold(), password),
        "CafeSummonTicketBuyLimitForValidate": convert_int(excel_instance.CafeSummonTicketBuyLimitForValidate(), password),
        "BattlePassNotifyDateGL": convert_int(excel_instance.BattlePassNotifyDateGL(), password),
        "PurchaseMailExpiredDayGL": convert_int(excel_instance.PurchaseMailExpiredDayGL(), password),
        "ReviewEventDateGL": convert_string(excel_instance.ReviewEventDateGL(), password),
        "ReviewEventStageIDGL": convert_int(excel_instance.ReviewEventStageIDGL(), password),
        "ReviewEventCharIDGL": convert_int(excel_instance.ReviewEventCharIDGL(), password),
        "AutoCraftPresetCountLimit": convert_int(excel_instance.AutoCraftPresetCountLimit(), password),
        "AutoCraftNodeSelectCount": convert_int(excel_instance.AutoCraftNodeSelectCount(), password),
        "CraftPresetNameMaxLength": convert_int(excel_instance.CraftPresetNameMaxLength(), password),
        "SelectionWaitTime": convert_int(excel_instance.SelectionWaitTime(), password),
        "RewardWaitTime": convert_int(excel_instance.RewardWaitTime(), password),
        "EpisodeContinueWaitTime": convert_int(excel_instance.EpisodeContinueWaitTime(), password),
        "ScenarioAutoDelayMillisecLong": convert_float(excel_instance.ScenarioAutoDelayMillisecLong(), password),
        "ScenarioAutoDelayMillisec": convert_float(excel_instance.ScenarioAutoDelayMillisec(), password),
        "ScenarioAutoDelayMillisecShort": convert_float(excel_instance.ScenarioAutoDelayMillisecShort(), password),
        "ScenarioAutoDelayMillisecVeryShort": convert_float(excel_instance.ScenarioAutoDelayMillisecVeryShort(), password),
        "PcBuildEnterInformation": convert_int(excel_instance.PcBuildEnterInformation(), password),
        "ComebackUserStandardDay": convert_int(excel_instance.ComebackUserStandardDay(), password),
        "ComebackUserLogSaveDay": convert_int(excel_instance.ComebackUserLogSaveDay(), password),
        "ComeBackActivateCooldown": convert_int(excel_instance.ComeBackActivateCooldown(), password),
        "CafeCopyPresetSlotCount": convert_int(excel_instance.CafeCopyPresetSlotCount(), password),
        "ExpiryProductDailyRecordItemReceiveDay": convert_int(excel_instance.ExpiryProductDailyRecordItemReceiveDay(), password),
        "NewbieUserStandardDay": convert_int(excel_instance.NewbieUserStandardDay(), password),
        "NewbieStateHoldDay": convert_int(excel_instance.NewbieStateHoldDay(), password),
        "QRIconUrlDev": convert_string(excel_instance.QRIconUrlDev(), password),
        "QRIconUrlLive": convert_string(excel_instance.QRIconUrlLive(), password),
        "ProbablityInfoBtnLinkKR": convert_string(excel_instance.ProbablityInfoBtnLinkKR(), password),
        "ClearDeckEchelonShowMaxCount": convert_int(excel_instance.ClearDeckEchelonShowMaxCount(), password),
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

def dump_ConstContentsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UseSearchFieldOptimize": bool(excel_instance.UseSearchFieldOptimize()),
        "SearchUpdateTime": convert_float(excel_instance.SearchUpdateTime(), password),
        "LobbyDayTimeFrom": convert_int(excel_instance.LobbyDayTimeFrom(), password),
        "LobbyNightTimeFrom": convert_int(excel_instance.LobbyNightTimeFrom(), password),
    }

def dump_ConstEventCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentHardStageCount": convert_int(excel_instance.EventContentHardStageCount(), password),
        "EventStrategyPlayTimeLimitInSeconds": convert_int(excel_instance.EventStrategyPlayTimeLimitInSeconds(), password),
        "SubEventChangeLimitSeconds": convert_int(excel_instance.SubEventChangeLimitSeconds(), password),
        "SubEventInstantClear": bool(excel_instance.SubEventInstantClear()),
        "CardShopProbWeightCount": convert_int(excel_instance.CardShopProbWeightCount(), password),
        "CardShopProbWeightRarity": excel_instance.CardShopProbWeightRarity(),
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

def dump_ConstKeyMappingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DragSensitivity": convert_float(excel_instance.DragSensitivity(), password),
        "PcInformationGroupID": convert_int(excel_instance.PcInformationGroupID(), password),
        "PcControllerInformationGroupID": convert_int(excel_instance.PcControllerInformationGroupID(), password),
        "ScrollWheelFactor": convert_float(excel_instance.ScrollWheelFactor(), password),
        "RemoveKeycodeWord": convert_string(excel_instance.RemoveKeycodeWord(), password),
        "TutorialDialogTouchKey": convert_string(excel_instance.TutorialDialogTouchKey(), password),
        "ControllerCursorFactorSlow": convert_int(excel_instance.ControllerCursorFactorSlow(), password),
        "ControllerCursorFactor": convert_int(excel_instance.ControllerCursorFactor(), password),
        "ControllerCursorFactorFast": convert_int(excel_instance.ControllerCursorFactorFast(), password),
        "VibrationSec": convert_float(excel_instance.VibrationSec(), password),
        "VibrationPower": convert_float(excel_instance.VibrationPower(), password),
        "ControllerScrollWheelFactor": convert_float(excel_instance.ControllerScrollWheelFactor(), password),
        "ControllerZoomSensitivity": convert_float(excel_instance.ControllerZoomSensitivity(), password),
        "ControllerDpadMoveCheckRangeX": convert_float(excel_instance.ControllerDpadMoveCheckRangeX(), password),
        "ControllerDpadMoveCheckRangeY": convert_float(excel_instance.ControllerDpadMoveCheckRangeY(), password),
        "ControllerCursorClickScale": convert_float(excel_instance.ControllerCursorClickScale(), password),
        "ControllerScrollSensitivity": convert_float(excel_instance.ControllerScrollSensitivity(), password),
    }

def dump_ConstMinigameCCGExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TurnDrawCount": convert_int(excel_instance.TurnDrawCount(), password),
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
        "MaxHandCount": convert_int(excel_instance.MaxHandCount(), password),
        "MaxCost": convert_int(excel_instance.MaxCost(), password),
        "StartCost": convert_int(excel_instance.StartCost(), password),
        "TurnCost": convert_int(excel_instance.TurnCost(), password),
        "StrikerSwapFrontCost": convert_int(excel_instance.StrikerSwapFrontCost(), password),
        "StrikerMaxEquipCount": convert_int(excel_instance.StrikerMaxEquipCount(), password),
        "StartDrawCount": convert_int(excel_instance.StartDrawCount(), password),
        "CampReviveHealthRate": convert_int(excel_instance.CampReviveHealthRate(), password),
        "BaseRewardRerollPoint": convert_int(excel_instance.BaseRewardRerollPoint(), password),
        "SelectRewardOptionCount": convert_int(excel_instance.SelectRewardOptionCount(), password),
        "AlternativeCardImagePath": convert_string(excel_instance.AlternativeCardImagePath(), password),
    }

def dump_ConstMinigameRoadPuzzleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RoadPuzzleMapBoundaryOffsetLeft": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetLeft(), password),
        "RoadPuzzleMapBoundaryOffsetRight": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetRight(), password),
        "RoadPuzzleMapBoundaryOffsetTop": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetTop(), password),
        "RoadPuzzleMapBoundaryOffsetBottom": convert_float(excel_instance.RoadPuzzleMapBoundaryOffsetBottom(), password),
        "RoadPuzzleMapCenterOffsetX": convert_float(excel_instance.RoadPuzzleMapCenterOffsetX(), password),
        "RoadPuzzleMapCenterOffsetY": convert_float(excel_instance.RoadPuzzleMapCenterOffsetY(), password),
        "CameraAngle": convert_float(excel_instance.CameraAngle(), password),
        "CameraZoomMax": convert_float(excel_instance.CameraZoomMax(), password),
        "CameraZoomMin": convert_float(excel_instance.CameraZoomMin(), password),
        "CameraZoomDefault": convert_float(excel_instance.CameraZoomDefault(), password),
        "StageLoadingProgressTime": convert_float(excel_instance.StageLoadingProgressTime(), password),
        "TileRotationDegree": convert_int(excel_instance.TileRotationDegree(), password),
        "StartStageIndex": convert_int(excel_instance.StartStageIndex(), password),
        "LoopStageIndex": convert_int(excel_instance.LoopStageIndex(), password),
    }

def dump_ConstMiniGameShootingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "NormalStageId": convert_int(excel_instance.NormalStageId(), password),
        "NormalSectionCount": convert_int(excel_instance.NormalSectionCount(), password),
        "HardStageId": convert_int(excel_instance.HardStageId(), password),
        "HardSectionCount": convert_int(excel_instance.HardSectionCount(), password),
        "FreeStageId": convert_int(excel_instance.FreeStageId(), password),
        "FreeSectionCount": convert_int(excel_instance.FreeSectionCount(), password),
        "PlayerCharacterId": [convert_int(excel_instance.PlayerCharacterId(j), password) for j in range(excel_instance.PlayerCharacterIdLength())],
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
        "HealCostType": excel_instance.HealCostType(),
        "HealCostAmount": [convert_int(excel_instance.HealCostAmount(j), password) for j in range(excel_instance.HealCostAmountLength())],
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
        "MultiSweepPresetNameMaxLengthKr": convert_int(excel_instance.MultiSweepPresetNameMaxLengthKr(), password),
        "MultiSweepPresetSelectStageMaxCount": convert_int(excel_instance.MultiSweepPresetSelectStageMaxCount(), password),
        "MultiSweepPresetMaxSweepCount": convert_int(excel_instance.MultiSweepPresetMaxSweepCount(), password),
        "MultiSweepPresetSelectParcelMaxCount": convert_int(excel_instance.MultiSweepPresetSelectParcelMaxCount(), password),
    }

def dump_CouponStuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StuffId": convert_int(excel_instance.StuffId(), password),
        "ParcelType": excel_instance.ParcelType(),
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
        "TimeCondition": [convert_int(excel_instance.TimeCondition(j), password) for j in range(excel_instance.TimeConditionLength())],
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardId": [convert_int(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
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
        "MainId": [convert_int(excel_instance.MainId(j), password) for j in range(excel_instance.MainIdLength())],
        "SupportId": [convert_int(excel_instance.SupportId(j), password) for j in range(excel_instance.SupportIdLength())],
        "TssId": convert_int(excel_instance.TssId(), password),
    }

def dump_DefaultFurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Location": excel_instance.Location(),
        "PositionX": convert_float(excel_instance.PositionX(), password),
        "PositionY": convert_float(excel_instance.PositionY(), password),
        "Rotation": convert_float(excel_instance.Rotation(), password),
    }

def dump_DefaultMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "MailType": excel_instance.MailType(),
        "MailSendPeriodFrom": convert_string(excel_instance.MailSendPeriodFrom(), password),
        "MailSendPeriodTo": convert_string(excel_instance.MailSendPeriodTo(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_DefaultParcelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": excel_instance.ParcelType(),
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "ParcelAmount": convert_int(excel_instance.ParcelAmount(), password),
    }

def dump_EmoticonSpecialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "CharacterUniqueId": convert_int(excel_instance.CharacterUniqueId(), password),
        "Random": convert_string(excel_instance.Random(), password),
    }

def dump_EventContentBoxGachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
    }

def dump_EventContentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "BgImagePath": convert_string(excel_instance.BgImagePath(), password),
    }

def dump_FieldContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "AreaId": convert_int(excel_instance.AreaId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "StageDifficulty": excel_instance.StageDifficulty(),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": excel_instance.StageEnterCostType(),
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "InstantClear": bool(excel_instance.InstantClear()),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "SkipFormationSettings": bool(excel_instance.SkipFormationSettings()),
        "DailyLastPlay": bool(excel_instance.DailyLastPlay()),
        "StarGoal": [excel_instance.StarGoal(j) for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
    }

def dump_FieldContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
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
        "StartConditionType": excel_instance.StartConditionType(),
        "StartConditionId": convert_int(excel_instance.StartConditionId(), password),
        "EndConditionType": excel_instance.EndConditionType(),
        "EndConditionId": convert_int(excel_instance.EndConditionId(), password),
        "EndReadyConditionType": excel_instance.EndReadyConditionType(),
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
        "InteractionType": [excel_instance.InteractionType(j) for j in range(excel_instance.InteractionTypeLength())],
        "InteractionId": [convert_long(excel_instance.InteractionId(j), password) for j in range(excel_instance.InteractionIdLength())],
        "ConditionClass": excel_instance.ConditionClass(),
        "ConditionClassParameters": [convert_long(excel_instance.ConditionClassParameters(j), password) for j in range(excel_instance.ConditionClassParametersLength())],
        "OnceOnly": bool(excel_instance.OnceOnly()),
        "ConditionIndex": [convert_long(excel_instance.ConditionIndex(j), password) for j in range(excel_instance.ConditionIndexLength())],
        "ConditionType": [excel_instance.ConditionType(j) for j in range(excel_instance.ConditionTypeLength())],
        "ConditionId": [convert_long(excel_instance.ConditionId(j), password) for j in range(excel_instance.ConditionIdLength())],
        "NegateCondition": [bool(excel_instance.NegateCondition(j)) for j in range(excel_instance.NegateConditionLength())],
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
        "TokenType": excel_instance.TokenType(),
        "TokenId": convert_int(excel_instance.TokenId(), password),
        "TokenRequirement": convert_int(excel_instance.TokenRequirement(), password),
        "AccomplishmentConditionType": excel_instance.AccomplishmentConditionType(),
        "AccomplishmentConditionId": convert_int(excel_instance.AccomplishmentConditionId(), password),
    }

def dump_FieldMasteryLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "Id": [convert_int(excel_instance.Id(j), password) for j in range(excel_instance.IdLength())],
        "Exp": [convert_int(excel_instance.Exp(j), password) for j in range(excel_instance.ExpLength())],
        "TotalExp": [convert_int(excel_instance.TotalExp(j), password) for j in range(excel_instance.TotalExpLength())],
        "RewardId": [convert_int(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
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
        "QuestGroupId": convert_int(excel_instance.QuestGroupId(), password),
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
        "RewardParcelType": excel_instance.RewardParcelType(),
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
        "ConditionalBGMQuestId": [convert_long(excel_instance.ConditionalBGMQuestId(j), password) for j in range(excel_instance.ConditionalBGMQuestIdLength())],
        "BeginConditionalBGMScenarioGroupId": [convert_long(excel_instance.BeginConditionalBGMScenarioGroupId(j), password) for j in range(excel_instance.BeginConditionalBGMScenarioGroupIdLength())],
        "BeginConditionalBGMInteractionId": [convert_long(excel_instance.BeginConditionalBGMInteractionId(j), password) for j in range(excel_instance.BeginConditionalBGMInteractionIdLength())],
        "EndConditionalBGMScenarioGroupId": [convert_long(excel_instance.EndConditionalBGMScenarioGroupId(j), password) for j in range(excel_instance.EndConditionalBGMScenarioGroupIdLength())],
        "EndConditionalBGMInteractionId": [convert_long(excel_instance.EndConditionalBGMInteractionId(j), password) for j in range(excel_instance.EndConditionalBGMInteractionIdLength())],
        "ConditionalBGMId": [convert_long(excel_instance.ConditionalBGMId(j), password) for j in range(excel_instance.ConditionalBGMIdLength())],
    }

def dump_FieldSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "FieldContentType": excel_instance.FieldContentType(),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EntryDateId": convert_int(excel_instance.EntryDateId(), password),
        "InstantEntryDateId": convert_int(excel_instance.InstantEntryDateId(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "LobbyBGMChangeStageId": convert_int(excel_instance.LobbyBGMChangeStageId(), password),
        "FieldPrefabControlID": convert_int(excel_instance.FieldPrefabControlID(), password),
        "FieldGetKeywordCallDialogEnum": excel_instance.FieldGetKeywordCallDialogEnum(),
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
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "SkipFormationSettings": bool(excel_instance.SkipFormationSettings()),
    }

def dump_FieldTutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "TutorialType": [excel_instance.TutorialType(j) for j in range(excel_instance.TutorialTypeLength())],
        "ConditionType": [excel_instance.ConditionType(j) for j in range(excel_instance.ConditionTypeLength())],
        "ConditionId": [convert_int(excel_instance.ConditionId(j), password) for j in range(excel_instance.ConditionIdLength())],
    }

def dump_FieldWorldMapZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Date": convert_int(excel_instance.Date(), password),
        "OpenConditionType": excel_instance.OpenConditionType(),
        "OpenConditionId": convert_int(excel_instance.OpenConditionId(), password),
        "CloseConditionType": excel_instance.CloseConditionType(),
        "CloseConditionId": convert_int(excel_instance.CloseConditionId(), password),
        "ResultFieldScene": convert_int(excel_instance.ResultFieldScene(), password),
        "FieldStageInteractionId": convert_int(excel_instance.FieldStageInteractionId(), password),
        "WorldMapButtonType": excel_instance.WorldMapButtonType(),
        "LocalizeCode": convert_uint(excel_instance.LocalizeCode(), password),
        "NewTagDisplay": bool(excel_instance.NewTagDisplay()),
    }

def dump_GroundGridFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "StartX": convert_float(excel_instance.StartX(), password),
        "StartY": convert_float(excel_instance.StartY(), password),
        "Gap": convert_float(excel_instance.Gap(), password),
        "Nodes": [excel_instance.Nodes(j) for j in range(excel_instance.NodesLength())],
        "Version": convert_string(excel_instance.Version(), password),
    }

def dump_GroundNodeFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_int(excel_instance.X(), password),
        "Y": convert_int(excel_instance.Y(), password),
        "IsCanNotUseSkill": bool(excel_instance.IsCanNotUseSkill()),
        "Position": excel_instance.Position(),
        "NodeType": excel_instance.NodeType(),
        "OriginalNodeType": excel_instance.OriginalNodeType(),
    }

def dump_GroundNodeLayerFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "Layers": [excel_instance.Layers(j) for j in range(excel_instance.LayersLength())],
    }

def dump_KatakanaConvertExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
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
        "StageDifficulty": excel_instance.StageDifficulty(),
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "OpenDate": convert_int(excel_instance.OpenDate(), password),
        "OpenEventPoint": convert_int(excel_instance.OpenEventPoint(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": excel_instance.StageEnterCostType(),
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "StrategyEnvironment": excel_instance.StrategyEnvironment(),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "ContentType": excel_instance.ContentType(),
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
        "RewardParcelType": excel_instance.RewardParcelType(),
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

def dump_MinigameCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [excel_instance.None_(j) for j in range(excel_instance.None_Length())],
    }

def dump_MinigameRoadExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [excel_instance.None_(j) for j in range(excel_instance.None_Length())],
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
        "SubOffset": [convert_float(excel_instance.SubOffset(j), password) for j in range(excel_instance.SubOffsetLength())],
        "X": convert_float(excel_instance.X(), password),
        "Z": convert_float(excel_instance.Z(), password),
        "Hp": convert_int(excel_instance.Hp(), password),
        "MaxHp": convert_int(excel_instance.MaxHp(), password),
        "BlockRate": convert_int(excel_instance.BlockRate(), password),
        "EvasionRate": convert_int(excel_instance.EvasionRate(), password),
        "DestroyType": excel_instance.DestroyType(),
        "Point1Offeset": [convert_float(excel_instance.Point1Offeset(j), password) for j in range(excel_instance.Point1OffesetLength())],
        "EnemyPoint1Osset": [convert_float(excel_instance.EnemyPoint1Osset(j), password) for j in range(excel_instance.EnemyPoint1OssetLength())],
        "Point2Offeset": [convert_float(excel_instance.Point2Offeset(j), password) for j in range(excel_instance.Point2OffesetLength())],
        "EnemyPoint2Osset": [convert_float(excel_instance.EnemyPoint2Osset(j), password) for j in range(excel_instance.EnemyPoint2OssetLength())],
        "SubObstacleID": [convert_int(excel_instance.SubObstacleID(j), password) for j in range(excel_instance.SubObstacleIDLength())],
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
        "Positions": [excel_instance.Positions(j) for j in range(excel_instance.PositionsLength())],
        "Rotations": [excel_instance.Rotations(j) for j in range(excel_instance.RotationsLength())],
    }

def dump_PropRootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "RootMotions": [excel_instance.RootMotions(j) for j in range(excel_instance.RootMotionsLength())],
    }

def dump_ProtocolSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Protocol": convert_string(excel_instance.Protocol(), password),
        "OpenConditionContent": excel_instance.OpenConditionContent(),
        "Currency": bool(excel_instance.Currency()),
        "Inventory": bool(excel_instance.Inventory()),
        "Mail": bool(excel_instance.Mail()),
    }

def dump_RecipeCraftExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "RecipeType": excel_instance.RecipeType(),
        "RecipeIngredientId": convert_int(excel_instance.RecipeIngredientId(), password),
        "RecipeIngredientDevName": convert_string(excel_instance.RecipeIngredientDevName(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelDevName": [convert_string(excel_instance.ParcelDevName(j), password) for j in range(excel_instance.ParcelDevNameLength())],
        "ResultAmountMin": [convert_int(excel_instance.ResultAmountMin(j), password) for j in range(excel_instance.ResultAmountMinLength())],
        "ResultAmountMax": [convert_int(excel_instance.ResultAmountMax(j), password) for j in range(excel_instance.ResultAmountMaxLength())],
    }

def dump_Position(excel_instance, password: bytes = b"") -> dict:
    return {
        "X": convert_float(excel_instance.X(), password),
        "Z": convert_float(excel_instance.Z(), password),
    }

def dump_Motion(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "Positions": [excel_instance.Positions(j) for j in range(excel_instance.PositionsLength())],
    }

def dump_MoveEnd(excel_instance, password: bytes = b"") -> dict:
    return {
        "Normal": excel_instance.Normal(),
        "Stand": excel_instance.Stand(),
        "Kneel": excel_instance.Kneel(),
    }

def dump_Form(excel_instance, password: bytes = b"") -> dict:
    return {
        "MoveEnd": excel_instance.MoveEnd(),
        "PublicSkill": excel_instance.PublicSkill(),
    }

def dump_RootMotionFlat(excel_instance, password: bytes = b"") -> dict:
    return {
        "Forms": [excel_instance.Forms(j) for j in range(excel_instance.FormsLength())],
        "ExSkills": [excel_instance.ExSkills(j) for j in range(excel_instance.ExSkillsLength())],
        "MoveLeft": excel_instance.MoveLeft(),
        "MoveRight": excel_instance.MoveRight(),
    }

def dump_ScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "None_": [excel_instance.None_(j) for j in range(excel_instance.None_Length())],
        "Idle": [excel_instance.Idle(j) for j in range(excel_instance.IdleLength())],
        "Cafe": excel_instance.Cafe(),
        "Talk": excel_instance.Talk(),
        "Open": excel_instance.Open(),
        "EnterConver": excel_instance.EnterConver(),
        "Center": excel_instance.Center(),
        "Instant": excel_instance.Instant(),
        "Prologue": excel_instance.Prologue(),
    }

def dump_ScenarioReplayExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeId": convert_int(excel_instance.ModeId(), password),
        "VolumeId": convert_int(excel_instance.VolumeId(), password),
        "ReplayType": excel_instance.ReplayType(),
        "ChapterId": convert_int(excel_instance.ChapterId(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeId(), password),
        "FrontScenarioGroupId": [convert_int(excel_instance.FrontScenarioGroupId(j), password) for j in range(excel_instance.FrontScenarioGroupIdLength())],
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "BackScenarioGroupId": [convert_int(excel_instance.BackScenarioGroupId(j), password) for j in range(excel_instance.BackScenarioGroupIdLength())],
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

def dump_StringTestExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "String": [convert_string(excel_instance.String(j), password) for j in range(excel_instance.StringLength())],
        "Sentence1": convert_string(excel_instance.Sentence1(), password),
        "Script": convert_string(excel_instance.Script(), password),
    }

def dump_SystemMailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MailType": excel_instance.MailType(),
        "IsProductMail": bool(excel_instance.IsProductMail()),
        "IsVariableExpiredDay": bool(excel_instance.IsVariableExpiredDay()),
        "ExpiredDay": convert_int(excel_instance.ExpiredDay(), password),
        "Sender": convert_string(excel_instance.Sender(), password),
        "Comment": convert_string(excel_instance.Comment(), password),
    }

def dump_TacticArenaSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Order": convert_int(excel_instance.Order(), password),
        "Repeat": convert_int(excel_instance.Repeat(), password),
        "AttackerFrom": excel_instance.AttackerFrom(),
        "AttackerUserArenaGroup": convert_int(excel_instance.AttackerUserArenaGroup(), password),
        "AttackerUserArenaRank": convert_int(excel_instance.AttackerUserArenaRank(), password),
        "AttackerPresetGroupId": convert_int(excel_instance.AttackerPresetGroupId(), password),
        "AttackerStrikerNum": convert_int(excel_instance.AttackerStrikerNum(), password),
        "AttackerSpecialNum": convert_int(excel_instance.AttackerSpecialNum(), password),
        "DefenderFrom": excel_instance.DefenderFrom(),
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
        "OverrideStreetAdaptation": excel_instance.OverrideStreetAdaptation(),
        "OverrideOutdoorAdaptation": excel_instance.OverrideOutdoorAdaptation(),
        "OverrideIndoorAdaptation": excel_instance.OverrideIndoorAdaptation(),
        "ApplyOverrideAdaptation": bool(excel_instance.ApplyOverrideAdaptation()),
        "OverrideFavorLevel": convert_int(excel_instance.OverrideFavorLevel(), password),
        "ApplyOverrideFavorLevel": bool(excel_instance.ApplyOverrideFavorLevel()),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "FixedCharacter": [convert_int(excel_instance.FixedCharacter(j), password) for j in range(excel_instance.FixedCharacterLength())],
    }

def dump_TacticSimulatorSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
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
        "Furniture": excel_instance.Furniture(),
        "None_": excel_instance.None_(),
    }

def dump_TranscendenceRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CostCurrencyType": excel_instance.CostCurrencyType(),
        "CostCurrencyAmount": convert_int(excel_instance.CostCurrencyAmount(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_VoiceSkillUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_string(excel_instance.Name(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_WeekDungeonFindGiftRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
        "RewardParcelProbability": [convert_int(excel_instance.RewardParcelProbability(j), password) for j in range(excel_instance.RewardParcelProbabilityLength())],
        "DropItemModelPrefabPath": [convert_string(excel_instance.DropItemModelPrefabPath(j), password) for j in range(excel_instance.DropItemModelPrefabPathLength())],
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
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_AcademyLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "PrefabPath": convert_string(excel_instance.PrefabPath(), password),
        "IconImagePath": convert_string(excel_instance.IconImagePath(), password),
        "OpenCondition": [excel_instance.OpenCondition(j) for j in range(excel_instance.OpenConditionLength())],
        "OpenConditionCount": [convert_int(excel_instance.OpenConditionCount(j), password) for j in range(excel_instance.OpenConditionCountLength())],
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "OpenTeacherRank": convert_int(excel_instance.OpenTeacherRank(), password),
    }

def dump_AcademyLocationRankExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Rank": convert_int(excel_instance.Rank(), password),
        "RankExp": convert_int(excel_instance.RankExp(), password),
        "TotalExp": convert_int(excel_instance.TotalExp(), password),
    }

def dump_AcademyMessangerExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MessageGroupId": convert_int(excel_instance.MessageGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MessageCondition": excel_instance.MessageCondition(),
        "ConditionValue": convert_int(excel_instance.ConditionValue(), password),
        "PreConditionGroupId": convert_int(excel_instance.PreConditionGroupId(), password),
        "PreConditionFavorScheduleId": convert_int(excel_instance.PreConditionFavorScheduleId(), password),
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleId(), password),
        "NextGroupId": convert_int(excel_instance.NextGroupId(), password),
        "FeedbackTimeMillisec": convert_int(excel_instance.FeedbackTimeMillisec(), password),
        "MessageType": excel_instance.MessageType(),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "MessageKR": convert_string(excel_instance.MessageKR(), password),
        "MessageJP": convert_string(excel_instance.MessageJP(), password),
        "MessageTH": convert_string(excel_instance.MessageTH(), password),
        "MessageTW": convert_string(excel_instance.MessageTW(), password),
        "MessageEN": convert_string(excel_instance.MessageEN(), password),
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
        "ExtraRewardParcelType": [excel_instance.ExtraRewardParcelType(j) for j in range(excel_instance.ExtraRewardParcelTypeLength())],
        "ExtraRewardParcelId": [convert_int(excel_instance.ExtraRewardParcelId(j), password) for j in range(excel_instance.ExtraRewardParcelIdLength())],
        "ExtraRewardAmount": [convert_int(excel_instance.ExtraRewardAmount(j), password) for j in range(excel_instance.ExtraRewardAmountLength())],
        "ExtraRewardProb": [convert_int(excel_instance.ExtraRewardProb(j), password) for j in range(excel_instance.ExtraRewardProbLength())],
        "IsExtraRewardDisplayed": [bool(excel_instance.IsExtraRewardDisplayed(j)) for j in range(excel_instance.IsExtraRewardDisplayedLength())],
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
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
        "StudentVisitProb": [convert_int(excel_instance.StudentVisitProb(j), password) for j in range(excel_instance.StudentVisitProbLength())],
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
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

def dump_AccountLevelRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_AlertPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CheckConfirmAble": bool(excel_instance.CheckConfirmAble()),
        "SystemPopupTitle": convert_uint(excel_instance.SystemPopupTitle(), password),
        "SystemPopupDescription": convert_uint(excel_instance.SystemPopupDescription(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescription(), password),
        "PopupType": excel_instance.PopupType(),
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
        "ArenaSeasonId": convert_int(excel_instance.ArenaSeasonId(), password),
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
        "ExceptionCharacterRarities": [excel_instance.ExceptionCharacterRarities(j) for j in range(excel_instance.ExceptionCharacterRaritiesLength())],
        "ExceptionMainCharacterIds": [convert_int(excel_instance.ExceptionMainCharacterIds(j), password) for j in range(excel_instance.ExceptionMainCharacterIdsLength())],
        "ExceptionSupportCharacterIds": [convert_int(excel_instance.ExceptionSupportCharacterIds(j), password) for j in range(excel_instance.ExceptionSupportCharacterIdsLength())],
        "ExceptionTSSIds": [convert_int(excel_instance.ExceptionTSSIds(j), password) for j in range(excel_instance.ExceptionTSSIdsLength())],
    }

def dump_ArenaRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ArenaRewardType": excel_instance.ArenaRewardType(),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "RankIconPath": convert_string(excel_instance.RankIconPath(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_ArenaSeasonCloseRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_ArenaSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDate(), password),
        "SeasonEndDate": convert_string(excel_instance.SeasonEndDate(), password),
        "SeasonGroupLimit": convert_int(excel_instance.SeasonGroupLimit(), password),
        "PrevSeasonId": convert_int(excel_instance.PrevSeasonId(), password),
        "InformationGroupId": convert_int(excel_instance.InformationGroupId(), password),
    }

def dump_AssistEchelonTypeConvertExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Contents": excel_instance.Contents(),
        "ConvertTo": excel_instance.ConvertTo(),
    }

def dump_AssistRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RewardType": excel_instance.RewardType(),
        "EchelonType": excel_instance.EchelonType(),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_AssistSlotExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SlotId": convert_int(excel_instance.SlotId(), password),
        "EchelonType": excel_instance.EchelonType(),
        "SlotNumber": convert_int(excel_instance.SlotNumber(), password),
        "AssistTermRewardPeriodFromSec": convert_int(excel_instance.AssistTermRewardPeriodFromSec(), password),
        "AssistRewardLimit": convert_int(excel_instance.AssistRewardLimit(), password),
        "AssistRentRewardDailyMaxCount": convert_int(excel_instance.AssistRentRewardDailyMaxCount(), password),
        "AssistRentalFeeAmount": convert_int(excel_instance.AssistRentalFeeAmount(), password),
        "AssistRentalFeeAmountStranger": convert_int(excel_instance.AssistRentalFeeAmountStranger(), password),
    }

def dump_AttendanceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Type": excel_instance.Type(),
        "CountdownPrefab": convert_string(excel_instance.CountdownPrefab(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "TargetGroup": excel_instance.TargetGroup(),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimit(), password),
        "Title": convert_string(excel_instance.Title(), password),
        "InfomationLocalizeCode": convert_string(excel_instance.InfomationLocalizeCode(), password),
        "CountRule": excel_instance.CountRule(),
        "CountReset": excel_instance.CountReset(),
        "BookSize": convert_int(excel_instance.BookSize(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDate(), password),
        "MailType": excel_instance.MailType(),
        "DialogCategory": excel_instance.DialogCategory(),
        "TitleImagePath": convert_string(excel_instance.TitleImagePath(), password),
        "DecorationImagePath": convert_string(excel_instance.DecorationImagePath(), password),
        "DecorationGarlandImagePath": convert_string(excel_instance.DecorationGarlandImagePath(), password),
    }

def dump_AttendanceRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "AttendanceId": convert_int(excel_instance.AttendanceId(), password),
        "Day": convert_int(excel_instance.Day(), password),
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardId": [convert_int(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_AudioAnimatorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerNameHash": convert_uint(excel_instance.ControllerNameHash(), password),
        "VoiceNamePrefix": convert_string(excel_instance.VoiceNamePrefix(), password),
        "StateNameHash": convert_uint(excel_instance.StateNameHash(), password),
        "StateName": convert_string(excel_instance.StateName(), password),
        "IgnoreInterruptDelay": bool(excel_instance.IgnoreInterruptDelay()),
        "IgnoreInterruptPlay": bool(excel_instance.IgnoreInterruptPlay()),
        "IgnoreVelocity": bool(excel_instance.IgnoreVelocity()),
        "Volume": convert_float(excel_instance.Volume(), password),
        "Delay": convert_float(excel_instance.Delay(), password),
        "RandomPitchMin": convert_int(excel_instance.RandomPitchMin(), password),
        "RandomPitchMax": convert_int(excel_instance.RandomPitchMax(), password),
        "AudioPriority": convert_int(excel_instance.AudioPriority(), password),
        "AudioClipPath": [convert_string(excel_instance.AudioClipPath(j), password) for j in range(excel_instance.AudioClipPathLength())],
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_BattleLevelFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiff(), password),
        "DamageRate": convert_int(excel_instance.DamageRate(), password),
    }

def dump_BattlePassExpLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BattlePassId": convert_int(excel_instance.BattlePassId(), password),
        "LimitStartTime": convert_string(excel_instance.LimitStartTime(), password),
        "LimitEndTime": convert_string(excel_instance.LimitEndTime(), password),
        "ExpLimitAmount": convert_int(excel_instance.ExpLimitAmount(), password),
    }

def dump_BattlePassFlavorTextExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "TextGroup": convert_int(excel_instance.TextGroup(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "Sort": convert_int(excel_instance.Sort(), password),
    }

def dump_BattlePassInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FreeRewardGroupID": convert_int(excel_instance.FreeRewardGroupID(), password),
        "PurchaseRewardGroupID": convert_int(excel_instance.PurchaseRewardGroupID(), password),
        "NormalProductGroupID": convert_int(excel_instance.NormalProductGroupID(), password),
        "PremiumProductGroupID": convert_int(excel_instance.PremiumProductGroupID(), password),
        "DiscountPremiumProductGroupID": convert_int(excel_instance.DiscountPremiumProductGroupID(), password),
        "NextLvNeedExp": convert_int(excel_instance.NextLvNeedExp(), password),
        "PassLvUpGoodsID": convert_int(excel_instance.PassLvUpGoodsID(), password),
        "BuyPremiumLvUpAmount": convert_int(excel_instance.BuyPremiumLvUpAmount(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "VideoId": [convert_int(excel_instance.VideoId(j), password) for j in range(excel_instance.VideoIdLength())],
        "FlavorTextGroupID": convert_int(excel_instance.FlavorTextGroupID(), password),
        "ExclusiveRewardID": convert_int(excel_instance.ExclusiveRewardID(), password),
        "ExclusiveEmblemID": convert_int(excel_instance.ExclusiveEmblemID(), password),
        "PassExpLocalizeEtcId": convert_uint(excel_instance.PassExpLocalizeEtcId(), password),
        "LobbyBannerPath": convert_string(excel_instance.LobbyBannerPath(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPath(), password),
        "PurchaseStepProductImagePath": convert_string(excel_instance.PurchaseStepProductImagePath(), password),
    }

def dump_BattlePassLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BattlePassId": convert_int(excel_instance.BattlePassId(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "IsPickUpReward": bool(excel_instance.IsPickUpReward()),
    }

def dump_BattlePassMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BattlePassId": convert_int(excel_instance.BattlePassId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Category": excel_instance.Category(),
        "PreMissionId": [convert_int(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": excel_instance.ResetType(),
        "ToastDisplayType": excel_instance.ToastDisplayType(),
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": excel_instance.CompleteConditionType(),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [excel_instance.CompleteConditionParameterTag(j) for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "BattlePassExpAmount": convert_int(excel_instance.BattlePassExpAmount(), password),
    }

def dump_BattlePassRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelUniqueId": convert_int(excel_instance.RewardParcelUniqueId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_BGMExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Nation": [excel_instance.Nation(j) for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "Volume": [convert_float(excel_instance.Volume(j), password) for j in range(excel_instance.VolumeLength())],
        "LoopStartTime": [convert_float(excel_instance.LoopStartTime(j), password) for j in range(excel_instance.LoopStartTimeLength())],
        "LoopEndTime": [convert_float(excel_instance.LoopEndTime(j), password) for j in range(excel_instance.LoopEndTimeLength())],
        "LoopTranstionTime": [convert_float(excel_instance.LoopTranstionTime(j), password) for j in range(excel_instance.LoopTranstionTimeLength())],
        "LoopOffsetTime": [convert_float(excel_instance.LoopOffsetTime(j), password) for j in range(excel_instance.LoopOffsetTimeLength())],
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

def dump_BGM_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupBGMId": convert_int(excel_instance.GroupBGMId(), password),
        "BGMIdKr": convert_int(excel_instance.BGMIdKr(), password),
        "BGMIdJp": convert_int(excel_instance.BGMIdJp(), password),
        "BGMIdTh": convert_int(excel_instance.BGMIdTh(), password),
        "BGMIdTw": convert_int(excel_instance.BGMIdTw(), password),
        "BGMIdEn": convert_int(excel_instance.BGMIdEn(), password),
    }

def dump_BossExternalBTExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ExternalBTId": convert_int(excel_instance.ExternalBTId(), password),
        "AIPhase": convert_int(excel_instance.AIPhase(), password),
        "ExternalBTNodeType": excel_instance.ExternalBTNodeType(),
        "ExternalBTTrigger": excel_instance.ExternalBTTrigger(),
        "TriggerArgument": convert_string(excel_instance.TriggerArgument(), password),
        "BehaviorRate": convert_int(excel_instance.BehaviorRate(), password),
        "ExternalBehavior": excel_instance.ExternalBehavior(),
        "BehaviorArgument": convert_string(excel_instance.BehaviorArgument(), password),
    }

def dump_BulletArmorDamageFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DamageFactorGroupId": convert_string(excel_instance.DamageFactorGroupId(), password),
        "BulletType": excel_instance.BulletType(),
        "ArmorType": excel_instance.ArmorType(),
        "DamageRate": convert_int(excel_instance.DamageRate(), password),
        "DamageAttribute": excel_instance.DamageAttribute(),
        "MinDamageRate": convert_int(excel_instance.MinDamageRate(), password),
        "MaxDamageRate": convert_int(excel_instance.MaxDamageRate(), password),
        "ShowHighlightFloater": bool(excel_instance.ShowHighlightFloater()),
    }

def dump_CafeInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeId(), password),
        "IsDefault": bool(excel_instance.IsDefault()),
        "OpenConditionCafeId": excel_instance.OpenConditionCafeId(),
        "OpenConditionCafeInvite": excel_instance.OpenConditionCafeInvite(),
        "SummonParcelType": excel_instance.SummonParcelType(),
        "SummonParcelId": convert_int(excel_instance.SummonParcelId(), password),
        "SummonParcelAmount": convert_int(excel_instance.SummonParcelAmount(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "SummonTicketIconPath": convert_string(excel_instance.SummonTicketIconPath(), password),
    }

def dump_CafeInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "IgnoreIfUnobtained": bool(excel_instance.IgnoreIfUnobtained()),
        "IgnoreIfUnobtainedStartDate": convert_string(excel_instance.IgnoreIfUnobtainedStartDate(), password),
        "IgnoreIfUnobtainedEndDate": convert_string(excel_instance.IgnoreIfUnobtainedEndDate(), password),
        "BubbleType": [excel_instance.BubbleType(j) for j in range(excel_instance.BubbleTypeLength())],
        "BubbleDuration": [convert_int(excel_instance.BubbleDuration(j), password) for j in range(excel_instance.BubbleDurationLength())],
        "FavorEmoticonRewardParcelType": excel_instance.FavorEmoticonRewardParcelType(),
        "FavorEmoticonRewardId": convert_int(excel_instance.FavorEmoticonRewardId(), password),
        "FavorEmoticonRewardAmount": convert_int(excel_instance.FavorEmoticonRewardAmount(), password),
        "CafeCharacterState": [convert_string(excel_instance.CafeCharacterState(j), password) for j in range(excel_instance.CafeCharacterStateLength())],
    }

def dump_CafeProductionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CafeId": convert_int(excel_instance.CafeId(), password),
        "Rank": convert_int(excel_instance.Rank(), password),
        "CafeProductionParcelType": excel_instance.CafeProductionParcelType(),
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
        "CafeVisitWeightTagBonusStep": [convert_int(excel_instance.CafeVisitWeightTagBonusStep(j), password) for j in range(excel_instance.CafeVisitWeightTagBonusStepLength())],
        "CafeVisitWeightTagBonus": [convert_int(excel_instance.CafeVisitWeightTagBonus(j), password) for j in range(excel_instance.CafeVisitWeightTagBonusLength())],
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

def dump_CampaignChapterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "NormalImagePath": convert_string(excel_instance.NormalImagePath(), password),
        "HardImagePath": convert_string(excel_instance.HardImagePath(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "PreChapterId": [convert_int(excel_instance.PreChapterId(j), password) for j in range(excel_instance.PreChapterIdLength())],
        "ChapterRewardId": convert_int(excel_instance.ChapterRewardId(), password),
        "ChapterHardRewardId": convert_int(excel_instance.ChapterHardRewardId(), password),
        "ChapterVeryHardRewardId": convert_int(excel_instance.ChapterVeryHardRewardId(), password),
        "NormalCampaignStageId": [convert_int(excel_instance.NormalCampaignStageId(j), password) for j in range(excel_instance.NormalCampaignStageIdLength())],
        "NormalExtraStageId": [convert_int(excel_instance.NormalExtraStageId(j), password) for j in range(excel_instance.NormalExtraStageIdLength())],
        "HardCampaignStageId": [convert_int(excel_instance.HardCampaignStageId(j), password) for j in range(excel_instance.HardCampaignStageIdLength())],
        "VeryHardCampaignStageId": [convert_int(excel_instance.VeryHardCampaignStageId(j), password) for j in range(excel_instance.VeryHardCampaignStageIdLength())],
        "IsTacticSkip": bool(excel_instance.IsTacticSkip()),
    }

def dump_CampaignChapterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CampaignChapterStar": convert_int(excel_instance.CampaignChapterStar(), password),
        "ChapterRewardParcelType": [excel_instance.ChapterRewardParcelType(j) for j in range(excel_instance.ChapterRewardParcelTypeLength())],
        "ChapterRewardId": [convert_int(excel_instance.ChapterRewardId(j), password) for j in range(excel_instance.ChapterRewardIdLength())],
        "ChapterRewardAmount": [convert_int(excel_instance.ChapterRewardAmount(j), password) for j in range(excel_instance.ChapterRewardAmountLength())],
    }

def dump_CampaignStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Deprecated": bool(excel_instance.Deprecated()),
        "Name": convert_string(excel_instance.Name(), password),
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "CleardScenarioId": convert_int(excel_instance.CleardScenarioId(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": excel_instance.StageEnterCostType(),
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "CampaignStageRewardId": convert_int(excel_instance.CampaignStageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "RecommandLevelGapForGuide": convert_int(excel_instance.RecommandLevelGapForGuide(), password),
        "MinEquipmentTierForGuide": [convert_int(excel_instance.MinEquipmentTierForGuide(j), password) for j in range(excel_instance.MinEquipmentTierForGuideLength())],
        "MinSkillLevelForGuide": [convert_int(excel_instance.MinSkillLevelForGuide(j), password) for j in range(excel_instance.MinSkillLevelForGuideLength())],
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "StrategyEnvironment": excel_instance.StrategyEnvironment(),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StrategySkipGroundId": convert_int(excel_instance.StrategySkipGroundId(), password),
        "ContentType": excel_instance.ContentType(),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventName(), password),
        "FirstClearFunnelMessage": convert_string(excel_instance.FirstClearFunnelMessage(), password),
        "FirstClearEventMessage": convert_string(excel_instance.FirstClearEventMessage(), password),
        "FirstStartFunnelMessage": convert_string(excel_instance.FirstStartFunnelMessage(), password),
        "TacticRewardExp": convert_int(excel_instance.TacticRewardExp(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_CampaignStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "StageRewardProb": convert_int(excel_instance.StageRewardProb(), password),
        "StageRewardParcelType": excel_instance.StageRewardParcelType(),
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
        "StrategyObjectType": excel_instance.StrategyObjectType(),
        "StrategyRewardParcelType": excel_instance.StrategyRewardParcelType(),
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
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "MoveRange": convert_int(excel_instance.MoveRange(), password),
        "AIMoveType": excel_instance.AIMoveType(),
        "Grade": excel_instance.Grade(),
        "EnvironmentType": excel_instance.EnvironmentType(),
        "Scale": convert_float(excel_instance.Scale(), password),
        "IsTacticSkip": bool(excel_instance.IsTacticSkip()),
    }

def dump_CharacterAcademyTagsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FavorTags": [excel_instance.FavorTags(j) for j in range(excel_instance.FavorTagsLength())],
        "FavorItemTags": [excel_instance.FavorItemTags(j) for j in range(excel_instance.FavorItemTagsLength())],
        "FavorItemUniqueTags": [excel_instance.FavorItemUniqueTags(j) for j in range(excel_instance.FavorItemUniqueTagsLength())],
        "ForbiddenTags": [excel_instance.ForbiddenTags(j) for j in range(excel_instance.ForbiddenTagsLength())],
        "ZoneWhiteListTags": [excel_instance.ZoneWhiteListTags(j) for j in range(excel_instance.ZoneWhiteListTagsLength())],
    }

def dump_CharacterAIExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EngageType": excel_instance.EngageType(),
        "Positioning": excel_instance.Positioning(),
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
        "TacticEntityType": excel_instance.TacticEntityType(),
        "CalculationValue": excel_instance.CalculationValue(),
        "MinValue": convert_int(excel_instance.MinValue(), password),
        "MaxValue": convert_int(excel_instance.MaxValue(), password),
        "LimitStartValue": [convert_int(excel_instance.LimitStartValue(j), password) for j in range(excel_instance.LimitStartValueLength())],
        "DecreaseRate": [convert_int(excel_instance.DecreaseRate(j), password) for j in range(excel_instance.DecreaseRateLength())],
    }

def dump_CharacterCombatSkinExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ResourcePath": convert_string(excel_instance.ResourcePath(), password),
    }

def dump_CharacterDialogBattlePassExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "OriginalCharacterId": convert_int(excel_instance.OriginalCharacterId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "BattlePassID": convert_int(excel_instance.BattlePassID(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "DialogCategory": excel_instance.DialogCategory(),
        "DialogCondition": excel_instance.DialogCondition(),
        "DialogConditionDetail": excel_instance.DialogConditionDetail(),
        "DialogConditionDetailValue": convert_int(excel_instance.DialogConditionDetailValue(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DialogType": excel_instance.DialogType(),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": excel_instance.CVCollectionType(),
        "UnlockBattlePassId": convert_int(excel_instance.UnlockBattlePassId(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "TeenMode": bool(excel_instance.TeenMode()),
    }

def dump_CharacterDialogEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "TargetIndex": convert_int(excel_instance.TargetIndex(), password),
        "DialogType": convert_string(excel_instance.DialogType(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "DurationAdd": convert_int(excel_instance.DurationAdd(), password),
        "HideUI": bool(excel_instance.HideUI()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": excel_instance.CVCollectionType(),
        "CVUnlockScenarioType": excel_instance.CVUnlockScenarioType(),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
        "UnlockEventSeason": convert_int(excel_instance.UnlockEventSeason(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
    }

def dump_CharacterDialogEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "OriginalCharacterId": convert_int(excel_instance.OriginalCharacterId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "EventID": convert_int(excel_instance.EventID(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "DialogCategory": excel_instance.DialogCategory(),
        "DialogCondition": excel_instance.DialogCondition(),
        "DialogConditionDetail": excel_instance.DialogConditionDetail(),
        "DialogConditionDetailValue": convert_int(excel_instance.DialogConditionDetailValue(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DialogType": excel_instance.DialogType(),
        "ActionName": convert_string(excel_instance.ActionName(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": excel_instance.CVCollectionType(),
        "CVUnlockScenarioType": excel_instance.CVUnlockScenarioType(),
        "UnlockEventSeason": convert_int(excel_instance.UnlockEventSeason(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "ScenarioCharacterShapes": excel_instance.ScenarioCharacterShapes(),
    }

def dump_CharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "DialogCategory": excel_instance.DialogCategory(),
        "DialogCondition": excel_instance.DialogCondition(),
        "Anniversary": excel_instance.Anniversary(),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DialogType": excel_instance.DialogType(),
        "ActionName": convert_string(excel_instance.ActionName(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "ApplyPosition": bool(excel_instance.ApplyPosition()),
        "PosX": convert_float(excel_instance.PosX(), password),
        "PosY": convert_float(excel_instance.PosY(), password),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "CVCollectionType": excel_instance.CVCollectionType(),
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRank(), password),
        "UnlockEquipWeapon": bool(excel_instance.UnlockEquipWeapon()),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "TeenMode": bool(excel_instance.TeenMode()),
    }

def dump_CharacterDialogSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "TLMID": convert_string(excel_instance.TLMID(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "Separate": bool(excel_instance.Separate()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
    }

def dump_CharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CostumeGroupId": convert_int(excel_instance.CostumeGroupId(), password),
        "IsPlayable": bool(excel_instance.IsPlayable()),
        "ProductionStep": excel_instance.ProductionStep(),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "ReleaseDate": convert_string(excel_instance.ReleaseDate(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDate(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDate(), password),
        "IsPlayableCharacter": bool(excel_instance.IsPlayableCharacter()),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Rarity": excel_instance.Rarity(),
        "IsNPC": bool(excel_instance.IsNPC()),
        "TacticEntityType": excel_instance.TacticEntityType(),
        "CanSurvive": bool(excel_instance.CanSurvive()),
        "IsDummy": bool(excel_instance.IsDummy()),
        "SubPartsCount": convert_int(excel_instance.SubPartsCount(), password),
        "TacticRole": convert_float(excel_instance.TacticRole(), password),
        "WeaponType": excel_instance.WeaponType(),
        "TacticRange": excel_instance.TacticRange(),
        "BulletType": excel_instance.BulletType(),
        "ArmorType": excel_instance.ArmorType(),
        "AimIKType": excel_instance.AimIKType(),
        "School": excel_instance.School(),
        "Club": excel_instance.Club(),
        "DefaultStarGrade": convert_int(excel_instance.DefaultStarGrade(), password),
        "MaxStarGrade": convert_int(excel_instance.MaxStarGrade(), password),
        "StatLevelUpType": excel_instance.StatLevelUpType(),
        "SquadType": excel_instance.SquadType(),
        "Jumpable": bool(excel_instance.Jumpable()),
        "PersonalityId": convert_int(excel_instance.PersonalityId(), password),
        "CharacterAIId": convert_int(excel_instance.CharacterAIId(), password),
        "ExternalBTId": convert_int(excel_instance.ExternalBTId(), password),
        "MainCombatStyleId": convert_int(excel_instance.MainCombatStyleId(), password),
        "CombatStyleIndex": convert_int(excel_instance.CombatStyleIndex(), password),
        "UseRepStyleOnCharacterGrowth": bool(excel_instance.UseRepStyleOnCharacterGrowth()),
        "ScenarioCharacter": convert_string(excel_instance.ScenarioCharacter(), password),
        "SpawnTemplateId": convert_uint(excel_instance.SpawnTemplateId(), password),
        "FavorLevelupType": convert_int(excel_instance.FavorLevelupType(), password),
        "EquipmentSlot": [excel_instance.EquipmentSlot(j) for j in range(excel_instance.EquipmentSlotLength())],
        "WeaponLocalizeId": convert_uint(excel_instance.WeaponLocalizeId(), password),
        "DisplayEnemyInfo": bool(excel_instance.DisplayEnemyInfo()),
        "BodyRadius": convert_int(excel_instance.BodyRadius(), password),
        "RandomEffectRadius": convert_int(excel_instance.RandomEffectRadius(), password),
        "TargetGuideScale": convert_float(excel_instance.TargetGuideScale(), password),
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
        "IgnoreObstacle": bool(excel_instance.IgnoreObstacle()),
        "IsAirUnit": bool(excel_instance.IsAirUnit()),
        "AirUnitHeight": convert_int(excel_instance.AirUnitHeight(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
        "SecretStoneItemId": convert_int(excel_instance.SecretStoneItemId(), password),
        "SecretStoneItemAmount": convert_int(excel_instance.SecretStoneItemAmount(), password),
        "CharacterPieceItemId": convert_int(excel_instance.CharacterPieceItemId(), password),
        "CharacterPieceItemAmount": convert_int(excel_instance.CharacterPieceItemAmount(), password),
        "CombineRecipeId": convert_int(excel_instance.CombineRecipeId(), password),
    }

def dump_CharacterGearExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "StatLevelUpType": excel_instance.StatLevelUpType(),
        "Tier": convert_int(excel_instance.Tier(), password),
        "NextTierEquipment": convert_int(excel_instance.NextTierEquipment(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "OpenFavorLevel": convert_int(excel_instance.OpenFavorLevel(), password),
        "MaxLevel": convert_int(excel_instance.MaxLevel(), password),
        "LearnSkillSlot": convert_string(excel_instance.LearnSkillSlot(), password),
        "StatType": [excel_instance.StatType(j) for j in range(excel_instance.StatTypeLength())],
        "MinStatValue": [convert_int(excel_instance.MinStatValue(j), password) for j in range(excel_instance.MinStatValueLength())],
        "MaxStatValue": [convert_int(excel_instance.MaxStatValue(j), password) for j in range(excel_instance.MaxStatValueLength())],
        "Icon": convert_string(excel_instance.Icon(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
    }

def dump_CharacterGearLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "TierLevelExp": [convert_int(excel_instance.TierLevelExp(j), password) for j in range(excel_instance.TierLevelExpLength())],
        "TotalExp": [convert_int(excel_instance.TotalExp(j), password) for j in range(excel_instance.TotalExpLength())],
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

def dump_CharacterPotentialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "PotentialStatGroupId": convert_int(excel_instance.PotentialStatGroupId(), password),
        "PotentialStatBonusRateType": excel_instance.PotentialStatBonusRateType(),
        "IsUnnecessaryStat": bool(excel_instance.IsUnnecessaryStat()),
    }

def dump_CharacterPotentialRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RequirePotentialStatType": [excel_instance.RequirePotentialStatType(j) for j in range(excel_instance.RequirePotentialStatTypeLength())],
        "RequirePotentialStatLevel": [convert_int(excel_instance.RequirePotentialStatLevel(j), password) for j in range(excel_instance.RequirePotentialStatLevelLength())],
        "RewardParcelType": excel_instance.RewardParcelType(),
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
        "NormalSkillGroupId": [convert_string(excel_instance.NormalSkillGroupId(j), password) for j in range(excel_instance.NormalSkillGroupIdLength())],
        "NormalSkillTimeLineIndex": [convert_int(excel_instance.NormalSkillTimeLineIndex(j), password) for j in range(excel_instance.NormalSkillTimeLineIndexLength())],
        "SelectExSkillActionSkillSlot": convert_int(excel_instance.SelectExSkillActionSkillSlot(), password),
        "ExSkillGroupId": [convert_string(excel_instance.ExSkillGroupId(j), password) for j in range(excel_instance.ExSkillGroupIdLength())],
        "ExSkillCutInTimeLineIndex": [convert_string(excel_instance.ExSkillCutInTimeLineIndex(j), password) for j in range(excel_instance.ExSkillCutInTimeLineIndexLength())],
        "ExSkillLevelTimeLineIndex": [convert_string(excel_instance.ExSkillLevelTimeLineIndex(j), password) for j in range(excel_instance.ExSkillLevelTimeLineIndexLength())],
        "PublicSkillGroupId": [convert_string(excel_instance.PublicSkillGroupId(j), password) for j in range(excel_instance.PublicSkillGroupIdLength())],
        "PublicSkillTimeLineIndex": [convert_int(excel_instance.PublicSkillTimeLineIndex(j), password) for j in range(excel_instance.PublicSkillTimeLineIndexLength())],
        "PassiveSkillGroupId": [convert_string(excel_instance.PassiveSkillGroupId(j), password) for j in range(excel_instance.PassiveSkillGroupIdLength())],
        "LeaderSkillGroupId": [convert_string(excel_instance.LeaderSkillGroupId(j), password) for j in range(excel_instance.LeaderSkillGroupIdLength())],
        "ExtraPassiveSkillGroupId": [convert_string(excel_instance.ExtraPassiveSkillGroupId(j), password) for j in range(excel_instance.ExtraPassiveSkillGroupIdLength())],
        "HiddenPassiveSkillGroupId": [convert_string(excel_instance.HiddenPassiveSkillGroupId(j), password) for j in range(excel_instance.HiddenPassiveSkillGroupIdLength())],
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
        "EnhanceChemicalRate": convert_int(excel_instance.EnhanceChemicalRate(), password),
        "EnhanceSiegeRate": convert_int(excel_instance.EnhanceSiegeRate(), password),
        "EnhanceNormalRate": convert_int(excel_instance.EnhanceNormalRate(), password),
        "EnhanceLightArmorRate": convert_int(excel_instance.EnhanceLightArmorRate(), password),
        "EnhanceHeavyArmorRate": convert_int(excel_instance.EnhanceHeavyArmorRate(), password),
        "EnhanceUnarmedRate": convert_int(excel_instance.EnhanceUnarmedRate(), password),
        "EnhanceElasticArmorRate": convert_int(excel_instance.EnhanceElasticArmorRate(), password),
        "EnhanceCompositeArmorRate": convert_int(excel_instance.EnhanceCompositeArmorRate(), password),
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
        "EnhanceBasicsDamageRate": convert_int(excel_instance.EnhanceBasicsDamageRate(), password),
        "ReduceBasicsDamagedRate": convert_int(excel_instance.ReduceBasicsDamagedRate(), password),
        "EnhanceWeakDamageRate": convert_int(excel_instance.EnhanceWeakDamageRate(), password),
        "ReduceWeakDamagedRate": convert_int(excel_instance.ReduceWeakDamagedRate(), password),
        "WeakDamagedRatio": convert_int(excel_instance.WeakDamagedRatio(), password),
        "EffectiveDamagedRatio": convert_int(excel_instance.EffectiveDamagedRatio(), password),
        "NormalDamagedRatio": convert_int(excel_instance.NormalDamagedRatio(), password),
        "ResistDamagedRatio": convert_int(excel_instance.ResistDamagedRatio(), password),
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
        "StreetBattleAdaptation": excel_instance.StreetBattleAdaptation(),
        "OutdoorBattleAdaptation": excel_instance.OutdoorBattleAdaptation(),
        "IndoorBattleAdaptation": excel_instance.IndoorBattleAdaptation(),
        "RegenCost": convert_int(excel_instance.RegenCost(), password),
    }

def dump_CharacterStatLimitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TacticEntityType": excel_instance.TacticEntityType(),
        "StatType": excel_instance.StatType(),
        "StatMinValue": convert_int(excel_instance.StatMinValue(), password),
        "StatMaxValue": convert_int(excel_instance.StatMaxValue(), password),
        "StatRatioMinValue": convert_int(excel_instance.StatRatioMinValue(), password),
        "StatRatioMaxValue": convert_int(excel_instance.StatRatioMaxValue(), password),
    }

def dump_CharacterStatsDetailExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DetailShowStats": [excel_instance.DetailShowStats(j) for j in range(excel_instance.DetailShowStatsLength())],
        "IsStatsPercent": [bool(excel_instance.IsStatsPercent(j)) for j in range(excel_instance.IsStatsPercentLength())],
    }

def dump_CharacterStatsTransExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TransSupportStats": excel_instance.TransSupportStats(),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
        "TransSupportStatsFactor": convert_int(excel_instance.TransSupportStatsFactor(), password),
        "StatTransType": excel_instance.StatTransType(),
    }

def dump_CharacterTranscendenceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "MaxFavorLevel": [convert_int(excel_instance.MaxFavorLevel(j), password) for j in range(excel_instance.MaxFavorLevelLength())],
        "StatBonusRateAttack": [convert_int(excel_instance.StatBonusRateAttack(j), password) for j in range(excel_instance.StatBonusRateAttackLength())],
        "StatBonusRateHP": [convert_int(excel_instance.StatBonusRateHP(j), password) for j in range(excel_instance.StatBonusRateHPLength())],
        "StatBonusRateHeal": [convert_int(excel_instance.StatBonusRateHeal(j), password) for j in range(excel_instance.StatBonusRateHealLength())],
        "RecipeId": [convert_int(excel_instance.RecipeId(j), password) for j in range(excel_instance.RecipeIdLength())],
        "SkillSlotA": [convert_string(excel_instance.SkillSlotA(j), password) for j in range(excel_instance.SkillSlotALength())],
        "SkillSlotB": [convert_string(excel_instance.SkillSlotB(j), password) for j in range(excel_instance.SkillSlotBLength())],
        "SkillSlotC": [convert_string(excel_instance.SkillSlotC(j), password) for j in range(excel_instance.SkillSlotCLength())],
        "MaxlevelStar": [convert_int(excel_instance.MaxlevelStar(j), password) for j in range(excel_instance.MaxlevelStarLength())],
    }

def dump_CharacterVictoryInteractionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "InteractionId": convert_int(excel_instance.InteractionId(), password),
        "CostumeId01": convert_int(excel_instance.CostumeId01(), password),
        "PositionIndex01": convert_int(excel_instance.PositionIndex01(), password),
        "VictoryStartAnimationPath01": convert_string(excel_instance.VictoryStartAnimationPath01(), password),
        "VictoryEndAnimationPath01": convert_string(excel_instance.VictoryEndAnimationPath01(), password),
        "VoiceEvent01": excel_instance.VoiceEvent01(),
        "CostumeId02": convert_int(excel_instance.CostumeId02(), password),
        "PositionIndex02": convert_int(excel_instance.PositionIndex02(), password),
        "VictoryStartAnimationPath02": convert_string(excel_instance.VictoryStartAnimationPath02(), password),
        "VictoryEndAnimationPath02": convert_string(excel_instance.VictoryEndAnimationPath02(), password),
        "VoiceEvent02": excel_instance.VoiceEvent02(),
        "CostumeId03": convert_int(excel_instance.CostumeId03(), password),
        "PositionIndex03": convert_int(excel_instance.PositionIndex03(), password),
        "VictoryStartAnimationPath03": convert_string(excel_instance.VictoryStartAnimationPath03(), password),
        "VictoryEndAnimationPath03": convert_string(excel_instance.VictoryEndAnimationPath03(), password),
        "VoiceEvent03": excel_instance.VoiceEvent03(),
        "CostumeId04": convert_int(excel_instance.CostumeId04(), password),
        "PositionIndex04": convert_int(excel_instance.PositionIndex04(), password),
        "VictoryStartAnimationPath04": convert_string(excel_instance.VictoryStartAnimationPath04(), password),
        "VictoryEndAnimationPath04": convert_string(excel_instance.VictoryEndAnimationPath04(), password),
        "VoiceEvent04": excel_instance.VoiceEvent04(),
        "CostumeId05": convert_int(excel_instance.CostumeId05(), password),
        "PositionIndex05": convert_int(excel_instance.PositionIndex05(), password),
        "VictoryStartAnimationPath05": convert_string(excel_instance.VictoryStartAnimationPath05(), password),
        "VictoryEndAnimationPath05": convert_string(excel_instance.VictoryEndAnimationPath05(), password),
        "VoiceEvent05": excel_instance.VoiceEvent05(),
        "CostumeId06": convert_int(excel_instance.CostumeId06(), password),
        "PositionIndex06": convert_int(excel_instance.PositionIndex06(), password),
        "VictoryStartAnimationPath06": convert_string(excel_instance.VictoryStartAnimationPath06(), password),
        "VictoryEndAnimationPath06": convert_string(excel_instance.VictoryEndAnimationPath06(), password),
        "VoiceEvent06": excel_instance.VoiceEvent06(),
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
        "CVCollectionType": excel_instance.CVCollectionType(),
        "UnlockFavorRank": convert_int(excel_instance.UnlockFavorRank(), password),
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "Nation": [excel_instance.Nation(j) for j in range(excel_instance.NationLength())],
        "Volume": [convert_float(excel_instance.Volume(j), password) for j in range(excel_instance.VolumeLength())],
        "Delay": [convert_float(excel_instance.Delay(j), password) for j in range(excel_instance.DelayLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
    }

def dump_CharacterVoiceSubtitleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LocalizeCVGroup": convert_string(excel_instance.LocalizeCVGroup(), password),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupId(), password),
        "TLMID": convert_string(excel_instance.TLMID(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "Separate": bool(excel_instance.Separate()),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
    }

def dump_CharacterWeaponExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "SetRecipe": convert_int(excel_instance.SetRecipe(), password),
        "StatLevelUpType": excel_instance.StatLevelUpType(),
        "AttackPower": convert_int(excel_instance.AttackPower(), password),
        "AttackPower100": convert_int(excel_instance.AttackPower100(), password),
        "MaxHP": convert_int(excel_instance.MaxHP(), password),
        "MaxHP100": convert_int(excel_instance.MaxHP100(), password),
        "HealPower": convert_int(excel_instance.HealPower(), password),
        "HealPower100": convert_int(excel_instance.HealPower100(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
        "Unlock": [bool(excel_instance.Unlock(j)) for j in range(excel_instance.UnlockLength())],
        "RecipeId": [convert_int(excel_instance.RecipeId(j), password) for j in range(excel_instance.RecipeIdLength())],
        "MaxLevel": [convert_int(excel_instance.MaxLevel(j), password) for j in range(excel_instance.MaxLevelLength())],
        "LearnSkillSlot": [convert_string(excel_instance.LearnSkillSlot(j), password) for j in range(excel_instance.LearnSkillSlotLength())],
        "StatType": [excel_instance.StatType(j) for j in range(excel_instance.StatTypeLength())],
        "StatValue": [convert_int(excel_instance.StatValue(j), password) for j in range(excel_instance.StatValueLength())],
    }

def dump_CharacterWeaponExpBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeaponType": excel_instance.WeaponType(),
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

def dump_ClanChattingEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TabGroupId": convert_int(excel_instance.TabGroupId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
        "ImagePathTh": convert_string(excel_instance.ImagePathTh(), password),
        "ImagePathTw": convert_string(excel_instance.ImagePathTw(), password),
        "ImagePathEn": convert_string(excel_instance.ImagePathEn(), password),
    }

def dump_ClanRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ClanRewardType": excel_instance.ClanRewardType(),
        "EchelonType": excel_instance.EchelonType(),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_CombatEmojiExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "EmojiEvent": excel_instance.EmojiEvent(),
        "OrderOfPriority": convert_int(excel_instance.OrderOfPriority(), password),
        "EmojiDuration": bool(excel_instance.EmojiDuration()),
        "EmojiReversal": bool(excel_instance.EmojiReversal()),
        "EmojiTurnOn": bool(excel_instance.EmojiTurnOn()),
        "ShowEmojiDelay": convert_int(excel_instance.ShowEmojiDelay(), password),
        "ShowDefaultBG": bool(excel_instance.ShowDefaultBG()),
    }

def dump_ConquestCalculateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CalculateConditionParcelType": excel_instance.CalculateConditionParcelType(),
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
        "ErosionType": excel_instance.ErosionType(),
        "Phase": convert_int(excel_instance.Phase(), password),
        "PhaseAlarm": bool(excel_instance.PhaseAlarm()),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "PhaseStartConditionType": [excel_instance.PhaseStartConditionType(j) for j in range(excel_instance.PhaseStartConditionTypeLength())],
        "PhaseStartConditionParameter": [convert_string(excel_instance.PhaseStartConditionParameter(j), password) for j in range(excel_instance.PhaseStartConditionParameterLength())],
        "PhaseBeforeExposeConditionType": [excel_instance.PhaseBeforeExposeConditionType(j) for j in range(excel_instance.PhaseBeforeExposeConditionTypeLength())],
        "PhaseBeforeExposeConditionParameter": [convert_string(excel_instance.PhaseBeforeExposeConditionParameter(j), password) for j in range(excel_instance.PhaseBeforeExposeConditionParameterLength())],
        "ErosionBattleConditionParcelType": excel_instance.ErosionBattleConditionParcelType(),
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
        "ConquestEventType": excel_instance.ConquestEventType(),
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
        "School": [excel_instance.School(j) for j in range(excel_instance.SchoolLength())],
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "BonusParcelType": [excel_instance.BonusParcelType(j) for j in range(excel_instance.BonusParcelTypeLength())],
        "BonusId": [convert_int(excel_instance.BonusId(j), password) for j in range(excel_instance.BonusIdLength())],
        "BonusCharacterCount1": [convert_int(excel_instance.BonusCharacterCount1(j), password) for j in range(excel_instance.BonusCharacterCount1Length())],
        "BonusPercentage1": [convert_int(excel_instance.BonusPercentage1(j), password) for j in range(excel_instance.BonusPercentage1Length())],
        "BonusCharacterCount2": [convert_int(excel_instance.BonusCharacterCount2(j), password) for j in range(excel_instance.BonusCharacterCount2Length())],
        "BonusPercentage2": [convert_int(excel_instance.BonusPercentage2(j), password) for j in range(excel_instance.BonusPercentage2Length())],
        "BonusCharacterCount3": [convert_int(excel_instance.BonusCharacterCount3(j), password) for j in range(excel_instance.BonusCharacterCount3Length())],
        "BonusPercentage3": [convert_int(excel_instance.BonusPercentage3(j), password) for j in range(excel_instance.BonusPercentage3Length())],
    }

def dump_ConquestGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConquestBuffId": convert_int(excel_instance.ConquestBuffId(), password),
        "School": [excel_instance.School(j) for j in range(excel_instance.SchoolLength())],
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
    }

def dump_ConquestMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "MapDifficulty": excel_instance.MapDifficulty(),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "ConquestMap": convert_string(excel_instance.ConquestMap(), password),
        "StepEnterScenarioGroupId": convert_int(excel_instance.StepEnterScenarioGroupId(), password),
        "StepOpenConditionType": [excel_instance.StepOpenConditionType(j) for j in range(excel_instance.StepOpenConditionTypeLength())],
        "StepOpenConditionParameter": [convert_string(excel_instance.StepOpenConditionParameter(j), password) for j in range(excel_instance.StepOpenConditionParameterLength())],
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
        "ConquestObjectType": excel_instance.ConquestObjectType(),
        "Key": convert_uint(excel_instance.Key(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ConquestRewardParcelType": excel_instance.ConquestRewardParcelType(),
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
        "Group": excel_instance.Group(),
        "ProgressResource": convert_string(excel_instance.ProgressResource(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "ProgressLocalizeCode": convert_string(excel_instance.ProgressLocalizeCode(), password),
    }

def dump_ConquestRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
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
        "TileType": excel_instance.TileType(),
        "NotMapFog": bool(excel_instance.NotMapFog()),
        "GroupBonusId": convert_int(excel_instance.GroupBonusId(), password),
        "ConquestCostType": excel_instance.ConquestCostType(),
        "ConquestCostId": convert_int(excel_instance.ConquestCostId(), password),
        "ConquestCostAmount": convert_int(excel_instance.ConquestCostAmount(), password),
        "ManageCostType": excel_instance.ManageCostType(),
        "ManageCostId": convert_int(excel_instance.ManageCostId(), password),
        "ManageCostAmount": convert_int(excel_instance.ManageCostAmount(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardId(), password),
        "MassErosionId": convert_int(excel_instance.MassErosionId(), password),
        "Upgrade2CostType": excel_instance.Upgrade2CostType(),
        "Upgrade2CostId": convert_int(excel_instance.Upgrade2CostId(), password),
        "Upgrade2CostAmount": convert_int(excel_instance.Upgrade2CostAmount(), password),
        "Upgrade3CostType": excel_instance.Upgrade3CostType(),
        "Upgrade3CostId": convert_int(excel_instance.Upgrade3CostId(), password),
        "Upgrade3CostAmount": convert_int(excel_instance.Upgrade3CostAmount(), password),
    }

def dump_ConquestUnexpectedEventExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UnexpectedEventConditionType": excel_instance.UnexpectedEventConditionType(),
        "UnexpectedEventConditionUniqueId": convert_int(excel_instance.UnexpectedEventConditionUniqueId(), password),
        "UnexpectedEventConditionAmount": convert_int(excel_instance.UnexpectedEventConditionAmount(), password),
        "UnexpectedEventOccurDailyLimitCount": convert_int(excel_instance.UnexpectedEventOccurDailyLimitCount(), password),
        "UnitCountPerStep": convert_int(excel_instance.UnitCountPerStep(), password),
        "UnexpectedEventPrefab": [convert_string(excel_instance.UnexpectedEventPrefab(j), password) for j in range(excel_instance.UnexpectedEventPrefabLength())],
        "UnexpectedEventUnitId": [convert_int(excel_instance.UnexpectedEventUnitId(j), password) for j in range(excel_instance.UnexpectedEventUnitIdLength())],
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
        "EnemyType": excel_instance.EnemyType(),
        "Team": excel_instance.Team(),
        "UnitGroup": convert_int(excel_instance.UnitGroup(), password),
        "PrevUnitGroup": convert_int(excel_instance.PrevUnitGroup(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoal": [excel_instance.StarGoal(j) for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "GroupBuffId": convert_int(excel_instance.GroupBuffId(), password),
        "StageEnterCostType": excel_instance.StageEnterCostType(),
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "ManageEchelonStageEnterCostType": excel_instance.ManageEchelonStageEnterCostType(),
        "ManageEchelonStageEnterCostId": convert_int(excel_instance.ManageEchelonStageEnterCostId(), password),
        "ManageEchelonStageEnterCostAmount": convert_int(excel_instance.ManageEchelonStageEnterCostAmount(), password),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupId(), password),
        "ClearScenarioGroupId": convert_int(excel_instance.ClearScenarioGroupId(), password),
        "ConquestRewardId": convert_int(excel_instance.ConquestRewardId(), password),
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "TacticRewardExp": convert_int(excel_instance.TacticRewardExp(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_ContentEnterCostReduceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EnterCostReduceGroupId": convert_int(excel_instance.EnterCostReduceGroupId(), password),
        "ContentType": excel_instance.ContentType(),
        "StageId": convert_int(excel_instance.StageId(), password),
        "ReduceEnterCostType": excel_instance.ReduceEnterCostType(),
        "ReduceEnterCostId": convert_int(excel_instance.ReduceEnterCostId(), password),
        "ReduceAmount": convert_int(excel_instance.ReduceAmount(), password),
    }

def dump_ContentsFeverExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ConditionContent": excel_instance.ConditionContent(),
        "SkillFeverCheckCondition": excel_instance.SkillFeverCheckCondition(),
        "SkillCostFever": convert_int(excel_instance.SkillCostFever(), password),
        "FeverStartTime": convert_int(excel_instance.FeverStartTime(), password),
        "FeverDurationTime": convert_int(excel_instance.FeverDurationTime(), password),
    }

def dump_ContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ContentType": excel_instance.ContentType(),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescription(), password),
        "PopupType": excel_instance.PopupType(),
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_ContentsScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.Id(), password),
        "LocalizeId": convert_uint(excel_instance.LocalizeId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ScenarioContentType": excel_instance.ScenarioContentType(),
        "ScenarioGroupId": [convert_int(excel_instance.ScenarioGroupId(j), password) for j in range(excel_instance.ScenarioGroupIdLength())],
    }

def dump_ContentsShortcutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ContentType": excel_instance.ContentType(),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ScenarioModeType": excel_instance.ScenarioModeType(),
        "ScenarioModeSubType": excel_instance.ScenarioModeSubType(),
        "ScenarioModeVolume": convert_int(excel_instance.ScenarioModeVolume(), password),
        "ScenarioModeChapter": convert_int(excel_instance.ScenarioModeChapter(), password),
        "ShortcutOpenTime": convert_string(excel_instance.ShortcutOpenTime(), password),
        "ShortcutCloseTime": convert_string(excel_instance.ShortcutCloseTime(), password),
        "ConditionContentId": convert_int(excel_instance.ConditionContentId(), password),
        "ConquestMapDifficulty": excel_instance.ConquestMapDifficulty(),
        "ConquestStepIndex": convert_int(excel_instance.ConquestStepIndex(), password),
        "ShortcutContentId": convert_int(excel_instance.ShortcutContentId(), password),
        "ShortcutUIName": [convert_string(excel_instance.ShortcutUIName(j), password) for j in range(excel_instance.ShortcutUINameLength())],
        "Localize": convert_string(excel_instance.Localize(), password),
    }

def dump_ContentTargetGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TargetGroup": excel_instance.TargetGroup(),
        "AccountType": [excel_instance.AccountType(j) for j in range(excel_instance.AccountTypeLength())],
    }

def dump_CostumeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeGroupId": convert_int(excel_instance.CostumeGroupId(), password),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "IsDefault": bool(excel_instance.IsDefault()),
        "CollectionVisible": bool(excel_instance.CollectionVisible()),
        "ReleaseDate": convert_string(excel_instance.ReleaseDate(), password),
        "CollectionVisibleStartDate": convert_string(excel_instance.CollectionVisibleStartDate(), password),
        "CollectionVisibleEndDate": convert_string(excel_instance.CollectionVisibleEndDate(), password),
        "Rarity": excel_instance.Rarity(),
        "CharacterSkillListGroupId": convert_int(excel_instance.CharacterSkillListGroupId(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceName(), password),
        "SpineResourceNameDiorama": convert_string(excel_instance.SpineResourceNameDiorama(), password),
        "SpineResourceNameDioramaForFormConversion": [convert_string(excel_instance.SpineResourceNameDioramaForFormConversion(j), password) for j in range(excel_instance.SpineResourceNameDioramaForFormConversionLength())],
        "EntityMaterialType": excel_instance.EntityMaterialType(),
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabName(), password),
        "AnimatorName": convert_string(excel_instance.AnimatorName(), password),
        "CafeModelPrefabName": convert_string(excel_instance.CafeModelPrefabName(), password),
        "EchelonModelPrefabName": convert_string(excel_instance.EchelonModelPrefabName(), password),
        "StrategyModelPrefabName": convert_string(excel_instance.StrategyModelPrefabName(), password),
        "TextureDir": convert_string(excel_instance.TextureDir(), password),
        "CollectionTexturePath": convert_string(excel_instance.CollectionTexturePath(), password),
        "CollectionBGTexturePath": convert_string(excel_instance.CollectionBGTexturePath(), password),
        "CombatStyleTexturePath": convert_string(excel_instance.CombatStyleTexturePath(), password),
        "UseObjectHPBAR": bool(excel_instance.UseObjectHPBAR()),
        "TextureBoss": convert_string(excel_instance.TextureBoss(), password),
        "TextureSkillCard": [convert_string(excel_instance.TextureSkillCard(j), password) for j in range(excel_instance.TextureSkillCardLength())],
        "InformationPacel": convert_string(excel_instance.InformationPacel(), password),
        "AnimationSSR": convert_string(excel_instance.AnimationSSR(), password),
        "EnterStrategyAnimationName": convert_string(excel_instance.EnterStrategyAnimationName(), password),
        "AnimationValidator": bool(excel_instance.AnimationValidator()),
        "CharacterVoiceGroupId": convert_int(excel_instance.CharacterVoiceGroupId(), password),
        "ShowObjectHpStatus": bool(excel_instance.ShowObjectHpStatus()),
    }

def dump_CurrencyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CurrencyType": excel_instance.CurrencyType(),
        "CurrencyName": convert_string(excel_instance.CurrencyName(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "Rarity": excel_instance.Rarity(),
        "AutoChargeMsc": convert_int(excel_instance.AutoChargeMsc(), password),
        "AutoChargeAmount": convert_int(excel_instance.AutoChargeAmount(), password),
        "CurrencyOverChargeType": excel_instance.CurrencyOverChargeType(),
        "CurrencyAdditionalChargeType": excel_instance.CurrencyAdditionalChargeType(),
        "ChargeLimit": convert_int(excel_instance.ChargeLimit(), password),
        "OverChargeLimit": convert_int(excel_instance.OverChargeLimit(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "DailyRefillType": excel_instance.DailyRefillType(),
        "DailyRefillAmount": convert_int(excel_instance.DailyRefillAmount(), password),
        "DailyRefillTime": [convert_int(excel_instance.DailyRefillTime(j), password) for j in range(excel_instance.DailyRefillTimeLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTime(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateIn(), password),
        "ExpiryChangeParcelType": excel_instance.ExpiryChangeParcelType(),
        "ExpiryChangeId": convert_int(excel_instance.ExpiryChangeId(), password),
        "ExpiryChangeAmount": convert_int(excel_instance.ExpiryChangeAmount(), password),
        "ResetType": excel_instance.ResetType(),
        "ResetAmount": convert_int(excel_instance.ResetAmount(), password),
    }

def dump_DuplicateBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ItemCategory": excel_instance.ItemCategory(),
        "ItemId": convert_int(excel_instance.ItemId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_EchelonConstraintExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsWhiteList": bool(excel_instance.IsWhiteList()),
        "CharacterId": [convert_int(excel_instance.CharacterId(j), password) for j in range(excel_instance.CharacterIdLength())],
        "PersonalityId": [convert_int(excel_instance.PersonalityId(j), password) for j in range(excel_instance.PersonalityIdLength())],
        "WeaponType": excel_instance.WeaponType(),
        "School": excel_instance.School(),
        "Club": excel_instance.Club(),
        "Role": convert_float(excel_instance.Role(), password),
    }

def dump_EliminateRaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "RankStartTw": convert_int(excel_instance.RankStartTw(), password),
        "RankEndTw": convert_int(excel_instance.RankEndTw(), password),
        "RankStartAsia": convert_int(excel_instance.RankStartAsia(), password),
        "RankEndAsia": convert_int(excel_instance.RankEndAsia(), password),
        "RankStartNa": convert_int(excel_instance.RankStartNa(), password),
        "RankEndNa": convert_int(excel_instance.RankEndNa(), password),
        "RankStartGlobal": convert_int(excel_instance.RankStartGlobal(), password),
        "RankEndGlobal": convert_int(excel_instance.RankEndGlobal(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelUniqueName": [convert_string(excel_instance.RewardParcelUniqueName(j), password) for j in range(excel_instance.RewardParcelUniqueNameLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EliminateRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "SeasonDisplay": convert_int(excel_instance.SeasonDisplay(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartData(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndData(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "LobbyTableBGPath": convert_string(excel_instance.LobbyTableBGPath(), password),
        "LobbyScreenBGPath": convert_string(excel_instance.LobbyScreenBGPath(), password),
        "OpenRaidBossGroup01": convert_string(excel_instance.OpenRaidBossGroup01(), password),
        "OpenRaidBossGroup02": convert_string(excel_instance.OpenRaidBossGroup02(), password),
        "OpenRaidBossGroup03": convert_string(excel_instance.OpenRaidBossGroup03(), password),
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauage(), password),
        "StackedSeasonRewardGauge": [convert_int(excel_instance.StackedSeasonRewardGauge(j), password) for j in range(excel_instance.StackedSeasonRewardGaugeLength())],
        "SeasonRewardId": [convert_int(excel_instance.SeasonRewardId(j), password) for j in range(excel_instance.SeasonRewardIdLength())],
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
        "RaidEnterCostType": excel_instance.RaidEnterCostType(),
        "RaidEnterCostId": convert_int(excel_instance.RaidEnterCostId(), password),
        "RaidEnterCostAmount": convert_int(excel_instance.RaidEnterCostAmount(), password),
        "BossSpinePath": convert_string(excel_instance.BossSpinePath(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterId(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "Difficulty": excel_instance.Difficulty(),
        "IsOpen": bool(excel_instance.IsOpen()),
        "MaxPlayerCount": convert_int(excel_instance.MaxPlayerCount(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTime(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RaidBossGroupType": excel_instance.RaidBossGroupType(),
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLine(), password),
        "TacticEnvironment": excel_instance.TacticEnvironment(),
        "DefaultClearScore": convert_int(excel_instance.DefaultClearScore(), password),
        "MaximumScore": convert_int(excel_instance.MaximumScore(), password),
        "PerSecondMinusScore": convert_int(excel_instance.PerSecondMinusScore(), password),
        "HPPercentScore": convert_int(excel_instance.HPPercentScore(), password),
        "MinimumAcquisitionScore": convert_int(excel_instance.MinimumAcquisitionScore(), password),
        "MaximumAcquisitionScore": convert_int(excel_instance.MaximumAcquisitionScore(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKey(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_EliminateRaidStageLimitedRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LimitedRewardId": convert_int(excel_instance.LimitedRewardId(), password),
        "LimitedRewardParcelType": [excel_instance.LimitedRewardParcelType(j) for j in range(excel_instance.LimitedRewardParcelTypeLength())],
        "LimitedRewardParcelUniqueId": [convert_int(excel_instance.LimitedRewardParcelUniqueId(j), password) for j in range(excel_instance.LimitedRewardParcelUniqueIdLength())],
        "LimitedRewardAmount": [convert_int(excel_instance.LimitedRewardAmount(j), password) for j in range(excel_instance.LimitedRewardAmountLength())],
    }

def dump_EliminateRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": excel_instance.ClearStageRewardParcelType(),
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_EliminateRaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_int(excel_instance.SeasonRewardId(), password),
        "SeasonRewardParcelType": [excel_instance.SeasonRewardParcelType(j) for j in range(excel_instance.SeasonRewardParcelTypeLength())],
        "SeasonRewardParcelUniqueId": [convert_int(excel_instance.SeasonRewardParcelUniqueId(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueIdLength())],
        "SeasonRewardAmount": [convert_int(excel_instance.SeasonRewardAmount(j), password) for j in range(excel_instance.SeasonRewardAmountLength())],
    }

def dump_EmblemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Category": excel_instance.Category(),
        "Rarity": excel_instance.Rarity(),
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
        "EmblemBGPathTh": convert_string(excel_instance.EmblemBGPathTh(), password),
        "EmblemBGPathTw": convert_string(excel_instance.EmblemBGPathTw(), password),
        "EmblemBGPathEn": convert_string(excel_instance.EmblemBGPathEn(), password),
        "EmblemEffectPath": convert_string(excel_instance.EmblemEffectPath(), password),
        "DisplayType": excel_instance.DisplayType(),
        "DisplayStartDate": convert_string(excel_instance.DisplayStartDate(), password),
        "DisplayEndDate": convert_string(excel_instance.DisplayEndDate(), password),
        "DislpayFavorLevel": convert_int(excel_instance.DislpayFavorLevel(), password),
        "CheckPassType": excel_instance.CheckPassType(),
        "EmblemParameter": convert_int(excel_instance.EmblemParameter(), password),
        "CheckPassCount": convert_int(excel_instance.CheckPassCount(), password),
    }

def dump_EquipmentChangePieceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EquipmentId": convert_int(excel_instance.EquipmentId(), password),
        "ChangeEquipmentId": convert_int(excel_instance.ChangeEquipmentId(), password),
        "ChangeAmount": convert_int(excel_instance.ChangeAmount(), password),
    }

def dump_EquipmentExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EquipmentCategory": excel_instance.EquipmentCategory(),
        "Rarity": excel_instance.Rarity(),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "Wear": bool(excel_instance.Wear()),
        "MaxLevel": convert_int(excel_instance.MaxLevel(), password),
        "RecipeId": convert_int(excel_instance.RecipeId(), password),
        "TierInit": convert_int(excel_instance.TierInit(), password),
        "NextTierEquipment": convert_int(excel_instance.NextTierEquipment(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "ImageName": convert_string(excel_instance.ImageName(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQuality(), password),
        "ShopCategory": [convert_float(excel_instance.ShopCategory(j), password) for j in range(excel_instance.ShopCategoryLength())],
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeId(), password),
        "RedirectItemId": convert_int(excel_instance.RedirectItemId(), password),
    }

def dump_EquipmentLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "TierLevelExp": [convert_int(excel_instance.TierLevelExp(j), password) for j in range(excel_instance.TierLevelExpLength())],
        "TotalExp": [convert_int(excel_instance.TotalExp(j), password) for j in range(excel_instance.TotalExpLength())],
    }

def dump_EquipmentStatExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EquipmentId": convert_int(excel_instance.EquipmentId(), password),
        "StatLevelUpType": excel_instance.StatLevelUpType(),
        "StatType": [excel_instance.StatType(j) for j in range(excel_instance.StatTypeLength())],
        "MinStat": [convert_int(excel_instance.MinStat(j), password) for j in range(excel_instance.MinStatLength())],
        "MaxStat": [convert_int(excel_instance.MaxStat(j), password) for j in range(excel_instance.MaxStatLength())],
        "LevelUpInsertLimit": convert_int(excel_instance.LevelUpInsertLimit(), password),
        "LevelUpFeedExp": convert_int(excel_instance.LevelUpFeedExp(), password),
        "LevelUpFeedCostCurrency": excel_instance.LevelUpFeedCostCurrency(),
        "LevelUpFeedCostAmount": convert_int(excel_instance.LevelUpFeedCostAmount(), password),
        "EquipmentCategory": excel_instance.EquipmentCategory(),
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
        "GoodsId": [convert_int(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
    }

def dump_EventContentBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentBuffId": convert_int(excel_instance.EventContentBuffId(), password),
        "IsBuff": bool(excel_instance.IsBuff()),
        "CharacterTag": excel_instance.CharacterTag(),
        "EnumType": excel_instance.EnumType(),
        "EnumTypeValue": [convert_string(excel_instance.EnumTypeValue(j), password) for j in range(excel_instance.EnumTypeValueLength())],
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
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
    }

def dump_EventContentCardShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Rarity": excel_instance.Rarity(),
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "CardGroupId": convert_int(excel_instance.CardGroupId(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbWeight1": convert_int(excel_instance.ProbWeight1(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentCardShopModifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabName(), password),
    }

def dump_EventContentChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ChangeCount": convert_int(excel_instance.ChangeCount(), password),
        "IsLast": bool(excel_instance.IsLast()),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "ChangeCostType": excel_instance.ChangeCostType(),
        "ChangeCostId": convert_int(excel_instance.ChangeCostId(), password),
        "ChangeCostAmount": convert_int(excel_instance.ChangeCostAmount(), password),
    }

def dump_EventContentChangeScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ChangeType": excel_instance.ChangeType(),
        "ChangeCount": convert_int(excel_instance.ChangeCount(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
    }

def dump_EventContentCharacterBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "EventContentItemType": [excel_instance.EventContentItemType(j) for j in range(excel_instance.EventContentItemTypeLength())],
        "BonusPercentage": [convert_int(excel_instance.BonusPercentage(j), password) for j in range(excel_instance.BonusPercentageLength())],
    }

def dump_EventContentClueExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ClueId": convert_int(excel_instance.ClueId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "SlotClueImagePath": convert_string(excel_instance.SlotClueImagePath(), password),
        "ClueImagePath": convert_string(excel_instance.ClueImagePath(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
        "HintUse": bool(excel_instance.HintUse()),
        "Hintlocalizeid": convert_uint(excel_instance.Hintlocalizeid(), password),
    }

def dump_EventContentClueSearchExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TitleLocalize": convert_uint(excel_instance.TitleLocalize(), password),
        "UsePrefabName": convert_string(excel_instance.UsePrefabName(), password),
        "ClueBGImagePath": convert_string(excel_instance.ClueBGImagePath(), password),
    }

def dump_EventContentClueSearchRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentClueSearchRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "IsLoop": bool(excel_instance.IsLoop()),
        "TargetImagePath": convert_string(excel_instance.TargetImagePath(), password),
        "Localizeld": convert_uint(excel_instance.Localizeld(), password),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "ClueSlotNumber": [convert_int(excel_instance.ClueSlotNumber(j), password) for j in range(excel_instance.ClueSlotNumberLength())],
        "ClueId": [convert_int(excel_instance.ClueId(j), password) for j in range(excel_instance.ClueIdLength())],
        "ClueCostAmount": [convert_int(excel_instance.ClueCostAmount(j), password) for j in range(excel_instance.ClueCostAmountLength())],
        "HintlocalizeId": convert_uint(excel_instance.HintlocalizeId(), password),
        "ClearlocalizeId": convert_uint(excel_instance.ClearlocalizeId(), password),
        "ClearPageImagePath": convert_string(excel_instance.ClearPageImagePath(), password),
    }

def dump_EventContentCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "UnlockConditionType": excel_instance.UnlockConditionType(),
        "UnlockConditionParameter": [convert_int(excel_instance.UnlockConditionParameter(j), password) for j in range(excel_instance.UnlockConditionParameterLength())],
        "MultipleConditionCheckType": excel_instance.MultipleConditionCheckType(),
        "UnlockConditionCount": convert_int(excel_instance.UnlockConditionCount(), password),
        "IsObject": bool(excel_instance.IsObject()),
        "IsObjectOnFullResource": bool(excel_instance.IsObjectOnFullResource()),
        "IsHorizon": bool(excel_instance.IsHorizon()),
        "EmblemResource": convert_string(excel_instance.EmblemResource(), password),
        "ThumbResource": convert_string(excel_instance.ThumbResource(), password),
        "FullResource": convert_string(excel_instance.FullResource(), password),
        "Decoration": convert_string(excel_instance.Decoration(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "SubNameLocalizeCodeId": convert_string(excel_instance.SubNameLocalizeCodeId(), password),
    }

def dump_EventContentConcentrationCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CardId": convert_int(excel_instance.CardId(), password),
        "Rarity": excel_instance.Rarity(),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
    }

def dump_EventContentConcentrationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "MaxCardPairCount": convert_int(excel_instance.MaxCardPairCount(), password),
        "MaxCardOpenCount": convert_int(excel_instance.MaxCardOpenCount(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRound(), password),
        "CardBoardPrefabs": convert_string(excel_instance.CardBoardPrefabs(), password),
        "BackImagePath": convert_string(excel_instance.BackImagePath(), password),
    }

def dump_EventContentConcentrationRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ConcentrationRewardType": excel_instance.ConcentrationRewardType(),
        "Rarity": excel_instance.Rarity(),
        "Round": convert_int(excel_instance.Round(), password),
        "IsLoop": bool(excel_instance.IsLoop()),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentConcentrationVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "VoiceCondition": excel_instance.VoiceCondition(),
        "VoiceClip": convert_uint(excel_instance.VoiceClip(), password),
    }

def dump_EventContentCurrencyItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentItemType": excel_instance.EventContentItemType(),
        "ItemUniqueId": convert_int(excel_instance.ItemUniqueId(), password),
        "UseShortCutContentType": convert_string(excel_instance.UseShortCutContentType(), password),
    }

def dump_EventContentDebuffRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventStageId": convert_int(excel_instance.EventStageId(), password),
        "EventContentItemType": excel_instance.EventContentItemType(),
        "RewardPercentage": convert_int(excel_instance.RewardPercentage(), password),
    }

def dump_EventContentDiceRaceEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentDiceRaceResultType": excel_instance.EventContentDiceRaceResultType(),
        "IsDiceResult": bool(excel_instance.IsDiceResult()),
        "AniClip": convert_string(excel_instance.AniClip(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
    }

def dump_EventContentDiceRaceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DiceCostGoodsId": convert_int(excel_instance.DiceCostGoodsId(), password),
        "SkipableLap": convert_int(excel_instance.SkipableLap(), password),
        "DiceRacePawnPrefab": convert_string(excel_instance.DiceRacePawnPrefab(), password),
        "IsUsingFixedDice": bool(excel_instance.IsUsingFixedDice()),
        "FixedDiceIcon": [convert_string(excel_instance.FixedDiceIcon(j), password) for j in range(excel_instance.FixedDiceIconLength())],
        "DiceRaceEventType": [convert_string(excel_instance.DiceRaceEventType(j), password) for j in range(excel_instance.DiceRaceEventTypeLength())],
    }

def dump_EventContentDiceRaceNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "NodeId": convert_int(excel_instance.NodeId(), password),
        "EventContentDiceRaceNodeType": excel_instance.EventContentDiceRaceNodeType(),
        "MoveForwardTypeArg": convert_int(excel_instance.MoveForwardTypeArg(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_EventContentDiceRaceProbExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentDiceRaceResultType": excel_instance.EventContentDiceRaceResultType(),
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
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentFortuneGachaExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FortuneGachaGroupId": convert_int(excel_instance.FortuneGachaGroupId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "NameImagePath": convert_string(excel_instance.NameImagePath(), password),
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
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentLobbyMenuExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentType": excel_instance.EventContentType(),
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
        "ScheduleEventPointCostParcelType": excel_instance.ScheduleEventPointCostParcelType(),
        "ScheduleEventPointCostParcelId": convert_int(excel_instance.ScheduleEventPointCostParcelId(), password),
        "ScheduleEventPointCostParcelAmount": convert_int(excel_instance.ScheduleEventPointCostParcelAmount(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
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
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "LocationRank": convert_int(excel_instance.LocationRank(), password),
        "FavorExp": convert_int(excel_instance.FavorExp(), password),
        "SecretStoneAmount": convert_int(excel_instance.SecretStoneAmount(), password),
        "SecretStoneProb": convert_int(excel_instance.SecretStoneProb(), password),
        "ExtraFavorExp": convert_int(excel_instance.ExtraFavorExp(), password),
        "ExtraFavorExpProb": convert_int(excel_instance.ExtraFavorExpProb(), password),
        "ExtraRewardParcelType": [excel_instance.ExtraRewardParcelType(j) for j in range(excel_instance.ExtraRewardParcelTypeLength())],
        "ExtraRewardParcelId": [convert_int(excel_instance.ExtraRewardParcelId(j), password) for j in range(excel_instance.ExtraRewardParcelIdLength())],
        "ExtraRewardAmount": [convert_int(excel_instance.ExtraRewardAmount(j), password) for j in range(excel_instance.ExtraRewardAmountLength())],
        "ExtraRewardProb": [convert_int(excel_instance.ExtraRewardProb(j), password) for j in range(excel_instance.ExtraRewardProbLength())],
        "IsExtraRewardDisplayed": [bool(excel_instance.IsExtraRewardDisplayed(j)) for j in range(excel_instance.IsExtraRewardDisplayedLength())],
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_EventContentMeetupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ConditionScenarioGroupId": convert_int(excel_instance.ConditionScenarioGroupId(), password),
        "ConditionType": excel_instance.ConditionType(),
        "ConditionParameter": [convert_int(excel_instance.ConditionParameter(j), password) for j in range(excel_instance.ConditionParameterLength())],
        "ConditionPrintType": excel_instance.ConditionPrintType(),
    }

def dump_EventContentMeetupInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CostParcelType": excel_instance.CostParcelType(),
        "CostId": convert_int(excel_instance.CostId(), password),
        "CostAmount": convert_int(excel_instance.CostAmount(), password),
    }

def dump_EventContentMiniEventShortCutExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "ShorcutContentType": excel_instance.ShorcutContentType(),
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
        "Category": excel_instance.Category(),
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": excel_instance.ResetType(),
        "ToastDisplayType": excel_instance.ToastDisplayType(),
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "TargetGroup": excel_instance.TargetGroup(),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": excel_instance.CompleteConditionType(),
        "IsCompleteExtensionTime": bool(excel_instance.IsCompleteExtensionTime()),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [excel_instance.CompleteConditionParameterTag(j) for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "CompleteConditionMissionId": [convert_int(excel_instance.CompleteConditionMissionId(j), password) for j in range(excel_instance.CompleteConditionMissionIdLength())],
        "CompleteConditionMissionCount": convert_int(excel_instance.CompleteConditionMissionCount(), password),
        "MissionRewardParcelType": [excel_instance.MissionRewardParcelType(j) for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
        "ConditionRewardParcelType": [excel_instance.ConditionRewardParcelType(j) for j in range(excel_instance.ConditionRewardParcelTypeLength())],
        "ConditionRewardParcelId": [convert_int(excel_instance.ConditionRewardParcelId(j), password) for j in range(excel_instance.ConditionRewardParcelIdLength())],
        "ConditionRewardAmount": [convert_int(excel_instance.ConditionRewardAmount(j), password) for j in range(excel_instance.ConditionRewardAmountLength())],
    }

def dump_EventContentNotifyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "EventNotifyType": excel_instance.EventNotifyType(),
        "EventTargetType": excel_instance.EventTargetType(),
        "ShortcutEventTargetType": excel_instance.ShortcutEventTargetType(),
        "IsShortcutEnable": bool(excel_instance.IsShortcutEnable()),
    }

def dump_EventContentPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "IsPcBuild": bool(excel_instance.IsPcBuild()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_string(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_string(excel_instance.GuideText(), password),
    }

def dump_EventContentScenarioExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ReturnScenarioPlay": bool(excel_instance.ReturnScenarioPlay()),
        "ReplayDisplayGroup": convert_int(excel_instance.ReplayDisplayGroup(), password),
        "Order": convert_int(excel_instance.Order(), password),
        "RecollectionNumber": convert_int(excel_instance.RecollectionNumber(), password),
        "IsRecollection": bool(excel_instance.IsRecollection()),
        "IsMeetup": bool(excel_instance.IsMeetup()),
        "IsOmnibus": bool(excel_instance.IsOmnibus()),
        "ScenarioGroupId": [convert_int(excel_instance.ScenarioGroupId(j), password) for j in range(excel_instance.ScenarioGroupIdLength())],
        "ScenarioConditionType": excel_instance.ScenarioConditionType(),
        "ConditionAmount": convert_int(excel_instance.ConditionAmount(), password),
        "ConditionEventContentId": convert_int(excel_instance.ConditionEventContentId(), password),
        "ClearedScenarioGroupId": convert_int(excel_instance.ClearedScenarioGroupId(), password),
        "RecollectionSummaryLocalizeScenarioId": convert_uint(excel_instance.RecollectionSummaryLocalizeScenarioId(), password),
        "RecollectionResource": convert_string(excel_instance.RecollectionResource(), password),
        "IsRecollectionHorizon": bool(excel_instance.IsRecollectionHorizon()),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardId": [convert_int(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_EventContentSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "OriginalEventContentId": convert_int(excel_instance.OriginalEventContentId(), password),
        "IsReturn": bool(excel_instance.IsReturn()),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentType": excel_instance.EventContentType(),
        "OpenConditionContent": excel_instance.OpenConditionContent(),
        "EventDisplay": bool(excel_instance.EventDisplay()),
        "IconOrder": convert_int(excel_instance.IconOrder(), password),
        "SubEventType": excel_instance.SubEventType(),
        "SubEvent": bool(excel_instance.SubEvent()),
        "EventItemId": convert_int(excel_instance.EventItemId(), password),
        "MainEventId": convert_int(excel_instance.MainEventId(), password),
        "EventChangeOpenCondition": convert_int(excel_instance.EventChangeOpenCondition(), password),
        "BeforehandExposedTime": convert_string(excel_instance.BeforehandExposedTime(), password),
        "EventContentOpenTime": convert_string(excel_instance.EventContentOpenTime(), password),
        "EventContentCloseNoteTime": convert_string(excel_instance.EventContentCloseNoteTime(), password),
        "EventContentCloseTime": convert_string(excel_instance.EventContentCloseTime(), password),
        "ExtensionTime": convert_string(excel_instance.ExtensionTime(), password),
        "MainIconParcelPath": convert_string(excel_instance.MainIconParcelPath(), password),
        "SubIconParcelPath": convert_string(excel_instance.SubIconParcelPath(), password),
        "BeforehandBgImagePath": convert_string(excel_instance.BeforehandBgImagePath(), password),
        "MinigamePrologScenarioGroupId": convert_int(excel_instance.MinigamePrologScenarioGroupId(), password),
        "BeforehandScenarioGroupId": [convert_int(excel_instance.BeforehandScenarioGroupId(j), password) for j in range(excel_instance.BeforehandScenarioGroupIdLength())],
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
        "EventContentReleaseType": excel_instance.EventContentReleaseType(),
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
        "GoodsId": [convert_int(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": excel_instance.PurchaseCountResetType(),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "RestrictBuyWhenInventoryFull": bool(excel_instance.RestrictBuyWhenInventoryFull()),
    }

def dump_EventContentShopInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "LocalizeCode": convert_uint(excel_instance.LocalizeCode(), password),
        "CostParcelType": [excel_instance.CostParcelType(j) for j in range(excel_instance.CostParcelTypeLength())],
        "CostParcelId": [convert_int(excel_instance.CostParcelId(j), password) for j in range(excel_instance.CostParcelIdLength())],
        "IsRefresh": bool(excel_instance.IsRefresh()),
        "IsSoldOutDimmed": bool(excel_instance.IsSoldOutDimmed()),
        "AutoRefreshCoolTime": convert_int(excel_instance.AutoRefreshCoolTime(), password),
        "RefreshAbleCount": convert_int(excel_instance.RefreshAbleCount(), password),
        "GoodsId": [convert_int(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
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
        "ProductUpdateTime": convert_string(excel_instance.ProductUpdateTime(), password),
    }

def dump_EventContentSpecialOperationsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "PointItemId": convert_int(excel_instance.PointItemId(), password),
    }

def dump_EventContentSpineDialogOffsetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentType": excel_instance.EventContentType(),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "SpineOffsetX": convert_float(excel_instance.SpineOffsetX(), password),
        "SpineOffsetY": convert_float(excel_instance.SpineOffsetY(), password),
        "DialogOffsetX": convert_float(excel_instance.DialogOffsetX(), password),
        "DialogOffsetY": convert_float(excel_instance.DialogOffsetY(), password),
    }

def dump_EventContentSpineDisplayPeriodExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DialogCategory": excel_instance.DialogCategory(),
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "ShowPeriodFrom": convert_string(excel_instance.ShowPeriodFrom(), password),
        "ShowPeriodTo": convert_string(excel_instance.ShowPeriodTo(), password),
        "ShowWorldRaidConditionIDFrom": convert_int(excel_instance.ShowWorldRaidConditionIDFrom(), password),
        "ShowWorldRaidConditionIDTo": convert_int(excel_instance.ShowWorldRaidConditionIDTo(), password),
    }

def dump_EventContentSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescription(), password),
        "PopupType": excel_instance.PopupType(),
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_EventContentStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "StageDifficulty": excel_instance.StageDifficulty(),
        "StageNumber": convert_string(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "OpenDate": convert_int(excel_instance.OpenDate(), password),
        "OpenEventPoint": convert_int(excel_instance.OpenEventPoint(), password),
        "OpenConditionScenarioPermanentSubEventId": convert_int(excel_instance.OpenConditionScenarioPermanentSubEventId(), password),
        "PrevStageSubEventId": convert_int(excel_instance.PrevStageSubEventId(), password),
        "OpenConditionScenarioId": convert_int(excel_instance.OpenConditionScenarioId(), password),
        "OpenConditionContentType": excel_instance.OpenConditionContentType(),
        "OpenConditionContentId": convert_int(excel_instance.OpenConditionContentId(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": excel_instance.StageEnterCostType(),
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "StageEnterEchelonCount": convert_int(excel_instance.StageEnterEchelonCount(), password),
        "StarConditionTacticRankSCount": convert_int(excel_instance.StarConditionTacticRankSCount(), password),
        "StarConditionTurnCount": convert_int(excel_instance.StarConditionTurnCount(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StrategyMap": convert_string(excel_instance.StrategyMap(), password),
        "StrategyMapBG": convert_string(excel_instance.StrategyMapBG(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardId(), password),
        "MaxTurn": convert_int(excel_instance.MaxTurn(), password),
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "StrategyEnvironment": excel_instance.StrategyEnvironment(),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "ContentType": excel_instance.ContentType(),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "InstantClear": bool(excel_instance.InstantClear()),
        "BuffContentId": convert_int(excel_instance.BuffContentId(), password),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "ChallengeDisplay": bool(excel_instance.ChallengeDisplay()),
        "StarGoal": [excel_instance.StarGoal(j) for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattle()),
        "StageHint": convert_uint(excel_instance.StageHint(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_EventContentStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_EventContentStageTotalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "RequiredEventItemAmount": convert_int(excel_instance.RequiredEventItemAmount(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_EventContentTreasureCellRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeCodeID": convert_string(excel_instance.LocalizeCodeID(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
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
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
        "CellUnderImagePath": convert_string(excel_instance.CellUnderImagePath(), password),
        "TreasureSmallImagePath": convert_string(excel_instance.TreasureSmallImagePath(), password),
        "TreasureSizeIconPath": convert_string(excel_instance.TreasureSizeIconPath(), password),
    }

def dump_EventContentTreasureRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "TreasureRound": convert_int(excel_instance.TreasureRound(), password),
        "TreasureRoundSize": [convert_int(excel_instance.TreasureRoundSize(j), password) for j in range(excel_instance.TreasureRoundSizeLength())],
        "CellVisualSortUnstructed": bool(excel_instance.CellVisualSortUnstructed()),
        "CellCheckGoodsId": convert_int(excel_instance.CellCheckGoodsId(), password),
        "CellRewardId": convert_int(excel_instance.CellRewardId(), password),
        "RewardID": [convert_int(excel_instance.RewardID(j), password) for j in range(excel_instance.RewardIDLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
        "TreasureCellImagePath": convert_string(excel_instance.TreasureCellImagePath(), password),
    }

def dump_EventContentZoneExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "OriginalZoneId": convert_int(excel_instance.OriginalZoneId(), password),
        "LocationId": convert_int(excel_instance.LocationId(), password),
        "LocationRank": convert_int(excel_instance.LocationRank(), password),
        "EventPointForLocationRank": convert_int(excel_instance.EventPointForLocationRank(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "StudentVisitProb": [convert_int(excel_instance.StudentVisitProb(j), password) for j in range(excel_instance.StudentVisitProbLength())],
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
        "WhiteListTags": [excel_instance.WhiteListTags(j) for j in range(excel_instance.WhiteListTagsLength())],
    }

def dump_EventContentZoneVisitRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentLocationId": convert_int(excel_instance.EventContentLocationId(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "CharacterDevName": convert_string(excel_instance.CharacterDevName(), password),
        "VisitRewardParcelType": [excel_instance.VisitRewardParcelType(j) for j in range(excel_instance.VisitRewardParcelTypeLength())],
        "VisitRewardParcelId": [convert_int(excel_instance.VisitRewardParcelId(j), password) for j in range(excel_instance.VisitRewardParcelIdLength())],
        "VisitRewardAmount": [convert_int(excel_instance.VisitRewardAmount(j), password) for j in range(excel_instance.VisitRewardAmountLength())],
        "VisitRewardProb": [convert_int(excel_instance.VisitRewardProb(j), password) for j in range(excel_instance.VisitRewardProbLength())],
    }

def dump_FarmingDungeonLocationManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FarmingDungeonLocationId": convert_int(excel_instance.FarmingDungeonLocationId(), password),
        "ContentType": excel_instance.ContentType(),
        "WeekDungeonType": convert_float(excel_instance.WeekDungeonType(), password),
        "SchoolDungeonType": excel_instance.SchoolDungeonType(),
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
        "ExpType": [convert_int(excel_instance.ExpType(j), password) for j in range(excel_instance.ExpTypeLength())],
    }

def dump_FavorLevelRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "FavorLevel": convert_int(excel_instance.FavorLevel(), password),
        "StatType": [excel_instance.StatType(j) for j in range(excel_instance.StatTypeLength())],
        "StatValue": [convert_int(excel_instance.StatValue(j), password) for j in range(excel_instance.StatValueLength())],
    }

def dump_FieldQuestGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SkipFromInteractionId": convert_int(excel_instance.SkipFromInteractionId(), password),
        "SkipToInteractionId": convert_int(excel_instance.SkipToInteractionId(), password),
        "NextSceneId": convert_int(excel_instance.NextSceneId(), password),
        "SkipResultUI": bool(excel_instance.SkipResultUI()),
    }

def dump_FieldSNSInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "InteractionGroupId": convert_int(excel_instance.InteractionGroupId(), password),
        "SNSStateType": excel_instance.SNSStateType(),
        "StateLocalizeKey": convert_uint(excel_instance.StateLocalizeKey(), password),
        "DescLocalizeKey": convert_uint(excel_instance.DescLocalizeKey(), password),
    }

def dump_FieldSNSPostExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupInteractionId": convert_int(excel_instance.GroupInteractionId(), password),
        "PostType": excel_instance.PostType(),
        "SNSPostId": convert_int(excel_instance.SNSPostId(), password),
        "IsSequence": bool(excel_instance.IsSequence()),
        "Order": convert_int(excel_instance.Order(), password),
        "DelayTime": convert_int(excel_instance.DelayTime(), password),
        "RepostMinNum": convert_int(excel_instance.RepostMinNum(), password),
        "RepostMaxNum": convert_int(excel_instance.RepostMaxNum(), password),
        "FavorMinNum": convert_int(excel_instance.FavorMinNum(), password),
        "FavorMaxNum": convert_int(excel_instance.FavorMaxNum(), password),
    }

def dump_FieldWarpExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "CurrentSceneId": convert_int(excel_instance.CurrentSceneId(), password),
        "ResultSceneId": convert_int(excel_instance.ResultSceneId(), password),
        "ResultSceneNameKey": convert_uint(excel_instance.ResultSceneNameKey(), password),
        "ResultSceneImagePath": convert_string(excel_instance.ResultSceneImagePath(), password),
    }

def dump_FixedEchelonSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FixedEchelonID": convert_int(excel_instance.FixedEchelonID(), password),
        "EchelonSceneSkip": bool(excel_instance.EchelonSceneSkip()),
        "MainLeaderSlot": convert_int(excel_instance.MainLeaderSlot(), password),
        "MainCharacterID": [convert_int(excel_instance.MainCharacterID(j), password) for j in range(excel_instance.MainCharacterIDLength())],
        "MainLevel": [convert_int(excel_instance.MainLevel(j), password) for j in range(excel_instance.MainLevelLength())],
        "MainGrade": [convert_int(excel_instance.MainGrade(j), password) for j in range(excel_instance.MainGradeLength())],
        "MainExSkillLevel": [convert_int(excel_instance.MainExSkillLevel(j), password) for j in range(excel_instance.MainExSkillLevelLength())],
        "MainNoneExSkillLevel": [convert_int(excel_instance.MainNoneExSkillLevel(j), password) for j in range(excel_instance.MainNoneExSkillLevelLength())],
        "MainEquipment1Tier": [convert_int(excel_instance.MainEquipment1Tier(j), password) for j in range(excel_instance.MainEquipment1TierLength())],
        "MainEquipment1Level": [convert_int(excel_instance.MainEquipment1Level(j), password) for j in range(excel_instance.MainEquipment1LevelLength())],
        "MainEquipment2Tier": [convert_int(excel_instance.MainEquipment2Tier(j), password) for j in range(excel_instance.MainEquipment2TierLength())],
        "MainEquipment2Level": [convert_int(excel_instance.MainEquipment2Level(j), password) for j in range(excel_instance.MainEquipment2LevelLength())],
        "MainEquipment3Tier": [convert_int(excel_instance.MainEquipment3Tier(j), password) for j in range(excel_instance.MainEquipment3TierLength())],
        "MainEquipment3Level": [convert_int(excel_instance.MainEquipment3Level(j), password) for j in range(excel_instance.MainEquipment3LevelLength())],
        "MainCharacterWeaponGrade": [convert_int(excel_instance.MainCharacterWeaponGrade(j), password) for j in range(excel_instance.MainCharacterWeaponGradeLength())],
        "MainCharacterWeaponLevel": [convert_int(excel_instance.MainCharacterWeaponLevel(j), password) for j in range(excel_instance.MainCharacterWeaponLevelLength())],
        "MainCharacterGearTier": [convert_int(excel_instance.MainCharacterGearTier(j), password) for j in range(excel_instance.MainCharacterGearTierLength())],
        "MainCharacterGearLevel": [convert_int(excel_instance.MainCharacterGearLevel(j), password) for j in range(excel_instance.MainCharacterGearLevelLength())],
        "SupportCharacterID": [convert_int(excel_instance.SupportCharacterID(j), password) for j in range(excel_instance.SupportCharacterIDLength())],
        "SupportLevel": [convert_int(excel_instance.SupportLevel(j), password) for j in range(excel_instance.SupportLevelLength())],
        "SupportGrade": [convert_int(excel_instance.SupportGrade(j), password) for j in range(excel_instance.SupportGradeLength())],
        "SupportExSkillLevel": [convert_int(excel_instance.SupportExSkillLevel(j), password) for j in range(excel_instance.SupportExSkillLevelLength())],
        "SupportNoneExSkillLevel": [convert_int(excel_instance.SupportNoneExSkillLevel(j), password) for j in range(excel_instance.SupportNoneExSkillLevelLength())],
        "SupportEquipment1Tier": [convert_int(excel_instance.SupportEquipment1Tier(j), password) for j in range(excel_instance.SupportEquipment1TierLength())],
        "SupportEquipment1Level": [convert_int(excel_instance.SupportEquipment1Level(j), password) for j in range(excel_instance.SupportEquipment1LevelLength())],
        "SupportEquipment2Tier": [convert_int(excel_instance.SupportEquipment2Tier(j), password) for j in range(excel_instance.SupportEquipment2TierLength())],
        "SupportEquipment2Level": [convert_int(excel_instance.SupportEquipment2Level(j), password) for j in range(excel_instance.SupportEquipment2LevelLength())],
        "SupportEquipment3Tier": [convert_int(excel_instance.SupportEquipment3Tier(j), password) for j in range(excel_instance.SupportEquipment3TierLength())],
        "SupportEquipment3Level": [convert_int(excel_instance.SupportEquipment3Level(j), password) for j in range(excel_instance.SupportEquipment3LevelLength())],
        "SupportCharacterWeaponGrade": [convert_int(excel_instance.SupportCharacterWeaponGrade(j), password) for j in range(excel_instance.SupportCharacterWeaponGradeLength())],
        "SupportCharacterWeaponLevel": [convert_int(excel_instance.SupportCharacterWeaponLevel(j), password) for j in range(excel_instance.SupportCharacterWeaponLevelLength())],
        "SupportCharacterGearTier": [convert_int(excel_instance.SupportCharacterGearTier(j), password) for j in range(excel_instance.SupportCharacterGearTierLength())],
        "SupportCharacterGearLevel": [convert_int(excel_instance.SupportCharacterGearLevel(j), password) for j in range(excel_instance.SupportCharacterGearLevelLength())],
        "InteractionTSCharacterId": convert_int(excel_instance.InteractionTSCharacterId(), password),
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
        "TacticEntityType": excel_instance.TacticEntityType(),
        "FloaterOffsetPosX": convert_int(excel_instance.FloaterOffsetPosX(), password),
        "FloaterOffsetPosY": convert_int(excel_instance.FloaterOffsetPosY(), password),
        "FloaterRandomPosRangeX": convert_int(excel_instance.FloaterRandomPosRangeX(), password),
        "FloaterRandomPosRangeY": convert_int(excel_instance.FloaterRandomPosRangeY(), password),
    }

def dump_FormationLocationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupID": convert_int(excel_instance.GroupID(), password),
        "SlotZ": [convert_float(excel_instance.SlotZ(j), password) for j in range(excel_instance.SlotZLength())],
        "SlotX": [convert_float(excel_instance.SlotX(j), password) for j in range(excel_instance.SlotXLength())],
    }

def dump_FurnitureExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "Rarity": excel_instance.Rarity(),
        "Category": excel_instance.Category(),
        "SubCategory": excel_instance.SubCategory(),
        "CheckFloorDecoration": bool(excel_instance.CheckFloorDecoration()),
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
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQuality(), password),
        "FurnitureFunctionType": excel_instance.FurnitureFunctionType(),
        "FurnitureFunctionParameter": [convert_int(excel_instance.FurnitureFunctionParameter(j), password) for j in range(excel_instance.FurnitureFunctionParameterLength())],
        "VideoId": convert_int(excel_instance.VideoId(), password),
        "EventCollectionId": convert_int(excel_instance.EventCollectionId(), password),
        "FurnitureBubbleOffsetX": convert_int(excel_instance.FurnitureBubbleOffsetX(), password),
        "FurnitureBubbleOffsetY": convert_int(excel_instance.FurnitureBubbleOffsetY(), password),
        "CafeCharacterStateReq": [convert_string(excel_instance.CafeCharacterStateReq(j), password) for j in range(excel_instance.CafeCharacterStateReqLength())],
        "CafeCharacterStateAdd": [convert_string(excel_instance.CafeCharacterStateAdd(j), password) for j in range(excel_instance.CafeCharacterStateAddLength())],
        "CafeCharacterStateMake": [convert_string(excel_instance.CafeCharacterStateMake(j), password) for j in range(excel_instance.CafeCharacterStateMakeLength())],
        "CafeCharacterStateOnly": [convert_string(excel_instance.CafeCharacterStateOnly(j), password) for j in range(excel_instance.CafeCharacterStateOnlyLength())],
        "HideCraftShortcut": bool(excel_instance.HideCraftShortcut()),
    }

def dump_FurnitureGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupNameLocalize": convert_uint(excel_instance.GroupNameLocalize(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "RequiredFurnitureCount": [convert_int(excel_instance.RequiredFurnitureCount(j), password) for j in range(excel_instance.RequiredFurnitureCountLength())],
        "ComfortBonus": [convert_int(excel_instance.ComfortBonus(j), password) for j in range(excel_instance.ComfortBonusLength())],
    }

def dump_FurnitureTemplateElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FurnitureTemplateId": convert_int(excel_instance.FurnitureTemplateId(), password),
        "FurnitureId": convert_int(excel_instance.FurnitureId(), password),
        "Location": excel_instance.Location(),
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

def dump_GachaCombinedCostExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Priority": convert_int(excel_instance.Priority(), password),
        "ConsumeGachaTicketType": excel_instance.ConsumeGachaTicketType(),
        "ConsumeGachaTicketTypeAmount": convert_int(excel_instance.ConsumeGachaTicketTypeAmount(), password),
        "ConsumeParcelType": excel_instance.ConsumeParcelType(),
        "ConsumeParcelId": convert_int(excel_instance.ConsumeParcelId(), password),
        "ConsumeParcelAmount": convert_int(excel_instance.ConsumeParcelAmount(), password),
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
        "Tag": [excel_instance.Tag(j) for j in range(excel_instance.TagLength())],
    }

def dump_GachaElementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupID(), password),
        "ParcelType": excel_instance.ParcelType(),
        "ParcelID": convert_int(excel_instance.ParcelID(), password),
        "Rarity": excel_instance.Rarity(),
        "ParcelAmountMin": convert_int(excel_instance.ParcelAmountMin(), password),
        "ParcelAmountMax": convert_int(excel_instance.ParcelAmountMax(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "State": convert_int(excel_instance.State(), password),
    }

def dump_GachaElementRecursiveExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "GachaGroupID": convert_int(excel_instance.GachaGroupID(), password),
        "ParcelType": excel_instance.ParcelType(),
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
        "GroupType": excel_instance.GroupType(),
    }

def dump_GachaSelectPickupGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GachaGroupId": convert_int(excel_instance.GachaGroupId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
    }

def dump_GoodsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Type": convert_int(excel_instance.Type(), password),
        "Rarity": excel_instance.Rarity(),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "ConsumeParcelType": [excel_instance.ConsumeParcelType(j) for j in range(excel_instance.ConsumeParcelTypeLength())],
        "ConsumeParcelId": [convert_int(excel_instance.ConsumeParcelId(j), password) for j in range(excel_instance.ConsumeParcelIdLength())],
        "ConsumeParcelAmount": [convert_int(excel_instance.ConsumeParcelAmount(j), password) for j in range(excel_instance.ConsumeParcelAmountLength())],
        "ConsumeCondition": [excel_instance.ConsumeCondition(j) for j in range(excel_instance.ConsumeConditionLength())],
        "ConsumeGachaTicketType": [excel_instance.ConsumeGachaTicketType(j) for j in range(excel_instance.ConsumeGachaTicketTypeLength())],
        "ConsumeGachaTicketTypeAmount": [convert_int(excel_instance.ConsumeGachaTicketTypeAmount(j), password) for j in range(excel_instance.ConsumeGachaTicketTypeAmountLength())],
        "CombinedGachaCostId": convert_int(excel_instance.CombinedGachaCostId(), password),
        "ProductIdAOS": convert_int(excel_instance.ProductIdAOS(), password),
        "ProductIdiOS": convert_int(excel_instance.ProductIdiOS(), password),
        "ProductIdONE": convert_int(excel_instance.ProductIdONE(), password),
        "ProductIdSGS": convert_int(excel_instance.ProductIdSGS(), password),
        "ProductIdSTEAM": convert_int(excel_instance.ProductIdSTEAM(), password),
        "ConsumeExtraStep": [convert_int(excel_instance.ConsumeExtraStep(j), password) for j in range(excel_instance.ConsumeExtraStepLength())],
        "ConsumeExtraAmount": [convert_int(excel_instance.ConsumeExtraAmount(j), password) for j in range(excel_instance.ConsumeExtraAmountLength())],
        "State": convert_int(excel_instance.State(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_GooglePlayAchievementExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ConditionType": excel_instance.ConditionType(),
        "ConditionValue": convert_int(excel_instance.ConditionValue(), password),
        "GooglePlayId": convert_string(excel_instance.GooglePlayId(), password),
        "AchievementType": excel_instance.AchievementType(),
    }

def dump_GroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StageFileName": [convert_string(excel_instance.StageFileName(j), password) for j in range(excel_instance.StageFileNameLength())],
        "GroundSceneName": convert_string(excel_instance.GroundSceneName(), password),
        "FormationGroupId": convert_int(excel_instance.FormationGroupId(), password),
        "StageTopography": excel_instance.StageTopography(),
        "EnemyBulletType": excel_instance.EnemyBulletType(),
        "EnemyArmorType": excel_instance.EnemyArmorType(),
        "EnemySubArmorType": excel_instance.EnemySubArmorType(),
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
        "ForcedTacticSpeed": excel_instance.ForcedTacticSpeed(),
        "ForcedSkillUse": excel_instance.ForcedSkillUse(),
        "ShowNPCSkillCutIn": excel_instance.ShowNPCSkillCutIn(),
        "ImmuneHitBeforeTimeOutEnd": bool(excel_instance.ImmuneHitBeforeTimeOutEnd()),
        "UIBattleHideFromScratch": bool(excel_instance.UIBattleHideFromScratch()),
        "UIEnemyCount": excel_instance.UIEnemyCount(),
        "BattleReadyTimelinePath": convert_string(excel_instance.BattleReadyTimelinePath(), password),
        "BeforeVictoryTimelinePath": convert_string(excel_instance.BeforeVictoryTimelinePath(), password),
        "SkipBattleEnd": bool(excel_instance.SkipBattleEnd()),
        "HideNPCWhenBattleEnd": bool(excel_instance.HideNPCWhenBattleEnd()),
        "CoverPointOff": bool(excel_instance.CoverPointOff()),
        "UIHpScale": convert_float(excel_instance.UIHpScale(), password),
        "UIEmojiScale": convert_float(excel_instance.UIEmojiScale(), password),
        "UISkillMainLogScale": convert_float(excel_instance.UISkillMainLogScale(), password),
        "EffectCountLimit": convert_int(excel_instance.EffectCountLimit(), password),
        "CarrierSkillGroupId": convert_int(excel_instance.CarrierSkillGroupId(), password),
        "AllyPassiveSkillId": [convert_string(excel_instance.AllyPassiveSkillId(j), password) for j in range(excel_instance.AllyPassiveSkillIdLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "EnemyPassiveSkillId": [convert_string(excel_instance.EnemyPassiveSkillId(j), password) for j in range(excel_instance.EnemyPassiveSkillIdLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevel(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelLength())],
    }

def dump_GroundModuleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_uint(excel_instance.GroupId(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPath(), password),
    }

def dump_GrowthScoreCalculationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "IncludeGrowthFactor": excel_instance.IncludeGrowthFactor(),
        "ConversionCoefficient": convert_int(excel_instance.ConversionCoefficient(), password),
    }

def dump_GuideMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Category": excel_instance.Category(),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "TabNumber": convert_int(excel_instance.TabNumber(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "Description": convert_uint(excel_instance.Description(), password),
        "ToastDisplayType": excel_instance.ToastDisplayType(),
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "CompleteConditionType": excel_instance.CompleteConditionType(),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [excel_instance.CompleteConditionParameterTag(j) for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "IsAutoClearForScenario": bool(excel_instance.IsAutoClearForScenario()),
        "MissionRewardParcelType": [excel_instance.MissionRewardParcelType(j) for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
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
        "TargetGroup": excel_instance.TargetGroup(),
        "Enabled": bool(excel_instance.Enabled()),
        "BannerOpenDate": convert_string(excel_instance.BannerOpenDate(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "CloseBannerAfterCompletion": bool(excel_instance.CloseBannerAfterCompletion()),
        "MaximumLoginCount": convert_int(excel_instance.MaximumLoginCount(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDate(), password),
        "IconOrder": convert_int(excel_instance.IconOrder(), password),
        "SpineCharacterId": convert_int(excel_instance.SpineCharacterId(), password),
        "RequirementParcelImage": convert_string(excel_instance.RequirementParcelImage(), password),
        "RewardImage": convert_string(excel_instance.RewardImage(), password),
        "LobbyBannerImage": convert_string(excel_instance.LobbyBannerImage(), password),
        "BackgroundImage": convert_string(excel_instance.BackgroundImage(), password),
        "TitleImage": convert_string(excel_instance.TitleImage(), password),
        "RequirementParcelType": excel_instance.RequirementParcelType(),
        "RequirementParcelId": convert_int(excel_instance.RequirementParcelId(), password),
        "RequirementParcelAmount": convert_int(excel_instance.RequirementParcelAmount(), password),
        "TabType": excel_instance.TabType(),
        "IsPermanent": bool(excel_instance.IsPermanent()),
        "PreSeasonId": convert_int(excel_instance.PreSeasonId(), password),
    }

def dump_HpBarAbbreviationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MonsterLv": convert_int(excel_instance.MonsterLv(), password),
        "StandardHpBar": convert_int(excel_instance.StandardHpBar(), password),
        "RaidBossHpBar": convert_int(excel_instance.RaidBossHpBar(), password),
    }

def dump_IAWorldRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": excel_instance.ClearStageRewardParcelType(),
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardParcelUniqueName": convert_string(excel_instance.ClearStageRewardParcelUniqueName(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_IdCardBackgroundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Rarity": excel_instance.Rarity(),
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
        "IsPcBuild": bool(excel_instance.IsPcBuild()),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeId(), password),
        "TutorialParentName": [convert_string(excel_instance.TutorialParentName(j), password) for j in range(excel_instance.TutorialParentNameLength())],
        "UIName": [convert_string(excel_instance.UIName(j), password) for j in range(excel_instance.UINameLength())],
    }

def dump_InformationStrategyObjectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StageId": convert_int(excel_instance.StageId(), password),
        "PageName": convert_string(excel_instance.PageName(), password),
        "LocalizeCodeId": convert_string(excel_instance.LocalizeCodeId(), password),
    }

def dump_InteractiveWorldRaidArcadeMachineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "MiniGameType": [excel_instance.MiniGameType(j) for j in range(excel_instance.MiniGameTypeLength())],
        "MiniGameCostItemId": [convert_int(excel_instance.MiniGameCostItemId(j), password) for j in range(excel_instance.MiniGameCostItemIdLength())],
        "MiniGameCostItemAmount": [convert_int(excel_instance.MiniGameCostItemAmount(j), password) for j in range(excel_instance.MiniGameCostItemAmountLength())],
        "MiniGameSoftLimitItemId": [convert_string(excel_instance.MiniGameSoftLimitItemId(j), password) for j in range(excel_instance.MiniGameSoftLimitItemIdLength())],
        "MiniGameSoftLimitItemAmount": [convert_string(excel_instance.MiniGameSoftLimitItemAmount(j), password) for j in range(excel_instance.MiniGameSoftLimitItemAmountLength())],
        "MiniGameImage": [convert_string(excel_instance.MiniGameImage(j), password) for j in range(excel_instance.MiniGameImageLength())],
        "LocalizeTitle": [convert_uint(excel_instance.LocalizeTitle(j), password) for j in range(excel_instance.LocalizeTitleLength())],
        "LocalizeDesc": [convert_uint(excel_instance.LocalizeDesc(j), password) for j in range(excel_instance.LocalizeDescLength())],
    }

def dump_InteractiveWorldRaidBossGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupId(), password),
        "WorldBossHPLinkGroup": convert_int(excel_instance.WorldBossHPLinkGroup(), password),
        "WorldBossName": convert_string(excel_instance.WorldBossName(), password),
        "WorldBossPopupPortrait": convert_string(excel_instance.WorldBossPopupPortrait(), password),
        "WorldBossPopupNameTexture": convert_string(excel_instance.WorldBossPopupNameTexture(), password),
        "WorldBossPopupBG": convert_string(excel_instance.WorldBossPopupBG(), password),
        "WorldBossParcelPortrait": convert_string(excel_instance.WorldBossParcelPortrait(), password),
        "WorldBossListParcel": convert_string(excel_instance.WorldBossListParcel(), password),
        "WorldBossHP": convert_int(excel_instance.WorldBossHP(), password),
        "WorldBossHPTw": convert_int(excel_instance.WorldBossHPTw(), password),
        "WorldBossHPAsia": convert_int(excel_instance.WorldBossHPAsia(), password),
        "WorldBossHPNa": convert_int(excel_instance.WorldBossHPNa(), password),
        "WorldBossHPGlobal": convert_int(excel_instance.WorldBossHPGlobal(), password),
        "UIHideBeforeSpawn": bool(excel_instance.UIHideBeforeSpawn()),
        "HideAnotherBossKilled": bool(excel_instance.HideAnotherBossKilled()),
        "WorldBossClearRewardGroupId": convert_int(excel_instance.WorldBossClearRewardGroupId(), password),
        "AnotherBossKilled": [convert_int(excel_instance.AnotherBossKilled(j), password) for j in range(excel_instance.AnotherBossKilledLength())],
        "EchelonConstraintGroupId": convert_int(excel_instance.EchelonConstraintGroupId(), password),
        "ExclusiveOperatorBossSpawn": convert_string(excel_instance.ExclusiveOperatorBossSpawn(), password),
        "ExclusiveOperatorBossKill": convert_string(excel_instance.ExclusiveOperatorBossKill(), password),
        "ExclusiveOperatorScenarioBattle": convert_string(excel_instance.ExclusiveOperatorScenarioBattle(), password),
        "ExclusiveOperatorBossDamaged": convert_string(excel_instance.ExclusiveOperatorBossDamaged(), password),
        "BossGroupOpenCondition": convert_int(excel_instance.BossGroupOpenCondition(), password),
        "RaidScenarioBattleLocalizeKey": convert_string(excel_instance.RaidScenarioBattleLocalizeKey(), password),
        "IsSeasonFinalBoss": bool(excel_instance.IsSeasonFinalBoss()),
    }

def dump_InteractiveWorldRaidCarrierExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CarrierSkillListGroupId": convert_int(excel_instance.CarrierSkillListGroupId(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "CharacterLevel": convert_int(excel_instance.CharacterLevel(), password),
        "CharacterGrade": convert_int(excel_instance.CharacterGrade(), password),
        "ExSkillGroupId": [convert_string(excel_instance.ExSkillGroupId(j), password) for j in range(excel_instance.ExSkillGroupIdLength())],
        "ExSkillCardTexture": [convert_string(excel_instance.ExSkillCardTexture(j), password) for j in range(excel_instance.ExSkillCardTextureLength())],
        "FixedExSkillLevel": [convert_int(excel_instance.FixedExSkillLevel(j), password) for j in range(excel_instance.FixedExSkillLevelLength())],
        "PassiveSkillGroupId": [convert_string(excel_instance.PassiveSkillGroupId(j), password) for j in range(excel_instance.PassiveSkillGroupIdLength())],
        "PassiveSkillCardTexture": [convert_string(excel_instance.PassiveSkillCardTexture(j), password) for j in range(excel_instance.PassiveSkillCardTextureLength())],
        "FixedPassiveSkillLevel": [convert_int(excel_instance.FixedPassiveSkillLevel(j), password) for j in range(excel_instance.FixedPassiveSkillLevelLength())],
        "ExtraPassiveSkillGroupId": [convert_string(excel_instance.ExtraPassiveSkillGroupId(j), password) for j in range(excel_instance.ExtraPassiveSkillGroupIdLength())],
        "ExtraPassiveSkillCardTexture": [convert_string(excel_instance.ExtraPassiveSkillCardTexture(j), password) for j in range(excel_instance.ExtraPassiveSkillCardTextureLength())],
        "FixedExtraPassiveSkillLevel": [convert_int(excel_instance.FixedExtraPassiveSkillLevel(j), password) for j in range(excel_instance.FixedExtraPassiveSkillLevelLength())],
        "HiddenPassiveSkillGroupId": [convert_string(excel_instance.HiddenPassiveSkillGroupId(j), password) for j in range(excel_instance.HiddenPassiveSkillGroupIdLength())],
        "HiddenPassiveSkillCardTexture": [convert_string(excel_instance.HiddenPassiveSkillCardTexture(j), password) for j in range(excel_instance.HiddenPassiveSkillCardTextureLength())],
        "FixedHiddenPassiveSkillLevel": [convert_int(excel_instance.FixedHiddenPassiveSkillLevel(j), password) for j in range(excel_instance.FixedHiddenPassiveSkillLevelLength())],
    }

def dump_InteractiveWorldRaidCarrierMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ConditionId": convert_int(excel_instance.ConditionId(), password),
        "WorldRaidSeasonId": convert_int(excel_instance.WorldRaidSeasonId(), password),
        "WorldRaidPhaseId": convert_int(excel_instance.WorldRaidPhaseId(), password),
        "ReplaySeasonGroupId": convert_int(excel_instance.ReplaySeasonGroupId(), password),
        "ReplaySeasonOriginalPhaseId": convert_int(excel_instance.ReplaySeasonOriginalPhaseId(), password),
        "RecentClearBossGroupId": convert_int(excel_instance.RecentClearBossGroupId(), password),
        "RecentClearEventStageId": convert_int(excel_instance.RecentClearEventStageId(), password),
        "ChangeTarget": excel_instance.ChangeTarget(),
        "Priority": convert_int(excel_instance.Priority(), password),
        "ArtLevelPath": convert_string(excel_instance.ArtLevelPath(), password),
        "DesignLevelPath": convert_string(excel_instance.DesignLevelPath(), password),
        "BridgeBGM": convert_int(excel_instance.BridgeBGM(), password),
        "HangarBGM": convert_int(excel_instance.HangarBGM(), password),
        "LobbyBGM": convert_int(excel_instance.LobbyBGM(), password),
        "WorldMapBGM": convert_int(excel_instance.WorldMapBGM(), password),
        "InformationGroupIdWorldMap": convert_int(excel_instance.InformationGroupIdWorldMap(), password),
        "InformationGroupIdUCPopup": convert_int(excel_instance.InformationGroupIdUCPopup(), password),
        "InformationGroupIdBridge": convert_int(excel_instance.InformationGroupIdBridge(), password),
        "InformationGroupIdHangar": convert_int(excel_instance.InformationGroupIdHangar(), password),
        "InformationGroupIdLobby": convert_int(excel_instance.InformationGroupIdLobby(), password),
    }

def dump_InteractiveWorldRaidCarrierRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SkillId": convert_int(excel_instance.SkillId(), password),
        "SkillSlot": convert_string(excel_instance.SkillSlot(), password),
        "Level": convert_int(excel_instance.Level(), password),
        "RecipeIngredientId": [convert_int(excel_instance.RecipeIngredientId(j), password) for j in range(excel_instance.RecipeIngredientIdLength())],
    }

def dump_InteractiveWorldRaidConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "WorldRaidSeasonId": convert_int(excel_instance.WorldRaidSeasonId(), password),
        "WorldRaidPhaseId": convert_int(excel_instance.WorldRaidPhaseId(), password),
        "Priority": convert_int(excel_instance.Priority(), password),
        "MultipleConditionCheckType": excel_instance.MultipleConditionCheckType(),
        "MultipleConditionCheckParameter": convert_int(excel_instance.MultipleConditionCheckParameter(), password),
        "ConditionType": [excel_instance.ConditionType(j) for j in range(excel_instance.ConditionTypeLength())],
        "ConditionValue": [convert_int(excel_instance.ConditionValue(j), password) for j in range(excel_instance.ConditionValueLength())],
    }

def dump_InteractiveWorldRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "PhaseId": convert_int(excel_instance.PhaseId(), password),
        "PhaseStartCondition": convert_int(excel_instance.PhaseStartCondition(), password),
        "IsReplaySeason": bool(excel_instance.IsReplaySeason()),
        "EnterTicket": excel_instance.EnterTicket(),
        "PhaseStartTime": convert_string(excel_instance.PhaseStartTime(), password),
        "PhaseEndTime": convert_string(excel_instance.PhaseEndTime(), password),
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
        "OpenRaidBossGroupId": [convert_int(excel_instance.OpenRaidBossGroupId(j), password) for j in range(excel_instance.OpenRaidBossGroupIdLength())],
        "BossSpawnTime": [convert_string(excel_instance.BossSpawnTime(j), password) for j in range(excel_instance.BossSpawnTimeLength())],
        "EliminateTime": [convert_string(excel_instance.EliminateTime(j), password) for j in range(excel_instance.EliminateTimeLength())],
        "ScenarioOutputConditionId": [convert_int(excel_instance.ScenarioOutputConditionId(j), password) for j in range(excel_instance.ScenarioOutputConditionIdLength())],
        "ConditionScenarioGroupid": [convert_int(excel_instance.ConditionScenarioGroupid(j), password) for j in range(excel_instance.ConditionScenarioGroupidLength())],
        "CarrierSkillGroupId": convert_int(excel_instance.CarrierSkillGroupId(), password),
        "WorldRaidMapEnterOperator": convert_string(excel_instance.WorldRaidMapEnterOperator(), password),
        "UseFavorRankBuff": bool(excel_instance.UseFavorRankBuff()),
    }

def dump_InteractiveWorldRaidSkillDescriptionListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SkillParcelEchelonType": excel_instance.SkillParcelEchelonType(),
        "GlobalSkillGroupId": [convert_string(excel_instance.GlobalSkillGroupId(j), password) for j in range(excel_instance.GlobalSkillGroupIdLength())],
        "GlobalSkillRemoveCondition": [convert_int(excel_instance.GlobalSkillRemoveCondition(j), password) for j in range(excel_instance.GlobalSkillRemoveConditionLength())],
        "GlobalSkillShowSkillSlot": [excel_instance.GlobalSkillShowSkillSlot(j) for j in range(excel_instance.GlobalSkillShowSkillSlotLength())],
        "GlobalSkillHighlightResource": [excel_instance.GlobalSkillHighlightResource(j) for j in range(excel_instance.GlobalSkillHighlightResourceLength())],
        "SkillGroupId": [convert_string(excel_instance.SkillGroupId(j), password) for j in range(excel_instance.SkillGroupIdLength())],
        "ShowSkillSlot": [excel_instance.ShowSkillSlot(j) for j in range(excel_instance.ShowSkillSlotLength())],
        "HighlightResource": [excel_instance.HighlightResource(j) for j in range(excel_instance.HighlightResourceLength())],
    }

def dump_InteractiveWorldRaidStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "UseBossIndex": bool(excel_instance.UseBossIndex()),
        "UseBossAIPhaseSync": bool(excel_instance.UseBossAIPhaseSync()),
        "WorldRaidBossGroupId": convert_int(excel_instance.WorldRaidBossGroupId(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "BGPath": convert_string(excel_instance.BGPath(), password),
        "RaidSkillDescriptionListId": convert_int(excel_instance.RaidSkillDescriptionListId(), password),
        "RaidCharacterId": convert_int(excel_instance.RaidCharacterId(), password),
        "BossCharacterId": [convert_int(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "AssistCharacterLimitCount": convert_int(excel_instance.AssistCharacterLimitCount(), password),
        "WorldRaidDifficulty": excel_instance.WorldRaidDifficulty(),
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenCondition()),
        "RaidEnterAmount": convert_int(excel_instance.RaidEnterAmount(), password),
        "ReEnterAmount": convert_int(excel_instance.ReEnterAmount(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RaidBattleEndRewardGroupId": convert_int(excel_instance.RaidBattleEndRewardGroupId(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
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
        "AllyPassiveSkill": [convert_string(excel_instance.AllyPassiveSkill(j), password) for j in range(excel_instance.AllyPassiveSkillLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "AllyPassiveSkillRemoveCondition": [convert_int(excel_instance.AllyPassiveSkillRemoveCondition(j), password) for j in range(excel_instance.AllyPassiveSkillRemoveConditionLength())],
        "EnemyPassiveSkill": [convert_string(excel_instance.EnemyPassiveSkill(j), password) for j in range(excel_instance.EnemyPassiveSkillLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevel(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelLength())],
        "EnemyPassiveSkillRemoveCondition": [convert_int(excel_instance.EnemyPassiveSkillRemoveCondition(j), password) for j in range(excel_instance.EnemyPassiveSkillRemoveConditionLength())],
        "SaveCurrentLocalBossHP": bool(excel_instance.SaveCurrentLocalBossHP()),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_InteractiveWorldRaidStatusPresetExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "WorldRaidSeasonId": convert_int(excel_instance.WorldRaidSeasonId(), password),
        "WorldRaidPhaseId": convert_int(excel_instance.WorldRaidPhaseId(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "IAWorldRaidGroupId": [convert_int(excel_instance.IAWorldRaidGroupId(j), password) for j in range(excel_instance.IAWorldRaidGroupIdLength())],
        "EventContentStageId": [convert_int(excel_instance.EventContentStageId(j), password) for j in range(excel_instance.EventContentStageIdLength())],
        "EventContentScenarioId": [convert_int(excel_instance.EventContentScenarioId(j), password) for j in range(excel_instance.EventContentScenarioIdLength())],
    }

def dump_ItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Rarity": excel_instance.Rarity(),
        "ProductionStep": excel_instance.ProductionStep(),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "ItemCategory": excel_instance.ItemCategory(),
        "Quality": convert_int(excel_instance.Quality(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
        "SpriteName": convert_string(excel_instance.SpriteName(), password),
        "StackableMax": convert_int(excel_instance.StackableMax(), password),
        "StackableFunction": convert_int(excel_instance.StackableFunction(), password),
        "ImmediateUse": bool(excel_instance.ImmediateUse()),
        "UsingResultParcelType": excel_instance.UsingResultParcelType(),
        "UsingResultId": convert_int(excel_instance.UsingResultId(), password),
        "UsingResultAmount": convert_int(excel_instance.UsingResultAmount(), password),
        "MailType": excel_instance.MailType(),
        "ExpiryChangeParcelType": excel_instance.ExpiryChangeParcelType(),
        "ExpiryChangeId": convert_int(excel_instance.ExpiryChangeId(), password),
        "ExpiryChangeAmount": convert_int(excel_instance.ExpiryChangeAmount(), password),
        "CanTierUpgrade": bool(excel_instance.CanTierUpgrade()),
        "TierUpgradeRecipeCraftId": convert_int(excel_instance.TierUpgradeRecipeCraftId(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
        "IsCollaboration": bool(excel_instance.IsCollaboration()),
        "CraftQualityTier0": convert_int(excel_instance.CraftQualityTier0(), password),
        "CraftQualityTier1": convert_int(excel_instance.CraftQualityTier1(), password),
        "CraftQualityTier2": convert_int(excel_instance.CraftQualityTier2(), password),
        "ShiftingCraftQuality": convert_int(excel_instance.ShiftingCraftQuality(), password),
        "MaxGiftTags": convert_int(excel_instance.MaxGiftTags(), password),
        "ShopCategory": [convert_float(excel_instance.ShopCategory(j), password) for j in range(excel_instance.ShopCategoryLength())],
        "ExpirationDateTime": convert_string(excel_instance.ExpirationDateTime(), password),
        "ExpirationNotifyDateIn": convert_int(excel_instance.ExpirationNotifyDateIn(), password),
        "IsOverrideExpiration": bool(excel_instance.IsOverrideExpiration()),
        "ShortcutTypeId": convert_int(excel_instance.ShortcutTypeId(), password),
        "GachaTicket": excel_instance.GachaTicket(),
        "AlertPopupId": convert_int(excel_instance.AlertPopupId(), password),
        "ShiftingCraftRecipe": convert_int(excel_instance.ShiftingCraftRecipe(), password),
    }

def dump_KeyControllerImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ControllerKeyCode": convert_string(excel_instance.ControllerKeyCode(), password),
        "PSIconName": convert_string(excel_instance.PSIconName(), password),
        "XBoxIconName": convert_string(excel_instance.XBoxIconName(), password),
        "SteamDeckIconName": convert_string(excel_instance.SteamDeckIconName(), password),
    }

def dump_KeyMappingDisplayInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "KeyMappingKeyCode": convert_string(excel_instance.KeyMappingKeyCode(), password),
        "KeyMappingDisplayName": convert_string(excel_instance.KeyMappingDisplayName(), password),
    }

def dump_KeyMappingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_string(excel_instance.Id(), password),
        "DisplayGroupType": excel_instance.DisplayGroupType(),
        "GroupId": convert_string(excel_instance.GroupId(), password),
        "EnableCustomMapping": bool(excel_instance.EnableCustomMapping()),
        "DisplayCustomMapping": bool(excel_instance.DisplayCustomMapping()),
        "LocalizeKeyMappingId": convert_uint(excel_instance.LocalizeKeyMappingId(), password),
        "TargetKeyCode": convert_string(excel_instance.TargetKeyCode(), password),
        "ControllerCursorFocus": bool(excel_instance.ControllerCursorFocus()),
        "ControllerKeyCode": convert_string(excel_instance.ControllerKeyCode(), password),
        "IsDisplay": bool(excel_instance.IsDisplay()),
        "IsDisplayController": bool(excel_instance.IsDisplayController()),
        "IsUsed": bool(excel_instance.IsUsed()),
        "IsUsedController": bool(excel_instance.IsUsedController()),
        "IsLongPress": bool(excel_instance.IsLongPress()),
        "IgnorePosCheck": bool(excel_instance.IgnorePosCheck()),
        "IconPositionX": convert_float(excel_instance.IconPositionX(), password),
        "IconPositionY": convert_float(excel_instance.IconPositionY(), password),
        "IconScaleX": convert_float(excel_instance.IconScaleX(), password),
        "IconScaleY": convert_float(excel_instance.IconScaleY(), password),
        "ControllerIconPositionX": convert_float(excel_instance.ControllerIconPositionX(), password),
        "ControllerIconPositionY": convert_float(excel_instance.ControllerIconPositionY(), password),
        "ControllerIconScaleX": convert_float(excel_instance.ControllerIconScaleX(), password),
        "ControllerIconScaleY": convert_float(excel_instance.ControllerIconScaleY(), password),
        "KeymappingIconBGName": convert_string(excel_instance.KeymappingIconBGName(), password),
    }

def dump_KeyMappingGroupInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DisplayGroupType": excel_instance.DisplayGroupType(),
        "LocalizeKeyMappingDisplayGroupId": convert_uint(excel_instance.LocalizeKeyMappingDisplayGroupId(), password),
    }

def dump_KeyMappingPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ButtonName": [convert_string(excel_instance.ButtonName(j), password) for j in range(excel_instance.ButtonNameLength())],
        "KeyMappingId": [convert_string(excel_instance.KeyMappingId(j), password) for j in range(excel_instance.KeyMappingIdLength())],
    }

def dump_KeyMappingPopupNoneFocusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "ButtonName": convert_string(excel_instance.ButtonName(), password),
    }

def dump_KeyMappingTabExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_string(excel_instance.Id(), password),
        "LeftArrowKey": convert_string(excel_instance.LeftArrowKey(), password),
        "RightArrowKey": convert_string(excel_instance.RightArrowKey(), password),
        "LeftIconPositionX": convert_float(excel_instance.LeftIconPositionX(), password),
        "LeftIconPositionY": convert_float(excel_instance.LeftIconPositionY(), password),
        "LeftIconScaleX": convert_float(excel_instance.LeftIconScaleX(), password),
        "LeftIconScaleY": convert_float(excel_instance.LeftIconScaleY(), password),
        "RightIconPositionX": convert_float(excel_instance.RightIconPositionX(), password),
        "RightIconPositionY": convert_float(excel_instance.RightIconPositionY(), password),
        "RightIconScaleX": convert_float(excel_instance.RightIconScaleX(), password),
        "RightIconScaleY": convert_float(excel_instance.RightIconScaleY(), password),
    }

def dump_LevelExpMasterCoinExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "MinLevel": convert_int(excel_instance.MinLevel(), password),
        "MaxLevel": convert_int(excel_instance.MaxLevel(), password),
        "Ratio": convert_int(excel_instance.Ratio(), password),
    }

def dump_LoadingImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
        "DisplayWeight": convert_int(excel_instance.DisplayWeight(), password),
        "ImagePathTh": convert_string(excel_instance.ImagePathTh(), password),
        "ImagePathTw": convert_string(excel_instance.ImagePathTw(), password),
        "ImagePathEn": convert_string(excel_instance.ImagePathEn(), password),
    }

def dump_LocalizeCharProfileChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "ChangeCharacterID": convert_int(excel_instance.ChangeCharacterID(), password),
        "OverrideClub": bool(excel_instance.OverrideClub()),
    }

def dump_LocalizeCharProfileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "StatusMessageKr": convert_string(excel_instance.StatusMessageKr(), password),
        "StatusMessageJp": convert_string(excel_instance.StatusMessageJp(), password),
        "StatusMessageTh": convert_string(excel_instance.StatusMessageTh(), password),
        "StatusMessageTw": convert_string(excel_instance.StatusMessageTw(), password),
        "StatusMessageEn": convert_string(excel_instance.StatusMessageEn(), password),
        "FullNameKr": convert_string(excel_instance.FullNameKr(), password),
        "FullNameJp": convert_string(excel_instance.FullNameJp(), password),
        "FullNameTh": convert_string(excel_instance.FullNameTh(), password),
        "FullNameTw": convert_string(excel_instance.FullNameTw(), password),
        "FullNameEn": convert_string(excel_instance.FullNameEn(), password),
        "FamilyNameKr": convert_string(excel_instance.FamilyNameKr(), password),
        "FamilyNameRubyKr": convert_string(excel_instance.FamilyNameRubyKr(), password),
        "PersonalNameKr": convert_string(excel_instance.PersonalNameKr(), password),
        "PersonalNameRubyKr": convert_string(excel_instance.PersonalNameRubyKr(), password),
        "FamilyNameJp": convert_string(excel_instance.FamilyNameJp(), password),
        "FamilyNameRubyJp": convert_string(excel_instance.FamilyNameRubyJp(), password),
        "PersonalNameJp": convert_string(excel_instance.PersonalNameJp(), password),
        "PersonalNameRubyJp": convert_string(excel_instance.PersonalNameRubyJp(), password),
        "FamilyNameTh": convert_string(excel_instance.FamilyNameTh(), password),
        "FamilyNameRubyTh": convert_string(excel_instance.FamilyNameRubyTh(), password),
        "PersonalNameTh": convert_string(excel_instance.PersonalNameTh(), password),
        "PersonalNameRubyTh": convert_string(excel_instance.PersonalNameRubyTh(), password),
        "FamilyNameTw": convert_string(excel_instance.FamilyNameTw(), password),
        "FamilyNameRubyTw": convert_string(excel_instance.FamilyNameRubyTw(), password),
        "PersonalNameTw": convert_string(excel_instance.PersonalNameTw(), password),
        "PersonalNameRubyTw": convert_string(excel_instance.PersonalNameRubyTw(), password),
        "FamilyNameEn": convert_string(excel_instance.FamilyNameEn(), password),
        "FamilyNameRubyEn": convert_string(excel_instance.FamilyNameRubyEn(), password),
        "PersonalNameEn": convert_string(excel_instance.PersonalNameEn(), password),
        "PersonalNameRubyEn": convert_string(excel_instance.PersonalNameRubyEn(), password),
        "Club": excel_instance.Club(),
        "ClubNameForGachaKr": convert_string(excel_instance.ClubNameForGachaKr(), password),
        "ClubNameForGachaJp": convert_string(excel_instance.ClubNameForGachaJp(), password),
        "ClubNameForGachaTh": convert_string(excel_instance.ClubNameForGachaTh(), password),
        "ClubNameForGachaTw": convert_string(excel_instance.ClubNameForGachaTw(), password),
        "ClubNameForGachaEn": convert_string(excel_instance.ClubNameForGachaEn(), password),
        "SchoolYearKr": convert_string(excel_instance.SchoolYearKr(), password),
        "SchoolYearJp": convert_string(excel_instance.SchoolYearJp(), password),
        "SchoolYearTh": convert_string(excel_instance.SchoolYearTh(), password),
        "SchoolYearTw": convert_string(excel_instance.SchoolYearTw(), password),
        "SchoolYearEn": convert_string(excel_instance.SchoolYearEn(), password),
        "CharacterAgeKr": convert_string(excel_instance.CharacterAgeKr(), password),
        "CharacterAgeJp": convert_string(excel_instance.CharacterAgeJp(), password),
        "CharacterAgeTh": convert_string(excel_instance.CharacterAgeTh(), password),
        "CharacterAgeTw": convert_string(excel_instance.CharacterAgeTw(), password),
        "CharacterAgeEn": convert_string(excel_instance.CharacterAgeEn(), password),
        "BirthDay": convert_string(excel_instance.BirthDay(), password),
        "BirthdayKr": convert_string(excel_instance.BirthdayKr(), password),
        "BirthdayJp": convert_string(excel_instance.BirthdayJp(), password),
        "BirthdayTh": convert_string(excel_instance.BirthdayTh(), password),
        "BirthdayTw": convert_string(excel_instance.BirthdayTw(), password),
        "BirthdayEn": convert_string(excel_instance.BirthdayEn(), password),
        "CharHeightKr": convert_string(excel_instance.CharHeightKr(), password),
        "CharHeightJp": convert_string(excel_instance.CharHeightJp(), password),
        "CharHeightTh": convert_string(excel_instance.CharHeightTh(), password),
        "CharHeightTw": convert_string(excel_instance.CharHeightTw(), password),
        "CharHeightEn": convert_string(excel_instance.CharHeightEn(), password),
        "DesignerNameKr": convert_string(excel_instance.DesignerNameKr(), password),
        "DesignerNameJp": convert_string(excel_instance.DesignerNameJp(), password),
        "DesignerNameTh": convert_string(excel_instance.DesignerNameTh(), password),
        "DesignerNameTw": convert_string(excel_instance.DesignerNameTw(), password),
        "DesignerNameEn": convert_string(excel_instance.DesignerNameEn(), password),
        "IllustratorNameKr": convert_string(excel_instance.IllustratorNameKr(), password),
        "IllustratorNameJp": convert_string(excel_instance.IllustratorNameJp(), password),
        "IllustratorNameTh": convert_string(excel_instance.IllustratorNameTh(), password),
        "IllustratorNameTw": convert_string(excel_instance.IllustratorNameTw(), password),
        "IllustratorNameEn": convert_string(excel_instance.IllustratorNameEn(), password),
        "CharacterVoiceKr": convert_string(excel_instance.CharacterVoiceKr(), password),
        "CharacterVoiceJp": convert_string(excel_instance.CharacterVoiceJp(), password),
        "CharacterVoiceTh": convert_string(excel_instance.CharacterVoiceTh(), password),
        "CharacterVoiceTw": convert_string(excel_instance.CharacterVoiceTw(), password),
        "CharacterVoiceEn": convert_string(excel_instance.CharacterVoiceEn(), password),
        "KRCharacterVoiceKr": convert_string(excel_instance.KRCharacterVoiceKr(), password),
        "KRCharacterVoiceTh": convert_string(excel_instance.KRCharacterVoiceTh(), password),
        "KRCharacterVoiceTw": convert_string(excel_instance.KRCharacterVoiceTw(), password),
        "KRCharacterVoiceEn": convert_string(excel_instance.KRCharacterVoiceEn(), password),
        "HobbyKr": convert_string(excel_instance.HobbyKr(), password),
        "HobbyJp": convert_string(excel_instance.HobbyJp(), password),
        "HobbyTh": convert_string(excel_instance.HobbyTh(), password),
        "HobbyTw": convert_string(excel_instance.HobbyTw(), password),
        "HobbyEn": convert_string(excel_instance.HobbyEn(), password),
        "WeaponNameKr": convert_string(excel_instance.WeaponNameKr(), password),
        "WeaponDescKr": convert_string(excel_instance.WeaponDescKr(), password),
        "WeaponNameJp": convert_string(excel_instance.WeaponNameJp(), password),
        "WeaponDescJp": convert_string(excel_instance.WeaponDescJp(), password),
        "WeaponNameTh": convert_string(excel_instance.WeaponNameTh(), password),
        "WeaponDescTh": convert_string(excel_instance.WeaponDescTh(), password),
        "WeaponNameTw": convert_string(excel_instance.WeaponNameTw(), password),
        "WeaponDescTw": convert_string(excel_instance.WeaponDescTw(), password),
        "WeaponNameEn": convert_string(excel_instance.WeaponNameEn(), password),
        "WeaponDescEn": convert_string(excel_instance.WeaponDescEn(), password),
        "ProfileIntroductionKr": convert_string(excel_instance.ProfileIntroductionKr(), password),
        "ProfileIntroductionJp": convert_string(excel_instance.ProfileIntroductionJp(), password),
        "ProfileIntroductionTh": convert_string(excel_instance.ProfileIntroductionTh(), password),
        "ProfileIntroductionTw": convert_string(excel_instance.ProfileIntroductionTw(), password),
        "ProfileIntroductionEn": convert_string(excel_instance.ProfileIntroductionEn(), password),
        "CharacterSSRNewKr": convert_string(excel_instance.CharacterSSRNewKr(), password),
        "CharacterSSRNewJp": convert_string(excel_instance.CharacterSSRNewJp(), password),
        "CharacterSSRNewTh": convert_string(excel_instance.CharacterSSRNewTh(), password),
        "CharacterSSRNewTw": convert_string(excel_instance.CharacterSSRNewTw(), password),
        "CharacterSSRNewEn": convert_string(excel_instance.CharacterSSRNewEn(), password),
    }

def dump_LocalizeCodeInBuildExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
        "Th": convert_string(excel_instance.Th(), password),
        "Tw": convert_string(excel_instance.Tw(), password),
        "En": convert_string(excel_instance.En(), password),
    }

def dump_LocalizeErrorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "ErrorLevel": excel_instance.ErrorLevel(),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
        "Th": convert_string(excel_instance.Th(), password),
        "Tw": convert_string(excel_instance.Tw(), password),
        "En": convert_string(excel_instance.En(), password),
    }

def dump_LocalizeEtcExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "NameKr": convert_string(excel_instance.NameKr(), password),
        "DescriptionKr": convert_string(excel_instance.DescriptionKr(), password),
        "NameJp": convert_string(excel_instance.NameJp(), password),
        "DescriptionJp": convert_string(excel_instance.DescriptionJp(), password),
        "NameTh": convert_string(excel_instance.NameTh(), password),
        "DescriptionTh": convert_string(excel_instance.DescriptionTh(), password),
        "NameTw": convert_string(excel_instance.NameTw(), password),
        "DescriptionTw": convert_string(excel_instance.DescriptionTw(), password),
        "NameEn": convert_string(excel_instance.NameEn(), password),
        "DescriptionEn": convert_string(excel_instance.DescriptionEn(), password),
    }

def dump_LocalizeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Key": convert_uint(excel_instance.Key(), password),
        "Kr": convert_string(excel_instance.Kr(), password),
        "Jp": convert_string(excel_instance.Jp(), password),
        "Th": convert_string(excel_instance.Th(), password),
        "Tw": convert_string(excel_instance.Tw(), password),
        "En": convert_string(excel_instance.En(), password),
    }

def dump_LocalizeGachaShopExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GachaShopId": convert_int(excel_instance.GachaShopId(), password),
        "TabNameKr": convert_string(excel_instance.TabNameKr(), password),
        "TabNameJp": convert_string(excel_instance.TabNameJp(), password),
        "TabNameTh": convert_string(excel_instance.TabNameTh(), password),
        "TabNameTw": convert_string(excel_instance.TabNameTw(), password),
        "TabNameEn": convert_string(excel_instance.TabNameEn(), password),
        "TitleNameKr": convert_string(excel_instance.TitleNameKr(), password),
        "TitleNameJp": convert_string(excel_instance.TitleNameJp(), password),
        "TitleNameTh": convert_string(excel_instance.TitleNameTh(), password),
        "TitleNameTw": convert_string(excel_instance.TitleNameTw(), password),
        "TitleNameEn": convert_string(excel_instance.TitleNameEn(), password),
        "SubTitleKr": convert_string(excel_instance.SubTitleKr(), password),
        "SubTitleJp": convert_string(excel_instance.SubTitleJp(), password),
        "SubTitleTh": convert_string(excel_instance.SubTitleTh(), password),
        "SubTitleTw": convert_string(excel_instance.SubTitleTw(), password),
        "SubTitleEn": convert_string(excel_instance.SubTitleEn(), password),
        "GachaDescriptionKr": convert_string(excel_instance.GachaDescriptionKr(), password),
        "GachaDescriptionJp": convert_string(excel_instance.GachaDescriptionJp(), password),
        "GachaDescriptionTh": convert_string(excel_instance.GachaDescriptionTh(), password),
        "GachaDescriptionTw": convert_string(excel_instance.GachaDescriptionTw(), password),
        "GachaDescriptionEn": convert_string(excel_instance.GachaDescriptionEn(), password),
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
        "NameTh": convert_string(excel_instance.NameTh(), password),
        "DescriptionTh": convert_string(excel_instance.DescriptionTh(), password),
        "SkillInvokeLocalizeTh": convert_string(excel_instance.SkillInvokeLocalizeTh(), password),
        "NameTw": convert_string(excel_instance.NameTw(), password),
        "DescriptionTw": convert_string(excel_instance.DescriptionTw(), password),
        "SkillInvokeLocalizeTw": convert_string(excel_instance.SkillInvokeLocalizeTw(), password),
        "NameEn": convert_string(excel_instance.NameEn(), password),
        "DescriptionEn": convert_string(excel_instance.DescriptionEn(), password),
        "SkillInvokeLocalizeEn": convert_string(excel_instance.SkillInvokeLocalizeEn(), password),
    }

def dump_LogicEffectCommonVisualExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringID": convert_uint(excel_instance.StringID(), password),
        "IconSpriteName": convert_string(excel_instance.IconSpriteName(), password),
        "IconDispelColor": [convert_float(excel_instance.IconDispelColor(j), password) for j in range(excel_instance.IconDispelColorLength())],
        "ParticleEnterPath": convert_string(excel_instance.ParticleEnterPath(), password),
        "ParticleEnterSocket": excel_instance.ParticleEnterSocket(),
        "ParticleLoopPath": convert_string(excel_instance.ParticleLoopPath(), password),
        "ParticleLoopSocket": excel_instance.ParticleLoopSocket(),
        "ParticleEndPath": convert_string(excel_instance.ParticleEndPath(), password),
        "ParticleEndSocket": excel_instance.ParticleEndSocket(),
        "ParticleApplyPath": convert_string(excel_instance.ParticleApplyPath(), password),
        "ParticleApplySocket": excel_instance.ParticleApplySocket(),
        "ParticleRemovedPath": convert_string(excel_instance.ParticleRemovedPath(), password),
        "ParticleRemovedSocket": excel_instance.ParticleRemovedSocket(),
    }

def dump_MemoryLobbyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "MemoryLobbyCategory": excel_instance.MemoryLobbyCategory(),
        "SlotTextureName": convert_string(excel_instance.SlotTextureName(), password),
        "RewardTextureName": convert_string(excel_instance.RewardTextureName(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "AudioClipJp": convert_string(excel_instance.AudioClipJp(), password),
        "AudioClipKr": convert_string(excel_instance.AudioClipKr(), password),
        "AudioClipTh": convert_string(excel_instance.AudioClipTh(), password),
        "AudioClipTw": convert_string(excel_instance.AudioClipTw(), password),
        "AudioClipEn": convert_string(excel_instance.AudioClipEn(), password),
    }

def dump_MemoryLobby_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "PrefabNameKr": convert_string(excel_instance.PrefabNameKr(), password),
        "PrefabNameTw": convert_string(excel_instance.PrefabNameTw(), password),
        "PrefabNameAsia": convert_string(excel_instance.PrefabNameAsia(), password),
        "PrefabNameNa": convert_string(excel_instance.PrefabNameNa(), password),
        "PrefabNameGlobal": convert_string(excel_instance.PrefabNameGlobal(), password),
        "PrefabNameTeen": convert_string(excel_instance.PrefabNameTeen(), password),
    }

def dump_MessagePopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StringId": convert_uint(excel_instance.StringId(), password),
        "MessagePopupLayout": excel_instance.MessagePopupLayout(),
        "OrderType": excel_instance.OrderType(),
        "Image": convert_string(excel_instance.Image(), password),
        "TitleText": convert_uint(excel_instance.TitleText(), password),
        "SubTitleText": convert_uint(excel_instance.SubTitleText(), password),
        "MessageText": convert_uint(excel_instance.MessageText(), password),
        "ConditionText": [convert_uint(excel_instance.ConditionText(j), password) for j in range(excel_instance.ConditionTextLength())],
        "DisplayXButton": bool(excel_instance.DisplayXButton()),
        "Button": [excel_instance.Button(j) for j in range(excel_instance.ButtonLength())],
        "ButtonText": [convert_uint(excel_instance.ButtonText(j), password) for j in range(excel_instance.ButtonTextLength())],
        "ButtonCommand": [convert_string(excel_instance.ButtonCommand(j), password) for j in range(excel_instance.ButtonCommandLength())],
        "ButtonParameter": [convert_string(excel_instance.ButtonParameter(j), password) for j in range(excel_instance.ButtonParameterLength())],
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
        "AudioClipPath": [convert_string(excel_instance.AudioClipPath(j), password) for j in range(excel_instance.AudioClipPathLength())],
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_MinigameCCGCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Type": excel_instance.Type(),
        "IsDisposal": bool(excel_instance.IsDisposal()),
        "ActiveSkillId": convert_int(excel_instance.ActiveSkillId(), password),
        "ActiveSkillCost": convert_int(excel_instance.ActiveSkillCost(), password),
        "ActiveSkilleCostVisible": bool(excel_instance.ActiveSkilleCostVisible()),
        "PassiveSkillId": [convert_int(excel_instance.PassiveSkillId(j), password) for j in range(excel_instance.PassiveSkillIdLength())],
        "PassiveActivateCount": convert_int(excel_instance.PassiveActivateCount(), password),
        "Name": convert_uint(excel_instance.Name(), password),
        "Description": convert_string(excel_instance.Description(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "UIImagePath": convert_string(excel_instance.UIImagePath(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
    }

def dump_MinigameCCGCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Type": excel_instance.Type(),
        "ActiveSkillId": convert_int(excel_instance.ActiveSkillId(), password),
        "ActiveSkillCost": convert_int(excel_instance.ActiveSkillCost(), password),
        "ActiveSkilleCostVisible": bool(excel_instance.ActiveSkilleCostVisible()),
        "ActiveSkillCooldown": convert_int(excel_instance.ActiveSkillCooldown(), password),
        "MaxHealth": convert_int(excel_instance.MaxHealth(), password),
        "PassiveSkillId": [convert_int(excel_instance.PassiveSkillId(j), password) for j in range(excel_instance.PassiveSkillIdLength())],
        "Name": convert_uint(excel_instance.Name(), password),
        "Description": convert_string(excel_instance.Description(), password),
        "ImagePath": convert_string(excel_instance.ImagePath(), password),
        "UIImagePath": convert_string(excel_instance.UIImagePath(), password),
        "Tags": [excel_instance.Tags(j) for j in range(excel_instance.TagsLength())],
    }

def dump_MinigameCCGEnemyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "CharacterType": excel_instance.CharacterType(),
        "Order": convert_int(excel_instance.Order(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
    }

def dump_MinigameCCGEnemyGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "EnemyAI": convert_string(excel_instance.EnemyAI(), password),
        "EnemyBGM": convert_int(excel_instance.EnemyBGM(), password),
        "LocalizeEnemyGroupName": convert_uint(excel_instance.LocalizeEnemyGroupName(), password),
        "LocalizeEnemyGroupDesc": convert_uint(excel_instance.LocalizeEnemyGroupDesc(), password),
    }

def dump_MinigameCCGInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "CCGId": convert_int(excel_instance.CCGId(), password),
        "CostParcelType": excel_instance.CostParcelType(),
        "CostParcelId": convert_int(excel_instance.CostParcelId(), password),
        "CostParcelAmount": convert_int(excel_instance.CostParcelAmount(), password),
        "CardBackPath": convert_string(excel_instance.CardBackPath(), password),
        "PerkCostParcelType": excel_instance.PerkCostParcelType(),
        "PerkCostParcelId": convert_int(excel_instance.PerkCostParcelId(), password),
    }

def dump_MinigameCCGLevelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelId": convert_int(excel_instance.LevelId(), password),
        "CCGId": convert_int(excel_instance.CCGId(), password),
        "FloorIndex": convert_int(excel_instance.FloorIndex(), password),
        "BackgroundPath": convert_string(excel_instance.BackgroundPath(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
    }

def dump_MinigameCCGLevelNodeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelId": convert_int(excel_instance.LevelId(), password),
        "NodeId": convert_int(excel_instance.NodeId(), password),
        "NodeIcon": excel_instance.NodeIcon(),
        "StageGroupId": convert_int(excel_instance.StageGroupId(), password),
        "NextNodeId": [convert_int(excel_instance.NextNodeId(j), password) for j in range(excel_instance.NextNodeIdLength())],
    }

def dump_MinigameCCGLevelStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "EnemyGroupId": [convert_int(excel_instance.EnemyGroupId(j), password) for j in range(excel_instance.EnemyGroupIdLength())],
        "StageType": excel_instance.StageType(),
        "CampDiscardCardCount": convert_int(excel_instance.CampDiscardCardCount(), password),
        "CampSprPath": convert_string(excel_instance.CampSprPath(), password),
        "CampBackgroundPath": convert_string(excel_instance.CampBackgroundPath(), password),
        "RewardType": excel_instance.RewardType(),
        "RewardCount": convert_int(excel_instance.RewardCount(), password),
        "RewardCardGroupId": convert_int(excel_instance.RewardCardGroupId(), password),
        "CardRarityGroupId": convert_int(excel_instance.CardRarityGroupId(), password),
        "IsSkipIntroScenario": bool(excel_instance.IsSkipIntroScenario()),
        "IntroScenarioGroupId": convert_int(excel_instance.IntroScenarioGroupId(), password),
        "IsSkipOutroScenario": bool(excel_instance.IsSkipOutroScenario()),
        "OutroScenarioGroupId": convert_int(excel_instance.OutroScenarioGroupId(), password),
    }

def dump_MinigameCCGLogicEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DataLoadPath": convert_string(excel_instance.DataLoadPath(), password),
        "Icon": convert_string(excel_instance.Icon(), password),
    }

def dump_MinigameCCGOpenDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "DialogId": convert_int(excel_instance.DialogId(), password),
        "PlayOrder": convert_int(excel_instance.PlayOrder(), password),
        "ConditionCard": convert_int(excel_instance.ConditionCard(), password),
        "Dialog": convert_uint(excel_instance.Dialog(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "DurationKr": convert_int(excel_instance.DurationKr(), password),
        "Voice": convert_uint(excel_instance.Voice(), password),
    }

def dump_MinigameCCGPerkExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CCGId": convert_int(excel_instance.CCGId(), password),
        "CostParcelAmount": convert_int(excel_instance.CostParcelAmount(), password),
        "RerollPoint": convert_int(excel_instance.RerollPoint(), password),
        "DiscardPoint": convert_int(excel_instance.DiscardPoint(), password),
        "EnvironmentLogicEffectId": [convert_int(excel_instance.EnvironmentLogicEffectId(j), password) for j in range(excel_instance.EnvironmentLogicEffectIdLength())],
        "RequiredPerkId": [convert_int(excel_instance.RequiredPerkId(j), password) for j in range(excel_instance.RequiredPerkIdLength())],
        "ShopOrder": convert_int(excel_instance.ShopOrder(), password),
        "ShopIcon": convert_string(excel_instance.ShopIcon(), password),
        "ShopLocalizeTitle": convert_uint(excel_instance.ShopLocalizeTitle(), password),
        "ShopLocalizeDesc": convert_uint(excel_instance.ShopLocalizeDesc(), password),
    }

def dump_MinigameCCGRewardCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "EntityType": excel_instance.EntityType(),
        "CardId": convert_int(excel_instance.CardId(), password),
        "CardRarity": convert_int(excel_instance.CardRarity(), password),
    }

def dump_MinigameCCGRewardCardRateExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RarityGroupId": convert_int(excel_instance.RarityGroupId(), password),
        "CardRarity": convert_int(excel_instance.CardRarity(), password),
        "Rate": convert_int(excel_instance.Rate(), password),
    }

def dump_MinigameCCGRewardItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CCGId": convert_int(excel_instance.CCGId(), password),
        "MinPoint": convert_int(excel_instance.MinPoint(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
    }

def dump_MinigameCCGSkillExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SkillType": convert_string(excel_instance.SkillType(), password),
        "DataLoadPath": convert_string(excel_instance.DataLoadPath(), password),
        "Name": convert_uint(excel_instance.Name(), password),
        "Description": convert_uint(excel_instance.Description(), password),
        "SkillIcon": convert_string(excel_instance.SkillIcon(), password),
    }

def dump_MinigameCCGStartDeckCardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CCGId": convert_int(excel_instance.CCGId(), password),
        "CardId": convert_int(excel_instance.CardId(), password),
    }

def dump_MinigameCCGStartDeckCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CCGId": convert_int(excel_instance.CCGId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
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
        "DefenseBattleParcelType": excel_instance.DefenseBattleParcelType(),
        "DefenseBattleParcelId": convert_int(excel_instance.DefenseBattleParcelId(), password),
        "DefenseBattleMultiplierMax": convert_int(excel_instance.DefenseBattleMultiplierMax(), password),
        "DisableRootMotion": bool(excel_instance.DisableRootMotion()),
    }

def dump_MiniGameDefenseStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Name": convert_string(excel_instance.Name(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "StageDifficulty": excel_instance.StageDifficulty(),
        "StageDifficultyLocalize": convert_uint(excel_instance.StageDifficultyLocalize(), password),
        "StageNumber": convert_int(excel_instance.StageNumber(), password),
        "StageDisplay": convert_int(excel_instance.StageDisplay(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "StageEnterCostType": excel_instance.StageEnterCostType(),
        "StageEnterCostId": convert_int(excel_instance.StageEnterCostId(), password),
        "StageEnterCostAmount": convert_int(excel_instance.StageEnterCostAmount(), password),
        "EventContentStageRewardId": convert_int(excel_instance.EventContentStageRewardId(), password),
        "EnterScenarioGroupId": [convert_int(excel_instance.EnterScenarioGroupId(j), password) for j in range(excel_instance.EnterScenarioGroupIdLength())],
        "ClearScenarioGroupId": [convert_int(excel_instance.ClearScenarioGroupId(j), password) for j in range(excel_instance.ClearScenarioGroupIdLength())],
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundID": convert_int(excel_instance.GroundID(), password),
        "ContentType": excel_instance.ContentType(),
        "StarGoal": [excel_instance.StarGoal(j) for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
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
        "Parameter": [excel_instance.Parameter(j) for j in range(excel_instance.ParameterLength())],
        "ParameterAmount": [convert_int(excel_instance.ParameterAmount(j), password) for j in range(excel_instance.ParameterAmountLength())],
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
        "DreamMakerEndingType": excel_instance.DreamMakerEndingType(),
        "Order": convert_int(excel_instance.Order(), password),
        "ScenarioGroupId": convert_int(excel_instance.ScenarioGroupId(), password),
        "EndingCondition": [excel_instance.EndingCondition(j) for j in range(excel_instance.EndingConditionLength())],
        "EndingConditionValue": [convert_int(excel_instance.EndingConditionValue(j), password) for j in range(excel_instance.EndingConditionValueLength())],
    }

def dump_MiniGameDreamEndingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EndingId": convert_int(excel_instance.EndingId(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "DreamMakerEndingRewardType": excel_instance.DreamMakerEndingRewardType(),
        "DreamMakerEndingType": excel_instance.DreamMakerEndingType(),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MiniGameDreamInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "DreamMakerMultiplierCondition": excel_instance.DreamMakerMultiplierCondition(),
        "DreamMakerMultiplierConditionValue": convert_int(excel_instance.DreamMakerMultiplierConditionValue(), password),
        "DreamMakerMultiplierMax": convert_int(excel_instance.DreamMakerMultiplierMax(), password),
        "DreamMakerDays": convert_int(excel_instance.DreamMakerDays(), password),
        "DreamMakerActionPoint": convert_int(excel_instance.DreamMakerActionPoint(), password),
        "DreamMakerParcelType": excel_instance.DreamMakerParcelType(),
        "DreamMakerParcelId": convert_int(excel_instance.DreamMakerParcelId(), password),
        "DreamMakerDailyPointParcelType": excel_instance.DreamMakerDailyPointParcelType(),
        "DreamMakerDailyPointId": convert_int(excel_instance.DreamMakerDailyPointId(), password),
        "DreamMakerParameterTransfer": convert_int(excel_instance.DreamMakerParameterTransfer(), password),
        "ScheduleCostGoodsId": convert_int(excel_instance.ScheduleCostGoodsId(), password),
        "LobbyBGMChangeScenarioId": convert_int(excel_instance.LobbyBGMChangeScenarioId(), password),
    }

def dump_MiniGameDreamParameterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "ParameterType": excel_instance.ParameterType(),
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
        "DreamMakerResult": excel_instance.DreamMakerResult(),
        "DreamMakerScheduleGroup": convert_int(excel_instance.DreamMakerScheduleGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "RewardParameter": [excel_instance.RewardParameter(j) for j in range(excel_instance.RewardParameterLength())],
        "RewardParameterOperationType": [excel_instance.RewardParameterOperationType(j) for j in range(excel_instance.RewardParameterOperationTypeLength())],
        "RewardParameterAmount": [convert_int(excel_instance.RewardParameterAmount(j), password) for j in range(excel_instance.RewardParameterAmountLength())],
        "RewardParcelType": excel_instance.RewardParcelType(),
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
        "VoiceCondition": excel_instance.VoiceCondition(),
        "VoiceClip": convert_uint(excel_instance.VoiceClip(), password),
    }

def dump_MiniGameMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "GroupName": convert_string(excel_instance.GroupName(), password),
        "Category": excel_instance.Category(),
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": excel_instance.ResetType(),
        "ToastDisplayType": excel_instance.ToastDisplayType(),
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "TargetGroup": excel_instance.TargetGroup(),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "CompleteConditionType": excel_instance.CompleteConditionType(),
        "IsCompleteExtensionTime": bool(excel_instance.IsCompleteExtensionTime()),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [excel_instance.CompleteConditionParameterTag(j) for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "CompleteConditionMissionId": [convert_int(excel_instance.CompleteConditionMissionId(j), password) for j in range(excel_instance.CompleteConditionMissionIdLength())],
        "CompleteConditionMissionCount": convert_int(excel_instance.CompleteConditionMissionCount(), password),
        "MissionRewardParcelType": [excel_instance.MissionRewardParcelType(j) for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
        "ConditionRewardParcelType": [excel_instance.ConditionRewardParcelType(j) for j in range(excel_instance.ConditionRewardParcelTypeLength())],
        "ConditionRewardParcelId": [convert_int(excel_instance.ConditionRewardParcelId(j), password) for j in range(excel_instance.ConditionRewardParcelIdLength())],
        "ConditionRewardAmount": [convert_int(excel_instance.ConditionRewardAmount(j), password) for j in range(excel_instance.ConditionRewardAmountLength())],
    }

def dump_MiniGamePlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "MiniGameType": excel_instance.MiniGameType(),
        "IsPcBuild": bool(excel_instance.IsPcBuild()),
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
        "StageDifficulty": excel_instance.StageDifficulty(),
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

def dump_MiniGameRoadPuzzleAdditionalRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_MiniGameRoadPuzzleInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventUseCostType": excel_instance.EventUseCostType(),
        "EventUseCostId": convert_int(excel_instance.EventUseCostId(), password),
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "RailSetRewardId": convert_int(excel_instance.RailSetRewardId(), password),
        "InstantClearRound": convert_int(excel_instance.InstantClearRound(), password),
    }

def dump_MinigameRoadPuzzleMapExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "MapGroupId": convert_int(excel_instance.MapGroupId(), password),
        "Map": convert_string(excel_instance.Map(), password),
        "MapBG": convert_string(excel_instance.MapBG(), password),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "AvailableRailTile": [convert_int(excel_instance.AvailableRailTile(j), password) for j in range(excel_instance.AvailableRailTileLength())],
        "AvailableRailTileAmount": [convert_int(excel_instance.AvailableRailTileAmount(j), password) for j in range(excel_instance.AvailableRailTileAmountLength())],
        "OriginalTileCount": [convert_int(excel_instance.OriginalTileCount(j), password) for j in range(excel_instance.OriginalTileCountLength())],
        "TrainSpeed": convert_float(excel_instance.TrainSpeed(), password),
    }

def dump_MinigameRoadPuzzleMapTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "MapTileType": excel_instance.MapTileType(),
    }

def dump_MiniGameRoadPuzzleRailSetRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "LocalizePrefabID": convert_string(excel_instance.LocalizePrefabID(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameRoadPuzzleRailTileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "OriginalTile": bool(excel_instance.OriginalTile()),
        "PrefabName": convert_string(excel_instance.PrefabName(), password),
        "RailTileType": excel_instance.RailTileType(),
    }

def dump_MiniGameRoadPuzzleRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameRoadPuzzleRoadRoundExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Round": convert_int(excel_instance.Round(), password),
        "IsLoop": bool(excel_instance.IsLoop()),
        "EnterScenarioGroupId": convert_int(excel_instance.EnterScenarioGroupId(), password),
        "EndScenarioGroupId": convert_int(excel_instance.EndScenarioGroupId(), password),
        "MapGroupId": convert_int(excel_instance.MapGroupId(), password),
        "RoundReward": convert_int(excel_instance.RoundReward(), password),
        "AdditionalRewardID": [convert_int(excel_instance.AdditionalRewardID(j), password) for j in range(excel_instance.AdditionalRewardIDLength())],
        "AdditionalRewardAmount": [convert_int(excel_instance.AdditionalRewardAmount(j), password) for j in range(excel_instance.AdditionalRewardAmountLength())],
    }

def dump_MiniGameRoadPuzzleVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "VoiceCondition": excel_instance.VoiceCondition(),
        "VoiceClip": convert_uint(excel_instance.VoiceClip(), password),
    }

def dump_MiniGameShootingCharacterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "SpineResourceName": convert_string(excel_instance.SpineResourceName(), password),
        "BodyRadius": convert_float(excel_instance.BodyRadius(), password),
        "ModelPrefabName": convert_string(excel_instance.ModelPrefabName(), password),
        "NormalAttackSkillData": convert_string(excel_instance.NormalAttackSkillData(), password),
        "PublicSkillData": [convert_string(excel_instance.PublicSkillData(j), password) for j in range(excel_instance.PublicSkillDataLength())],
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
        "GeasType": excel_instance.GeasType(),
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
        "BgmId": [convert_int(excel_instance.BgmId(j), password) for j in range(excel_instance.BgmIdLength())],
        "CostGoodsId": convert_int(excel_instance.CostGoodsId(), password),
        "Difficulty": excel_instance.Difficulty(),
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
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameTBGDiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "DiceGroup": convert_int(excel_instance.DiceGroup(), password),
        "DiceResult": convert_int(excel_instance.DiceResult(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "ProbModifyCondition": [excel_instance.ProbModifyCondition(j) for j in range(excel_instance.ProbModifyConditionLength())],
        "ProbModifyValue": [convert_int(excel_instance.ProbModifyValue(j), password) for j in range(excel_instance.ProbModifyValueLength())],
        "ProbModifyLimit": [convert_int(excel_instance.ProbModifyLimit(j), password) for j in range(excel_instance.ProbModifyLimitLength())],
    }

def dump_MinigameTBGEncounterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "AllThema": bool(excel_instance.AllThema()),
        "ThemaIndex": convert_int(excel_instance.ThemaIndex(), password),
        "ThemaType": excel_instance.ThemaType(),
        "ObjectType": excel_instance.ObjectType(),
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
        "TBGOptionSuccessType": excel_instance.TBGOptionSuccessType(),
        "Paremeter": convert_int(excel_instance.Paremeter(), password),
        "ParcelType": excel_instance.ParcelType(),
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "Amount": convert_int(excel_instance.Amount(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
    }

def dump_MinigameTBGItemExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "ItemType": excel_instance.ItemType(),
        "TBGItemEffectType": excel_instance.TBGItemEffectType(),
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
        "ObjectType": excel_instance.ObjectType(),
        "ObjectCostType": excel_instance.ObjectCostType(),
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
        "EventUseCostType": excel_instance.EventUseCostType(),
        "EventUseCostId": convert_int(excel_instance.EventUseCostId(), password),
        "EchelonRevivalCostType": excel_instance.EchelonRevivalCostType(),
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
        "ThemaType": excel_instance.ThemaType(),
        "ThemaMap": convert_string(excel_instance.ThemaMap(), password),
        "ThemaMapBG": convert_string(excel_instance.ThemaMapBG(), password),
        "PortalCondition": [excel_instance.PortalCondition(j) for j in range(excel_instance.PortalConditionLength())],
        "PortalConditionParameter": [convert_string(excel_instance.PortalConditionParameter(j), password) for j in range(excel_instance.PortalConditionParameterLength())],
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
        "MiniGameTBGThemaRewardType": excel_instance.MiniGameTBGThemaRewardType(),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_MinigameTBGVoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "VoiceCondition": excel_instance.VoiceCondition(),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_MissionEmergencyCompleteExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MissionId": convert_int(excel_instance.MissionId(), password),
        "EmergencyComplete": bool(excel_instance.EmergencyComplete()),
    }

def dump_MissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Category": excel_instance.Category(),
        "Description": convert_uint(excel_instance.Description(), password),
        "ResetType": excel_instance.ResetType(),
        "ToastDisplayType": excel_instance.ToastDisplayType(),
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ViewFlag": bool(excel_instance.ViewFlag()),
        "Limit": bool(excel_instance.Limit()),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "EndDay": convert_int(excel_instance.EndDay(), password),
        "StartableEndDate": convert_string(excel_instance.StartableEndDate(), password),
        "DateAutoRefer": excel_instance.DateAutoRefer(),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "TargetGroup": excel_instance.TargetGroup(),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ContentTags": [excel_instance.ContentTags(j) for j in range(excel_instance.ContentTagsLength())],
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "ChallengeStageShortcut": convert_int(excel_instance.ChallengeStageShortcut(), password),
        "CompleteConditionType": excel_instance.CompleteConditionType(),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [excel_instance.CompleteConditionParameterTag(j) for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "RewardIcon": convert_string(excel_instance.RewardIcon(), password),
        "MissionRewardParcelType": [excel_instance.MissionRewardParcelType(j) for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
    }

def dump_MomotalkScheduleSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "FavorScheduleId": convert_int(excel_instance.FavorScheduleId(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescription(), password),
        "PopupType": excel_instance.PopupType(),
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_MultiFloorRaidRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": excel_instance.ClearStageRewardParcelType(),
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_MultiFloorRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "LobbyEnterScenario": convert_uint(excel_instance.LobbyEnterScenario(), password),
        "ShowLobbyBanner": bool(excel_instance.ShowLobbyBanner()),
        "SeasonStartDate": convert_string(excel_instance.SeasonStartDate(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
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
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
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
        "BossCharacterId": [convert_int(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "StatChangeId": [convert_int(excel_instance.StatChangeId(j), password) for j in range(excel_instance.StatChangeIdLength())],
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevel(), password),
        "RewardGroupId": convert_int(excel_instance.RewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
    }

def dump_MultiFloorRaidStatChangeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StatChangeId": convert_int(excel_instance.StatChangeId(), password),
        "StatType": [excel_instance.StatType(j) for j in range(excel_instance.StatTypeLength())],
        "StatAdd": [convert_int(excel_instance.StatAdd(j), password) for j in range(excel_instance.StatAddLength())],
        "StatMultiply": [convert_int(excel_instance.StatMultiply(j), password) for j in range(excel_instance.StatMultiplyLength())],
        "ApplyCharacterId": [convert_int(excel_instance.ApplyCharacterId(j), password) for j in range(excel_instance.ApplyCharacterIdLength())],
    }

def dump_ObstacleFireLineCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "MyObstacleFireLineCheck": bool(excel_instance.MyObstacleFireLineCheck()),
        "AllyObstacleFireLineCheck": bool(excel_instance.AllyObstacleFireLineCheck()),
        "EnemyObstacleFireLineCheck": bool(excel_instance.EnemyObstacleFireLineCheck()),
        "EmptyObstacleFireLineCheck": bool(excel_instance.EmptyObstacleFireLineCheck()),
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
        "EnhanceCompositeArmorRate": convert_int(excel_instance.EnhanceCompositeArmorRate(), password),
        "EnhanceStructureRate": convert_int(excel_instance.EnhanceStructureRate(), password),
        "EnhanceNormalArmorRate": convert_int(excel_instance.EnhanceNormalArmorRate(), password),
        "ReduceExDamagedRate": convert_int(excel_instance.ReduceExDamagedRate(), password),
        "ReduceBasicsDamagedRate": convert_int(excel_instance.ReduceBasicsDamagedRate(), password),
        "ReduceWeakDamagedRate": convert_int(excel_instance.ReduceWeakDamagedRate(), password),
        "WeakDamagedRatio": convert_int(excel_instance.WeakDamagedRatio(), password),
        "EffectiveDamagedRatio": convert_int(excel_instance.EffectiveDamagedRatio(), password),
        "NormalDamagedRatio": convert_int(excel_instance.NormalDamagedRatio(), password),
        "ResistDamagedRatio": convert_int(excel_instance.ResistDamagedRatio(), password),
    }

def dump_OpenConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "OpenConditionContentType": excel_instance.OpenConditionContentType(),
        "LockUI": [convert_string(excel_instance.LockUI(j), password) for j in range(excel_instance.LockUILength())],
        "ShortcutPopupPriority": convert_int(excel_instance.ShortcutPopupPriority(), password),
        "ShortcutUIName": [convert_string(excel_instance.ShortcutUIName(j), password) for j in range(excel_instance.ShortcutUINameLength())],
        "ShortcutParam": convert_int(excel_instance.ShortcutParam(), password),
        "Scene": convert_string(excel_instance.Scene(), password),
        "HideWhenLocked": bool(excel_instance.HideWhenLocked()),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "CampaignStageId": convert_int(excel_instance.CampaignStageId(), password),
        "MultipleConditionCheckType": excel_instance.MultipleConditionCheckType(),
        "OpenDayOfWeek": excel_instance.OpenDayOfWeek(),
        "OpenHour": convert_int(excel_instance.OpenHour(), password),
        "CloseDayOfWeek": excel_instance.CloseDayOfWeek(),
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
        "OperatorCondition": excel_instance.OperatorCondition(),
        "OutputSequence": convert_int(excel_instance.OutputSequence(), password),
        "RandomWeight": convert_int(excel_instance.RandomWeight(), password),
        "OutputDelay": convert_int(excel_instance.OutputDelay(), password),
        "Duration": convert_int(excel_instance.Duration(), password),
        "OperatorOutputPriority": convert_int(excel_instance.OperatorOutputPriority(), password),
        "PortraitPath": convert_string(excel_instance.PortraitPath(), password),
        "TextLocalizeKey": convert_string(excel_instance.TextLocalizeKey(), password),
        "VoiceId": [convert_uint(excel_instance.VoiceId(j), password) for j in range(excel_instance.VoiceIdLength())],
        "OperatorWaitQueue": bool(excel_instance.OperatorWaitQueue()),
        "CharacterVoiceOverridePriority": excel_instance.CharacterVoiceOverridePriority(),
    }

def dump_ParcelAutoSynthExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RequireParcelType": excel_instance.RequireParcelType(),
        "RequireParcelId": convert_int(excel_instance.RequireParcelId(), password),
        "RequireParcelAmount": convert_int(excel_instance.RequireParcelAmount(), password),
        "SynthStartAmount": convert_int(excel_instance.SynthStartAmount(), password),
        "SynthEndAmount": convert_int(excel_instance.SynthEndAmount(), password),
        "SynthMaxItem": bool(excel_instance.SynthMaxItem()),
        "ResultParcelType": excel_instance.ResultParcelType(),
        "ResultParcelId": convert_int(excel_instance.ResultParcelId(), password),
        "ResultParcelAmount": convert_int(excel_instance.ResultParcelAmount(), password),
    }

def dump_PermanentRaidManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Type": excel_instance.Type(),
        "OpenRaidBossGroup": [convert_string(excel_instance.OpenRaidBossGroup(j), password) for j in range(excel_instance.OpenRaidBossGroupLength())],
        "HideDifficulty": [convert_string(excel_instance.HideDifficulty(j), password) for j in range(excel_instance.HideDifficultyLength())],
        "OpenDate": convert_string(excel_instance.OpenDate(), password),
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
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_PickupFirstGetBonus2Excel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ShopRecruitId": convert_int(excel_instance.ShopRecruitId(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopId(), password),
        "PickupCharacterId": convert_int(excel_instance.PickupCharacterId(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_PickupFirstGetBonusExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ShopRecruitId": convert_int(excel_instance.ShopRecruitId(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopId(), password),
        "PickupCharacterId": convert_int(excel_instance.PickupCharacterId(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
    }

def dump_PossessionCheckExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "DefaultParcelType": excel_instance.DefaultParcelType(),
        "DefaultParcelId": convert_int(excel_instance.DefaultParcelId(), password),
        "DefaultParcelAmount": convert_int(excel_instance.DefaultParcelAmount(), password),
        "ReplaceParcelType": excel_instance.ReplaceParcelType(),
        "ReplaceParcelId": convert_int(excel_instance.ReplaceParcelId(), password),
        "ReplaceParcelAmount": convert_int(excel_instance.ReplaceParcelAmount(), password),
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
        "PotentialType01": excel_instance.PotentialType01(),
        "PotentialLevel01": convert_int(excel_instance.PotentialLevel01(), password),
        "PotentialType02": excel_instance.PotentialType02(),
        "PotentialLevel02": convert_int(excel_instance.PotentialLevel02(), password),
        "PotentialType03": excel_instance.PotentialType03(),
        "PotentialLevel03": convert_int(excel_instance.PotentialLevel03(), password),
    }

def dump_PresetCharacterGroupSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "ArenaSimulatorFixed": bool(excel_instance.ArenaSimulatorFixed()),
        "PresetType": [convert_string(excel_instance.PresetType(j), password) for j in range(excel_instance.PresetTypeLength())],
    }

def dump_PresetParcelsExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ParcelType": excel_instance.ParcelType(),
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "PresetGroupId": convert_int(excel_instance.PresetGroupId(), password),
        "ParcelAmount": convert_int(excel_instance.ParcelAmount(), password),
    }

def dump_ProductAutoSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ProductAutoSelectionGroupId": convert_int(excel_instance.ProductAutoSelectionGroupId(), password),
        "CharacterId": convert_int(excel_instance.CharacterId(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "ResultAmount": [convert_int(excel_instance.ResultAmount(j), password) for j in range(excel_instance.ResultAmountLength())],
        "ConditionParcelType": excel_instance.ConditionParcelType(),
        "ConditionParcelId": convert_int(excel_instance.ConditionParcelId(), password),
    }

def dump_ProductBattlePassExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductId(), password),
        "StoreType": excel_instance.StoreType(),
        "Price": convert_int(excel_instance.Price(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "BattlePassProductGroupId": convert_int(excel_instance.BattlePassProductGroupId(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_ProductDailyRecordExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductId(), password),
        "StoreType": excel_instance.StoreType(),
        "Price": convert_int(excel_instance.Price(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
        "TitleImagePath": convert_string(excel_instance.TitleImagePath(), password),
    }

def dump_ProductDailyRecordInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DaySize": convert_int(excel_instance.DaySize(), password),
        "ExpirationDate": convert_string(excel_instance.ExpirationDate(), password),
    }

def dump_ProductDailyRecordRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Day": convert_int(excel_instance.Day(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardId": [convert_int(excel_instance.RewardId(j), password) for j in range(excel_instance.RewardIdLength())],
        "RewardAmount": [convert_int(excel_instance.RewardAmount(j), password) for j in range(excel_instance.RewardAmountLength())],
    }

def dump_ProductExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductId(), password),
        "StoreType": excel_instance.StoreType(),
        "Price": convert_int(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "PurchasePeriodType": excel_instance.PurchasePeriodType(),
        "PurchasePeriodLimit": convert_int(excel_instance.PurchasePeriodLimit(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
    }

def dump_ProductMonthlyExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductId(), password),
        "StoreType": excel_instance.StoreType(),
        "Price": convert_int(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "ProductTagType": excel_instance.ProductTagType(),
        "MonthlyDays": convert_int(excel_instance.MonthlyDays(), password),
        "UseMonthlyProductCheck": bool(excel_instance.UseMonthlyProductCheck()),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
        "EnterCostReduceGroupId": convert_int(excel_instance.EnterCostReduceGroupId(), password),
        "DailyParcelType": [excel_instance.DailyParcelType(j) for j in range(excel_instance.DailyParcelTypeLength())],
        "DailyParcelId": [convert_int(excel_instance.DailyParcelId(j), password) for j in range(excel_instance.DailyParcelIdLength())],
        "DailyParcelAmount": [convert_int(excel_instance.DailyParcelAmount(j), password) for j in range(excel_instance.DailyParcelAmountLength())],
    }

def dump_ProductSelectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ProductSelectSubType": excel_instance.ProductSelectSubType(),
        "AutoSelectPopupType": excel_instance.AutoSelectPopupType(),
        "ProductId": convert_string(excel_instance.ProductId(), password),
        "TeenProductId": convert_string(excel_instance.TeenProductId(), password),
        "StoreType": excel_instance.StoreType(),
        "Price": convert_int(excel_instance.Price(), password),
        "PriceReference": convert_string(excel_instance.PriceReference(), password),
        "PurchasePeriodType": excel_instance.PurchasePeriodType(),
        "PurchasePeriodLimit": convert_int(excel_instance.PurchasePeriodLimit(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ParcelAmount": [convert_int(excel_instance.ParcelAmount(j), password) for j in range(excel_instance.ParcelAmountLength())],
        "ProductSelectionSlot": [convert_int(excel_instance.ProductSelectionSlot(j), password) for j in range(excel_instance.ProductSelectionSlotLength())],
    }

def dump_ProductSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ProductSelectionGroupId": convert_int(excel_instance.ProductSelectionGroupId(), password),
        "ProductSelectionGroupComponentId": convert_int(excel_instance.ProductSelectionGroupComponentId(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ParcelType": excel_instance.ParcelType(),
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "ResultAmount": convert_int(excel_instance.ResultAmount(), password),
        "ConditionParcelType": excel_instance.ConditionParcelType(),
        "ConditionParcelId": convert_int(excel_instance.ConditionParcelId(), password),
    }

def dump_RaidContentPlayGuideExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RaidBossGroupType": excel_instance.RaidBossGroupType(),
        "IsPCBuild": bool(excel_instance.IsPCBuild()),
        "IdExport": bool(excel_instance.IdExport()),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GuideTitle": convert_uint(excel_instance.GuideTitle(), password),
        "GuideImagePath": convert_string(excel_instance.GuideImagePath(), password),
        "GuideText": convert_uint(excel_instance.GuideText(), password),
    }

def dump_RaidRankingRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "RankStart": convert_int(excel_instance.RankStart(), password),
        "RankEnd": convert_int(excel_instance.RankEnd(), password),
        "RankStartTw": convert_int(excel_instance.RankStartTw(), password),
        "RankEndTw": convert_int(excel_instance.RankEndTw(), password),
        "RankStartAsia": convert_int(excel_instance.RankStartAsia(), password),
        "RankEndAsia": convert_int(excel_instance.RankEndAsia(), password),
        "RankStartNa": convert_int(excel_instance.RankStartNa(), password),
        "RankEndNa": convert_int(excel_instance.RankEndNa(), password),
        "RankStartGlobal": convert_int(excel_instance.RankStartGlobal(), password),
        "RankEndGlobal": convert_int(excel_instance.RankEndGlobal(), password),
        "PercentRankStart": convert_int(excel_instance.PercentRankStart(), password),
        "PercentRankEnd": convert_int(excel_instance.PercentRankEnd(), password),
        "Tier": convert_int(excel_instance.Tier(), password),
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelUniqueId": [convert_int(excel_instance.RewardParcelUniqueId(j), password) for j in range(excel_instance.RewardParcelUniqueIdLength())],
        "RewardParcelAmount": [convert_int(excel_instance.RewardParcelAmount(j), password) for j in range(excel_instance.RewardParcelAmountLength())],
    }

def dump_RaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "SeasonDisplay": convert_int(excel_instance.SeasonDisplay(), password),
        "SeasonStartData": convert_string(excel_instance.SeasonStartData(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "SeasonEndData": convert_string(excel_instance.SeasonEndData(), password),
        "SettlementEndDate": convert_string(excel_instance.SettlementEndDate(), password),
        "OpenRaidBossGroup": [convert_string(excel_instance.OpenRaidBossGroup(j), password) for j in range(excel_instance.OpenRaidBossGroupLength())],
        "RankingRewardGroupId": convert_int(excel_instance.RankingRewardGroupId(), password),
        "MaxSeasonRewardGauage": convert_int(excel_instance.MaxSeasonRewardGauage(), password),
        "StackedSeasonRewardGauge": [convert_int(excel_instance.StackedSeasonRewardGauge(j), password) for j in range(excel_instance.StackedSeasonRewardGaugeLength())],
        "SeasonRewardId": [convert_int(excel_instance.SeasonRewardId(j), password) for j in range(excel_instance.SeasonRewardIdLength())],
    }

def dump_RaidSkillDescriptionListExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "BossGroup": convert_string(excel_instance.BossGroup(), password),
        "Difficulty": convert_string(excel_instance.Difficulty(), password),
        "PhaseNameOverrideKey": convert_string(excel_instance.PhaseNameOverrideKey(), password),
        "SkillGroupId": [convert_string(excel_instance.SkillGroupId(j), password) for j in range(excel_instance.SkillGroupIdLength())],
        "SkillUsePhase": [convert_int(excel_instance.SkillUsePhase(j), password) for j in range(excel_instance.SkillUsePhaseLength())],
        "ShowSkillSlot": [excel_instance.ShowSkillSlot(j) for j in range(excel_instance.ShowSkillSlotLength())],
        "HighlightResource": [excel_instance.HighlightResource(j) for j in range(excel_instance.HighlightResourceLength())],
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
        "BossCharacterId": [convert_int(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "Difficulty": excel_instance.Difficulty(),
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenCondition()),
        "MaxPlayerCount": convert_int(excel_instance.MaxPlayerCount(), password),
        "RaidRoomLifeTime": convert_int(excel_instance.RaidRoomLifeTime(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RaidBossGroupType": excel_instance.RaidBossGroupType(),
        "EnterTimeLine": convert_string(excel_instance.EnterTimeLine(), password),
        "TacticEnvironment": excel_instance.TacticEnvironment(),
        "DefaultClearScore": convert_int(excel_instance.DefaultClearScore(), password),
        "MaximumScore": convert_int(excel_instance.MaximumScore(), password),
        "PerSecondMinusScore": convert_int(excel_instance.PerSecondMinusScore(), password),
        "HPPercentScore": convert_int(excel_instance.HPPercentScore(), password),
        "MinimumAcquisitionScore": convert_int(excel_instance.MinimumAcquisitionScore(), password),
        "MaximumAcquisitionScore": convert_int(excel_instance.MaximumAcquisitionScore(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
        "VictoryTimelinePath": convert_string(excel_instance.VictoryTimelinePath(), password),
        "PhaseChangeTimelinePath": convert_string(excel_instance.PhaseChangeTimelinePath(), password),
        "TimeLinePhase": convert_int(excel_instance.TimeLinePhase(), password),
        "EnterScenarioKey": convert_uint(excel_instance.EnterScenarioKey(), password),
        "ClearScenarioKey": convert_uint(excel_instance.ClearScenarioKey(), password),
        "ShowSkillCard": bool(excel_instance.ShowSkillCard()),
        "BossBGInfoKey": convert_uint(excel_instance.BossBGInfoKey(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_RaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": excel_instance.ClearStageRewardParcelType(),
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_RaidStageSeasonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonRewardId": convert_int(excel_instance.SeasonRewardId(), password),
        "SeasonRewardParcelType": [excel_instance.SeasonRewardParcelType(j) for j in range(excel_instance.SeasonRewardParcelTypeLength())],
        "SeasonRewardParcelUniqueId": [convert_int(excel_instance.SeasonRewardParcelUniqueId(j), password) for j in range(excel_instance.SeasonRewardParcelUniqueIdLength())],
        "SeasonRewardAmount": [convert_int(excel_instance.SeasonRewardAmount(j), password) for j in range(excel_instance.SeasonRewardAmountLength())],
    }

def dump_RecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RecipeType": excel_instance.RecipeType(),
        "RecipeIngredientId": convert_int(excel_instance.RecipeIngredientId(), password),
        "RecipeSelectionGroupId": convert_int(excel_instance.RecipeSelectionGroupId(), password),
        "ParcelType": [excel_instance.ParcelType(j) for j in range(excel_instance.ParcelTypeLength())],
        "ParcelId": [convert_int(excel_instance.ParcelId(j), password) for j in range(excel_instance.ParcelIdLength())],
        "ResultAmountMin": [convert_int(excel_instance.ResultAmountMin(j), password) for j in range(excel_instance.ResultAmountMinLength())],
        "ResultAmountMax": [convert_int(excel_instance.ResultAmountMax(j), password) for j in range(excel_instance.ResultAmountMaxLength())],
    }

def dump_RecipeIngredientExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RecipeType": excel_instance.RecipeType(),
        "CostParcelType": [excel_instance.CostParcelType(j) for j in range(excel_instance.CostParcelTypeLength())],
        "CostId": [convert_int(excel_instance.CostId(j), password) for j in range(excel_instance.CostIdLength())],
        "CostAmount": [convert_int(excel_instance.CostAmount(j), password) for j in range(excel_instance.CostAmountLength())],
        "IngredientParcelType": [excel_instance.IngredientParcelType(j) for j in range(excel_instance.IngredientParcelTypeLength())],
        "IngredientId": [convert_int(excel_instance.IngredientId(j), password) for j in range(excel_instance.IngredientIdLength())],
        "IngredientAmount": [convert_int(excel_instance.IngredientAmount(j), password) for j in range(excel_instance.IngredientAmountLength())],
        "CostTimeInSecond": convert_int(excel_instance.CostTimeInSecond(), password),
    }

def dump_RecipeSelectionAutoUseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ParcelType": excel_instance.ParcelType(),
        "TargetItemId": convert_int(excel_instance.TargetItemId(), password),
        "Priority": [convert_int(excel_instance.Priority(j), password) for j in range(excel_instance.PriorityLength())],
    }

def dump_RecipeSelectionGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "RecipeSelectionGroupId": convert_int(excel_instance.RecipeSelectionGroupId(), password),
        "RecipeSelectionGroupComponentId": convert_int(excel_instance.RecipeSelectionGroupComponentId(), password),
        "ParcelType": excel_instance.ParcelType(),
        "ParcelId": convert_int(excel_instance.ParcelId(), password),
        "ResultAmountMin": convert_int(excel_instance.ResultAmountMin(), password),
        "ResultAmountMax": convert_int(excel_instance.ResultAmountMax(), password),
    }

def dump_ScenarioBGEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "Effect": convert_string(excel_instance.Effect(), password),
        "Effect2": convert_string(excel_instance.Effect2(), password),
        "Scroll": excel_instance.Scroll(),
        "ScrollTime": convert_int(excel_instance.ScrollTime(), password),
        "ScrollFrom": convert_int(excel_instance.ScrollFrom(), password),
        "ScrollTo": convert_int(excel_instance.ScrollTo(), password),
    }

def dump_ScenarioBGNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Name": convert_uint(excel_instance.Name(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "BGFileName": convert_string(excel_instance.BGFileName(), password),
        "BGType": excel_instance.BGType(),
        "AnimationRoot": convert_string(excel_instance.AnimationRoot(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "SpineScale": convert_float(excel_instance.SpineScale(), password),
        "SpineLocalPosX": convert_int(excel_instance.SpineLocalPosX(), password),
        "SpineLocalPosY": convert_int(excel_instance.SpineLocalPosY(), password),
    }

def dump_ScenarioBGName_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupName": convert_uint(excel_instance.GroupName(), password),
        "NameKr": convert_uint(excel_instance.NameKr(), password),
        "NameTw": convert_uint(excel_instance.NameTw(), password),
        "NameAsia": convert_uint(excel_instance.NameAsia(), password),
        "NameNa": convert_uint(excel_instance.NameNa(), password),
        "NameGlobal": convert_uint(excel_instance.NameGlobal(), password),
        "NameTeen": convert_uint(excel_instance.NameTeen(), password),
    }

def dump_ScenarioCharacterEmotionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "EmoticonName": convert_string(excel_instance.EmoticonName(), password),
        "Name": convert_uint(excel_instance.Name(), password),
    }

def dump_ScenarioCharacterNameExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CharacterName": convert_uint(excel_instance.CharacterName(), password),
        "ProductionStep": excel_instance.ProductionStep(),
        "NameKR": convert_string(excel_instance.NameKR(), password),
        "NicknameKR": convert_string(excel_instance.NicknameKR(), password),
        "NameJP": convert_string(excel_instance.NameJP(), password),
        "NicknameJP": convert_string(excel_instance.NicknameJP(), password),
        "NameTH": convert_string(excel_instance.NameTH(), password),
        "NicknameTH": convert_string(excel_instance.NicknameTH(), password),
        "NameTW": convert_string(excel_instance.NameTW(), password),
        "NicknameTW": convert_string(excel_instance.NicknameTW(), password),
        "NameEN": convert_string(excel_instance.NameEN(), password),
        "NicknameEN": convert_string(excel_instance.NicknameEN(), password),
        "Shape": excel_instance.Shape(),
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
        "UnlockConditionType": excel_instance.UnlockConditionType(),
        "UnlockConditionParameter": [convert_int(excel_instance.UnlockConditionParameter(j), password) for j in range(excel_instance.UnlockConditionParameterLength())],
        "MultipleConditionCheckType": excel_instance.MultipleConditionCheckType(),
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
        "ModeType": excel_instance.ModeType(),
        "SubType": excel_instance.SubType(),
        "DisplayVolumeId": convert_string(excel_instance.DisplayVolumeId(), password),
        "VolumeId": convert_int(excel_instance.VolumeId(), password),
        "ChapterId": convert_int(excel_instance.ChapterId(), password),
        "EpisodeId": convert_int(excel_instance.EpisodeId(), password),
        "ExposedTime": convert_string(excel_instance.ExposedTime(), password),
        "Hide": bool(excel_instance.Hide()),
        "Open": bool(excel_instance.Open()),
        "ScenarioOpenDate": convert_string(excel_instance.ScenarioOpenDate(), password),
        "ScenarioCloseDate": convert_string(excel_instance.ScenarioCloseDate(), password),
        "IsContinue": bool(excel_instance.IsContinue()),
        "EpisodeContinueModeId": convert_int(excel_instance.EpisodeContinueModeId(), password),
        "FrontScenarioGroupId": [convert_int(excel_instance.FrontScenarioGroupId(j), password) for j in range(excel_instance.FrontScenarioGroupIdLength())],
        "StrategyId": convert_int(excel_instance.StrategyId(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "IsDefeatBattle": bool(excel_instance.IsDefeatBattle()),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "FieldDateId": convert_int(excel_instance.FieldDateId(), password),
        "BackScenarioGroupId": [convert_int(excel_instance.BackScenarioGroupId(j), password) for j in range(excel_instance.BackScenarioGroupIdLength())],
        "ClearedModeId": [convert_int(excel_instance.ClearedModeId(j), password) for j in range(excel_instance.ClearedModeIdLength())],
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardId(), password),
        "IsScenarioSpecialReward": bool(excel_instance.IsScenarioSpecialReward()),
        "SpecialRewardPrefabName": convert_string(excel_instance.SpecialRewardPrefabName(), password),
        "SpecialRewardLogOut": bool(excel_instance.SpecialRewardLogOut()),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimit(), password),
        "ClearedStageId": convert_int(excel_instance.ClearedStageId(), password),
        "NeedClub": excel_instance.NeedClub(),
        "NeedClubStudentCount": convert_int(excel_instance.NeedClubStudentCount(), password),
        "EventContentId": convert_int(excel_instance.EventContentId(), password),
        "EventContentType": excel_instance.EventContentType(),
        "EventContentCondition": convert_int(excel_instance.EventContentCondition(), password),
        "EventContentConditionGroup": convert_int(excel_instance.EventContentConditionGroup(), password),
        "MapDifficulty": excel_instance.MapDifficulty(),
        "StepIndex": convert_int(excel_instance.StepIndex(), password),
        "RecommendLevel": convert_int(excel_instance.RecommendLevel(), password),
        "EventIconParcelPath": convert_string(excel_instance.EventIconParcelPath(), password),
        "EventBannerTitle": convert_uint(excel_instance.EventBannerTitle(), password),
        "Lof": bool(excel_instance.Lof()),
        "StageTopography": excel_instance.StageTopography(),
        "FixedEchelonId": convert_int(excel_instance.FixedEchelonId(), password),
        "CompleteReportEventName": convert_string(excel_instance.CompleteReportEventName(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
        "CollectionGroupId": convert_int(excel_instance.CollectionGroupId(), password),
        "FirstClearFunnelMessage": convert_string(excel_instance.FirstClearFunnelMessage(), password),
    }

def dump_ScenarioModeRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ScenarioModeRewardId": convert_int(excel_instance.ScenarioModeRewardId(), password),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardProb": convert_int(excel_instance.RewardProb(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_ScenarioModeSpoilerPopupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ModeType": excel_instance.ModeType(),
        "SubType": excel_instance.SubType(),
        "VolumeId": convert_int(excel_instance.VolumeId(), password),
        "ChapterId": convert_int(excel_instance.ChapterId(), password),
        "SpoilerPopupTitle": convert_uint(excel_instance.SpoilerPopupTitle(), password),
        "SpoilerPopupDescription": convert_uint(excel_instance.SpoilerPopupDescription(), password),
        "PopupType": excel_instance.PopupType(),
        "ConditionScenarioModeId": convert_int(excel_instance.ConditionScenarioModeId(), password),
    }

def dump_ScenarioResourceInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ScenarioModeId": convert_int(excel_instance.ScenarioModeId(), password),
        "PriorityOrder": convert_int(excel_instance.PriorityOrder(), password),
        "PVDisplayOrder": convert_int(excel_instance.PVDisplayOrder(), password),
        "VideoId": convert_int(excel_instance.VideoId(), password),
        "BgmId": convert_int(excel_instance.BgmId(), password),
        "AudioName": convert_string(excel_instance.AudioName(), password),
        "SpinePath": convert_string(excel_instance.SpinePath(), password),
        "Ratio": convert_int(excel_instance.Ratio(), password),
        "LobbyAniPath": convert_string(excel_instance.LobbyAniPath(), password),
        "MovieCGPath": convert_string(excel_instance.MovieCGPath(), password),
        "ScenarioForceEnter": excel_instance.ScenarioForceEnter(),
        "LocalizeId": convert_uint(excel_instance.LocalizeId(), password),
        "AcademyLobbyCharacterId": [convert_int(excel_instance.AcademyLobbyCharacterId(j), password) for j in range(excel_instance.AcademyLobbyCharacterIdLength())],
        "SweepAnimation": [convert_string(excel_instance.SweepAnimation(j), password) for j in range(excel_instance.SweepAnimationLength())],
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
        "TextTh": convert_string(excel_instance.TextTh(), password),
        "TextTw": convert_string(excel_instance.TextTw(), password),
        "TextEn": convert_string(excel_instance.TextEn(), password),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
        "TeenMode": bool(excel_instance.TeenMode()),
    }

def dump_ScenarioScriptFunnelExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "Index": convert_int(excel_instance.Index(), password),
        "FunnelId": convert_string(excel_instance.FunnelId(), password),
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
        "DungeonType": excel_instance.DungeonType(),
        "RewardTag": convert_float(excel_instance.RewardTag(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
    }

def dump_SchoolDungeonStageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageId(), password),
        "DungeonType": excel_instance.DungeonType(),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "StageEnterCostType": [excel_instance.StageEnterCostType(j) for j in range(excel_instance.StageEnterCostTypeLength())],
        "StageEnterCostId": [convert_int(excel_instance.StageEnterCostId(j), password) for j in range(excel_instance.StageEnterCostIdLength())],
        "StageEnterCostAmount": [convert_int(excel_instance.StageEnterCostAmount(j), password) for j in range(excel_instance.StageEnterCostAmountLength())],
        "StageEnterCostMinimumAmount": [convert_int(excel_instance.StageEnterCostMinimumAmount(j), password) for j in range(excel_instance.StageEnterCostMinimumAmountLength())],
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoal": [excel_instance.StarGoal(j) for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_ServiceActionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ServiceActionType": excel_instance.ServiceActionType(),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
    }

def dump_ShiftingCraftRecipeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "NotificationId": convert_int(excel_instance.NotificationId(), password),
        "ResultParcel": excel_instance.ResultParcel(),
        "ResultId": convert_int(excel_instance.ResultId(), password),
        "ResultAmount": convert_int(excel_instance.ResultAmount(), password),
        "RequireItemId": convert_int(excel_instance.RequireItemId(), password),
        "RequireItemAmount": convert_int(excel_instance.RequireItemAmount(), password),
        "RequireGold": convert_int(excel_instance.RequireGold(), password),
        "AdditionalCostParcelType": excel_instance.AdditionalCostParcelType(),
        "AdditionalCostParcelId": convert_int(excel_instance.AdditionalCostParcelId(), password),
        "AdditionalCostParcelAmount": convert_int(excel_instance.AdditionalCostParcelAmount(), password),
        "IngredientTag": [excel_instance.IngredientTag(j) for j in range(excel_instance.IngredientTagLength())],
        "IngredientExp": convert_int(excel_instance.IngredientExp(), password),
        "RecipeDisplayOptions": excel_instance.RecipeDisplayOptions(),
    }

def dump_ShopCashExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CashProductId": convert_int(excel_instance.CashProductId(), password),
        "PackageType": excel_instance.PackageType(),
        "TargetGroup": excel_instance.TargetGroup(),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "InMailPurchaseLock": bool(excel_instance.InMailPurchaseLock()),
        "UseMailParcel": bool(excel_instance.UseMailParcel()),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "RenewalDisplayOrder": convert_int(excel_instance.RenewalDisplayOrder(), password),
        "CategoryType": excel_instance.CategoryType(),
        "DisplayTag": excel_instance.DisplayTag(),
        "ProductSaleType": excel_instance.ProductSaleType(),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "ProductSaleDay": convert_int(excel_instance.ProductSaleDay(), password),
        "PeriodTag": bool(excel_instance.PeriodTag()),
        "AccountLevelLimit": convert_int(excel_instance.AccountLevelLimit(), password),
        "AccountLevelHide": bool(excel_instance.AccountLevelHide()),
        "ClearMissionLimit": convert_int(excel_instance.ClearMissionLimit(), password),
        "ClearMissionHide": bool(excel_instance.ClearMissionHide()),
        "PurchaseReportEventName": convert_string(excel_instance.PurchaseReportEventName(), password),
        "PackageClientType": excel_instance.PackageClientType(),
        "IsStartDash": bool(excel_instance.IsStartDash()),
        "ViewFlag": bool(excel_instance.ViewFlag()),
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
        "UseBigPopup": bool(excel_instance.UseBigPopup()),
        "GoodsId": [convert_int(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": excel_instance.PurchaseCountResetType(),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "RestrictBuyWhenInventoryFull": bool(excel_instance.RestrictBuyWhenInventoryFull()),
        "DisplayTag": excel_instance.DisplayTag(),
        "ShopUpdateGroupId": convert_int(excel_instance.ShopUpdateGroupId(), password),
    }

def dump_ShopFilterClassifiedExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "ConsumeParcelType": excel_instance.ConsumeParcelType(),
        "ConsumeParcelId": convert_int(excel_instance.ConsumeParcelId(), password),
        "ShopFilterType": excel_instance.ShopFilterType(),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
    }

def dump_ShopFreeRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "FreeRecruitPeriodFrom": convert_string(excel_instance.FreeRecruitPeriodFrom(), password),
        "FreeRecruitPeriodTo": convert_string(excel_instance.FreeRecruitPeriodTo(), password),
        "FreeRecruitType": excel_instance.FreeRecruitType(),
        "FreeRecruitDecorationImagePath": convert_string(excel_instance.FreeRecruitDecorationImagePath(), password),
        "TenRecruitCountOnly": bool(excel_instance.TenRecruitCountOnly()),
        "ShopRecruitId": [convert_int(excel_instance.ShopRecruitId(j), password) for j in range(excel_instance.ShopRecruitIdLength())],
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
        "CostParcelType": [excel_instance.CostParcelType(j) for j in range(excel_instance.CostParcelTypeLength())],
        "CostParcelId": [convert_int(excel_instance.CostParcelId(j), password) for j in range(excel_instance.CostParcelIdLength())],
        "AutoRefreshCoolTime": convert_int(excel_instance.AutoRefreshCoolTime(), password),
        "ShopRefresherType": excel_instance.ShopRefresherType(),
        "ShopRefreshPeriodType": excel_instance.ShopRefreshPeriodType(),
        "RefreshAbleCount": convert_int(excel_instance.RefreshAbleCount(), password),
        "GoodsId": [convert_int(excel_instance.GoodsId(j), password) for j in range(excel_instance.GoodsIdLength())],
        "OpenPeriodFrom": convert_string(excel_instance.OpenPeriodFrom(), password),
        "OpenPeriodTo": convert_string(excel_instance.OpenPeriodTo(), password),
        "RefreshPeriodBaseTime": convert_string(excel_instance.RefreshPeriodBaseTime(), password),
        "ShopProductUpdateTime": convert_string(excel_instance.ShopProductUpdateTime(), password),
        "DisplayParcelType": excel_instance.DisplayParcelType(),
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

def dump_ShopRecruitDirectingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Path": convert_string(excel_instance.Path(), password),
        "Phase": excel_instance.Phase(),
        "GachaAmount": convert_int(excel_instance.GachaAmount(), password),
        "IsSSR": bool(excel_instance.IsSSR()),
        "Character": excel_instance.Character(),
    }

def dump_ShopRecruitExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "OneGachaGoodsId": convert_int(excel_instance.OneGachaGoodsId(), password),
        "TenGachaGoodsId": convert_int(excel_instance.TenGachaGoodsId(), password),
        "GoodsDevName": convert_string(excel_instance.GoodsDevName(), password),
        "DisplayTag": excel_instance.DisplayTag(),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "GachaBannerPath": convert_string(excel_instance.GachaBannerPath(), password),
        "VideoId": [convert_int(excel_instance.VideoId(j), password) for j in range(excel_instance.VideoIdLength())],
        "LinkedRobbyBannerId": convert_int(excel_instance.LinkedRobbyBannerId(), password),
        "InfoCharacterId": [convert_int(excel_instance.InfoCharacterId(j), password) for j in range(excel_instance.InfoCharacterIdLength())],
        "SalePeriodVisible": bool(excel_instance.SalePeriodVisible()),
        "SalePeriodFrom": convert_string(excel_instance.SalePeriodFrom(), password),
        "SalePeriodTo": convert_string(excel_instance.SalePeriodTo(), password),
        "RecruitCoinId": convert_int(excel_instance.RecruitCoinId(), password),
        "RecruitSellectionShopId": convert_int(excel_instance.RecruitSellectionShopId(), password),
        "PurchaseCooltimeMin": convert_int(excel_instance.PurchaseCooltimeMin(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "PurchaseCountResetType": excel_instance.PurchaseCountResetType(),
        "SalePeriodDayParameter": convert_int(excel_instance.SalePeriodDayParameter(), password),
        "IsOverrideSalePeriodTo": bool(excel_instance.IsOverrideSalePeriodTo()),
        "IsNewbie": bool(excel_instance.IsNewbie()),
        "IsSelectRecruit": bool(excel_instance.IsSelectRecruit()),
        "DirectPayInvisibleTokenId": convert_int(excel_instance.DirectPayInvisibleTokenId(), password),
        "DirectPayProductId": convert_string(excel_instance.DirectPayProductId(), password),
        "DirectPayAndroidShopCashId": convert_int(excel_instance.DirectPayAndroidShopCashId(), password),
        "DirectPayAppleShopCashId": convert_int(excel_instance.DirectPayAppleShopCashId(), password),
        "SelectAbleGachaGroupId": convert_int(excel_instance.SelectAbleGachaGroupId(), password),
        "MaxSelectCharacterNum": convert_int(excel_instance.MaxSelectCharacterNum(), password),
        "DirectPayOneStoreShopCashId": convert_int(excel_instance.DirectPayOneStoreShopCashId(), password),
        "ProbabilityUrlDev": convert_string(excel_instance.ProbabilityUrlDev(), password),
        "ProbabilityUrlLive": convert_string(excel_instance.ProbabilityUrlLive(), password),
    }

def dump_ShopRecruitSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RecruitChangeScenarioModeID": convert_int(excel_instance.RecruitChangeScenarioModeID(), password),
        "PriorityOrder": convert_int(excel_instance.PriorityOrder(), password),
        "TogetherPercentage": convert_int(excel_instance.TogetherPercentage(), password),
        "AnotherPercentage": convert_int(excel_instance.AnotherPercentage(), password),
        "TwistPercentage": convert_int(excel_instance.TwistPercentage(), password),
        "RecruitChangeIcon": convert_string(excel_instance.RecruitChangeIcon(), password),
        "SeriesForceEnter": excel_instance.SeriesForceEnter(),
    }

def dump_ShopRefreshExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LocalizeEtcId": convert_uint(excel_instance.LocalizeEtcId(), password),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "GoodsId": convert_int(excel_instance.GoodsId(), password),
        "IsBundle": bool(excel_instance.IsBundle()),
        "ShopPurchasePopupType": excel_instance.ShopPurchasePopupType(),
        "VisibleAmount": convert_int(excel_instance.VisibleAmount(), password),
        "PurchaseCountLimit": convert_int(excel_instance.PurchaseCountLimit(), password),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "CategoryType": convert_float(excel_instance.CategoryType(), password),
        "RefreshGroup": convert_int(excel_instance.RefreshGroup(), password),
        "Prob": convert_int(excel_instance.Prob(), password),
        "BuyReportEventName": convert_string(excel_instance.BuyReportEventName(), password),
        "ProductUpdateTime": convert_string(excel_instance.ProductUpdateTime(), password),
        "DisplayTag": excel_instance.DisplayTag(),
    }

def dump_ShopTabGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "ShopGroupType": excel_instance.ShopGroupType(),
        "DisplayOrder": convert_int(excel_instance.DisplayOrder(), password),
        "ShopCategoryTypes": [convert_float(excel_instance.ShopCategoryTypes(j), password) for j in range(excel_instance.ShopCategoryTypesLength())],
    }

def dump_ShortcutTypeExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "IsAscending": bool(excel_instance.IsAscending()),
        "ContentType": [excel_instance.ContentType(j) for j in range(excel_instance.ContentTypeLength())],
    }

def dump_SkillAdditionalTooltipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "AdditionalSkillGroupId": convert_string(excel_instance.AdditionalSkillGroupId(), password),
        "ShowSkillSlot": convert_string(excel_instance.ShowSkillSlot(), password),
        "DisplayIconBg": bool(excel_instance.DisplayIconBg()),
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
        "BulletType": excel_instance.BulletType(),
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
        "SelectExSkillToolTipId": convert_int(excel_instance.SelectExSkillToolTipId(), password),
        "TextureSkillCardForFormConversion": convert_string(excel_instance.TextureSkillCardForFormConversion(), password),
        "SkillCardLabelPath": convert_string(excel_instance.SkillCardLabelPath(), password),
    }

def dump_SkillSelectExTooltipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "SelectableExSkillGroupId": convert_string(excel_instance.SelectableExSkillGroupId(), password),
        "SkillUseConditionLocalizeId": convert_string(excel_instance.SkillUseConditionLocalizeId(), password),
    }

def dump_SNSInfoExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "OpenScenarioModeId": convert_int(excel_instance.OpenScenarioModeId(), password),
        "CloseScenarioModeId": convert_int(excel_instance.CloseScenarioModeId(), password),
        "OpenTitleLocalizeKey": convert_uint(excel_instance.OpenTitleLocalizeKey(), password),
        "CloseTitleLocalizeKey": convert_uint(excel_instance.CloseTitleLocalizeKey(), password),
        "OpenDescLocalizeKey": convert_uint(excel_instance.OpenDescLocalizeKey(), password),
        "CloseDescLocalizeKey": convert_uint(excel_instance.CloseDescLocalizeKey(), password),
    }

def dump_SNSPostExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SNSInfoId": convert_int(excel_instance.SNSInfoId(), password),
        "MasterPostId": convert_int(excel_instance.MasterPostId(), password),
        "RepostSNSProfileId": convert_int(excel_instance.RepostSNSProfileId(), password),
        "SNSProfileId": convert_int(excel_instance.SNSProfileId(), password),
        "PostTextLocalizeKey": convert_uint(excel_instance.PostTextLocalizeKey(), password),
        "PostImagePath": [convert_string(excel_instance.PostImagePath(j), password) for j in range(excel_instance.PostImagePathLength())],
        "RepostMinNum": convert_int(excel_instance.RepostMinNum(), password),
        "RepostMaxNum": convert_int(excel_instance.RepostMaxNum(), password),
        "FavorMinNum": convert_int(excel_instance.FavorMinNum(), password),
        "FavorMaxNum": convert_int(excel_instance.FavorMaxNum(), password),
    }

def dump_SNSProfileExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "DevName": convert_string(excel_instance.DevName(), password),
        "ProfileImagePath": convert_string(excel_instance.ProfileImagePath(), password),
        "NameLocalizeKey": convert_uint(excel_instance.NameLocalizeKey(), password),
        "IdLocalizeKey": convert_uint(excel_instance.IdLocalizeKey(), password),
        "MarkIconVisible": bool(excel_instance.MarkIconVisible()),
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
        "AnimJson": convert_string(excel_instance.AnimJson(), password),
        "AnimJsonKr": convert_string(excel_instance.AnimJsonKr(), password),
    }

def dump_StageFileRefreshSettingExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "ForceSave": bool(excel_instance.ForceSave()),
    }

def dump_StatLevelInterpolationExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Level": convert_int(excel_instance.Level(), password),
        "StatTypeIndex": [convert_int(excel_instance.StatTypeIndex(j), password) for j in range(excel_instance.StatTypeIndexLength())],
    }

def dump_StickerGroupExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Layout": convert_string(excel_instance.Layout(), password),
        "UniqueLayoutPath": convert_string(excel_instance.UniqueLayoutPath(), password),
        "StickerGroupIconpath": convert_string(excel_instance.StickerGroupIconpath(), password),
        "PageCompleteSlot": convert_int(excel_instance.PageCompleteSlot(), password),
        "PageCompleteRewardParcelType": excel_instance.PageCompleteRewardParcelType(),
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
        "StickerGetConditionType": excel_instance.StickerGetConditionType(),
        "StickerCheckPassType": excel_instance.StickerCheckPassType(),
        "GetStickerConditionType": excel_instance.GetStickerConditionType(),
        "StickerGetConditionCount": convert_int(excel_instance.StickerGetConditionCount(), password),
        "StickerGetConditionParameter": [convert_int(excel_instance.StickerGetConditionParameter(j), password) for j in range(excel_instance.StickerGetConditionParameterLength())],
        "StickerGetConditionParameterTag": [excel_instance.StickerGetConditionParameterTag(j) for j in range(excel_instance.StickerGetConditionParameterTagLength())],
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
        "StageTopography": excel_instance.StageTopography(),
        "StrategyEnvironment": excel_instance.StrategyEnvironment(),
        "ContentType": excel_instance.ContentType(),
        "BGMId": convert_int(excel_instance.BGMId(), password),
        "FirstClearReportEventName": convert_string(excel_instance.FirstClearReportEventName(), password),
    }

def dump_StrategyObjectBuffDefineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StrategyObjectBuffID": convert_int(excel_instance.StrategyObjectBuffID(), password),
        "StrategyObjectTurn": convert_int(excel_instance.StrategyObjectTurn(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
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

def dump_TacticEntityEffectFilterExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TargetEffectName": convert_string(excel_instance.TargetEffectName(), password),
        "ShowEffectToVehicle": bool(excel_instance.ShowEffectToVehicle()),
        "ShowEffectToBoss": bool(excel_instance.ShowEffectToBoss()),
    }

def dump_TacticSkipExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LevelDiff": convert_int(excel_instance.LevelDiff(), password),
        "HPResult": convert_int(excel_instance.HPResult(), password),
    }

def dump_TerrainAdaptationFactorExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TerrainAdaptation": excel_instance.TerrainAdaptation(),
        "TerrainAdaptationStat": excel_instance.TerrainAdaptationStat(),
        "ShotFactor": convert_int(excel_instance.ShotFactor(), password),
        "BlockFactor": convert_int(excel_instance.BlockFactor(), password),
        "AccuracyFactor": convert_int(excel_instance.AccuracyFactor(), password),
        "DodgeFactor": convert_int(excel_instance.DodgeFactor(), password),
        "AttackPowerFactor": convert_int(excel_instance.AttackPowerFactor(), password),
        "TerrainFactorDescription": convert_string(excel_instance.TerrainFactorDescription(), password),
    }

def dump_TimeAttackDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TimeAttackDungeonType": excel_instance.TimeAttackDungeonType(),
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKey(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "InformationGroupID": convert_int(excel_instance.InformationGroupID(), password),
    }

def dump_TimeAttackDungeonGeasExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TimeAttackDungeonType": excel_instance.TimeAttackDungeonType(),
        "LocalizeEtcKey": convert_uint(excel_instance.LocalizeEtcKey(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "ClearDefaultPoint": convert_int(excel_instance.ClearDefaultPoint(), password),
        "ClearTimeWeightPoint": convert_int(excel_instance.ClearTimeWeightPoint(), password),
        "TimeWeightConst": convert_int(excel_instance.TimeWeightConst(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "AllyPassiveSkillId": [convert_string(excel_instance.AllyPassiveSkillId(j), password) for j in range(excel_instance.AllyPassiveSkillIdLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "EnemyPassiveSkillId": [convert_string(excel_instance.EnemyPassiveSkillId(j), password) for j in range(excel_instance.EnemyPassiveSkillIdLength())],
        "EnemyPassiveSkillLevel": [convert_int(excel_instance.EnemyPassiveSkillLevel(j), password) for j in range(excel_instance.EnemyPassiveSkillLevelLength())],
        "GeasIconPath": [convert_string(excel_instance.GeasIconPath(j), password) for j in range(excel_instance.GeasIconPathLength())],
        "GeasLocalizeEtcKey": [convert_uint(excel_instance.GeasLocalizeEtcKey(j), password) for j in range(excel_instance.GeasLocalizeEtcKeyLength())],
    }

def dump_TimeAttackDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "RewardMaxPoint": convert_int(excel_instance.RewardMaxPoint(), password),
        "RewardType": [excel_instance.RewardType(j) for j in range(excel_instance.RewardTypeLength())],
        "RewardMinPoint": [convert_int(excel_instance.RewardMinPoint(j), password) for j in range(excel_instance.RewardMinPointLength())],
        "RewardParcelType": [excel_instance.RewardParcelType(j) for j in range(excel_instance.RewardParcelTypeLength())],
        "RewardParcelId": [convert_int(excel_instance.RewardParcelId(j), password) for j in range(excel_instance.RewardParcelIdLength())],
        "RewardParcelDefaultAmount": [convert_int(excel_instance.RewardParcelDefaultAmount(j), password) for j in range(excel_instance.RewardParcelDefaultAmountLength())],
        "RewardParcelMaxAmount": [convert_int(excel_instance.RewardParcelMaxAmount(j), password) for j in range(excel_instance.RewardParcelMaxAmountLength())],
    }

def dump_TimeAttackDungeonSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndNoteLabelStartDate": convert_string(excel_instance.EndNoteLabelStartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "UISlot": convert_int(excel_instance.UISlot(), password),
        "DungeonId": convert_int(excel_instance.DungeonId(), password),
        "DifficultyGeas": [convert_int(excel_instance.DifficultyGeas(j), password) for j in range(excel_instance.DifficultyGeasLength())],
        "TimeAttackDungeonRewardId": convert_int(excel_instance.TimeAttackDungeonRewardId(), password),
        "RoomLifeTimeInSeconds": convert_int(excel_instance.RoomLifeTimeInSeconds(), password),
    }

def dump_ToastExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_uint(excel_instance.Id(), password),
        "ToastType": excel_instance.ToastType(),
        "MissionId": convert_uint(excel_instance.MissionId(), password),
        "TextId": convert_uint(excel_instance.TextId(), password),
        "LifeTime": convert_int(excel_instance.LifeTime(), password),
    }

def dump_TrophyCollectionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "FurnitureId": [convert_int(excel_instance.FurnitureId(j), password) for j in range(excel_instance.FurnitureIdLength())],
    }

def dump_TutorialCharacterDialogExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "TalkId": convert_int(excel_instance.TalkId(), password),
        "AnimationName": convert_string(excel_instance.AnimationName(), password),
        "LocalizeKR": convert_string(excel_instance.LocalizeKR(), password),
        "LocalizeJP": convert_string(excel_instance.LocalizeJP(), password),
        "LocalizeTH": convert_string(excel_instance.LocalizeTH(), password),
        "LocalizeTW": convert_string(excel_instance.LocalizeTW(), password),
        "LocalizeEN": convert_string(excel_instance.LocalizeEN(), password),
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_TutorialExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "ID": convert_int(excel_instance.ID(), password),
        "CompletionReportEventName": convert_string(excel_instance.CompletionReportEventName(), password),
        "CompulsoryTutorial": bool(excel_instance.CompulsoryTutorial()),
        "DescriptionTutorial": bool(excel_instance.DescriptionTutorial()),
        "TutorialStageId": convert_int(excel_instance.TutorialStageId(), password),
        "UIName": [convert_string(excel_instance.UIName(j), password) for j in range(excel_instance.UINameLength())],
        "TutorialParentName": [convert_string(excel_instance.TutorialParentName(j), password) for j in range(excel_instance.TutorialParentNameLength())],
    }

def dump_TutorialFailureImageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Contents": excel_instance.Contents(),
        "Type": convert_string(excel_instance.Type(), password),
        "ImagePathKr": convert_string(excel_instance.ImagePathKr(), password),
        "ImagePathJp": convert_string(excel_instance.ImagePathJp(), password),
        "ImagePathTh": convert_string(excel_instance.ImagePathTh(), password),
        "ImagePathTw": convert_string(excel_instance.ImagePathTw(), password),
        "ImagePathEn": convert_string(excel_instance.ImagePathEn(), password),
        "ReplaceLocalizeKey": convert_string(excel_instance.ReplaceLocalizeKey(), password),
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
        "Nation": [excel_instance.Nation(j) for j in range(excel_instance.NationLength())],
        "VideoPath": [convert_string(excel_instance.VideoPath(j), password) for j in range(excel_instance.VideoPathLength())],
        "VideoTeenPath": [convert_string(excel_instance.VideoTeenPath(j), password) for j in range(excel_instance.VideoTeenPathLength())],
        "SoundPath": [convert_string(excel_instance.SoundPath(j), password) for j in range(excel_instance.SoundPathLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolume(j), password) for j in range(excel_instance.SoundVolumeLength())],
    }

def dump_Video_GlobalExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VideoId": convert_int(excel_instance.VideoId(), password),
        "VideoPathKr": convert_string(excel_instance.VideoPathKr(), password),
        "VideoTeenPathKr": convert_string(excel_instance.VideoTeenPathKr(), password),
        "VideoPathTh": convert_string(excel_instance.VideoPathTh(), password),
        "VideoTeenPathTh": convert_string(excel_instance.VideoTeenPathTh(), password),
        "VideoPathTw": convert_string(excel_instance.VideoPathTw(), password),
        "VideoTeenPathTw": convert_string(excel_instance.VideoTeenPathTw(), password),
        "VideoPathEn": convert_string(excel_instance.VideoPathEn(), password),
        "VideoTeenPathEn": convert_string(excel_instance.VideoTeenPathEn(), password),
    }

def dump_VoiceCommonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "VoiceEvent": excel_instance.VoiceEvent(),
        "Rate": convert_int(excel_instance.Rate(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
    }

def dump_VoiceExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "Nation": [excel_instance.Nation(j) for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "Volume": [convert_float(excel_instance.Volume(j), password) for j in range(excel_instance.VolumeLength())],
    }

def dump_VoiceLogicEffectExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "LogicEffectNameHash": convert_uint(excel_instance.LogicEffectNameHash(), password),
        "Self": bool(excel_instance.Self()),
        "Priority": convert_int(excel_instance.Priority(), password),
        "VoiceHash": [convert_uint(excel_instance.VoiceHash(j), password) for j in range(excel_instance.VoiceHashLength())],
        "VoiceId": convert_uint(excel_instance.VoiceId(), password),
    }

def dump_VoiceRoomExceptionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "CostumeUniqueId": convert_int(excel_instance.CostumeUniqueId(), password),
        "LinkedCharacterVoicePrintType": excel_instance.LinkedCharacterVoicePrintType(),
        "LinkedCostumeUniqueId": convert_int(excel_instance.LinkedCostumeUniqueId(), password),
    }

def dump_VoiceSpineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "Nation": [excel_instance.Nation(j) for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolume(j), password) for j in range(excel_instance.SoundVolumeLength())],
    }

def dump_VoiceTimelineExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "UniqueId": convert_int(excel_instance.UniqueId(), password),
        "Id": convert_uint(excel_instance.Id(), password),
        "Nation": [excel_instance.Nation(j) for j in range(excel_instance.NationLength())],
        "Path": [convert_string(excel_instance.Path(j), password) for j in range(excel_instance.PathLength())],
        "SoundVolume": [convert_float(excel_instance.SoundVolume(j), password) for j in range(excel_instance.SoundVolumeLength())],
    }

def dump_WebEventSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "Enabled": bool(excel_instance.Enabled()),
        "IconOrder": convert_int(excel_instance.IconOrder(), password),
        "WebEventId": [convert_int(excel_instance.WebEventId(j), password) for j in range(excel_instance.WebEventIdLength())],
        "IsFull": bool(excel_instance.IsFull()),
        "UseExternalBrowser": bool(excel_instance.UseExternalBrowser()),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "LobbyBannerImage": convert_string(excel_instance.LobbyBannerImage(), password),
        "PopupTitleLocalizeKey": convert_string(excel_instance.PopupTitleLocalizeKey(), password),
        "StageEventUrl": convert_string(excel_instance.StageEventUrl(), password),
        "LiveEventUrl": convert_string(excel_instance.LiveEventUrl(), password),
    }

def dump_WeekDungeonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "StageId": convert_int(excel_instance.StageId(), password),
        "WeekDungeonType": convert_float(excel_instance.WeekDungeonType(), password),
        "Difficulty": convert_int(excel_instance.Difficulty(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "PrevStageId": convert_int(excel_instance.PrevStageId(), password),
        "StageEnterCostType": [excel_instance.StageEnterCostType(j) for j in range(excel_instance.StageEnterCostTypeLength())],
        "StageEnterCostId": [convert_int(excel_instance.StageEnterCostId(j), password) for j in range(excel_instance.StageEnterCostIdLength())],
        "StageEnterCostAmount": [convert_int(excel_instance.StageEnterCostAmount(j), password) for j in range(excel_instance.StageEnterCostAmountLength())],
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "StarGoal": [excel_instance.StarGoal(j) for j in range(excel_instance.StarGoalLength())],
        "StarGoalAmount": [convert_int(excel_instance.StarGoalAmount(j), password) for j in range(excel_instance.StarGoalAmountLength())],
        "StageTopography": excel_instance.StageTopography(),
        "RecommandLevel": convert_int(excel_instance.RecommandLevel(), password),
        "StageRewardId": convert_int(excel_instance.StageRewardId(), password),
        "PlayTimeLimitInSeconds": convert_int(excel_instance.PlayTimeLimitInSeconds(), password),
        "BattleRewardExp": convert_int(excel_instance.BattleRewardExp(), password),
        "BattleRewardPlayerExp": convert_int(excel_instance.BattleRewardPlayerExp(), password),
        "GroupBuffID": [convert_int(excel_instance.GroupBuffID(j), password) for j in range(excel_instance.GroupBuffIDLength())],
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_WeekDungeonGroupBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDungeonBuffId": convert_int(excel_instance.WeekDungeonBuffId(), password),
        "School": excel_instance.School(),
        "RecommandLocalizeEtcId": convert_uint(excel_instance.RecommandLocalizeEtcId(), password),
        "FormationLocalizeEtcId": convert_uint(excel_instance.FormationLocalizeEtcId(), password),
        "SkillGroupId": convert_string(excel_instance.SkillGroupId(), password),
    }

def dump_WeekDungeonOpenScheduleExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WeekDay": excel_instance.WeekDay(),
        "Open": [convert_float(excel_instance.Open(j), password) for j in range(excel_instance.OpenLength())],
    }

def dump_WeekDungeonRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "DungeonType": convert_float(excel_instance.DungeonType(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelId": convert_int(excel_instance.RewardParcelId(), password),
        "RewardParcelAmount": convert_int(excel_instance.RewardParcelAmount(), password),
        "RewardParcelProbability": convert_int(excel_instance.RewardParcelProbability(), password),
        "IsDisplayed": bool(excel_instance.IsDisplayed()),
        "DropItemModelPrefabPath": convert_string(excel_instance.DropItemModelPrefabPath(), password),
    }

def dump_WelcomeCampaignAttendanceRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "CountCheckType": excel_instance.CountCheckType(),
        "Day": convert_int(excel_instance.Day(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardId": convert_int(excel_instance.RewardId(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
    }

def dump_WelcomeCampaignEnterRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "RewardParcelType": excel_instance.RewardParcelType(),
        "RewardParcelUniqueID": convert_int(excel_instance.RewardParcelUniqueID(), password),
        "RewardAmount": convert_int(excel_instance.RewardAmount(), password),
    }

def dump_WelcomeCampaignMissionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "Id": convert_int(excel_instance.Id(), password),
        "Category": excel_instance.Category(),
        "IsLegacy": bool(excel_instance.IsLegacy()),
        "Day": convert_int(excel_instance.Day(), password),
        "PreMissionId": [convert_int(excel_instance.PreMissionId(j), password) for j in range(excel_instance.PreMissionIdLength())],
        "Description": convert_uint(excel_instance.Description(), password),
        "ToastDisplayType": excel_instance.ToastDisplayType(),
        "ToastImagePath": convert_string(excel_instance.ToastImagePath(), password),
        "ShortcutUI": [convert_string(excel_instance.ShortcutUI(j), password) for j in range(excel_instance.ShortcutUILength())],
        "CompleteConditionDayBlock": bool(excel_instance.CompleteConditionDayBlock()),
        "CompleteConditionType": excel_instance.CompleteConditionType(),
        "CompleteConditionCount": convert_int(excel_instance.CompleteConditionCount(), password),
        "CompleteConditionParameter": [convert_int(excel_instance.CompleteConditionParameter(j), password) for j in range(excel_instance.CompleteConditionParameterLength())],
        "CompleteConditionParameterTag": [excel_instance.CompleteConditionParameterTag(j) for j in range(excel_instance.CompleteConditionParameterTagLength())],
        "CompleteConditionParameterUIPrefabType": excel_instance.CompleteConditionParameterUIPrefabType(),
        "MissionRewardParcelType": [excel_instance.MissionRewardParcelType(j) for j in range(excel_instance.MissionRewardParcelTypeLength())],
        "MissionRewardParcelId": [convert_int(excel_instance.MissionRewardParcelId(j), password) for j in range(excel_instance.MissionRewardParcelIdLength())],
        "MissionRewardAmount": [convert_int(excel_instance.MissionRewardAmount(j), password) for j in range(excel_instance.MissionRewardAmountLength())],
    }

def dump_WelcomeCampaignRewardIncreaseExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "LocalizeCodeId": convert_uint(excel_instance.LocalizeCodeId(), password),
        "IconPath": convert_string(excel_instance.IconPath(), password),
        "EventTargetType": excel_instance.EventTargetType(),
        "IncreaseRatio": convert_int(excel_instance.IncreaseRatio(), password),
        "ShortcutEventTargetType": excel_instance.ShortcutEventTargetType(),
    }

def dump_WelcomeCampaignSeasonExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "TitleLocalizeCode": convert_uint(excel_instance.TitleLocalizeCode(), password),
        "TargetGroup": excel_instance.TargetGroup(),
        "ActiveOrder": convert_int(excel_instance.ActiveOrder(), password),
        "StartDate": convert_string(excel_instance.StartDate(), password),
        "EndDate": convert_string(excel_instance.EndDate(), password),
        "ExpiryDate": convert_int(excel_instance.ExpiryDate(), password),
        "EnterIconImage": convert_string(excel_instance.EnterIconImage(), password),
        "BackgroundImage": convert_string(excel_instance.BackgroundImage(), password),
        "TitleImage": convert_string(excel_instance.TitleImage(), password),
        "EnterRewardGroupId": convert_int(excel_instance.EnterRewardGroupId(), password),
        "RewardIncreaseId": convert_int(excel_instance.RewardIncreaseId(), password),
        "MaximumLoginCount": convert_int(excel_instance.MaximumLoginCount(), password),
        "AttendanceBookSize": convert_int(excel_instance.AttendanceBookSize(), password),
        "ContinuousAttendance": bool(excel_instance.ContinuousAttendance()),
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
        "WorldBossHPTw": convert_int(excel_instance.WorldBossHPTw(), password),
        "WorldBossHPAsia": convert_int(excel_instance.WorldBossHPAsia(), password),
        "WorldBossHPNa": convert_int(excel_instance.WorldBossHPNa(), password),
        "WorldBossHPGlobal": convert_int(excel_instance.WorldBossHPGlobal(), password),
        "UIHideBeforeSpawn": bool(excel_instance.UIHideBeforeSpawn()),
        "HideAnotherBossKilled": bool(excel_instance.HideAnotherBossKilled()),
        "WorldBossClearRewardGroupId": convert_int(excel_instance.WorldBossClearRewardGroupId(), password),
        "AnotherBossKilled": [convert_int(excel_instance.AnotherBossKilled(j), password) for j in range(excel_instance.AnotherBossKilledLength())],
        "EchelonConstraintGroupId": convert_int(excel_instance.EchelonConstraintGroupId(), password),
        "ExclusiveOperatorBossSpawn": convert_string(excel_instance.ExclusiveOperatorBossSpawn(), password),
        "ExclusiveOperatorBossKill": convert_string(excel_instance.ExclusiveOperatorBossKill(), password),
        "ExclusiveOperatorScenarioBattle": convert_string(excel_instance.ExclusiveOperatorScenarioBattle(), password),
        "ExclusiveOperatorBossDamaged": convert_string(excel_instance.ExclusiveOperatorBossDamaged(), password),
        "BossGroupOpenCondition": convert_int(excel_instance.BossGroupOpenCondition(), password),
    }

def dump_WorldRaidConditionExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "Id": convert_int(excel_instance.Id(), password),
        "LockUI": [convert_string(excel_instance.LockUI(j), password) for j in range(excel_instance.LockUILength())],
        "HideWhenLocked": bool(excel_instance.HideWhenLocked()),
        "AccountLevel": convert_int(excel_instance.AccountLevel(), password),
        "ScenarioModeId": [convert_int(excel_instance.ScenarioModeId(j), password) for j in range(excel_instance.ScenarioModeIdLength())],
        "CampaignStageID": [convert_int(excel_instance.CampaignStageID(j), password) for j in range(excel_instance.CampaignStageIDLength())],
        "MultipleConditionCheckType": excel_instance.MultipleConditionCheckType(),
        "AfterWhenDate": convert_string(excel_instance.AfterWhenDate(), password),
        "WorldRaidBossKill": [convert_int(excel_instance.WorldRaidBossKill(j), password) for j in range(excel_instance.WorldRaidBossKillLength())],
    }

def dump_WorldRaidFavorBuffExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "WorldRaidFavorRank": convert_int(excel_instance.WorldRaidFavorRank(), password),
        "WorldRaidFavorRankBonus": convert_int(excel_instance.WorldRaidFavorRankBonus(), password),
    }

def dump_WorldRaidSeasonManageExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "SeasonId": convert_int(excel_instance.SeasonId(), password),
        "PhaseId": convert_int(excel_instance.PhaseId(), password),
        "EnterTicket": excel_instance.EnterTicket(),
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
        "OpenRaidBossGroupId": [convert_int(excel_instance.OpenRaidBossGroupId(j), password) for j in range(excel_instance.OpenRaidBossGroupIdLength())],
        "BossSpawnTime": [convert_string(excel_instance.BossSpawnTime(j), password) for j in range(excel_instance.BossSpawnTimeLength())],
        "EliminateTime": [convert_string(excel_instance.EliminateTime(j), password) for j in range(excel_instance.EliminateTimeLength())],
        "ScenarioOutputConditionId": [convert_int(excel_instance.ScenarioOutputConditionId(j), password) for j in range(excel_instance.ScenarioOutputConditionIdLength())],
        "ConditionScenarioGroupid": [convert_int(excel_instance.ConditionScenarioGroupid(j), password) for j in range(excel_instance.ConditionScenarioGroupidLength())],
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
        "BossCharacterId": [convert_int(excel_instance.BossCharacterId(j), password) for j in range(excel_instance.BossCharacterIdLength())],
        "AssistCharacterLimitCount": convert_int(excel_instance.AssistCharacterLimitCount(), password),
        "WorldRaidDifficulty": excel_instance.WorldRaidDifficulty(),
        "DifficultyOpenCondition": bool(excel_instance.DifficultyOpenCondition()),
        "RaidEnterAmount": convert_int(excel_instance.RaidEnterAmount(), password),
        "ReEnterAmount": convert_int(excel_instance.ReEnterAmount(), password),
        "BattleDuration": convert_int(excel_instance.BattleDuration(), password),
        "GroundId": convert_int(excel_instance.GroundId(), password),
        "RaidBattleEndRewardGroupId": convert_int(excel_instance.RaidBattleEndRewardGroupId(), password),
        "RaidRewardGroupId": convert_int(excel_instance.RaidRewardGroupId(), password),
        "BattleReadyTimelinePath": [convert_string(excel_instance.BattleReadyTimelinePath(j), password) for j in range(excel_instance.BattleReadyTimelinePathLength())],
        "BattleReadyTimelinePhaseStart": [convert_int(excel_instance.BattleReadyTimelinePhaseStart(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseStartLength())],
        "BattleReadyTimelinePhaseEnd": [convert_int(excel_instance.BattleReadyTimelinePhaseEnd(j), password) for j in range(excel_instance.BattleReadyTimelinePhaseEndLength())],
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
        "AllyPassiveSkill": [convert_string(excel_instance.AllyPassiveSkill(j), password) for j in range(excel_instance.AllyPassiveSkillLength())],
        "AllyPassiveSkillLevel": [convert_int(excel_instance.AllyPassiveSkillLevel(j), password) for j in range(excel_instance.AllyPassiveSkillLevelLength())],
        "SaveCurrentLocalBossHP": bool(excel_instance.SaveCurrentLocalBossHP()),
        "EchelonExtensionType": excel_instance.EchelonExtensionType(),
    }

def dump_WorldRaidStageRewardExcel(excel_instance, password: bytes = b"") -> dict:
    return {
        "GroupId": convert_int(excel_instance.GroupId(), password),
        "IsClearStageRewardHideInfo": bool(excel_instance.IsClearStageRewardHideInfo()),
        "ClearStageRewardProb": convert_int(excel_instance.ClearStageRewardProb(), password),
        "ClearStageRewardParcelType": excel_instance.ClearStageRewardParcelType(),
        "ClearStageRewardParcelUniqueID": convert_int(excel_instance.ClearStageRewardParcelUniqueID(), password),
        "ClearStageRewardAmount": convert_int(excel_instance.ClearStageRewardAmount(), password),
    }

def dump_AddressableBlackListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AddressableBlackListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AddressableWhiteListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AddressableWhiteListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BossPhaseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BossPhaseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BuffParticleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BuffParticleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterDialogFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CheatCodeListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CheatCodeListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ClearDeckRuleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ClearDeckRuleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConquestStepExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConquestStepExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ConstContentsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstContentsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstEventCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstEventCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstFieldExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstFieldExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstKeyMappingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstKeyMappingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMinigameCCGExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMinigameCCGExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ConstMinigameRoadPuzzleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ConstMinigameRoadPuzzleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EmoticonSpecialExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EmoticonSpecialExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentBoxGachaElementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentBoxGachaElementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_KatakanaConvertExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KatakanaConvertExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_MinigameCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_NormalSkillTemplateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_NormalSkillTemplateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ObstacleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProtocolSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProtocolSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RecipeCraftExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RecipeCraftExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioReplayExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioReplayExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SpecialLobbyIllustExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SpecialLobbyIllustExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StringTestExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StringTestExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SystemMailExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SystemMailExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticArenaSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticArenaSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticDamageSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticDamageSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticSimulatorSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticSimulatorSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticTimeAttackSimulatorConfigExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticTimeAttackSimulatorConfigExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TagExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TagExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TranscendenceRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TranscendenceRecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_VoiceSkillUseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_VoiceSkillUseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonFindGiftRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonFindGiftRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_AccountLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AccountLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AccountLevelRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AccountLevelRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AlertPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AlertPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_AssistEchelonTypeConvertExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AssistEchelonTypeConvertExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AssistRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AssistRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_AssistSlotExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_AssistSlotExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_BattleLevelFactorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattleLevelFactorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattlePassExpLimitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattlePassExpLimitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattlePassFlavorTextExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattlePassFlavorTextExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattlePassInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattlePassInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattlePassLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattlePassLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattlePassMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattlePassMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BattlePassRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BattlePassRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_BGM_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BGM_GlobalExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_BossExternalBTExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_BossExternalBTExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_CameraExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CameraExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_CharacterDialogBattlePassExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterDialogBattlePassExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_CharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterGearExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterGearExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterGearLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterGearLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_CharacterVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CharacterVoiceSubtitleExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CharacterVoiceSubtitleExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ContentEnterCostReduceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentEnterCostReduceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ContentsFeverExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentsFeverExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ContentTargetGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ContentTargetGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CostumeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CostumeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_CurrencyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_CurrencyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EmblemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EmblemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EquipmentChangePieceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EquipmentChangePieceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EventContentCardShopModifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCardShopModifyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EventContentClueExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentClueExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentClueSearchExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentClueSearchExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentClueSearchRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentClueSearchRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentClueSearchRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentClueSearchRoundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentConcentrationCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentConcentrationCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentConcentrationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentConcentrationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentConcentrationRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentConcentrationRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentConcentrationVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentConcentrationVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EventContentNotifyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentNotifyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EventContentSpineDisplayPeriodExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpineDisplayPeriodExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_EventContentZoneExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentZoneExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_EventContentZoneVisitRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_EventContentZoneVisitRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_FieldQuestGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldQuestGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldSNSInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldSNSInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldSNSPostExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldSNSPostExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FieldWarpExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FieldWarpExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FixedEchelonSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FixedEchelonSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FixedStrategyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FixedStrategyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FloaterCommonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FloaterCommonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_FormationLocationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_FormationLocationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_GachaCombinedCostExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaCombinedCostExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_GachaSelectPickupGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GachaSelectPickupGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GoodsExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GoodsExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GooglePlayAchievementExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GooglePlayAchievementExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GroundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GroundModuleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GroundModuleRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_GrowthScoreCalculationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_GrowthScoreCalculationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_IAWorldRaidStageRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_IAWorldRaidStageRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_IdCardBackgroundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_IdCardBackgroundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InformationExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InformationExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InformationStrategyObjectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InformationStrategyObjectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidArcadeMachineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidArcadeMachineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidBossGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidBossGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidCarrierExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidCarrierExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidCarrierMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidCarrierMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidCarrierRecipeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidCarrierRecipeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidSkillDescriptionListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidSkillDescriptionListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_InteractiveWorldRaidStatusPresetExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_InteractiveWorldRaidStatusPresetExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyControllerImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyControllerImageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyMappingDisplayInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyMappingDisplayInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyMappingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyMappingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyMappingGroupInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyMappingGroupInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyMappingPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyMappingPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyMappingPopupNoneFocusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyMappingPopupNoneFocusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_KeyMappingTabExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_KeyMappingTabExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LevelExpMasterCoinExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LevelExpMasterCoinExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LoadingImageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LoadingImageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCharProfileChangeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCharProfileChangeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeCharProfileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeCharProfileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_LocalizeGachaShopExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeGachaShopExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LocalizeSkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LocalizeSkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_LogicEffectCommonVisualExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_LogicEffectCommonVisualExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MemoryLobbyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MemoryLobbyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MemoryLobby_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MemoryLobby_GlobalExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MessagePopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MessagePopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameAudioAnimatorExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameAudioAnimatorExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGCharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGEnemyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGEnemyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGEnemyGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGEnemyGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGLevelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGLevelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGLevelNodeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGLevelNodeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGLevelStageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGLevelStageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGLogicEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGLogicEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGOpenDialogExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGOpenDialogExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGPerkExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGPerkExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGRewardCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGRewardCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGRewardCardRateExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGRewardCardRateExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGRewardItemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGRewardItemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGSkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGSkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGStartDeckCardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGStartDeckCardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameCCGStartDeckCharacterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameCCGStartDeckCharacterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_MiniGameRoadPuzzleAdditionalRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleAdditionalRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleMapExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleMapExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleMapTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleMapTileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleRailSetRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleRailSetRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleRailTileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleRailTileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MinigameRoadPuzzleRoadRoundExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MinigameRoadPuzzleRoadRoundExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MiniGameRoadPuzzleVoiceExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MiniGameRoadPuzzleVoiceExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_MissionEmergencyCompleteExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MissionEmergencyCompleteExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_MomotalkScheduleSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_MomotalkScheduleSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ObstacleFireLineCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ObstacleFireLineCheckExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ParcelAutoSynthExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ParcelAutoSynthExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PermanentRaidManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PermanentRaidManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PersonalityExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PersonalityExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PickupDuplicateBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PickupDuplicateBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PickupFirstGetBonus2ExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PickupFirstGetBonus2Excel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PickupFirstGetBonusExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PickupFirstGetBonusExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_PossessionCheckExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_PossessionCheckExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ProductAutoSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductAutoSelectionGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductBattlePassExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductBattlePassExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductDailyRecordExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductDailyRecordExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductDailyRecordInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductDailyRecordInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductDailyRecordRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductDailyRecordRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductMonthlyExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductMonthlyExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductSelectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductSelectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ProductSelectionGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ProductSelectionGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidContentPlayGuideExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidContentPlayGuideExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidRankingRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidRankingRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidSeasonManageExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidSeasonManageExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_RaidSkillDescriptionListExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_RaidSkillDescriptionListExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ScenarioBGEffectExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGEffectExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioBGNameExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGNameExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioBGName_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioBGName_GlobalExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ScenarioModeSpoilerPopupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioModeSpoilerPopupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioResourceInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioResourceInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ScenarioScriptFunnelExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ScenarioScriptFunnelExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ShopRecruitDirectingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRecruitDirectingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRecruitExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRecruitExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRecruitSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRecruitSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopRefreshExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopRefreshExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShopTabGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShopTabGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_ShortcutTypeExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ShortcutTypeExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillAdditionalTooltipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillAdditionalTooltipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SkillSelectExTooltipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SkillSelectExTooltipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SNSInfoExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SNSInfoExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SNSPostExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SNSPostExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SNSProfileExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SNSProfileExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SoundUIExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SoundUIExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_SpineLipsyncExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_SpineLipsyncExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_StageFileRefreshSettingExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StageFileRefreshSettingExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_StrategyObjectBuffDefineExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_StrategyObjectBuffDefineExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticalSupportSystemExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticalSupportSystemExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticEntityEffectFilterExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticEntityEffectFilterExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TacticSkipExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TacticSkipExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_ToastExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_ToastExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_TrophyCollectionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_TrophyCollectionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_Video_GlobalExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_Video_GlobalExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_WebEventSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WebEventSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WeekDungeonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WeekDungeonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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

def dump_WelcomeCampaignAttendanceRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WelcomeCampaignAttendanceRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WelcomeCampaignEnterRewardExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WelcomeCampaignEnterRewardExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WelcomeCampaignMissionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WelcomeCampaignMissionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WelcomeCampaignRewardIncreaseExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WelcomeCampaignRewardIncreaseExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WelcomeCampaignSeasonExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WelcomeCampaignSeasonExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidBossGroupExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidBossGroupExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
    }

def dump_WorldRaidConditionExcelTable(excel_instance, password: bytes = b"") -> dict:
    return {
        "DataList": [dump_WorldRaidConditionExcel(excel_instance.DataList(j), password) for j in range(excel_instance.DataListLength())],
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
