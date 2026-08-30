
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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BossCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AssistCharacterLimitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ReEnterAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidBattleEndRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RaidRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePhaseStartLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleReadyTimelinePhaseEndLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnterScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearScenarioKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseFixedEchelon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def FixedEchelonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllyPassiveSkillRemoveConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPassiveSkillLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPassiveSkillLevelLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPassiveSkillRemoveConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


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
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddUseBossIndex(builder, UseBossIndex): builder.PrependBoolSlot(1, UseBossIndex, 0)


    @staticmethod
    def AddUseBossAIPhaseSync(builder, UseBossAIPhaseSync): builder.PrependBoolSlot(2, UseBossAIPhaseSync, 0)


    @staticmethod
    def AddWorldRaidBossGroupId(builder, WorldRaidBossGroupId): builder.PrependInt32Slot(3, WorldRaidBossGroupId, 0)


    @staticmethod
    def AddPortraitPath(builder, PortraitPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(PortraitPath), 0)

    @staticmethod
    def AddBGPath(builder, BGPath): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(BGPath), 0)

    @staticmethod
    def AddRaidSkillDescriptionListId(builder, RaidSkillDescriptionListId): builder.PrependInt32Slot(6, RaidSkillDescriptionListId, 0)


    @staticmethod
    def AddRaidCharacterId(builder, RaidCharacterId): builder.PrependInt32Slot(7, RaidCharacterId, 0)


    @staticmethod
    def AddBossCharacterIdLength(builder, BossCharacterIdLength): builder.PrependInt32Slot(8, BossCharacterIdLength, 0)


    @staticmethod
    def AddAssistCharacterLimitCount(builder, AssistCharacterLimitCount): builder.PrependInt32Slot(9, AssistCharacterLimitCount, 0)


    @staticmethod
    def AddWorldRaidDifficulty(builder, WorldRaidDifficulty): builder.PrependInt32Slot(10, WorldRaidDifficulty, 0)


    @staticmethod
    def AddDifficultyOpenCondition(builder, DifficultyOpenCondition): builder.PrependBoolSlot(11, DifficultyOpenCondition, 0)


    @staticmethod
    def AddRaidEnterAmount(builder, RaidEnterAmount): builder.PrependInt32Slot(12, RaidEnterAmount, 0)


    @staticmethod
    def AddReEnterAmount(builder, ReEnterAmount): builder.PrependInt32Slot(13, ReEnterAmount, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt32Slot(14, BattleDuration, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt32Slot(15, GroundId, 0)


    @staticmethod
    def AddRaidBattleEndRewardGroupId(builder, RaidBattleEndRewardGroupId): builder.PrependInt32Slot(16, RaidBattleEndRewardGroupId, 0)


    @staticmethod
    def AddRaidRewardGroupId(builder, RaidRewardGroupId): builder.PrependInt32Slot(17, RaidRewardGroupId, 0)


    @staticmethod
    def AddBattleReadyTimelinePathLength(builder, BattleReadyTimelinePathLength): builder.PrependInt32Slot(18, BattleReadyTimelinePathLength, 0)


    @staticmethod
    def AddBattleReadyTimelinePhaseStartLength(builder, BattleReadyTimelinePhaseStartLength): builder.PrependInt32Slot(19, BattleReadyTimelinePhaseStartLength, 0)


    @staticmethod
    def AddBattleReadyTimelinePhaseEndLength(builder, BattleReadyTimelinePhaseEndLength): builder.PrependInt32Slot(20, BattleReadyTimelinePhaseEndLength, 0)


    @staticmethod
    def AddVictoryTimelinePath(builder, VictoryTimelinePath): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(VictoryTimelinePath), 0)

    @staticmethod
    def AddPhaseChangeTimelinePath(builder, PhaseChangeTimelinePath): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseChangeTimelinePath), 0)

    @staticmethod
    def AddTimeLinePhase(builder, TimeLinePhase): builder.PrependInt32Slot(23, TimeLinePhase, 0)


    @staticmethod
    def AddEnterScenarioKey(builder, EnterScenarioKey): builder.PrependInt32Slot(24, EnterScenarioKey, 0)


    @staticmethod
    def AddClearScenarioKey(builder, ClearScenarioKey): builder.PrependInt32Slot(25, ClearScenarioKey, 0)


    @staticmethod
    def AddUseFixedEchelon(builder, UseFixedEchelon): builder.PrependBoolSlot(26, UseFixedEchelon, 0)


    @staticmethod
    def AddFixedEchelonId(builder, FixedEchelonId): builder.PrependInt32Slot(27, FixedEchelonId, 0)


    @staticmethod
    def AddIsRaidScenarioBattle(builder, IsRaidScenarioBattle): builder.PrependBoolSlot(28, IsRaidScenarioBattle, 0)


    @staticmethod
    def AddShowSkillCard(builder, ShowSkillCard): builder.PrependBoolSlot(29, ShowSkillCard, 0)


    @staticmethod
    def AddBossBGInfoKey(builder, BossBGInfoKey): builder.PrependUint32Slot(30, BossBGInfoKey, 0)


    @staticmethod
    def AddDamageToWorldBoss(builder, DamageToWorldBoss): builder.PrependInt32Slot(31, DamageToWorldBoss, 0)


    @staticmethod
    def AddAllyPassiveSkillLength(builder, AllyPassiveSkillLength): builder.PrependInt32Slot(32, AllyPassiveSkillLength, 0)


    @staticmethod
    def AddAllyPassiveSkillLevelLength(builder, AllyPassiveSkillLevelLength): builder.PrependInt32Slot(33, AllyPassiveSkillLevelLength, 0)


    @staticmethod
    def AddAllyPassiveSkillRemoveConditionLength(builder, AllyPassiveSkillRemoveConditionLength): builder.PrependInt32Slot(34, AllyPassiveSkillRemoveConditionLength, 0)


    @staticmethod
    def AddEnemyPassiveSkillLength(builder, EnemyPassiveSkillLength): builder.PrependInt32Slot(35, EnemyPassiveSkillLength, 0)


    @staticmethod
    def AddEnemyPassiveSkillLevelLength(builder, EnemyPassiveSkillLevelLength): builder.PrependInt32Slot(36, EnemyPassiveSkillLevelLength, 0)


    @staticmethod
    def AddEnemyPassiveSkillRemoveConditionLength(builder, EnemyPassiveSkillRemoveConditionLength): builder.PrependInt32Slot(37, EnemyPassiveSkillRemoveConditionLength, 0)


    @staticmethod
    def AddSaveCurrentLocalBossHP(builder, SaveCurrentLocalBossHP): builder.PrependBoolSlot(38, SaveCurrentLocalBossHP, 0)


    @staticmethod
    def AddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(39, EchelonExtensionType, 0)

