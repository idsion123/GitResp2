from django import forms
from . import models
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
class UserRegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True,
                             min_length=6,
                             max_length=15,
                             error_messages=
                             {'required':'这是必填项',
                              'mix_length':'密码必须大于6位',
                              'max_length':'密码必须小于15位',
                              },
                             widget=forms.PasswordInput(attrs={'placeholder':'输入密码','type':'password'}),label='密码')
    captcha=CaptchaField()
class UserLoginForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True,
                             min_length=6,
                             max_length=20,
                             error_messages=
                             {'required':'这是必填项',
                              'mix_length':'密码必须大于6位',
                              'max_length':'密码必须小于15位',
                              },
                             widget=forms.PasswordInput(attrs={'placeholder':'输入密码','type':'password'}),label='密码')
class UserForgetForm(forms.Form):
    email=forms.EmailField()
    captcha=CaptchaField()
class UserResetForm(forms.Form):
    password=forms.CharField(required=True,
                             min_length=6,
                             max_length=20,
                             error_messages=
                             {'required':'这是必填项',
                              'mix_length':'密码必须大于6位',
                              'max_length':'密码必须小于15位',
                              },
                             widget=forms.PasswordInput(attrs={'placeholder':'输入密码','type':'password'}),label='密码')
    repassword = forms.CharField(required=True,
                               min_length=6,
                               max_length=20,
                               error_messages=
                               {'required': '这是必填项',
                                'mix_length': '密码必须大于6位',
                                'max_length': '密码必须小于15位',
                                },
                               widget=forms.PasswordInput(attrs={'placeholder': '输入密码', 'type': 'password'}),
                               label='第二次密码')

class User_ChangeImageForm(forms.ModelForm):
    class Meta:
        model=models.UserProfile
        fields=['image']


class User_ChangeInfoForm(forms.ModelForm):
    class Meta:
        model=models.UserProfile
        fields=['nick_name','birthday','gender','address','phone']

class User_ChangeEmailForm(forms.ModelForm):
    class Meta:
        model=models.EmailVerifyCode
        fields=['email']

class User_ResetEmailForm(forms.ModelForm):
    class Meta:
        model=models.EmailVerifyCode
        fields=['email','code']