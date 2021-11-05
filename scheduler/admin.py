from django.contrib import admin
from django.contrib.auth.models import User
from scheduler.models import TimeSlot, CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('is_staff', 'is_superuser')


admin.site.register(TimeSlot)

# admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)
