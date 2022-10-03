from django.contrib import admin

from .models import Payment, Reservation


admin.site.register(Reservation)
admin.site.register(Payment)