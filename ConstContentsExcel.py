
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstContentsExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstContentsExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UseSearchFieldOptimize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SearchUpdateTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def LobbyDayTimeFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LobbyNightTimeFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUseSearchFieldOptimize(builder, UseSearchFieldOptimize): builder.PrependBoolSlot(0, UseSearchFieldOptimize, 0)


    @staticmethod
    def AddSearchUpdateTime(builder, SearchUpdateTime): builder.PrependFloat32Slot(1, SearchUpdateTime, 0)


    @staticmethod
    def AddLobbyDayTimeFrom(builder, LobbyDayTimeFrom): builder.PrependInt32Slot(2, LobbyDayTimeFrom, 0)


    @staticmethod
    def AddLobbyNightTimeFrom(builder, LobbyNightTimeFrom): builder.PrependInt32Slot(3, LobbyNightTimeFrom, 0)

