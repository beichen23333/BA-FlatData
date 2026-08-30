
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WelcomeCampaignMissionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WelcomeCampaignMissionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def SeasonId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def Day(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PreMissionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ToastDisplayType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ToastImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ShortcutUILength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionDayBlock(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CompleteConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionParameterTagLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionParameterUIPrefabType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionRewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddSeasonId(builder, SeasonId): builder.PrependInt32Slot(0, SeasonId, 0)


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(1, Id, 0)


    @staticmethod
    def AddCategory(builder, Category): builder.PrependInt32Slot(2, Category, 0)


    @staticmethod
    def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(3, IsLegacy, 0)


    @staticmethod
    def AddDay(builder, Day): builder.PrependInt32Slot(4, Day, 0)


    @staticmethod
    def AddPreMissionIdLength(builder, PreMissionIdLength): builder.PrependInt32Slot(5, PreMissionIdLength, 0)


    @staticmethod
    def AddDescription(builder, Description): builder.PrependUint32Slot(6, Description, 0)


    @staticmethod
    def AddToastDisplayType(builder, ToastDisplayType): builder.PrependInt32Slot(7, ToastDisplayType, 0)


    @staticmethod
    def AddToastImagePath(builder, ToastImagePath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ToastImagePath), 0)

    @staticmethod
    def AddShortcutUILength(builder, ShortcutUILength): builder.PrependInt32Slot(9, ShortcutUILength, 0)


    @staticmethod
    def AddCompleteConditionDayBlock(builder, CompleteConditionDayBlock): builder.PrependBoolSlot(10, CompleteConditionDayBlock, 0)


    @staticmethod
    def AddCompleteConditionType(builder, CompleteConditionType): builder.PrependInt32Slot(11, CompleteConditionType, 0)


    @staticmethod
    def AddCompleteConditionCount(builder, CompleteConditionCount): builder.PrependInt32Slot(12, CompleteConditionCount, 0)


    @staticmethod
    def AddCompleteConditionParameterLength(builder, CompleteConditionParameterLength): builder.PrependInt32Slot(13, CompleteConditionParameterLength, 0)


    @staticmethod
    def AddCompleteConditionParameterTagLength(builder, CompleteConditionParameterTagLength): builder.PrependInt32Slot(14, CompleteConditionParameterTagLength, 0)


    @staticmethod
    def AddCompleteConditionParameterUIPrefabType(builder, CompleteConditionParameterUIPrefabType): builder.PrependInt32Slot(15, CompleteConditionParameterUIPrefabType, 0)


    @staticmethod
    def AddMissionRewardParcelTypeLength(builder, MissionRewardParcelTypeLength): builder.PrependInt32Slot(16, MissionRewardParcelTypeLength, 0)


    @staticmethod
    def AddMissionRewardParcelIdLength(builder, MissionRewardParcelIdLength): builder.PrependInt32Slot(17, MissionRewardParcelIdLength, 0)


    @staticmethod
    def AddMissionRewardAmountLength(builder, MissionRewardAmountLength): builder.PrependInt32Slot(18, MissionRewardAmountLength, 0)

