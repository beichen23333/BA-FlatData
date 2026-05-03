
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BGM_GlobalExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BGM_GlobalExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupBGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BGMIdKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BGMIdJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BGMIdTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BGMIdTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BGMIdEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(6)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupBGMId(builder, GroupBGMId): builder.PrependInt64Slot(0, GroupBGMId, 0)


    @staticmethod
    def AddBGMIdKr(builder, BGMIdKr): builder.PrependInt64Slot(1, BGMIdKr, 0)


    @staticmethod
    def AddBGMIdJp(builder, BGMIdJp): builder.PrependInt64Slot(2, BGMIdJp, 0)


    @staticmethod
    def AddBGMIdTh(builder, BGMIdTh): builder.PrependInt64Slot(3, BGMIdTh, 0)


    @staticmethod
    def AddBGMIdTw(builder, BGMIdTw): builder.PrependInt64Slot(4, BGMIdTw, 0)


    @staticmethod
    def AddBGMIdEn(builder, BGMIdEn): builder.PrependInt64Slot(5, BGMIdEn, 0)

