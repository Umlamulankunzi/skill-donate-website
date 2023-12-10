from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from . import views

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),

    path(
        "signup/volunteer",
        views.VolunteerSignUpView.as_view(),
        name="signup-volunteer"),

    path(
        "signup/charity",
        views.CharitySignUpView.as_view(),
        name="signup-charity"),

    path(
        'logout/',
        LogoutView.as_view(template_name = "core/homepage.html"),
        name="logout"),
    path(
        'password-reset/',
        PasswordResetView.as_view(
            html_email_template_name='app_auth/password_reset_email.html',
            template_name='app_auth/password_reset.html'),
        name='password-reset'),

    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='app_auth/password_reset_done.html'),
        name='password_reset_done'),

    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='app_auth/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='app_auth/password_reset_complete.html'),
        name='password_reset_complete'),
]

# LOGIN_REDIRECT_URL = 'student-home'
# LOGIN_URL = 'login'
