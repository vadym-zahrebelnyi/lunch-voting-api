from rest_framework import generics, permissions
from django.utils import timezone
from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer


class RestaurantCreateView(generics.CreateAPIView):
    """
    Endpoint for creating a restaurant.
    Only admin users should be allowed to create restaurants.
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAdminUser]


class MenuUploadView(generics.CreateAPIView):
    """
    Endpoint for uploading a menu for a restaurant.
    Only admin users should be allowed to upload menus.
    """

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAdminUser]


class CurrentDayMenuView(generics.ListAPIView):
    """
    Endpoint for getting current day menu for all restaurants.
    Any authenticated user can view today's menu.
    """

    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = timezone.now().date()
        return Menu.objects.filter(date=today)
