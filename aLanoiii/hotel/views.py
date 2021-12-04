from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Comments, Hotels,Rooms,Reservation, ImageHotel, ImageRoom
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from account.models import CustomUser, Owner


def homepage(request):
    return HttpResponse(render(request,'index.html'))

def search(request):
    all_location = Hotels.objects.values_list('location','id').distinct().order_by()
    if request.method =="POST":
        try:
            print(request.POST)
            hotel = Hotels.objects.all().get(id=int(request.POST['search_location']))
            rr = []
            
            #for finding the reserved rooms on this time period for excluding from the query set
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.check_in) < str(request.POST['cin']) and str(each_reservation.check_out) < str(request.POST['cout']):
                    pass
                elif str(each_reservation.check_in) > str(request.POST['cin']) and str(each_reservation.check_out) > str(request.POST['cout']):
                    pass
                else:
                    rr.append(each_reservation.room.id)
                
            room = Rooms.objects.all().filter(hotel=hotel,capacity__gte = int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(request,"Sorry No Rooms Are Available on this time period")
            data = {'rooms':room,'all_location':all_location,'flag':True}
            response = render(request,'search.html',data)
        except Exception as e:
            messages.error(request,e)
            response = render(request,'search.html',{'all_location':all_location})

    else:
        data = {'all_location':all_location}
        response = render(request,'search.html',data)
    return HttpResponse(response)


#about
def aboutpage(request):
    return HttpResponse(render(request,'about.html'))


def accountprofile(request):
    return HttpResponse(render(request,'account.html'))


#contact page
def contactpage(request):
    return HttpResponse(render(request,'contact.html'))


# owner
def panel(request):
    
    if request.user.account_role == "client":
        return HttpResponse('Access Denied')

    user = CustomUser.objects.get(id=request.user.id)
    # print(f"request user id ={request.user.id}")
    # bookings = Reservation.objects.all().filter(guest=user) 

    # hotel_list = []
    # rooms = []

    hotel_list = Hotels.objects.filter(owner=user)
    # for hotel in hotel_list:
    #     rooms.append(hotel.rooms_set.all())


    rooms = Rooms.objects.filter(hotel__owner=user)


    # hotel_list = Hotels.objects.filter(owner=user)

    # for hotel in hotel_list:
    #     room_list
    # print(hotel_own)

    # hotel = Hotels.objects.all().filter(owner=user)

    # print(request.user.id)
    

    # print("all room" + str(rooms))

    # rooms2 = Rooms.objects.all()
    # print("all room2" + str(rooms2))

    total_rooms = len(rooms)
    if total_rooms == 0:
        total_rooms2 = 1
    else:
        total_rooms2 = total_rooms
    available_rooms = len(Rooms.objects.filter(status='1', hotel__owner=user))
    # available_rooms = len(Rooms.objects.fi)
    unavailable_rooms = len(Rooms.objects.all().filter(status='2', hotel__owner=user))
    reserved = len(Reservation.objects.filter(room__hotel__owner=user))

    hotel = Hotels.objects.filter(owner=user).values_list('location','id').distinct().order_by()
    if not rooms:
        messages.warning(request,"No Bookings Found")
    # response = render(request,'staff/panel.html',{'location':hotel,'reserved':reserved,'rooms':rooms,'total_rooms':total_rooms,'available':available_rooms,'unavailable':unavailable_rooms})
    # return HttpResponse(response)
    return HttpResponse(render(request,'staff/panel.html',{'location':hotel,'reserved':reserved,'rooms':rooms,'total_rooms':total_rooms,'available':available_rooms,'unavailable':unavailable_rooms, 'total_rooms2':total_rooms2}))
    # return HttpResponse(render(request, 'owner/panel.html', ))

def all_bookings(request):
    user = CustomUser.objects.get(id=request.user.id)

    # hotel = Hotels.objects.get(owner=user)

    # rooms = []
    # bookings = []

    # for hotel in hotel_list:
    #     rooms.append(hotel.room_set.all())
    # # print(f"request user id ={request.user.id}")

    # for room in rooms:
    #     bookings.append(Reservation.objects.filter(rooms=room))
    # # bookings = Reservation.objects.filter(guest=user)

    bookings = Reservation.objects.filter(room__hotel__owner=user)

    # bookings = Reservation.objects.all()
    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'staff/allbookings.html',{'bookings':bookings}))

