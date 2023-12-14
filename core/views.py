"""
Core app views
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from skilldonate.settings import EMAIL_HOST_USER
from .models import Testimonial
from .forms import ContactForm, TestimonialForm



def home(request):
    reviews = Testimonial.objects.order_by('-created_at')[:3]
    context = {
        'reviews': reviews,
    }
    return render(request, "core/homepage.html", context)


@login_required
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

        # Configure the email
        subject = f'Skill Donate User: Message from {name}'
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        from_email = EMAIL_HOST_USER
        recipient_list = ['umlamulankunzi@gmail.com', ]

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        # Redirect after success
        messages.success(request, 'Message sent successfully.')
        return redirect('contact')

    return render(request, "core/contact.html", {'form': form})

def about(request):
    return render(request, "core/about.html")


def testimonials(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, "core/testimonials.html", context)


@login_required
def create_testimonial(request):
    """Create a skill donation request"""

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimony = form.save(commit=False)
            testimony.user = request.user
            testimony.save()
            messages.success(request, "Review created successfully")
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'core/testimony-create.html', {'form': form})


@login_required
def update_testimonial(request, testimonial_id):
    testimonial = Testimonial.objects.get(id=testimonial_id)

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect('testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(
        request, 'core/testimony-update.html',
        {
            'form': form,
            'testimonial_id': testimonial.id,
        })


def delete_testimonial(request, testimonial_pk):
    testimonial = get_object_or_404(Testimonial, pk=testimonial_pk)
    testimonial.delete()
    messages.warning(request, 'Review deleted Successfully')
    return redirect('testimonials')
