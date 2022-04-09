from datetime import date
from ncapp.models.viral_load import ViralLoad
from django.core import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse

class VlMonitoringViewSet(viewsets.ViewSet):
    """
    Generate Daily Viral load Monitoring
    """
   
    queryset = ViralLoad.objects.filter( vl_date=date.today()  )
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # print(ViralLoad.objects.all())
        return self.queryset

    def list(self, request):
        vl_all = []
        for i , vl in enumerate( self.get_queryset().select_related('clinic')  ):
            vl_all += [[ i, vl.clinic.patient.__str__(), vl.clinic.patient.sex, \
                vl.clinic.art_number, vl.clinic.file_number, \
                vl.clinic.initiation_date, vl.vl_date, vl.result, vl.regimen.__str__(), \
                vl.clinic.cpt, vl.clinic.date_of_enrollment]]
            
        response = JsonResponse(vl_all, safe=False)
        return response
    # self.check_permissions(request=request)
    # queryset = self.get_queryset()
    # data = serializers.serialize('json', queryset.all())
    # return Response(data)