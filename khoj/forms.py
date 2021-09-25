from django import forms
from backend.models import Evident


class EvidentForm(forms.ModelForm):
    class Meta:
        model = Evident
        fields = ['input_values']
