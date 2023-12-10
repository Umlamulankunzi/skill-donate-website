from django import forms
from .models import Testimonial

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(), required=False)
    email = forms.EmailField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))



class TestimonialForm(forms.Form):
    testimony = forms.CharField(
        label="Testimony", max_length=255, widget=forms.TextInput())

    class Meta:
        model = Testimonial
        fields = ('testimony', )
