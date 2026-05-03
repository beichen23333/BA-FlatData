
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ShopRecruitExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ShopRecruitExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OneGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def TenGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GoodsDevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def GachaBannerPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def VideoIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def VideoIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def VideoIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0


    def LinkedRobbyBannerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def InfoCharacterId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def InfoCharacterIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def InfoCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def InfoCharacterIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0


    def SalePeriodVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SalePeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SalePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RecruitCoinId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def RecruitSellectionShopId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PurchaseCooltimeMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PurchaseCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PurchaseCountResetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsNewbie(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsSelectRecruit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DirectPayInvisibleTokenId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DirectPayAndroidShopCashId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DirectPayAppleShopCashId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def SelectAbleGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def MaxSelectCharacterNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DirectPayOneStoreShopCashId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ProbabilityUrlDev(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def ProbabilityUrlLive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(30)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddCategoryType(builder, CategoryType): builder.PrependInt32Slot(1, CategoryType, 0)


    @staticmethod
    def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(2, IsLegacy, 0)


    @staticmethod
    def AddOneGachaGoodsId(builder, OneGachaGoodsId): builder.PrependInt64Slot(3, OneGachaGoodsId, 0)


    @staticmethod
    def AddTenGachaGoodsId(builder, TenGachaGoodsId): builder.PrependInt64Slot(4, TenGachaGoodsId, 0)


    @staticmethod
    def AddGoodsDevName(builder, GoodsDevName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(GoodsDevName), 0)

    @staticmethod
    def AddDisplayTag(builder, DisplayTag): builder.PrependInt32Slot(6, DisplayTag, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt64Slot(7, DisplayOrder, 0)


    @staticmethod
    def AddGachaBannerPath(builder, GachaBannerPath): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(GachaBannerPath), 0)

    @staticmethod
    def AddVideoId(builder, VideoId): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(VideoId), 0)
    @staticmethod
    def StartVideoIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddLinkedRobbyBannerId(builder, LinkedRobbyBannerId): builder.PrependInt64Slot(10, LinkedRobbyBannerId, 0)


    @staticmethod
    def AddInfoCharacterId(builder, InfoCharacterId): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(InfoCharacterId), 0)
    @staticmethod
    def StartInfoCharacterIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddSalePeriodVisible(builder, SalePeriodVisible): builder.PrependBoolSlot(12, SalePeriodVisible, 0)


    @staticmethod
    def AddSalePeriodFrom(builder, SalePeriodFrom): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodFrom), 0)

    @staticmethod
    def AddSalePeriodTo(builder, SalePeriodTo): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodTo), 0)

    @staticmethod
    def AddRecruitCoinId(builder, RecruitCoinId): builder.PrependInt64Slot(15, RecruitCoinId, 0)


    @staticmethod
    def AddRecruitSellectionShopId(builder, RecruitSellectionShopId): builder.PrependInt64Slot(16, RecruitSellectionShopId, 0)


    @staticmethod
    def AddPurchaseCooltimeMin(builder, PurchaseCooltimeMin): builder.PrependInt64Slot(17, PurchaseCooltimeMin, 0)


    @staticmethod
    def AddPurchaseCountLimit(builder, PurchaseCountLimit): builder.PrependInt64Slot(18, PurchaseCountLimit, 0)


    @staticmethod
    def AddPurchaseCountResetType(builder, PurchaseCountResetType): builder.PrependInt32Slot(19, PurchaseCountResetType, 0)


    @staticmethod
    def AddIsNewbie(builder, IsNewbie): builder.PrependBoolSlot(20, IsNewbie, 0)


    @staticmethod
    def AddIsSelectRecruit(builder, IsSelectRecruit): builder.PrependBoolSlot(21, IsSelectRecruit, 0)


    @staticmethod
    def AddDirectPayInvisibleTokenId(builder, DirectPayInvisibleTokenId): builder.PrependInt64Slot(22, DirectPayInvisibleTokenId, 0)


    @staticmethod
    def AddDirectPayAndroidShopCashId(builder, DirectPayAndroidShopCashId): builder.PrependInt64Slot(23, DirectPayAndroidShopCashId, 0)


    @staticmethod
    def AddDirectPayAppleShopCashId(builder, DirectPayAppleShopCashId): builder.PrependInt64Slot(24, DirectPayAppleShopCashId, 0)


    @staticmethod
    def AddSelectAbleGachaGroupId(builder, SelectAbleGachaGroupId): builder.PrependInt64Slot(25, SelectAbleGachaGroupId, 0)


    @staticmethod
    def AddMaxSelectCharacterNum(builder, MaxSelectCharacterNum): builder.PrependInt64Slot(26, MaxSelectCharacterNum, 0)


    @staticmethod
    def AddDirectPayOneStoreShopCashId(builder, DirectPayOneStoreShopCashId): builder.PrependInt64Slot(27, DirectPayOneStoreShopCashId, 0)


    @staticmethod
    def AddProbabilityUrlDev(builder, ProbabilityUrlDev): builder.PrependUOffsetTRelativeSlot(28, flatbuffers.number_types.UOffsetTFlags.py_type(ProbabilityUrlDev), 0)

    @staticmethod
    def AddProbabilityUrlLive(builder, ProbabilityUrlLive): builder.PrependUOffsetTRelativeSlot(29, flatbuffers.number_types.UOffsetTFlags.py_type(ProbabilityUrlLive), 0)
