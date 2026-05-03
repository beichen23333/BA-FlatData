
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentScenarioExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentScenarioExcel()
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


    def ReplayDisplayGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecollectionNumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsRecollection(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsMeetup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsOmnibus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScenarioConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionEventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ClearedScenarioGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecollectionSummaryLocalizeScenarioId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def RecollectionResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IsRecollectionHorizon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardAmountLength(self):
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
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(1, EventContentId, 0)


    @staticmethod
    def AddReplayDisplayGroup(builder, ReplayDisplayGroup): builder.PrependInt32Slot(2, ReplayDisplayGroup, 0)


    @staticmethod
    def AddOrder(builder, Order): builder.PrependInt32Slot(3, Order, 0)


    @staticmethod
    def AddRecollectionNumber(builder, RecollectionNumber): builder.PrependInt32Slot(4, RecollectionNumber, 0)


    @staticmethod
    def AddIsRecollection(builder, IsRecollection): builder.PrependBoolSlot(5, IsRecollection, 0)


    @staticmethod
    def AddIsMeetup(builder, IsMeetup): builder.PrependBoolSlot(6, IsMeetup, 0)


    @staticmethod
    def AddIsOmnibus(builder, IsOmnibus): builder.PrependBoolSlot(7, IsOmnibus, 0)


    @staticmethod
    def AddScenarioGroupIdLength(builder, ScenarioGroupIdLength): builder.PrependInt32Slot(8, ScenarioGroupIdLength, 0)


    @staticmethod
    def AddScenarioConditionType(builder, ScenarioConditionType): builder.PrependInt32Slot(9, ScenarioConditionType, 0)


    @staticmethod
    def AddConditionAmount(builder, ConditionAmount): builder.PrependInt32Slot(10, ConditionAmount, 0)


    @staticmethod
    def AddConditionEventContentId(builder, ConditionEventContentId): builder.PrependInt32Slot(11, ConditionEventContentId, 0)


    @staticmethod
    def AddClearedScenarioGroupId(builder, ClearedScenarioGroupId): builder.PrependInt32Slot(12, ClearedScenarioGroupId, 0)


    @staticmethod
    def AddRecollectionSummaryLocalizeScenarioId(builder, RecollectionSummaryLocalizeScenarioId): builder.PrependUint32Slot(13, RecollectionSummaryLocalizeScenarioId, 0)


    @staticmethod
    def AddRecollectionResource(builder, RecollectionResource): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(RecollectionResource), 0)

    @staticmethod
    def AddIsRecollectionHorizon(builder, IsRecollectionHorizon): builder.PrependBoolSlot(15, IsRecollectionHorizon, 0)


    @staticmethod
    def AddRewardParcelTypeLength(builder, RewardParcelTypeLength): builder.PrependInt32Slot(16, RewardParcelTypeLength, 0)


    @staticmethod
    def AddRewardIdLength(builder, RewardIdLength): builder.PrependInt32Slot(17, RewardIdLength, 0)


    @staticmethod
    def AddRewardAmountLength(builder, RewardAmountLength): builder.PrependInt32Slot(18, RewardAmountLength, 0)

