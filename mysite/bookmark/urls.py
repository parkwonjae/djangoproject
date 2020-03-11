from django.urls import path
#from bookmark.views import BookmarkDV, BookmarkLV
from bookmark import views

app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # example : /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name='add'),

    # example : /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),

    # example : /bookmark/1/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),

    # example : /bookmark/1/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),

]
