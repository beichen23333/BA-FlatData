
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstKeyMappingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstKeyMappingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def DragSensitivity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def PcInformationGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScrollWheelFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RemoveKeycodeWord(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TutorialDialogTouchKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddDragSensitivity(builder, DragSensitivity): builder.PrependFloat32Slot(0, DragSensitivity, 0)


    @staticmethod
    def AddPcInformationGroupID(builder, PcInformationGroupID): builder.PrependInt64Slot(1, PcInformationGroupID, 0)


    @staticmethod
    def AddScrollWheelFactor(builder, ScrollWheelFactor): builder.PrependFloat32Slot(2, ScrollWheelFactor, 0)


    @staticmethod
    def AddRemoveKeycodeWord(builder, RemoveKeycodeWord): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(RemoveKeycodeWord), 0)

    @staticmethod
    def AddTutorialDialogTouchKey(builder, TutorialDialogTouchKey): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(TutorialDialogTouchKey), 0)
