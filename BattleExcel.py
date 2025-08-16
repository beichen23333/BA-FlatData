
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BattleExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BattleExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def None_(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def None_AsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def None_Length(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def None_IsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0


    def Single(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Guided(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Blue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CoverEnter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Normal(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    def NormalAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    def NormalLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def NormalIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0


    def Crush(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Able(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AllySelf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LightArmor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Wood(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def All(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DISTANCE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CloseToObstacle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Students(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Sequence(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UseNextExSkill(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Student(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SearchAndMove(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Street(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def D(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MAIN(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Remain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Low(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Resist(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Ally(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Main(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TargetToCaster(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Duration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Preset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FinalDamage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SpecialTransStat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Talk(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(34)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddNone_(builder, None_): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(None_), 0)
    @staticmethod
    def StartNone_Vector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddSingle(builder, Single): builder.PrependInt32Slot(1, Single, 0)


    @staticmethod
    def AddGuided(builder, Guided): builder.PrependInt32Slot(2, Guided, 0)


    @staticmethod
    def AddBlue(builder, Blue): builder.PrependInt32Slot(3, Blue, 0)


    @staticmethod
    def AddCoverEnter(builder, CoverEnter): builder.PrependInt32Slot(4, CoverEnter, 0)


    @staticmethod
    def AddNormal(builder, Normal): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(Normal), 0)
    @staticmethod
    def StartNormalVector(builder, numElems): return builder.StartVector(4, numElems, 4)


    @staticmethod
    def AddCrush(builder, Crush): builder.PrependInt32Slot(6, Crush, 0)


    @staticmethod
    def AddAble(builder, Able): builder.PrependInt32Slot(7, Able, 0)


    @staticmethod
    def AddAllySelf(builder, AllySelf): builder.PrependInt32Slot(8, AllySelf, 0)


    @staticmethod
    def AddLightArmor(builder, LightArmor): builder.PrependInt32Slot(9, LightArmor, 0)


    @staticmethod
    def AddWood(builder, Wood): builder.PrependInt32Slot(10, Wood, 0)


    @staticmethod
    def AddAll(builder, All): builder.PrependInt32Slot(11, All, 0)


    @staticmethod
    def AddDISTANCE(builder, DISTANCE): builder.PrependInt32Slot(12, DISTANCE, 0)


    @staticmethod
    def AddCloseToObstacle(builder, CloseToObstacle): builder.PrependInt32Slot(13, CloseToObstacle, 0)


    @staticmethod
    def AddStudents(builder, Students): builder.PrependInt32Slot(14, Students, 0)


    @staticmethod
    def AddSequence(builder, Sequence): builder.PrependInt32Slot(15, Sequence, 0)


    @staticmethod
    def AddUseNextExSkill(builder, UseNextExSkill): builder.PrependInt32Slot(16, UseNextExSkill, 0)


    @staticmethod
    def AddStudent(builder, Student): builder.PrependInt32Slot(17, Student, 0)


    @staticmethod
    def AddSearchAndMove(builder, SearchAndMove): builder.PrependInt32Slot(18, SearchAndMove, 0)


    @staticmethod
    def AddPosition(builder, Position): builder.PrependInt32Slot(19, Position, 0)


    @staticmethod
    def AddStreet(builder, Street): builder.PrependInt32Slot(20, Street, 0)


    @staticmethod
    def AddD(builder, D): builder.PrependInt32Slot(21, D, 0)


    @staticmethod
    def AddMAIN(builder, MAIN): builder.PrependInt32Slot(22, MAIN, 0)


    @staticmethod
    def AddRemain(builder, Remain): builder.PrependInt32Slot(23, Remain, 0)


    @staticmethod
    def AddLow(builder, Low): builder.PrependInt32Slot(24, Low, 0)


    @staticmethod
    def AddResist(builder, Resist): builder.PrependInt32Slot(25, Resist, 0)


    @staticmethod
    def AddAlly(builder, Ally): builder.PrependInt32Slot(26, Ally, 0)


    @staticmethod
    def AddMain(builder, Main): builder.PrependInt32Slot(27, Main, 0)


    @staticmethod
    def AddTargetToCaster(builder, TargetToCaster): builder.PrependInt32Slot(28, TargetToCaster, 0)


    @staticmethod
    def AddDuration(builder, Duration): builder.PrependInt32Slot(29, Duration, 0)


    @staticmethod
    def AddPreset(builder, Preset): builder.PrependInt32Slot(30, Preset, 0)


    @staticmethod
    def AddFinalDamage(builder, FinalDamage): builder.PrependInt32Slot(31, FinalDamage, 0)


    @staticmethod
    def AddSpecialTransStat(builder, SpecialTransStat): builder.PrependInt32Slot(32, SpecialTransStat, 0)


    @staticmethod
    def AddTalk(builder, Talk): builder.PrependInt32Slot(33, Talk, 0)

