
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Form:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Form()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def MoveEnd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            from .Type_0x00004F4F import Type_0x00004F4F
            obj = Type_0x00004F4F()
            obj.Init(self._tab.Bytes, o + self._tab.Pos)
            return obj
        return None


    def PublicSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from .Type_0x00004F4E import Type_0x00004F4E
            obj = Type_0x00004F4E()
            obj.Init(self._tab.Bytes, o + self._tab.Pos)
            return obj
        return None




    @staticmethod
    def Start(builder): builder.StartObject(2)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddMoveEnd(builder, MoveEnd): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(MoveEnd), 0)
    @staticmethod
    def StartMoveEndVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddPublicSkill(builder, PublicSkill): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(PublicSkill), 0)
    @staticmethod
    def StartPublicSkillVector(builder, numElems): return builder.StartVector(4, numElems, 4)

