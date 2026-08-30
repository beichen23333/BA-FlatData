
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CampaignChapterExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CampaignChapterExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def NormalImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HardImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Order(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PreChapterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ChapterRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ChapterHardRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ChapterVeryHardRewardId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NormalCampaignStageIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def NormalExtraStageIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HardCampaignStageIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VeryHardCampaignStageIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsTacticSkip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(14)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)

    @staticmethod
    def AddNormalImagePath(builder, NormalImagePath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(NormalImagePath), 0)

    @staticmethod
    def AddHardImagePath(builder, HardImagePath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(HardImagePath), 0)

    @staticmethod
    def AddOrder(builder, Order): builder.PrependInt32Slot(4, Order, 0)


    @staticmethod
    def AddPreChapterIdLength(builder, PreChapterIdLength): builder.PrependInt32Slot(5, PreChapterIdLength, 0)


    @staticmethod
    def AddChapterRewardId(builder, ChapterRewardId): builder.PrependInt32Slot(6, ChapterRewardId, 0)


    @staticmethod
    def AddChapterHardRewardId(builder, ChapterHardRewardId): builder.PrependInt32Slot(7, ChapterHardRewardId, 0)


    @staticmethod
    def AddChapterVeryHardRewardId(builder, ChapterVeryHardRewardId): builder.PrependInt32Slot(8, ChapterVeryHardRewardId, 0)


    @staticmethod
    def AddNormalCampaignStageIdLength(builder, NormalCampaignStageIdLength): builder.PrependInt32Slot(9, NormalCampaignStageIdLength, 0)


    @staticmethod
    def AddNormalExtraStageIdLength(builder, NormalExtraStageIdLength): builder.PrependInt32Slot(10, NormalExtraStageIdLength, 0)


    @staticmethod
    def AddHardCampaignStageIdLength(builder, HardCampaignStageIdLength): builder.PrependInt32Slot(11, HardCampaignStageIdLength, 0)


    @staticmethod
    def AddVeryHardCampaignStageIdLength(builder, VeryHardCampaignStageIdLength): builder.PrependInt32Slot(12, VeryHardCampaignStageIdLength, 0)


    @staticmethod
    def AddIsTacticSkip(builder, IsTacticSkip): builder.PrependBoolSlot(13, IsTacticSkip, 0)

