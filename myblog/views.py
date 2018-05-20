from django.shortcuts import redirect, render

def start(request):
    return redirect('/home')

def google(request):
    return render(request, 'google3b2ce12912f0a3e6.html')