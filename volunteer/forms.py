from django import forms
from app_auth.models import Volunteer
from .models import SkillDonated



class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(
        label="Last name",widget=forms.TextInput(), required=False)
    phone = forms.CharField(label="Phone", widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())
    profile_pic = forms.ImageField(label="Profile Picture", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.profile_pic:
            # self.fields['profile_pic'].widget.attrs['placeholder'] = self.instance.profile_pic
            # # or
            self.fields['profile_pic'].initial = self.instance.profile_pic

    class Meta:
        model = Volunteer
        fields = (
            'name', 'last_name', 'phone', 'city', 'country', 'profile_pic')



class SkillDonateForm(forms.ModelForm):
    """Form for creating or updating skill donated"""
    skill_name = forms.CharField(widget=forms.TextInput())
    category = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = SkillDonated
        fields = ('skill_name', 'category', 'description')