def edit_room(request):
    if request.user.account_role == "client":   
        return HttpResponse('Access Denied')
    if request.method == 'POST' and request.user.account_role == "owner":
        print(request.POST)
        old_room = Rooms.objects.all().get(id= int(request.POST['roomid']))
        hotel = Hotels.objects.all().get(id=int(request.POST['hotel']))
        old_room.room_type  = request.POST['roomtype']
        old_room.capacity   =int(request.POST['capacity'])
        old_room.price      = int(request.POST['price'])
        old_room.size       = int(request.POST['size'])
        old_room.hotel      = hotel
        old_room.status     = request.POST['status']
        old_room.room_number=int(request.POST['roomnumber'])

        old_room.save()
        messages.success(request,"Room Details Updated Successfully")
        return redirect('staffpanel')
    else:
    
        room_id = request.GET['roomid']
        room = Rooms.objects.all().get(id=room_id)
        response = render(request,'staff/editroom.html',{'room':room})
        return HttpResponse(response)

def add_new_room(request):
    if request.user.account_role == "client":  
        return HttpResponse('Access Denied')
    if request.method == "POST":
        total_rooms = len(Rooms.objects.all())
        new_room = Rooms()
        hotel = Hotels.objects.all().get(id = int(request.POST['hotel']))
        print(f"id={hotel.id}")
        print(f"name={hotel.name}")

        new_room.name       = request.POST['name']
        new_room.roomnumber = total_rooms + 1
        new_room.room_type  = request.POST['roomtype']
        new_room.capacity   = int(request.POST['capacity'])
        new_room.size       = int(request.POST['size'])
        new_room.capacity   = int(request.POST['capacity'])
        new_room.hotel      = hotel
        new_room.status     = request.POST['status']
        new_room.price      = request.POST['price']

        new_room.save()
        
        # images = request.Files.getlist('images')
        images = request.FILES
        for image in images:
            # photo = ImageRoom.objects.create(image=image, room = new_room)
            photo = ImageRoom()
            photo.image  = image
            photo.room   = new_room
            photo.save()


        messages.success(request,"New Room Added Successfully")
    
    return redirect('staffpanel')

def view_room_staff(request):
    room_id = request.GET['roomid']
    room = Rooms.objects.all().get(id=room_id)

    reservation = Reservation.objects.all().filter(room=room)
    return HttpResponse(render(request,'staff/viewroom.html',{'room':room,'reservations':reservation}))


def view_room_user(request):
    room_id = request.GET['roomid']
    room = Rooms.objects.all().get(id=room_id)

    reservation = Reservation.objects.all().filter(room=room)

    comment = Comments.objects.filter(book__room=room)

    return HttpResponse(render(request,'user/viewroom.html',{'room':room,'reservations':reservation, 'comments':comment}))


def add_new_location(request):
    if request.method == "POST" and request.user.account_role == "owner":  
        name = request.POST['new_hotel']
        location = request.POST['new_city']
        state = request.POST['new_state']
        country = request.POST['new_country']
        
        hotels = Hotels.objects.all().filter(name=name, state=state)
        if hotels:
            messages.warning(request,"Sorry City at this Hotel already exist")
            return redirect("staffpanel")
        else:
            new_hotel = Hotels()
            new_hotel.name = name
            new_hotel.owner = request.user
            new_hotel.location = location
            new_hotel.state = state
            new_hotel.country = country
            new_hotel.save()
            images = request.FILES.getlist('images')
            for image in images:
                photo = ImageHotel.objects.create(image=image, hotel=new_hotel)
                photo.save()

            messages.success(request,"New Location Has been Added Successfully")
            return redirect("staffpanel")
            

    else:
        return HttpResponse("Not Allowed")


