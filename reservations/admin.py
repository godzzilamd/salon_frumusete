from django.contrib import admin
from reservations.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    exclude = ['date_created', 'date_updated']


admin.site.register(Reservation, ReservationAdmin)
