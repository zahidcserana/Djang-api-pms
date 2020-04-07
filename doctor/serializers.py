from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'mobile', 'education', 'title', 'organisation', 'experience', 'location', 'status', 'created_at']
