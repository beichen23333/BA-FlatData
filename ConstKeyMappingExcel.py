
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


    def PcControllerInformationGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ScrollWheelFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RemoveKeycodeWord(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TutorialDialogTouchKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ControllerCursorFactorSlow(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ControllerCursorFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ControllerCursorFactorFast(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VibrationSec(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def VibrationPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerScrollWheelFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerZoomSensitivity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerDpadMoveCheckRangeX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerDpadMoveCheckRangeY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerCursorClickScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerScrollSensitivity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(17)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddDragSensitivity(builder, DragSensitivity): builder.PrependFloat32Slot(0, DragSensitivity, 0)


    @staticmethod
    def AddPcInformationGroupID(builder, PcInformationGroupID): builder.PrependInt64Slot(1, PcInformationGroupID, 0)


    @staticmethod
    def AddPcControllerInformationGroupID(builder, PcControllerInformationGroupID): builder.PrependInt64Slot(2, PcControllerInformationGroupID, 0)


    @staticmethod
    def AddScrollWheelFactor(builder, ScrollWheelFactor): builder.PrependFloat32Slot(3, ScrollWheelFactor, 0)


    @staticmethod
    def AddRemoveKeycodeWord(builder, RemoveKeycodeWord): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RemoveKeycodeWord), 0)

    @staticmethod
    def AddTutorialDialogTouchKey(builder, TutorialDialogTouchKey): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(TutorialDialogTouchKey), 0)

    @staticmethod
    def AddControllerCursorFactorSlow(builder, ControllerCursorFactorSlow): builder.PrependInt32Slot(6, ControllerCursorFactorSlow, 0)


    @staticmethod
    def AddControllerCursorFactor(builder, ControllerCursorFactor): builder.PrependInt32Slot(7, ControllerCursorFactor, 0)


    @staticmethod
    def AddControllerCursorFactorFast(builder, ControllerCursorFactorFast): builder.PrependInt32Slot(8, ControllerCursorFactorFast, 0)


    @staticmethod
    def AddVibrationSec(builder, VibrationSec): builder.PrependFloat32Slot(9, VibrationSec, 0)


    @staticmethod
    def AddVibrationPower(builder, VibrationPower): builder.PrependFloat32Slot(10, VibrationPower, 0)


    @staticmethod
    def AddControllerScrollWheelFactor(builder, ControllerScrollWheelFactor): builder.PrependFloat32Slot(11, ControllerScrollWheelFactor, 0)


    @staticmethod
    def AddControllerZoomSensitivity(builder, ControllerZoomSensitivity): builder.PrependFloat32Slot(12, ControllerZoomSensitivity, 0)


    @staticmethod
    def AddControllerDpadMoveCheckRangeX(builder, ControllerDpadMoveCheckRangeX): builder.PrependFloat32Slot(13, ControllerDpadMoveCheckRangeX, 0)


    @staticmethod
    def AddControllerDpadMoveCheckRangeY(builder, ControllerDpadMoveCheckRangeY): builder.PrependFloat32Slot(14, ControllerDpadMoveCheckRangeY, 0)


    @staticmethod
    def AddControllerCursorClickScale(builder, ControllerCursorClickScale): builder.PrependFloat32Slot(15, ControllerCursorClickScale, 0)


    @staticmethod
    def AddControllerScrollSensitivity(builder, ControllerScrollSensitivity): builder.PrependFloat32Slot(16, ControllerScrollSensitivity, 0)

