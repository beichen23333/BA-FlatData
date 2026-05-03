
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterWeaponExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterWeaponExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SetRecipe(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatLevelUpType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackPower100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxHP100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HealPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HealPower100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnlockLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecipeIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LearnSkillSlotLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(16)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddImagePath(builder, ImagePath): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(ImagePath), 0)

    @staticmethod
    def AddSetRecipe(builder, SetRecipe): builder.PrependInt32Slot(2, SetRecipe, 0)


    @staticmethod
    def AddStatLevelUpType(builder, StatLevelUpType): builder.PrependInt32Slot(3, StatLevelUpType, 0)


    @staticmethod
    def AddAttackPower(builder, AttackPower): builder.PrependInt32Slot(4, AttackPower, 0)


    @staticmethod
    def AddAttackPower100(builder, AttackPower100): builder.PrependInt32Slot(5, AttackPower100, 0)


    @staticmethod
    def AddMaxHP(builder, MaxHP): builder.PrependInt32Slot(6, MaxHP, 0)


    @staticmethod
    def AddMaxHP100(builder, MaxHP100): builder.PrependInt32Slot(7, MaxHP100, 0)


    @staticmethod
    def AddHealPower(builder, HealPower): builder.PrependInt32Slot(8, HealPower, 0)


    @staticmethod
    def AddHealPower100(builder, HealPower100): builder.PrependInt32Slot(9, HealPower100, 0)


    @staticmethod
    def AddUnlockLength(builder, UnlockLength): builder.PrependInt32Slot(10, UnlockLength, 0)


    @staticmethod
    def AddRecipeIdLength(builder, RecipeIdLength): builder.PrependInt32Slot(11, RecipeIdLength, 0)


    @staticmethod
    def AddMaxLevelLength(builder, MaxLevelLength): builder.PrependInt32Slot(12, MaxLevelLength, 0)


    @staticmethod
    def AddLearnSkillSlotLength(builder, LearnSkillSlotLength): builder.PrependInt32Slot(13, LearnSkillSlotLength, 0)


    @staticmethod
    def AddStatTypeLength(builder, StatTypeLength): builder.PrependInt32Slot(14, StatTypeLength, 0)


    @staticmethod
    def AddStatValueLength(builder, StatValueLength): builder.PrependInt32Slot(15, StatValueLength, 0)

