from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from ..models import Vote
from ..services import VoteService


class VoteCreateSerializer(serializers.ModelSerializer):
    """
    Non-versioned serializer for creating votes.
    Delegates business logic and validation to VoteService.
    """
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


class MyVoteHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for viewing own vote history.
    """
    restaurant_name = serializers.CharField(source="menu.restaurant.name")
    
    class Meta:
        model = Vote
        fields = ["id", "menu", "restaurant_name", "date"]