# client

def book_room_page(request):
    room = Rooms.objects.all().get(id=int(request.GET['roomid']))
    return HttpResponse(render(request,'user/bookroom.html',{'room':room}))

def book_room(request):
    
    if request.method =="POST":

        room_id = request.POST['room_id']
        
        room = Rooms.objects.all().get(id=room_id)
        #for finding the reserved rooms on this time period for excluding from the query set
        for each_reservation in Reservation.objects.filter(room = room):
            if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
                pass
            elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request,"Sorry This Room is unavailable for Booking")
                return redirect("homepage")
            
        current_user = request.user
        total_person = int( request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        room_object = Rooms.objects.get(id=room_id)
        room_object.status = '2'
        
        user_object = CustomUser.objects.get(username=current_user)

        reservation.guest = user_object
        reservation.room = room_object
        person = total_person
        reservation.check_in = request.POST['check_in']
        reservation.check_out = request.POST['check_out']
        reservation.booking_id = booking_id
        reservation.save()

        messages.success(request,"Congratulations! Booking Successfull")

        return redirect("homepage")
    else:
        return HttpResponse('Access Denied')

def user_bookings(request):
    if request.user.is_authenticated == False:
        return redirect('homepage')
    user = CustomUser.objects.get(id=request.user.id)
    # print(f"request user id ={request.user.id}")
    bookings = Reservation.objects.filter(guest=user)
    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'user/mybookings.html',{'bookings':bookings}))

def vote_room(request):
    booking = Reservation.objects.all().get(id=int(request.GET['book_id']))
    return HttpResponse(render(request,'user/vote.html',{'booking':booking}))

def user_vote(request):
    if request.method =="POST":

        book_id = request.POST['book_id']

        reser = Reservation.objects.get(id=book_id)
        reser.is_rate = 1
        reser.save()
        
        # room = Rooms.objects.all().get(id=room_id)
        # #for finding the reserved rooms on this time period for excluding from the query set
        # for each_reservation in Reservation.objects.filter(room = room):
        #     if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
        #         pass
        #     elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
        #         pass
        #     else:
        #         messages.warning(request,"Sorry This Room is unavailable for Booking")
        #         return redirect("homepage")
            
        current_user = request.user
        # total_person = int( request.POST['person'])
        # booking_id = str(room_id) + str(datetime.datetime.now())

        # reservation = Reservation()
        # room_object = Rooms.objects.get(id=room_id)
        # room_object.status = '2'
        
        user_object = CustomUser.objects.get(username=current_user)

        cmt = Comments()
        cmt.name = user_object
        cmt.body = request.POST['cmt']
        cmt.book = reser
        cmt.star = int(request.POST['star'])
        cmt.save()

        # print(request.POST)



        # reservation.guest = user_object
        # reservation.room = room_object
        # person = total_person
        # reservation.check_in = request.POST['check_in']
        # reservation.check_out = request.POST['check_out']
        # reservation.booking_id = booking_id
        # reservation.save()

        messages.success(request,"Congratulations! Vote Successfull")

        return redirect("dashboard")
    else:
        return HttpResponse('Access Denied')
    # room = Rooms.objects.all().get(id=int(request.GET['book_id']))

    # return HttpResponse(render(request, 'user/vote.html', {'room':room}))


# def user_votings(request):
#     if request.user.is_authenticated == False:
#         return redirect('homepage')
#     user = CustomUser.objects.get(id=request.user.id)
#     # print(f"request user id ={request.user.id}")
#     bookings = Reservation.objects.filter(guest=user)
#     if not bookings:
#         messages.warning(request,"No Bookings Found")
#     return HttpResponse(render(request,'user/mybookings.html',{'bookings':bookings}))
    