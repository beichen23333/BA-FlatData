
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestUnexpectedEventExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestUnexpectedEventExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventConditionUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventConditionAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventOccurDailyLimitCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnitCountPerStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventPrefabLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnexpectedEventUnitIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(0, EventContentId, 0)


    @staticmethod
    def AddUnexpectedEventConditionType(builder, UnexpectedEventConditionType): builder.PrependInt32Slot(1, UnexpectedEventConditionType, 0)


    @staticmethod
    def AddUnexpectedEventConditionUniqueId(builder, UnexpectedEventConditionUniqueId): builder.PrependInt32Slot(2, UnexpectedEventConditionUniqueId, 0)


    @staticmethod
    def AddUnexpectedEventConditionAmount(builder, UnexpectedEventConditionAmount): builder.PrependInt32Slot(3, UnexpectedEventConditionAmount, 0)


    @staticmethod
    def AddUnexpectedEventOccurDailyLimitCount(builder, UnexpectedEventOccurDailyLimitCount): builder.PrependInt32Slot(4, UnexpectedEventOccurDailyLimitCount, 0)


    @staticmethod
    def AddUnitCountPerStep(builder, UnitCountPerStep): builder.PrependInt32Slot(5, UnitCountPerStep, 0)


    @staticmethod
    def AddUnexpectedEventPrefabLength(builder, UnexpectedEventPrefabLength): builder.PrependInt32Slot(6, UnexpectedEventPrefabLength, 0)


    @staticmethod
    def AddUnexpectedEventUnitIdLength(builder, UnexpectedEventUnitIdLength): builder.PrependInt32Slot(7, UnexpectedEventUnitIdLength, 0)

