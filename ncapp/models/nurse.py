from django.db import models
from .actor import Actor

class Nurse(models.Model):
    user = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
