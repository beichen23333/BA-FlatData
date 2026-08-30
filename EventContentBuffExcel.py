
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentBuffExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentBuffExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentBuffId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsBuff(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CharacterTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnumType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnumTypeValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SkillGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SpriteName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BuffDescriptionLocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentBuffId(builder, EventContentBuffId): builder.PrependInt32Slot(0, EventContentBuffId, 0)


    @staticmethod
    def AddIsBuff(builder, IsBuff): builder.PrependBoolSlot(1, IsBuff, 0)


    @staticmethod
    def AddCharacterTag(builder, CharacterTag): builder.PrependInt32Slot(2, CharacterTag, 0)


    @staticmethod
    def AddEnumType(builder, EnumType): builder.PrependInt32Slot(3, EnumType, 0)


    @staticmethod
    def AddEnumTypeValueLength(builder, EnumTypeValueLength): builder.PrependInt32Slot(4, EnumTypeValueLength, 0)


    @staticmethod
    def AddSkillGroupId(builder, SkillGroupId): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(SkillGroupId), 0)

    @staticmethod
    def AddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)

    @staticmethod
    def AddSpriteName(builder, SpriteName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(SpriteName), 0)

    @staticmethod
    def AddBuffDescriptionLocalizeCodeId(builder, BuffDescriptionLocalizeCodeId): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(BuffDescriptionLocalizeCodeId), 0)
