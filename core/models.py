from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models

User = get_user_model()

# Create your models here.
class Testimonial(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonial_author")
    testimony = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
