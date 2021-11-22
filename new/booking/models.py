from django.db import models

from home.models import User

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    #hotel = models.ForeignKey("model of hotel here")
    booking_status_choices = (
        ('A', 'Availed'),
        ('B', 'Booked'),
        ('C1', 'Cancelled by user'),
        ('C2', 'Cancelled by hotel')
    )
    booking_status = models.CharField(max_length=2, choices=booking_status_choices)
    booking_date = models.DateField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    #room = models.ForeignKey("model of room here")
    total_rooms = models.PositiveIntegerField(default=0)
    total_guests = models.PositiveIntegerField(default=0)
    total_days = models.PositiveIntegerField(default=0)
    def __str__(self):
        return "Booking ID: "+str(self.booking_id)