from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from core.mixins import VersionedSerializerMixin
from voting.serializers.versions import VOTE_RESULT_SERIALIZERS
from voting.serializers.base import VoteCreateSerializer
from voting.services import VoteService


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="X-App-Version",
            description="Semantic version of the client app, e.g., 1.0.0, 2.0.0",
            required=False,
            type=str,
            examples=[
                OpenApiExample(name="v1", value="1.0.0"),
                OpenApiExample(name="v2", value="2.0.0"),
            ],
            location="header",
        )
    ],
    description="Retrieve today's voting results. Response is versioned depending on the X-App-Version header.",
)
class TodayResultsView(VersionedSerializerMixin, generics.ListAPIView):
    """Return today's voting results with versioned response format."""

    versioned_serializers = VOTE_RESULT_SERIALIZERS

    def get_queryset(self):
        """Fetch today's voting results."""
        return VoteService.get_today_results()


@extend_schema(description="Allow authenticated users to cast a vote for today's menu.")
class CastVoteView(generics.CreateAPIView):
    """Allow authenticated users to cast a vote."""

    serializer_class = VoteCreateSerializer
