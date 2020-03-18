from .models import User
from rest_framework import serializers
from setting.serializers import DepartmentSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'name', 'department', 'department_id', 'email', 'mobile', 'type', 'status', 'timestamp']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.status = validated_data.get('status', instance.status)
        instance.type = validated_data.get('type', instance.type)
        instance.department_id = validated_data.get('department_id', instance.department_id)

        instance.save()
        return instance
