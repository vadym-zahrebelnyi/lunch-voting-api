from rest_framework import serializers
from voting.serializers.base import BaseVoteResultSerializer


class VoteResultV2Serializer(BaseVoteResultSerializer):
    """v2: Full ranked list with menu details."""

    id = serializers.IntegerField()
    date = serializers.DateField()
    items = serializers.JSONField()
