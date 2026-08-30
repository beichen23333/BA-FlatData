
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TimeAttackDungeonGeasExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TimeAttackDungeonGeasExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeAttackDungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearDefaultPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearTimeWeightPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TimeWeightConst(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Difficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPassiveSkillIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GeasIconPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GeasLocalizeEtcKeyLength(self):
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
    def AddTimeAttackDungeonType(builder, TimeAttackDungeonType): builder.PrependInt32Slot(1, TimeAttackDungeonType, 0)


    @staticmethod
    def AddLocalizeEtcKey(builder, LocalizeEtcKey): builder.PrependUint32Slot(2, LocalizeEtcKey, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt32Slot(3, BattleDuration, 0)


    @staticmethod
    def AddClearDefaultPoint(builder, ClearDefaultPoint): builder.PrependInt32Slot(4, ClearDefaultPoint, 0)


    @staticmethod
    def AddClearTimeWeightPoint(builder, ClearTimeWeightPoint): builder.PrependInt32Slot(5, ClearTimeWeightPoint, 0)


    @staticmethod
    def AddTimeWeightConst(builder, TimeWeightConst): builder.PrependInt32Slot(6, TimeWeightConst, 0)


    @staticmethod
    def AddDifficulty(builder, Difficulty): builder.PrependInt32Slot(7, Difficulty, 0)


    @staticmethod
    def AddRecommandLevel(builder, RecommandLevel): builder.PrependInt32Slot(8, RecommandLevel, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt32Slot(9, GroundId, 0)


    @staticmethod
    def AddAllyPassiveSkillIdLength(builder, AllyPassiveSkillIdLength): builder.PrependInt32Slot(10, AllyPassiveSkillIdLength, 0)


    @staticmethod
    def AddAllyPassiveSkillLevelLength(builder, AllyPassiveSkillLevelLength): builder.PrependInt32Slot(11, AllyPassiveSkillLevelLength, 0)


    @staticmethod
    def AddEnemyPassiveSkillIdLength(builder, EnemyPassiveSkillIdLength): builder.PrependInt32Slot(12, EnemyPassiveSkillIdLength, 0)


    @staticmethod
    def AddEnemyPassiveSkillLevelLength(builder, EnemyPassiveSkillLevelLength): builder.PrependInt32Slot(13, EnemyPassiveSkillLevelLength, 0)


    @staticmethod
    def AddGeasIconPathLength(builder, GeasIconPathLength): builder.PrependInt32Slot(14, GeasIconPathLength, 0)


    @staticmethod
    def AddGeasLocalizeEtcKeyLength(builder, GeasLocalizeEtcKeyLength): builder.PrependInt32Slot(15, GeasLocalizeEtcKeyLength, 0)

