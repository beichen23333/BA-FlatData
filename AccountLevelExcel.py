
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AccountLevelExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AccountLevelExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Exp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NewbieExpRatio(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CloseInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def APAutoChargeMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NeedReportEvent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def PlusExpProductMonthlyId1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusExpRatio1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusExpIconName1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PlusExpProductMonthlyId2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusExpRatio2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PlusExpIconName2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PlusExpIconName3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddLevel(builder, Level): builder.PrependInt32Slot(1, Level, 0)


    @staticmethod
    def AddExp(builder, Exp): builder.PrependInt32Slot(2, Exp, 0)


    @staticmethod
    def AddNewbieExpRatio(builder, NewbieExpRatio): builder.PrependInt32Slot(3, NewbieExpRatio, 0)


    @staticmethod
    def AddCloseInterval(builder, CloseInterval): builder.PrependInt32Slot(4, CloseInterval, 0)


    @staticmethod
    def AddAPAutoChargeMax(builder, APAutoChargeMax): builder.PrependInt32Slot(5, APAutoChargeMax, 0)


    @staticmethod
    def AddNeedReportEvent(builder, NeedReportEvent): builder.PrependBoolSlot(6, NeedReportEvent, 0)


    @staticmethod
    def AddPlusExpProductMonthlyId1Length(builder, PlusExpProductMonthlyId1Length): builder.PrependInt32Slot(7, PlusExpProductMonthlyId1Length, 0)


    @staticmethod
    def AddPlusExpRatio1(builder, PlusExpRatio1): builder.PrependInt32Slot(8, PlusExpRatio1, 0)


    @staticmethod
    def AddPlusExpIconName1(builder, PlusExpIconName1): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(PlusExpIconName1), 0)

    @staticmethod
    def AddPlusExpProductMonthlyId2Length(builder, PlusExpProductMonthlyId2Length): builder.PrependInt32Slot(10, PlusExpProductMonthlyId2Length, 0)


    @staticmethod
    def AddPlusExpRatio2(builder, PlusExpRatio2): builder.PrependInt32Slot(11, PlusExpRatio2, 0)


    @staticmethod
    def AddPlusExpIconName2(builder, PlusExpIconName2): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(PlusExpIconName2), 0)

    @staticmethod
    def AddPlusExpIconName3(builder, PlusExpIconName3): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(PlusExpIconName3), 0)
