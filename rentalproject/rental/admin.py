from django.contrib import admin
from .models import Bike, Booking, Service, Shop

# Register your models here.
admin.site.register(Bike)
admin.site.register(Booking)
admin.site.register(Service)
admin.site.register(Shop)