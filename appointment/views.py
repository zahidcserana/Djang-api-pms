from django.http import HttpResponse
from django.utils import timezone
from rest_framework.parsers import FileUploadParser

from .models import AppointmentSerial, DoctorAppointment
from patient.models import Patient
from .serializers import AppointmentSerialSerializer, DoctorAppointmentSerializer
from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
import datetime
import dateutil.parser


class AppointmentSerialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AppointmentSerial.objects.all()
    serializer_class = AppointmentSerialSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'name', 'mobile', 'schedule_time', 'doctor_id', 'created_at', 'status']
    ordering_fields = ['id', 'schedule_time']

    def get_queryset(self):
        queryset = AppointmentSerial.objects.all()
        status = self.request.query_params.get('status')
        schedule_time = self.request.query_params.get('schedule_time')

        if not status:
            queryset = queryset.exclude(status="DELETE")

        # if schedule_time:
        #     d = dateutil.parser.isoparse(schedule_time)
        #     dateTime = d.strftime('%Y-%m-%d %H:%M:%S')
        #     date = datetime.datetime.strptime(dateTime, "%Y-%m-%d  %H:%M:%S").strftime("%Y,%-m,%d")
        #     time = datetime.datetime.strptime(dateTime, "%Y-%m-%d  %H:%M:%S").strftime("%H:%M:%S")
        #     print(d.year, d.month, d.day)
        #     queryset = queryset.filter(schedule_time__date=datetime.date(d.year, d.month, d.day))
        # if time == '00:00:00':
        #     queryset = queryset.filter(schedule_time__date=datetime.date(2020,3,25))
        # else:
        #     queryset = queryset.filter(schedule_time__contains=date)
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


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = DoctorAppointment.objects.all()
    serializer_class = DoctorAppointmentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'name', 'mobile', 'description', 'doctor_id', 'patient_id']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = DoctorAppointment.objects.all()
        reference_mobile = self.request.query_params.get('reference_mobile')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if reference_mobile:
            queryset = queryset.filter(patient__mobile=reference_mobile)
        if date_from and date_to:
            queryset = queryset.filter(created_at__range=(date_from, date_to))
        if date_from and not date_to:
            queryset = queryset.filter(created_at__date=date_from)

        return queryset

    def create(self, request):
        parser_classes = [FileUploadParser]
        data = request.data
        # return HttpResponse(str(data))
        serializer = DoctorAppointmentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            model_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success", "id": model_saved.id}}
        return Response(content)

    def retrieve(self, request, pk=None):
        queryset = DoctorAppointment.objects.all()
        modelData = get_object_or_404(queryset, pk=pk)
        serializer = DoctorAppointmentSerializer(modelData)
        content = {"code": 20000, "data": serializer.data}
        return Response(content)

    def update(self, request, pk=None):
        saved_user = get_object_or_404(DoctorAppointment.objects.all(), pk=pk)
        data = request.data
        serializer = DoctorAppointmentSerializer(
            instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)


class PatientAppointmentView(generics.ListAPIView):
    queryset = DoctorAppointment.objects.all()
    serializer_class = DoctorAppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__id']

    def get(self, request):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)
        serializer = DoctorAppointmentSerializer(filter_backends, many=True)
        content = {"code": 20000, "data": serializer.data}
        return Response(content)
