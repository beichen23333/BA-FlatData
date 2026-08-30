
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MinigameRoadPuzzleMapExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MinigameRoadPuzzleMapExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MapGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Map(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MapBG(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AvailableRailTileLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AvailableRailTileAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OriginalTileCountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TrainSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(10)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(0, EventContentId, 0)


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt32Slot(1, UniqueId, 0)


    @staticmethod
    def AddMapGroupId(builder, MapGroupId): builder.PrependInt32Slot(2, MapGroupId, 0)


    @staticmethod
    def AddMap(builder, Map): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(Map), 0)

    @staticmethod
    def AddMapBG(builder, MapBG): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(MapBG), 0)

    @staticmethod
    def AddBGMId(builder, BGMId): builder.PrependInt32Slot(5, BGMId, 0)


    @staticmethod
    def AddAvailableRailTileLength(builder, AvailableRailTileLength): builder.PrependInt32Slot(6, AvailableRailTileLength, 0)


    @staticmethod
    def AddAvailableRailTileAmountLength(builder, AvailableRailTileAmountLength): builder.PrependInt32Slot(7, AvailableRailTileAmountLength, 0)


    @staticmethod
    def AddOriginalTileCountLength(builder, OriginalTileCountLength): builder.PrependInt32Slot(8, OriginalTileCountLength, 0)


    @staticmethod
    def AddTrainSpeed(builder, TrainSpeed): builder.PrependFloat32Slot(9, TrainSpeed, 0)

