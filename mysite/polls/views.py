from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from config.views import OwnerOnlyMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import FormView
from polls.forms import *
from polls.multiforms import MultiFormsView
from django.db.models import Q
from django.views.generic import View

# Create your views here.


class PollsHomeView(TemplateView):
    template_name = 'polls/polls_home.html'


'''
class EmployeeLV(ListView):
    model = Employee
    context_object_name = 'Employees'
'''


class EmployerView(LoginRequiredMixin, FormView):
    template_name = 'polls/employer_list.html'
    form_class = ChoiceFormTest



'''
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
'''


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

'''
def multiple_forms(request):
    if request.method == 'POST':
        compassion_form = CompassionForm(request.POST)
        surfaceacting_form = SurfaceActingForm(request.POST)
        if compassion_form.is_valid() or surfaceacting_form.is_valid():
            # Do the needful
            return HttpResponseRedirect(reverse('form-redirect'))
    else:
        compassion_form = CompassionForm()
        surfaceacting_form = SurfaceActingForm()

    return render(request, 'polls/multiple_forms.html', {
        'compassion_form': compassion_form,
        'surfaceacting_form': surfaceacting_form,
    })
'''


class MultipleFormsDemoView(MultiFormsView):
    template_name = 'polls/cbv_multiple_forms.html'
    form_classes = {
        'compassion': CompassionForm,
        'surfaceacting': SurfaceActingForm,
    }
    '''
    success_urls = {
        'compassion': reverse_lazy('form-redirect'),
        'surfaceacting': reverse_lazy('form-redirect'),
    }

    def compassion_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def surfaceacting_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))
    '''


class TestView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('hello, world')
