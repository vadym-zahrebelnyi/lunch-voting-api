from rest_framework import serializers
from .base import BaseMenuSerializer

class MenuV2Serializer(BaseMenuSerializer):
    """v2: Adds last_updated for clarity."""

    last_updated = serializers.DateField(source="date")
