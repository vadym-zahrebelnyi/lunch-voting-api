from django.utils import timezone
from django.db.models import Count
from restaurants.models import Menu
from voting.models import Vote


class VoteService:
    @staticmethod
    def get_today_results():
        today = timezone.now().date()
        return (
            Menu.objects.filter(date=today)
            .annotate(votes_count=Count("votes")) # Унікальне ім'я
            .select_related("restaurant")
            .order_by("-votes_count")
        )

    @staticmethod
    def cast_vote(employee, menu_id):
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
        return Vote.objects.filter(employee=employee).select_related("menu__restaurant")
