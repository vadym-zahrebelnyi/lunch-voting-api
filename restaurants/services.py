from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Restaurant, Menu


class RestaurantService:
    @staticmethod
    def create_restaurant(name):
        return Restaurant.objects.create(name=name)

    @staticmethod
    def get_all_restaurants():
        return Restaurant.objects.all().order_by("name")

    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        return Restaurant.objects.get(id=restaurant_id)


class MenuService:
    @staticmethod
    def get_today_menus():
        today = timezone.now().date()
        return Menu.objects.filter(date=today).select_related("restaurant")

    @staticmethod
    def upload_menu(restaurant_id, items, date=None):
        if date is None:
            date = timezone.now().date()
            
        # Захист: чи існує ресторан
        if not Restaurant.objects.filter(id=restaurant_id).exists():
            raise ValidationError("Restaurant does not exist.")
            
        existing_menu = Menu.objects.filter(restaurant_id=restaurant_id, date=date).first()
        if existing_menu:
            if existing_menu.votes.exists():
                raise ValidationError("Cannot update menu because voting has already started.")
            existing_menu.items = items
            existing_menu.save()
            return existing_menu
            
        return Menu.objects.create(restaurant_id=restaurant_id, date=date, items=items)
