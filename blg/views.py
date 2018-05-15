from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic

def home(request):
    topic = Topic.objects.all()
    return render(request, 'index.html', {'topic':topic})

def blog(request, topic):
    topic = Topic.objects.get(topic_name = topic)
    context = {'topic':topic}
    return render(request, 'blog_page.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')