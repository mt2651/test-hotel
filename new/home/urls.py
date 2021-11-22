from django.urls import path
from home import views
from django.contrib.auth import views as auth_views


# from .views import registration_view

urlpatterns = [
    path('', views.Home_view, name='home'),
    # path('signup/', views.Signup_view, name='signup'),
    # path('signup', RegisterAPI.as_view(), name='signup'),
    path('register1/', views.register, name="signup"),
    # path('signup', registration_view, name='signup'),
    # path('hotel-owner-signup/', views.HotelOwnerSignup_view, name='hotelowner_signup'),
    path('login1/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout1/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    # path('logout/',knox_views.LogoutView.as_view(), name='logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('signup_1success/', views.Signup_success, name='signup_success'),
]
