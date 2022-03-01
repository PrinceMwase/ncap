from django.db import models
from .location import Location

class SupportGroup(models.Model):
    name = models.CharField(max_length=42)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name+"_"+self.location.name