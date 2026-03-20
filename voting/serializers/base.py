from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from voting.models import Vote
from voting.services import VoteService

class VoteCreateSerializer(serializers.ModelSerializer):
    menu_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vote
        fields = ["id", "menu_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        try:
            return VoteService.cast_vote(
                employee=self.context["request"].user,
                menu_id=validated_data["menu_id"]
            )
        except DjangoValidationError as exc:
            raise DRFValidationError({"detail": exc.message})

class BaseVoteResultSerializer(serializers.Serializer):
    restaurant = serializers.CharField(source="restaurant.name")
    votes = serializers.IntegerField(source="votes_count")
