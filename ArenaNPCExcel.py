
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ArenaNPCExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArenaNPCExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Rank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCAccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCLevelDeviation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NPCStarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExceptionCharacterRaritiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExceptionMainCharacterIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExceptionSupportCharacterIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExceptionTSSIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt32Slot(0, UniqueId, 0)


    @staticmethod
    def AddRank(builder, Rank): builder.PrependInt32Slot(1, Rank, 0)


    @staticmethod
    def AddNPCAccountLevel(builder, NPCAccountLevel): builder.PrependInt32Slot(2, NPCAccountLevel, 0)


    @staticmethod
    def AddNPCLevel(builder, NPCLevel): builder.PrependInt32Slot(3, NPCLevel, 0)


    @staticmethod
    def AddNPCLevelDeviation(builder, NPCLevelDeviation): builder.PrependInt32Slot(4, NPCLevelDeviation, 0)


    @staticmethod
    def AddNPCStarGrade(builder, NPCStarGrade): builder.PrependInt32Slot(5, NPCStarGrade, 0)


    @staticmethod
    def AddExceptionCharacterRaritiesLength(builder, ExceptionCharacterRaritiesLength): builder.PrependInt32Slot(6, ExceptionCharacterRaritiesLength, 0)


    @staticmethod
    def AddExceptionMainCharacterIdsLength(builder, ExceptionMainCharacterIdsLength): builder.PrependInt32Slot(7, ExceptionMainCharacterIdsLength, 0)


    @staticmethod
    def AddExceptionSupportCharacterIdsLength(builder, ExceptionSupportCharacterIdsLength): builder.PrependInt32Slot(8, ExceptionSupportCharacterIdsLength, 0)


    @staticmethod
    def AddExceptionTSSIdsLength(builder, ExceptionTSSIdsLength): builder.PrependInt32Slot(9, ExceptionTSSIdsLength, 0)

