from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from polls.models import Employer
from django.contrib import auth
from django.db import transaction
from config.forms import UserForm, CompanyForm, EmployerForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


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
            employer_id = request.POST['employer_id']
            employer_age = request.POST['employer_age']
            employer_gender = request.POST['employer_gender']
            employer = Employer(user=user,
                                employer_id=employer_id,
                                employer_age=employer_age,
                                employer_gender=employer_gender)
            employer.save()

            auth.login(request, user)
            return redirect('register_done')
    return render(request, 'registration/register_test.html')


def test(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        employer_form = EmployerForm(request.POST)
        user_form = UserForm(request.POST)
        if company_form.is_valid() and employer_form.is_valid() and user_form.is_valid():
            company_form.save()
            employer_form.save()
            user_form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        company_form = CompanyForm()
        employer_form = EmployerForm()
        user_form = UserForm()
    return render(request, 'registration/test.html', {
        'company_form': company_form,
        'employer_form': employer_form,
        'user_form': user_form,
    })
