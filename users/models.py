from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    avatar = models.ImageField(upload_to="avatars", blank=True)
    phone_number = models.IntegerField(default=None)
    birthday = models.DateField(default=None)
    half_money = models.DecimalField(max_digits=9, decimal_places=1)
# Create your models here.
