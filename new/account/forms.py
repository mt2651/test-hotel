# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = (
#             'email', 
#             'username', 
#             'password',
#             'password2')


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'username')

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from account.models import CustomUser

ACCOUNT_ROLES_CHOICE = [
    ["client", "client"],
    ["owner", "owner"],
]

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    account_role = forms.ChoiceField(choices= ACCOUNT_ROLES_CHOICE)
    

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'account_role', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    # remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password']


# from django import forms
# import re
# from django.contrib.auth.models import User

# class RegistrationForm(forms.Form):
#     username = forms.CharField(label='Tài khoản', max_length=30)
#     email = forms.EmailField(label='Email')
#     password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

#     def clean_password2(self):
#         if 'password1' in self.cleaned_data:
#             password1 = self.cleaned_data['password1']
#             password2 = self.cleaned_data['password2']
#             if password1 == password2 and password1:
#                 return password2
#         raise forms.ValidationError("Mật khẩu không hợp lệ")

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         # if not re.search(r'^\w+&', username):
#         #     raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError("Tài khoản đã tồn tại")
    
#     def clean_email(self):
#         email = self.cleaned_data['email']

#         try:
#             User.objects.get(email=email)
#         except User.DoesNotExist:
#             return email
#         raise forms.ValidationError("Gmail đã tồn tại")

#     def save(self):
#         User.objects.create_user(
#             username=self.cleaned_data['username'], 
#             email=self.cleaned_data['email'], 
#             password=self.cleaned_data['password1']
#         )
