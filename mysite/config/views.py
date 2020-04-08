from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from polls.models import ComToEmployer, Employer, Company
from django.contrib import auth
from django.db import transaction
from config.forms import ComToEmployerForm, CompanyForm, EmployerForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('test')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "owner only can update/delete the object"


def dispatch(self, request, *args, **kwargs):
    obj = self.get_object()
    if request.user != obj.owner:
        return self.handle_no_permission()
    return super().dispatch(request, *args, **kwargs)


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            '''
            employer_id = request.POST['employer_id']
            employer_age = request.POST['employer_age']
            employer_gender = request.POST['employer_gender']
            employer = Employer(user=user,
                                employer_id=employer_id,
                                employer_age=employer_age,
                                employer_gender=employer_gender)
            employer.save()
            '''

            auth.login(request, user)
            return redirect('test')
    return render(request, 'registration/register_test.html')


def test(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        employer_form = EmployerForm(request.POST)
        if company_form.is_valid() and employer_form.is_valid() and request.user.is_active:
            employer_form.user = request.user.get_username()
            company = company_form.save(commit=False)
            employer = employer_form.save(commit=False)

            if employer.user_id is None:
                employer.user_id = request.user.id
            employer.save()
            company.save()

            comtoem = ComToEmployer(
                employer_id=Employer.objects.get(employer_id=employer_form.cleaned_data['employer_id']),
                company_id=Company.objects.get(company_id=company_form.cleaned_data['company_id'])
            )
            comtoem.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        company_form = CompanyForm()
        employer_form = EmployerForm()
        return render(request, 'registration/test.html', {
            'company_form': company_form,
            'employer_form': employer_form,
        })


def usersignup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('companysignup')
    return render(request, 'registration/user.html')


@login_required
def companysignup(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return render(request, 'registration/employer.html', {
                'company_form': company_form
            })
    else:
        company_form = CompanyForm()
        return render(request, 'registration/company.html', {
            'company_form': company_form
        })


@login_required
def employersignup(request):
    if request.method == 'POST':
        employer_form = EmployerForm(request.POST)
        if employer_form.is_valid():
            employer_form.user = request.user.get_username()
            employer = employer_form.save(commit=False)
            if employer.user_id is None:
                employer.user_id = request.user.id
            employer.save()
            return redirect('home')
    else:
        employer_form = EmployerForm()
        return render(request, 'registration/employer.html', {
            'employer_form': employer_form
        })
