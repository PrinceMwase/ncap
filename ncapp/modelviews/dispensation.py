from django.shortcuts import get_object_or_404
from ncapp.serializers import ClinicSerializer, ArtSerializer, DrugDispensationSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.art import Art
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from ncapp.models.actor import Actor
from rest_framework import permissions


class DrugDispensationViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Drug dispensations.
    """
    queryset = DrugDispensation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DrugDispensationSerializer
    def get_queryset(self):
        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=self.request.user.pk)
        queryset = self.queryset.filter(nurse_id = user.nurse.pk).all()
        return queryset

    def list(self, request):

        self.check_permissions(request=request)
        queryset = self.queryset
        serializer = DrugDispensationSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DrugDispensation.objects.all()
        art = get_object_or_404(queryset, pk=pk)
        serializer = ArtSerializer(art, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        self.check_permissions(request=request)
        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=request.user.pk)
        todayDispenstion = self.queryset.filter(nurse=user.nurse, dis_date=request.data['dis_date'] )

        if ( todayDispenstion.count() > 0 ):
            return Response(status=403, data={"error" : "cannot add drug dispensation of the same patient twice for the same nurse"})

        queryset = DrugDispensation(
                    nurse=user.nurse,
                    dis_date=request.data['dis_date'],
        )
        queryset.save()
        
        return Response(status=200, data={"success" : "Filled drug Dispensation Succesfully"});
       
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Art.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success" : "Deleted Visit Succesfully"});
        


    
