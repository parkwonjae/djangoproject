from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
<<<<<<< HEAD
from .forms import CompanyForm, EmployerForm
=======
from .forms import CreateEmployerForm
>>>>>>> cf4cb7f497e2ae9113f34b33bac71ca4212e89cc


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class EmployerCreateView(CreateView):
    template_name = 'registration/create_employer.html'
    form_class = CreateEmployerForm
    success_url = reverse_lazy('create_employer_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class EmployerCreateDone(TemplateView):
    template_name = 'registration/create_employer_done.html'


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "owner only can update/delete the object"


def dispatch(self, request, *args, **kwargs):
    obj = self.get_object()
    if request.user != obj.owner:
        return self.handle_no_permission()
    return super().dispatch(request, *args, **kwargs)

