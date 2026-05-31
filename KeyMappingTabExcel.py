
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class KeyMappingTabExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = KeyMappingTabExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LeftArrowKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RightArrowKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LeftIconPositionX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def LeftIconPositionY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def LeftIconScaleX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def LeftIconScaleY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RightIconPositionX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RightIconPositionY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RightIconScaleX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def RightIconScaleY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Id), 0)

    @staticmethod
    def AddLeftArrowKey(builder, LeftArrowKey): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(LeftArrowKey), 0)

    @staticmethod
    def AddRightArrowKey(builder, RightArrowKey): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(RightArrowKey), 0)

    @staticmethod
    def AddLeftIconPositionX(builder, LeftIconPositionX): builder.PrependFloat32Slot(3, LeftIconPositionX, 0)


    @staticmethod
    def AddLeftIconPositionY(builder, LeftIconPositionY): builder.PrependFloat32Slot(4, LeftIconPositionY, 0)


    @staticmethod
    def AddLeftIconScaleX(builder, LeftIconScaleX): builder.PrependFloat32Slot(5, LeftIconScaleX, 0)


    @staticmethod
    def AddLeftIconScaleY(builder, LeftIconScaleY): builder.PrependFloat32Slot(6, LeftIconScaleY, 0)


    @staticmethod
    def AddRightIconPositionX(builder, RightIconPositionX): builder.PrependFloat32Slot(7, RightIconPositionX, 0)


    @staticmethod
    def AddRightIconPositionY(builder, RightIconPositionY): builder.PrependFloat32Slot(8, RightIconPositionY, 0)


    @staticmethod
    def AddRightIconScaleX(builder, RightIconScaleX): builder.PrependFloat32Slot(9, RightIconScaleX, 0)


    @staticmethod
    def AddRightIconScaleY(builder, RightIconScaleY): builder.PrependFloat32Slot(10, RightIconScaleY, 0)

