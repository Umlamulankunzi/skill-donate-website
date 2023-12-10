from django.db import transaction
from django import forms
from app_auth.models import Charity

from .models import SkillRequired



class SkillRequiredForm(forms.ModelForm):
    """Form for creating or updating skill required"""
    skill_name = forms.CharField(widget=forms.TextInput())
    category = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = SkillRequired
        fields = ('skill_name', 'category', 'description')



class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Charity
        fields = ('name', 'description', 'city', 'country')
