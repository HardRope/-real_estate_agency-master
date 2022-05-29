from django.contrib import admin

from .models import Flat
from .models import Appeal
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ['created_at',]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town',)
    raw_id_fields = ('liked_by',)


class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    list_display=('name', 'owner_phonenumber', 'owner_pure_phone',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Appeal, AppealAdmin)
admin.site.register(Owner, OwnerAdmin)
