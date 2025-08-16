
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameCCGEnemyGroupExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameCCGEnemyGroupExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def EnemyAI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def EnemyBGM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def LocalizeEnemyGroupName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEnemyGroupDesc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(5)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)


    @staticmethod
    def AddEnemyAI(builder, EnemyAI): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(EnemyAI), 0)

    @staticmethod
    def AddEnemyBGM(builder, EnemyBGM): builder.PrependInt64Slot(2, EnemyBGM, 0)


    @staticmethod
    def AddLocalizeEnemyGroupName(builder, LocalizeEnemyGroupName): builder.PrependUint32Slot(3, LocalizeEnemyGroupName, 0)


    @staticmethod
    def AddLocalizeEnemyGroupDesc(builder, LocalizeEnemyGroupDesc): builder.PrependUint32Slot(4, LocalizeEnemyGroupDesc, 0)

