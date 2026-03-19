from django.urls import path
from .views import VoteCreateView, TodayResultsView

app_name = "voting"

urlpatterns = [
    path("vote/", VoteCreateView.as_view(), name="vote"),
    path("results/", TodayResultsView.as_view(), name="results"),
]
