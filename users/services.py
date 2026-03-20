from django.contrib.auth import get_user_model

User = get_user_model()


class UserService:
    """Service layer for user-related operations."""

    @staticmethod
    def create_user(email, password, **extra_fields):
        """Create and return a new user."""
        return User.objects.create_user(email=email, password=password, **extra_fields)

    @staticmethod
    def update_user(user, **validated_data):
        """
        Update user fields and handle password change if provided.
        """
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(user, attr, value)
        if password:
            user.set_password(password)
        user.save()
        return user
