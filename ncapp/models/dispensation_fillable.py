from django.db import models
from .drug_fillable import DrugFillable
from .drug_dispensation import DrugDispensation

class DispensationFillable (models.Model):
    dispensation = models.ForeignKey(DrugDispensation, on_delete=models.CASCADE)
    fillable = models.ForeignKey(DrugFillable, on_delete=models.CASCADE)
    count = models.IntegerField("amount")

    def __str__(self):
        return self.dispensation.__str__()