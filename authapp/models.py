from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractUser):
    user_type1 = models.BooleanField(default=False)
    user_type2 = models.BooleanField(default=False)
    user_type3 = models.BooleanField(default=False)
