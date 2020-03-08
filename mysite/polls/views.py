from django.shortcuts import render
from django.views.generic import ListView, DetailView
from polls.models import SelectVariable


# Create your views here.

class SelectVariableLV(ListView):
    model = SelectVariable


class SelectVariableDV(DetailView):
    model = SelectVariable


