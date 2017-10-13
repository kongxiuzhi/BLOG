from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser

# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmation",widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email','username','phone')
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email','password','username','phone','is_active','is_admin',
                  'sex','desc','follow','favor')
    def clean_password(self):
        return self.initial['password']

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','username','phone','is_admin','sex')
    list_filter = ('is_admin','sex','favor')
    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Personal info',{'fields':('avatar','username','phone','sex','favor','desc','follow')}),
        ('Permission',{'fields':('is_admin',)}),
    )
    add_fieldsets = (
        (None,{
            "classes":('wide',),
            'fields':('email','username','password1','password2','phone')
        }

        ),
    )
    search_fields=('email','username')
    ordering = ('-created',)
    filter_horizontal= ('follow',)




admin.site.register(MyUser,UserAdmin)
admin.site.unregister(Group)










































