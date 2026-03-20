from rest_framework import serializers


class VoteResultV2Serializer(serializers.Serializer):
    """
    Full response for newer app versions.
    Returns a sorted list of all results.
    """
    restaurant = serializers.CharField(source="restaurant.name")
    votes = serializers.IntegerField(source="votes_count")
    menu_items = serializers.JSONField(source="items")
