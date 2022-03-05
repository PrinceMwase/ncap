from django.db import models
from .drug_fillable import DrugFillable


class DispensationFillable (models.Model):
    dispensation = models.ForeignKey('DrugDispensation', on_delete=models.CASCADE, unique=False )
    fillable = models.ForeignKey(DrugFillable, on_delete=models.CASCADE, unique=False)
    count = models.IntegerField("amount")
    
    class Meta:
        verbose_name = "Drug Dispensation"

    def __str__(self):
        return "%s : %i" % (self.fillable.name, self.count )