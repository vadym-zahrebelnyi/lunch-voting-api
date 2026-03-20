from django.urls import path
from .views import (
    RestaurantViewSet, 
    MenuUploadView,
)

app_name = "restaurants"

urlpatterns = [
    # Creating restaurant (POST) and list (GET)
    path("", RestaurantViewSet.as_view(), name="restaurant_list_create"),
    
    # Menu upload for a specific restaurant
    path("<int:id>/menus/", MenuUploadView.as_view(), name="upload_menu"),
]
