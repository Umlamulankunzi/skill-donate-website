"""core urls file"""


from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),

    path(
        "testimonials",
        views.testimonials,
        name='testimonials'),

    path(
        "testimonial/create",
        views.create_testimonial,
        name='testimonial-create'),

    path(
        "testimonial/update/<int:testimonial_id>",
        views.update_testimonial,
        name='testimonial-update'),

    path(
        "testimonial/delete/<int:testimonial_pk>",
        views.delete_testimonial,
        name='testimonial-delete'),
]
