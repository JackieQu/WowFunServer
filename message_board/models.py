from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    index = models.IntegerField(default=0)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_time']