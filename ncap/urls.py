from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ncapp/', include('ncapp.urls')),
    path('admin/', admin.site.urls),
]