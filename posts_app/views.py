from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from posts_app.forms import PostForm
from accounts_app.models import *
from django.contrib.auth.models import User
from accounts_app.models import *


# Create your views here.

@login_required
def home_page(request):
    posts_form = PostForm()

    if request.method == 'POST':
        posts_form = PostForm(request.POST, request.FILES)

        if posts_form.is_valid():
            posts = posts_form.save(commit=False)
            posts.name = request.user
            posts.save()
            return redirect('user-details')

    return render(request, 'posts_app/homepage.html', {
        'posts_form': posts_form,
    })


@login_required
def search_user(request):
    if request.method == 'GET':
        search_users= request.GET.get('search','')
        result = User.objects.filter(username__icontains=search_users)
    return render(request, 'posts_app/search.html', {
        'search_users': search_users,
        'result': result,
    })

@login_required
def searched_user(request,username):
    su = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=su)
    if searched_user == request.user:
        return redirect('profiles')
    return render(request, "posts_app/searched_user.html",{
        'su':su,
        'already_followed': already_followed,
    })


@login_required
def follow_user(request, username):
    following_usr = User.objects.get(username=username)
    follow_usr = request.user
    already_followed = Follow.objects.filter(followers=follow_usr, following=following_usr)
    if not already_followed:
        followed_user = Follow(followers=follow_usr, following=following_usr)
        followed_user.save()
        return HttpResponseRedirect(reverse('searched-user', kwargs={"username":username}))

@login_required
def unfollow_user(request, username):
    following_usr = User.objects.get(username=username)
    follow_usr = request.user
    already_followed = Follow.objects.filter(followers=follow_usr, following=following_usr)
    already_followed.delete()
    return HttpResponseRedirect(reverse('searched-user', kwargs={"username":username}))
