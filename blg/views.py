import time
from django.shortcuts import render, redirect
from .models import Topic, Author, Comment, WebsiteDetail
from .client import store_req
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        user = Author.objects.get(user=request.user)
    else:
        user = ''
    store_req(request)
    topic = Topic.objects.all()
    footer = WebsiteDetail.objects.get(id=1)
    pages = list(range(1, topic.count()//5 + 2))
    current_page = 1
    context = {
        'topic': topic,
        'footer': footer,
        'pages': pages,
        'current_page': current_page,
        'user':user
    }
    return render(request, 'index.html', context)


def blog_edu(request, topic):
    # try:
    if request.user.is_authenticated:
        user = Author.objects.get(user=request.user)
    else:
        user = ''
    topic = Topic.objects.get(topic_name=topic)
    author = Author.objects.get(name=topic.author)
    comment = Comment.objects.filter(topic=topic)
    next_ = topic.id + 1
    prev_ = topic.id - 1
    if next_ <= Topic.objects.all().count():
        next_ = Topic.objects.get(id=next_).topic_name
    else:
        next_ = Topic.objects.get(id=1).topic_name
    if prev_ > 0:
        prev_ = Topic.objects.get(id=prev_).topic_name
    else:
        prev_ = Topic.objects.get(id=Topic.objects.all().count()).topic_name

    footer = WebsiteDetail.objects.get(id=1)

    context = {'topic': topic,
               'author': author,
               'footer': footer,
               'comment': comment,
               'nav': {'next': next_, 'prev': prev_},
               'user':user,
              }
    return render(request, 'blog_page.html', context)
    # except:
    #    return render(request, 'pageNotFound.html')


def about(request):
    if request.user.is_authenticated:
        user = Author.objects.get(user=request.user)
    else:
        user = ''
    website = WebsiteDetail.objects.get(id=1)
    context = {
        'footer': website,
        'user':user
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.user.is_authenticated:
        user = Author.objects.get(user=request.user)
    else:
        user = ''
    footer = WebsiteDetail.objects.get(id=1)
    context = {
        'footer': footer,
        'user':user
    }
    return render(request, 'contact.html', context)


def blog(request):
    footer = WebsiteDetail.objects.get(id=1)
    return render(request, 'pageNotFound.html')


def add_comment(request):
    cmt = Comment(cmt=request.POST['cMessage'], writer_name=request.POST['cName'], time=time.ctime(
    ), email=request.POST['cEmail'], topic=Topic.objects.get(topic_name=request.POST['topic']))
    cmt.save()
    return redirect('/home/' + request.POST['topic'])


@login_required(login_url='/accounts/login')
def create_blog(request, topic):
    if request.user.is_authenticated:
        user = Author.objects.get(user=request.user)
    else:
        user = ''
    footer = WebsiteDetail.objects.get(id=1)
    if topic == 'new blog':
        topic = Topic(topic_name='new blog')
    else:
        topic = Topic.objects.get(topic_name=topic)
    context = {
        'topic': topic,
        'footer': footer,
        'user':user
    }
    return render(request, 'create_blog.html', context)


def add_blog(request):
    if request.POST['topic'] == 'new blog':
        topic = Topic()
        topic.id = Topic.objects.all().count() + 1
    else:
        topic = Topic.objects.get(topic_name=request.POST['topic'])
    topic.author = Author.objects.get(user=request.user)
    topic.topic_name = request.POST['topic_name']
    topic.abstract_img = request.POST['abstract_img']
    topic.abstract = request.POST['abstract']
    topic.category = request.POST['category']
    topic.upload_date = time.ctime()
    topic.link = request.POST['link']
    topic.content = request.POST['content']
    topic.save()
    return redirect('/home/create_blog/' + request.POST['topic_name'])