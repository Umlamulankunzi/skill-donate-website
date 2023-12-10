"""core urls file"""

from django.urls import path

from . import views

urlpatterns = [
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("how-it-works", views.info, name='how-it-works'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("testimonials", views.testimonials, name='testimonials'),
    path("testimonial/create", views.create_testimonial, name='testimonial-create'),
    path("testimonial/update/int <testimonial_id>", views.update_testimonial, name='testimonial-update'),
]
