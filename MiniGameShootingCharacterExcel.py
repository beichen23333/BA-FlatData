
import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MiniGameShootingCharacterExcel:
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MiniGameShootingCharacterExcel()
        x.Init(buf, n + offset)
        return x

    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


    def UniqueId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def SpineResourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def BodyRadius(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def ModelPrefabName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def NormalAttackSkillData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def PublicSkillDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DeathSkillData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


    def MaxHP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackPower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def DefensePower(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CriticalRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def CriticalDamageRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def AttackRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def MoveSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def ShotTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0


    def IsBoss(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def Scale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0


    def IgnoreObstacleCheck(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0


    def CharacterVoiceGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0




    @staticmethod
    def Start(builder): builder.StartObject(19)
    @staticmethod
    def End(builder): return builder.EndObject()


    @staticmethod
    def AddUniqueId(builder, UniqueId): builder.PrependInt32Slot(0, UniqueId, 0)


    @staticmethod
    def AddSpineResourceName(builder, SpineResourceName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(SpineResourceName), 0)

    @staticmethod
    def AddBodyRadius(builder, BodyRadius): builder.PrependFloat32Slot(2, BodyRadius, 0)


    @staticmethod
    def AddModelPrefabName(builder, ModelPrefabName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ModelPrefabName), 0)

    @staticmethod
    def AddNormalAttackSkillData(builder, NormalAttackSkillData): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(NormalAttackSkillData), 0)

    @staticmethod
    def AddPublicSkillDataLength(builder, PublicSkillDataLength): builder.PrependInt32Slot(5, PublicSkillDataLength, 0)


    @staticmethod
    def AddDeathSkillData(builder, DeathSkillData): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(DeathSkillData), 0)

    @staticmethod
    def AddMaxHP(builder, MaxHP): builder.PrependInt32Slot(7, MaxHP, 0)


    @staticmethod
    def AddAttackPower(builder, AttackPower): builder.PrependInt32Slot(8, AttackPower, 0)


    @staticmethod
    def AddDefensePower(builder, DefensePower): builder.PrependInt32Slot(9, DefensePower, 0)


    @staticmethod
    def AddCriticalRate(builder, CriticalRate): builder.PrependInt32Slot(10, CriticalRate, 0)


    @staticmethod
    def AddCriticalDamageRate(builder, CriticalDamageRate): builder.PrependInt32Slot(11, CriticalDamageRate, 0)


    @staticmethod
    def AddAttackRange(builder, AttackRange): builder.PrependInt32Slot(12, AttackRange, 0)


    @staticmethod
    def AddMoveSpeed(builder, MoveSpeed): builder.PrependInt32Slot(13, MoveSpeed, 0)


    @staticmethod
    def AddShotTime(builder, ShotTime): builder.PrependInt32Slot(14, ShotTime, 0)


    @staticmethod
    def AddIsBoss(builder, IsBoss): builder.PrependBoolSlot(15, IsBoss, 0)


    @staticmethod
    def AddScale(builder, Scale): builder.PrependFloat32Slot(16, Scale, 0)


    @staticmethod
    def AddIgnoreObstacleCheck(builder, IgnoreObstacleCheck): builder.PrependBoolSlot(17, IgnoreObstacleCheck, 0)


    @staticmethod
    def AddCharacterVoiceGroupId(builder, CharacterVoiceGroupId): builder.PrependInt32Slot(18, CharacterVoiceGroupId, 0)

