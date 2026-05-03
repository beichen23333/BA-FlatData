
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ScenarioBGName_GlobalExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScenarioBGName_GlobalExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def NameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def NameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def NameAsia(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def NameNa(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def NameGlobal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def NameTeen(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupName(builder, GroupName): builder.PrependUint32Slot(0, GroupName, 0)


    @staticmethod
    def AddNameKr(builder, NameKr): builder.PrependUint32Slot(1, NameKr, 0)


    @staticmethod
    def AddNameTw(builder, NameTw): builder.PrependUint32Slot(2, NameTw, 0)


    @staticmethod
    def AddNameAsia(builder, NameAsia): builder.PrependUint32Slot(3, NameAsia, 0)


    @staticmethod
    def AddNameNa(builder, NameNa): builder.PrependUint32Slot(4, NameNa, 0)


    @staticmethod
    def AddNameGlobal(builder, NameGlobal): builder.PrependUint32Slot(5, NameGlobal, 0)


    @staticmethod
    def AddNameTeen(builder, NameTeen): builder.PrependUint32Slot(6, NameTeen, 0)

