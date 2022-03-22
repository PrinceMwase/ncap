from django.contrib import admin
from django.urls import include, path

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from ncapp.token import CustomAuthToken


from rest_framework import routers
from ncapp import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'visits', views.CLinicViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('ncapp/', include('ncapp.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthToken.as_view())
]