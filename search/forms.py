from django import forms

CHOICES = [
    ('1', 'Donated Skill'), ('2', 'Requested Skill'),
    ('3', 'Charity'), ('4', 'Volunteer')
]

class SearchForm(forms.Form):
    category = forms.ChoiceField(choices=CHOICES, widget=forms.Select())
    query = forms.CharField(label="Search query", widget=forms.TextInput())
