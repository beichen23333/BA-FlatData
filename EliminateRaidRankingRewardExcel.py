
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidRankingRewardExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidRankingRewardExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def RankingRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankStartTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankEndTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankStartAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankEndAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankStartNa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankEndNa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankStartGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RankEndGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PercentRankStart(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PercentRankEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        return o == 0


    def RewardParcelUniqueId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def RewardParcelUniqueIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def RewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RewardParcelUniqueIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        return o == 0


    def RewardParcelUniqueName(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def RewardParcelUniqueNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RewardParcelUniqueNameIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        return o == 0


    def RewardParcelAmount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def RewardParcelAmountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def RewardParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RewardParcelAmountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddRankingRewardGroupId(builder, RankingRewardGroupId): builder.PrependInt64Slot(0, RankingRewardGroupId, 0)


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(1, Id, 0)


    @staticmethod
    def AddRankStart(builder, RankStart): builder.PrependInt64Slot(2, RankStart, 0)


    @staticmethod
    def AddRankEnd(builder, RankEnd): builder.PrependInt64Slot(3, RankEnd, 0)


    @staticmethod
    def AddRankStartTw(builder, RankStartTw): builder.PrependInt64Slot(4, RankStartTw, 0)


    @staticmethod
    def AddRankEndTw(builder, RankEndTw): builder.PrependInt64Slot(5, RankEndTw, 0)


    @staticmethod
    def AddRankStartAsia(builder, RankStartAsia): builder.PrependInt64Slot(6, RankStartAsia, 0)


    @staticmethod
    def AddRankEndAsia(builder, RankEndAsia): builder.PrependInt64Slot(7, RankEndAsia, 0)


    @staticmethod
    def AddRankStartNa(builder, RankStartNa): builder.PrependInt64Slot(8, RankStartNa, 0)


    @staticmethod
    def AddRankEndNa(builder, RankEndNa): builder.PrependInt64Slot(9, RankEndNa, 0)


    @staticmethod
    def AddRankStartGlobal(builder, RankStartGlobal): builder.PrependInt64Slot(10, RankStartGlobal, 0)


    @staticmethod
    def AddRankEndGlobal(builder, RankEndGlobal): builder.PrependInt64Slot(11, RankEndGlobal, 0)


    @staticmethod
    def AddPercentRankStart(builder, PercentRankStart): builder.PrependInt64Slot(12, PercentRankStart, 0)


    @staticmethod
    def AddPercentRankEnd(builder, PercentRankEnd): builder.PrependInt64Slot(13, PercentRankEnd, 0)


    @staticmethod
    def AddTier(builder, Tier): builder.PrependInt32Slot(14, Tier, 0)


    @staticmethod
    def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
    @staticmethod
    def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddRewardParcelUniqueId(builder, RewardParcelUniqueId): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelUniqueId), 0)
    @staticmethod
    def StartRewardParcelUniqueIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddRewardParcelUniqueName(builder, RewardParcelUniqueName): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelUniqueName), 0)
    @staticmethod
    def StartRewardParcelUniqueNameVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelAmount), 0)
    @staticmethod
    def StartRewardParcelAmountVector(builder, numElems): return builder.StartVector(8, numElems, 8)

