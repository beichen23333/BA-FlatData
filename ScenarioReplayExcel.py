
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ScenarioReplayExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScenarioReplayExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VolumeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ReplayType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ChapterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EpisodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FrontScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BattleDuration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BackScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddModeId(builder, ModeId): builder.PrependInt32Slot(0, ModeId, 0)


    @staticmethod
    def AddVolumeId(builder, VolumeId): builder.PrependInt32Slot(1, VolumeId, 0)


    @staticmethod
    def AddReplayType(builder, ReplayType): builder.PrependInt32Slot(2, ReplayType, 0)


    @staticmethod
    def AddChapterId(builder, ChapterId): builder.PrependInt32Slot(3, ChapterId, 0)


    @staticmethod
    def AddEpisodeId(builder, EpisodeId): builder.PrependInt32Slot(4, EpisodeId, 0)


    @staticmethod
    def AddFrontScenarioGroupIdLength(builder, FrontScenarioGroupIdLength): builder.PrependInt32Slot(5, FrontScenarioGroupIdLength, 0)


    @staticmethod
    def AddGroundId(builder, GroundId): builder.PrependInt32Slot(6, GroundId, 0)


    @staticmethod
    def AddBattleDuration(builder, BattleDuration): builder.PrependInt32Slot(7, BattleDuration, 0)


    @staticmethod
    def AddBackScenarioGroupIdLength(builder, BackScenarioGroupIdLength): builder.PrependInt32Slot(8, BackScenarioGroupIdLength, 0)

