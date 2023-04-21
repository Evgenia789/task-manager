from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    A custom user model with additional fields for first name,
    last name, role, date of birth and phone.

    Attributes:
    first_name (str): A string representing the user's first name.
    last_name (str): A string representing the user's last name.
    role (str):A string representing the user's role.
    email (str): A string representing the user's email address.
    date_of_birth (date): A string representing the user's date of birth
    phone (str): A string representing the user's phone
    """

    class Roles(models.TextChoices):
        ADMIN = "admin"
        MANAGER = "manager"
        DEVELOPER = "developer"

    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    role = models.CharField(
        max_length=255, choices=Roles.choices, default=Roles.DEVELOPER
    )
    email = models.EmailField(unique=True, null=True, blank=False)
    date_of_birth = models.DateField(null=True, blank=False)
    phone = models.CharField(max_length=30, null=True, blank=False)
