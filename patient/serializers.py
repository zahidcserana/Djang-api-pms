from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'mobile', 'age', 'address', 'gender', 'type', 'status', 'created_at']

class PatientListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'mobile', 'age']
