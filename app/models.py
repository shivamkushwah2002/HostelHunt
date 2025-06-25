from django.db import models

from django.contrib.auth.models import User
from django.db import models


class Listing(models.Model):
    Room=[('pg','PG'),('hostel','Hostel')]
    room = models.CharField(max_length=10,choices=Room)

    hostel_name = models.CharField(max_length=100)

    Room_Type=[('single','Single'),('sharing','Sharing')]
    room_type = models.CharField(max_length=10,choices=Room_Type)

    location = models.CharField(max_length=100)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    contact_info = models.CharField(max_length=15)
    owner = models.CharField(max_length=50)
    college=models.CharField( max_length=100)
    image = models.ImageField(upload_to='media/listing_images/', blank=True, null=True)
    description = models.TextField()
    landmark=models.CharField(max_length=50)

    Beds=[('single','Single'),('double','Double'),('triple','Triple')]
    beds=models.CharField( max_length=50,choices=Beds)

    Wifi=[('yes','Yes'),('no','No')]
    wifi = models.CharField(max_length=10,choices=Wifi)

    home_service=models.CharField( max_length=50)

    
    Meals=[('yes','Yes'),('no','No')]
    meals = models.CharField(max_length=10,choices=Meals)
    
    Type_room=[('ac','AC'),('non-ac','Non-AC')]
    type_room = models.CharField(max_length=10,choices=Type_room)
    
    Laundry=[('yes','Yes'),('no','No')]
    laundry = models.CharField(max_length=10,choices=Laundry)
