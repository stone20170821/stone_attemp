from django.contrib import admin

from .models import HorseBasicTemp


# Register your models here.

class HorseBasicTempAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'industry', 'pe', 'outstanding', 'totals', 'totalAssets', 'liquidAssets',
                    'fixedAssets', 'esp', 'bvps', 'pb','timeToMarket', 'rev', 'profit', 'gpr', 'npr')


admin.site.register(HorseBasicTemp, HorseBasicTempAdmin)
