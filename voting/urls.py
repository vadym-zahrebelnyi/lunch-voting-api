from django.urls import path
from voting.views import CastVoteView, TodayResultsView

app_name = "voting"

urlpatterns = [
    path("", CastVoteView.as_view(), name="vote"),
    path("results/today/", TodayResultsView.as_view(), name="results_today"),
]
