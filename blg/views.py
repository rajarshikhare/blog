from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Topic, Author, Comment
import time
from .client import store_req

footer = {
    'about':'This site contains few concepts that I have learned throughout my 3 years of b-tech journey. Most of the articles here will be on machine learning and data strucures.',
    'twitter':'https://twitter.com/Rajarshivaibhav',
    'facebook':'https://www.facebook.com/rajarshiv',
    'instagram':'https://www.instagram.com/kharerajarshi/'

}

def home(request):
    client_address = request.META['REMOTE_ADDR']  
    print(client_address)
    store_req(request)
    topic = Topic.objects.all()
    context = {
        'topic':topic,
        'footer':footer
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
    context = {
        'footer':footer
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'footer':footer
    }
    return render(request, 'contact.html', context)

def blog(request):
    return render(request, 'pageNotFound.html')

def comment(request):
    cmt = Comment(cmt=request.POST['cMessage'], writer_name=request.POST['cName'], time=time.ctime(), email=request.POST['cEmail'], topic=Topic.objects.get(topic_name=request.POST['topic']))
    cmt.save()
    return redirect('/home/' + request.POST['topic'])