from django.contrib.auth.models import User
from django.db import models




class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'