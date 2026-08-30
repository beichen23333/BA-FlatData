
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterLeveladjustmentExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterLeveladjustmentExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PublicSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotTier01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotTier02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotTier03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(13)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddContentType(builder, ContentType): builder.PrependInt32Slot(0, ContentType, 0)


    @staticmethod
    def AddDifficulty(builder, Difficulty): builder.PrependInt32Slot(1, Difficulty, 0)


    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt32Slot(2, Level, 0)


    @staticmethod
    def AddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(3, ExSkillLevel, 0)


    @staticmethod
    def AddPublicSkillLevel(builder, PublicSkillLevel): builder.PrependInt32Slot(4, PublicSkillLevel, 0)


    @staticmethod
    def AddPassiveSkillLevel(builder, PassiveSkillLevel): builder.PrependInt32Slot(5, PassiveSkillLevel, 0)


    @staticmethod
    def AddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel): builder.PrependInt32Slot(6, ExtraPassiveSkillLevel, 0)


    @staticmethod
    def AddEquipSlotTier01(builder, EquipSlotTier01): builder.PrependInt32Slot(7, EquipSlotTier01, 0)


    @staticmethod
    def AddEquipSlotLevel01(builder, EquipSlotLevel01): builder.PrependInt32Slot(8, EquipSlotLevel01, 0)


    @staticmethod
    def AddEquipSlotTier02(builder, EquipSlotTier02): builder.PrependInt32Slot(9, EquipSlotTier02, 0)


    @staticmethod
    def AddEquipSlotLevel02(builder, EquipSlotLevel02): builder.PrependInt32Slot(10, EquipSlotLevel02, 0)


    @staticmethod
    def AddEquipSlotTier03(builder, EquipSlotTier03): builder.PrependInt32Slot(11, EquipSlotTier03, 0)


    @staticmethod
    def AddEquipSlotLevel03(builder, EquipSlotLevel03): builder.PrependInt32Slot(12, EquipSlotLevel03, 0)

