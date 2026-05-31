
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InteractiveWorldRaidStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InteractiveWorldRaidStageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UseBossIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseBossAIPhaseSync(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def WorldRaidBossGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PortraitPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BGPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RaidSkillDescriptionListId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BossCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def BossCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def BossCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BossCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0


    def AssistCharacterLimitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DifficultyOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def RaidEnterAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReEnterAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidBattleEndRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RaidRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def BattleReadyTimelinePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        return o == 0


    def BattleReadyTimelinePhaseStart(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def BattleReadyTimelinePhaseStartAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def BattleReadyTimelinePhaseStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePhaseStartIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        return o == 0


    def BattleReadyTimelinePhaseEnd(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def BattleReadyTimelinePhaseEndAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def BattleReadyTimelinePhaseEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BattleReadyTimelinePhaseEndIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0


    def VictoryTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PhaseChangeTimelinePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TimeLinePhase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnterScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ClearScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def UseFixedEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsRaidScenarioBattle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ShowSkillCard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def BossBGInfoKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def DamageToWorldBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkill(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def AllyPassiveSkillLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        return o == 0


    def AllyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def AllyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def AllyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        return o == 0


    def AllyPassiveSkillRemoveCondition(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def AllyPassiveSkillRemoveConditionAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def AllyPassiveSkillRemoveConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def AllyPassiveSkillRemoveConditionIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        return o == 0


    def EnemyPassiveSkill(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def EnemyPassiveSkillLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        return o == 0


    def EnemyPassiveSkillLevel(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def EnemyPassiveSkillLevelAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def EnemyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillLevelIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        return o == 0


    def EnemyPassiveSkillRemoveCondition(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def EnemyPassiveSkillRemoveConditionAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def EnemyPassiveSkillRemoveConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnemyPassiveSkillRemoveConditionIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        return o == 0


    def SaveCurrentLocalBossHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(40)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddUseBossIndex(builder, UseBossIndex): builder.PrependBoolSlot(1, UseBossIndex, 0)


    @staticmethod
    def AddUseBossAIPhaseSync(builder, UseBossAIPhaseSync): builder.PrependBoolSlot(2, UseBossAIPhaseSync, 0)


    @staticmethod
    def AddWorldRaidBossGroupId(builder, WorldRaidBossGroupId): builder.PrependInt64Slot(3, WorldRaidBossGroupId, 0)


    @staticmethod
    def AddPortraitPath(builder, PortraitPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PortraitPath), 0)

    @staticmethod
    def AddBGPath(builder, BGPath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BGPath), 0)

    @staticmethod
    def AddRaidSkillDescriptionListId(builder, RaidSkillDescriptionListId): builder.PrependInt64Slot(6, RaidSkillDescriptionListId, 0)


    @staticmethod
    def AddRaidCharacterId(builder, RaidCharacterId): builder.PrependInt64Slot(7, RaidCharacterId, 0)


    @staticmethod
    def AddBossCharacterId(builder, BossCharacterId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BossCharacterId), 0)
    @staticmethod
    def StartBossCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddAssistCharacterLimitCount(builder, AssistCharacterLimitCount): builder.PrependInt64Slot(9, AssistCharacterLimitCount, 0)


    @staticmethod
    def AddWorldRaidDifficulty(builder, WorldRaidDifficulty): builder.PrependInt32Slot(10, WorldRaidDifficulty, 0)


    @staticmethod
    def AddDifficultyOpenCondition(builder, DifficultyOpenCondition): builder.PrependBoolSlot(11, DifficultyOpenCondition, 0)


    @staticmethod
    def AddRaidEnterAmount(builder, RaidEnterAmount): builder.PrependInt64Slot(12, RaidEnterAmount, 0)


    @staticmethod
    def AddReEnterAmount(builder, ReEnterAmount): builder.PrependInt64Slot(13, ReEnterAmount, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt64Slot(14, BattleDuration, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt64Slot(15, GroundId, 0)


    @staticmethod
    def AddRaidBattleEndRewardGroupId(builder, RaidBattleEndRewardGroupId): builder.PrependInt64Slot(16, RaidBattleEndRewardGroupId, 0)


    @staticmethod
    def AddRaidRewardGroupId(builder, RaidRewardGroupId): builder.PrependInt64Slot(17, RaidRewardGroupId, 0)


    @staticmethod
    def AddBattleReadyTimelinePath(builder, BattleReadyTimelinePath): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePath), 0)
    @staticmethod
    def StartBattleReadyTimelinePathVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddBattleReadyTimelinePhaseStart(builder, BattleReadyTimelinePhaseStart): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseStart), 0)
    @staticmethod
    def StartBattleReadyTimelinePhaseStartVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddBattleReadyTimelinePhaseEnd(builder, BattleReadyTimelinePhaseEnd): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(BattleReadyTimelinePhaseEnd), 0)
    @staticmethod
    def StartBattleReadyTimelinePhaseEndVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)

    @staticmethod
    def AddPhaseChangeTimelinePath(builder, PhaseChangeTimelinePath): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseChangeTimelinePath), 0)

    @staticmethod
    def AddTimeLinePhase(builder, TimeLinePhase): builder.PrependInt64Slot(23, TimeLinePhase, 0)


    @staticmethod
    def AddEnterScenarioKey(builder, EnterScenarioKey): builder.PrependInt64Slot(24, EnterScenarioKey, 0)


    @staticmethod
    def AddClearScenarioKey(builder, ClearScenarioKey): builder.PrependInt64Slot(25, ClearScenarioKey, 0)


    @staticmethod
    def AddUseFixedEchelon(builder, UseFixedEchelon): builder.PrependBoolSlot(26, UseFixedEchelon, 0)


    @staticmethod
    def AddFixedEchelonId(builder, FixedEchelonId): builder.PrependInt64Slot(27, FixedEchelonId, 0)


    @staticmethod
    def AddIsRaidScenarioBattle(builder, IsRaidScenarioBattle): builder.PrependBoolSlot(28, IsRaidScenarioBattle, 0)


    @staticmethod
    def AddShowSkillCard(builder, ShowSkillCard): builder.PrependBoolSlot(29, ShowSkillCard, 0)


    @staticmethod
    def AddBossBGInfoKey(builder, BossBGInfoKey): builder.PrependUint32Slot(30, BossBGInfoKey, 0)


    @staticmethod
    def AddDamageToWorldBoss(builder, DamageToWorldBoss): builder.PrependInt64Slot(31, DamageToWorldBoss, 0)


    @staticmethod
    def AddAllyPassiveSkill(builder, AllyPassiveSkill): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkill), 0)
    @staticmethod
    def StartAllyPassiveSkillVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddAllyPassiveSkillLevel(builder, AllyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(33, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillLevel), 0)
    @staticmethod
    def StartAllyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddAllyPassiveSkillRemoveCondition(builder, AllyPassiveSkillRemoveCondition): builder.PrependUOffsetTRelativeSlot(34, flatbuffers.number_types.UOffsetTFlags.py_type(AllyPassiveSkillRemoveCondition), 0)
    @staticmethod
    def StartAllyPassiveSkillRemoveConditionVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddEnemyPassiveSkill(builder, EnemyPassiveSkill): builder.PrependUOffsetTRelativeSlot(35, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkill), 0)
    @staticmethod
    def StartEnemyPassiveSkillVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEnemyPassiveSkillLevel(builder, EnemyPassiveSkillLevel): builder.PrependUOffsetTRelativeSlot(36, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkillLevel), 0)
    @staticmethod
    def StartEnemyPassiveSkillLevelVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEnemyPassiveSkillRemoveCondition(builder, EnemyPassiveSkillRemoveCondition): builder.PrependUOffsetTRelativeSlot(37, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyPassiveSkillRemoveCondition), 0)
    @staticmethod
    def StartEnemyPassiveSkillRemoveConditionVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddSaveCurrentLocalBossHP(builder, SaveCurrentLocalBossHP): builder.PrependBoolSlot(38, SaveCurrentLocalBossHP, 0)


    @staticmethod
    def AddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(39, EchelonExtensionType, 0)

