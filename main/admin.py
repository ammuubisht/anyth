

from django.contrib import admin

from main.models import Like, Message, Comment

# Register your models here.

admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Comment)
# admin.site.register(Person)

