from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=255)
    gender_choice = [
        ('M', 'Nam'),
        ('F', 'Nữ')
    ]
    gender = models.CharField(max_length=1, choices=gender_choice, default='M')
    phonenumber = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username

class HotelOwner(models.Model):
    username = models.CharField(primary_key=True, max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=255)
    gender_choice = [
        ('M', 'Nam'),
        ('F', 'Nữ')
    ]
    gender = models.CharField(max_length=1, choices=gender_choice, default='M')
    phonenumber = models.CharField(max_length=10)
    def __str__(self):
        return self.username