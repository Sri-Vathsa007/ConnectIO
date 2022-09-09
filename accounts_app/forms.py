from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class Sign_Up_Form(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class Login_Form(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class User_Profile_Form(forms.ModelForm):
    dob = forms.DateField(label="", widget=forms.TextInput(attrs={'type':'date'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    age = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder':'Age'}))
    about = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder':'About'}))

    class Meta:
        model = UserProfile
        exclude = ('user',)
