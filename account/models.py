from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
ACCOUNT_ROLES = [
    "client",
    "owner"
]

ACCOUNT_ROLES_CHOICE = [
    ["client", "client"],
    ["onwer", "onwer"],
]


class CustomUser(AbstractUser):

    username    = models.CharField(max_length=32, unique=True)
    email       = models.EmailField(max_length=64, unique=True)
    is_valid    = models.BooleanField(default=False)
    phone       = models.CharField(max_length=11, default="")
    account_role = models.CharField(max_length=12, choices=ACCOUNT_ROLES_CHOICE)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.client_set.all() \
            or self.onwer_set.all():
            return

        if self.account_role == "client":
            client = Client(user=self)
            client.save()
        elif self.account_role == "owner":
            owner = Owner(user=self)
            owner.save()
        else:
            print("Invalid User")


class Client(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Owner(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    income = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username