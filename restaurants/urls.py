from django.urls import path
from restaurants.views import (
    RestaurantViewSet,
    MenuUploadView,
    TodayMenusView
)

app_name = "restaurants"

urlpatterns = [
    path("", RestaurantViewSet.as_view(), name="restaurant_list_create"),
    path("<int:id>/menus/", MenuUploadView.as_view(), name="upload_menu"),
    path("today/", TodayMenusView.as_view(), name="restaurants_menus_today")
]
