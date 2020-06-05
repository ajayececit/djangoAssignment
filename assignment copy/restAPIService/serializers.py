from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=120)
    lastName = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
