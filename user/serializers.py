from .models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'department_id', 'email', 'mobile', 'type', 'status', 'timestamp']
