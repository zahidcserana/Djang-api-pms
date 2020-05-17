from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from user.models import Profile


class ProfileSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    department = serializers.CharField(max_length=100)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'profile']

    def validate(self, data):
        return data

    def create(self, validated_data):
        profile_data = validated_data.get('profile')
        del validated_data['profile']

        instance = self.Meta.model(**validated_data)
        instance.set_password(self.initial_data['password'])
        instance.is_active = True
        instance.save()

        if profile_data:
            profile_data = dict(profile_data)
            instance.profile.mobile = profile_data['mobile']
            instance.profile.department = profile_data['department']
            instance.profile.save()

        return instance

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        profile_data = validated_data.get('profile')
        if profile_data:
            profile_data = dict(profile_data)
            instance.profile.mobile = profile_data['mobile']
            instance.profile.department = profile_data['department']
            instance.profile.save()

        return instance
