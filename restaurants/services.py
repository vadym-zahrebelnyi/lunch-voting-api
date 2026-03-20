from django.utils import timezone
from django.core.exceptions import ValidationError
from restaurants.models import Restaurant, Menu


class RestaurantService:
    """Service layer for restaurant-related operations."""

    @staticmethod
    def create_restaurant(name):
        """Create and return a new restaurant."""
        return Restaurant.objects.create(name=name)

    @staticmethod
    def get_all_restaurants():
        """Return all restaurants ordered by name."""
        return Restaurant.objects.all().order_by("name")

    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        """Return a restaurant by its ID."""
        return Restaurant.objects.get(id=restaurant_id)


class MenuService:
    """Service layer for menu-related operations."""

    @staticmethod
    def get_today_menus():
        """Return all menus for today with related restaurants."""
        today = timezone.now().date()
        return Menu.objects.filter(date=today).select_related("restaurant")

    @staticmethod
    def upload_menu(restaurant_id, items, date=None):
        """
        Create or update a menu for a restaurant on a given date.

        - Creates a new menu if it does not exist.
        - Updates existing menu if no votes have been cast yet.
        - Raises ValidationError if restaurant does not exist or voting already started.
        """
        if date is None:
            date = timezone.now().date()

        if not Restaurant.objects.filter(id=restaurant_id).exists():
            raise ValidationError("Restaurant does not exist.")

        existing_menu = Menu.objects.filter(
            restaurant_id=restaurant_id, date=date
        ).first()
        if existing_menu:
            if existing_menu.votes.exists():
                raise ValidationError(
                    "Cannot update menu because voting has already started."
                )
            existing_menu.items = items
            existing_menu.save()
            return existing_menu

        return Menu.objects.create(restaurant_id=restaurant_id, date=date, items=items)
