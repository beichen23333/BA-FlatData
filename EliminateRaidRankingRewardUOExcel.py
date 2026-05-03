
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidRankingRewardUOExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidRankingRewardUOExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def RankingRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RankStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RankEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PercentRankStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PercentRankEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelUniqueNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddRankingRewardGroupId(builder, RankingRewardGroupId): builder.PrependInt32Slot(0, RankingRewardGroupId, 0)


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(1, Id, 0)


    @staticmethod
    def AddRankStart(builder, RankStart): builder.PrependInt32Slot(2, RankStart, 0)


    @staticmethod
    def AddRankEnd(builder, RankEnd): builder.PrependInt32Slot(3, RankEnd, 0)


    @staticmethod
    def AddPercentRankStart(builder, PercentRankStart): builder.PrependInt32Slot(4, PercentRankStart, 0)


    @staticmethod
    def AddPercentRankEnd(builder, PercentRankEnd): builder.PrependInt32Slot(5, PercentRankEnd, 0)


    @staticmethod
    def AddTier(builder, Tier): builder.PrependInt32Slot(6, Tier, 0)


    @staticmethod
    def AddRewardParcelTypeLength(builder, RewardParcelTypeLength): builder.PrependInt32Slot(7, RewardParcelTypeLength, 0)


    @staticmethod
    def AddRewardParcelUniqueIdLength(builder, RewardParcelUniqueIdLength): builder.PrependInt32Slot(8, RewardParcelUniqueIdLength, 0)


    @staticmethod
    def AddRewardParcelUniqueNameLength(builder, RewardParcelUniqueNameLength): builder.PrependInt32Slot(9, RewardParcelUniqueNameLength, 0)


    @staticmethod
    def AddRewardParcelAmountLength(builder, RewardParcelAmountLength): builder.PrependInt32Slot(10, RewardParcelAmountLength, 0)

