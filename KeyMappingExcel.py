
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class KeyMappingExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = KeyMappingExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayGroupType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnableCustomMapping(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DisplayCustomMapping(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def LocalizeKeyMappingId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def TargetKeyCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ControllerCursorFocus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ControllerKeyCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IsDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsDisplayController(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsUsed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsUsedController(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsLongPress(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IgnorePosCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IconPositionX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IconPositionY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IconScaleX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IconScaleY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerIconPositionX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerIconPositionY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerIconScaleX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ControllerIconScaleY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def KeymappingIconBGName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(24)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Id), 0)

    @staticmethod
    def AddDisplayGroupType(builder, DisplayGroupType): builder.PrependInt32Slot(1, DisplayGroupType, 0)


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(GroupId), 0)

    @staticmethod
    def AddEnableCustomMapping(builder, EnableCustomMapping): builder.PrependBoolSlot(3, EnableCustomMapping, 0)


    @staticmethod
    def AddDisplayCustomMapping(builder, DisplayCustomMapping): builder.PrependBoolSlot(4, DisplayCustomMapping, 0)


    @staticmethod
    def AddLocalizeKeyMappingId(builder, LocalizeKeyMappingId): builder.PrependUint32Slot(5, LocalizeKeyMappingId, 0)


    @staticmethod
    def AddTargetKeyCode(builder, TargetKeyCode): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(TargetKeyCode), 0)

    @staticmethod
    def AddControllerCursorFocus(builder, ControllerCursorFocus): builder.PrependBoolSlot(7, ControllerCursorFocus, 0)


    @staticmethod
    def AddControllerKeyCode(builder, ControllerKeyCode): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ControllerKeyCode), 0)

    @staticmethod
    def AddIsDisplay(builder, IsDisplay): builder.PrependBoolSlot(9, IsDisplay, 0)


    @staticmethod
    def AddIsDisplayController(builder, IsDisplayController): builder.PrependBoolSlot(10, IsDisplayController, 0)


    @staticmethod
    def AddIsUsed(builder, IsUsed): builder.PrependBoolSlot(11, IsUsed, 0)


    @staticmethod
    def AddIsUsedController(builder, IsUsedController): builder.PrependBoolSlot(12, IsUsedController, 0)


    @staticmethod
    def AddIsLongPress(builder, IsLongPress): builder.PrependBoolSlot(13, IsLongPress, 0)


    @staticmethod
    def AddIgnorePosCheck(builder, IgnorePosCheck): builder.PrependBoolSlot(14, IgnorePosCheck, 0)


    @staticmethod
    def AddIconPositionX(builder, IconPositionX): builder.PrependFloat32Slot(15, IconPositionX, 0)


    @staticmethod
    def AddIconPositionY(builder, IconPositionY): builder.PrependFloat32Slot(16, IconPositionY, 0)


    @staticmethod
    def AddIconScaleX(builder, IconScaleX): builder.PrependFloat32Slot(17, IconScaleX, 0)


    @staticmethod
    def AddIconScaleY(builder, IconScaleY): builder.PrependFloat32Slot(18, IconScaleY, 0)


    @staticmethod
    def AddControllerIconPositionX(builder, ControllerIconPositionX): builder.PrependFloat32Slot(19, ControllerIconPositionX, 0)


    @staticmethod
    def AddControllerIconPositionY(builder, ControllerIconPositionY): builder.PrependFloat32Slot(20, ControllerIconPositionY, 0)


    @staticmethod
    def AddControllerIconScaleX(builder, ControllerIconScaleX): builder.PrependFloat32Slot(21, ControllerIconScaleX, 0)


    @staticmethod
    def AddControllerIconScaleY(builder, ControllerIconScaleY): builder.PrependFloat32Slot(22, ControllerIconScaleY, 0)


    @staticmethod
    def AddKeymappingIconBGName(builder, KeymappingIconBGName): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(KeymappingIconBGName), 0)
