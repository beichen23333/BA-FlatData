
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SNSPostExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SNSPostExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SNSInfoId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MasterPostId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RepostSNSProfileId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SNSProfileId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PostTextLocalizeKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def PostImagePath(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    def PostImagePathLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def PostImagePathIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0


    def RepostMinNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RepostMaxNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FavorMinNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FavorMaxNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddSNSInfoId(builder, SNSInfoId): builder.PrependInt64Slot(1, SNSInfoId, 0)


    @staticmethod
    def AddMasterPostId(builder, MasterPostId): builder.PrependInt64Slot(2, MasterPostId, 0)


    @staticmethod
    def AddRepostSNSProfileId(builder, RepostSNSProfileId): builder.PrependInt64Slot(3, RepostSNSProfileId, 0)


    @staticmethod
    def AddSNSProfileId(builder, SNSProfileId): builder.PrependInt64Slot(4, SNSProfileId, 0)


    @staticmethod
    def AddPostTextLocalizeKey(builder, PostTextLocalizeKey): builder.PrependUint32Slot(5, PostTextLocalizeKey, 0)


    @staticmethod
    def AddPostImagePath(builder, PostImagePath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(PostImagePath), 0)
    @staticmethod
    def StartPostImagePathVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddRepostMinNum(builder, RepostMinNum): builder.PrependInt64Slot(7, RepostMinNum, 0)


    @staticmethod
    def AddRepostMaxNum(builder, RepostMaxNum): builder.PrependInt64Slot(8, RepostMaxNum, 0)


    @staticmethod
    def AddFavorMinNum(builder, FavorMinNum): builder.PrependInt64Slot(9, FavorMinNum, 0)


    @staticmethod
    def AddFavorMaxNum(builder, FavorMaxNum): builder.PrependInt64Slot(10, FavorMaxNum, 0)

