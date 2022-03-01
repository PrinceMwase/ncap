
from ncapp.models import Location
from datetime import datetime,timedelta
import random

from django.contrib.auth.models import User
from ncapp.models.location import Location
from ncapp.models.actor import Actor

from ncapp.models.patient import Patient
from ncapp.models.nurse import Nurse
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from ncapp.models.clinic import Clinic
from ncapp.models.viral_load import ViralLoad
from ncapp.models.drug_fillable import DrugFillable
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.dispensation_fillable import DispensationFillable
from ncapp.models.art import Art



class seedAll():
    """for generating seeders"""
    inserted_pks = {}
    def getModel( self,  model):
        primary_key = random.choice (self.inserted_pks[model])
        model_list = self.inserted_pks[model]
        index = self.inserted_pks[model].index(primary_key)
        
        self.model = model.objects.get(pk = primary_key )
        del model_list[index]
        
        return self.model
    def update_inserted_pks( self):
        self.inserted_pks.update( self.seeder.execute())

    def seed( self):
        from django_seed import Seed

        self.seeder = Seed.seeder()

        self.seeder.add_entity(Patient, 100)

        self.seeder.add_entity(Location, 10)
    
    
        self.inserted_pks = self.seeder.execute()


        self.seeder.add_entity(Regimen, 10),


        self.seeder.add_entity( SupportGroup, 20, {
            'location' : self.getModel( self, Location)
        })
        self.update_inserted_pks( self)

        
        
        self.seeder.add_entity( Site, 5 ,  {
            'location' : self.getModel( self, Location)
        })
        
        self.seeder.add_entity( Clinic, 1000, {
            'initiation_date' : lambda x: datetime.now().isoformat( sep=" "),
            'next_appointment' : lambda x: (datetime.now() + timedelta(days=1)).isoformat( sep=" ") ,
            'date_of_enrollment' : lambda x: datetime.now().isoformat( sep=" "),
            'visit_date' : lambda x: datetime.now().isoformat( sep=" "),
            'patient' : self.getModel( self, Patient),
            'nurse' : Nurse.objects.get(pk=random.choice(list ( [random.randint(1,17)] * 50 ) )),
            'support_group' : self.getModel( self, SupportGroup),
            
        } )

        self.update_inserted_pks( self)

        self.seeder.add_entity( ViralLoad, 50 , {
            'vl_date' : lambda x: datetime.now().isoformat( sep=" "),
            'clinic' : self.getModel( self, Clinic),
            'regimen' : self.getModel( self, Regimen)
        })
        self.update_inserted_pks( self)

        self.seeder.add_entity(DrugFillable, 300)
        self.update_inserted_pks( self)
        
        self.seeder.add_entity(DrugDispensation, 1, {
            'dis_date' : lambda x: datetime.now().isoformat( sep=" "),
            'nurse' :  Nurse.objects.get(pk=random.choice(list ( [random.randint(1,17)] * 50 ) )),
        })
        self.update_inserted_pks( self)

        self.seeder.add_entity(DispensationFillable, 20, {
            'dispensation' : self.getModel( self, DrugDispensation),
            'fillable' : self.getModel( self, DrugFillable)
            
        })
        self.update_inserted_pks( self)

        self.seeder.add_entity(Art, 50,{
            'clinic' : self.getModel( self, Clinic),
            'art_given' : self.getModel( self, Regimen)
        })
        self.update_inserted_pks( self)
