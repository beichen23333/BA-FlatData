
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidStageLimitedRewardExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidStageLimitedRewardExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def LimitedRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LimitedRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddLimitedRewardId(builder, LimitedRewardId): builder.PrependInt32Slot(0, LimitedRewardId, 0)


    @staticmethod
    def AddLimitedRewardParcelTypeLength(builder, LimitedRewardParcelTypeLength): builder.PrependInt32Slot(1, LimitedRewardParcelTypeLength, 0)


    @staticmethod
    def AddLimitedRewardParcelUniqueIdLength(builder, LimitedRewardParcelUniqueIdLength): builder.PrependInt32Slot(2, LimitedRewardParcelUniqueIdLength, 0)


    @staticmethod
    def AddLimitedRewardAmountLength(builder, LimitedRewardAmountLength): builder.PrependInt32Slot(3, LimitedRewardAmountLength, 0)

