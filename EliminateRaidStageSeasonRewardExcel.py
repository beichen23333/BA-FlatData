
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EliminateRaidStageSeasonRewardExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EliminateRaidStageSeasonRewardExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRewardParcelUniqueIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRewardParcelUniqueNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonRewardId(builder, SeasonRewardId): builder.PrependInt32Slot(0, SeasonRewardId, 0)


    @staticmethod
    def AddSeasonRewardParcelTypeLength(builder, SeasonRewardParcelTypeLength): builder.PrependInt32Slot(1, SeasonRewardParcelTypeLength, 0)


    @staticmethod
    def AddSeasonRewardParcelUniqueIdLength(builder, SeasonRewardParcelUniqueIdLength): builder.PrependInt32Slot(2, SeasonRewardParcelUniqueIdLength, 0)


    @staticmethod
    def AddSeasonRewardParcelUniqueNameLength(builder, SeasonRewardParcelUniqueNameLength): builder.PrependInt32Slot(3, SeasonRewardParcelUniqueNameLength, 0)


    @staticmethod
    def AddSeasonRewardAmountLength(builder, SeasonRewardAmountLength): builder.PrependInt32Slot(4, SeasonRewardAmountLength, 0)

