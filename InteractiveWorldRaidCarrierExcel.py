
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InteractiveWorldRaidCarrierExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InteractiveWorldRaidCarrierExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CarrierSkillListGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillCardTextureLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FixedExSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillCardTextureLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FixedPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillCardTextureLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FixedExtraPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HiddenPassiveSkillGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HiddenPassiveSkillCardTextureLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FixedHiddenPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(17)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCarrierSkillListGroupId(builder, CarrierSkillListGroupId): builder.PrependInt32Slot(0, CarrierSkillListGroupId, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(1, EventContentId, 0)


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt32Slot(2, CharacterId, 0)


    @staticmethod
    def AddCharacterLevel(builder, CharacterLevel): builder.PrependInt32Slot(3, CharacterLevel, 0)


    @staticmethod
    def AddCharacterGrade(builder, CharacterGrade): builder.PrependInt32Slot(4, CharacterGrade, 0)


    @staticmethod
    def AddExSkillGroupIdLength(builder, ExSkillGroupIdLength): builder.PrependInt32Slot(5, ExSkillGroupIdLength, 0)


    @staticmethod
    def AddExSkillCardTextureLength(builder, ExSkillCardTextureLength): builder.PrependInt32Slot(6, ExSkillCardTextureLength, 0)


    @staticmethod
    def AddFixedExSkillLevelLength(builder, FixedExSkillLevelLength): builder.PrependInt32Slot(7, FixedExSkillLevelLength, 0)


    @staticmethod
    def AddPassiveSkillGroupIdLength(builder, PassiveSkillGroupIdLength): builder.PrependInt32Slot(8, PassiveSkillGroupIdLength, 0)


    @staticmethod
    def AddPassiveSkillCardTextureLength(builder, PassiveSkillCardTextureLength): builder.PrependInt32Slot(9, PassiveSkillCardTextureLength, 0)


    @staticmethod
    def AddFixedPassiveSkillLevelLength(builder, FixedPassiveSkillLevelLength): builder.PrependInt32Slot(10, FixedPassiveSkillLevelLength, 0)


    @staticmethod
    def AddExtraPassiveSkillGroupIdLength(builder, ExtraPassiveSkillGroupIdLength): builder.PrependInt32Slot(11, ExtraPassiveSkillGroupIdLength, 0)


    @staticmethod
    def AddExtraPassiveSkillCardTextureLength(builder, ExtraPassiveSkillCardTextureLength): builder.PrependInt32Slot(12, ExtraPassiveSkillCardTextureLength, 0)


    @staticmethod
    def AddFixedExtraPassiveSkillLevelLength(builder, FixedExtraPassiveSkillLevelLength): builder.PrependInt32Slot(13, FixedExtraPassiveSkillLevelLength, 0)


    @staticmethod
    def AddHiddenPassiveSkillGroupIdLength(builder, HiddenPassiveSkillGroupIdLength): builder.PrependInt32Slot(14, HiddenPassiveSkillGroupIdLength, 0)


    @staticmethod
    def AddHiddenPassiveSkillCardTextureLength(builder, HiddenPassiveSkillCardTextureLength): builder.PrependInt32Slot(15, HiddenPassiveSkillCardTextureLength, 0)


    @staticmethod
    def AddFixedHiddenPassiveSkillLevelLength(builder, FixedHiddenPassiveSkillLevelLength): builder.PrependInt32Slot(16, FixedHiddenPassiveSkillLevelLength, 0)

