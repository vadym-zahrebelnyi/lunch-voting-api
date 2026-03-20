from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema, OpenApiExample

from users.serializers.base import UserSerializer
from users.services import UserService


@extend_schema(
    description="Register a new user. Public endpoint, no authentication required.",
    examples=[
        OpenApiExample(
            "Register Example",
            value={
                "email": "user@example.com",
                "password": "strongpassword123",
                "first_name": "John",
                "last_name": "Doe"
            },
            request_only=True,
        ),
        OpenApiExample(
            "Register Response Example",
            value={
                "id": 1,
                "email": "user@example.com",
                "first_name": "John",
                "last_name": "Doe"
            },
            response_only=True,
        ),
    ],
)
class CreateUserView(generics.CreateAPIView):
    """
    POST /api/auth/register/
    Public endpoint for user registration.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    description="Retrieve or update the authenticated user's profile.",
    examples=[
        OpenApiExample(
            "Get User Profile Example",
            value={
                "id": 1,
                "email": "user@example.com",
                "first_name": "John",
                "last_name": "Doe"
            },
            response_only=True,
        ),
        OpenApiExample(
            "Update User Profile Example",
            value={"first_name": "Jane", "last_name": "Doe"},
            request_only=True,
        ),
    ],
)
class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    GET, PUT, PATCH /api/users/me/
    Retrieve or update the authenticated user's profile.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        UserService.update_user(self.get_object(), **serializer.validated_data)
