
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterSkillListExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterSkillListExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterSkillListGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinimumGradeCharacterWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinimumTierCharacterGear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FormIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsRootMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsMoveLeftRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseRandomExSkillTimeline(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TSAInteractionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NormalSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NormalSkillTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillCutInTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevelTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PublicSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PublicSkillTimeLineIndexLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LeaderSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HiddenPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterSkillListGroupId(builder, CharacterSkillListGroupId): builder.PrependInt32Slot(0, CharacterSkillListGroupId, 0)


    @staticmethod
    def AddMinimumGradeCharacterWeapon(builder, MinimumGradeCharacterWeapon): builder.PrependInt32Slot(1, MinimumGradeCharacterWeapon, 0)


    @staticmethod
    def AddMinimumTierCharacterGear(builder, MinimumTierCharacterGear): builder.PrependInt32Slot(2, MinimumTierCharacterGear, 0)


    @staticmethod
    def AddFormIndex(builder, FormIndex): builder.PrependInt32Slot(3, FormIndex, 0)


    @staticmethod
    def AddIsRootMotion(builder, IsRootMotion): builder.PrependBoolSlot(4, IsRootMotion, 0)


    @staticmethod
    def AddIsMoveLeftRight(builder, IsMoveLeftRight): builder.PrependBoolSlot(5, IsMoveLeftRight, 0)


    @staticmethod
    def AddUseRandomExSkillTimeline(builder, UseRandomExSkillTimeline): builder.PrependBoolSlot(6, UseRandomExSkillTimeline, 0)


    @staticmethod
    def AddTSAInteractionId(builder, TSAInteractionId): builder.PrependInt32Slot(7, TSAInteractionId, 0)


    @staticmethod
    def AddNormalSkillGroupIdLength(builder, NormalSkillGroupIdLength): builder.PrependInt32Slot(8, NormalSkillGroupIdLength, 0)


    @staticmethod
    def AddNormalSkillTimeLineIndexLength(builder, NormalSkillTimeLineIndexLength): builder.PrependInt32Slot(9, NormalSkillTimeLineIndexLength, 0)


    @staticmethod
    def AddExSkillGroupIdLength(builder, ExSkillGroupIdLength): builder.PrependInt32Slot(10, ExSkillGroupIdLength, 0)


    @staticmethod
    def AddExSkillCutInTimeLineIndexLength(builder, ExSkillCutInTimeLineIndexLength): builder.PrependInt32Slot(11, ExSkillCutInTimeLineIndexLength, 0)


    @staticmethod
    def AddExSkillLevelTimeLineIndexLength(builder, ExSkillLevelTimeLineIndexLength): builder.PrependInt32Slot(12, ExSkillLevelTimeLineIndexLength, 0)


    @staticmethod
    def AddPublicSkillGroupIdLength(builder, PublicSkillGroupIdLength): builder.PrependInt32Slot(13, PublicSkillGroupIdLength, 0)


    @staticmethod
    def AddPublicSkillTimeLineIndexLength(builder, PublicSkillTimeLineIndexLength): builder.PrependInt32Slot(14, PublicSkillTimeLineIndexLength, 0)


    @staticmethod
    def AddPassiveSkillGroupIdLength(builder, PassiveSkillGroupIdLength): builder.PrependInt32Slot(15, PassiveSkillGroupIdLength, 0)


    @staticmethod
    def AddLeaderSkillGroupIdLength(builder, LeaderSkillGroupIdLength): builder.PrependInt32Slot(16, LeaderSkillGroupIdLength, 0)


    @staticmethod
    def AddExtraPassiveSkillGroupIdLength(builder, ExtraPassiveSkillGroupIdLength): builder.PrependInt32Slot(17, ExtraPassiveSkillGroupIdLength, 0)


    @staticmethod
    def AddHiddenPassiveSkillGroupIdLength(builder, HiddenPassiveSkillGroupIdLength): builder.PrependInt32Slot(18, HiddenPassiveSkillGroupIdLength, 0)

