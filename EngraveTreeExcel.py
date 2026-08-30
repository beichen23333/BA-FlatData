
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EngraveTreeExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EngraveTreeExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NodeIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsUnlock(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def PreNodeIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GradeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Recipe(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LearnSkillSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddNodeIndex(builder, NodeIndex): builder.PrependInt32Slot(1, NodeIndex, 0)


    @staticmethod
    def AddIsUnlock(builder, IsUnlock): builder.PrependBoolSlot(2, IsUnlock, 0)


    @staticmethod
    def AddPreNodeIndexLength(builder, PreNodeIndexLength): builder.PrependInt32Slot(3, PreNodeIndexLength, 0)


    @staticmethod
    def AddGradeType(builder, GradeType): builder.PrependInt32Slot(4, GradeType, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeEtcId), 0)

    @staticmethod
    def AddRecipe(builder, Recipe): builder.PrependInt32Slot(6, Recipe, 0)


    @staticmethod
    def AddMaxLevel(builder, MaxLevel): builder.PrependInt32Slot(7, MaxLevel, 0)


    @staticmethod
    def AddLearnSkillSlot(builder, LearnSkillSlot): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(LearnSkillSlot), 0)

    @staticmethod
    def AddStatTypeLength(builder, StatTypeLength): builder.PrependInt32Slot(9, StatTypeLength, 0)


    @staticmethod
    def AddStatValueLength(builder, StatValueLength): builder.PrependInt32Slot(10, StatValueLength, 0)

