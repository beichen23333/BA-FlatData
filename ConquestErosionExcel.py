
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestErosionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestErosionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ErosionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Phase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseAlarm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def StepIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseStartConditionTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseStartConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseBeforeExposeConditionTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PhaseBeforeExposeConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ErosionBattleConditionParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ErosionBattleConditionParcelUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ErosionBattleConditionParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestRewardId(self):
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
    def AddId(builder, Id): builder.PrependInt32Slot(1, Id, 0)


    @staticmethod
    def AddErosionType(builder, ErosionType): builder.PrependInt32Slot(2, ErosionType, 0)


    @staticmethod
    def AddPhase(builder, Phase): builder.PrependInt32Slot(3, Phase, 0)


    @staticmethod
    def AddPhaseAlarm(builder, PhaseAlarm): builder.PrependBoolSlot(4, PhaseAlarm, 0)


    @staticmethod
    def AddStepIndex(builder, StepIndex): builder.PrependInt32Slot(5, StepIndex, 0)


    @staticmethod
    def AddPhaseStartConditionTypeLength(builder, PhaseStartConditionTypeLength): builder.PrependInt32Slot(6, PhaseStartConditionTypeLength, 0)


    @staticmethod
    def AddPhaseStartConditionParameterLength(builder, PhaseStartConditionParameterLength): builder.PrependInt32Slot(7, PhaseStartConditionParameterLength, 0)


    @staticmethod
    def AddPhaseBeforeExposeConditionTypeLength(builder, PhaseBeforeExposeConditionTypeLength): builder.PrependInt32Slot(8, PhaseBeforeExposeConditionTypeLength, 0)


    @staticmethod
    def AddPhaseBeforeExposeConditionParameterLength(builder, PhaseBeforeExposeConditionParameterLength): builder.PrependInt32Slot(9, PhaseBeforeExposeConditionParameterLength, 0)


    @staticmethod
    def AddErosionBattleConditionParcelType(builder, ErosionBattleConditionParcelType): builder.PrependInt32Slot(10, ErosionBattleConditionParcelType, 0)


    @staticmethod
    def AddErosionBattleConditionParcelUniqueId(builder, ErosionBattleConditionParcelUniqueId): builder.PrependInt32Slot(11, ErosionBattleConditionParcelUniqueId, 0)


    @staticmethod
    def AddErosionBattleConditionParcelAmount(builder, ErosionBattleConditionParcelAmount): builder.PrependInt32Slot(12, ErosionBattleConditionParcelAmount, 0)


    @staticmethod
    def AddConquestRewardId(builder, ConquestRewardId): builder.PrependInt32Slot(13, ConquestRewardId, 0)

