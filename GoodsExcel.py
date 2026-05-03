
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GoodsExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GoodsExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ConsumeParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeGachaTicketType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeGachaTicketTypeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductIdAOS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductIdiOS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductIdHarmony(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeExtraStepLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConsumeExtraAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ParcelAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddType(builder, Type): builder.PrependInt32Slot(1, Type, 0)


    @staticmethod
    def AddRarity(builder, Rarity): builder.PrependInt32Slot(2, Rarity, 0)


    @staticmethod
    def AddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)

    @staticmethod
    def AddConsumeParcelTypeLength(builder, ConsumeParcelTypeLength): builder.PrependInt32Slot(4, ConsumeParcelTypeLength, 0)


    @staticmethod
    def AddConsumeParcelIdLength(builder, ConsumeParcelIdLength): builder.PrependInt32Slot(5, ConsumeParcelIdLength, 0)


    @staticmethod
    def AddConsumeParcelAmountLength(builder, ConsumeParcelAmountLength): builder.PrependInt32Slot(6, ConsumeParcelAmountLength, 0)


    @staticmethod
    def AddConsumeConditionLength(builder, ConsumeConditionLength): builder.PrependInt32Slot(7, ConsumeConditionLength, 0)


    @staticmethod
    def AddConsumeGachaTicketType(builder, ConsumeGachaTicketType): builder.PrependInt32Slot(8, ConsumeGachaTicketType, 0)


    @staticmethod
    def AddConsumeGachaTicketTypeAmount(builder, ConsumeGachaTicketTypeAmount): builder.PrependInt32Slot(9, ConsumeGachaTicketTypeAmount, 0)


    @staticmethod
    def AddProductIdAOS(builder, ProductIdAOS): builder.PrependInt32Slot(10, ProductIdAOS, 0)


    @staticmethod
    def AddProductIdiOS(builder, ProductIdiOS): builder.PrependInt32Slot(11, ProductIdiOS, 0)


    @staticmethod
    def AddProductIdHarmony(builder, ProductIdHarmony): builder.PrependInt32Slot(12, ProductIdHarmony, 0)


    @staticmethod
    def AddConsumeExtraStepLength(builder, ConsumeExtraStepLength): builder.PrependInt32Slot(13, ConsumeExtraStepLength, 0)


    @staticmethod
    def AddConsumeExtraAmountLength(builder, ConsumeExtraAmountLength): builder.PrependInt32Slot(14, ConsumeExtraAmountLength, 0)


    @staticmethod
    def AddState(builder, State): builder.PrependInt32Slot(15, State, 0)


    @staticmethod
    def AddParcelTypeLength(builder, ParcelTypeLength): builder.PrependInt32Slot(16, ParcelTypeLength, 0)


    @staticmethod
    def AddParcelIdLength(builder, ParcelIdLength): builder.PrependInt32Slot(17, ParcelIdLength, 0)


    @staticmethod
    def AddParcelAmountLength(builder, ParcelAmountLength): builder.PrependInt32Slot(18, ParcelAmountLength, 0)

