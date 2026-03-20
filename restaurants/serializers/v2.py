from rest_framework import serializers


class MenuV2Serializer(serializers.Serializer):
    """
    Detailed menu representation for modern apps.
    """
    id = serializers.IntegerField()
    restaurant_id = serializers.IntegerField(source="restaurant.id")
    restaurant_name = serializers.CharField(source="restaurant.name")
    menu_items = serializers.JSONField(source="items")
    date = serializers.DateField()
    last_updated = serializers.SerializerMethodField()

    def get_last_updated(self, obj):
        # Additional field for v2
        return obj.date.strftime("%Y-%m-%d")
    
    # Not inheriting from V1 as structure differs for clarity
