
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FieldSceneExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldSceneExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DateId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ArtLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignLevelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ConditionalBGMQuestIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BeginConditionalBGMScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BeginConditionalBGMInteractionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EndConditionalBGMScenarioGroupIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EndConditionalBGMInteractionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConditionalBGMIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(12)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt64Slot(0, UniqueId, 0)


    @staticmethod
    def AddDateId(builder, DateId): builder.PrependInt64Slot(1, DateId, 0)


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(2, GroupId, 0)


    @staticmethod
    def AddArtLevelPath(builder, ArtLevelPath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ArtLevelPath), 0)

    @staticmethod
    def AddDesignLevelPath(builder, DesignLevelPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(DesignLevelPath), 0)

    @staticmethod
    def AddBGMId(builder, BGMId): builder.PrependInt64Slot(5, BGMId, 0)


    @staticmethod
    def AddConditionalBGMQuestIdLength(builder, ConditionalBGMQuestIdLength): builder.PrependInt32Slot(6, ConditionalBGMQuestIdLength, 0)


    @staticmethod
    def AddBeginConditionalBGMScenarioGroupIdLength(builder, BeginConditionalBGMScenarioGroupIdLength): builder.PrependInt32Slot(7, BeginConditionalBGMScenarioGroupIdLength, 0)


    @staticmethod
    def AddBeginConditionalBGMInteractionIdLength(builder, BeginConditionalBGMInteractionIdLength): builder.PrependInt32Slot(8, BeginConditionalBGMInteractionIdLength, 0)


    @staticmethod
    def AddEndConditionalBGMScenarioGroupIdLength(builder, EndConditionalBGMScenarioGroupIdLength): builder.PrependInt32Slot(9, EndConditionalBGMScenarioGroupIdLength, 0)


    @staticmethod
    def AddEndConditionalBGMInteractionIdLength(builder, EndConditionalBGMInteractionIdLength): builder.PrependInt32Slot(10, EndConditionalBGMInteractionIdLength, 0)


    @staticmethod
    def AddConditionalBGMIdLength(builder, ConditionalBGMIdLength): builder.PrependInt32Slot(11, ConditionalBGMIdLength, 0)

