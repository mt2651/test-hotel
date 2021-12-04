from django.urls import path
from account import views
from django.contrib.auth import views as core_views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from account import views as core_views
from account.views import CustomLoginView  
from account.forms import LoginForm


# from .views import registration_view

urlpatterns = [
    path('', core_views.home, name='home'),
    path('signup/', core_views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
]
