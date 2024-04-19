from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "address",
            "phone_no",
            "image",
            "password1",
            "password2",
        ]


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "address",
            "phone_no",
            "image",
        ]
