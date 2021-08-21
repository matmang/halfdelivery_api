from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):

    avatar = models.ImageField(upload_to="avatars", blank=True)
    phone_number = models.IntegerField(default=0)
    birthday = models.DateField(default=now())
    half_money = models.DecimalField(max_digits=9, decimal_places=1, default=0)
# Create your models here.
