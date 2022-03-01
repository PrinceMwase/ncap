from django.db import models
from django.contrib.auth.models import User
from .location import Location

class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex= models.CharField(
            max_length=1,
            choices= [
                ('m' , 'Male'),
                ('f' , 'Female')
            ]
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name