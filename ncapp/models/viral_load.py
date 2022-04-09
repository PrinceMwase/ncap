from django.db import models
from .patient import Patient
from .clinic import Clinic
from .regimen import Regimen

class ViralLoad (models.Model):
    clinic = models.OneToOneField(Clinic, on_delete=models.CASCADE)
    regimen = models.ForeignKey(Regimen, on_delete=models.CASCADE)
    vl_date = models.DateField('viral load date')
    result = models.CharField(max_length=20)
    remark = models.TextField( max_length=64, default="" )

    def __str__(self):
        return self.clinic.__str__()