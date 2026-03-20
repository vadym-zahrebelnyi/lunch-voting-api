from rest_framework import generics, permissions
from users.serializers.base import UserSerializer
from users.services import UserService


class CreateUserView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    PUBLIC endpoint for registration.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    GET, PUT, PATCH /api/users/me/
    Returns or updates the authenticated user's profile.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        UserService.update_user(self.get_object(), **serializer.validated_data)
