from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm, TestimonialForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


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


def testimonials(request):
    return HttpResponse("list of testimonials")


@login_required
def create_testimonial(request):
    """Create a skill donation request"""

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimony = form.save(commit=False)
            testimony.user = request.user
            testimony.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'core/testimony-create.html', {'form': form})


@login_required
def update_testimonial(request, testimonial_id):
    testimonial = TestimonialForm.objects.get(id=testimonial_id)

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(
        request, 'core/testimony-update.html',
        {
            'form': form,
            'testimonial_id': testimonial.id,
        })
