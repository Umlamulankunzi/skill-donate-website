# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """ Create and save a user with the given username, email,

        and password.
        """
        if not email:
            raise ValueError("Please provide a valid email address !")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name=('email address'), unique=True)
    is_volunteer = models.BooleanField(default=False)
    is_charity = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.email.split('@')[0]

    def get_full_name(self):
        """
        calls self.get_short_name
        """
        return self.get_short_name()


class Charity(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,
        related_name='charity')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)

    # Brief description of charity
    # eg charity cares for orphans or maybe for the elderly
    description = models.TextField(
        blank=True,
        help_text="Brief description of charity. For e.g charity "\
        "cares for the elderly")
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default="zimbabwe")
    created_at = models.DateTimeField(default=timezone.now)

    def get_display_name(self):
        """Gets name to display in navbar of website
        """
        display_name = name.split()[0]
        if len(display_name) > 10:
            return f"{display_name[:10]}.."
        return display_name


class Volunteer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,
        related_name='volunteer')
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default="zimbabwe")
    created_at = models.DateTimeField(default=timezone.now)

    def get_display_name(self):
        """Gets name to display in navbar of website
        """
        display_name = self.name.split()[0]
        if len(display_name) > 10:
            return f"{display_name[:10]}.."
        return display_name
