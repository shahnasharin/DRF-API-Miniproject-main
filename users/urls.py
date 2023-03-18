from django.urls import path
from .views import * 
#import static 

urlpatterns = [
    path('auth/signup/',Signup.as_view(),name='signup'),
    path('auth/signin/',Login.as_view(),name='login'),
    path('profile/',UserView.as_view(),name='user'),
    path('upload/',ProfileImageView.as_view(),name='upload'),
    path('admin/',AdminView.as_view(),name='admin'),

]



