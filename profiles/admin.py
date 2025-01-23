from django.contrib import admin
from .models import Profile, Race, TextMessage, Combat1v1_result

admin.site.register(Profile)
admin.site.register(Race)
admin.site.register(TextMessage)
admin.site.register(Combat1v1_result)
