from django.urls import path
from booking import views as bv
from django.contrib.auth import views as auth_views
from home import views as hv

urlpatterns = [
    path('', hv.Home_view, name='home'),
    path('search/', bv.Search_view, name='search'),
    path('booking/', bv.Booking_view, name='booking'),
    path('bookingconfirm/', bv.BookingConfirm_view, name='bookingconfirm'),
    path('cancelbooking/', bv.CancelBooking_view, name='cancelbooking'),

]