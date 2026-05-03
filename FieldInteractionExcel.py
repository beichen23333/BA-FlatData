
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldInteractionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldInteractionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def FieldSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FieldDateId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ShowEmoji(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def KeywordLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def InteractionTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def InteractionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionClass(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionClassParametersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OnceOnly(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ConditionIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NegateConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddFieldSeasonId(builder, FieldSeasonId): builder.PrependInt64Slot(0, FieldSeasonId, 0)


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(1, UniqueId, 0)


    @staticmethod
    def AddFieldDateId(builder, FieldDateId): builder.PrependInt64Slot(2, FieldDateId, 0)


    @staticmethod
    def AddShowEmoji(builder, ShowEmoji): builder.PrependBoolSlot(3, ShowEmoji, 0)


    @staticmethod
    def AddKeywordLocalize(builder, KeywordLocalize): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(KeywordLocalize), 0)

    @staticmethod
    def AddInteractionTypeLength(builder, InteractionTypeLength): builder.PrependInt32Slot(5, InteractionTypeLength, 0)


    @staticmethod
    def AddInteractionIdLength(builder, InteractionIdLength): builder.PrependInt32Slot(6, InteractionIdLength, 0)


    @staticmethod
    def AddConditionClass(builder, ConditionClass): builder.PrependInt32Slot(7, ConditionClass, 0)


    @staticmethod
    def AddConditionClassParametersLength(builder, ConditionClassParametersLength): builder.PrependInt32Slot(8, ConditionClassParametersLength, 0)


    @staticmethod
    def AddOnceOnly(builder, OnceOnly): builder.PrependBoolSlot(9, OnceOnly, 0)


    @staticmethod
    def AddConditionIndexLength(builder, ConditionIndexLength): builder.PrependInt32Slot(10, ConditionIndexLength, 0)


    @staticmethod
    def AddConditionTypeLength(builder, ConditionTypeLength): builder.PrependInt32Slot(11, ConditionTypeLength, 0)


    @staticmethod
    def AddConditionIdLength(builder, ConditionIdLength): builder.PrependInt32Slot(12, ConditionIdLength, 0)


    @staticmethod
    def AddNegateConditionLength(builder, NegateConditionLength): builder.PrependInt32Slot(13, NegateConditionLength, 0)

