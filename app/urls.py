from django.urls import path
from django.conf.urls import include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',view= views.home, name='home'),
    path('delete/<int:pk>/', view=views.delete_post,name='delete'),
    path('signin/',view=views.signin_view,name='login'),
    path('register/',view=views.register_form,name='register'),
    path('post/',view=views.post , name='post'),
    path('signin/',view=views.signin_view,name='signin'),
    path('logout/',view=views.logout_view,name='logout'),
    path('profile/',view=views.profile,name='profile'),
    path('profile/',view=views.my_posts,name='my_posts'),
    path('profile/createbio', views.profile, name='createbio'),
    path('like/',view=views.like_post,name='like-post'),
    path('admin/panel/',view=views.show_users_to_admin,name='adminshowusers')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)