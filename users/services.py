from django.contrib.auth import get_user_model

User = get_user_model()


class UserService:
    @staticmethod
    def create_user(email, password, **extra_fields):
        return User.objects.create_user(email=email, password=password, **extra_fields)

    @staticmethod
    def update_user(user, **validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(user, attr, value)
        if password:
            user.set_password(password)
        user.save()
        return user
