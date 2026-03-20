from rest_framework import serializers


class MenuV1Serializer(serializers.Serializer):
    """
    Compact menu representation for older apps.
    """
    id = serializers.IntegerField()
    restaurant = serializers.CharField(source="restaurant.name")
    items = serializers.JSONField()
    date = serializers.DateField()
