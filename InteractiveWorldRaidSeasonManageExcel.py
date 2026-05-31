
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InteractiveWorldRaidSeasonManageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InteractiveWorldRaidSeasonManageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PhaseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PhaseStartCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def IsReplaySeason(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def EnterTicket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PhaseEndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldRaidLobbyScene(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldRaidLobbyBanner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldRaidLobbyBG(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldRaidLobbyBannerShow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SeasonOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidLobbyEnterScenario(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CanPlayNotSeasonTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def WorldRaidUniqueThemeLobbyUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def WorldRaidUniqueThemeName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CanWorldRaidGemEnter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def HideWorldRaidTicketUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def HideWorldRaidBossCompleteRewardUI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def UseWorldRaidCommonToast(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OpenRaidBossGroupId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def OpenRaidBossGroupIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def OpenRaidBossGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def OpenRaidBossGroupIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0


    def BossSpawnTime(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def BossSpawnTimeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def BossSpawnTimeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        return o == 0


    def EliminateTime(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def EliminateTimeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EliminateTimeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        return o == 0


    def ScenarioOutputConditionId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def ScenarioOutputConditionIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def ScenarioOutputConditionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ScenarioOutputConditionIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        return o == 0


    def ConditionScenarioGroupid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def ConditionScenarioGroupidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def ConditionScenarioGroupidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def ConditionScenarioGroupidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        return o == 0


    def CarrierSkillGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidMapEnterOperator(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def UseFavorRankBuff(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(28)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt64Slot(0, SeasonId, 0)


    @staticmethod
    def AddPhaseId(builder, PhaseId): builder.PrependInt64Slot(1, PhaseId, 0)


    @staticmethod
    def AddPhaseStartCondition(builder, PhaseStartCondition): builder.PrependInt64Slot(2, PhaseStartCondition, 0)


    @staticmethod
    def AddIsReplaySeason(builder, IsReplaySeason): builder.PrependBoolSlot(3, IsReplaySeason, 0)


    @staticmethod
    def AddEnterTicket(builder, EnterTicket): builder.PrependInt32Slot(4, EnterTicket, 0)


    @staticmethod
    def AddPhaseStartTime(builder, PhaseStartTime): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseStartTime), 0)

    @staticmethod
    def AddPhaseEndTime(builder, PhaseEndTime): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(PhaseEndTime), 0)

    @staticmethod
    def AddWorldRaidLobbyScene(builder, WorldRaidLobbyScene): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(WorldRaidLobbyScene), 0)

    @staticmethod
    def AddWorldRaidLobbyBanner(builder, WorldRaidLobbyBanner): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(WorldRaidLobbyBanner), 0)

    @staticmethod
    def AddWorldRaidLobbyBG(builder, WorldRaidLobbyBG): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(WorldRaidLobbyBG), 0)

    @staticmethod
    def AddWorldRaidLobbyBannerShow(builder, WorldRaidLobbyBannerShow): builder.PrependBoolSlot(10, WorldRaidLobbyBannerShow, 0)


    @staticmethod
    def AddSeasonOpenCondition(builder, SeasonOpenCondition): builder.PrependInt64Slot(11, SeasonOpenCondition, 0)


    @staticmethod
    def AddWorldRaidLobbyEnterScenario(builder, WorldRaidLobbyEnterScenario): builder.PrependInt64Slot(12, WorldRaidLobbyEnterScenario, 0)


    @staticmethod
    def AddCanPlayNotSeasonTime(builder, CanPlayNotSeasonTime): builder.PrependBoolSlot(13, CanPlayNotSeasonTime, 0)


    @staticmethod
    def AddWorldRaidUniqueThemeLobbyUI(builder, WorldRaidUniqueThemeLobbyUI): builder.PrependBoolSlot(14, WorldRaidUniqueThemeLobbyUI, 0)


    @staticmethod
    def AddWorldRaidUniqueThemeName(builder, WorldRaidUniqueThemeName): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(WorldRaidUniqueThemeName), 0)

    @staticmethod
    def AddCanWorldRaidGemEnter(builder, CanWorldRaidGemEnter): builder.PrependBoolSlot(16, CanWorldRaidGemEnter, 0)


    @staticmethod
    def AddHideWorldRaidTicketUI(builder, HideWorldRaidTicketUI): builder.PrependBoolSlot(17, HideWorldRaidTicketUI, 0)


    @staticmethod
    def AddHideWorldRaidBossCompleteRewardUI(builder, HideWorldRaidBossCompleteRewardUI): builder.PrependBoolSlot(18, HideWorldRaidBossCompleteRewardUI, 0)


    @staticmethod
    def AddUseWorldRaidCommonToast(builder, UseWorldRaidCommonToast): builder.PrependBoolSlot(19, UseWorldRaidCommonToast, 0)


    @staticmethod
    def AddOpenRaidBossGroupId(builder, OpenRaidBossGroupId): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(OpenRaidBossGroupId), 0)
    @staticmethod
    def StartOpenRaidBossGroupIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddBossSpawnTime(builder, BossSpawnTime): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(BossSpawnTime), 0)
    @staticmethod
    def StartBossSpawnTimeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddEliminateTime(builder, EliminateTime): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(EliminateTime), 0)
    @staticmethod
    def StartEliminateTimeVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddScenarioOutputConditionId(builder, ScenarioOutputConditionId): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(ScenarioOutputConditionId), 0)
    @staticmethod
    def StartScenarioOutputConditionIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddConditionScenarioGroupid(builder, ConditionScenarioGroupid): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(ConditionScenarioGroupid), 0)
    @staticmethod
    def StartConditionScenarioGroupidVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddCarrierSkillGroupId(builder, CarrierSkillGroupId): builder.PrependInt64Slot(25, CarrierSkillGroupId, 0)


    @staticmethod
    def AddWorldRaidMapEnterOperator(builder, WorldRaidMapEnterOperator): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(WorldRaidMapEnterOperator), 0)

    @staticmethod
    def AddUseFavorRankBuff(builder, UseFavorRankBuff): builder.PrependBoolSlot(27, UseFavorRankBuff, 0)

