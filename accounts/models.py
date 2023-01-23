from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class CustomRegistrationModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
