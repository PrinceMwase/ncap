from django.db import models

class DrugFillable (models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Drug"
        
    def __str__(self):
        return self.name