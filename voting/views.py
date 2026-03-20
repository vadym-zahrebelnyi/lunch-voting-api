from rest_framework import generics
from core.mixins import VersionedSerializerMixin
from voting.serializers.versions import VOTE_RESULT_SERIALIZERS
from voting.serializers.base import VoteCreateSerializer
from voting.services import VoteService


class TodayResultsView(VersionedSerializerMixin, generics.ListAPIView):
    versioned_serializers = VOTE_RESULT_SERIALIZERS

    def get_queryset(self):
        return VoteService.get_today_results()


class CastVoteView(generics.CreateAPIView):
    serializer_class = VoteCreateSerializer
