
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ApcSlotDefineExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ApcSlotDefineExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ApcSlotDefineId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotSquadType01Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotStartCooltime01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotCooltime01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotSquadType02Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotStartCooltime02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotCooltime02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotSquadType03Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotStartCooltime03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotCooltime03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotSquadType04Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotStartCooltime04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSlotCooltime04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ApcSynergyId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AddCostRule(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatType01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatAdd01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatMultiply01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatType02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatAdd02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatMultiply02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatType03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatAdd03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StatMultiply03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(25)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddApcSlotDefineId(builder, ApcSlotDefineId): builder.PrependInt32Slot(0, ApcSlotDefineId, 0)


    @staticmethod
    def AddApcSlotAmount(builder, ApcSlotAmount): builder.PrependInt32Slot(1, ApcSlotAmount, 0)


    @staticmethod
    def AddApcSlotSquadType01Length(builder, ApcSlotSquadType01Length): builder.PrependInt32Slot(2, ApcSlotSquadType01Length, 0)


    @staticmethod
    def AddApcSlotStartCooltime01(builder, ApcSlotStartCooltime01): builder.PrependInt32Slot(3, ApcSlotStartCooltime01, 0)


    @staticmethod
    def AddApcSlotCooltime01(builder, ApcSlotCooltime01): builder.PrependInt32Slot(4, ApcSlotCooltime01, 0)


    @staticmethod
    def AddApcSlotSquadType02Length(builder, ApcSlotSquadType02Length): builder.PrependInt32Slot(5, ApcSlotSquadType02Length, 0)


    @staticmethod
    def AddApcSlotStartCooltime02(builder, ApcSlotStartCooltime02): builder.PrependInt32Slot(6, ApcSlotStartCooltime02, 0)


    @staticmethod
    def AddApcSlotCooltime02(builder, ApcSlotCooltime02): builder.PrependInt32Slot(7, ApcSlotCooltime02, 0)


    @staticmethod
    def AddApcSlotSquadType03Length(builder, ApcSlotSquadType03Length): builder.PrependInt32Slot(8, ApcSlotSquadType03Length, 0)


    @staticmethod
    def AddApcSlotStartCooltime03(builder, ApcSlotStartCooltime03): builder.PrependInt32Slot(9, ApcSlotStartCooltime03, 0)


    @staticmethod
    def AddApcSlotCooltime03(builder, ApcSlotCooltime03): builder.PrependInt32Slot(10, ApcSlotCooltime03, 0)


    @staticmethod
    def AddApcSlotSquadType04Length(builder, ApcSlotSquadType04Length): builder.PrependInt32Slot(11, ApcSlotSquadType04Length, 0)


    @staticmethod
    def AddApcSlotStartCooltime04(builder, ApcSlotStartCooltime04): builder.PrependInt32Slot(12, ApcSlotStartCooltime04, 0)


    @staticmethod
    def AddApcSlotCooltime04(builder, ApcSlotCooltime04): builder.PrependInt32Slot(13, ApcSlotCooltime04, 0)


    @staticmethod
    def AddApcSynergyId(builder, ApcSynergyId): builder.PrependInt32Slot(14, ApcSynergyId, 0)


    @staticmethod
    def AddAddCostRule(builder, AddCostRule): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(AddCostRule), 0)

    @staticmethod
    def AddStatType01(builder, StatType01): builder.PrependInt32Slot(16, StatType01, 0)


    @staticmethod
    def AddStatAdd01(builder, StatAdd01): builder.PrependInt32Slot(17, StatAdd01, 0)


    @staticmethod
    def AddStatMultiply01(builder, StatMultiply01): builder.PrependInt32Slot(18, StatMultiply01, 0)


    @staticmethod
    def AddStatType02(builder, StatType02): builder.PrependInt32Slot(19, StatType02, 0)


    @staticmethod
    def AddStatAdd02(builder, StatAdd02): builder.PrependInt32Slot(20, StatAdd02, 0)


    @staticmethod
    def AddStatMultiply02(builder, StatMultiply02): builder.PrependInt32Slot(21, StatMultiply02, 0)


    @staticmethod
    def AddStatType03(builder, StatType03): builder.PrependInt32Slot(22, StatType03, 0)


    @staticmethod
    def AddStatAdd03(builder, StatAdd03): builder.PrependInt32Slot(23, StatAdd03, 0)


    @staticmethod
    def AddStatMultiply03(builder, StatMultiply03): builder.PrependInt32Slot(24, StatMultiply03, 0)

