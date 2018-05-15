from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic

def home(request):
    topic = Topic.objects.all()
    test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, 'index.html', {'test':test, 'topic':topic})

def blog(request, topic):
    topic = Topic.objects.get(topic_name = topic)
    context = {'topic':topic}
    return render(request, 'single-standard.html', context)