from django.contrib import admin
from .models import Item, item_base, item_prefix, item_sufix, Trip_result


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'base', 'prefix', 'sufix']


@admin.register(item_base)
class Item_BaseAdmin(admin.ModelAdmin):
    list_display =['__str__', 'item_type', 'type_of_wep', 'item_base_number', 'name']

@admin.register(item_prefix)
class Item_PrefixAdmin(admin.ModelAdmin):
    list_display =['__str__', 'item_type', 'type_of_wep', 'prefix_number', 'name']

@admin.register(item_sufix)
class Item_SufixAdmin(admin.ModelAdmin):
    list_display =['__str__', 'item_type', 'type_of_wep', 'sufix_number', 'name']


admin.site.register(Trip_result)
