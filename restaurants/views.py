from rest_framework import generics, permissions
from core.mixins import VersionedSerializerMixin
from restaurants.serializers.versions import MENU_SERIALIZERS
from restaurants.serializers.base import RestaurantSerializer, MenuUploadSerializer
from restaurants.services import RestaurantService, MenuService


class RestaurantViewSet(generics.ListCreateAPIView):
    """
    GET /api/restaurants/ - List all restaurants.
    POST /api/restaurants/ - Create a restaurant (Admin only).
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return RestaurantService.get_all_restaurants()

    def get_permissions(self):
        # Allow any authenticated user for GET, but only admin for POST
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class TodayMenusView(VersionedSerializerMixin, generics.ListAPIView):
    """
    GET /api/menus/today/
    Returns all today's menus. Response format is versioned.
    """
    versioned_serializers = MENU_SERIALIZERS

    def get_queryset(self):
        return MenuService.get_today_menus()


class MenuUploadView(generics.CreateAPIView):
    """
    POST /api/restaurants/{id}/menus/
    Uploads menu for a specific restaurant for today (Admin only).
    """

    permission_classes = [permissions.IsAdminUser]
    serializer_class = MenuUploadSerializer

    def perform_create(self, serializer):
        # We pass the restaurant_id from the URL to the service
        serializer.save(restaurant_id=self.kwargs["id"])
