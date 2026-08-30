
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameJankenEquipmentExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameJankenEquipmentExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipmentGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def UnlockConditionStage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HitPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IconResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(1, EventContentId, 0)


    @staticmethod
    def AddEquipmentGroup(builder, EquipmentGroup): builder.PrependInt32Slot(2, EquipmentGroup, 0)


    @staticmethod
    def AddTier(builder, Tier): builder.PrependInt32Slot(3, Tier, 0)


    @staticmethod
    def AddLocalizeId(builder, LocalizeId): builder.PrependUint32Slot(4, LocalizeId, 0)


    @staticmethod
    def AddUnlockConditionStage(builder, UnlockConditionStage): builder.PrependInt32Slot(5, UnlockConditionStage, 0)


    @staticmethod
    def AddAttackPower(builder, AttackPower): builder.PrependInt32Slot(6, AttackPower, 0)


    @staticmethod
    def AddHitPoint(builder, HitPoint): builder.PrependInt32Slot(7, HitPoint, 0)


    @staticmethod
    def AddModelPrefabName(builder, ModelPrefabName): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ModelPrefabName), 0)

    @staticmethod
    def AddIconResourceName(builder, IconResourceName): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(IconResourceName), 0)
