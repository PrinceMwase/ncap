from django.shortcuts import get_object_or_404
from ncapp.serializers import (
    ClinicSerializer,
    ArtSerializer,
    DrugDispensationSerializer,
    DispensationFillableSerializer,
)
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.art import Art
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.site import Site
from ncapp.models.stock import Stock
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
        return self.queryset

    def list(self, request):

        self.check_permissions(request=request)
        queryset = self.queryset
        serializer = DispensationFillableSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DispensationFillableSerializer.objects.all()
        dispensation_fillable = get_object_or_404(queryset, pk=pk)
        serializer = DispensationFillableSerializer(
            dispensation_fillable, context={"request": request}
        )
        return Response(serializer.data)

    def create(self, request):
        print(request.data["dispensation"])
        self.check_permissions(request=request)
        stock = Stock.objects.filter(date=timezone.now().date(), fillable_id=request.data["fillable"], support_group_id=1 )
        
        
        if stock.count() < 1:
            return Response(status=403, data={"error": "Check Stock, make sure you theres stock for this drug today"})
        stock = get_object_or_404(Stock, pk=stock[:1].get().id )
        
        
        if ( (stock.count - request.data["count"]) < 0 ):
            return Response(status=403, data={"error": "check available stock for this day"})
        
                
        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=request.user.pk)
        print("this is %i affter user " % request.data["dispensation"])
        dispensation = get_object_or_404(
            DrugDispensation, pk=request.data["dispensation"]
        )
        
        
        fillable = get_object_or_404(DrugFillable, pk=request.data["fillable"])

        if dispensation.nurse.pk != user.nurse.pk:
            return Response(status=403, data={"error": "not allowed to edit this dispensation"})

        todayDispenstionFillable = self.queryset.filter(
            dispensation=dispensation, fillable=fillable
        )

        if todayDispenstionFillable.count() > 0:
            return Response(status=403, data={"error": "already added"})

        queryset = DispensationFillable(
            dispensation=dispensation,
            fillable=fillable, count=request.data["count"]
        )
        stock.count -=  request.data["count"]
        stock.save()
        queryset.save()

        return Response(
            status=200, data={"success": "addded to dispensation succesfully"}
        )

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Art.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success": "Deleted Visit Succesfully"})
