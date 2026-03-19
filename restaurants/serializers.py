from rest_framework import serializers
from django.utils import timezone
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "items"]

    def validate_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Cannot upload menu for a past date.")
        return value

    def validate_items(self, value):
        if not value or not isinstance(value, list):
            raise serializers.ValidationError("Menu items must be a non-empty list.")
        return value
