from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from core.mixins import VersionedSerializerMixin
from restaurants.serializers.versions import MENU_SERIALIZERS
from restaurants.serializers.base import RestaurantSerializer, MenuUploadSerializer
from restaurants.services import RestaurantService, MenuService


@extend_schema(
    summary="List all restaurants or create a new one",
    description="GET returns all restaurants. POST creates a new restaurant (Admin only).",
    responses={200: RestaurantSerializer(many=True)},
)
class RestaurantViewSet(generics.ListCreateAPIView):
    """
    GET /api/restaurants/ - List all restaurants.
    POST /api/restaurants/ - Create a restaurant (Admin only).
    """

    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return RestaurantService.get_all_restaurants()

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


@extend_schema(
    summary="Get today's menus",
    description=(
        "Returns all menus for today. Response format is versioned based on "
        "the `X-App-Version` header."
    ),
    parameters=[
        OpenApiParameter(
            name="X-App-Version",
            description="Semantic version of the client app, e.g., 1.0.0, 2.0.0",
            required=False,
            type=str,
            examples=[
                OpenApiExample(name="v1", value="1.0.0"),
                OpenApiExample(name="v2", value="2.0.0"),
            ],
            location="header",
        )
    ],
    responses={200: "Versioned response depends on X-App-Version"},
)
class TodayMenusView(VersionedSerializerMixin, generics.ListAPIView):
    """
    GET /api/restaurants/today/
    Returns all today's menus. Response format is versioned.
    """

    versioned_serializers = MENU_SERIALIZERS

    def get_queryset(self):
        return MenuService.get_today_menus()


@extend_schema(
    summary="Upload a menu for a restaurant",
    description="Uploads today's menu for a specific restaurant (Admin only).",
    request=MenuUploadSerializer,
    responses={201: MenuUploadSerializer},
)
class MenuUploadView(generics.CreateAPIView):
    """
    POST /api/restaurants/{id}/menus/
    Uploads menu for a specific restaurant for today (Admin only).
    """

    permission_classes = [permissions.IsAdminUser]
    serializer_class = MenuUploadSerializer

    def perform_create(self, serializer):
        serializer.save(restaurant_id=self.kwargs["id"])
