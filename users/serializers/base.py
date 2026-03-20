from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..services import UserService

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Uses UserService for data manipulation.
    """
    class Meta:
        model = User
        fields = ("id", "email", "password", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5}
        }

    def create(self, validated_data):
        return UserService.create_user(**validated_data)
