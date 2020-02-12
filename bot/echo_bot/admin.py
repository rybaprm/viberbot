from django.contrib import admin

from .models import ViberUser, Message

admin.site.register(ViberUser)
admin.site.register(Message)
# Register your models here.
