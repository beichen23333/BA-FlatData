
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeGachaShopExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeGachaShopExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GachaShopId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TabNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TabNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TabNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TabNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TabNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TitleNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TitleNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TitleNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TitleNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TitleNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubTitleKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubTitleJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubTitleTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubTitleTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubTitleEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def GachaDescriptionKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def GachaDescriptionJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def GachaDescriptionTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def GachaDescriptionTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def GachaDescriptionEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(21)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGachaShopId(builder, GachaShopId): builder.PrependInt64Slot(0, GachaShopId, 0)


    @staticmethod
    def AddTabNameKr(builder, TabNameKr): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(TabNameKr), 0)

    @staticmethod
    def AddTabNameJp(builder, TabNameJp): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(TabNameJp), 0)

    @staticmethod
    def AddTabNameTh(builder, TabNameTh): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(TabNameTh), 0)

    @staticmethod
    def AddTabNameTw(builder, TabNameTw): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(TabNameTw), 0)

    @staticmethod
    def AddTabNameEn(builder, TabNameEn): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(TabNameEn), 0)

    @staticmethod
    def AddTitleNameKr(builder, TitleNameKr): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(TitleNameKr), 0)

    @staticmethod
    def AddTitleNameJp(builder, TitleNameJp): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(TitleNameJp), 0)

    @staticmethod
    def AddTitleNameTh(builder, TitleNameTh): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(TitleNameTh), 0)

    @staticmethod
    def AddTitleNameTw(builder, TitleNameTw): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(TitleNameTw), 0)

    @staticmethod
    def AddTitleNameEn(builder, TitleNameEn): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(TitleNameEn), 0)

    @staticmethod
    def AddSubTitleKr(builder, SubTitleKr): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(SubTitleKr), 0)

    @staticmethod
    def AddSubTitleJp(builder, SubTitleJp): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SubTitleJp), 0)

    @staticmethod
    def AddSubTitleTh(builder, SubTitleTh): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(SubTitleTh), 0)

    @staticmethod
    def AddSubTitleTw(builder, SubTitleTw): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(SubTitleTw), 0)

    @staticmethod
    def AddSubTitleEn(builder, SubTitleEn): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(SubTitleEn), 0)

    @staticmethod
    def AddGachaDescriptionKr(builder, GachaDescriptionKr): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(GachaDescriptionKr), 0)

    @staticmethod
    def AddGachaDescriptionJp(builder, GachaDescriptionJp): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(GachaDescriptionJp), 0)

    @staticmethod
    def AddGachaDescriptionTh(builder, GachaDescriptionTh): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(GachaDescriptionTh), 0)

    @staticmethod
    def AddGachaDescriptionTw(builder, GachaDescriptionTw): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(GachaDescriptionTw), 0)

    @staticmethod
    def AddGachaDescriptionEn(builder, GachaDescriptionEn): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(GachaDescriptionEn), 0)
