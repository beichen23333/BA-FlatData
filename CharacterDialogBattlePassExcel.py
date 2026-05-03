
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterDialogBattlePassExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterDialogBattlePassExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def OriginalCharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BattlePassID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DialogCategory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DialogCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DialogConditionDetail(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DialogConditionDetailValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DialogType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DurationKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def AnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeTH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeTW(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeEN(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def VoiceIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    def VoiceIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def VoiceIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        return o == 0


    def CollectionVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CVCollectionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UnlockBattlePassId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LocalizeCVGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def TeenMode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(25)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCostumeUniqueId(builder, CostumeUniqueId): builder.PrependInt64Slot(0, CostumeUniqueId, 0)


    @staticmethod
    def AddOriginalCharacterId(builder, OriginalCharacterId): builder.PrependInt64Slot(1, OriginalCharacterId, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(2, DisplayOrder, 0)


    @staticmethod
    def AddBattlePassID(builder, BattlePassID): builder.PrependInt64Slot(3, BattlePassID, 0)


    @staticmethod
    def AddProductionStep(builder, ProductionStep): builder.PrependInt32Slot(4, ProductionStep, 0)


    @staticmethod
    def AddDialogCategory(builder, DialogCategory): builder.PrependInt32Slot(5, DialogCategory, 0)


    @staticmethod
    def AddDialogCondition(builder, DialogCondition): builder.PrependInt32Slot(6, DialogCondition, 0)


    @staticmethod
    def AddDialogConditionDetail(builder, DialogConditionDetail): builder.PrependInt32Slot(7, DialogConditionDetail, 0)


    @staticmethod
    def AddDialogConditionDetailValue(builder, DialogConditionDetailValue): builder.PrependInt64Slot(8, DialogConditionDetailValue, 0)


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(9, GroupId, 0)


    @staticmethod
    def AddDialogType(builder, DialogType): builder.PrependInt32Slot(10, DialogType, 0)


    @staticmethod
    def AddDuration(builder, Duration): builder.PrependInt64Slot(11, Duration, 0)


    @staticmethod
    def AddDurationKr(builder, DurationKr): builder.PrependInt64Slot(12, DurationKr, 0)


    @staticmethod
    def AddAnimationName(builder, AnimationName): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(AnimationName), 0)

    @staticmethod
    def AddLocalizeKR(builder, LocalizeKR): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeKR), 0)

    @staticmethod
    def AddLocalizeJP(builder, LocalizeJP): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeJP), 0)

    @staticmethod
    def AddLocalizeTH(builder, LocalizeTH): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTH), 0)

    @staticmethod
    def AddLocalizeTW(builder, LocalizeTW): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTW), 0)

    @staticmethod
    def AddLocalizeEN(builder, LocalizeEN): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeEN), 0)

    @staticmethod
    def AddVoiceId(builder, VoiceId): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceId), 0)
    @staticmethod
    def StartVoiceIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddCollectionVisible(builder, CollectionVisible): builder.PrependBoolSlot(20, CollectionVisible, 0)


    @staticmethod
    def AddCVCollectionType(builder, CVCollectionType): builder.PrependInt32Slot(21, CVCollectionType, 0)


    @staticmethod
    def AddUnlockBattlePassId(builder, UnlockBattlePassId): builder.PrependInt64Slot(22, UnlockBattlePassId, 0)


    @staticmethod
    def AddLocalizeCVGroup(builder, LocalizeCVGroup): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeCVGroup), 0)

    @staticmethod
    def AddTeenMode(builder, TeenMode): builder.PrependBoolSlot(24, TeenMode, 0)

