from django.shortcuts import get_object_or_404
from ncapp.serializers import ClinicSerializer, ArtSerializer, DrugDispensationSerializer, DispensationFillableSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.art import Art
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.site import Site
from ncapp.models.dispensation_fillable import DispensationFillable
from ncapp.models.drug_fillable import DrugFillable
from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from ncapp.models.actor import Actor
from rest_framework import permissions


class DispensationFillableViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Drug dispensations.
    """
    queryset = DispensationFillable.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DispensationFillableSerializer
    def get_queryset(self):
        return queryset

    def list(self, request):

        self.check_permissions(request=request)
        queryset = self.queryset
        serializer = DispensationFillableSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DispensationFillableSerializer.objects.all()
        dispensation_fillable = get_object_or_404(queryset, pk=pk)
        serializer = DispensationFillableSerializer(dispensation_fillable, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        print( request.data['dispensation'] )
        self.check_permissions(request=request)
        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=request.user.pk)
        dispensation = get_object_or_404(DrugDispensation, pk=request.data['dispensation'])
        fillable = get_object_or_404(DrugFillable, pk=request.data['fillable'])

        if (dispensation.nurse.pk != user.nurse.pk ) :
            return Response(status=403, data={'error' : "not allowed"})

        todayDispenstionFillable = self.queryset.filter(dispensation=dispensation, fillable=fillable )


        if ( todayDispenstionFillable.count() > 0 ):
            return Response(status=403, data={"error" : "already added"})

        queryset = DispensationFillable(
                    dispensation=dispensation,
                    fillable=fillable,
                    count=request.data['count']
        )
        queryset.save()
        
        return Response(status=200, data={"success" : "addded to dispensation succesfully"});
       
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Art.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success" : "Deleted Visit Succesfully"});
        


    
