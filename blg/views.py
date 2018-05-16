from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Topic, Author, Comment, WebsiteDetail
import time
from .client import store_req

def home(request):
    store_req(request)
    topic = Topic.objects.all()
    footer = WebsiteDetail.objects.get(id=1)
    pages = list(range(1, topic.count()//5 + 2))
    current_page = 1
    context = {
        'topic':topic,
        'footer':footer,
        'pages':pages,
        'current_page':current_page
    }
    return render(request, 'index.html', context)

def blog_edu(request, topic):
    #try:
    topic = Topic.objects.get(topic_name=topic)
    author = Author.objects.get(name=topic.author)
    comment = Comment.objects.filter(topic=topic)
    next_ = topic.id + 1
    prev_ = topic.id - 1
    if next_ <= Topic.objects.all().count():
        next_ = Topic.objects.get(id=next_).topic_name
    else:
        next_ = '....End'
    if prev_ > 0:
        prev_ = Topic.objects.get(id=prev_).topic_name
    else:
        prev_ = 'Start....'

    footer = WebsiteDetail.objects.get(id=1)

    context = {'topic':topic,
                'author':author,
                'footer':footer,
                'comment':comment,
                'nav':{'next':next_, 'prev':prev_}
                }
    return render(request, 'blog_page.html', context)
    #except:
    #    return render(request, 'pageNotFound.html')


def about(request):
    footer = WebsiteDetail.objects.get(id=1)
    context = {
        'footer':footer
    }
    return render(request, 'about.html', context)


def contact(request):
    footer = WebsiteDetail.objects.get(id=1)
    context = {
        'footer':footer
    }
    return render(request, 'contact.html', context)

def blog(request):
    footer = WebsiteDetail.objects.get(id=1)
    return render(request, 'pageNotFound.html')

def comment(request):
    cmt = Comment(cmt=request.POST['cMessage'], writer_name=request.POST['cName'], time=time.ctime(), email=request.POST['cEmail'], topic=Topic.objects.get(topic_name=request.POST['topic']))
    cmt.save()
    return redirect('/home/' + request.POST['topic'])