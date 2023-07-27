from django.contrib import admin
from .models import Item, item_base, item_prefix, item_sufix, Trip_result

admin.site.register(Item)
admin.site.register(item_base)
admin.site.register(item_prefix)
admin.site.register(item_sufix)
admin.site.register(Trip_result)
