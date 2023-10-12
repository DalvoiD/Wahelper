from django.contrib import admin

from .models import Weapon, Unit, Keyword


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
                    'base', 'points')

    @staticmethod
    def faction_keywords(obj) -> str:
        return ', '.join([a.name for a in obj.faction_keyword.all()])

    @staticmethod
    def keywords(obj) -> str:
        return ', '.join([k.name for k in obj.keyword.all()])

    @staticmethod
    def weapons(obj) -> str:
        return ', '.join([w.name for w in obj.weapon.all()])


@admin.register(Keyword)
class KeywordCSMAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
