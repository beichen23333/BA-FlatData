
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterSettingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterSettingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterSettingId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PublicSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraPassiveSkillLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotTier01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotTier02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotTier03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipSlotLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterWeapon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipCharacterWeaponTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterWeaponLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterGear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EquipCharacterGearTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipCharacterGearLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialType01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialLevel01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialType02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialLevel02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialType03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PotentialLevel03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(26)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterSettingId(builder, CharacterSettingId): builder.PrependInt32Slot(0, CharacterSettingId, 0)


    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt32Slot(1, Level, 0)


    @staticmethod
    def AddFavorRank(builder, FavorRank): builder.PrependInt32Slot(2, FavorRank, 0)


    @staticmethod
    def AddStarGrade(builder, StarGrade): builder.PrependInt32Slot(3, StarGrade, 0)


    @staticmethod
    def AddExSkillLevel(builder, ExSkillLevel): builder.PrependInt32Slot(4, ExSkillLevel, 0)


    @staticmethod
    def AddPublicSkillLevel(builder, PublicSkillLevel): builder.PrependInt32Slot(5, PublicSkillLevel, 0)


    @staticmethod
    def AddPassiveSkillLevel(builder, PassiveSkillLevel): builder.PrependInt32Slot(6, PassiveSkillLevel, 0)


    @staticmethod
    def AddExtraPassiveSkillLevel(builder, ExtraPassiveSkillLevel): builder.PrependInt32Slot(7, ExtraPassiveSkillLevel, 0)


    @staticmethod
    def AddEquipSlotTier01(builder, EquipSlotTier01): builder.PrependInt32Slot(8, EquipSlotTier01, 0)


    @staticmethod
    def AddEquipSlotLevel01(builder, EquipSlotLevel01): builder.PrependInt32Slot(9, EquipSlotLevel01, 0)


    @staticmethod
    def AddEquipSlotTier02(builder, EquipSlotTier02): builder.PrependInt32Slot(10, EquipSlotTier02, 0)


    @staticmethod
    def AddEquipSlotLevel02(builder, EquipSlotLevel02): builder.PrependInt32Slot(11, EquipSlotLevel02, 0)


    @staticmethod
    def AddEquipSlotTier03(builder, EquipSlotTier03): builder.PrependInt32Slot(12, EquipSlotTier03, 0)


    @staticmethod
    def AddEquipSlotLevel03(builder, EquipSlotLevel03): builder.PrependInt32Slot(13, EquipSlotLevel03, 0)


    @staticmethod
    def AddEquipCharacterWeapon(builder, EquipCharacterWeapon): builder.PrependBoolSlot(14, EquipCharacterWeapon, 0)


    @staticmethod
    def AddEquipCharacterWeaponTier(builder, EquipCharacterWeaponTier): builder.PrependInt32Slot(15, EquipCharacterWeaponTier, 0)


    @staticmethod
    def AddEquipCharacterWeaponLevel(builder, EquipCharacterWeaponLevel): builder.PrependInt32Slot(16, EquipCharacterWeaponLevel, 0)


    @staticmethod
    def AddEquipCharacterGear(builder, EquipCharacterGear): builder.PrependBoolSlot(17, EquipCharacterGear, 0)


    @staticmethod
    def AddEquipCharacterGearTier(builder, EquipCharacterGearTier): builder.PrependInt32Slot(18, EquipCharacterGearTier, 0)


    @staticmethod
    def AddEquipCharacterGearLevel(builder, EquipCharacterGearLevel): builder.PrependInt32Slot(19, EquipCharacterGearLevel, 0)


    @staticmethod
    def AddPotentialType01(builder, PotentialType01): builder.PrependInt32Slot(20, PotentialType01, 0)


    @staticmethod
    def AddPotentialLevel01(builder, PotentialLevel01): builder.PrependInt32Slot(21, PotentialLevel01, 0)


    @staticmethod
    def AddPotentialType02(builder, PotentialType02): builder.PrependInt32Slot(22, PotentialType02, 0)


    @staticmethod
    def AddPotentialLevel02(builder, PotentialLevel02): builder.PrependInt32Slot(23, PotentialLevel02, 0)


    @staticmethod
    def AddPotentialType03(builder, PotentialType03): builder.PrependInt32Slot(24, PotentialType03, 0)


    @staticmethod
    def AddPotentialLevel03(builder, PotentialLevel03): builder.PrependInt32Slot(25, PotentialLevel03, 0)

