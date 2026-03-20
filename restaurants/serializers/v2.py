from rest_framework import serializers
from restaurants.serializers.base import BaseMenuSerializer

class MenuV2Serializer(BaseMenuSerializer):
    """v2: Adds last_updated for clarity."""

    last_updated = serializers.DateField(source="date")
