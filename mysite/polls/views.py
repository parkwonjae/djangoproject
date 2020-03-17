from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from polls.models import Employee, SelectVariable
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from config.views import OwnerOnlyMixin
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from polls.forms import InputCodeForm
from polls.forms import ChoiceForm
from django.db.models import Q


# Create your views here.


class PollsHomeView(TemplateView):
    template_name = 'polls/polls_home.html'


class EmployeeLV(ListView):
    model = Employee
    context_object_name = 'Employees'


class EmployerView(LoginRequiredMixin, TemplateView):
    template_name = 'polls/employer_list.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class InputCodeFormView(FormView):
    form_class = InputCodeForm
    template_name = 'polls/form.html'

    def form_valid(self, form):
        inputcompanycode = form.cleaned_data['input_code']

        #selectlist는 queryset이다(dic type)
        selectlist = SelectVariable.objects.filter(Q(company_id__icontains=inputcompanycode)).distinct().values()

        #dic 형태를 활용하기 위해 list 형태로 바꿈
        makelist = list(selectlist)

        #list 출력 test
        #printlist(makelist)

        #value 가 true인 key만 뽑아서 list 형태로 바꿈
        makelist = truecheck(makelist)

        context = {}
        context['form'] = form
        context['code'] = inputcompanycode
        context['object_list'] = selectlist
        context['makelist'] = makelist

        return render(self.request, self.template_name, context)


class ChoiceFormView(FormView):
    form_class = ChoiceForm
    template_name = 'polls/choiceform.html'

    def form_valid(self, form):
        like = form.cleaned_data['like']
        context = {}
        context['form'] = form
        context['object_list'] = like
        return render(self.request, self.template_name, context)

# 인사담당자가 true 체크한 리스트를 뽑아주는 함수 return값은 list 형태
def truecheck(makelist):
    truelist = []
    temp = list(makelist[0].keys())
    for k in temp:
        if makelist[0].get(k) ==True:
            truelist.append(k)
    return truelist


def printlist(makelist):
    temp = list(makelist[0].keys())
    truelist = []
    for k in temp:
        print(k)
    print(makelist[0])
    print(type(makelist[0]))
    for k in makelist[0]:
        for l in temp:
            if makelist[0].get(l) == True:
                print(makelist[0].get(l))
    for k in temp:
        if makelist[0].get(k) ==True:
            truelist.append(k)
            print("2",makelist[0].get(k))
    print(truelist)
