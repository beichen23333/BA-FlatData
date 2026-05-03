
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RaidSeasonManageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RaidSeasonManageExcel()
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


    def OpenRaidBossGroupLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RankingRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxSeasonRewardGauage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StackedSeasonRewardGaugeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRewardIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
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
    def AddOpenRaidBossGroupLength(builder, OpenRaidBossGroupLength): builder.PrependInt32Slot(5, OpenRaidBossGroupLength, 0)


    @staticmethod
    def AddRankingRewardGroupId(builder, RankingRewardGroupId): builder.PrependInt32Slot(6, RankingRewardGroupId, 0)


    @staticmethod
    def AddMaxSeasonRewardGauage(builder, MaxSeasonRewardGauage): builder.PrependInt32Slot(7, MaxSeasonRewardGauage, 0)


    @staticmethod
    def AddStackedSeasonRewardGaugeLength(builder, StackedSeasonRewardGaugeLength): builder.PrependInt32Slot(8, StackedSeasonRewardGaugeLength, 0)


    @staticmethod
    def AddSeasonRewardIdLength(builder, SeasonRewardIdLength): builder.PrependInt32Slot(9, SeasonRewardIdLength, 0)

