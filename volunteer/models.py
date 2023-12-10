from django.db import models
from django.utils import timezone
from app_auth.models import Volunteer



# Create your models here.
class SkillDonated(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name="volunteer_donator")
    skill_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(
        blank=True,
        help_text="Please provide a brief description of skill you want to offer to donate")
    created_at = models.DateTimeField(default=timezone.now)


class InterestInSkillRequired(models.Model):
    skill_required = models.ForeignKey("charity.SkillRequired", on_delete=models.CASCADE, related_name='skill_required')
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='volunteer')
    created_at = models.DateTimeField(default=timezone.now)
