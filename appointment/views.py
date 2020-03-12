from .models import AppointmentSerial
from patient.models import Patient
from .serializers import AppointmentSerialSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404


class AppointmentSerialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AppointmentSerial.objects.all()
    serializer_class = AppointmentSerialSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'name', 'mobile', 'schedule_time', 'created_at', 'status']
    ordering_fields = ['id', 'schedule_time']

    def get_queryset(self):
        queryset = AppointmentSerial.objects.all()
        status = self.request.query_params.get('status')

        if not status:
            queryset = queryset.exclude(status="DELETE")

        return queryset

    def create(self, request):
        data = request.data
        serializer = AppointmentSerialSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)

    def update(self, request, pk=None):
        saved_user = get_object_or_404(AppointmentSerial.objects.all(), pk=pk)
        data = request.data
        # department_id = request.data.get('department_id')
        # department = get_object_or_404(Department.objects.all(), pk=department_id)
        # return HttpResponse(str(department))
        serializer = AppointmentSerialSerializer(
            instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)