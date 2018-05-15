from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Topic, Author

footer = {
    'about':'This site contains few concepts that i have learnt throughtout my 4 years of b-tech jounrney. Most of the articles here will be on machine learning.',
    'twitter':'https://twitter.com/Rajarshivaibhav',
    'facebook':'https://www.facebook.com/rajarshiv',
    'instagram':'https://www.instagram.com/kharerajarshi/'

}

def home(request):
    topic = Topic.objects.all()
    context = {
        'topic':topic,
        'footer':footer
    }
    return render(request, 'index.html', context)

def blog_edu(request, topic):
    try:
        topic = Topic.objects.get(topic_name = topic)
        author = Author.objects.get(name=topic.author)
        context = {'topic':topic,
                    'author':author,
                    'footer':footer
                    }
        return render(request, 'blog_page.html', context)
    except:
        return render(request, 'pageNotFound.html')


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