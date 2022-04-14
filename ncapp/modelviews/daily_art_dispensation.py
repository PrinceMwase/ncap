from datetime import date
from ncapp.models.art import Art
from django.core import serializers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse
from ncapp.serializers import VlSerializer
from tabular_export.core import export_to_excel_response
from django.utils import timezone
import pandas as pd
from openpyxl import load_workbook

class ARTDispensingViewSet(viewsets.ViewSet):
    """
    Generate Daily Nurse art dispensation 
    """

    queryset = Art.objects.filter(created_at=date.today())
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset

    def list(self, request):
        art_total = []
        for i, art in enumerate(self.get_queryset().select_related('clinic', 'art_given', 'clinic__patient')):
            art_total += [[i, art.clinic.patient.__str__(), art.clinic.patient.sex,
                           art.clinic.art_number, art.clinic.file_number, art.wt,
                           art.ht, art.sbp_dbp, art.side_effect,
                           art.tb_status, art.dose_missed, art.pill_count,
                           art.art_given.name, art.number_of_regimen_pills,
                           art.pyridoxine, art.inh, art.bp_drug,
                           art.number_of_tabs, art.fp_meth, art.number_of_condoms,
                           art.adverse_outcome]]
        workbook = load_workbook('./daily_art.xlsx')
        headers = ['ID', 'Patient', 'Sex', 'ART Number', 'File Number', 'wt',
                'ht', 'sbp dbp', 'side effect', 'tb status', 'dose missed', 'pill count', 'regimen', '# of regimen pills', 
                'pyridoxine', 'inh' , 'bp drug', 'number of tabs', 'fp meth', 'number of condoms', 'adverse outcome'
                ]
        print(workbook)
        excel = export_to_excel_response(
            'art%s.xlsx' % timezone.datetime.today(), headers, art_total)
        return 1
