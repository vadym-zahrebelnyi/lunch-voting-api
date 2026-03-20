from types import MappingProxyType
from voting.serializers.v1 import VoteResultV1Serializer
from voting.serializers.v2 import VoteResultV2Serializer

VOTE_RESULT_SERIALIZERS = MappingProxyType({
    (1, 0, 0): VoteResultV1Serializer,
    (2, 0, 0): VoteResultV2Serializer,
})
