
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StreakRecordInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StreakRecordInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DaySize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FreeRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PurchaseRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TitleImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DecorationImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RestoreCostParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RestoreCostParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RestoreCostParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostIncreaseDayMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddDaySize(builder, DaySize): builder.PrependInt32Slot(1, DaySize, 0)


    @staticmethod
    def AddStartDate(builder, StartDate): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StartDate), 0)

    @staticmethod
    def AddEndDate(builder, EndDate): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(EndDate), 0)

    @staticmethod
    def AddFreeRewardGroupId(builder, FreeRewardGroupId): builder.PrependInt32Slot(4, FreeRewardGroupId, 0)


    @staticmethod
    def AddPurchaseRewardGroupId(builder, PurchaseRewardGroupId): builder.PrependInt32Slot(5, PurchaseRewardGroupId, 0)


    @staticmethod
    def AddTitleImagePath(builder, TitleImagePath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(TitleImagePath), 0)

    @staticmethod
    def AddDecorationImagePath(builder, DecorationImagePath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(DecorationImagePath), 0)

    @staticmethod
    def AddRestoreCostParcelType(builder, RestoreCostParcelType): builder.PrependInt32Slot(8, RestoreCostParcelType, 0)


    @staticmethod
    def AddRestoreCostParcelId(builder, RestoreCostParcelId): builder.PrependInt32Slot(9, RestoreCostParcelId, 0)


    @staticmethod
    def AddRestoreCostParcelAmount(builder, RestoreCostParcelAmount): builder.PrependInt32Slot(10, RestoreCostParcelAmount, 0)


    @staticmethod
    def AddCostIncreaseDayMax(builder, CostIncreaseDayMax): builder.PrependInt32Slot(11, CostIncreaseDayMax, 0)

