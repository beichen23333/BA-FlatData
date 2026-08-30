
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameJankenVoiceExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameJankenVoiceExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CostumeUniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VoiceCondition(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def LocalizeJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VoiceId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt32Slot(1, CharacterId, 0)


    @staticmethod
    def AddCostumeUniqueId(builder, CostumeUniqueId): builder.PrependInt32Slot(2, CostumeUniqueId, 0)


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(3, EventContentId, 0)


    @staticmethod
    def AddVoiceCondition(builder, VoiceCondition): builder.PrependInt32Slot(4, VoiceCondition, 0)


    @staticmethod
    def AddAnimationName(builder, AnimationName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(AnimationName), 0)

    @staticmethod
    def AddDuration(builder, Duration): builder.PrependInt32Slot(6, Duration, 0)


    @staticmethod
    def AddLocalizeKR(builder, LocalizeKR): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeKR), 0)

    @staticmethod
    def AddLocalizeJP(builder, LocalizeJP): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeJP), 0)

    @staticmethod
    def AddVoiceId(builder, VoiceId): builder.PrependUint32Slot(9, VoiceId, 0)

