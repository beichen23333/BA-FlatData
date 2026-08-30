
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FavorCollectionScoreBonusExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FavorCollectionScoreBonusExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScorePerOwnedStudent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScorePerFavorRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScoreForRank20(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScoreForRank50(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScoreForRank75(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ScoreForRank100(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RequiredScore01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId01(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId02(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId03(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId04(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId05(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId06(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore07(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId07(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore08(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId08(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore09(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId09(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore10(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId10(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore11(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId11(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore12(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId12(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore13(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId13(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore14(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId14(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore15(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId15(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore16(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId16(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore17(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId17(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore18(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId18(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore19(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId19(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RequiredScore20(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AppliedSkillGroupId20(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(47)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddScorePerOwnedStudent(builder, ScorePerOwnedStudent): builder.PrependInt32Slot(1, ScorePerOwnedStudent, 0)


    @staticmethod
    def AddScorePerFavorRank(builder, ScorePerFavorRank): builder.PrependInt32Slot(2, ScorePerFavorRank, 0)


    @staticmethod
    def AddScoreForRank20(builder, ScoreForRank20): builder.PrependInt32Slot(3, ScoreForRank20, 0)


    @staticmethod
    def AddScoreForRank50(builder, ScoreForRank50): builder.PrependInt32Slot(4, ScoreForRank50, 0)


    @staticmethod
    def AddScoreForRank75(builder, ScoreForRank75): builder.PrependInt32Slot(5, ScoreForRank75, 0)


    @staticmethod
    def AddScoreForRank100(builder, ScoreForRank100): builder.PrependInt32Slot(6, ScoreForRank100, 0)


    @staticmethod
    def AddRequiredScore01(builder, RequiredScore01): builder.PrependInt32Slot(7, RequiredScore01, 0)


    @staticmethod
    def AddAppliedSkillGroupId01(builder, AppliedSkillGroupId01): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId01), 0)

    @staticmethod
    def AddRequiredScore02(builder, RequiredScore02): builder.PrependInt32Slot(9, RequiredScore02, 0)


    @staticmethod
    def AddAppliedSkillGroupId02(builder, AppliedSkillGroupId02): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId02), 0)

    @staticmethod
    def AddRequiredScore03(builder, RequiredScore03): builder.PrependInt32Slot(11, RequiredScore03, 0)


    @staticmethod
    def AddAppliedSkillGroupId03(builder, AppliedSkillGroupId03): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId03), 0)

    @staticmethod
    def AddRequiredScore04(builder, RequiredScore04): builder.PrependInt32Slot(13, RequiredScore04, 0)


    @staticmethod
    def AddAppliedSkillGroupId04(builder, AppliedSkillGroupId04): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId04), 0)

    @staticmethod
    def AddRequiredScore05(builder, RequiredScore05): builder.PrependInt32Slot(15, RequiredScore05, 0)


    @staticmethod
    def AddAppliedSkillGroupId05(builder, AppliedSkillGroupId05): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId05), 0)

    @staticmethod
    def AddRequiredScore06(builder, RequiredScore06): builder.PrependInt32Slot(17, RequiredScore06, 0)


    @staticmethod
    def AddAppliedSkillGroupId06(builder, AppliedSkillGroupId06): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId06), 0)

    @staticmethod
    def AddRequiredScore07(builder, RequiredScore07): builder.PrependInt32Slot(19, RequiredScore07, 0)


    @staticmethod
    def AddAppliedSkillGroupId07(builder, AppliedSkillGroupId07): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId07), 0)

    @staticmethod
    def AddRequiredScore08(builder, RequiredScore08): builder.PrependInt32Slot(21, RequiredScore08, 0)


    @staticmethod
    def AddAppliedSkillGroupId08(builder, AppliedSkillGroupId08): builder.PrependUOffsetTRelativeSlot(22, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId08), 0)

    @staticmethod
    def AddRequiredScore09(builder, RequiredScore09): builder.PrependInt32Slot(23, RequiredScore09, 0)


    @staticmethod
    def AddAppliedSkillGroupId09(builder, AppliedSkillGroupId09): builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId09), 0)

    @staticmethod
    def AddRequiredScore10(builder, RequiredScore10): builder.PrependInt32Slot(25, RequiredScore10, 0)


    @staticmethod
    def AddAppliedSkillGroupId10(builder, AppliedSkillGroupId10): builder.PrependUOffsetTRelativeSlot(26, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId10), 0)

    @staticmethod
    def AddRequiredScore11(builder, RequiredScore11): builder.PrependInt32Slot(27, RequiredScore11, 0)


    @staticmethod
    def AddAppliedSkillGroupId11(builder, AppliedSkillGroupId11): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId11), 0)

    @staticmethod
    def AddRequiredScore12(builder, RequiredScore12): builder.PrependInt32Slot(29, RequiredScore12, 0)


    @staticmethod
    def AddAppliedSkillGroupId12(builder, AppliedSkillGroupId12): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId12), 0)

    @staticmethod
    def AddRequiredScore13(builder, RequiredScore13): builder.PrependInt32Slot(31, RequiredScore13, 0)


    @staticmethod
    def AddAppliedSkillGroupId13(builder, AppliedSkillGroupId13): builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId13), 0)

    @staticmethod
    def AddRequiredScore14(builder, RequiredScore14): builder.PrependInt32Slot(33, RequiredScore14, 0)


    @staticmethod
    def AddAppliedSkillGroupId14(builder, AppliedSkillGroupId14): builder.PrependUOffsetTRelativeSlot(34, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId14), 0)

    @staticmethod
    def AddRequiredScore15(builder, RequiredScore15): builder.PrependInt32Slot(35, RequiredScore15, 0)


    @staticmethod
    def AddAppliedSkillGroupId15(builder, AppliedSkillGroupId15): builder.PrependUOffsetTRelativeSlot(36, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId15), 0)

    @staticmethod
    def AddRequiredScore16(builder, RequiredScore16): builder.PrependInt32Slot(37, RequiredScore16, 0)


    @staticmethod
    def AddAppliedSkillGroupId16(builder, AppliedSkillGroupId16): builder.PrependUOffsetTRelativeSlot(38, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId16), 0)

    @staticmethod
    def AddRequiredScore17(builder, RequiredScore17): builder.PrependInt32Slot(39, RequiredScore17, 0)


    @staticmethod
    def AddAppliedSkillGroupId17(builder, AppliedSkillGroupId17): builder.PrependUOffsetTRelativeSlot(40, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId17), 0)

    @staticmethod
    def AddRequiredScore18(builder, RequiredScore18): builder.PrependInt32Slot(41, RequiredScore18, 0)


    @staticmethod
    def AddAppliedSkillGroupId18(builder, AppliedSkillGroupId18): builder.PrependUOffsetTRelativeSlot(42, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId18), 0)

    @staticmethod
    def AddRequiredScore19(builder, RequiredScore19): builder.PrependInt32Slot(43, RequiredScore19, 0)


    @staticmethod
    def AddAppliedSkillGroupId19(builder, AppliedSkillGroupId19): builder.PrependUOffsetTRelativeSlot(44, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId19), 0)

    @staticmethod
    def AddRequiredScore20(builder, RequiredScore20): builder.PrependInt32Slot(45, RequiredScore20, 0)


    @staticmethod
    def AddAppliedSkillGroupId20(builder, AppliedSkillGroupId20): builder.PrependUOffsetTRelativeSlot(46, flatbuffers.number_types.UOffsetTFlags.py_type(AppliedSkillGroupId20), 0)
