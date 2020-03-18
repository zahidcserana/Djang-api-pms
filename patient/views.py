from .models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets, request, status, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from django.http import HttpResponse


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'name', 'email', 'mobile', 'status', 'type']
    ordering_fields = ['id', 'name']

    def get_queryset(self):
        queryset = Patient.objects.all()
        status = self.request.query_params.get('status')
        if not status:
            queryset = queryset.exclude(status="DELETE")
        return queryset

    def retrieve(self, request, pk=None):
        queryset = Patient.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = PatientSerializer(patient)
        content = {"code": 20000, "data": serializer.data}
        return Response(content)

    def create(self, request):
        data = request.data
        serializer = PatientSerializer(data=data)
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
