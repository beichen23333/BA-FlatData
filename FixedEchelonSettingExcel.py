
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FixedEchelonSettingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FixedEchelonSettingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def FixedEchelonID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonSceneSkip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def MainLeaderSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainCharacterIDLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainGradeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainExSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainNoneExSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainEquipment1TierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainEquipment1LevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainEquipment2TierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainEquipment2LevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainEquipment3TierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainEquipment3LevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainCharacterWeaponGradeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainCharacterWeaponLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainCharacterGearTierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MainCharacterGearLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportCharacterIDLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportGradeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportExSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportNoneExSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportEquipment1TierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportEquipment1LevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportEquipment2TierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportEquipment2LevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportEquipment3TierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportEquipment3LevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportCharacterWeaponGradeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportCharacterWeaponLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportCharacterGearTierLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SupportCharacterGearLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def InteractionTSCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(34)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddFixedEchelonID(builder, FixedEchelonID): builder.PrependInt32Slot(0, FixedEchelonID, 0)


    @staticmethod
    def AddEchelonSceneSkip(builder, EchelonSceneSkip): builder.PrependBoolSlot(1, EchelonSceneSkip, 0)


    @staticmethod
    def AddMainLeaderSlot(builder, MainLeaderSlot): builder.PrependInt32Slot(2, MainLeaderSlot, 0)


    @staticmethod
    def AddMainCharacterIDLength(builder, MainCharacterIDLength): builder.PrependInt32Slot(3, MainCharacterIDLength, 0)


    @staticmethod
    def AddMainLevelLength(builder, MainLevelLength): builder.PrependInt32Slot(4, MainLevelLength, 0)


    @staticmethod
    def AddMainGradeLength(builder, MainGradeLength): builder.PrependInt32Slot(5, MainGradeLength, 0)


    @staticmethod
    def AddMainExSkillLevelLength(builder, MainExSkillLevelLength): builder.PrependInt32Slot(6, MainExSkillLevelLength, 0)


    @staticmethod
    def AddMainNoneExSkillLevelLength(builder, MainNoneExSkillLevelLength): builder.PrependInt32Slot(7, MainNoneExSkillLevelLength, 0)


    @staticmethod
    def AddMainEquipment1TierLength(builder, MainEquipment1TierLength): builder.PrependInt32Slot(8, MainEquipment1TierLength, 0)


    @staticmethod
    def AddMainEquipment1LevelLength(builder, MainEquipment1LevelLength): builder.PrependInt32Slot(9, MainEquipment1LevelLength, 0)


    @staticmethod
    def AddMainEquipment2TierLength(builder, MainEquipment2TierLength): builder.PrependInt32Slot(10, MainEquipment2TierLength, 0)


    @staticmethod
    def AddMainEquipment2LevelLength(builder, MainEquipment2LevelLength): builder.PrependInt32Slot(11, MainEquipment2LevelLength, 0)


    @staticmethod
    def AddMainEquipment3TierLength(builder, MainEquipment3TierLength): builder.PrependInt32Slot(12, MainEquipment3TierLength, 0)


    @staticmethod
    def AddMainEquipment3LevelLength(builder, MainEquipment3LevelLength): builder.PrependInt32Slot(13, MainEquipment3LevelLength, 0)


    @staticmethod
    def AddMainCharacterWeaponGradeLength(builder, MainCharacterWeaponGradeLength): builder.PrependInt32Slot(14, MainCharacterWeaponGradeLength, 0)


    @staticmethod
    def AddMainCharacterWeaponLevelLength(builder, MainCharacterWeaponLevelLength): builder.PrependInt32Slot(15, MainCharacterWeaponLevelLength, 0)


    @staticmethod
    def AddMainCharacterGearTierLength(builder, MainCharacterGearTierLength): builder.PrependInt32Slot(16, MainCharacterGearTierLength, 0)


    @staticmethod
    def AddMainCharacterGearLevelLength(builder, MainCharacterGearLevelLength): builder.PrependInt32Slot(17, MainCharacterGearLevelLength, 0)


    @staticmethod
    def AddSupportCharacterIDLength(builder, SupportCharacterIDLength): builder.PrependInt32Slot(18, SupportCharacterIDLength, 0)


    @staticmethod
    def AddSupportLevelLength(builder, SupportLevelLength): builder.PrependInt32Slot(19, SupportLevelLength, 0)


    @staticmethod
    def AddSupportGradeLength(builder, SupportGradeLength): builder.PrependInt32Slot(20, SupportGradeLength, 0)


    @staticmethod
    def AddSupportExSkillLevelLength(builder, SupportExSkillLevelLength): builder.PrependInt32Slot(21, SupportExSkillLevelLength, 0)


    @staticmethod
    def AddSupportNoneExSkillLevelLength(builder, SupportNoneExSkillLevelLength): builder.PrependInt32Slot(22, SupportNoneExSkillLevelLength, 0)


    @staticmethod
    def AddSupportEquipment1TierLength(builder, SupportEquipment1TierLength): builder.PrependInt32Slot(23, SupportEquipment1TierLength, 0)


    @staticmethod
    def AddSupportEquipment1LevelLength(builder, SupportEquipment1LevelLength): builder.PrependInt32Slot(24, SupportEquipment1LevelLength, 0)


    @staticmethod
    def AddSupportEquipment2TierLength(builder, SupportEquipment2TierLength): builder.PrependInt32Slot(25, SupportEquipment2TierLength, 0)


    @staticmethod
    def AddSupportEquipment2LevelLength(builder, SupportEquipment2LevelLength): builder.PrependInt32Slot(26, SupportEquipment2LevelLength, 0)


    @staticmethod
    def AddSupportEquipment3TierLength(builder, SupportEquipment3TierLength): builder.PrependInt32Slot(27, SupportEquipment3TierLength, 0)


    @staticmethod
    def AddSupportEquipment3LevelLength(builder, SupportEquipment3LevelLength): builder.PrependInt32Slot(28, SupportEquipment3LevelLength, 0)


    @staticmethod
    def AddSupportCharacterWeaponGradeLength(builder, SupportCharacterWeaponGradeLength): builder.PrependInt32Slot(29, SupportCharacterWeaponGradeLength, 0)


    @staticmethod
    def AddSupportCharacterWeaponLevelLength(builder, SupportCharacterWeaponLevelLength): builder.PrependInt32Slot(30, SupportCharacterWeaponLevelLength, 0)


    @staticmethod
    def AddSupportCharacterGearTierLength(builder, SupportCharacterGearTierLength): builder.PrependInt32Slot(31, SupportCharacterGearTierLength, 0)


    @staticmethod
    def AddSupportCharacterGearLevelLength(builder, SupportCharacterGearLevelLength): builder.PrependInt32Slot(32, SupportCharacterGearLevelLength, 0)


    @staticmethod
    def AddInteractionTSCharacterId(builder, InteractionTSCharacterId): builder.PrependInt32Slot(33, InteractionTSCharacterId, 0)

