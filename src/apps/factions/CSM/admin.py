from django.contrib import admin

from .models import Weapon, Unit, Keyword, ArmyRule, Ability


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discretion')


@admin.register(ArmyRule)
class ArmyRuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discretion')


@admin.register(Weapon)
class WeaponCSMAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'types', 'range', 'attack', 'ballistic_skill', 'strength',
                    'armour_penetration', 'damage')

    @staticmethod
    def types(obj) -> str:
        return ', '.join([t.name for t in obj.type.all()])


@admin.register(Unit)
class UnitCSMAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'move', 'toughness', 'save_unit', 'invulnerable_save', 'wound',
                    'leadership', 'objective_control', 'weapons', 'keywords', 'faction_keywords',
                    'base', 'points', 'army_rule', 'fraction', 'core_abilities', 'abilities')

    @staticmethod
    def faction_keywords(obj) -> str:
        return ', '.join([fk.name for fk in obj.faction_keyword.all()])

    @staticmethod
    def keywords(obj) -> str:
        return ', '.join([k.name for k in obj.keyword.all()])

    @staticmethod
    def weapons(obj) -> str:
        return ', '.join([w.name for w in obj.weapon.all()])

    @staticmethod
    def core_abilities(obj) -> str:
        return ', '.join([ca.name for ca in obj.core_ability.all()])

    @staticmethod
    def abilities(obj) -> str:
        return ', '.join([a.name for a in obj.core_ability.all()])


@admin.register(Keyword)
class KeywordCSMAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
