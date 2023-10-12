import uuid
from django.db import models

from apps.core.models import CharField, IntegerField, UUIDField, ManyToManyField, ForeignKey
from apps.core.models import WeaponType, FactionKeyword, Faction


class Chapter(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'


class Keyword(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'


class Weapon(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=30)
    type = ManyToManyField(WeaponType, blank=True)
    range = CharField(max_length=5)
    attack = CharField(max_length=5)
    ballistic_skill = CharField(max_length=5)
    strength = IntegerField()
    armour_penetration = CharField(max_length=5)
    damage = CharField(max_length=5)

    def __str__(self) -> str:
        return f'{self.name}'


class Unit(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=50)
    move = CharField(max_length=3)
    toughness = IntegerField()
    save_unit = CharField(max_length=2)
    invulnerable_save = CharField(max_length=3)
    wound = IntegerField()
    leadership = CharField(max_length=3)
    objective_control = IntegerField()
    weapon = ManyToManyField(Weapon)
    keyword = ManyToManyField(Keyword)
    faction_keyword = ManyToManyField(FactionKeyword)
    base = CharField(max_length=10)
    points = IntegerField()
    chapter = ForeignKey(Chapter, on_delete=models.CASCADE)
    faction = ForeignKey(Faction, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
