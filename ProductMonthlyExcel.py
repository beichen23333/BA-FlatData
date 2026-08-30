
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ProductMonthlyExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ProductMonthlyExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StoreType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Price(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PriceReference(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProductTagType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MonthlyDays(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseMonthlyProductCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def PurchaseCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterCostReduceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DailyParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DailyParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DailyParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(16)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddProductId(builder, ProductId): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(ProductId), 0)

    @staticmethod
    def AddStoreType(builder, StoreType): builder.PrependInt32Slot(2, StoreType, 0)


    @staticmethod
    def AddPrice(builder, Price): builder.PrependInt32Slot(3, Price, 0)


    @staticmethod
    def AddPriceReference(builder, PriceReference): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PriceReference), 0)

    @staticmethod
    def AddProductTagType(builder, ProductTagType): builder.PrependInt32Slot(5, ProductTagType, 0)


    @staticmethod
    def AddMonthlyDays(builder, MonthlyDays): builder.PrependInt32Slot(6, MonthlyDays, 0)


    @staticmethod
    def AddUseMonthlyProductCheck(builder, UseMonthlyProductCheck): builder.PrependBoolSlot(7, UseMonthlyProductCheck, 0)


    @staticmethod
    def AddPurchaseCountLimit(builder, PurchaseCountLimit): builder.PrependInt32Slot(8, PurchaseCountLimit, 0)


    @staticmethod
    def AddParcelTypeLength(builder, ParcelTypeLength): builder.PrependInt32Slot(9, ParcelTypeLength, 0)


    @staticmethod
    def AddParcelIdLength(builder, ParcelIdLength): builder.PrependInt32Slot(10, ParcelIdLength, 0)


    @staticmethod
    def AddParcelAmountLength(builder, ParcelAmountLength): builder.PrependInt32Slot(11, ParcelAmountLength, 0)


    @staticmethod
    def AddEnterCostReduceGroupId(builder, EnterCostReduceGroupId): builder.PrependInt32Slot(12, EnterCostReduceGroupId, 0)


    @staticmethod
    def AddDailyParcelTypeLength(builder, DailyParcelTypeLength): builder.PrependInt32Slot(13, DailyParcelTypeLength, 0)


    @staticmethod
    def AddDailyParcelIdLength(builder, DailyParcelIdLength): builder.PrependInt32Slot(14, DailyParcelIdLength, 0)


    @staticmethod
    def AddDailyParcelAmountLength(builder, DailyParcelAmountLength): builder.PrependInt32Slot(15, DailyParcelAmountLength, 0)

