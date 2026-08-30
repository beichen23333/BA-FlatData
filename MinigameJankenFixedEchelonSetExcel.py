
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameJankenFixedEchelonSetExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameJankenFixedEchelonSetExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def FixedEchelonID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EchelonSceneSkip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CharacterID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EquipMentID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(4)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddFixedEchelonID(builder, FixedEchelonID): builder.PrependInt32Slot(0, FixedEchelonID, 0)


    @staticmethod
    def AddEchelonSceneSkip(builder, EchelonSceneSkip): builder.PrependBoolSlot(1, EchelonSceneSkip, 0)


    @staticmethod
    def AddCharacterID(builder, CharacterID): builder.PrependInt32Slot(2, CharacterID, 0)


    @staticmethod
    def AddEquipMentID(builder, EquipMentID): builder.PrependInt32Slot(3, EquipMentID, 0)

