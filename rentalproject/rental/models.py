from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bike(models.Model):
    class Type(models.TextChoices):
        STANDARD = "STD", "Standard"
        MOUNTAIN = "MTN", "Mountain"
        ROAD = "RD", "Road"
        ELECTRIC = "ELC", "Electric"

    name = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bike_type = models.CharField(max_length=50, choices=Type.choices)
    location = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='bike_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    x_location = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    y_location = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    bikes = models.ManyToManyField(Bike, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.bike.name}"

class Service(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.bike.name} - Service on {self.service_date}"