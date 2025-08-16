
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameCCGPerkExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameCCGPerkExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CCGId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CostParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RerollPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DiscardPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnvironmentLogicEffectId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def EnvironmentLogicEffectIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def EnvironmentLogicEffectIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def EnvironmentLogicEffectIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0


    def RequiredPerkId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def RequiredPerkIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def RequiredPerkIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def RequiredPerkIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


    def ShopOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShopIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShopLocalizeTitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ShopLocalizeDesc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddCCGId(builder, CCGId): builder.PrependInt64Slot(1, CCGId, 0)


    @staticmethod
    def AddCostParcelAmount(builder, CostParcelAmount): builder.PrependInt32Slot(2, CostParcelAmount, 0)


    @staticmethod
    def AddRerollPoint(builder, RerollPoint): builder.PrependInt32Slot(3, RerollPoint, 0)


    @staticmethod
    def AddDiscardPoint(builder, DiscardPoint): builder.PrependInt32Slot(4, DiscardPoint, 0)


    @staticmethod
    def AddEnvironmentLogicEffectId(builder, EnvironmentLogicEffectId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(EnvironmentLogicEffectId), 0)
    @staticmethod
    def StartEnvironmentLogicEffectIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddRequiredPerkId(builder, RequiredPerkId): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(RequiredPerkId), 0)
    @staticmethod
    def StartRequiredPerkIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddShopOrder(builder, ShopOrder): builder.PrependInt32Slot(7, ShopOrder, 0)


    @staticmethod
    def AddShopIcon(builder, ShopIcon): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ShopIcon), 0)

    @staticmethod
    def AddShopLocalizeTitle(builder, ShopLocalizeTitle): builder.PrependUint32Slot(9, ShopLocalizeTitle, 0)


    @staticmethod
    def AddShopLocalizeDesc(builder, ShopLocalizeDesc): builder.PrependUint32Slot(10, ShopLocalizeDesc, 0)

