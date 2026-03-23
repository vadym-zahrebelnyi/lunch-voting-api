from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from restaurants.models import Restaurant, Menu
from restaurants.services import MenuService


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]


class BaseMenuSerializer(serializers.Serializer):
    """Base serializer for common menu fields."""

    id = serializers.IntegerField()
    restaurant = serializers.CharField(source="restaurant.name")
    date = serializers.DateField()
    items = serializers.JSONField()


class MenuUploadSerializer(serializers.ModelSerializer):
    """
    Serializer used for uploading/updating a menu.
    Takes restaurant_id from validated_data (passed from view.save()).
    """

    class Meta:
        model = Menu
        fields = ["items"]

    def validate_items(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("Menu items must be a non-empty list.")
        return value

    def create(self, validated_data):
        try:
            return MenuService.upload_menu(
                restaurant_id=validated_data["restaurant_id"],
                items=validated_data["items"],
            )
        except DjangoValidationError as exc:
            raise DRFValidationError({"detail": exc.message})
