from django.shortcuts import get_object_or_404
from ncapp.serializers import ClinicSerializer, ArtSerializer
from ncapp.models.clinic import Clinic
from ncapp.models.patient import Patient
from ncapp.models.art import Art
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from ncapp.models.actor import Actor
from rest_framework import permissions


class ArtViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving ART dispensations.
    """
    queryset = Art.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArtSerializer
    def get_queryset(self):
        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=self.request.user.pk)
        queryset = self.queryset.filter(nurse_id = user.nurse.pk).all()
        return queryset

    def list(self, request):

        self.check_permissions(request=request)
        queryset = self.queryset
        serializer = ArtSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Art.objects.all()
        art = get_object_or_404(queryset, pk=pk)
        serializer = ArtSerializer(art, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        self.check_permissions(request=request)
        todayArtVisits = self.queryset.filter(clinic=request.data['clinic'] )

        if ( todayArtVisits.count() > 0 ):
            return Response(status=403, data={"error" : "cannot add art dispensation of the same patient twice for the same visit date"})


        userQ = Actor.objects.all()
        user = get_object_or_404(userQ, pk=request.user.pk)
        regimen = get_object_or_404(Regimen.objects.all(), pk=request.data['art_given'])
        clinic = get_object_or_404(Clinic.objects.all(), pk=request.data['clinic'])
        
        

        print(user.nurse)
        queryset = Art(
                    wt=request.data['wt'],
                    ht=request.data['ht'],
                    sbp_dbp=request.data['sbp_dbp'],
                    side_effect=request.data['side_effect'],
                    tb_status=request.data['tb_status'],
                    dose_missed=request.data['dose_missed'],
                    pill_count=request.data['pill_count'],
                    art_given=regimen,
                    number_of_regimen_pills=request.data['number_of_regimen_pills'],
                    pyridoxine=request.data['pyridoxine'],
                    inh=request.data['inh'],
                    bp_drug=request.data['bp_drug'],
                    number_of_tabs=request.data['number_of_tabs'],
                    fp_meth=request.data['fp_meth'],
                    number_of_condoms=request.data['number_of_condoms'],
                    adverse_outcome=request.data['adverse_outcome'],
                    clinic=clinic,
        )
        queryset.save()
        
        return Response(status=200, data={"success" : "Filled ART Dispensation Succesfully"});
       
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Art.objects.all()
        clinic = get_object_or_404(queryset, pk=pk)
        clinic.delete()
        return Response(status=200, data={"success" : "Deleted Visit Succesfully"});
        


    
