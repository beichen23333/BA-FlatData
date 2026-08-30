
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameJankenStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameJankenStageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def JankenStageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageTypeLocalize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StageNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PrevStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageDiscription(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def SKillCostEventChance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentStageRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StarGoalLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StarGoalAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyInfoImage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnemyInfoDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StageIconName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FixedEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Bgm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BgmClimax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(25)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(2, EventContentId, 0)


    @staticmethod
    def AddJankenStageType(builder, JankenStageType): builder.PrependInt32Slot(3, JankenStageType, 0)


    @staticmethod
    def AddStageTypeLocalize(builder, StageTypeLocalize): builder.PrependUint32Slot(4, StageTypeLocalize, 0)


    @staticmethod
    def AddStageNumber(builder, StageNumber): builder.PrependInt32Slot(5, StageNumber, 0)


    @staticmethod
    def AddStageDisplay(builder, StageDisplay): builder.PrependInt32Slot(6, StageDisplay, 0)


    @staticmethod
    def AddPrevStageId(builder, PrevStageId): builder.PrependInt32Slot(7, PrevStageId, 0)


    @staticmethod
    def AddEnemyId(builder, EnemyId): builder.PrependInt32Slot(8, EnemyId, 0)


    @staticmethod
    def AddStageDiscription(builder, StageDiscription): builder.PrependUint32Slot(9, StageDiscription, 0)


    @staticmethod
    def AddSKillCostEventChance(builder, SKillCostEventChance): builder.PrependInt32Slot(10, SKillCostEventChance, 0)


    @staticmethod
    def AddStageEnterCostType(builder, StageEnterCostType): builder.PrependInt32Slot(11, StageEnterCostType, 0)


    @staticmethod
    def AddStageEnterCostId(builder, StageEnterCostId): builder.PrependInt32Slot(12, StageEnterCostId, 0)


    @staticmethod
    def AddStageEnterCostAmount(builder, StageEnterCostAmount): builder.PrependInt32Slot(13, StageEnterCostAmount, 0)


    @staticmethod
    def AddEventContentStageRewardId(builder, EventContentStageRewardId): builder.PrependInt32Slot(14, EventContentStageRewardId, 0)


    @staticmethod
    def AddEnterScenarioGroupId(builder, EnterScenarioGroupId): builder.PrependInt32Slot(15, EnterScenarioGroupId, 0)


    @staticmethod
    def AddClearScenarioGroupId(builder, ClearScenarioGroupId): builder.PrependInt32Slot(16, ClearScenarioGroupId, 0)


    @staticmethod
    def AddStarGoalLength(builder, StarGoalLength): builder.PrependInt32Slot(17, StarGoalLength, 0)


    @staticmethod
    def AddStarGoalAmountLength(builder, StarGoalAmountLength): builder.PrependInt32Slot(18, StarGoalAmountLength, 0)


    @staticmethod
    def AddEnemyInfoImage(builder, EnemyInfoImage): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyInfoImage), 0)

    @staticmethod
    def AddEnemyInfoDifficulty(builder, EnemyInfoDifficulty): builder.PrependUint32Slot(20, EnemyInfoDifficulty, 0)


    @staticmethod
    def AddStageIconName(builder, StageIconName): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(StageIconName), 0)

    @staticmethod
    def AddFixedEchelon(builder, FixedEchelon): builder.PrependInt32Slot(22, FixedEchelon, 0)


    @staticmethod
    def AddBgm(builder, Bgm): builder.PrependInt32Slot(23, Bgm, 0)


    @staticmethod
    def AddBgmClimax(builder, BgmClimax): builder.PrependInt32Slot(24, BgmClimax, 0)

