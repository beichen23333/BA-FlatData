
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WorldRaidBossGroupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WorldRaidBossGroupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WorldRaidBossGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WorldBossName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldBossPopupPortrait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldBossPopupBG(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldBossParcelPortrait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldBossListParcel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WorldBossHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WorldBossHPUO(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UIHideBeforeSpawn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def HideAnotherBossKilled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def WorldBossClearRewardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnotherBossKilledLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonConstraintGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExclusiveOperatorBossSpawn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ExclusiveOperatorBossKill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ExclusiveOperatorScenarioBattle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ExclusiveOperatorBossDamaged(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BossGroupOpenCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddWorldRaidBossGroupId(builder, WorldRaidBossGroupId): builder.PrependInt32Slot(1, WorldRaidBossGroupId, 0)


    @staticmethod
    def AddWorldBossName(builder, WorldBossName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(WorldBossName), 0)

    @staticmethod
    def AddWorldBossPopupPortrait(builder, WorldBossPopupPortrait): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(WorldBossPopupPortrait), 0)

    @staticmethod
    def AddWorldBossPopupBG(builder, WorldBossPopupBG): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(WorldBossPopupBG), 0)

    @staticmethod
    def AddWorldBossParcelPortrait(builder, WorldBossParcelPortrait): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(WorldBossParcelPortrait), 0)

    @staticmethod
    def AddWorldBossListParcel(builder, WorldBossListParcel): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(WorldBossListParcel), 0)

    @staticmethod
    def AddWorldBossHP(builder, WorldBossHP): builder.PrependInt32Slot(7, WorldBossHP, 0)


    @staticmethod
    def AddWorldBossHPUO(builder, WorldBossHPUO): builder.PrependInt32Slot(8, WorldBossHPUO, 0)


    @staticmethod
    def AddUIHideBeforeSpawn(builder, UIHideBeforeSpawn): builder.PrependBoolSlot(9, UIHideBeforeSpawn, 0)


    @staticmethod
    def AddHideAnotherBossKilled(builder, HideAnotherBossKilled): builder.PrependBoolSlot(10, HideAnotherBossKilled, 0)


    @staticmethod
    def AddWorldBossClearRewardGroupId(builder, WorldBossClearRewardGroupId): builder.PrependInt32Slot(11, WorldBossClearRewardGroupId, 0)


    @staticmethod
    def AddAnotherBossKilledLength(builder, AnotherBossKilledLength): builder.PrependInt32Slot(12, AnotherBossKilledLength, 0)


    @staticmethod
    def AddEchelonConstraintGroupId(builder, EchelonConstraintGroupId): builder.PrependInt32Slot(13, EchelonConstraintGroupId, 0)


    @staticmethod
    def AddExclusiveOperatorBossSpawn(builder, ExclusiveOperatorBossSpawn): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(ExclusiveOperatorBossSpawn), 0)

    @staticmethod
    def AddExclusiveOperatorBossKill(builder, ExclusiveOperatorBossKill): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(ExclusiveOperatorBossKill), 0)

    @staticmethod
    def AddExclusiveOperatorScenarioBattle(builder, ExclusiveOperatorScenarioBattle): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(ExclusiveOperatorScenarioBattle), 0)

    @staticmethod
    def AddExclusiveOperatorBossDamaged(builder, ExclusiveOperatorBossDamaged): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(ExclusiveOperatorBossDamaged), 0)

    @staticmethod
    def AddBossGroupOpenCondition(builder, BossGroupOpenCondition): builder.PrependInt32Slot(18, BossGroupOpenCondition, 0)

