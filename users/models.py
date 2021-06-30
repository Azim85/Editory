from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=16, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Colleague(models.Model):
    fullname = models.CharField(max_length=100)
    profession = models.CharField(max_length=255)
    linkedLn = models.URLField()
    photo = models.ImageField(upload_to='staff/')

    def __str__(self):
        return self.fullname


