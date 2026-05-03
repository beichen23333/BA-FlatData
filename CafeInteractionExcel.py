
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CafeInteractionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CafeInteractionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IgnoreIfUnobtained(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IgnoreIfUnobtainedStartDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IgnoreIfUnobtainedEndDate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BubbleTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BubbleDurationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorEmoticonRewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorEmoticonRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorEmoticonRewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeCharacterStateLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt32Slot(0, CharacterId, 0)


    @staticmethod
    def AddIgnoreIfUnobtained(builder, IgnoreIfUnobtained): builder.PrependBoolSlot(1, IgnoreIfUnobtained, 0)


    @staticmethod
    def AddIgnoreIfUnobtainedStartDate(builder, IgnoreIfUnobtainedStartDate): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(IgnoreIfUnobtainedStartDate), 0)

    @staticmethod
    def AddIgnoreIfUnobtainedEndDate(builder, IgnoreIfUnobtainedEndDate): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(IgnoreIfUnobtainedEndDate), 0)

    @staticmethod
    def AddBubbleTypeLength(builder, BubbleTypeLength): builder.PrependInt32Slot(4, BubbleTypeLength, 0)


    @staticmethod
    def AddBubbleDurationLength(builder, BubbleDurationLength): builder.PrependInt32Slot(5, BubbleDurationLength, 0)


    @staticmethod
    def AddFavorEmoticonRewardParcelType(builder, FavorEmoticonRewardParcelType): builder.PrependInt32Slot(6, FavorEmoticonRewardParcelType, 0)


    @staticmethod
    def AddFavorEmoticonRewardId(builder, FavorEmoticonRewardId): builder.PrependInt32Slot(7, FavorEmoticonRewardId, 0)


    @staticmethod
    def AddFavorEmoticonRewardAmount(builder, FavorEmoticonRewardAmount): builder.PrependInt32Slot(8, FavorEmoticonRewardAmount, 0)


    @staticmethod
    def AddCafeCharacterStateLength(builder, CafeCharacterStateLength): builder.PrependInt32Slot(9, CafeCharacterStateLength, 0)

