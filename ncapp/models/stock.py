from django.db import models
from .drug_fillable import DrugFillable
from .support_group import SupportGroup
from .nurse import Nurse
from .drug_dispensation import DrugDispensation

class Stock (models.Model):
    count = models.IntegerField(verbose_name="Drug amount")
    fillable = models.ForeignKey(DrugFillable, on_delete=models.CASCADE, unique=False, verbose_name="Drug")
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE, default=1)
    dispensation = models.ForeignKey(DrugDispensation, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    date = models.DateField('Date of Stock')
    
    class Meta:
        verbose_name = "Drug Stock"
