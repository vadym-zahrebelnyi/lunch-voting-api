from django.db import models


class Restaurant(models.Model):
    """Represents a restaurant available for voting."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """
    Represents a daily menu for a restaurant.
    Ensures only one menu per restaurant per day.
    """

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    date = models.DateField()
    items = models.JSONField(help_text="Structured list of dishes")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["restaurant", "date"], name="unique_restaurant_menu_per_day"
            )
        ]

    def __str__(self):
        return f"{self.restaurant.name} - {self.date}"
