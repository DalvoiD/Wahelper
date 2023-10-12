import graphene
from graphene_django import DjangoObjectType

from .models import Ability, ArmyRule, Keyword, Weapon, Unit


class AbilityNode(DjangoObjectType):
    class Meta:
        model = Ability


class ArmyRuleNode(DjangoObjectType):
    class Meta:
        model = ArmyRule


class KeywordNode(DjangoObjectType):
    class Meta:
        model = Keyword


class WeaponNode(DjangoObjectType):
    class Meta:
        model = Weapon


class UnitNode(DjangoObjectType):
    class Meta:
        model = Unit


class Query(graphene.ObjectType):
    abilities = graphene.List(AbilityNode)
    armies_rules = graphene.List(ArmyRuleNode)
    keywords = graphene.List(KeywordNode)
    weapons = graphene.List(WeaponNode)
    units = graphene.List(UnitNode)

    def resolve_abilities(self, info):
        return Ability.objects.all()

    def resolve_armies_rules(self, info):
        return ArmyRule.objects.all()

    def resolve_keywords(self, info):
        return Keyword.objects.all()

    def resolve_weapons(self, info):
        return Weapon.objects.all()

    def resolve_units(self, info):
        return Unit.objects.all()
