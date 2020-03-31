from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.PollsHomeView.as_view(), name='polls_home'),
    #path('employee/', views.EmployeeLV.as_view(), name='employeelist'),

    # /polls/employer
    path('employer/', views.EmployerView.as_view(), name='employer'),



    # /polls/employee/inputcode/
    #path('employee/inputcode/', views.InputCodeFormView.as_view(), name='inputcode'),

    # /polls/employee/choiceform/
    #path('employee/choiceform/', views.ChoiceFormView.as_view(), name='choice'),

    #path('employee/multiform/', views.MultipleFormsDemoView.as_view(), name='forms'),
    #path('test/', views.TestView.as_view(), name='test'),
]
