import uuid
from django.db import models

from apps.factions.common.models import CharField, IntegerField, UUIDField, ManyToManyField, ForeignKey
from apps.factions.common.models import WeaponType


class KeywordCSM(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'


class WeaponCSM(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)
    type = ManyToManyField(WeaponType)
    range = CharField(max_length=5)
    attack = CharField(max_length=5)
    ballistic_skill = CharField(max_length=5)
    strength = IntegerField()
    armour_penetration = CharField(max_length=5)
    damage = CharField(max_length=5)

    def __str__(self) -> str:
        return f'{self.name}'


class UnitCSM(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=50)
