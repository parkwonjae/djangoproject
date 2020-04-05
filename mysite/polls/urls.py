from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.PollsHomeView.as_view(), name='polls_home'),
    #path('employee/', views.EmployeeLV.as_view(), name='employeelist'),

    # /polls/employer
    path('employer/', views.EmployerView.as_view(), name='employer'),


]
