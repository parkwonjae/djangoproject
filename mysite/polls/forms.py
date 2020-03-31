from django import forms
from polls.models import EmployerQuestion


class InputCodeForm(forms.Form):
    input_code = forms.CharField(label='Input Code')


class ChoiceForm(forms.Form):
    CHOICES = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ]
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    test = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ChoiceFormTest(forms.ModelForm):
    class Meta:
        model = EmployerQuestion
        fields = '__all__'
        exclude = ('company_id', 'employer_id')


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


class CompassionForm(MultipleForm):
    Choice = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ]
    compassion_1 = forms.ChoiceField(choices=Choice, widget=forms.RadioSelect)
    compassion_2 = forms.ChoiceField(choices=Choice, widget=forms.RadioSelect)


class SurfaceActingForm(MultipleForm):
    Choice = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
    ]
    surface_acting_1 = forms.ChoiceField(choices=Choice, widget=forms.RadioSelect)
    surface_acting_2 = forms.ChoiceField(choices=Choice, widget=forms.RadioSelect)


