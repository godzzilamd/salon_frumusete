from django.contrib import admin
from workers.models import Worker


class WorkerAdmin(admin.ModelAdmin):
    exclude = ['date_created', 'date_updated']


admin.site.register(Worker, WorkerAdmin)
