
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopRefreshExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopRefreshExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def GoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsBundle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShopPurchasePopupType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VisibleAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PurchaseCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RefreshGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Prob(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BuyReportEventName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProductUpdateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(15)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(1, LocalizeEtcId, 0)


    @staticmethod
    def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(2, IsLegacy, 0)


    @staticmethod
    def AddGoodsId(builder, GoodsId): builder.PrependInt64Slot(3, GoodsId, 0)


    @staticmethod
    def AddIsBundle(builder, IsBundle): builder.PrependBoolSlot(4, IsBundle, 0)


    @staticmethod
    def AddShopPurchasePopupType(builder, ShopPurchasePopupType): builder.PrependInt32Slot(5, ShopPurchasePopupType, 0)


    @staticmethod
    def AddVisibleAmount(builder, VisibleAmount): builder.PrependInt64Slot(6, VisibleAmount, 0)


    @staticmethod
    def AddPurchaseCountLimit(builder, PurchaseCountLimit): builder.PrependInt64Slot(7, PurchaseCountLimit, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(8, DisplayOrder, 0)


    @staticmethod
    def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(9, CategoryType, 0)


    @staticmethod
    def AddRefreshGroup(builder, RefreshGroup): builder.PrependInt32Slot(10, RefreshGroup, 0)


    @staticmethod
    def AddProb(builder, Prob): builder.PrependInt32Slot(11, Prob, 0)


    @staticmethod
    def AddBuyReportEventName(builder, BuyReportEventName): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(BuyReportEventName), 0)

    @staticmethod
    def AddProductUpdateTime(builder, ProductUpdateTime): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(ProductUpdateTime), 0)

    @staticmethod
    def AddDisplayTag(builder, DisplayTag): builder.PrependInt32Slot(14, DisplayTag, 0)

