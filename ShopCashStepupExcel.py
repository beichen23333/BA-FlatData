
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopCashStepupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopCashStepupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Step(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsFreeProduct(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShopCashIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TargetGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TitlePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ColorsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def BottomBoxPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StepupDisplayTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductSaleType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SalePeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SalePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProductSaleDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PeriodTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(16)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddStep(builder, Step): builder.PrependInt32Slot(1, Step, 0)


    @staticmethod
    def AddIsFreeProduct(builder, IsFreeProduct): builder.PrependBoolSlot(2, IsFreeProduct, 0)


    @staticmethod
    def AddShopCashIdsLength(builder, ShopCashIdsLength): builder.PrependInt32Slot(3, ShopCashIdsLength, 0)


    @staticmethod
    def AddTargetGroup(builder, TargetGroup): builder.PrependInt32Slot(4, TargetGroup, 0)


    @staticmethod
    def AddTitlePath(builder, TitlePath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(TitlePath), 0)

    @staticmethod
    def AddColorsLength(builder, ColorsLength): builder.PrependInt32Slot(6, ColorsLength, 0)


    @staticmethod
    def AddLocalizeCodeId(builder, LocalizeCodeId): builder.PrependUint32Slot(7, LocalizeCodeId, 0)


    @staticmethod
    def AddBottomBoxPrefabName(builder, BottomBoxPrefabName): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BottomBoxPrefabName), 0)

    @staticmethod
    def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(9, CategoryType, 0)


    @staticmethod
    def AddStepupDisplayTag(builder, StepupDisplayTag): builder.PrependInt32Slot(10, StepupDisplayTag, 0)


    @staticmethod
    def AddProductSaleType(builder, ProductSaleType): builder.PrependInt32Slot(11, ProductSaleType, 0)


    @staticmethod
    def AddSalePeriodFrom(builder, SalePeriodFrom): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodFrom), 0)

    @staticmethod
    def AddSalePeriodTo(builder, SalePeriodTo): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodTo), 0)

    @staticmethod
    def AddProductSaleDay(builder, ProductSaleDay): builder.PrependInt32Slot(14, ProductSaleDay, 0)


    @staticmethod
    def AddPeriodTag(builder, PeriodTag): builder.PrependBoolSlot(15, PeriodTag, 0)

