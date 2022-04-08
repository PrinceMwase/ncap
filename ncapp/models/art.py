from django.db import models
from .nurse import Nurse
from .patient import Patient
from .site import Site
from .support_group import SupportGroup
from .regimen import Regimen
from .clinic import Clinic

class Art (models.Model):
    wt = models.FloatField("Weight", max_length=1000)
    ht = models.IntegerField("Height")
    sbp_dbp = models.CharField("Sytolic blood pressure over Dystolic blood pressure", max_length=20)
    side_effect = models.CharField(
            "Side effect",
            max_length=3,
            choices=[ 
                ("NO", "NO"),
                ("PN", "PN"),
                ("HP","HP"),
                ("SK","SK"),
                ("LIP","LIP"),
                ("OTH","OTH")
            ]  
    )
    tb_status = models.CharField("TB Status", max_length=20,
                choices=[
                    ("No TB", "NO TB"),
                    ("Y", "Yes"),
                    ('C', "conclusive"),
                    ("on_RX", "On RX")
                ]
        )
    dose_missed = models.IntegerField()
    pill_count = models.IntegerField()
    art_given = models.ForeignKey(Regimen, on_delete=models.CASCADE)
    number_of_regimen_pills = models.IntegerField()
    pyridoxine = models.IntegerField()
    inh = models.IntegerField()  
    bp_drug = models.CharField(max_length=20)
    number_of_tabs = models.IntegerField()
    fp_meth = models.CharField(max_length=20)
    number_of_condoms = models.IntegerField()
    adverse_outcome = models.CharField(max_length=20)
    clinic = models.OneToOneField(Clinic, on_delete=models.CASCADE, verbose_name="Visit")
    # next appointment will be generated from clinic report

    class Meta:
        verbose_name = "ART Dispensation"
    
    def __str__(self):
        return self.clinic.__str__()
