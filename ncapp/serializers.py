from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ncapp.models import Clinic

from ncapp.models.location import Location
from ncapp.models.actor import Actor
from ncapp.models.patient import Patient
from ncapp.models.nurse import Nurse
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from ncapp.models.viral_load import ViralLoad
from ncapp.models.drug_fillable import DrugFillable

from ncapp.models.dispensation_fillable import DispensationFillable
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.art import Art

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinic
        fields = "__all__"

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class ArtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Art
        fields = "__all__"

class DispensationFillableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DispensationFillable
        fields = "__all__"

class DrugDispensationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DrugDispensation
        fields = "__all__"

class DrugFillableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DrugFillable
        fields = "__all__"

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class NurseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"

class RegimenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regimen
        fields = "__all__"

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"

class SupportGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupportGroup
        fields = "__all__"

class ViralLoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ViralLoad
        fields = "__all__"





