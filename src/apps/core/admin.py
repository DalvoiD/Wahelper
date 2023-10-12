from django.contrib import admin

from .models import Fraction, FactionKeyword, WeaponType, CoreAbility


@admin.register(CoreAbility)
class CoreAbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discretion')


@admin.register(Fraction)
class FractionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(FactionKeyword)
class FactionKeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discretion')
