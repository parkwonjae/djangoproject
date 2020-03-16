from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from polls.models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from config.views import OwnerOnlyMixin

# Create your views here.


class PollsHomeView(TemplateView):
    template_name = 'polls/polls_home.html'


class EmployeeLV(ListView):
    model = Employee
    context_object_name = 'Employees'


class EmployerView(LoginRequiredMixin, TemplateView):
    #success_url = reverse_lazy('polls:employerlist')
    template_name = 'polls/employer_list.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)