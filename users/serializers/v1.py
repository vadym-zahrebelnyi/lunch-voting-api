from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserV1Serializer(serializers.ModelSerializer):
    """
    Standard user profile representation for v1.
    """
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", "is_staff")
        read_only_fields = ("id", "is_staff")
