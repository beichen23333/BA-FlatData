
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CafeRankExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CafeRankExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CafeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Rank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecipeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ComfortMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TagCountMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterVisitMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterVisitMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeVisitWeightBase(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeVisitWeightTagBonusStepLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeVisitWeightTagBonusLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCafeId(builder, CafeId): builder.PrependInt32Slot(0, CafeId, 0)


    @staticmethod
    def AddRank(builder, Rank): builder.PrependInt32Slot(1, Rank, 0)


    @staticmethod
    def AddRecipeId(builder, RecipeId): builder.PrependInt32Slot(2, RecipeId, 0)


    @staticmethod
    def AddComfortMax(builder, ComfortMax): builder.PrependInt32Slot(3, ComfortMax, 0)


    @staticmethod
    def AddTagCountMax(builder, TagCountMax): builder.PrependInt32Slot(4, TagCountMax, 0)


    @staticmethod
    def AddCharacterVisitMin(builder, CharacterVisitMin): builder.PrependInt32Slot(5, CharacterVisitMin, 0)


    @staticmethod
    def AddCharacterVisitMax(builder, CharacterVisitMax): builder.PrependInt32Slot(6, CharacterVisitMax, 0)


    @staticmethod
    def AddCafeVisitWeightBase(builder, CafeVisitWeightBase): builder.PrependInt32Slot(7, CafeVisitWeightBase, 0)


    @staticmethod
    def AddCafeVisitWeightTagBonusStepLength(builder, CafeVisitWeightTagBonusStepLength): builder.PrependInt32Slot(8, CafeVisitWeightTagBonusStepLength, 0)


    @staticmethod
    def AddCafeVisitWeightTagBonusLength(builder, CafeVisitWeightTagBonusLength): builder.PrependInt32Slot(9, CafeVisitWeightTagBonusLength, 0)

