from django.shortcuts import redirect, render
from blg.models import WebsiteDetail

def start(request):
    return redirect('/home')

def google(request):
    return render(request, 'google3b2ce12912f0a3e6.html')

def sitemap(request):
    context = {'map': WebsiteDetail.objects.get(id=1).sitemap}
    return render(request, 'sitemap.xml' ,context)