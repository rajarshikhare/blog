from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserLoginForm, UserRegisterForm
from blg.models import Author

def start(request):
    return redirect('login/')

def login_view(request):
    next_ = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        
        if next_:
            return redirect(next_)

        return redirect('/home/')
    context = {
        'form':form,
        'title':'Login',
        'register':'Register',
    }

    return render(request, "form.html", context)

def register_view(request):
    next_ = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        author = Author()
        author.user = user
        author.name = form.cleaned_data.get('name')
        author.facebook = form.cleaned_data.get('facebook')
        author.instagram = form.cleaned_data.get('instagram')
        author.twitter = form.cleaned_data.get('twitter')
        author.about = form.cleaned_data.get('about')
        author.email = form.cleaned_data.get('email')
        author.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next_:
            return redirect(next_)
        return redirect('/home')

    context = {
        'form':form,
        'title':title
    }

    return render(request, 'form.html', context)

def logout_view(request):
    logout(request)
    return redirect('/home')

