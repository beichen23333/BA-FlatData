
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SeasonRecordInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SeasonRecordInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TargetGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccountLevelLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Title(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BasicRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccumulatedRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupplementCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TitleImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddTargetGroup(builder, TargetGroup): builder.PrependInt32Slot(1, TargetGroup, 0)


    @staticmethod
    def AddAccountLevelLimit(builder, AccountLevelLimit): builder.PrependInt32Slot(2, AccountLevelLimit, 0)


    @staticmethod
    def AddTitle(builder, Title): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Title), 0)

    @staticmethod
    def AddStartDate(builder, StartDate): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(StartDate), 0)

    @staticmethod
    def AddEndDate(builder, EndDate): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(EndDate), 0)

    @staticmethod
    def AddBasicRewardId(builder, BasicRewardId): builder.PrependInt32Slot(6, BasicRewardId, 0)


    @staticmethod
    def AddAccumulatedRewardId(builder, AccumulatedRewardId): builder.PrependInt32Slot(7, AccumulatedRewardId, 0)


    @staticmethod
    def AddSupplementCost(builder, SupplementCost): builder.PrependInt32Slot(8, SupplementCost, 0)


    @staticmethod
    def AddTitleImagePath(builder, TitleImagePath): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(TitleImagePath), 0)
