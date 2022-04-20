from django.contrib.auth.models import User, Group
from ncapp.models.stock import Stock
from rest_framework import serializers
from ncapp.models import Clinic
from django.contrib.auth import authenticate
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
        fields = ['url', 'username', 'email', 'is_superuser']


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
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
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
        list_serializer_class = DispensationFieldSerializer
        model = DrugDispensation
        exclude = ["nurse"]

class VlSerializer(serializers.Serializer):
    date_of_enrollment = serializers.DateField()
    regimen = serializers.CharField(max_length=64)
    vl_date = serializers.DateField('viral load date')
    result = serializers.CharField(max_length=20)
    patient = serializers.CharField(max_length=20)
    sex = serializers.CharField(max_length=20)
    art_number = serializers.CharField(max_length=20)
    file_number = serializers.CharField(max_length=20)
    initiation_date = serializers.DateField()
    cpt = serializers.CharField(max_length=20)
    remark = serializers.CharField( max_length=64, default="" ) 


class DispensationFillableSerializer(serializers.ModelSerializer):
    dispensation = DrugDispensationSerializer
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

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs




