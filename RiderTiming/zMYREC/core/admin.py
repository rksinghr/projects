from django.contrib import admin
from .models import userProfile, eventType, eventName, userPerfData

# Register your models here.
admin.site.register(userProfile)
admin.site.register(eventType)
admin.site.register(eventName)
admin.site.register(userPerfData)