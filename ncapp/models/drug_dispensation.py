from django.db import models
from .drug_fillable import DrugFillable
from ncapp.models.dispensation_fillable import DispensationFillable
from .nurse import Nurse

class DrugDispensation (models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    dis_date = models.DateField("Drug dispensation date")

    drugs = models.ManyToManyField( 
        DrugFillable,
        through='DispensationFillable',
        through_fields=('dispensation', 'fillable'))

    fillable = models.ForeignObjectRel('dispensation', DispensationFillable)
    
    def __str__(self):
        return "%s : %s " %  (self.dis_date.__str__(), self.nurse.user.__str__() )
    def getKey(self):
        return self.pk

    class Meta:
        verbose_name = "Dispensation session"