from .v1 import UserV1Serializer
from .v2 import UserV2Serializer


USER_SERIALIZERS = {
    (1, 0, 0): UserV1Serializer,
    (2, 0, 0): UserV2Serializer,
}
