from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from polls.models import Employer
from polls.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'


