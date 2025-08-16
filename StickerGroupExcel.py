
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StickerGroupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StickerGroupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def Layout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def UniqueLayoutPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StickerGroupIconpath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PageCompleteSlot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PageCompleteRewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PageCompleteRewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PageCompleteRewardAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeTitle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def LocalizeDescription(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StickerGroupCoverpath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddLayout(builder, Layout): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Layout), 0)

    @staticmethod
    def AddUniqueLayoutPath(builder, UniqueLayoutPath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(UniqueLayoutPath), 0)

    @staticmethod
    def AddStickerGroupIconpath(builder, StickerGroupIconpath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(StickerGroupIconpath), 0)

    @staticmethod
    def AddPageCompleteSlot(builder, PageCompleteSlot): builder.PrependInt64Slot(4, PageCompleteSlot, 0)


    @staticmethod
    def AddPageCompleteRewardParcelType(builder, PageCompleteRewardParcelType): builder.PrependInt32Slot(5, PageCompleteRewardParcelType, 0)


    @staticmethod
    def AddPageCompleteRewardParcelId(builder, PageCompleteRewardParcelId): builder.PrependInt64Slot(6, PageCompleteRewardParcelId, 0)


    @staticmethod
    def AddPageCompleteRewardAmount(builder, PageCompleteRewardAmount): builder.PrependInt32Slot(7, PageCompleteRewardAmount, 0)


    @staticmethod
    def AddLocalizeTitle(builder, LocalizeTitle): builder.PrependUint32Slot(8, LocalizeTitle, 0)


    @staticmethod
    def AddLocalizeDescription(builder, LocalizeDescription): builder.PrependUint32Slot(9, LocalizeDescription, 0)


    @staticmethod
    def AddStickerGroupCoverpath(builder, StickerGroupCoverpath): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(StickerGroupCoverpath), 0)
