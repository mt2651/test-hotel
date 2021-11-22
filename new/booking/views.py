from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from booking.models import Booking
from home.models import User
import datetime
# Create your views here.
def Search_view(request):
    #Lấy thành phố, số lượng người, ngày checkin checkout trong box rồi list ra những khách sạn còn phòng
    return render(request, 'search.html')
def Booking_view(request):
    if request.method=='POST':
        guest = request.POST['username']
        checkin_date = request.POST['checkin_date']
        checkout_date = request.POST['checkout_date']
        total_rooms = request.POST['total_rooms']
        total_guests = request.POST['total_guests']
        total_days = (checkout_date - checkin_date).days
        request.session['guest'] = guest 
        request.session['checkin_date'] = checkin_date
        request.session['checkout_date'] = checkout_date
        request.session['total_rooms'] = total_rooms
        request.session['total_guest'] = total_guests
        request.session['total_days'] = total_days
        return render(request, 'booking.html')
    else:
        return redirect('index')

def BookingConfirm_view(request):
    new_booking = Booking()
    username = request.session['username']
    new_booking.guest = User.objects.get(username=username)
    new_booking.booking_status = "B"
    new_booking.booking_date = datetime.datetime.today()
    new_booking.check_in_date = request.session['checkin_date']
    new_booking.check_out_date = request.session['checkout_date']
    new_booking.total_rooms = request.session['total_rooms']
    new_booking.total_guests = request.session['total_guests']
    '''
    new_booking.x; 
    **x: các thuộc tính của khách sạn như id, tên, ...
    '''
    new_booking.save()
    # Cập nhật lại số lượng phòng và loại phòng trong database?
    '''
    # Gửi email xác nhận đã đặt phòng tại khách sạn với số lượng là "", loại phòng là ""
    hotel_name = 
    email_acc 
    email = EmailMessage(to=[email_acc])
    email.send()
    '''
    return redirect(request, 'guest_dashboard.html')

def CancelBooking_view(request, id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    #Cập nhật lại số lượng và loại phòng trong database
    return HttpResponse("Your Booking Was Cancelled!")