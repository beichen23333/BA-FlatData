
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMinigameJankenExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMinigameJankenExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def TimeLimitPerTurn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DamageCurveCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def DrawConstantAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DrawConstantBlock(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WinSceneRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LoseSceneRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyAppearRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlayerSpAtkConditionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemySpAtkConditionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ATGGroggyFixedDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxSkillCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeLimitQTE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageOutroTimeOffset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UIBossHpBarCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(15)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddTimeLimitPerTurn(builder, TimeLimitPerTurn): builder.PrependInt32Slot(0, TimeLimitPerTurn, 0)


    @staticmethod
    def AddMaxDamageRate(builder, MaxDamageRate): builder.PrependInt32Slot(1, MaxDamageRate, 0)


    @staticmethod
    def AddDamageCurveCoefficient(builder, DamageCurveCoefficient): builder.PrependFloat32Slot(2, DamageCurveCoefficient, 0)


    @staticmethod
    def AddDrawConstantAttack(builder, DrawConstantAttack): builder.PrependInt32Slot(3, DrawConstantAttack, 0)


    @staticmethod
    def AddDrawConstantBlock(builder, DrawConstantBlock): builder.PrependInt32Slot(4, DrawConstantBlock, 0)


    @staticmethod
    def AddWinSceneRate(builder, WinSceneRate): builder.PrependInt32Slot(5, WinSceneRate, 0)


    @staticmethod
    def AddLoseSceneRate(builder, LoseSceneRate): builder.PrependInt32Slot(6, LoseSceneRate, 0)


    @staticmethod
    def AddEnemyAppearRate(builder, EnemyAppearRate): builder.PrependInt32Slot(7, EnemyAppearRate, 0)


    @staticmethod
    def AddPlayerSpAtkConditionRate(builder, PlayerSpAtkConditionRate): builder.PrependInt32Slot(8, PlayerSpAtkConditionRate, 0)


    @staticmethod
    def AddEnemySpAtkConditionRate(builder, EnemySpAtkConditionRate): builder.PrependInt32Slot(9, EnemySpAtkConditionRate, 0)


    @staticmethod
    def AddATGGroggyFixedDamage(builder, ATGGroggyFixedDamage): builder.PrependInt32Slot(10, ATGGroggyFixedDamage, 0)


    @staticmethod
    def AddMaxSkillCost(builder, MaxSkillCost): builder.PrependInt32Slot(11, MaxSkillCost, 0)


    @staticmethod
    def AddTimeLimitQTE(builder, TimeLimitQTE): builder.PrependInt32Slot(12, TimeLimitQTE, 0)


    @staticmethod
    def AddStageOutroTimeOffset(builder, StageOutroTimeOffset): builder.PrependInt32Slot(13, StageOutroTimeOffset, 0)


    @staticmethod
    def AddUIBossHpBarCount(builder, UIBossHpBarCount): builder.PrependInt32Slot(14, UIBossHpBarCount, 0)

