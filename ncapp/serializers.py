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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        exclude = ["nurse"]

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        exclude = ["password", "last_login", "user_permissions", "is_superuser", "date_joined"]

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = "__all__"

class DispensationFieldSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        userQ = Actor.objects.all()
        requestUser = self.context['request'].user
        user = get_object_or_404(userQ, pk=requestUser.pk)
        data = data(nurse_id = user.nurse.pk)
        
        return super(DispensationFieldSerializer, self).to_representation(data)

class DrugDispensationSerializer(serializers.ModelSerializer):
    class Meta:
        # list_serializer_class = DispensationFieldSerializer
        model = DrugDispensation
        exclude = ["nurse"]

        

class DispensationFillableSerializer(serializers.ModelSerializer):
    # dispensation = DrugDispensationSerializer
    class Meta:
        model = DispensationFillable
        fields = "__all__"
        

class DrugFillableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugFillable
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"

class RegimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regimen
        fields = "__all__"

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = "__all__"

class SupportGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportGroup
        fields = "__all__"

class ViralLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViralLoad
        fields = "__all__"





