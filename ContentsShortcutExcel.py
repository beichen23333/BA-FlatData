
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ContentsShortcutExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContentsShortcutExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScenarioModeVolume(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScenarioModeChapter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShortcutOpenTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShortcutCloseTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ConditionContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapDifficulty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestStepIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShortcutContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShortcutUINameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Localize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(13)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt32Slot(0, UniqueId, 0)


    @staticmethod
    def AddContentType(builder, ContentType): builder.PrependInt32Slot(1, ContentType, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(2, EventContentId, 0)


    @staticmethod
    def AddScenarioModeVolume(builder, ScenarioModeVolume): builder.PrependInt32Slot(3, ScenarioModeVolume, 0)


    @staticmethod
    def AddScenarioModeChapter(builder, ScenarioModeChapter): builder.PrependInt32Slot(4, ScenarioModeChapter, 0)


    @staticmethod
    def AddShortcutOpenTime(builder, ShortcutOpenTime): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(ShortcutOpenTime), 0)

    @staticmethod
    def AddShortcutCloseTime(builder, ShortcutCloseTime): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(ShortcutCloseTime), 0)

    @staticmethod
    def AddConditionContentId(builder, ConditionContentId): builder.PrependInt32Slot(7, ConditionContentId, 0)


    @staticmethod
    def AddConquestMapDifficulty(builder, ConquestMapDifficulty): builder.PrependInt32Slot(8, ConquestMapDifficulty, 0)


    @staticmethod
    def AddConquestStepIndex(builder, ConquestStepIndex): builder.PrependInt32Slot(9, ConquestStepIndex, 0)


    @staticmethod
    def AddShortcutContentId(builder, ShortcutContentId): builder.PrependInt32Slot(10, ShortcutContentId, 0)


    @staticmethod
    def AddShortcutUINameLength(builder, ShortcutUINameLength): builder.PrependInt32Slot(11, ShortcutUINameLength, 0)


    @staticmethod
    def AddLocalize(builder, Localize): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(Localize), 0)
