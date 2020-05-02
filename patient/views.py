from django.db.models import Sum
from rest_framework.utils import json

from appointment.models import DoctorAppointment
from appointment.serializers import DoctorAppointmentSerializer
from .models import Patient, PatientPayment
from .serializers import PatientSerializer, PatientListSerializer, PaymentSerializer, PaymentSearchSerializer, \
    PatientAddSerializer
from rest_framework import viewsets, request, status, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from django.http import HttpResponse


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'email', 'mobile', 'status', 'type', 'gender']
    ordering_fields = ['id', 'name']

    def get_queryset(self):
        queryset = Patient.objects.all()
        status = self.request.query_params.get('status')
        name = self.request.query_params.get('name')
        if not status:
            queryset = queryset.exclude(status="DELETE")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def retrieve(self, request, pk=None):
        queryset = Patient.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = PatientSerializer(patient)

        content = {"code": 20000, "data": serializer.data}
        return Response(content)

    def create(self, request):
        data = request.data
        serializer = PatientAddSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            Patient_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)

    def update(self, request, pk=None):
        saved_Patient = get_object_or_404(Patient.objects.all(), pk=pk)
        data = request.data
        serializer = PatientSerializer(
            instance=saved_Patient, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            Patient_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = PatientPayment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'patient__id']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = PatientPayment.objects.all()
        patient_id = self.request.query_params.get('patient_id')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if patient_id:
            queryset = queryset.filter(patient__id=patient_id)

        if date_from and date_to:
            queryset = queryset.filter(created_at__range=(date_from, date_to))
        if date_from and not date_to:
            queryset = queryset.filter(created_at__date=date_from)

        return queryset

    def retrieve(self, request, pk=None):
        queryset = PatientPayment.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = PaymentSerializer(patient)
        content = {"code": 20000, "data": serializer.data}
        return Response(content)

    def create(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)

    def update(self, request, pk=None):
        model_data = get_object_or_404(PatientPayment.objects.all(), pk=pk)
        data = request.data
        serializer = PaymentSerializer(
            instance=model_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)


class PatientSearchView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'mobile']

    def get(self, request):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)
        serializer = PatientListSerializer(filter_backends, many=True)
        content = {"code": 20000, "data": serializer.data}
        return Response(content)


class PaymentSearchView(generics.ListAPIView):
    queryset = PatientPayment.objects.all()
    serializer_class = PaymentSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__id']

    def get(self, request):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)
        serializer = PaymentSearchSerializer(filter_backends, many=True)
        search = self.request.query_params.get('search')
        payment = list(PatientPayment.objects.filter(patient_id=search).aggregate(Sum('amount')).values())[0]
        content = {"code": 20000, "data": serializer.data, "payment": payment}
        return Response(content)


class Summary(generics.ListAPIView):

    def get(self, request, pk=None):
        summary = dict()
        summary['payment'] = list(PatientPayment.objects.filter(patient_id=pk).aggregate(Sum('amount')).values())[0]
        summary['appointment'] = DoctorAppointment.objects.filter(patient_id=pk).count()

        d_appoint = DoctorAppointment.objects.filter(patient__id=pk).last()
        if d_appoint:
            d_appoint.created_at = d_appoint.created_at.strftime("%Y-%m-%d")
            summary['last_appointment'] = d_appoint.created_at

        # appoint_data = DoctorAppointmentSerializer(d_appoint)

        content = {"code": 20000, "data": summary}
        return Response(content)
