from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
<<<<<<< HEAD
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


=======


class CreateEmployerForm(UserCreationForm):
    company_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    company_establishment = forms.IntegerField(required=True)
    company_size = forms.IntegerField(required=True)
    employer_age = forms.IntegerField(required=True)
    employer_gender = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'company_name', 'company_establishment', 'company_size',
                  'employer_age', 'employer_gender', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CreateEmployerForm, self).save(commit=False)
        user.company_name = self.cleaned_data['company_name']
        user.company_establishment = self.cleaned_data['company_establishment']
        user.company_size = self.cleaned_data['company_size']
        user.employer_age = self.cleaned_data['employer_age']
        user.employer_gender = self.cleaned_data['employer_gender']

        if commit:
            user.save()
        return user
>>>>>>> cf4cb7f497e2ae9113f34b33bac71ca4212e89cc
