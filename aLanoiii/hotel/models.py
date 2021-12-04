from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from account.models import CustomUser
# Create your models here.
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="3t")
    # owner = models.CharField(max_length=20)
    owner = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="hcm")
    country = models.CharField(max_length=50,default="laos")
    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=30,default="P101")
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 
    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return self.hotel.name

def room_thumbnail_path(instance, filename):
    return f"{str(instance.room).replace(' ','_')}/{str(instance.room.name)}/{filename}"

def hotel_thumbnail_path(instance, filename):
    return f"{str(instance.hotel).replace(' ','_')}/{filename}"

ROOM_IMG_DEFAULT = 'hotel/room/default.png'

class ImageRoom(models.Model):
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    image = models.ImageField(upload_to =room_thumbnail_path, default=ROOM_IMG_DEFAULT)


class ImageHotel(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    image = models.ImageField(upload_to =hotel_thumbnail_path, default=ROOM_IMG_DEFAULT)
    # image = models.FileField(upload_to = 'static/')

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    
    booking_id = models.CharField(max_length=100,default="null")

    is_rate = models.BooleanField(default=0)
    def __str__(self):
        return self.guest.username

class Comments(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)   
    book = models.ForeignKey(Reservation, on_delete=models.CASCADE) 
    star = models.IntegerField()

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment to {} by {}".format(self.book.room, self.name)
