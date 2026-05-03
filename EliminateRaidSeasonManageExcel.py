
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidSeasonManageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidSeasonManageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonStartData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SeasonEndData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SettlementEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LobbyTableBGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LobbyScreenBGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenRaidBossGroup01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenRaidBossGroup02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenRaidBossGroup03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RankingRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxSeasonRewardGauage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StackedSeasonRewardGaugeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRewardIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdNormal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdHard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdVeryhard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdHardcore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdExtreme(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdInsane(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardIdTorment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(21)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt32Slot(0, SeasonId, 0)


    @staticmethod
    def AddSeasonDisplay(builder, SeasonDisplay): builder.PrependInt32Slot(1, SeasonDisplay, 0)


    @staticmethod
    def AddSeasonStartData(builder, SeasonStartData): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonStartData), 0)

    @staticmethod
    def AddSeasonEndData(builder, SeasonEndData): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonEndData), 0)

    @staticmethod
    def AddSettlementEndDate(builder, SettlementEndDate): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(SettlementEndDate), 0)

    @staticmethod
    def AddLobbyTableBGPath(builder, LobbyTableBGPath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(LobbyTableBGPath), 0)

    @staticmethod
    def AddLobbyScreenBGPath(builder, LobbyScreenBGPath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(LobbyScreenBGPath), 0)

    @staticmethod
    def AddOpenRaidBossGroup01(builder, OpenRaidBossGroup01): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(OpenRaidBossGroup01), 0)

    @staticmethod
    def AddOpenRaidBossGroup02(builder, OpenRaidBossGroup02): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(OpenRaidBossGroup02), 0)

    @staticmethod
    def AddOpenRaidBossGroup03(builder, OpenRaidBossGroup03): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(OpenRaidBossGroup03), 0)

    @staticmethod
    def AddRankingRewardGroupId(builder, RankingRewardGroupId): builder.PrependInt32Slot(10, RankingRewardGroupId, 0)


    @staticmethod
    def AddMaxSeasonRewardGauage(builder, MaxSeasonRewardGauage): builder.PrependInt32Slot(11, MaxSeasonRewardGauage, 0)


    @staticmethod
    def AddStackedSeasonRewardGaugeLength(builder, StackedSeasonRewardGaugeLength): builder.PrependInt32Slot(12, StackedSeasonRewardGaugeLength, 0)


    @staticmethod
    def AddSeasonRewardIdLength(builder, SeasonRewardIdLength): builder.PrependInt32Slot(13, SeasonRewardIdLength, 0)


    @staticmethod
    def AddLimitedRewardIdNormal(builder, LimitedRewardIdNormal): builder.PrependInt32Slot(14, LimitedRewardIdNormal, 0)


    @staticmethod
    def AddLimitedRewardIdHard(builder, LimitedRewardIdHard): builder.PrependInt32Slot(15, LimitedRewardIdHard, 0)


    @staticmethod
    def AddLimitedRewardIdVeryhard(builder, LimitedRewardIdVeryhard): builder.PrependInt32Slot(16, LimitedRewardIdVeryhard, 0)


    @staticmethod
    def AddLimitedRewardIdHardcore(builder, LimitedRewardIdHardcore): builder.PrependInt32Slot(17, LimitedRewardIdHardcore, 0)


    @staticmethod
    def AddLimitedRewardIdExtreme(builder, LimitedRewardIdExtreme): builder.PrependInt32Slot(18, LimitedRewardIdExtreme, 0)


    @staticmethod
    def AddLimitedRewardIdInsane(builder, LimitedRewardIdInsane): builder.PrependInt32Slot(19, LimitedRewardIdInsane, 0)


    @staticmethod
    def AddLimitedRewardIdTorment(builder, LimitedRewardIdTorment): builder.PrependInt32Slot(20, LimitedRewardIdTorment, 0)

