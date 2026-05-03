
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TutorialExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TutorialExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def ID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompletionReportEventName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CompulsoryTutorial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DescriptionTutorial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def TutorialStageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UINameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TutorialParentNameLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(7)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddID(builder, ID): builder.PrependInt32Slot(0, ID, 0)


    @staticmethod
    def AddCompletionReportEventName(builder, CompletionReportEventName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(CompletionReportEventName), 0)

    @staticmethod
    def AddCompulsoryTutorial(builder, CompulsoryTutorial): builder.PrependBoolSlot(2, CompulsoryTutorial, 0)


    @staticmethod
    def AddDescriptionTutorial(builder, DescriptionTutorial): builder.PrependBoolSlot(3, DescriptionTutorial, 0)


    @staticmethod
    def AddTutorialStageId(builder, TutorialStageId): builder.PrependInt32Slot(4, TutorialStageId, 0)


    @staticmethod
    def AddUINameLength(builder, UINameLength): builder.PrependInt32Slot(5, UINameLength, 0)


    @staticmethod
    def AddTutorialParentNameLength(builder, TutorialParentNameLength): builder.PrependInt32Slot(6, TutorialParentNameLength, 0)

