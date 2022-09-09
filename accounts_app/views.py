from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import *
from posts_app.forms import *
from .models import UserProfile,Follow
from posts_app.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    sign_up_form = Sign_Up_Form()
    registered = False

    if request.method == 'POST':
        sign_up_form = Sign_Up_Form(data=request.POST)

        if sign_up_form.is_valid():
            user = sign_up_form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'accounts_app/signup.html',{
        'sign_up_form':sign_up_form,
    })


def login_user(request):
    login_form = Login_Form()

    if request.method == 'POST':
        login_form = Login_Form(data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')

    return render(request, 'accounts_app/login.html', {
        'login_form': login_form,
    })

@login_required
def profies(request):
    current_user = UserProfile.objects.get(user=request.user)
    profile_form = User_Profile_Form(instance=current_user)

    if request.method == 'POST':
        profile_form = User_Profile_Form(request.POST,request.FILES, instance=current_user)

        if profile_form.is_valid():
            profile_form.save(commit=True)
            profile_form = User_Profile_Form(instance=current_user)
            return redirect('user-details')

    return render(request, 'accounts_app/profile.html', {
        'profile_form': profile_form,
    })


def logout_user(request):
    logout(request)
    return redirect('login')


def user_details(request):
    user_posts = PostForm()
    return render(request, 'accounts_app/userdetails.html',{
        'user_posts':user_posts,
    })
