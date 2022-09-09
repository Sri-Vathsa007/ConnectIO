from django.urls import path
from posts_app import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('search_users', views.search_user, name='search'),
    path('searched_user/<username>/', views.searched_user, name='searched-user'),
    path('follow/<username>/', views.follow_user, name='follow'),
    path('unfollow/<username>/', views.unfollow_user, name='un-follow'),

]
