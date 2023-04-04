from django.urls import path
from . import views


urlpatterns = [
  path('', views.hop, name='hop')
]