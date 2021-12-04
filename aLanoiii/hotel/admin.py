from django.contrib import admin
from .models import Hotels,Rooms,Reservation,Comments,ImageHotel,ImageRoom
# Register your models here.

admin.site.register(Hotels)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Comments)
admin.site.register(ImageRoom)
admin.site.register(ImageHotel)