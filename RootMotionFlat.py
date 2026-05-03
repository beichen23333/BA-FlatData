
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RootMotionFlat:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RootMotionFlat()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def FormsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExSkillsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MoveLeft(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from .Type_0x00004F4E import Type_0x00004F4E
            obj = Type_0x00004F4E()
            obj.Init(self._tab.Bytes, o + self._tab.Pos)
            return obj
        return None


    def MoveRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from .Type_0x00004F4E import Type_0x00004F4E
            obj = Type_0x00004F4E()
            obj.Init(self._tab.Bytes, o + self._tab.Pos)
            return obj
        return None




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddFormsLength(builder, FormsLength): builder.PrependInt32Slot(0, FormsLength, 0)


    @staticmethod
    def AddExSkillsLength(builder, ExSkillsLength): builder.PrependInt32Slot(1, ExSkillsLength, 0)


    @staticmethod
    def AddMoveLeft(builder, MoveLeft): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(MoveLeft), 0)
    @staticmethod
    def StartMoveLeftVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddMoveRight(builder, MoveRight): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(MoveRight), 0)
    @staticmethod
    def StartMoveRightVector(builder, numElems): return builder.StartVector(4, numElems, 4)

