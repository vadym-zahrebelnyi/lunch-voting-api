from rest_framework import generics
from core.mixins import VersionedSerializerMixin
from .serializers.versions import VOTE_RESULT_SERIALIZERS
from .serializers.base import VoteCreateSerializer
from .services import VoteService


class TodayResultsView(VersionedSerializerMixin, generics.ListAPIView):
    """
    GET /api/votes/results/today/
    """
    versioned_serializers = VOTE_RESULT_SERIALIZERS

    def get_queryset(self):
        return VoteService.get_today_results()


class CastVoteView(generics.CreateAPIView):
    """
    POST /api/votes/
    """
    serializer_class = VoteCreateSerializer
