from rest_framework import serializers
from django.utils import timezone
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "menu", "date"]
        read_only_fields = ["id", "date"]

    def validate_menu(self, value):
        """
        Check that the employee is voting for today's menu.
        """
        today = timezone.now().date()
        if value.date != today:
            raise serializers.ValidationError("You can only vote for today's menu.")
        return value

    def validate(self, attrs):
        """
        Check if the employee has already voted today.
        """
        request = self.context.get("request")
        if request and request.user:
            today = timezone.now().date()
            if Vote.objects.filter(employee=request.user, date=today).exists():
                raise serializers.ValidationError("You have already voted today.")

        return attrs

    def create(self, validated_data):
        """
        Set the employee from the request user.
        """
        validated_data["employee"] = self.context["request"].user
        return super().create(validated_data)
