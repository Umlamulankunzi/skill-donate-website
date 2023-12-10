"""charity urls file"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.charities, name="charities-list"),
    path("home/", views.charity_home, name="charity-home"),

    path(
        "profile/<int:user_id>/",
        views.profile,
        name="charity-profile"),

    path(
        "profile/update/<int:user_id>/",
        views.update_profile,
        name="charity-profile-update"),

    path(
        "skill_required/",
        views.skills_required,
        name="charities-skills-required"),

    path(
        "skill_required/<int:skill_required_id>/",
        views.skill_required_detail,
        name="skill-required-detail"),

    path(
        "skill_required/create/",
        views.create_skill_request,
        name="create-skill-required"),

    path(
      "skill_donated/show_interest/<int:skill_donated_id>/",
      views.show_interest_in_skill_donated,
      name="show-interest-in-skill-donated"),

    path(
        "skills/required/update/<int:skill_required_id>/",
        views.update_skill_required,
        name="skill-required-update"),
]
