
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BattlePassExpLimitExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BattlePassExpLimitExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def BattlePassId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LimitStartTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LimitEndTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ExpLimitAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddBattlePassId(builder, BattlePassId): builder.PrependInt64Slot(0, BattlePassId, 0)


    @staticmethod
    def AddLimitStartTime(builder, LimitStartTime): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(LimitStartTime), 0)

    @staticmethod
    def AddLimitEndTime(builder, LimitEndTime): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(LimitEndTime), 0)

    @staticmethod
    def AddExpLimitAmount(builder, ExpLimitAmount): builder.PrependInt64Slot(3, ExpLimitAmount, 0)

