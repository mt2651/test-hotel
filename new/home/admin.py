from django.contrib import admin
from home.models import User
# Register your models here.
@admin.register(User)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fullname', 'phonenumber')
    search_fields = ('username', 'email', 'fullname', 'phonenumber')