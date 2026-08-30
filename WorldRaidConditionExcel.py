
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WorldRaidConditionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WorldRaidConditionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LockUILength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HideWhenLocked(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def AccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScenarioModeIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CampaignStageIDLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultipleConditionCheckType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AfterWhenDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldRaidBossKillLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddLockUILength(builder, LockUILength): builder.PrependInt32Slot(1, LockUILength, 0)


    @staticmethod
    def AddHideWhenLocked(builder, HideWhenLocked): builder.PrependBoolSlot(2, HideWhenLocked, 0)


    @staticmethod
    def AddAccountLevel(builder, AccountLevel): builder.PrependInt32Slot(3, AccountLevel, 0)


    @staticmethod
    def AddScenarioModeIdLength(builder, ScenarioModeIdLength): builder.PrependInt32Slot(4, ScenarioModeIdLength, 0)


    @staticmethod
    def AddCampaignStageIDLength(builder, CampaignStageIDLength): builder.PrependInt32Slot(5, CampaignStageIDLength, 0)


    @staticmethod
    def AddMultipleConditionCheckType(builder, MultipleConditionCheckType): builder.PrependInt32Slot(6, MultipleConditionCheckType, 0)


    @staticmethod
    def AddAfterWhenDate(builder, AfterWhenDate): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(AfterWhenDate), 0)

    @staticmethod
    def AddWorldRaidBossKillLength(builder, WorldRaidBossKillLength): builder.PrependInt32Slot(8, WorldRaidBossKillLength, 0)

