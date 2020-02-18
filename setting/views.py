from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
