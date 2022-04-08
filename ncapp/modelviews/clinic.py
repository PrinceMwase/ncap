from django.shortcuts import get_object_or_404
from ncapp.serializers import ClinicSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.site import Site
from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from ncapp.models.actor import Actor
from rest_framework import permissions


class ClinicViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving visits.
    """
    queryset = Clinic.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClinicSerializer
    def get_queryset(self):
        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=self.request.user.pk)
        queryset = self.queryset.filter(nurse_id = user.nurse.pk).all()
        return queryset

    def list(self, request):
        self.check_permissions(request=request)
        queryset = self.get_queryset()
        serializer = ClinicSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Clinic.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        serializer = ClinicSerializer(clinic, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        self.check_permissions(request=request)
        todayPatientVisits = self.queryset.filter(patient=request.data['patient'] , visit_date=request.data['visit_date'])

        if ( todayPatientVisits.count() > 0 ):
            return Response(status=403, data={"error" : "cannot add visit of the same patient twice for the same visit date"})


        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=request.user.pk)
        patient = get_object_or_404(Patient.objects.all(), pk=request.data['patient'])
        support_group = get_object_or_404(SupportGroup.objects.all(), pk=request.data['support_group'])
        site = get_object_or_404(Site.objects.all(), pk=request.data['site'])
        

        print(user.nurse)
        queryset = Clinic(
                    support_group= support_group,
                    patient=patient,
                    nurse = user.nurse,
                    site=site,
                    art_number=request.data['art_number'],
                    file_number=request.data['file_number'],
                    initiation_date=request.data['initiation_date'],
                    next_appointment=request.data['next_appointment'],
                    cpt=request.data['cpt'],
                    date_of_enrollment=request.data['date_of_enrollment'],
                    visit_date=request.data['visit_date']
        )
        queryset.save()
        serializer = ClinicSerializer( queryset )
        return Response(serializer.data)
       
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Clinic.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success" : "Deleted Visit Succesfully"});
        


    
