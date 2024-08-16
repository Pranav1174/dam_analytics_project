from django.contrib import admin
from .models import Dam, DamStatistics

@admin.register(Dam)
class DamAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')

@admin.register(DamStatistics)
class DamStatisticsAdmin(admin.ModelAdmin):
    list_display = ('dam', 'date', 'rainfall', 'inflow', 'power_house_discharge', 'spillway_release')
    list_filter = ('dam', 'date')
    search_fields = ('dam__name',)
