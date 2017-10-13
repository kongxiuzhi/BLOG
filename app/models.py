from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.



class Category(models.Model):
    category = models.CharField(max_length=50,verbose_name="类别")

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.category

class Tags(models.Model):
    tag = models.CharField(max_length=50,verbose_name="标签")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.tag

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,phone,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email),phone=phone,username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,phone,password):
        user = self.create_user(email=email,password=password,username=username,phone=phone)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='邮箱',max_length=255,unique=True)
    username = models.CharField(verbose_name="姓名",max_length=20)
    phone = models.CharField(verbose_name="电话",max_length=11)
    SEX_CHOICE = (('m','男'),('f','女'),('s',"保密"))
    sex = models.CharField(max_length=4,verbose_name="性别",choices=SEX_CHOICE,default='s')
    desc = models.CharField(max_length=200,verbose_name="个人简介",blank=True,null=True)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d",default="defa/avatar.jpg",
                               max_length=200,blank=True,verbose_name="头像")
    follow = models.ManyToManyField('self',verbose_name="关注",symmetrical=False)
    favor = models.ForeignKey(Category,on_delete=models.SET_NULL,verbose_name="爱好",blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return  self.username
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        #"Does the user have a specific permission?"
        return True
    def has_module_perms(self,app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    def is_staff(self):
        return self.is_admin



class BlogArtical(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章")
    author = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name="作者")
    desc = models.CharField(max_length=50,verbose_name="描述",blank=True,null=True)
    content = models.TextField(verbose_name="内容",blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,verbose_name="类别",related_name="artical",blank=True,null=True)
    tags = models.ForeignKey(Tags,verbose_name="标签",on_delete=models.SET_NULL,related_name="artical",blank=True,null=True)
    visit = models.IntegerField(default=0,verbose_name="浏览量")
    agreed = models.IntegerField(default=0,verbose_name="赞成")
    disagreed = models.IntegerField(default=0,verbose_name="反对")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering =('-created',)
    def __str__(self):

        return self.title

class Comment(models.Model):
    content = models.TextField(verbose_name="评论")
    author = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    artical = models.ForeignKey(BlogArtical,on_delete=models.CASCADE,related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    commentid = models.ForeignKey("self",on_delete=models.CASCADE,blank=True,null=True)
    agreed = models.IntegerField(default=0,verbose_name="赞成")
    disagreed = models.IntegerField(default=0,verbose_name="反对")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ('created',)

    def __str__(self):
        return "comment of %s" %self.artical


















