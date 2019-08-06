from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Information(models.Model):
    index = models.IntegerField(default=0)
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_time']