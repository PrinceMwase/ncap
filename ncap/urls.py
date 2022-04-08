from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from ncapp.token import CustomAuthToken


from rest_framework import routers
from ncapp import views as myViews
from ncapp.modelviews.clinic import ClinicViewSet
from ncapp.modelviews.art import ArtViewSet
from ncapp.modelviews.dispensation import DrugDispensationViewSet
from ncapp.modelviews.drug import DrugFillableViewSet
from ncapp.modelviews.dispensation_fillable import DispensationFillableViewSet


router = routers.DefaultRouter()
router.register(r'users', myViews.UserViewSet)
router.register(r'groups', myViews.GroupViewSet)
router.register(r'patients', myViews.PatientViewSet)
router.register(r'visits', ClinicViewSet, basename="visits")
router.register(r'art_dispensation', ArtViewSet, basename="art_dispensation")
router.register(r'drug_dispensation', DrugDispensationViewSet, basename="drug_dispensation")
router.register(r'drug_fillable', DrugFillableViewSet, basename="drug_fillable")
router.register(r'dispensation_fillable', DispensationFillableViewSet, basename="dispensation_fillable")
router.register(r'actors', myViews.ActorViewSet)
router.register(r'nurse', myViews.NurseViewSet)
router.register(r'location', myViews.LocationViewSet)
router.register(r'support_group', myViews.SupportGroupViewSet)
router.register(r'site', myViews.SiteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ncapp/', include('ncapp.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view())
]