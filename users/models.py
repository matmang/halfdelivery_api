from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    avatar = models.ImageField(upload_to="avatars", blank=True)
    phone_number = models.CharField(max_length=13);
    birthday = models.DateField(auto_now_add=True)
    half_money = models.DecimalField(max_digits=9, decimal_places=1, default=0)
# Create your models here.
