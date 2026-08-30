
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InteractiveWorldRaidSkillDescriptionListExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InteractiveWorldRaidSkillDescriptionListExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillParcelEchelonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GlobalSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GlobalSkillRemoveConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GlobalSkillShowSkillSlotLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GlobalSkillHighlightResourceLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShowSkillSlotLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HighlightResourceLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddSkillParcelEchelonType(builder, SkillParcelEchelonType): builder.PrependInt32Slot(1, SkillParcelEchelonType, 0)


    @staticmethod
    def AddGlobalSkillGroupIdLength(builder, GlobalSkillGroupIdLength): builder.PrependInt32Slot(2, GlobalSkillGroupIdLength, 0)


    @staticmethod
    def AddGlobalSkillRemoveConditionLength(builder, GlobalSkillRemoveConditionLength): builder.PrependInt32Slot(3, GlobalSkillRemoveConditionLength, 0)


    @staticmethod
    def AddGlobalSkillShowSkillSlotLength(builder, GlobalSkillShowSkillSlotLength): builder.PrependInt32Slot(4, GlobalSkillShowSkillSlotLength, 0)


    @staticmethod
    def AddGlobalSkillHighlightResourceLength(builder, GlobalSkillHighlightResourceLength): builder.PrependInt32Slot(5, GlobalSkillHighlightResourceLength, 0)


    @staticmethod
    def AddSkillGroupIdLength(builder, SkillGroupIdLength): builder.PrependInt32Slot(6, SkillGroupIdLength, 0)


    @staticmethod
    def AddShowSkillSlotLength(builder, ShowSkillSlotLength): builder.PrependInt32Slot(7, ShowSkillSlotLength, 0)


    @staticmethod
    def AddHighlightResourceLength(builder, HighlightResourceLength): builder.PrependInt32Slot(8, HighlightResourceLength, 0)

