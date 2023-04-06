from django.contrib import admin
from services.models import Service


class ServiceAdmin(admin.ModelAdmin):
    exclude = ['date_created', 'date_updated']


admin.site.register(Service, ServiceAdmin)
