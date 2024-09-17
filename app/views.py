from django.shortcuts import render,redirect,get_object_or_404
from app import forms 
from app import models
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

# ADMIN PANEL
@login_required(login_url='signin')
def show_users_to_admin(request):
     users = models.User.objects.all()
     msg = 'No Users'
     if users is None or users.count()== 0:
          return render(request,'adminpanel.html',{'msg':msg})
     return render(request,'adminpanel.html',{'users':users})




# AUTH
# SIGNUP
def signin_view(request):
     if request.method == 'POST':
          form = forms.SigninForm(request,request.POST)
          if form.is_valid():
               user = form.get_user()
               login(request,user)
               return redirect('home')
     else:
          form = forms.SigninForm()
     return render(request,'signin.html',{'form':form})

@login_required(login_url='signin')            
def logout_view(request):
     logout(request)
     return redirect('signin')

@login_required(login_url='signin')  
def home(request):
     tweets = models.TwitterPost.objects.all().order_by('-date_created')
     forma = forms.PostForm()
     if request.method == 'POST':
          forma = forms.PostForm(request.POST)
          if forma.is_valid():
               tweet = forma.save(commit=False)
               tweet.author = request.user
               forma.save(commit=True)
               return redirect('home')
          else:
               forma = forms.PostForm()
     return render(request,'home.html',{
          'tweets':tweets,
          'forma': forma
     })


@login_required(login_url='signin')  
def post(request):
     user = request.user
     if request.method == 'POST':
          forma = forms.PostForm(request.POST,request.FILES)
          if forma.is_valid():
               tweet = forma.save(commit=False)
               tweet.author = request.user
               tweet.save()
               return redirect('home')
     else :
          forma = forms.PostForm()
     return render(request,'post.html',{'forma':forma,'user':user})

 

 
def register_form(request):
     if request.method == 'POST':
          form = forms.CreateUser(request.POST)
          if form.is_valid():
               user = form.save(commit=True)
               # subject = 'Welcome to MyBlog'
               # message = f'Dear {user.username},\n\nThank you for registering at MyBlog. We are excited to have you on board!'
               # from_email = 'ermal_beqiri@outlook.com'
               # recipient_list = [user.email]
               # send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=False)
               return redirect('home')
               
     else:
          form = forms.CreateUser()
     return render(request,'register.html',{'form':form})

@login_required(login_url='signin')   
def delete_post(request,pk):
     post = get_object_or_404(models.TwitterPost,pk=pk)
     if request.method == 'POST':
          post.delete()
          return redirect('home')
     return render(request,'home.html',{'post':post})

@login_required(login_url='signin') 
def profile(request):
     tweets = models.TwitterPost.objects.all()
     return render(request,'profile.html',{'tweets':tweets})

@login_required(login_url='signin')
def my_posts(request,author):
     posts = get_object_or_404(models.TwitterPost,author)
     return render(request,'profile.html',{'posts':posts})


# def like(request, pk):
#     user = request.user
#     post = get_object_or_404(models.TwitterPost, pk=pk)

#     # Kontrollo nëse përdoruesi ka pëlqyer këtë postim
#     existing_like = models.Likes.objects.filter(user=user, post=post).first()
    
#     if existing_like:
#         # Përdoruesi ka pëlqyer postimin, hiqe pëlqimin
#         existing_like.delete()
#         post.likes.remove(user)
#     else:
#         # Përdoruesi nuk ka pëlqyer postimin, shto pëlqimin
#         models.Likes.objects.create(user=user, post=post)
#         post.likes.add(user)
    
#     post.save()
#     return redirect('home')
          
@login_required(login_url='signin')
def createbio(request):
     if request.method == 'POST':
          bioform = forms.CreateBioProfile(request.POST)
          if bioform.is_valid():
               bioform.save(commit=True)
               return redirect('profile')
          else:
               bioform = forms.CreateBioProfile()
     return render(request,'profile.html',{
          'bioform':bioform
     })

@login_required(login_url='signin')
def like_post(request):
     user = request.user
     if request.method == 'POST':
          post_id = request.POST.get('post_id')
          post_obj = models.TwitterPost.objects.get(id=post_id)
          if user in post_obj.likes.all():
               post_obj.likes.remove(user)
          else:
               post_obj.likes.add(user)
          like, created = models.Like.objects.get_or_create(user=user,post_id=post_id)
          if not created:
               if like.value == 'Like':
                    like.value = 'Unlike'
               else:
                    like.value = 'Like'
          like.save()
          return redirect('home')