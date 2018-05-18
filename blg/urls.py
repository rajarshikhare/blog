from django.urls import path
from . import views

app_name = 'blg'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    #/ is added because of anomaly in loading home page
    path('/<topic>/', views.blog_edu, name='blog_edu'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('create_blog/<topic>', views.create_blog, name='create_blog'),
    path('add_blog', views.add_blog, name='add_blog')
]
