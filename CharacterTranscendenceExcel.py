
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterTranscendenceExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterTranscendenceExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxFavorLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatBonusRateAttackLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatBonusRateHPLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatBonusRateHealLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecipeIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillSlotALength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillSlotBLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillSlotCLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxlevelStarLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt32Slot(0, CharacterId, 0)


    @staticmethod
    def AddMaxFavorLevelLength(builder, MaxFavorLevelLength): builder.PrependInt32Slot(1, MaxFavorLevelLength, 0)


    @staticmethod
    def AddStatBonusRateAttackLength(builder, StatBonusRateAttackLength): builder.PrependInt32Slot(2, StatBonusRateAttackLength, 0)


    @staticmethod
    def AddStatBonusRateHPLength(builder, StatBonusRateHPLength): builder.PrependInt32Slot(3, StatBonusRateHPLength, 0)


    @staticmethod
    def AddStatBonusRateHealLength(builder, StatBonusRateHealLength): builder.PrependInt32Slot(4, StatBonusRateHealLength, 0)


    @staticmethod
    def AddRecipeIdLength(builder, RecipeIdLength): builder.PrependInt32Slot(5, RecipeIdLength, 0)


    @staticmethod
    def AddSkillSlotALength(builder, SkillSlotALength): builder.PrependInt32Slot(6, SkillSlotALength, 0)


    @staticmethod
    def AddSkillSlotBLength(builder, SkillSlotBLength): builder.PrependInt32Slot(7, SkillSlotBLength, 0)


    @staticmethod
    def AddSkillSlotCLength(builder, SkillSlotCLength): builder.PrependInt32Slot(8, SkillSlotCLength, 0)


    @staticmethod
    def AddMaxlevelStarLength(builder, MaxlevelStarLength): builder.PrependInt32Slot(9, MaxlevelStarLength, 0)

