from django.db.models import Count
from django.utils import timezone
from rest_framework import generics, permissions
from restaurants.models import Menu
from restaurants.serializers import MenuSerializer
from .models import Vote
from .serializers import VoteSerializer


class VoteCreateView(generics.CreateAPIView):
    """
    Endpoint for voting for a menu.
    Any authenticated employee can vote once per day.
    """

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodayResultsView(generics.ListAPIView):
    """
    Endpoint for getting current day results.
    Lists today's menus with their vote counts.
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = timezone.now().date()
        # Get today's menus and annotate each with the count of its votes
        return Menu.objects.filter(date=today).annotate(votes_count=Count("votes"))
