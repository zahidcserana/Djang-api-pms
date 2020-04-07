from .models import Patient, PatientPayment
from rest_framework import serializers


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'mobile', 'age', 'address', 'gender', 'type', 'status', 'created_at']


class PatientListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'mobile', 'age']


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.IntegerField()

    class Meta:
        model = PatientPayment
        fields = ['id', 'amount', 'description', 'patient', 'patient_id', 'created_at']


class PaymentSearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientPayment
        fields = ['id', 'amount', 'description', 'created_at']
