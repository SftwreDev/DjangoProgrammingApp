from django import forms 

from .models import Programming

class ProgrammingForm(forms.Form):
    language = forms.CharField()
    slug = forms.SlugField()
    description = forms.CharField()

