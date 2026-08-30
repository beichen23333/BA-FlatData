
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstArenaExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstArenaExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def AttackCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefenseCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TSSStartCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EndAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeRewardMaxAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TicketCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DailyRewardResetTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSlotHideRankLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MapSlotHideRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RelativeOpponentRankStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RelativeOpponentRankEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ModifiedStatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatMulFactorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatSumFactorLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCMainCharacterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCSupportCharacterCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCCharacterSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeSpanInDaysForBattleHistory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HiddenCharacterImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DefenseVictoryRewardMaxCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TopRankerCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AutoRefreshIntervalMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonSettingIntervalMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkipAllowedTimeMilliSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShowSeasonChangeInfoStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShowSeasonChangeInfoEndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShowSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ArenaHistoryQueryLimitDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(33)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddAttackCoolTime(builder, AttackCoolTime): builder.PrependInt32Slot(0, AttackCoolTime, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt32Slot(1, BattleDuration, 0)


    @staticmethod
    def AddDefenseCoolTime(builder, DefenseCoolTime): builder.PrependInt32Slot(2, DefenseCoolTime, 0)


    @staticmethod
    def AddTSSStartCoolTime(builder, TSSStartCoolTime): builder.PrependInt32Slot(3, TSSStartCoolTime, 0)


    @staticmethod
    def AddEndAlarm(builder, EndAlarm): builder.PrependInt32Slot(4, EndAlarm, 0)


    @staticmethod
    def AddTimeRewardMaxAmount(builder, TimeRewardMaxAmount): builder.PrependInt32Slot(5, TimeRewardMaxAmount, 0)


    @staticmethod
    def AddEnterCostType(builder, EnterCostType): builder.PrependInt32Slot(6, EnterCostType, 0)


    @staticmethod
    def AddEnterCostId(builder, EnterCostId): builder.PrependInt32Slot(7, EnterCostId, 0)


    @staticmethod
    def AddTicketCost(builder, TicketCost): builder.PrependInt32Slot(8, TicketCost, 0)


    @staticmethod
    def AddDailyRewardResetTime(builder, DailyRewardResetTime): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(DailyRewardResetTime), 0)

    @staticmethod
    def AddOpenScenarioId(builder, OpenScenarioId): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(OpenScenarioId), 0)

    @staticmethod
    def AddCharacterSlotHideRankLength(builder, CharacterSlotHideRankLength): builder.PrependInt32Slot(11, CharacterSlotHideRankLength, 0)


    @staticmethod
    def AddMapSlotHideRank(builder, MapSlotHideRank): builder.PrependInt32Slot(12, MapSlotHideRank, 0)


    @staticmethod
    def AddRelativeOpponentRankStartLength(builder, RelativeOpponentRankStartLength): builder.PrependInt32Slot(13, RelativeOpponentRankStartLength, 0)


    @staticmethod
    def AddRelativeOpponentRankEndLength(builder, RelativeOpponentRankEndLength): builder.PrependInt32Slot(14, RelativeOpponentRankEndLength, 0)


    @staticmethod
    def AddModifiedStatTypeLength(builder, ModifiedStatTypeLength): builder.PrependInt32Slot(15, ModifiedStatTypeLength, 0)


    @staticmethod
    def AddStatMulFactorLength(builder, StatMulFactorLength): builder.PrependInt32Slot(16, StatMulFactorLength, 0)


    @staticmethod
    def AddStatSumFactorLength(builder, StatSumFactorLength): builder.PrependInt32Slot(17, StatSumFactorLength, 0)


    @staticmethod
    def AddNPCNameLength(builder, NPCNameLength): builder.PrependInt32Slot(18, NPCNameLength, 0)


    @staticmethod
    def AddNPCMainCharacterCount(builder, NPCMainCharacterCount): builder.PrependInt32Slot(19, NPCMainCharacterCount, 0)


    @staticmethod
    def AddNPCSupportCharacterCount(builder, NPCSupportCharacterCount): builder.PrependInt32Slot(20, NPCSupportCharacterCount, 0)


    @staticmethod
    def AddNPCCharacterSkillLevel(builder, NPCCharacterSkillLevel): builder.PrependInt32Slot(21, NPCCharacterSkillLevel, 0)


    @staticmethod
    def AddTimeSpanInDaysForBattleHistory(builder, TimeSpanInDaysForBattleHistory): builder.PrependInt32Slot(22, TimeSpanInDaysForBattleHistory, 0)


    @staticmethod
    def AddHiddenCharacterImagePath(builder, HiddenCharacterImagePath): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(HiddenCharacterImagePath), 0)

    @staticmethod
    def AddDefenseVictoryRewardMaxCount(builder, DefenseVictoryRewardMaxCount): builder.PrependInt32Slot(24, DefenseVictoryRewardMaxCount, 0)


    @staticmethod
    def AddTopRankerCountLimit(builder, TopRankerCountLimit): builder.PrependInt32Slot(25, TopRankerCountLimit, 0)


    @staticmethod
    def AddAutoRefreshIntervalMilliSeconds(builder, AutoRefreshIntervalMilliSeconds): builder.PrependInt32Slot(26, AutoRefreshIntervalMilliSeconds, 0)


    @staticmethod
    def AddEchelonSettingIntervalMilliSeconds(builder, EchelonSettingIntervalMilliSeconds): builder.PrependInt32Slot(27, EchelonSettingIntervalMilliSeconds, 0)


    @staticmethod
    def AddSkipAllowedTimeMilliSeconds(builder, SkipAllowedTimeMilliSeconds): builder.PrependInt32Slot(28, SkipAllowedTimeMilliSeconds, 0)


    @staticmethod
    def AddShowSeasonChangeInfoStartTime(builder, ShowSeasonChangeInfoStartTime): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(ShowSeasonChangeInfoStartTime), 0)

    @staticmethod
    def AddShowSeasonChangeInfoEndTime(builder, ShowSeasonChangeInfoEndTime): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(ShowSeasonChangeInfoEndTime), 0)

    @staticmethod
    def AddShowSeasonId(builder, ShowSeasonId): builder.PrependInt32Slot(31, ShowSeasonId, 0)


    @staticmethod
    def AddArenaHistoryQueryLimitDays(builder, ArenaHistoryQueryLimitDays): builder.PrependInt32Slot(32, ArenaHistoryQueryLimitDays, 0)

