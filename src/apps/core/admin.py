from django.contrib import admin

from .models import Faction, FactionKeyword, WeaponType


@admin.register(Faction)
class FactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(FactionKeyword)
class FactionKeywordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'discretion')
