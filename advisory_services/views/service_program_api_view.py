
from rest_framework import permissions
from rest_framework import viewsets

from ..models import ServicePrograme
from ..serializers import ServiceProgrameSerializer


class ServiceProgrameViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = ServicePrograme.objects.all()
    serializer_class = ServiceProgrameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]