from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blg'

urlpatterns = [
    path('', views.home, name='home'),
    path('/<topic>/', views.blog)
    
]
