from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.

class Myuser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    username = models.CharField(verbose_name="xingming",max_length=20)
    phone = models.CharField(verbose_name="phone",max_length="11")
    SEX_CHOICE = ((nan,'nan'),(nv,'nv'),(mimi,"mimi"))
    sex = models.CharField(max_length=4,verbose_name="xingbian",choices=SEX_CHOICE,default='mimi')
    desc = models.CharField(max_length=200,verbose_name="gerenjianjie")
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d",default="/media/defa/avatar.jpg",
                               max_length=200,blank=True,verbose_name="avatar")
    follow = models.ManyToManyField('self',verbose_name="follower",symmetrical=False)
    favor = models.ForeignKey(Category,on_delete=models.SET_NULL,verbose_name="favoruser")
class BlogArtical(models.Model):
    title = models.CharField(max_length=50,verbose_name="title")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="zuozhe")
    desc = models.CharField(max_length=50,verbose_name="description",blank=True,null=True)
    content = models.TextField(verbose_name="content",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,verbose_name="fenlei",related_name="cat_artitle",blank=True,null=True)
    tags = models.ForeignKey(Tags,verbose_name="biaoqian",on_delete=models.SET_NULL,related_name="tag_artitle",blank=True,null=True)
    visit = models.IntegerField(default=0,verbose_name="liulanliang")
    agreed = models.IntegerField(default=0,verbose_name="zancheng")
    disagreed = models.IntegerField(default=0,verbose_name="fandui")

class Comment(models.Model):
    content = models.TextField(verbose_name="content")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    artical = models.ForeignKey(BlogArtical,on_delete=models.CASCADE,related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    commentid = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    agreed = models.IntegerField(default=0,verbose_name="zancheng")
    disagreed = models.IntegerField(default=0,verbose_name="fandui")

