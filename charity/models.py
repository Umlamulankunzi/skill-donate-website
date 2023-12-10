from django.db import models
from django.utils import timezone
from app_auth.models import Charity


# Create your models here.

from django.db import models

class SkillRequired(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(
        blank=True,
        help_text="Please provide a brief description of skill required")
    created_at = models.DateTimeField(default=timezone.now)


class InterestInSkillDonated(models.Model):
    skill_donated = models.ForeignKey("volunteer.SkillDonated", on_delete=models.CASCADE, related_name='skill_donated')
    Charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='charity')
    created_at = models.DateTimeField(default=timezone.now)
