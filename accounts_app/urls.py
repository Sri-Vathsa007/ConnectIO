from django.urls import path
from accounts_app import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign-up'),
    path('login/', views.login_user, name='login'),
    path('profiles/', views.profies, name='profiles'),
    path('logout/', views.logout_user, name='logout'),
    path('userdetails/', views.user_details, name='user-details'),
]
