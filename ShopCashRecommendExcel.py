
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopCashRecommendExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopCashRecommendExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommendPageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopCashId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VisiblePeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VisiblePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def InfoLocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddRecommendPageType(builder, RecommendPageType): builder.PrependInt32Slot(1, RecommendPageType, 0)


    @staticmethod
    def AddShopCashId(builder, ShopCashId): builder.PrependInt32Slot(2, ShopCashId, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(3, DisplayOrder, 0)


    @staticmethod
    def AddVisiblePeriodFrom(builder, VisiblePeriodFrom): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(VisiblePeriodFrom), 0)

    @staticmethod
    def AddVisiblePeriodTo(builder, VisiblePeriodTo): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(VisiblePeriodTo), 0)

    @staticmethod
    def AddVideoIdLength(builder, VideoIdLength): builder.PrependInt32Slot(6, VideoIdLength, 0)


    @staticmethod
    def AddImagePath(builder, ImagePath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(ImagePath), 0)

    @staticmethod
    def AddInfoLocalizeCodeId(builder, InfoLocalizeCodeId): builder.PrependUint32Slot(8, InfoLocalizeCodeId, 0)

