from django import views
from django.urls import path
from . import views

app_name = "players"
urlpatterns = [
    path('getname/', views.getname, name='getname')
]