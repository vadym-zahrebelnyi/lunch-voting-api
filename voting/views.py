from rest_framework import generics
from core.mixins import VersionedSerializerMixin
from voting.serializers.versions import VOTE_RESULT_SERIALIZERS
from voting.serializers.base import VoteCreateSerializer
from voting.services import VoteService


class TodayResultsView(VersionedSerializerMixin, generics.ListAPIView):
    """Return today's voting results with versioned response format."""

    versioned_serializers = VOTE_RESULT_SERIALIZERS

    def get_queryset(self):
        """Fetch today's voting results."""
        return VoteService.get_today_results()


class CastVoteView(generics.CreateAPIView):
    """Allow authenticated users to cast a vote."""

    serializer_class = VoteCreateSerializer
