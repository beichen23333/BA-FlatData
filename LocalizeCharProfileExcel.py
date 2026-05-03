
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LocalizeCharProfileExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LocalizeCharProfileExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def CharacterId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def StatusMessageKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatusMessageJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatusMessageTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatusMessageTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StatusMessageEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FullNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def FamilyNameRubyEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PersonalNameRubyEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SchoolYearEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterAgeEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BirthdayEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharHeightEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DesignerNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(124))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def IllustratorNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(126))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(128))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(130))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(132))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(134))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterVoiceEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(136))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def KRCharacterVoiceKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(138))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def KRCharacterVoiceTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(140))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def KRCharacterVoiceTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(142))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def KRCharacterVoiceEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(144))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(146))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(148))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(150))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(152))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def HobbyEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(154))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(156))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(158))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(160))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(162))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(164))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(166))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(168))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(170))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponNameEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(172))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def WeaponDescEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(174))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(176))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(178))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(180))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(182))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProfileIntroductionEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(184))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewKr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(186))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewJp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(188))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewTh(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(190))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewTw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(192))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CharacterSSRNewEn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(194))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(96)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddCharacterId(builder, CharacterId): builder.PrependInt64Slot(0, CharacterId, 0)


    @staticmethod
    def AddStatusMessageKr(builder, StatusMessageKr): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageKr), 0)

    @staticmethod
    def AddStatusMessageJp(builder, StatusMessageJp): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageJp), 0)

    @staticmethod
    def AddStatusMessageTh(builder, StatusMessageTh): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageTh), 0)

    @staticmethod
    def AddStatusMessageTw(builder, StatusMessageTw): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageTw), 0)

    @staticmethod
    def AddStatusMessageEn(builder, StatusMessageEn): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(StatusMessageEn), 0)

    @staticmethod
    def AddFullNameKr(builder, FullNameKr): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameKr), 0)

    @staticmethod
    def AddFullNameJp(builder, FullNameJp): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameJp), 0)

    @staticmethod
    def AddFullNameTh(builder, FullNameTh): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameTh), 0)

    @staticmethod
    def AddFullNameTw(builder, FullNameTw): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameTw), 0)

    @staticmethod
    def AddFullNameEn(builder, FullNameEn): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(FullNameEn), 0)

    @staticmethod
    def AddFamilyNameKr(builder, FamilyNameKr): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameKr), 0)

    @staticmethod
    def AddFamilyNameRubyKr(builder, FamilyNameRubyKr): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyKr), 0)

    @staticmethod
    def AddPersonalNameKr(builder, PersonalNameKr): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameKr), 0)

    @staticmethod
    def AddPersonalNameRubyKr(builder, PersonalNameRubyKr): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyKr), 0)

    @staticmethod
    def AddFamilyNameJp(builder, FamilyNameJp): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameJp), 0)

    @staticmethod
    def AddFamilyNameRubyJp(builder, FamilyNameRubyJp): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyJp), 0)

    @staticmethod
    def AddPersonalNameJp(builder, PersonalNameJp): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameJp), 0)

    @staticmethod
    def AddPersonalNameRubyJp(builder, PersonalNameRubyJp): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyJp), 0)

    @staticmethod
    def AddFamilyNameTh(builder, FamilyNameTh): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameTh), 0)

    @staticmethod
    def AddFamilyNameRubyTh(builder, FamilyNameRubyTh): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyTh), 0)

    @staticmethod
    def AddPersonalNameTh(builder, PersonalNameTh): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameTh), 0)

    @staticmethod
    def AddPersonalNameRubyTh(builder, PersonalNameRubyTh): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyTh), 0)

    @staticmethod
    def AddFamilyNameTw(builder, FamilyNameTw): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameTw), 0)

    @staticmethod
    def AddFamilyNameRubyTw(builder, FamilyNameRubyTw): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyTw), 0)

    @staticmethod
    def AddPersonalNameTw(builder, PersonalNameTw): builder.PrependUOffsetTRelativeSlot(25, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameTw), 0)

    @staticmethod
    def AddPersonalNameRubyTw(builder, PersonalNameRubyTw): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyTw), 0)

    @staticmethod
    def AddFamilyNameEn(builder, FamilyNameEn): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameEn), 0)

    @staticmethod
    def AddFamilyNameRubyEn(builder, FamilyNameRubyEn): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(FamilyNameRubyEn), 0)

    @staticmethod
    def AddPersonalNameEn(builder, PersonalNameEn): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameEn), 0)

    @staticmethod
    def AddPersonalNameRubyEn(builder, PersonalNameRubyEn): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(PersonalNameRubyEn), 0)

    @staticmethod
    def AddSchoolYearKr(builder, SchoolYearKr): builder.PrependUOffsetTRelativeSlot(31, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearKr), 0)

    @staticmethod
    def AddSchoolYearJp(builder, SchoolYearJp): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearJp), 0)

    @staticmethod
    def AddSchoolYearTh(builder, SchoolYearTh): builder.PrependUOffsetTRelativeSlot(33, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearTh), 0)

    @staticmethod
    def AddSchoolYearTw(builder, SchoolYearTw): builder.PrependUOffsetTRelativeSlot(34, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearTw), 0)

    @staticmethod
    def AddSchoolYearEn(builder, SchoolYearEn): builder.PrependUOffsetTRelativeSlot(35, flatbuffers.number_types.UOffsetTFlags.py_type(SchoolYearEn), 0)

    @staticmethod
    def AddCharacterAgeKr(builder, CharacterAgeKr): builder.PrependUOffsetTRelativeSlot(36, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeKr), 0)

    @staticmethod
    def AddCharacterAgeJp(builder, CharacterAgeJp): builder.PrependUOffsetTRelativeSlot(37, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeJp), 0)

    @staticmethod
    def AddCharacterAgeTh(builder, CharacterAgeTh): builder.PrependUOffsetTRelativeSlot(38, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeTh), 0)

    @staticmethod
    def AddCharacterAgeTw(builder, CharacterAgeTw): builder.PrependUOffsetTRelativeSlot(39, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeTw), 0)

    @staticmethod
    def AddCharacterAgeEn(builder, CharacterAgeEn): builder.PrependUOffsetTRelativeSlot(40, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterAgeEn), 0)

    @staticmethod
    def AddBirthDay(builder, BirthDay): builder.PrependUOffsetTRelativeSlot(41, flatbuffers.number_types.UOffsetTFlags.py_type(BirthDay), 0)

    @staticmethod
    def AddBirthdayKr(builder, BirthdayKr): builder.PrependUOffsetTRelativeSlot(42, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayKr), 0)

    @staticmethod
    def AddBirthdayJp(builder, BirthdayJp): builder.PrependUOffsetTRelativeSlot(43, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayJp), 0)

    @staticmethod
    def AddBirthdayTh(builder, BirthdayTh): builder.PrependUOffsetTRelativeSlot(44, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayTh), 0)

    @staticmethod
    def AddBirthdayTw(builder, BirthdayTw): builder.PrependUOffsetTRelativeSlot(45, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayTw), 0)

    @staticmethod
    def AddBirthdayEn(builder, BirthdayEn): builder.PrependUOffsetTRelativeSlot(46, flatbuffers.number_types.UOffsetTFlags.py_type(BirthdayEn), 0)

    @staticmethod
    def AddCharHeightKr(builder, CharHeightKr): builder.PrependUOffsetTRelativeSlot(47, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightKr), 0)

    @staticmethod
    def AddCharHeightJp(builder, CharHeightJp): builder.PrependUOffsetTRelativeSlot(48, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightJp), 0)

    @staticmethod
    def AddCharHeightTh(builder, CharHeightTh): builder.PrependUOffsetTRelativeSlot(49, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightTh), 0)

    @staticmethod
    def AddCharHeightTw(builder, CharHeightTw): builder.PrependUOffsetTRelativeSlot(50, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightTw), 0)

    @staticmethod
    def AddCharHeightEn(builder, CharHeightEn): builder.PrependUOffsetTRelativeSlot(51, flatbuffers.number_types.UOffsetTFlags.py_type(CharHeightEn), 0)

    @staticmethod
    def AddDesignerNameKr(builder, DesignerNameKr): builder.PrependUOffsetTRelativeSlot(52, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameKr), 0)

    @staticmethod
    def AddDesignerNameJp(builder, DesignerNameJp): builder.PrependUOffsetTRelativeSlot(53, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameJp), 0)

    @staticmethod
    def AddDesignerNameTh(builder, DesignerNameTh): builder.PrependUOffsetTRelativeSlot(54, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameTh), 0)

    @staticmethod
    def AddDesignerNameTw(builder, DesignerNameTw): builder.PrependUOffsetTRelativeSlot(55, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameTw), 0)

    @staticmethod
    def AddDesignerNameEn(builder, DesignerNameEn): builder.PrependUOffsetTRelativeSlot(56, flatbuffers.number_types.UOffsetTFlags.py_type(DesignerNameEn), 0)

    @staticmethod
    def AddIllustratorNameKr(builder, IllustratorNameKr): builder.PrependUOffsetTRelativeSlot(57, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameKr), 0)

    @staticmethod
    def AddIllustratorNameJp(builder, IllustratorNameJp): builder.PrependUOffsetTRelativeSlot(58, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameJp), 0)

    @staticmethod
    def AddIllustratorNameTh(builder, IllustratorNameTh): builder.PrependUOffsetTRelativeSlot(59, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameTh), 0)

    @staticmethod
    def AddIllustratorNameTw(builder, IllustratorNameTw): builder.PrependUOffsetTRelativeSlot(60, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameTw), 0)

    @staticmethod
    def AddIllustratorNameEn(builder, IllustratorNameEn): builder.PrependUOffsetTRelativeSlot(61, flatbuffers.number_types.UOffsetTFlags.py_type(IllustratorNameEn), 0)

    @staticmethod
    def AddCharacterVoiceKr(builder, CharacterVoiceKr): builder.PrependUOffsetTRelativeSlot(62, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceKr), 0)

    @staticmethod
    def AddCharacterVoiceJp(builder, CharacterVoiceJp): builder.PrependUOffsetTRelativeSlot(63, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceJp), 0)

    @staticmethod
    def AddCharacterVoiceTh(builder, CharacterVoiceTh): builder.PrependUOffsetTRelativeSlot(64, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceTh), 0)

    @staticmethod
    def AddCharacterVoiceTw(builder, CharacterVoiceTw): builder.PrependUOffsetTRelativeSlot(65, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceTw), 0)

    @staticmethod
    def AddCharacterVoiceEn(builder, CharacterVoiceEn): builder.PrependUOffsetTRelativeSlot(66, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterVoiceEn), 0)

    @staticmethod
    def AddKRCharacterVoiceKr(builder, KRCharacterVoiceKr): builder.PrependUOffsetTRelativeSlot(67, flatbuffers.number_types.UOffsetTFlags.py_type(KRCharacterVoiceKr), 0)

    @staticmethod
    def AddKRCharacterVoiceTh(builder, KRCharacterVoiceTh): builder.PrependUOffsetTRelativeSlot(68, flatbuffers.number_types.UOffsetTFlags.py_type(KRCharacterVoiceTh), 0)

    @staticmethod
    def AddKRCharacterVoiceTw(builder, KRCharacterVoiceTw): builder.PrependUOffsetTRelativeSlot(69, flatbuffers.number_types.UOffsetTFlags.py_type(KRCharacterVoiceTw), 0)

    @staticmethod
    def AddKRCharacterVoiceEn(builder, KRCharacterVoiceEn): builder.PrependUOffsetTRelativeSlot(70, flatbuffers.number_types.UOffsetTFlags.py_type(KRCharacterVoiceEn), 0)

    @staticmethod
    def AddHobbyKr(builder, HobbyKr): builder.PrependUOffsetTRelativeSlot(71, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyKr), 0)

    @staticmethod
    def AddHobbyJp(builder, HobbyJp): builder.PrependUOffsetTRelativeSlot(72, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyJp), 0)

    @staticmethod
    def AddHobbyTh(builder, HobbyTh): builder.PrependUOffsetTRelativeSlot(73, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyTh), 0)

    @staticmethod
    def AddHobbyTw(builder, HobbyTw): builder.PrependUOffsetTRelativeSlot(74, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyTw), 0)

    @staticmethod
    def AddHobbyEn(builder, HobbyEn): builder.PrependUOffsetTRelativeSlot(75, flatbuffers.number_types.UOffsetTFlags.py_type(HobbyEn), 0)

    @staticmethod
    def AddWeaponNameKr(builder, WeaponNameKr): builder.PrependUOffsetTRelativeSlot(76, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameKr), 0)

    @staticmethod
    def AddWeaponDescKr(builder, WeaponDescKr): builder.PrependUOffsetTRelativeSlot(77, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescKr), 0)

    @staticmethod
    def AddWeaponNameJp(builder, WeaponNameJp): builder.PrependUOffsetTRelativeSlot(78, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameJp), 0)

    @staticmethod
    def AddWeaponDescJp(builder, WeaponDescJp): builder.PrependUOffsetTRelativeSlot(79, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescJp), 0)

    @staticmethod
    def AddWeaponNameTh(builder, WeaponNameTh): builder.PrependUOffsetTRelativeSlot(80, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameTh), 0)

    @staticmethod
    def AddWeaponDescTh(builder, WeaponDescTh): builder.PrependUOffsetTRelativeSlot(81, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescTh), 0)

    @staticmethod
    def AddWeaponNameTw(builder, WeaponNameTw): builder.PrependUOffsetTRelativeSlot(82, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameTw), 0)

    @staticmethod
    def AddWeaponDescTw(builder, WeaponDescTw): builder.PrependUOffsetTRelativeSlot(83, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescTw), 0)

    @staticmethod
    def AddWeaponNameEn(builder, WeaponNameEn): builder.PrependUOffsetTRelativeSlot(84, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponNameEn), 0)

    @staticmethod
    def AddWeaponDescEn(builder, WeaponDescEn): builder.PrependUOffsetTRelativeSlot(85, flatbuffers.number_types.UOffsetTFlags.py_type(WeaponDescEn), 0)

    @staticmethod
    def AddProfileIntroductionKr(builder, ProfileIntroductionKr): builder.PrependUOffsetTRelativeSlot(86, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionKr), 0)

    @staticmethod
    def AddProfileIntroductionJp(builder, ProfileIntroductionJp): builder.PrependUOffsetTRelativeSlot(87, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionJp), 0)

    @staticmethod
    def AddProfileIntroductionTh(builder, ProfileIntroductionTh): builder.PrependUOffsetTRelativeSlot(88, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionTh), 0)

    @staticmethod
    def AddProfileIntroductionTw(builder, ProfileIntroductionTw): builder.PrependUOffsetTRelativeSlot(89, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionTw), 0)

    @staticmethod
    def AddProfileIntroductionEn(builder, ProfileIntroductionEn): builder.PrependUOffsetTRelativeSlot(90, flatbuffers.number_types.UOffsetTFlags.py_type(ProfileIntroductionEn), 0)

    @staticmethod
    def AddCharacterSSRNewKr(builder, CharacterSSRNewKr): builder.PrependUOffsetTRelativeSlot(91, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewKr), 0)

    @staticmethod
    def AddCharacterSSRNewJp(builder, CharacterSSRNewJp): builder.PrependUOffsetTRelativeSlot(92, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewJp), 0)

    @staticmethod
    def AddCharacterSSRNewTh(builder, CharacterSSRNewTh): builder.PrependUOffsetTRelativeSlot(93, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewTh), 0)

    @staticmethod
    def AddCharacterSSRNewTw(builder, CharacterSSRNewTw): builder.PrependUOffsetTRelativeSlot(94, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewTw), 0)

    @staticmethod
    def AddCharacterSSRNewEn(builder, CharacterSSRNewEn): builder.PrependUOffsetTRelativeSlot(95, flatbuffers.number_types.UOffsetTFlags.py_type(CharacterSSRNewEn), 0)
