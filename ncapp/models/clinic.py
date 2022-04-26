from django.db import models
from .location import Location
from .support_group import SupportGroup
from .site import Site
from .patient import Patient
from .nurse import Nurse

class Clinic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    art_number = models.CharField(max_length=20)
    file_number = models.CharField(max_length=20)
    initiation_date = models.DateField('Date initiated')
    next_appointment = models.DateField('Next appointment')
    cpt = models.CharField(max_length=10)
    date_of_enrollment = models.DateField('Date of Enrollment')
    visit_date = models.DateField('Visit Date' )

    class Meta:
        verbose_name = "Appointment"
        ordering = ['-id']
        
    
    

    def __str__(self):
        return self.art_number+"_"+self.support_group.__str__()+"_"+self.visit_date.__str__()
        
