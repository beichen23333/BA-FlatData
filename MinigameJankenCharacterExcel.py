
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameJankenCharacterExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameJankenCharacterExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsPlayable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IconResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IconDecoResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def NameTagResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BattlePortraitResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillIconResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillCardResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def CharacterNameLocalizeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def AttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HitPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BlockPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def JankenSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsBossUnit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ATGGauge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ATGDmgBlock(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ATGDmgHit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ATGLogicEffect(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def AiProfile(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(23)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddIsPlayable(builder, IsPlayable): builder.PrependBoolSlot(1, IsPlayable, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(2, DisplayOrder, 0)


    @staticmethod
    def AddIconResourceName(builder, IconResourceName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(IconResourceName), 0)

    @staticmethod
    def AddIconDecoResourceName(builder, IconDecoResourceName): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(IconDecoResourceName), 0)

    @staticmethod
    def AddNameTagResourceName(builder, NameTagResourceName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(NameTagResourceName), 0)

    @staticmethod
    def AddBattlePortraitResource(builder, BattlePortraitResource): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(BattlePortraitResource), 0)

    @staticmethod
    def AddSkillIconResourceName(builder, SkillIconResourceName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(SkillIconResourceName), 0)

    @staticmethod
    def AddSkillCardResourceName(builder, SkillCardResourceName): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(SkillCardResourceName), 0)

    @staticmethod
    def AddLocalizeId(builder, LocalizeId): builder.PrependUint32Slot(9, LocalizeId, 0)


    @staticmethod
    def AddCharacterNameLocalizeId(builder, CharacterNameLocalizeId): builder.PrependUint32Slot(10, CharacterNameLocalizeId, 0)


    @staticmethod
    def AddAttackPower(builder, AttackPower): builder.PrependInt32Slot(11, AttackPower, 0)


    @staticmethod
    def AddHitPoint(builder, HitPoint): builder.PrependInt32Slot(12, HitPoint, 0)


    @staticmethod
    def AddBlockPower(builder, BlockPower): builder.PrependInt32Slot(13, BlockPower, 0)


    @staticmethod
    def AddJankenSkill(builder, JankenSkill): builder.PrependInt32Slot(14, JankenSkill, 0)


    @staticmethod
    def AddIsBoss(builder, IsBoss): builder.PrependBoolSlot(15, IsBoss, 0)


    @staticmethod
    def AddIsBossUnit(builder, IsBossUnit): builder.PrependBoolSlot(16, IsBossUnit, 0)


    @staticmethod
    def AddATGGauge(builder, ATGGauge): builder.PrependInt32Slot(17, ATGGauge, 0)


    @staticmethod
    def AddATGDmgBlock(builder, ATGDmgBlock): builder.PrependFloat32Slot(18, ATGDmgBlock, 0)


    @staticmethod
    def AddATGDmgHit(builder, ATGDmgHit): builder.PrependFloat32Slot(19, ATGDmgHit, 0)


    @staticmethod
    def AddATGLogicEffect(builder, ATGLogicEffect): builder.PrependInt32Slot(20, ATGLogicEffect, 0)


    @staticmethod
    def AddModelPrefabName(builder, ModelPrefabName): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(ModelPrefabName), 0)

    @staticmethod
    def AddAiProfile(builder, AiProfile): builder.PrependInt32Slot(22, AiProfile, 0)

