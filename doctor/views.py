from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import viewsets, request, status, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from django.http import HttpResponse


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['id', 'email', 'mobile', 'status']
    ordering_fields = ['id', 'name']

    def get_queryset(self):
        queryset = Doctor.objects.all()
        status = self.request.query_params.get('status')
        name = self.request.query_params.get('name')

        if not status:
            queryset = queryset.exclude(status="DELETE")
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def retrieve(self, request, pk=None):
        queryset = Doctor.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = DoctorSerializer(patient)
        content = {"code": 20000, "data": serializer.data}
        return Response(content)

    def create(self, request):
        data = request.data
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            Doctor_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)

    def update(self, request, pk=None):
        saved_Doctor = get_object_or_404(Doctor.objects.all(), pk=pk)
        data = request.data
        serializer = DoctorSerializer(
            instance=saved_Doctor, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            Doctor_saved = serializer.save()
            content = {"code": 20000, "data": {"status": "success"}}
        return Response(content)
