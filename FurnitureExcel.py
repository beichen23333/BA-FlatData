
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FurnitureExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FurnitureExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ProductionStep(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Rarity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Category(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SubCategory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def StarGradeInit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Tier(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Icon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SizeWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SizeHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def OtherSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ExpandWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def Enable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def ReverseRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def Prefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PrefabExpand(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubPrefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SubExpandPrefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def CornerPrefab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def StackableMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecipeCraftId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SetGroudpId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ComfortBonus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VisitOperationType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VisitBonusOperationType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftQualityTier0(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftQualityTier1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CraftQualityTier2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShiftingCraftQuality(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FurnitureFunctionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FurnitureFunctionParameterLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def VideoId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def EventCollectionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FurnitureBubbleOffsetX(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FurnitureBubbleOffsetY(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeCharacterStateReqLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeCharacterStateAddLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeCharacterStateMakeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CafeCharacterStateOnlyLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(41)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt32Slot(0, Id, 0)


    @staticmethod
    def AddProductionStep(builder, ProductionStep): builder.PrependInt32Slot(1, ProductionStep, 0)


    @staticmethod
    def AddRarity(builder, Rarity): builder.PrependInt32Slot(2, Rarity, 0)


    @staticmethod
    def AddCategory(builder, Category): builder.PrependInt32Slot(3, Category, 0)


    @staticmethod
    def AddSubCategory(builder, SubCategory): builder.PrependInt32Slot(4, SubCategory, 0)


    @staticmethod
    def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(5, LocalizeEtcId, 0)


    @staticmethod
    def AddStarGradeInit(builder, StarGradeInit): builder.PrependInt32Slot(6, StarGradeInit, 0)


    @staticmethod
    def AddTier(builder, Tier): builder.PrependInt32Slot(7, Tier, 0)


    @staticmethod
    def AddIcon(builder, Icon): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(Icon), 0)

    @staticmethod
    def AddSizeWidth(builder, SizeWidth): builder.PrependInt32Slot(9, SizeWidth, 0)


    @staticmethod
    def AddSizeHeight(builder, SizeHeight): builder.PrependInt32Slot(10, SizeHeight, 0)


    @staticmethod
    def AddOtherSize(builder, OtherSize): builder.PrependInt32Slot(11, OtherSize, 0)


    @staticmethod
    def AddExpandWidth(builder, ExpandWidth): builder.PrependInt32Slot(12, ExpandWidth, 0)


    @staticmethod
    def AddEnable(builder, Enable): builder.PrependBoolSlot(13, Enable, 0)


    @staticmethod
    def AddReverseRotation(builder, ReverseRotation): builder.PrependBoolSlot(14, ReverseRotation, 0)


    @staticmethod
    def AddPrefab(builder, Prefab): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(Prefab), 0)

    @staticmethod
    def AddPrefabExpand(builder, PrefabExpand): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabExpand), 0)

    @staticmethod
    def AddSubPrefab(builder, SubPrefab): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(SubPrefab), 0)

    @staticmethod
    def AddSubExpandPrefab(builder, SubExpandPrefab): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(SubExpandPrefab), 0)

    @staticmethod
    def AddCornerPrefab(builder, CornerPrefab): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(CornerPrefab), 0)

    @staticmethod
    def AddStackableMax(builder, StackableMax): builder.PrependInt32Slot(20, StackableMax, 0)


    @staticmethod
    def AddRecipeCraftId(builder, RecipeCraftId): builder.PrependInt32Slot(21, RecipeCraftId, 0)


    @staticmethod
    def AddSetGroudpId(builder, SetGroudpId): builder.PrependInt32Slot(22, SetGroudpId, 0)


    @staticmethod
    def AddComfortBonus(builder, ComfortBonus): builder.PrependInt32Slot(23, ComfortBonus, 0)


    @staticmethod
    def AddVisitOperationType(builder, VisitOperationType): builder.PrependInt32Slot(24, VisitOperationType, 0)


    @staticmethod
    def AddVisitBonusOperationType(builder, VisitBonusOperationType): builder.PrependInt32Slot(25, VisitBonusOperationType, 0)


    @staticmethod
    def AddTagsLength(builder, TagsLength): builder.PrependInt32Slot(26, TagsLength, 0)


    @staticmethod
    def AddCraftQualityTier0(builder, CraftQualityTier0): builder.PrependInt32Slot(27, CraftQualityTier0, 0)


    @staticmethod
    def AddCraftQualityTier1(builder, CraftQualityTier1): builder.PrependInt32Slot(28, CraftQualityTier1, 0)


    @staticmethod
    def AddCraftQualityTier2(builder, CraftQualityTier2): builder.PrependInt32Slot(29, CraftQualityTier2, 0)


    @staticmethod
    def AddShiftingCraftQuality(builder, ShiftingCraftQuality): builder.PrependInt32Slot(30, ShiftingCraftQuality, 0)


    @staticmethod
    def AddFurnitureFunctionType(builder, FurnitureFunctionType): builder.PrependInt32Slot(31, FurnitureFunctionType, 0)


    @staticmethod
    def AddFurnitureFunctionParameterLength(builder, FurnitureFunctionParameterLength): builder.PrependInt32Slot(32, FurnitureFunctionParameterLength, 0)


    @staticmethod
    def AddVideoId(builder, VideoId): builder.PrependInt32Slot(33, VideoId, 0)


    @staticmethod
    def AddEventCollectionId(builder, EventCollectionId): builder.PrependInt32Slot(34, EventCollectionId, 0)


    @staticmethod
    def AddFurnitureBubbleOffsetX(builder, FurnitureBubbleOffsetX): builder.PrependInt32Slot(35, FurnitureBubbleOffsetX, 0)


    @staticmethod
    def AddFurnitureBubbleOffsetY(builder, FurnitureBubbleOffsetY): builder.PrependInt32Slot(36, FurnitureBubbleOffsetY, 0)


    @staticmethod
    def AddCafeCharacterStateReqLength(builder, CafeCharacterStateReqLength): builder.PrependInt32Slot(37, CafeCharacterStateReqLength, 0)


    @staticmethod
    def AddCafeCharacterStateAddLength(builder, CafeCharacterStateAddLength): builder.PrependInt32Slot(38, CafeCharacterStateAddLength, 0)


    @staticmethod
    def AddCafeCharacterStateMakeLength(builder, CafeCharacterStateMakeLength): builder.PrependInt32Slot(39, CafeCharacterStateMakeLength, 0)


    @staticmethod
    def AddCafeCharacterStateOnlyLength(builder, CafeCharacterStateOnlyLength): builder.PrependInt32Slot(40, CafeCharacterStateOnlyLength, 0)

