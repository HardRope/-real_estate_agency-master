from django.contrib import admin

from .models import Flat
from .models import Appeal
from .models import Owner


class OwnerInline(admin.StackedInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'flat_owners__name')
    readonly_fields = ['created_at',]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'town',)
    raw_id_fields = ('liked_by', 'flat_owners',)
    inlines = [OwnerInline]

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    list_display=('name', 'owner_pure_phone',)
