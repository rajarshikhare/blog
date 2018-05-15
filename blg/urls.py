from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blg'

urlpatterns = [
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('/contact', views.contact, name='contact'),
    path('/<topic>/', views.blog, name='blog')
]
