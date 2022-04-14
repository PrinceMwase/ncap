from ncapp.models.support_group import SupportGroup
from rest_framework import viewsets
from ncapp.serializers import SupportGroupSerializer
from rest_framework import permissions

class SupportGroupViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows support groups to be viewed or edited.
        """
        queryset = SupportGroup.objects.all()
        serializer_class = SupportGroupSerializer
        permission_classes = [permissions.AllowAny]