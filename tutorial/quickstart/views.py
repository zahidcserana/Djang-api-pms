from django.contrib.auth.models import User, Group
from django.db.models import Sum
from rest_framework import viewsets, generics

from appointment.models import AppointmentSerial, DoctorAppointment
from patient.models import Patient, PatientPayment
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Summary(generics.ListAPIView):

    def get(self, request):
        summaryInfo = dict()
        patient = Patient.objects.count()
        serial = AppointmentSerial.objects.count()
        appointment = DoctorAppointment.objects.count()
        payment = list(PatientPayment.objects.aggregate(Sum('amount')).values())[0]

        summaryInfo['patient'] = patient
        summaryInfo['serial'] = serial
        summaryInfo['appointment'] = appointment
        summaryInfo['payment'] = payment
        
        content = {"code": 20000, "data": summaryInfo}
        return Response(content)
