
from rest_framework import permissions
from rest_framework import viewsets

from ..models import BioData
from ..serializers import BioDataSerializer


class BioDataViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = BioData.objects.all()
    serializer_class = BioDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]