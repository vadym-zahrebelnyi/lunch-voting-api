from django.urls import path
from voting.views import CastVoteView, TodayResultsView

app_name = "voting"

urlpatterns = [
    # POST /api/votes/
    path("", CastVoteView.as_view(), name="vote"),
    # GET /api/votes/results/today/
    path("results/today/", TodayResultsView.as_view(), name="results_today"),
]
