from django.contrib import admin
# from .models import Faction


# @admin.register(Ability)
# class AbilityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#
#
# @admin.register(Keyword)
# class KeywordAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# @admin.register(Faction)
# class FactionAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# @admin.register(Unit)
# class UnitAdmin(admin.ModelAdmin):
#     list_display = ('name', 'faction', 'weapons', 'move', 'toughness', 'save', 'invulnerable_save', 'wound',
#                     'leadership', 'objective_control', 'abilities', 'keywords')
#
#     @staticmethod
#     def abilities(obj) -> str:
#         return ', '.join([a.name for a in obj.ability.all()])
#
#     @staticmethod
#     def keywords(obj) -> str:
#         return ', '.join([k.name for k in obj.keyword.all()])
#
#     @staticmethod
#     def weapons(obj) -> str:
#         return ', '.join([w.name for w in obj.weapon.all()])
#
#
# @admin.register(WeaponType)
# class WeaponTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#
#
# @admin.register(Weapon)
# class WeaponAdmin(admin.ModelAdmin):
#     list_display = ('name', 'types', 'range', 'attack', 'ballistic_skill', 'strength', 'armour_penetration', 'damage')
#
#     @staticmethod
#     def types(obj) -> str:
#         return ', '.join([t.name for t in obj.type.all()])
