
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InteractiveWorldRaidArcadeMachineExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InteractiveWorldRaidArcadeMachineExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def EventContentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniGameTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniGameCostItemIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniGameCostItemAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniGameSoftLimitItemIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniGameSoftLimitItemAmountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MiniGameImageLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeTitleLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeDescLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(9)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddEventContentId(builder, EventContentId): builder.PrependInt32Slot(0, EventContentId, 0)


    @staticmethod
    def AddMiniGameTypeLength(builder, MiniGameTypeLength): builder.PrependInt32Slot(1, MiniGameTypeLength, 0)


    @staticmethod
    def AddMiniGameCostItemIdLength(builder, MiniGameCostItemIdLength): builder.PrependInt32Slot(2, MiniGameCostItemIdLength, 0)


    @staticmethod
    def AddMiniGameCostItemAmountLength(builder, MiniGameCostItemAmountLength): builder.PrependInt32Slot(3, MiniGameCostItemAmountLength, 0)


    @staticmethod
    def AddMiniGameSoftLimitItemIdLength(builder, MiniGameSoftLimitItemIdLength): builder.PrependInt32Slot(4, MiniGameSoftLimitItemIdLength, 0)


    @staticmethod
    def AddMiniGameSoftLimitItemAmountLength(builder, MiniGameSoftLimitItemAmountLength): builder.PrependInt32Slot(5, MiniGameSoftLimitItemAmountLength, 0)


    @staticmethod
    def AddMiniGameImageLength(builder, MiniGameImageLength): builder.PrependInt32Slot(6, MiniGameImageLength, 0)


    @staticmethod
    def AddLocalizeTitleLength(builder, LocalizeTitleLength): builder.PrependInt32Slot(7, LocalizeTitleLength, 0)


    @staticmethod
    def AddLocalizeDescLength(builder, LocalizeDescLength): builder.PrependInt32Slot(8, LocalizeDescLength, 0)

