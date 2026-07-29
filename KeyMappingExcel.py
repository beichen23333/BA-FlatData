
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


    def TargetKeyCode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IsDisplay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsUsed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsLongPress(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IgnorePosCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IconPositionX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IconPositionY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IconScaleX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IconScaleY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Id), 0)

    @staticmethod
    def AddTargetKeyCode(builder, TargetKeyCode): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(TargetKeyCode), 0)

    @staticmethod
    def AddIsDisplay(builder, IsDisplay): builder.PrependBoolSlot(2, IsDisplay, 0)


    @staticmethod
    def AddIsUsed(builder, IsUsed): builder.PrependBoolSlot(3, IsUsed, 0)


    @staticmethod
    def AddIsLongPress(builder, IsLongPress): builder.PrependBoolSlot(4, IsLongPress, 0)


    @staticmethod
    def AddIgnorePosCheck(builder, IgnorePosCheck): builder.PrependBoolSlot(5, IgnorePosCheck, 0)


    @staticmethod
    def AddIconPositionX(builder, IconPositionX): builder.PrependFloat32Slot(6, IconPositionX, 0)


    @staticmethod
    def AddIconPositionY(builder, IconPositionY): builder.PrependFloat32Slot(7, IconPositionY, 0)


    @staticmethod
    def AddIconScaleX(builder, IconScaleX): builder.PrependFloat32Slot(8, IconScaleX, 0)


    @staticmethod
    def AddIconScaleY(builder, IconScaleY): builder.PrependFloat32Slot(9, IconScaleY, 0)

