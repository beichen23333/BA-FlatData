
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MessagePopupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MessagePopupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def StringId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def MessagePopupLayout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OrderType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Image(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TitleText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def SubTitleText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def MessageText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ConditionTextLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayXButton(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ButtonLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ButtonTextLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ButtonCommandLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ButtonParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(13)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddStringId(builder, StringId): builder.PrependUint32Slot(0, StringId, 0)


    @staticmethod
    def AddMessagePopupLayout(builder, MessagePopupLayout): builder.PrependInt32Slot(1, MessagePopupLayout, 0)


    @staticmethod
    def AddOrderType(builder, OrderType): builder.PrependInt32Slot(2, OrderType, 0)


    @staticmethod
    def AddImage(builder, Image): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Image), 0)

    @staticmethod
    def AddTitleText(builder, TitleText): builder.PrependUint32Slot(4, TitleText, 0)


    @staticmethod
    def AddSubTitleText(builder, SubTitleText): builder.PrependUint32Slot(5, SubTitleText, 0)


    @staticmethod
    def AddMessageText(builder, MessageText): builder.PrependUint32Slot(6, MessageText, 0)


    @staticmethod
    def AddConditionTextLength(builder, ConditionTextLength): builder.PrependInt32Slot(7, ConditionTextLength, 0)


    @staticmethod
    def AddDisplayXButton(builder, DisplayXButton): builder.PrependBoolSlot(8, DisplayXButton, 0)


    @staticmethod
    def AddButtonLength(builder, ButtonLength): builder.PrependInt32Slot(9, ButtonLength, 0)


    @staticmethod
    def AddButtonTextLength(builder, ButtonTextLength): builder.PrependInt32Slot(10, ButtonTextLength, 0)


    @staticmethod
    def AddButtonCommandLength(builder, ButtonCommandLength): builder.PrependInt32Slot(11, ButtonCommandLength, 0)


    @staticmethod
    def AddButtonParameterLength(builder, ButtonParameterLength): builder.PrependInt32Slot(12, ButtonParameterLength, 0)

