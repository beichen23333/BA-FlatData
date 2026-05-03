
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopRecruitSettingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopRecruitSettingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RecruitChangeScenarioModeID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PriorityOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TogetherPercentage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnotherPercentage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TwistPercentage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecruitChangeIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SeriesForceEnter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(8)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddRecruitChangeScenarioModeID(builder, RecruitChangeScenarioModeID): builder.PrependInt64Slot(1, RecruitChangeScenarioModeID, 0)


    @staticmethod
    def AddPriorityOrder(builder, PriorityOrder): builder.PrependInt64Slot(2, PriorityOrder, 0)


    @staticmethod
    def AddTogetherPercentage(builder, TogetherPercentage): builder.PrependInt32Slot(3, TogetherPercentage, 0)


    @staticmethod
    def AddAnotherPercentage(builder, AnotherPercentage): builder.PrependInt32Slot(4, AnotherPercentage, 0)


    @staticmethod
    def AddTwistPercentage(builder, TwistPercentage): builder.PrependInt32Slot(5, TwistPercentage, 0)


    @staticmethod
    def AddRecruitChangeIcon(builder, RecruitChangeIcon): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RecruitChangeIcon), 0)

    @staticmethod
    def AddSeriesForceEnter(builder, SeriesForceEnter): builder.PrependInt32Slot(7, SeriesForceEnter, 0)

