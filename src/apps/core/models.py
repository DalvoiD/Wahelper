import uuid
from django.db import models


class IntegerField(models.IntegerField):
    pass


class CharField(models.CharField):
    pass


class ForeignKey(models.ForeignKey):
    pass


class UUIDField(models.UUIDField):
    pass


class ManyToManyField(models.ManyToManyField):
    pass


class TextField(models.TextField):
    pass


class CoreAbility(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)
    discretion = TextField()

    def __str__(self) -> str:
        return f'{self.name}'


class Fraction(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'


class FactionKeyword(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'


class WeaponType(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=20)
    discretion = TextField()

    def __str__(self) -> str:
        return f'{self.name}'
