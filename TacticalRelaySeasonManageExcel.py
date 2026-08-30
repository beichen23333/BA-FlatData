
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticalRelaySeasonManageExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticalRelaySeasonManageExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SeasonStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EndNoteLabelStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SeasonEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PrevSeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SeasonRankStillCounting(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt32Slot(0, SeasonId, 0)


    @staticmethod
    def AddSeasonName(builder, SeasonName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonName), 0)

    @staticmethod
    def AddSeasonStartDate(builder, SeasonStartDate): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonStartDate), 0)

    @staticmethod
    def AddEndNoteLabelStartDate(builder, EndNoteLabelStartDate): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(EndNoteLabelStartDate), 0)

    @staticmethod
    def AddSeasonEndDate(builder, SeasonEndDate): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(SeasonEndDate), 0)

    @staticmethod
    def AddPrevSeasonId(builder, PrevSeasonId): builder.PrependInt32Slot(5, PrevSeasonId, 0)


    @staticmethod
    def AddSeasonRankStillCounting(builder, SeasonRankStillCounting): builder.PrependInt32Slot(6, SeasonRankStillCounting, 0)

