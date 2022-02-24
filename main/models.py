from email.policy import default
from django.conf import settings
from django.db import models
from datetime import date, datetime 
import uuid
from django.contrib.auth.models import User


# Create your models here.


class Message(models.Model):
    message = models.TextField(blank=True, null=True)
    image = models.ImageField( blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    date_posted = models.DateTimeField(auto_now_add=True)
    time_posted = models.TimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    @property
    def num_likes(self):
        return self.likes.all().count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Message,
                             on_delete=models.CASCADE,
                             related_name='comments')
    username = models.CharField(max_length=20)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

