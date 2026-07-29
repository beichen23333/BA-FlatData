
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameRoadExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameRoadExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def NoneLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(1)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddNoneLength(builder, NoneLength): builder.PrependInt32Slot(0, NoneLength, 0)

