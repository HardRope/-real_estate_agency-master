from django.contrib import admin

from .models import Flat
from .models import Appeal


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ['created_at',]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town',)
    raw_id_fields = ('liked_by',)

class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Appeal, AppealAdmin)
