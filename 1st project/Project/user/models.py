from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    native_name = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=11)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="Profile_images", blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone_no"]

    def __str__(self):
        return "{}".format(self.email)