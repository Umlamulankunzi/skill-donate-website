from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User, Volunteer, Charity
from .forms import CharitySignUpForm, VolunteerSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import charity_required, volunteer_required

class VolunteerSignUpView(CreateView):
    model = User
    form_class = VolunteerSignUpForm
    template_name = 'app_auth/volunteer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volunteer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('volunteer-home')


class CharitySignUpView(CreateView):
    model = User
    form_class = CharitySignUpForm
    template_name = 'app_auth/charity_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'charity'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('charity-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app_auth/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_volunteer:
                return reverse('volunteer-home')
            elif user.is_charity:
                return reverse('charity-home')
        else:
            return reverse('login')
