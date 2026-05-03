
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentLocationRewardExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentLocationRewardExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Location(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ScheduleGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OrderInGroup(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProgressTexture(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def LocationRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FavorExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SecretStoneAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SecretStoneProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraFavorExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraFavorExpProb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraRewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraRewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraRewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExtraRewardProbLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsExtraRewardDisplayedLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RewardAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(21)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddLocation(builder, Location): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Location), 0)

    @staticmethod
    def AddScheduleGroupId(builder, ScheduleGroupId): builder.PrependInt32Slot(1, ScheduleGroupId, 0)


    @staticmethod
    def AddOrderInGroup(builder, OrderInGroup): builder.PrependInt32Slot(2, OrderInGroup, 0)


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(3, Id, 0)


    @staticmethod
    def AddProgressTexture(builder, ProgressTexture): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(ProgressTexture), 0)

    @staticmethod
    def AddVoiceIdLength(builder, VoiceIdLength): builder.PrependInt32Slot(5, VoiceIdLength, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(6, LocalizeEtcId, 0)


    @staticmethod
    def AddLocationRank(builder, LocationRank): builder.PrependInt32Slot(7, LocationRank, 0)


    @staticmethod
    def AddFavorExp(builder, FavorExp): builder.PrependInt32Slot(8, FavorExp, 0)


    @staticmethod
    def AddSecretStoneAmount(builder, SecretStoneAmount): builder.PrependInt32Slot(9, SecretStoneAmount, 0)


    @staticmethod
    def AddSecretStoneProb(builder, SecretStoneProb): builder.PrependInt32Slot(10, SecretStoneProb, 0)


    @staticmethod
    def AddExtraFavorExp(builder, ExtraFavorExp): builder.PrependInt32Slot(11, ExtraFavorExp, 0)


    @staticmethod
    def AddExtraFavorExpProb(builder, ExtraFavorExpProb): builder.PrependInt32Slot(12, ExtraFavorExpProb, 0)


    @staticmethod
    def AddExtraRewardParcelTypeLength(builder, ExtraRewardParcelTypeLength): builder.PrependInt32Slot(13, ExtraRewardParcelTypeLength, 0)


    @staticmethod
    def AddExtraRewardParcelIdLength(builder, ExtraRewardParcelIdLength): builder.PrependInt32Slot(14, ExtraRewardParcelIdLength, 0)


    @staticmethod
    def AddExtraRewardAmountLength(builder, ExtraRewardAmountLength): builder.PrependInt32Slot(15, ExtraRewardAmountLength, 0)


    @staticmethod
    def AddExtraRewardProbLength(builder, ExtraRewardProbLength): builder.PrependInt32Slot(16, ExtraRewardProbLength, 0)


    @staticmethod
    def AddIsExtraRewardDisplayedLength(builder, IsExtraRewardDisplayedLength): builder.PrependInt32Slot(17, IsExtraRewardDisplayedLength, 0)


    @staticmethod
    def AddRewardParcelTypeLength(builder, RewardParcelTypeLength): builder.PrependInt32Slot(18, RewardParcelTypeLength, 0)


    @staticmethod
    def AddRewardParcelIdLength(builder, RewardParcelIdLength): builder.PrependInt32Slot(19, RewardParcelIdLength, 0)


    @staticmethod
    def AddRewardAmountLength(builder, RewardAmountLength): builder.PrependInt32Slot(20, RewardAmountLength, 0)

