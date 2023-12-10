from django.contrib import admin

from .models import SkillRequired, InterestInSkillDonated

# Register your models here.
admin.site.register(SkillRequired)
admin.site.register(InterestInSkillDonated)
