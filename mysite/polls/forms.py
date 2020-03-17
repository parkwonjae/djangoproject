from django import forms
from .models import Employee


class InputCodeForm(forms.Form):
    input_code = forms.CharField(label='Input Code')
