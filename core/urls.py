"""core urls file"""

from django.urls import path

from . import views

urlpatterns = [
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home, info, about, contact


urlpatterns = [
    path("", home, name='home'),
    path("how-it-works", info, name='how-it-works'),
    path("about", about, name='about'),
    path("contact", contact, name='contact'),
]
