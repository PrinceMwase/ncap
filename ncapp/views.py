from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ncapp.serializers import StockSerializer, UserSerializer, \
    GroupSerializer, ClinicSerializer, \
    PatientSerializer, NurseSerializer, \
    ActorSerializer, LocationSerializer, \
    SupportGroupSerializer, SiteSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.location import Location
from ncapp.models.actor import Actor
from ncapp.models.patient import Patient
from ncapp.models.nurse import Nurse
from ncapp.models.site import Site
from ncapp.models.stock import Stock
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from ncapp.models.viral_load import ViralLoad
from ncapp.models.drug_fillable import DrugFillable
from rest_framework.response import Response
from ncapp.models.dispensation_fillable import DispensationFillable
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.art import Art
from rest_framework import permissions
from rest_framework import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stock to be viewed or edited.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def support_group(self, request):
        patients = self.queryset.filter(
            support_group=request.GET['support_group'])
        page = self.paginate_queryset(patients)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(patients, many=True)
        return Response(serializer.data)


class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupportGroupViewSet(viewsets.ModelViewSet):
    queryset = SupportGroup.objects.all()
    serializer_class = SupportGroupSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return HttpResponse("Hello, world. You're at the ncaap index.")


class authentication (APIView):
    permission_classes = [permissions.AllowAny]

    @api_view(['POST'])
    def loginUser(request):

        if request.method == "POST":
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                data = UserSerializer(user, context={'request': request})
                return Response(status=200, data=data.data)
            else:
                return Response(status=304, data=None)
        return Response(status=304, data=None)
