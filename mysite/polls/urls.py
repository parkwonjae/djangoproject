from django.urls import path
from polls import views

app_name = 'polls'
urlpatterns = [
    path('', views.SelectVariableLV.as_view(), name='index'),
    path('<int:pk>/', views.SelectVariableDV.as_view(), name='detail'),
    path('employee/', views.EmployeeLV.as_view(), name='employeelist'),
    path('employer/', views.EmployeeLV.as_view(), name='employerlist'),

]
