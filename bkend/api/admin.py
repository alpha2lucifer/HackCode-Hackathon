from django.contrib import admin
from .models import Udata

# Register your models here.
@admin.register(Udata)
class UserAdmin(admin.ModelAdmin):
    listdisplay = ['id', 'Uname', 'email']
