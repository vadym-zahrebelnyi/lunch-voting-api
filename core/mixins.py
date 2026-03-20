from typing import Mapping, Tuple, Type
from rest_framework import serializers
from types import MappingProxyType

from django.core.exceptions import ImproperlyConfigured


class VersionedSerializerMixin:
    versioned_serializers: Mapping[
        Tuple[int, int, int], Type[serializers.Serializer]
    ] = MappingProxyType({})

    def get_serializer_class(self):
        if not self.versioned_serializers:
            raise ImproperlyConfigured("versioned_serializers must be defined")

        version = getattr(self.request, "version", (1, 0, 0))

        for v in sorted(self.versioned_serializers.keys(), reverse=True):
            if version >= v:
                return self.versioned_serializers[v]

        return self.versioned_serializers[min(self.versioned_serializers)]
