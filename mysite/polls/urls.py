from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.PollsHomeView.as_view(), name='polls_home'),
    path('employee/', views.EmployeeLV.as_view(), name='employeelist'),
    path('employer/', views.EmployerView.as_view(), name='employerlist'),

    # /polls/employee/inputcode/
    path('employee/inputcode/', views.InputCodeFormView.as_view(), name='inputcode'),
    path('employee/choiceform/', views.ChoiceFormView.as_view(), name='choice'),
]
