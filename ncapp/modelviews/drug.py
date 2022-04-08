from django.shortcuts import get_object_or_404
from ncapp.serializers import ClinicSerializer, ArtSerializer, DrugDispensationSerializer, DrugFillableSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.art import Art
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.drug_fillable import DrugFillable
from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from ncapp.models.actor import Actor
from rest_framework import permissions


class DrugFillableViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Drugs
    """
    queryset = DrugFillable.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DrugFillableSerializer

    def get_queryset(self):
        return self.queryset

    def list(self, request):

        self.check_permissions(request=request)
        queryset = self.queryset
        serializer = DrugFillableSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
       
        art = get_object_or_404(self.queryset, pk=pk)
        serializer = DrugFillableSerializer(DrugFillable, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        self.check_permissions(request=request)

        queryset = DrugFillable(
                    name=request.data['name']
                    
        )
        queryset.save()
        
        return Response(status=200, data={"success" : "Added drug Succesfully"});
       
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Art.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success" : "Deleted Visit Succesfully"});
        


    
