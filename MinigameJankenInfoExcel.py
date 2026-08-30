
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameJankenInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameJankenInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MultipleMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostParcelEquipUpgradeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostParcelEquipUpgradeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ChallengeMultipleUnlockScore(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NeedItemAmountT2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NeedItemAmountT3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NeedItemAmountT4(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NeedItemAmountT5(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipmentMaxTier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScoreMaxStack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(0, EventContentId, 0)


    @staticmethod
    def AddCostParcelType(builder, CostParcelType): builder.PrependInt32Slot(1, CostParcelType, 0)


    @staticmethod
    def AddCostParcelId(builder, CostParcelId): builder.PrependInt32Slot(2, CostParcelId, 0)


    @staticmethod
    def AddMultipleMax(builder, MultipleMax): builder.PrependInt32Slot(3, MultipleMax, 0)


    @staticmethod
    def AddCostParcelEquipUpgradeType(builder, CostParcelEquipUpgradeType): builder.PrependInt32Slot(4, CostParcelEquipUpgradeType, 0)


    @staticmethod
    def AddCostParcelEquipUpgradeId(builder, CostParcelEquipUpgradeId): builder.PrependInt32Slot(5, CostParcelEquipUpgradeId, 0)


    @staticmethod
    def AddChallengeMultipleUnlockScore(builder, ChallengeMultipleUnlockScore): builder.PrependInt32Slot(6, ChallengeMultipleUnlockScore, 0)


    @staticmethod
    def AddNeedItemAmountT2(builder, NeedItemAmountT2): builder.PrependInt32Slot(7, NeedItemAmountT2, 0)


    @staticmethod
    def AddNeedItemAmountT3(builder, NeedItemAmountT3): builder.PrependInt32Slot(8, NeedItemAmountT3, 0)


    @staticmethod
    def AddNeedItemAmountT4(builder, NeedItemAmountT4): builder.PrependInt32Slot(9, NeedItemAmountT4, 0)


    @staticmethod
    def AddNeedItemAmountT5(builder, NeedItemAmountT5): builder.PrependInt32Slot(10, NeedItemAmountT5, 0)


    @staticmethod
    def AddEquipmentMaxTier(builder, EquipmentMaxTier): builder.PrependInt32Slot(11, EquipmentMaxTier, 0)


    @staticmethod
    def AddBGMId(builder, BGMId): builder.PrependInt32Slot(12, BGMId, 0)


    @staticmethod
    def AddScoreMaxStack(builder, ScoreMaxStack): builder.PrependInt32Slot(13, ScoreMaxStack, 0)

