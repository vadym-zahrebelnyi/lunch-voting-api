from rest_framework import serializers
from ..models import Restaurant, Menu
from ..services import MenuService


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]


class MenuUploadSerializer(serializers.ModelSerializer):
    """
    Serializer for uploading menu.
    Does not depend on Django ORM directly.
    """
    restaurant_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Menu
        fields = ["id", "restaurant_id", "items"]
        read_only_fields = ["id"]

    def validate_items(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("Menu items must be a non-empty list.")
        return value

    def create(self, validated_data):
        return MenuService.upload_menu(
            restaurant_id=validated_data['restaurant_id'],
            items=validated_data['items']
        )
