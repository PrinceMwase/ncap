from django.db import models
from django.contrib.auth.models import User
from .location import Location

class Actor(User):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, default=False)
    
    