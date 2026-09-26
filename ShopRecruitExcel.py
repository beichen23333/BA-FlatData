
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
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CategoryType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IsLegacy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def OneGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def TenGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WishListOneGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WishListTenGachaGoodsId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GoodsDevName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def DisplayTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DisplayOrder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def GachaBannerPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def LinkedRobbyBannerId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def InfoCharacterIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SalePeriodVisible(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def SalePeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SalePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def RecruitCoinId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecruitSellectionShopId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecruitStackItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecruitMileageGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MileageCountFreeRecruit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def PurchaseCooltimeMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PurchaseCountLimit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PurchaseCountResetType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SalePeriodDayParameter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsOverrideSalePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsNewbie(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def IsSelectRecruit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def DirectPayInvisibleTokenId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DirectPayProductId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SelectAbleGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MaxSelectCharacterNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecruitStackId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HalfStackDisplayItemId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def HalfStackGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def FullStackGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WishListConfig(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WishListHalfStackGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def WishListFullStackGachaGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def RecruitSeason(self):
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
    def AddCategoryType(builder, CategoryType): builder.PrependFloat32Slot(1, CategoryType, 0)


    @staticmethod
    def AddIsLegacy(builder, IsLegacy): builder.PrependBoolSlot(2, IsLegacy, 0)


    @staticmethod
    def AddOneGachaGoodsId(builder, OneGachaGoodsId): builder.PrependInt32Slot(3, OneGachaGoodsId, 0)


    @staticmethod
    def AddTenGachaGoodsId(builder, TenGachaGoodsId): builder.PrependInt32Slot(4, TenGachaGoodsId, 0)


    @staticmethod
    def AddWishListOneGachaGoodsId(builder, WishListOneGachaGoodsId): builder.PrependInt32Slot(5, WishListOneGachaGoodsId, 0)


    @staticmethod
    def AddWishListTenGachaGoodsId(builder, WishListTenGachaGoodsId): builder.PrependInt32Slot(6, WishListTenGachaGoodsId, 0)


    @staticmethod
    def AddGoodsDevName(builder, GoodsDevName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(GoodsDevName), 0)

    @staticmethod
    def AddDisplayTag(builder, DisplayTag): builder.PrependInt32Slot(8, DisplayTag, 0)


    @staticmethod
    def AddDisplayOrder(builder, DisplayOrder): builder.PrependInt32Slot(9, DisplayOrder, 0)


    @staticmethod
    def AddGachaBannerPath(builder, GachaBannerPath): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(GachaBannerPath), 0)

    @staticmethod
    def AddVideoIdLength(builder, VideoIdLength): builder.PrependInt32Slot(11, VideoIdLength, 0)


    @staticmethod
    def AddLinkedRobbyBannerId(builder, LinkedRobbyBannerId): builder.PrependInt32Slot(12, LinkedRobbyBannerId, 0)


    @staticmethod
    def AddInfoCharacterIdLength(builder, InfoCharacterIdLength): builder.PrependInt32Slot(13, InfoCharacterIdLength, 0)


    @staticmethod
    def AddSalePeriodVisible(builder, SalePeriodVisible): builder.PrependBoolSlot(14, SalePeriodVisible, 0)


    @staticmethod
    def AddSalePeriodFrom(builder, SalePeriodFrom): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodFrom), 0)

    @staticmethod
    def AddSalePeriodTo(builder, SalePeriodTo): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodTo), 0)

    @staticmethod
    def AddRecruitCoinId(builder, RecruitCoinId): builder.PrependInt32Slot(17, RecruitCoinId, 0)


    @staticmethod
    def AddRecruitSellectionShopId(builder, RecruitSellectionShopId): builder.PrependInt32Slot(18, RecruitSellectionShopId, 0)


    @staticmethod
    def AddRecruitStackItemId(builder, RecruitStackItemId): builder.PrependInt32Slot(19, RecruitStackItemId, 0)


    @staticmethod
    def AddRecruitMileageGroupId(builder, RecruitMileageGroupId): builder.PrependInt32Slot(20, RecruitMileageGroupId, 0)


    @staticmethod
    def AddMileageCountFreeRecruit(builder, MileageCountFreeRecruit): builder.PrependBoolSlot(21, MileageCountFreeRecruit, 0)


    @staticmethod
    def AddPurchaseCooltimeMin(builder, PurchaseCooltimeMin): builder.PrependInt32Slot(22, PurchaseCooltimeMin, 0)


    @staticmethod
    def AddPurchaseCountLimit(builder, PurchaseCountLimit): builder.PrependInt32Slot(23, PurchaseCountLimit, 0)


    @staticmethod
    def AddPurchaseCountResetType(builder, PurchaseCountResetType): builder.PrependInt32Slot(24, PurchaseCountResetType, 0)


    @staticmethod
    def AddSalePeriodDayParameter(builder, SalePeriodDayParameter): builder.PrependInt32Slot(25, SalePeriodDayParameter, 0)


    @staticmethod
    def AddIsOverrideSalePeriodTo(builder, IsOverrideSalePeriodTo): builder.PrependBoolSlot(26, IsOverrideSalePeriodTo, 0)


    @staticmethod
    def AddIsNewbie(builder, IsNewbie): builder.PrependBoolSlot(27, IsNewbie, 0)


    @staticmethod
    def AddIsSelectRecruit(builder, IsSelectRecruit): builder.PrependBoolSlot(28, IsSelectRecruit, 0)


    @staticmethod
    def AddDirectPayInvisibleTokenId(builder, DirectPayInvisibleTokenId): builder.PrependInt32Slot(29, DirectPayInvisibleTokenId, 0)


    @staticmethod
    def AddDirectPayProductId(builder, DirectPayProductId): builder.PrependUOffsetTRelativeSlot(30, flatbuffers.number_types.UOffsetTFlags.py_type(DirectPayProductId), 0)

    @staticmethod
    def AddSelectAbleGachaGroupId(builder, SelectAbleGachaGroupId): builder.PrependInt32Slot(31, SelectAbleGachaGroupId, 0)


    @staticmethod
    def AddMaxSelectCharacterNum(builder, MaxSelectCharacterNum): builder.PrependInt32Slot(32, MaxSelectCharacterNum, 0)


    @staticmethod
    def AddRecruitStackId(builder, RecruitStackId): builder.PrependInt32Slot(33, RecruitStackId, 0)


    @staticmethod
    def AddHalfStackDisplayItemId(builder, HalfStackDisplayItemId): builder.PrependInt32Slot(34, HalfStackDisplayItemId, 0)


    @staticmethod
    def AddHalfStackGachaGroupId(builder, HalfStackGachaGroupId): builder.PrependInt32Slot(35, HalfStackGachaGroupId, 0)


    @staticmethod
    def AddFullStackGachaGroupId(builder, FullStackGachaGroupId): builder.PrependInt32Slot(36, FullStackGachaGroupId, 0)


    @staticmethod
    def AddWishListConfig(builder, WishListConfig): builder.PrependInt32Slot(37, WishListConfig, 0)


    @staticmethod
    def AddWishListHalfStackGachaGroupId(builder, WishListHalfStackGachaGroupId): builder.PrependInt32Slot(38, WishListHalfStackGachaGroupId, 0)


    @staticmethod
    def AddWishListFullStackGachaGroupId(builder, WishListFullStackGachaGroupId): builder.PrependInt32Slot(39, WishListFullStackGachaGroupId, 0)


    @staticmethod
    def AddRecruitSeason(builder, RecruitSeason): builder.PrependInt32Slot(40, RecruitSeason, 0)

