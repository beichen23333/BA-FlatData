
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeSkillEffectExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeSkillEffectExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def IconSpriteName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillEffectNameKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillEffectNameJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillEffectDescriptionKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SkillEffectDescriptionJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SuffixTextKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SuffixTextJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SuffixLabel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SharedCharacterParcelsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TextFontSizeOverride(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(11)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddKey(builder, Key): builder.PrependUint32Slot(0, Key, 0)


    @staticmethod
    def AddIconSpriteName(builder, IconSpriteName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(IconSpriteName), 0)

    @staticmethod
    def AddSkillEffectNameKR(builder, SkillEffectNameKR): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(SkillEffectNameKR), 0)

    @staticmethod
    def AddSkillEffectNameJP(builder, SkillEffectNameJP): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(SkillEffectNameJP), 0)

    @staticmethod
    def AddSkillEffectDescriptionKR(builder, SkillEffectDescriptionKR): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(SkillEffectDescriptionKR), 0)

    @staticmethod
    def AddSkillEffectDescriptionJP(builder, SkillEffectDescriptionJP): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(SkillEffectDescriptionJP), 0)

    @staticmethod
    def AddSuffixTextKR(builder, SuffixTextKR): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(SuffixTextKR), 0)

    @staticmethod
    def AddSuffixTextJP(builder, SuffixTextJP): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(SuffixTextJP), 0)

    @staticmethod
    def AddSuffixLabel(builder, SuffixLabel): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(SuffixLabel), 0)

    @staticmethod
    def AddSharedCharacterParcelsLength(builder, SharedCharacterParcelsLength): builder.PrependInt32Slot(9, SharedCharacterParcelsLength, 0)


    @staticmethod
    def AddTextFontSizeOverride(builder, TextFontSizeOverride): builder.PrependFloat32Slot(10, TextFontSizeOverride, 0)

