
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SNSInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SNSInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenScenarioModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CloseScenarioModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OpenTitleLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def CloseTitleLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def OpenDescLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def CloseDescLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddOpenScenarioModeId(builder, OpenScenarioModeId): builder.PrependInt64Slot(1, OpenScenarioModeId, 0)


    @staticmethod
    def AddCloseScenarioModeId(builder, CloseScenarioModeId): builder.PrependInt64Slot(2, CloseScenarioModeId, 0)


    @staticmethod
    def AddOpenTitleLocalizeKey(builder, OpenTitleLocalizeKey): builder.PrependUint32Slot(3, OpenTitleLocalizeKey, 0)


    @staticmethod
    def AddCloseTitleLocalizeKey(builder, CloseTitleLocalizeKey): builder.PrependUint32Slot(4, CloseTitleLocalizeKey, 0)


    @staticmethod
    def AddOpenDescLocalizeKey(builder, OpenDescLocalizeKey): builder.PrependUint32Slot(5, OpenDescLocalizeKey, 0)


    @staticmethod
    def AddCloseDescLocalizeKey(builder, CloseDescLocalizeKey): builder.PrependUint32Slot(6, CloseDescLocalizeKey, 0)

