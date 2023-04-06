from django.urls import path
from . import views

app_name = "Tasks"
urlpatterns = [
  path('', views.Tasks, name='tests'),
  path('add/', views.add, name='add')

]