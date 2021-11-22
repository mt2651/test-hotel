from django.contrib import admin

from account.models import (
    CustomUser,
    Client, Owner
)


admin.site.register(CustomUser)
admin.site.register(Client)
admin.site.register(Owner)

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fullname', 'phonenumber')
    search_fields = ('username', 'email', 'fullname', 'phonenumber')