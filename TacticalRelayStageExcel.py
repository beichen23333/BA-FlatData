
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticalRelayStageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticalRelayStageExcel()
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


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StageDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WavesPerSectionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLevelGapForGuide(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinEquipmentTierForGuideLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinSkillLevelForGuideLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PrevStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageTopography(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyArmorType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemySubArmorType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageEnterCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TacticRewardExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageRewardIdEgo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageRewardIdConscious(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageRewardIdUnconscious(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageRewardLocalizePrefabId01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StageRewardLocalizePrefabId02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StageRewardLocalizePrefabId03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def EchelonCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotDefineId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorCollectionScoreBonusId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonExtensionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AssistSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StageHint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def WaveInfoTipIconPathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WaveInfoTipLocalizeEtcIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(35)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt32Slot(2, SeasonId, 0)


    @staticmethod
    def AddStageType(builder, StageType): builder.PrependInt32Slot(3, StageType, 0)


    @staticmethod
    def AddStageNumber(builder, StageNumber): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(StageNumber), 0)

    @staticmethod
    def AddStageDifficulty(builder, StageDifficulty): builder.PrependInt32Slot(5, StageDifficulty, 0)


    @staticmethod
    def AddWavesPerSectionsLength(builder, WavesPerSectionsLength): builder.PrependInt32Slot(6, WavesPerSectionsLength, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt32Slot(7, BattleDuration, 0)


    @staticmethod
    def AddRecommandLevel(builder, RecommandLevel): builder.PrependInt32Slot(8, RecommandLevel, 0)


    @staticmethod
    def AddRecommandLevelGapForGuide(builder, RecommandLevelGapForGuide): builder.PrependInt32Slot(9, RecommandLevelGapForGuide, 0)


    @staticmethod
    def AddMinEquipmentTierForGuideLength(builder, MinEquipmentTierForGuideLength): builder.PrependInt32Slot(10, MinEquipmentTierForGuideLength, 0)


    @staticmethod
    def AddMinSkillLevelForGuideLength(builder, MinSkillLevelForGuideLength): builder.PrependInt32Slot(11, MinSkillLevelForGuideLength, 0)


    @staticmethod
    def AddPrevStageId(builder, PrevStageId): builder.PrependInt32Slot(12, PrevStageId, 0)


    @staticmethod
    def AddGroundID(builder, GroundID): builder.PrependInt32Slot(13, GroundID, 0)


    @staticmethod
    def AddStageTopography(builder, StageTopography): builder.PrependInt32Slot(14, StageTopography, 0)


    @staticmethod
    def AddEnemyArmorType(builder, EnemyArmorType): builder.PrependInt32Slot(15, EnemyArmorType, 0)


    @staticmethod
    def AddEnemySubArmorType(builder, EnemySubArmorType): builder.PrependInt32Slot(16, EnemySubArmorType, 0)


    @staticmethod
    def AddStageEnterCostType(builder, StageEnterCostType): builder.PrependInt32Slot(17, StageEnterCostType, 0)


    @staticmethod
    def AddStageEnterCostId(builder, StageEnterCostId): builder.PrependInt32Slot(18, StageEnterCostId, 0)


    @staticmethod
    def AddStageEnterCostAmount(builder, StageEnterCostAmount): builder.PrependInt32Slot(19, StageEnterCostAmount, 0)


    @staticmethod
    def AddTacticRewardExp(builder, TacticRewardExp): builder.PrependInt32Slot(20, TacticRewardExp, 0)


    @staticmethod
    def AddStageRewardIdEgo(builder, StageRewardIdEgo): builder.PrependInt32Slot(21, StageRewardIdEgo, 0)


    @staticmethod
    def AddStageRewardIdConscious(builder, StageRewardIdConscious): builder.PrependInt32Slot(22, StageRewardIdConscious, 0)


    @staticmethod
    def AddStageRewardIdUnconscious(builder, StageRewardIdUnconscious): builder.PrependInt32Slot(23, StageRewardIdUnconscious, 0)


    @staticmethod
    def AddStageRewardLocalizePrefabId01(builder, StageRewardLocalizePrefabId01): builder.PrependUint32Slot(24, StageRewardLocalizePrefabId01, 0)


    @staticmethod
    def AddStageRewardLocalizePrefabId02(builder, StageRewardLocalizePrefabId02): builder.PrependUint32Slot(25, StageRewardLocalizePrefabId02, 0)


    @staticmethod
    def AddStageRewardLocalizePrefabId03(builder, StageRewardLocalizePrefabId03): builder.PrependUint32Slot(26, StageRewardLocalizePrefabId03, 0)


    @staticmethod
    def AddEchelonCount(builder, EchelonCount): builder.PrependInt32Slot(27, EchelonCount, 0)


    @staticmethod
    def AddApcSlotDefineId(builder, ApcSlotDefineId): builder.PrependInt32Slot(28, ApcSlotDefineId, 0)


    @staticmethod
    def AddFavorCollectionScoreBonusId(builder, FavorCollectionScoreBonusId): builder.PrependInt32Slot(29, FavorCollectionScoreBonusId, 0)


    @staticmethod
    def AddEchelonExtensionType(builder, EchelonExtensionType): builder.PrependInt32Slot(30, EchelonExtensionType, 0)


    @staticmethod
    def AddAssistSlot(builder, AssistSlot): builder.PrependInt32Slot(31, AssistSlot, 0)


    @staticmethod
    def AddStageHint(builder, StageHint): builder.PrependUint32Slot(32, StageHint, 0)


    @staticmethod
    def AddWaveInfoTipIconPathLength(builder, WaveInfoTipIconPathLength): builder.PrependInt32Slot(33, WaveInfoTipIconPathLength, 0)


    @staticmethod
    def AddWaveInfoTipLocalizeEtcIdLength(builder, WaveInfoTipLocalizeEtcIdLength): builder.PrependInt32Slot(34, WaveInfoTipLocalizeEtcIdLength, 0)

