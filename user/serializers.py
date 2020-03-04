from .models import User
from rest_framework import serializers
from setting.serializers import DepartmentSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'department', 'email', 'mobile', 'type', 'status', 'timestamp']
