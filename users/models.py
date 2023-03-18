from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def upload_to(instance, filename):
    return 'profile_pictures/{filename}'.format(filename=filename)

class User(AbstractUser):
    mobile_number = models.IntegerField(default='7034725940')
    email = models.EmailField(unique=True,max_length=255)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=8,default='2017-01-01')
    profile_picture = models.ImageField(upload_to=upload_to,blank=True,null=True,default='profile_pictures/default.jpg')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','mobile_number','password','date_of_birth','profile_picture']

    

    