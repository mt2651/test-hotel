# from django.urls import path
# from account import ac_views
# from django.contrib.auth import views as core_views
# from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views

"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
import hotel.views as views
urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('home', views.homepage,name="home"),
    path('search/', views.search,name="search"),
    path('about', views.aboutpage,name="aboutpage"),
    path('contact', views.contactpage,name="contactpage"),
    path('accounts/profile/', views.accountprofile, name='accountsprofile'),

    # path('client', views.user_log_sign_page,name="userloginpage"),
    # path('client/login', views.user_log_sign_page,name="userloginpage"),
    path('user/bookings', views.user_bookings,name="dashboard"),
    path('user/book-room', views.book_room_page,name="bookroompage"),
    path('user/book-room/book', views.book_room,name="bookroom"),
    path('user/view-room', views.view_room_user),
    path('user/vote-room', views.vote_room, name="voteroom"),
    path('user/vote-room/vote', views.user_vote, name="vote"),
    # path('client/signup', views.user_sign_up,name="usersignup"),

    # path('owner/', views.staff_log_sign_page,name="staffloginpage"),
    # path('owner/login', views.staff_log_sign_page,name="staffloginpage"),
    # path('owner/signup', views.staff_sign_up,name="staffsignup"),
    # path('logout', views.logoutuser,name="logout"),
    path('staff/panel', views.panel,name="staffpanel"),
    path('staff/allbookings', views.all_bookings,name="allbookigs"),
    # path('search/', views.search, name='search'),
    path('staff/panel/add-new-location', views.add_new_location,name="addnewlocation"),
    path('staff/panel/edit-room', views.edit_room),
    path('staff/panel/add-new-room', views.add_new_room,name="addroom"),
    path('staff/panel/edit-room/edit', views.edit_room),
    path('staff/panel/view-room', views.view_room_staff),

    # path('admin/', admin.site.urls),
    

]
