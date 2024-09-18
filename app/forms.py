from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app import models

class CreateUser(UserCreationForm):
     class Meta:
          model = User
          fields = ['username','first_name','last_name','email','password1','password2']

class PostForm(forms.ModelForm):
     class Meta:
          model = models.TwitterPost
          fields = ['content','image']
          widgets = {
               'content':forms.Textarea(attrs={'placeholder':"What's happening ?"})
          }

class SigninForm(AuthenticationForm):
     username = forms.CharField(label='Username',max_length=150)
     password = forms.CharField(label='Password',widget=forms.PasswordInput)

class CreateBioProfile(forms.ModelForm):
     class Meta:
          model = models.UserProfile
          fields = '__all__'
          widgets = {
               'content':forms.Textarea(attrs={'placeholder':"What's happening ?"})
          }
          

class BioCreation(forms.ModelForm):
     class Meta:
          model = models.Bio
          fields = ['content']
          widgets = {
               'content':forms.Textarea(attrs={'placeholder':"What's happening ?"})
          }
          