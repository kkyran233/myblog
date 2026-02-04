from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel


User=get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=20,min_length=2,error_messages={
        'required':'用户名不能为空','min_length':'用户名长度不能小于2','max_length':'用户名长度不能大于20'
    })
    email=forms.EmailField(label='邮箱',error_messages={'required':'邮箱不能为空','invalid':'邮箱格式不正确'})
    captcha=forms.CharField(label='验证码',max_length=4,min_length=4)
    password=forms.CharField(label='密码',max_length=20,min_length=6,error_messages={
        'required':'密码不能为空','min_length':'密码长度不能小于6','max_length':'密码长度不能大于20'
    })
    def clean_email(self):
        email=self.cleaned_data.get('email')
        exists=User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('邮箱已存在')
        return email
    def clean_captcha(self):
        captcha=self.cleaned_data.get('captcha')
        email=self.cleaned_data.get('email')

        captcha_model=CaptchaModel.objects.filter(email=email,captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError('验证码错误')
        captcha_model.delete()
        return captcha

class LoginForm(forms.Form):
    email = forms.EmailField(label='邮箱', error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式不正确'})
    password = forms.CharField(label='密码', max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)

