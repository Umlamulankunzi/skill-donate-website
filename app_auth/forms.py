from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import Charity, Volunteer, User
from django import forms
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()

class LoginForm(AuthenticationForm):
    # email = forms.EmailField(widget=forms.EmailInput())
    # password = forms.CharField(widget=forms.PasswordInput())
    pass

class VolunteerSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), label="Email Address")
    # Additional Fields
    name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput(), required=False)
    phone = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput(), required=False)
    country = forms.CharField(widget=forms.TextInput(), required=False, initial="zimbabwe")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_volunteer = True
        if commit:
            user.save()

        volunteer = Volunteer.objects.create(
            user=user,
            name=self.cleaned_data.get('name'),
            last_name=self.cleaned_data.get('last_name'),
            phone=self.cleaned_data.get('phone'),
            city=self.cleaned_data.get('city'),
            country=self.cleaned_data.get('country'),
            )
        return user


class CharitySignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), label="Email Address")

    name = forms.CharField(widget=forms.TextInput())
    phone = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    city = forms.CharField(widget=forms.TextInput())
    country = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_charity = True
        if commit:
            user.save()

        charity = Charity.objects.create(
            user=user, name=self.cleaned_data.get('name'),
            phone=self.cleaned_data.get('phone'),
            description=self.cleaned_data.get('description'),
            city=self.cleaned_data.get('city'),
            country=self.cleaned_data.get('country'),
            )
        return user
