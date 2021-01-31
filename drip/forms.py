from django import forms
from .models import *

class DripForm(forms.ModelForm):
    class Meta:
        fields = ['name', 'image']