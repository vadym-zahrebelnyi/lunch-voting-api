from django.urls import path
from .views import RestaurantCreateView, MenuUploadView, CurrentDayMenuView

app_name = "restaurants"

urlpatterns = [
    path("create/", RestaurantCreateView.as_view(), name="create_restaurant"),
    path("menu/upload/", MenuUploadView.as_view(), name="upload_menu"),
    path("menu/today/", CurrentDayMenuView.as_view(), name="today_menu"),
]
