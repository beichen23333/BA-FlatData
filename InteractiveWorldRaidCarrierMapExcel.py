
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InteractiveWorldRaidCarrierMapExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InteractiveWorldRaidCarrierMapExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConditionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldRaidPhaseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReplaySeasonGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ReplaySeasonOriginalPhaseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RecentClearBossGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RecentClearEventStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ChangeTarget(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Priority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ArtLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BridgeBGM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def HangarBGM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LobbyBGM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def WorldMapBGM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InformationGroupIdWorldMap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InformationGroupIdUCPopup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InformationGroupIdBridge(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InformationGroupIdHangar(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InformationGroupIdLobby(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(21)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddConditionId(builder, ConditionId): builder.PrependInt64Slot(1, ConditionId, 0)


    @staticmethod
    def AddWorldRaidSeasonId(builder, WorldRaidSeasonId): builder.PrependInt64Slot(2, WorldRaidSeasonId, 0)


    @staticmethod
    def AddWorldRaidPhaseId(builder, WorldRaidPhaseId): builder.PrependInt64Slot(3, WorldRaidPhaseId, 0)


    @staticmethod
    def AddReplaySeasonGroupId(builder, ReplaySeasonGroupId): builder.PrependInt64Slot(4, ReplaySeasonGroupId, 0)


    @staticmethod
    def AddReplaySeasonOriginalPhaseId(builder, ReplaySeasonOriginalPhaseId): builder.PrependInt64Slot(5, ReplaySeasonOriginalPhaseId, 0)


    @staticmethod
    def AddRecentClearBossGroupId(builder, RecentClearBossGroupId): builder.PrependInt64Slot(6, RecentClearBossGroupId, 0)


    @staticmethod
    def AddRecentClearEventStageId(builder, RecentClearEventStageId): builder.PrependInt64Slot(7, RecentClearEventStageId, 0)


    @staticmethod
    def AddChangeTarget(builder, ChangeTarget): builder.PrependInt32Slot(8, ChangeTarget, 0)


    @staticmethod
    def AddPriority(builder, Priority): builder.PrependInt64Slot(9, Priority, 0)


    @staticmethod
    def AddArtLevelPath(builder, ArtLevelPath): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(ArtLevelPath), 0)

    @staticmethod
    def AddDesignLevelPath(builder, DesignLevelPath): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(DesignLevelPath), 0)

    @staticmethod
    def AddBridgeBGM(builder, BridgeBGM): builder.PrependInt64Slot(12, BridgeBGM, 0)


    @staticmethod
    def AddHangarBGM(builder, HangarBGM): builder.PrependInt64Slot(13, HangarBGM, 0)


    @staticmethod
    def AddLobbyBGM(builder, LobbyBGM): builder.PrependInt64Slot(14, LobbyBGM, 0)


    @staticmethod
    def AddWorldMapBGM(builder, WorldMapBGM): builder.PrependInt64Slot(15, WorldMapBGM, 0)


    @staticmethod
    def AddInformationGroupIdWorldMap(builder, InformationGroupIdWorldMap): builder.PrependInt64Slot(16, InformationGroupIdWorldMap, 0)


    @staticmethod
    def AddInformationGroupIdUCPopup(builder, InformationGroupIdUCPopup): builder.PrependInt64Slot(17, InformationGroupIdUCPopup, 0)


    @staticmethod
    def AddInformationGroupIdBridge(builder, InformationGroupIdBridge): builder.PrependInt64Slot(18, InformationGroupIdBridge, 0)


    @staticmethod
    def AddInformationGroupIdHangar(builder, InformationGroupIdHangar): builder.PrependInt64Slot(19, InformationGroupIdHangar, 0)


    @staticmethod
    def AddInformationGroupIdLobby(builder, InformationGroupIdLobby): builder.PrependInt64Slot(20, InformationGroupIdLobby, 0)

