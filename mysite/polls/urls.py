from django.urls import path
from polls import views
from polls.views import employer_question

app_name = 'polls'
urlpatterns = [
    path('', views.PollsHomeView.as_view(), name='polls_home'),
    path('employee/', views.EmployeeView.as_view(), name='employeelist'),

    # /polls/employer
    path('employer/', employer_question, name='employer'),
    path('employee/inputcode/', views.InputCodeFormView.as_view(),name='inputcode')


]
