
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstMinigameCCGExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstMinigameCCGExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def TurnDrawCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetRight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetTop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapBoundaryOffsetBottom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapCenterOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ConquestMapCenterOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def CameraZoomDefault(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ThemaLoadingProgressTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def MapAllyRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def AniAllyBattleAttack(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MaxHandCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StartCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TurnCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StrikerSwapFrontCost(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StrikerMaxEquipCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def StartDrawCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CampReviveHealthRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def BaseRewardRerollPoint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SelectRewardOptionCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AlternativeCardImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(24)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddTurnDrawCount(builder, TurnDrawCount): builder.PrependInt32Slot(0, TurnDrawCount, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetRight(builder, ConquestMapBoundaryOffsetRight): builder.PrependFloat32Slot(1, ConquestMapBoundaryOffsetRight, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetTop(builder, ConquestMapBoundaryOffsetTop): builder.PrependFloat32Slot(2, ConquestMapBoundaryOffsetTop, 0)


    @staticmethod
    def AddConquestMapBoundaryOffsetBottom(builder, ConquestMapBoundaryOffsetBottom): builder.PrependFloat32Slot(3, ConquestMapBoundaryOffsetBottom, 0)


    @staticmethod
    def AddConquestMapCenterOffsetX(builder, ConquestMapCenterOffsetX): builder.PrependFloat32Slot(4, ConquestMapCenterOffsetX, 0)


    @staticmethod
    def AddConquestMapCenterOffsetY(builder, ConquestMapCenterOffsetY): builder.PrependFloat32Slot(5, ConquestMapCenterOffsetY, 0)


    @staticmethod
    def AddCameraAngle(builder, CameraAngle): builder.PrependFloat32Slot(6, CameraAngle, 0)


    @staticmethod
    def AddCameraZoomMax(builder, CameraZoomMax): builder.PrependFloat32Slot(7, CameraZoomMax, 0)


    @staticmethod
    def AddCameraZoomMin(builder, CameraZoomMin): builder.PrependFloat32Slot(8, CameraZoomMin, 0)


    @staticmethod
    def AddCameraZoomDefault(builder, CameraZoomDefault): builder.PrependFloat32Slot(9, CameraZoomDefault, 0)


    @staticmethod
    def AddThemaLoadingProgressTime(builder, ThemaLoadingProgressTime): builder.PrependFloat32Slot(10, ThemaLoadingProgressTime, 0)


    @staticmethod
    def AddMapAllyRotation(builder, MapAllyRotation): builder.PrependFloat32Slot(11, MapAllyRotation, 0)


    @staticmethod
    def AddAniAllyBattleAttack(builder, AniAllyBattleAttack): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(AniAllyBattleAttack), 0)

    @staticmethod
    def AddMaxHandCount(builder, MaxHandCount): builder.PrependInt32Slot(13, MaxHandCount, 0)


    @staticmethod
    def AddMaxCost(builder, MaxCost): builder.PrependInt32Slot(14, MaxCost, 0)


    @staticmethod
    def AddStartCost(builder, StartCost): builder.PrependInt32Slot(15, StartCost, 0)


    @staticmethod
    def AddTurnCost(builder, TurnCost): builder.PrependInt32Slot(16, TurnCost, 0)


    @staticmethod
    def AddStrikerSwapFrontCost(builder, StrikerSwapFrontCost): builder.PrependInt32Slot(17, StrikerSwapFrontCost, 0)


    @staticmethod
    def AddStrikerMaxEquipCount(builder, StrikerMaxEquipCount): builder.PrependInt32Slot(18, StrikerMaxEquipCount, 0)


    @staticmethod
    def AddStartDrawCount(builder, StartDrawCount): builder.PrependInt32Slot(19, StartDrawCount, 0)


    @staticmethod
    def AddCampReviveHealthRate(builder, CampReviveHealthRate): builder.PrependInt32Slot(20, CampReviveHealthRate, 0)


    @staticmethod
    def AddBaseRewardRerollPoint(builder, BaseRewardRerollPoint): builder.PrependInt32Slot(21, BaseRewardRerollPoint, 0)


    @staticmethod
    def AddSelectRewardOptionCount(builder, SelectRewardOptionCount): builder.PrependInt32Slot(22, SelectRewardOptionCount, 0)


    @staticmethod
    def AddAlternativeCardImagePath(builder, AlternativeCardImagePath): builder.PrependUOffsetTRelativeSlot(23, flatbuffers.number_types.UOffsetTFlags.py_type(AlternativeCardImagePath), 0)
