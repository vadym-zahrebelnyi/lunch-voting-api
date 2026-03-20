from types import MappingProxyType
from .v1 import MenuV1Serializer
from .v2 import MenuV2Serializer

MENU_SERIALIZERS = MappingProxyType({
    (1, 0, 0): MenuV1Serializer,
    (2, 0, 0): MenuV2Serializer,
})
