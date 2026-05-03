
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ScenarioScriptFunnelExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScenarioScriptFunnelExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Index(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FunnelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(3)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)


    @staticmethod
    def AddIndex(builder, Index): builder.PrependInt64Slot(1, Index, 0)


    @staticmethod
    def AddFunnelId(builder, FunnelId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(FunnelId), 0)
