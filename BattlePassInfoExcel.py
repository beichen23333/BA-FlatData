
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BattlePassInfoExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BattlePassInfoExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def FreeRewardGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PurchaseRewardGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NormalProductGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PremiumProductGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def DiscountPremiumProductGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def NextLvNeedExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def PassLvUpGoodsID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def BuyPremiumLvUpAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SalePeriodFrom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def SalePeriodTo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def VideoId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    def VideoIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    def VideoIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    def VideoIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0


    def FlavorTextGroupID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExclusiveRewardID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def ExclusiveEmblemID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0


    def PassExpLocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0


    def LobbyBannerPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MainIconParcelPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PurchaseStepProductImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)


    @staticmethod
    def AddFreeRewardGroupID(builder, FreeRewardGroupID): builder.PrependInt64Slot(1, FreeRewardGroupID, 0)


    @staticmethod
    def AddPurchaseRewardGroupID(builder, PurchaseRewardGroupID): builder.PrependInt64Slot(2, PurchaseRewardGroupID, 0)


    @staticmethod
    def AddNormalProductGroupID(builder, NormalProductGroupID): builder.PrependInt64Slot(3, NormalProductGroupID, 0)


    @staticmethod
    def AddPremiumProductGroupID(builder, PremiumProductGroupID): builder.PrependInt64Slot(4, PremiumProductGroupID, 0)


    @staticmethod
    def AddDiscountPremiumProductGroupID(builder, DiscountPremiumProductGroupID): builder.PrependInt64Slot(5, DiscountPremiumProductGroupID, 0)


    @staticmethod
    def AddNextLvNeedExp(builder, NextLvNeedExp): builder.PrependInt32Slot(6, NextLvNeedExp, 0)


    @staticmethod
    def AddPassLvUpGoodsID(builder, PassLvUpGoodsID): builder.PrependInt64Slot(7, PassLvUpGoodsID, 0)


    @staticmethod
    def AddBuyPremiumLvUpAmount(builder, BuyPremiumLvUpAmount): builder.PrependInt32Slot(8, BuyPremiumLvUpAmount, 0)


    @staticmethod
    def AddSalePeriodFrom(builder, SalePeriodFrom): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodFrom), 0)

    @staticmethod
    def AddSalePeriodTo(builder, SalePeriodTo): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(SalePeriodTo), 0)

    @staticmethod
    def AddVideoId(builder, VideoId): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(VideoId), 0)
    @staticmethod
    def StartVideoIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)


    @staticmethod
    def AddFlavorTextGroupID(builder, FlavorTextGroupID): builder.PrependInt64Slot(12, FlavorTextGroupID, 0)


    @staticmethod
    def AddExclusiveRewardID(builder, ExclusiveRewardID): builder.PrependInt64Slot(13, ExclusiveRewardID, 0)


    @staticmethod
    def AddExclusiveEmblemID(builder, ExclusiveEmblemID): builder.PrependInt64Slot(14, ExclusiveEmblemID, 0)


    @staticmethod
    def AddPassExpLocalizeEtcId(builder, PassExpLocalizeEtcId): builder.PrependUint32Slot(15, PassExpLocalizeEtcId, 0)


    @staticmethod
    def AddLobbyBannerPath(builder, LobbyBannerPath): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(LobbyBannerPath), 0)

    @staticmethod
    def AddMainIconParcelPath(builder, MainIconParcelPath): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(MainIconParcelPath), 0)

    @staticmethod
    def AddPurchaseStepProductImagePath(builder, PurchaseStepProductImagePath): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(PurchaseStepProductImagePath), 0)
