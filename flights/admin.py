from django.contrib import admin

from .models import Flight, Airport, Passenger
# Register your models here.

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)

#14:21