
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameMissionExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameMissionExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GroupName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def ResetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
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


    def ViewFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PreMissionIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccountType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AccountLevel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShortcutUILength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsCompleteExtensionTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CompleteConditionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CompleteConditionParameterTagLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardIcon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MissionRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionRewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MissionRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(24)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(1, EventContentId, 0)


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt32Slot(2, GroupId, 0)


    @staticmethod
    def AddGroupName(builder, GroupName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(GroupName), 0)

    @staticmethod
    def AddCategory(builder, Category): builder.PrependInt32Slot(4, Category, 0)


    @staticmethod
    def AddDescription(builder, Description): builder.PrependUint32Slot(5, Description, 0)


    @staticmethod
    def AddResetType(builder, ResetType): builder.PrependInt32Slot(6, ResetType, 0)


    @staticmethod
    def AddToastDisplayType(builder, ToastDisplayType): builder.PrependInt32Slot(7, ToastDisplayType, 0)


    @staticmethod
    def AddToastImagePath(builder, ToastImagePath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(ToastImagePath), 0)

    @staticmethod
    def AddViewFlag(builder, ViewFlag): builder.PrependBoolSlot(9, ViewFlag, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(10, DisplayOrder, 0)


    @staticmethod
    def AddPreMissionIdLength(builder, PreMissionIdLength): builder.PrependInt32Slot(11, PreMissionIdLength, 0)


    @staticmethod
    def AddAccountType(builder, AccountType): builder.PrependInt32Slot(12, AccountType, 0)


    @staticmethod
    def AddAccountLevel(builder, AccountLevel): builder.PrependInt32Slot(13, AccountLevel, 0)


    @staticmethod
    def AddShortcutUILength(builder, ShortcutUILength): builder.PrependInt32Slot(14, ShortcutUILength, 0)


    @staticmethod
    def AddCompleteConditionType(builder, CompleteConditionType): builder.PrependInt32Slot(15, CompleteConditionType, 0)


    @staticmethod
    def AddIsCompleteExtensionTime(builder, IsCompleteExtensionTime): builder.PrependBoolSlot(16, IsCompleteExtensionTime, 0)


    @staticmethod
    def AddCompleteConditionCount(builder, CompleteConditionCount): builder.PrependInt32Slot(17, CompleteConditionCount, 0)


    @staticmethod
    def AddCompleteConditionParameterLength(builder, CompleteConditionParameterLength): builder.PrependInt32Slot(18, CompleteConditionParameterLength, 0)


    @staticmethod
    def AddCompleteConditionParameterTagLength(builder, CompleteConditionParameterTagLength): builder.PrependInt32Slot(19, CompleteConditionParameterTagLength, 0)


    @staticmethod
    def AddRewardIcon(builder, RewardIcon): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(RewardIcon), 0)

    @staticmethod
    def AddMissionRewardParcelTypeLength(builder, MissionRewardParcelTypeLength): builder.PrependInt32Slot(21, MissionRewardParcelTypeLength, 0)


    @staticmethod
    def AddMissionRewardParcelIdLength(builder, MissionRewardParcelIdLength): builder.PrependInt32Slot(22, MissionRewardParcelIdLength, 0)


    @staticmethod
    def AddMissionRewardAmountLength(builder, MissionRewardAmountLength): builder.PrependInt32Slot(23, MissionRewardAmountLength, 0)

