
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RaidSkillDescriptionListExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RaidSkillDescriptionListExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def BossGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PhaseNameOverrideKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillUsePhaseLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShowSkillSlotLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HighlightResourceLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddBossGroup(builder, BossGroup): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(BossGroup), 0)

    @staticmethod
    def AddDifficulty(builder, Difficulty): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Difficulty), 0)

    @staticmethod
    def AddPhaseNameOverrideKey(builder, PhaseNameOverrideKey): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseNameOverrideKey), 0)

    @staticmethod
    def AddSkillGroupIdLength(builder, SkillGroupIdLength): builder.PrependInt32Slot(3, SkillGroupIdLength, 0)


    @staticmethod
    def AddSkillUsePhaseLength(builder, SkillUsePhaseLength): builder.PrependInt32Slot(4, SkillUsePhaseLength, 0)


    @staticmethod
    def AddShowSkillSlotLength(builder, ShowSkillSlotLength): builder.PrependInt32Slot(5, ShowSkillSlotLength, 0)


    @staticmethod
    def AddHighlightResourceLength(builder, HighlightResourceLength): builder.PrependInt32Slot(6, HighlightResourceLength, 0)

