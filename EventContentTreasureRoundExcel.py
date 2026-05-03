
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentTreasureRoundExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentTreasureRoundExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TreasureRound(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TreasureRoundSizeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CellVisualSortUnstructed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CellCheckGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CellRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardIDLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TreasureCellImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(0, EventContentId, 0)


    @staticmethod
    def AddTreasureRound(builder, TreasureRound): builder.PrependInt32Slot(1, TreasureRound, 0)


    @staticmethod
    def AddTreasureRoundSizeLength(builder, TreasureRoundSizeLength): builder.PrependInt32Slot(2, TreasureRoundSizeLength, 0)


    @staticmethod
    def AddCellVisualSortUnstructed(builder, CellVisualSortUnstructed): builder.PrependBoolSlot(3, CellVisualSortUnstructed, 0)


    @staticmethod
    def AddCellCheckGoodsId(builder, CellCheckGoodsId): builder.PrependInt32Slot(4, CellCheckGoodsId, 0)


    @staticmethod
    def AddCellRewardId(builder, CellRewardId): builder.PrependInt32Slot(5, CellRewardId, 0)


    @staticmethod
    def AddRewardIDLength(builder, RewardIDLength): builder.PrependInt32Slot(6, RewardIDLength, 0)


    @staticmethod
    def AddRewardAmountLength(builder, RewardAmountLength): builder.PrependInt32Slot(7, RewardAmountLength, 0)


    @staticmethod
    def AddTreasureCellImagePath(builder, TreasureCellImagePath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(TreasureCellImagePath), 0)
