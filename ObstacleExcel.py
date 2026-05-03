
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ObstacleExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ObstacleExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Index(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def JumpAble(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SubOffsetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def X(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def Z(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def Hp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxHp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BlockRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EvasionRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DestroyType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Point1OffesetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPoint1OssetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Point2OffesetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EnemyPoint2OssetLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SubObstacleIDLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(16)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddIndex(builder, Index): builder.PrependInt32Slot(0, Index, 0)


    @staticmethod
    def AddPrefabName(builder, PrefabName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabName), 0)

    @staticmethod
    def AddJumpAble(builder, JumpAble): builder.PrependBoolSlot(2, JumpAble, 0)


    @staticmethod
    def AddSubOffsetLength(builder, SubOffsetLength): builder.PrependInt32Slot(3, SubOffsetLength, 0)


    @staticmethod
    def AddX(builder, X): builder.PrependFloat32Slot(4, X, 0)


    @staticmethod
    def AddZ(builder, Z): builder.PrependFloat32Slot(5, Z, 0)


    @staticmethod
    def AddHp(builder, Hp): builder.PrependInt32Slot(6, Hp, 0)


    @staticmethod
    def AddMaxHp(builder, MaxHp): builder.PrependInt32Slot(7, MaxHp, 0)


    @staticmethod
    def AddBlockRate(builder, BlockRate): builder.PrependInt32Slot(8, BlockRate, 0)


    @staticmethod
    def AddEvasionRate(builder, EvasionRate): builder.PrependInt32Slot(9, EvasionRate, 0)


    @staticmethod
    def AddDestroyType(builder, DestroyType): builder.PrependInt32Slot(10, DestroyType, 0)


    @staticmethod
    def AddPoint1OffesetLength(builder, Point1OffesetLength): builder.PrependInt32Slot(11, Point1OffesetLength, 0)


    @staticmethod
    def AddEnemyPoint1OssetLength(builder, EnemyPoint1OssetLength): builder.PrependInt32Slot(12, EnemyPoint1OssetLength, 0)


    @staticmethod
    def AddPoint2OffesetLength(builder, Point2OffesetLength): builder.PrependInt32Slot(13, Point2OffesetLength, 0)


    @staticmethod
    def AddEnemyPoint2OssetLength(builder, EnemyPoint2OssetLength): builder.PrependInt32Slot(14, EnemyPoint2OssetLength, 0)


    @staticmethod
    def AddSubObstacleIDLength(builder, SubObstacleIDLength): builder.PrependInt32Slot(15, SubObstacleIDLength, 0)

