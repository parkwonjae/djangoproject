from django.shortcuts import render
from django.views.generic import ListView, DetailView
from polls.models import SelectVariable
from polls.models import Employee

# Create your views here.


class SelectVariableLV(ListView):
    model = SelectVariable
    context_object_name = 'SelectVariables'


class SelectVariableDV(DetailView):
    model = SelectVariable


class EmployeeLV(ListView):
    model = Employee
    context_object_name = 'Employees'

