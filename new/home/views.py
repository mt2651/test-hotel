from django.shortcuts import redirect, render
#from home.forms import Signup, Login
from django.urls import reverse
from django.contrib import messages
#from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password,check_password
from home.forms import Login, Signup, RegistrationForm
from home.models import HotelOwner, User
from django.http import HttpResponseRedirect



# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# Create your views here.
def Home_view(request):
    return render(request, 'home.html')

def Signup_view(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # email = request.POST['email']
        # if User.objects.filter(username = username) and User.objects.filter(email = email):
        #     messages.warning('Account existed')
        # else:
        #     #ràng buộc cho các thuộc tính của guest khi nhập vào?
        #     guest = User()
        #     password = request.POST['password']
        #     guest.password = make_password(password)
        #     guest.fullname = request.POST['fullname']
        #     guest.gender = request.POST['gender']
        #     guest.phonenumber = request.POST['phonenumber']
        #     guest.save()
        #     signup_succes = reverse('signup_success')
        #     redirect(signup_succes)

        # if HotelOwner.objects.filter(username = username) and HotelOwner.objects.filter(email = email):
        #     messages.warning('')
        # else:
        #     #ràng buộc cho các thuộc tính của guest khi nhập vào?
        #     hotelowner = HotelOwner()
        #     password = request.POST['password']
        #     hotelowner.password = make_password(password)
        #     hotelowner.fullname = request.POST['fullname']
        #     hotelowner.gender = request.POST['gender']
        #     hotelowner.phonenumber = request.POST['phonenumber']
        #     hotelowner.save()
        #     signup_succes = reverse('signup_success')
        #     redirect(signup_succes)
        form = Signup()
        if form.is_valid(request.POST):
            form.save()
            return HttpResponseRedirect('../signup_succes.html')
    else:
        form = Signup()
    return render(
        request,
        'signup.html',
        {
            'form' : form
        }
    )

def Signup_success(request):
    return render(request, 'signup_success.html')


        # return render(request, 'signup.html')
    # return render(request, 'guest_signup.html')
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     if HotelOwner.objects.filter(username = username) and HotelOwner.objects.filter(email = email):
    #         messages.warning('')
    #     else:
    #         #ràng buộc cho các thuộc tính của guest khi nhập vào?
    #         hotelowner = HotelOwner()
    #         password = request.POST['password']
    #         hotelowner.password = make_password(password)
    #         hotelowner.fullname = request.POST['fullname']
    #         hotelowner.gender = request.POST['gender']
    #         hotelowner.phonenumber = request.POST['phonenumber']
    #         hotelowner.save()
    #         redirect('signup_success')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            signup_succes = reverse('signup_success')
            redirect(signup_succes)
    return render(request, 'signup.html', {'form': form})


# def HotelOwnerSignup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         if HotelOwner.objects.filter(username = username) and HotelOwner.objects.filter(email = email):
#             messages.warning('')
#         else:
#             #ràng buộc cho các thuộc tính của guest khi nhập vào?
#             hotelowner = HotelOwner()
#             password = request.POST['password']
#             hotelowner.password = make_password(password)
#             hotelowner.fullname = request.POST['fullname']
#             hotelowner.gender = request.POST['gender']
#             hotelowner.phonenumber = request.POST['phonenumber']
#             hotelowner.save()
#             redirect('signup_success')
#         return render(request, 'hotelowner_signup.html')
#     # return render(request, 'hotelowner_signup.html')

def Login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username):
            user = User.objects.filter(username=username)
            password_hash = user.password
            equal = check_password(password,password_hash)
            if equal == True:
                request.session['username'] = username
                return render(request,'home')
            else:
                messages.warning(request,"Incorrect Username/Password!")
                login = reverse('login')
                redirect(login)

        if HotelOwner.objects.filter(username=username):
            user = HotelOwner.objects.filter(username=username)
            password_hash = user.password
            equal = check_password(password,password_hash)
            if equal == True:
                request.session['username'] = username
                return render(request,'home')
            else:
                messages.warning(request,"Incorrect Username/Password!")
                login = reverse('login')
                redirect(login)
    else:
        form = Login
            # return render(request, 'guest_login')
    # return render(request, 'guest_login')

    return render(
        request, 
        'login.html',
        {
            'form' : form
        }
    )

# def HotelOwnerLogin_view(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         if HotelOwner.objects.filter(username=username):
#             user = HotelOwner.objects.filter(username=username)
#             password_hash = user.password
#             equal = check_password(password,password_hash)
#             if equal == True:
#                 request.session['username'] = username
#                 return render(request,'home')
#             else:
#                 messages.warning(request,"Incorrect Username/Password!")
#                 redirect('hotelowner_login')
#             return render(request, 'hotelowner_login')
#     # return render(request, 'hotelowner_login')

def Logout_view(request):
    if request.session.get('username', None):
        del request.session['username']
        return render(request,"home.html",{})

'''
def Signup_view(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successful registration!")
            return redirect('home')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = Signup()
    return render(
        request, 
        'signup.html', 
        {
            'form': form
        }
        )

def Login_view(request):       
    if request.method == 'POST':
        form = Login(request.POST)
        username = form.data.get('username')
        password = form.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('home')
        else:
            messages.error(request, "Invalid infomation")
    else:
        form = Login()
    return render(
        request,
        'login.html',
        {
            'form' : form
        }
    )

def Logout_view(request):
    #if request.method == 'POST':
    logout(request)
    return redirect('home')
'''
