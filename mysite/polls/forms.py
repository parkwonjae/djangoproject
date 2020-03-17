from django import forms
from .models import Employee


class InputCodeForm(forms.Form):
    input_code = forms.CharField(label='Input Code')


class ChoiceForm(forms.Form):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
