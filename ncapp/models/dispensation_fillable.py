from django.db import models
from .drug_fillable import DrugFillable
from .drug_dispensation import DrugDispensation

class DispensationFillable (models.Model):
    dispensation = models.OneToOneField(DrugDispensation, on_delete=models.CASCADE)
    fillable = models.OneToOneField(DrugFillable, on_delete=models.CASCADE)
    count = models.IntegerField("amount")