
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ScenarioModeSpoilerPopupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ScenarioModeSpoilerPopupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ModeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VolumeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ChapterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SpoilerPopupTitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def SpoilerPopupDescription(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def PopupType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionScenarioModeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddModeType(builder, ModeType): builder.PrependInt32Slot(0, ModeType, 0)


    @staticmethod
    def AddVolumeId(builder, VolumeId): builder.PrependInt64Slot(1, VolumeId, 0)


    @staticmethod
    def AddChapterId(builder, ChapterId): builder.PrependInt64Slot(2, ChapterId, 0)


    @staticmethod
    def AddSpoilerPopupTitle(builder, SpoilerPopupTitle): builder.PrependUint32Slot(3, SpoilerPopupTitle, 0)


    @staticmethod
    def AddSpoilerPopupDescription(builder, SpoilerPopupDescription): builder.PrependUint32Slot(4, SpoilerPopupDescription, 0)


    @staticmethod
    def AddPopupType(builder, PopupType): builder.PrependInt32Slot(5, PopupType, 0)


    @staticmethod
    def AddConditionScenarioModeId(builder, ConditionScenarioModeId): builder.PrependInt64Slot(6, ConditionScenarioModeId, 0)

