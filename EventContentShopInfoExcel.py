
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentShopInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentShopInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def LocalizeCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def CostParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsRefresh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsSoldOutDimmed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def AutoRefreshCoolTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RefreshAbleCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GoodsIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OpenPeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def OpenPeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShopProductUpdateDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(13)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(0, EventContentId, 0)


    @staticmethod
    def AddCategoryType(builder, CategoryType): builder.PrependFloat32Slot(1, CategoryType, 0)


    @staticmethod
    def AddLocalizeCode(builder, LocalizeCode): builder.PrependUint32Slot(2, LocalizeCode, 0)


    @staticmethod
    def AddCostParcelTypeLength(builder, CostParcelTypeLength): builder.PrependInt32Slot(3, CostParcelTypeLength, 0)


    @staticmethod
    def AddCostParcelIdLength(builder, CostParcelIdLength): builder.PrependInt32Slot(4, CostParcelIdLength, 0)


    @staticmethod
    def AddIsRefresh(builder, IsRefresh): builder.PrependBoolSlot(5, IsRefresh, 0)


    @staticmethod
    def AddIsSoldOutDimmed(builder, IsSoldOutDimmed): builder.PrependBoolSlot(6, IsSoldOutDimmed, 0)


    @staticmethod
    def AddAutoRefreshCoolTime(builder, AutoRefreshCoolTime): builder.PrependInt32Slot(7, AutoRefreshCoolTime, 0)


    @staticmethod
    def AddRefreshAbleCount(builder, RefreshAbleCount): builder.PrependInt32Slot(8, RefreshAbleCount, 0)


    @staticmethod
    def AddGoodsIdLength(builder, GoodsIdLength): builder.PrependInt32Slot(9, GoodsIdLength, 0)


    @staticmethod
    def AddOpenPeriodFrom(builder, OpenPeriodFrom): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(OpenPeriodFrom), 0)

    @staticmethod
    def AddOpenPeriodTo(builder, OpenPeriodTo): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(OpenPeriodTo), 0)

    @staticmethod
    def AddShopProductUpdateDate(builder, ShopProductUpdateDate): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(ShopProductUpdateDate), 0)
