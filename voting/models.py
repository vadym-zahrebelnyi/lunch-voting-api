from django.conf import settings
from django.db import models
from restaurants.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="votes"
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="votes"
    )
    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "date"],
                name="unique_vote_per_day"
            )
        ]

    def __str__(self):
        return f"{self.employee.email} voted for {self.menu.restaurant.name} on {self.date}"
