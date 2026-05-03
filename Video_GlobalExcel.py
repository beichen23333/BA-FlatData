
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Video_GlobalExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Video_GlobalExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def VideoId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def VideoPathKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoTeenPathKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoPathTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoTeenPathTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoPathTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoTeenPathTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoPathEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoTeenPathEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddVideoId(builder, VideoId): builder.PrependInt64Slot(0, VideoId, 0)


    @staticmethod
    def AddVideoPathKr(builder, VideoPathKr): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(VideoPathKr), 0)

    @staticmethod
    def AddVideoTeenPathKr(builder, VideoTeenPathKr): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(VideoTeenPathKr), 0)

    @staticmethod
    def AddVideoPathTh(builder, VideoPathTh): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(VideoPathTh), 0)

    @staticmethod
    def AddVideoTeenPathTh(builder, VideoTeenPathTh): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(VideoTeenPathTh), 0)

    @staticmethod
    def AddVideoPathTw(builder, VideoPathTw): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(VideoPathTw), 0)

    @staticmethod
    def AddVideoTeenPathTw(builder, VideoTeenPathTw): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(VideoTeenPathTw), 0)

    @staticmethod
    def AddVideoPathEn(builder, VideoPathEn): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(VideoPathEn), 0)

    @staticmethod
    def AddVideoTeenPathEn(builder, VideoTeenPathEn): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(VideoTeenPathEn), 0)
