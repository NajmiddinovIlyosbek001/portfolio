from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    rasm = models.ImageField(upload_to="userimages/", null=True, blank=True)