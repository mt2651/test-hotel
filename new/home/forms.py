from django import forms
from django.forms import fields
from home.models import User

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'fullname',
            'gender',
            'phonenumber',
            # 'cmnd',
        )
class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        # if not re.search(r'^\w+&', username):
        #     raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    
    def clean_email(self):
        email = self.cleaned_data['email']

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Gmail đã tồn tại")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'], 
            email=self.cleaned_data['email'], 
            password=self.cleaned_data['password1']
        )




