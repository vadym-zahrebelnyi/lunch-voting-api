from rest_framework import serializers


class VoteResultV1Serializer(serializers.Serializer):
    winner = serializers.CharField(source="restaurant.name")
    votes = serializers.IntegerField(source="votes_count")
