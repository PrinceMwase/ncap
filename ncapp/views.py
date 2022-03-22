from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ncapp.serializers import UserSerializer, GroupSerializer,ClinicSerializer
from ncapp.models.clinic import Clinic
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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CLinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("Hello, world. You're at the ncaap index.")