from rest_framework import generics, permissions
from core.mixins import VersionedSerializerMixin
from .serializers.versions import USER_SERIALIZERS
from .serializers.base import RegisterSerializer
from .services import UserService


class CreateUserView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    PUBLIC endpoint for registration.
    """
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ManageUserView(VersionedSerializerMixin, generics.RetrieveUpdateAPIView):
    """
    GET, PUT, PATCH /api/users/me/
    Returns or updates the authenticated user's profile.
    Response format is versioned for GET requests.
    """
    permission_classes = [permissions.IsAuthenticated]
    versioned_serializers = USER_SERIALIZERS

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        UserService.update_user(self.get_object(), **serializer.validated_data)
