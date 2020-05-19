from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.
class MyUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=48)
    first_name=models.CharField(_('First_Name'),max_length=48)
    nike_name=models.CharField(_('Nike_Name'),unique=True,max_length=48)
    last_name=models.CharField(('Family_Name'),max_length=48)
    email=models.EmailField(_('Email Address'),unique=True)
    date_join=models.DateTimeField(_('date_joined'),auto_now=False,auto_now_add=True)
    date_update=models.DateTimeField(_('date_update'),auto_now=True,auto_now_add=False)
    is_active=models.BooleanField(_('Account is Active'),default=True)
    is_staff=models.BooleanField(_('is the user among the admin team'),default=True)
    avatar=models.ImageField(upload_to='profile_image',blank=True,null=True)
    def __str__(self):
        return "User Profile {}".format(self.user.username)
class ForumsPost(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=45)
    content=models.TextField(max_length=87877)
    date_created=models.DateTimeField(auto_now=False,auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True,auto_now_add=False)
    likes=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    
    #save method
    def save(self,*args,**kwargs):
        super(ForumsPost,self).save(*args,**kwargs)
    def __str__(self):
        return self.id


class ForumsPostImage(models.Model):
    id=models.AutoField(primary_key=True)
    post=models.ForeignKey(ForumsPost,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='ForumsPostImage/%Y/%m/%d',blank=True,null=True)

class ForumsComments(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    post=models.ForeignKey(ForumsPost,on_delete=models.CASCADE)
    comment_content=models.TextField(max_length=23232)
    date_created=models.DateTimeField(auto_now=False,auto_now_add=True)
    date_uodate=models.DateTimeField(auto_now=True,auto_now_add=False)
class ForumCommentsImages(models.Model):
    id=models.AutoField(primary_key=True)
    cooment=models.ForeignKey(ForumsComments,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='ForumCommentsImages',blank=True,null=True)


