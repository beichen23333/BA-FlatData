
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConquestGroupBonusExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConquestGroupBonusExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ConquestBonusId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SchoolLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecommandLocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def BonusParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusCharacterCount1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusPercentage1Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusCharacterCount2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusPercentage2Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusCharacterCount3Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BonusPercentage3Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddConquestBonusId(builder, ConquestBonusId): builder.PrependInt32Slot(0, ConquestBonusId, 0)


    @staticmethod
    def AddSchoolLength(builder, SchoolLength): builder.PrependInt32Slot(1, SchoolLength, 0)


    @staticmethod
    def AddRecommandLocalizeEtcId(builder, RecommandLocalizeEtcId): builder.PrependUint32Slot(2, RecommandLocalizeEtcId, 0)


    @staticmethod
    def AddBonusParcelTypeLength(builder, BonusParcelTypeLength): builder.PrependInt32Slot(3, BonusParcelTypeLength, 0)


    @staticmethod
    def AddBonusIdLength(builder, BonusIdLength): builder.PrependInt32Slot(4, BonusIdLength, 0)


    @staticmethod
    def AddBonusCharacterCount1Length(builder, BonusCharacterCount1Length): builder.PrependInt32Slot(5, BonusCharacterCount1Length, 0)


    @staticmethod
    def AddBonusPercentage1Length(builder, BonusPercentage1Length): builder.PrependInt32Slot(6, BonusPercentage1Length, 0)


    @staticmethod
    def AddBonusCharacterCount2Length(builder, BonusCharacterCount2Length): builder.PrependInt32Slot(7, BonusCharacterCount2Length, 0)


    @staticmethod
    def AddBonusPercentage2Length(builder, BonusPercentage2Length): builder.PrependInt32Slot(8, BonusPercentage2Length, 0)


    @staticmethod
    def AddBonusCharacterCount3Length(builder, BonusCharacterCount3Length): builder.PrependInt32Slot(9, BonusCharacterCount3Length, 0)


    @staticmethod
    def AddBonusPercentage3Length(builder, BonusPercentage3Length): builder.PrependInt32Slot(10, BonusPercentage3Length, 0)

