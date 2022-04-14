from django.db import models
from django.contrib.auth.models import User
from .location import Location
from .support_group import SupportGroup
from datetime import date
from django.utils import timezone
import uuid

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
    uuid  = models.UUIDField( default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField('Date of Birth', default=timezone.now )
    support_group = models.ForeignKey(SupportGroup, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name + ' ' + self.last_name