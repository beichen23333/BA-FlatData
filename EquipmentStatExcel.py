
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EquipmentStatExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EquipmentStatExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EquipmentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatLevelUpType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinStatLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxStatLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LevelUpInsertLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LevelUpFeedExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LevelUpFeedCostCurrency(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LevelUpFeedCostAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipmentCategory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LevelUpFeedAddExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefaultMaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TranscendenceMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DamageFactorGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEquipmentId(builder, EquipmentId): builder.PrependInt32Slot(0, EquipmentId, 0)


    @staticmethod
    def AddStatLevelUpType(builder, StatLevelUpType): builder.PrependInt32Slot(1, StatLevelUpType, 0)


    @staticmethod
    def AddStatTypeLength(builder, StatTypeLength): builder.PrependInt32Slot(2, StatTypeLength, 0)


    @staticmethod
    def AddMinStatLength(builder, MinStatLength): builder.PrependInt32Slot(3, MinStatLength, 0)


    @staticmethod
    def AddMaxStatLength(builder, MaxStatLength): builder.PrependInt32Slot(4, MaxStatLength, 0)


    @staticmethod
    def AddLevelUpInsertLimit(builder, LevelUpInsertLimit): builder.PrependInt32Slot(5, LevelUpInsertLimit, 0)


    @staticmethod
    def AddLevelUpFeedExp(builder, LevelUpFeedExp): builder.PrependInt32Slot(6, LevelUpFeedExp, 0)


    @staticmethod
    def AddLevelUpFeedCostCurrency(builder, LevelUpFeedCostCurrency): builder.PrependInt32Slot(7, LevelUpFeedCostCurrency, 0)


    @staticmethod
    def AddLevelUpFeedCostAmount(builder, LevelUpFeedCostAmount): builder.PrependInt32Slot(8, LevelUpFeedCostAmount, 0)


    @staticmethod
    def AddEquipmentCategory(builder, EquipmentCategory): builder.PrependInt32Slot(9, EquipmentCategory, 0)


    @staticmethod
    def AddLevelUpFeedAddExp(builder, LevelUpFeedAddExp): builder.PrependInt32Slot(10, LevelUpFeedAddExp, 0)


    @staticmethod
    def AddDefaultMaxLevel(builder, DefaultMaxLevel): builder.PrependInt32Slot(11, DefaultMaxLevel, 0)


    @staticmethod
    def AddTranscendenceMax(builder, TranscendenceMax): builder.PrependInt32Slot(12, TranscendenceMax, 0)


    @staticmethod
    def AddDamageFactorGroupId(builder, DamageFactorGroupId): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(DamageFactorGroupId), 0)
