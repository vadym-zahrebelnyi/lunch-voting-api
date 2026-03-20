from django.utils import timezone
from django.db.models import Count
from restaurants.models import Menu
from voting.models import Vote


class VoteService:
    """Service layer for voting-related operations."""

    @staticmethod
    def get_today_results():
        """Return today's menus annotated with vote counts, ordered by popularity."""
        today = timezone.now().date()
        return (
            Menu.objects.filter(date=today)
            .annotate(votes_count=Count("votes"))
            .select_related("restaurant")
            .order_by("-votes_count")
        )

    @staticmethod
    def cast_vote(employee, menu_id):
        """
        Cast a vote for a menu.

        Ensures the user votes only once per day and the menu is valid for today.
        """
        from django.core.exceptions import ValidationError

        today = timezone.now().date()

        already_voted = Vote.objects.filter(employee=employee, date=today).exists()
        if already_voted:
            raise ValidationError("You have already voted today.")

        try:
            menu = Menu.objects.get(id=menu_id, date=today)
        except Menu.DoesNotExist:
            raise ValidationError("Invalid menu ID or menu is not for today.")

        return Vote.objects.create(employee=employee, menu=menu)

    @staticmethod
    def get_employee_votes(employee):
        """Return all votes made by the given employee."""
        return Vote.objects.filter(employee=employee).select_related("menu__restaurant")
