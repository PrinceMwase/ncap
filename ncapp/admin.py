from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django_seed import Seed
from django.shortcuts import get_object_or_404

from ncapp.models.location import Location
from ncapp.models.actor import Actor
from ncapp.models.patient import Patient
from ncapp.models.nurse import Nurse
from ncapp.models.site import Site
from ncapp.models.regimen import Regimen
from ncapp.models.support_group import SupportGroup
from ncapp.models.clinic import Clinic
from ncapp.models.viral_load import ViralLoad
from ncapp.models.drug_fillable import DrugFillable 
from ncapp.models.stock import Stock 

from ncapp.models.dispensation_fillable import DispensationFillable
from ncapp.models.drug_dispensation import DrugDispensation
from ncapp.models.art import Art


from ncapp.models.filters.clinicNurseListFilter import CLinicNurseListFilter
# Model actions

@admin.action(description='Generate Art daily dispensation form')
def generate_art_daily(modeladmin, request, queryset):
    """generate Nurse Art Dispensations"""
    
    art_total = []
    for i, art in enumerate (queryset.select_related('clinic', 'art_given', 'clinic__patient'  )):
        art_total += [[i, art.clinic.patient.__str__(), art.clinic.patient.sex, \
            art.clinic.art_number, art.clinic.file_number, art.wt, \
            art.ht, art.sbp_dbp, art.side_effect, \
            art.tb_status, art.dose_missed, art.pill_count, \
            art.art_given.name, art.number_of_regimen_pills, \
            art.pyridoxine, art.inh, art.bp_drug, \
            art.number_of_tabs, art.fp_meth, art.number_of_condoms, \
            art.adverse_outcome]]
        
    response = JsonResponse(art_total, safe=False)
    return response



@admin.action(description='generate viral load monitoring')
def viral_load_monitoring(modeladmin, request, queryset):
    """generate viral load monitoring"""
    vl_all = []
    for i , vl in enumerate( queryset.select_related('clinic')  ):
        vl_all += [[ i, vl.clinic.patient.__str__(), vl.clinic.patient.sex, \
            vl.clinic.art_number, vl.clinic.file_number, \
            vl.clinic.initiation_date, vl.vl_date, vl.result, vl.regimen.__str__(), \
            vl.clinic.cpt, vl.clinic.date_of_enrollment]]
        
    response = JsonResponse(vl_all, safe=False)
    return response

@admin.action(description= "daily Drug Dispensation")
def nurse_drug_dispesation(model_admin, request, queryset):
    """nurses daily drug dispensation form"""
    dis_all = []
    for i, dis in enumerate(queryset.select_related('nurse')):
        # for y in DispensationFillable.objects.filter(dispensation=dis.pk).all().values()[:]
        print(dis.drugs.all().distinct().values('name')[:])
        print( "%s" % filter(lambda x : x['name'] == x['name'] ,   
                  dis.drugs.all().distinct().values('name')[:]  )
                 )
      
        dis_all += [ 
          [
            i, 
            dis.nurse.__str__(), 
            
            [ (x['name'], get_object_or_404(DispensationFillable, dispensation=dis.pk, fillable=x["id"]).count  ) for 
                x in 
            [ 
                x
                 for x in dis.drugs.all().values()[:]  
                 
            ]]  
         ]
        ]
    response = JsonResponse(dis_all, safe=False)
    return response


# Register your models here.
class ViralLoadAdmin(admin.ModelAdmin):
    list_filter = ['vl_date']
    list_display = ['clinic','vl_date', 'remark']
    actions = [ viral_load_monitoring]
    date_hierarchy = 'vl_date'



class ClinicAdmin(admin.ModelAdmin):    
    list_display = ['art_number','visit_date', 'nurse']
    list_filter = ('visit_date', CLinicNurseListFilter)
    search_fields = ['art_number']

class NurseAdmin(admin.ModelAdmin):
    pass

class DispensationAdmin(admin.ModelAdmin):
    list_display =['nurse', 'dis_date', ]
    list_filter = ['dis_date']
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    actions = [nurse_drug_dispesation]

class ArtAdmin ( admin.ModelAdmin):
    fieldsets = [
        ('Clinic Session', {'fields': ['clinic']}),
        ('ART Dispensation' , {'fields': [
            'wt',
            'ht',
            'sbp_dbp',
            'side_effect',
            'tb_status',
            'dose_missed',
            'pill_count',
            'art_given',
            'number_of_regimen_pills',
            'pyridoxine',
            'inh',
            'bp_drug',
            'number_of_tabs',
            'fp_meth',
            'number_of_condoms',
            'adverse_outcome',
        ] })
    ]
    actions = [generate_art_daily]
    list_filter = ['clinic']
        

admin.site.register(Location)
admin.site.register(Actor)
admin.site.register(Patient)
admin.site.register(SupportGroup)
admin.site.register(Site)
admin.site.register(Regimen)
admin.site.register(Nurse, NurseAdmin )
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(ViralLoad, ViralLoadAdmin)
admin.site.register(DrugFillable)
admin.site.register(DrugDispensation, DispensationAdmin)
admin.site.register(DispensationFillable)
admin.site.register(Art, ArtAdmin)
admin.site.register(Stock)