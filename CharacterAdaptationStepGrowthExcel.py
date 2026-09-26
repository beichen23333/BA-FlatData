
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterAdaptationStepGrowthExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterAdaptationStepGrowthExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot1Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot1Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot2Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot2Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot3Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlot3Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PublicSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt32Slot(1, GroupId, 0)


    @staticmethod
    def AddMissionStep(builder, MissionStep): builder.PrependInt32Slot(2, MissionStep, 0)


    @staticmethod
    def AddCharacterLevel(builder, CharacterLevel): builder.PrependInt32Slot(3, CharacterLevel, 0)


    @staticmethod
    def AddEquipSlot1Tier(builder, EquipSlot1Tier): builder.PrependInt32Slot(4, EquipSlot1Tier, 0)


    @staticmethod
    def AddEquipSlot1Level(builder, EquipSlot1Level): builder.PrependInt32Slot(5, EquipSlot1Level, 0)


    @staticmethod
    def AddEquipSlot2Tier(builder, EquipSlot2Tier): builder.PrependInt32Slot(6, EquipSlot2Tier, 0)


    @staticmethod
    def AddEquipSlot2Level(builder, EquipSlot2Level): builder.PrependInt32Slot(7, EquipSlot2Level, 0)


    @staticmethod
    def AddEquipSlot3Tier(builder, EquipSlot3Tier): builder.PrependInt32Slot(8, EquipSlot3Tier, 0)


    @staticmethod
    def AddEquipSlot3Level(builder, EquipSlot3Level): builder.PrependInt32Slot(9, EquipSlot3Level, 0)


    @staticmethod
    def AddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(10, ExSkillLevel, 0)


    @staticmethod
    def AddPublicSkillLevel(builder, PublicSkillLevel): builder.PrependInt32Slot(11, PublicSkillLevel, 0)


    @staticmethod
    def AddPassiveSkillLevel(builder, PassiveSkillLevel): builder.PrependInt32Slot(12, PassiveSkillLevel, 0)


    @staticmethod
    def AddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel): builder.PrependInt32Slot(13, ExtraPassiveSkillLevel, 0)

