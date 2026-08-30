
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StudentFrameExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StudentFrameExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FrameImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BigFrameImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EmblemEffectPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DislpayLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CheckPassType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FrameParameter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CheckPassCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(15)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddCategory(builder, Category): builder.PrependInt32Slot(1, Category, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(2, DisplayOrder, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(3, LocalizeEtcId, 0)


    @staticmethod
    def AddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)

    @staticmethod
    def AddFrameImagePath(builder, FrameImagePath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(FrameImagePath), 0)

    @staticmethod
    def AddBigFrameImagePath(builder, BigFrameImagePath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BigFrameImagePath), 0)

    @staticmethod
    def AddEmblemEffectPath(builder, EmblemEffectPath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(EmblemEffectPath), 0)

    @staticmethod
    def AddDisplayType(builder, DisplayType): builder.PrependInt32Slot(8, DisplayType, 0)


    @staticmethod
    def AddDisplayStartDate(builder, DisplayStartDate): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(DisplayStartDate), 0)

    @staticmethod
    def AddDisplayEndDate(builder, DisplayEndDate): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(DisplayEndDate), 0)

    @staticmethod
    def AddDislpayLevel(builder, DislpayLevel): builder.PrependInt32Slot(11, DislpayLevel, 0)


    @staticmethod
    def AddCheckPassType(builder, CheckPassType): builder.PrependInt32Slot(12, CheckPassType, 0)


    @staticmethod
    def AddFrameParameter(builder, FrameParameter): builder.PrependInt32Slot(13, FrameParameter, 0)


    @staticmethod
    def AddCheckPassCount(builder, CheckPassCount): builder.PrependInt32Slot(14, CheckPassCount, 0)

