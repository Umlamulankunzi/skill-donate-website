from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from django.core.exceptions import PermissionDenied


def home(request):
    return render(request, "core/homepage.html")

def info(request):
    return render(request, "core/how_it_works.html")

def contact(request):
    if request.method == 'POST':
        # process contact info with provided email and message
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    if form.is_valid():
        # Access cleaned form data here
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # TODO: configure settings of project for this section
        # to send messages to admins from the contact form

        # # Configure the email
        # subject = f'Skill Donate User: Message from {name}'
        # message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        # from_email = 'no_reply@skilldonate.com'
        # recipient_list = ['admin@skilldonate.com']

        # # Send the email
        # send_mail( subject, message, from_email, recipient_list)

        # Redirect after success
        return HttpResponse(f"Form Submitted\n{message}")

    return render(request, "core/contact.html", {'form': form})

def about(request):
    return render(request, "core/about.html")
