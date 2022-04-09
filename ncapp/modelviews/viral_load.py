from django.shortcuts import get_object_or_404
from ncapp.serializers import ClinicSerializer, ArtSerializer, ViralLoadSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.viral_load import ViralLoad
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from ncapp.models.actor import Actor
from rest_framework import permissions


class ViralLoadViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving ViralLoad
    """
    queryset = ViralLoad.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ViralLoadSerializer
    def get_queryset(self):
        return self.queryset

    def list(self, request):

        self.check_permissions(request=request)
        queryset = self.get_queryset()
        serializer = ViralLoadSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ViralLoad.objects.all()
        viral_load = get_object_or_404(queryset, pk=pk)
        serializer = ViralLoadSerializer(viral_load, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        self.check_permissions(request=request)
        todayArtVisits = self.queryset.filter(clinic_id=request.data['clinic'] )

        if ( todayArtVisits.count() > 0 ):
            return Response(status=403, data={"error" : "cannot add art viral load of the same patient twice for the same visit date"})


        userQ = Actor.objects.all()
        regimen = get_object_or_404(Regimen.objects.all(), pk=request.data['regimen'])
        clinic = get_object_or_404(Clinic.objects.all(), pk=request.data['clinic'])
        
        

        queryset = ViralLoad(
                    clinic=clinic,
                    regimen=regimen,
                    vl_date=request.data['vl_date'],
                    result=request.data['result'],
                    remark=request.data['remark']
        )
        queryset.save()
        
        return Response(status=200, data={"success" : "Filled Viral Load Succesfully"});
       
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Art.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success" : "Deleted Visit Succesfully"});
        


    
