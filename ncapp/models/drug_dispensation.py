from django.db import models
from .drug_fillable import DrugFillable
from .nurse import Nurse

class DrugDispensation (models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    dis_date = models.DateTimeField("Drug dispensation date")
    
    def __str__(self):
        return "Drug dispensation on :" + self.dis_date.__str__()