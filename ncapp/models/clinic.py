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
    initiation_date = models.DateTimeField('Date initiated')
    next_appointment = models.DateTimeField('Next appointment')
    cpt = models.CharField(max_length=10)
    date_of_enrollment = models.DateTimeField('Date of Enrollment')
    visit_date = models.DateField('Visit Date' )

    class Meta:
        verbose_name = "Appointment"
        
    
    

    def __str__(self):
        return self.art_number+"_"+self.patient.first_name+"_"+self.visit_date.__str__()
        
