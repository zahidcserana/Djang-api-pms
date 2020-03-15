from .models import AppointmentSerial, DoctorAppointment
from rest_framework import serializers
from patient.serializers import PatientSerializer


class AppointmentSerialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AppointmentSerial
        fields = ['id', 'schedule_time', 'name', 'mobile', 'status', 'created_at']


class DoctorAppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.IntegerField()

    class Meta:
        model = DoctorAppointment
        fields = ['id', 'description', 'patient', 'patient_id', 'created_at']
