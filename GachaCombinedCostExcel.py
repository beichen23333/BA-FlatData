
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GachaCombinedCostExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GachaCombinedCostExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Priority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConsumeGachaTicketType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeGachaTicketTypeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConsumeParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConsumeParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)


    @staticmethod
    def AddPriority(builder, Priority): builder.PrependInt64Slot(1, Priority, 0)


    @staticmethod
    def AddConsumeGachaTicketType(builder, ConsumeGachaTicketType): builder.PrependInt32Slot(2, ConsumeGachaTicketType, 0)


    @staticmethod
    def AddConsumeGachaTicketTypeAmount(builder, ConsumeGachaTicketTypeAmount): builder.PrependInt64Slot(3, ConsumeGachaTicketTypeAmount, 0)


    @staticmethod
    def AddConsumeParcelType(builder, ConsumeParcelType): builder.PrependInt32Slot(4, ConsumeParcelType, 0)


    @staticmethod
    def AddConsumeParcelId(builder, ConsumeParcelId): builder.PrependInt64Slot(5, ConsumeParcelId, 0)


    @staticmethod
    def AddConsumeParcelAmount(builder, ConsumeParcelAmount): builder.PrependInt64Slot(6, ConsumeParcelAmount, 0)

