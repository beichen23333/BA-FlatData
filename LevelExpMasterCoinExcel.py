
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LevelExpMasterCoinExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LevelExpMasterCoinExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MinLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Ratio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductMonthlyId1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusMasterCoinRatio1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusMasterCoinIconName1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProductMonthlyId2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusMasterCoinRatio2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusMasterCoinIconName2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PlusMasterCoinIconName3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddMinLevel(builder, MinLevel): builder.PrependInt32Slot(1, MinLevel, 0)


    @staticmethod
    def AddMaxLevel(builder, MaxLevel): builder.PrependInt32Slot(2, MaxLevel, 0)


    @staticmethod
    def AddRatio(builder, Ratio): builder.PrependInt32Slot(3, Ratio, 0)


    @staticmethod
    def AddProductMonthlyId1Length(builder, ProductMonthlyId1Length): builder.PrependInt32Slot(4, ProductMonthlyId1Length, 0)


    @staticmethod
    def AddPlusMasterCoinRatio1(builder, PlusMasterCoinRatio1): builder.PrependInt32Slot(5, PlusMasterCoinRatio1, 0)


    @staticmethod
    def AddPlusMasterCoinIconName1(builder, PlusMasterCoinIconName1): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(PlusMasterCoinIconName1), 0)

    @staticmethod
    def AddProductMonthlyId2Length(builder, ProductMonthlyId2Length): builder.PrependInt32Slot(7, ProductMonthlyId2Length, 0)


    @staticmethod
    def AddPlusMasterCoinRatio2(builder, PlusMasterCoinRatio2): builder.PrependInt32Slot(8, PlusMasterCoinRatio2, 0)


    @staticmethod
    def AddPlusMasterCoinIconName2(builder, PlusMasterCoinIconName2): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(PlusMasterCoinIconName2), 0)

    @staticmethod
    def AddPlusMasterCoinIconName3(builder, PlusMasterCoinIconName3): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(PlusMasterCoinIconName3), 0)
