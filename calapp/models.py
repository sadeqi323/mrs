from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CalIn(models.Model):
    text = models.CharField(max_length=255)
    amount = models.IntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class CalOut(models.Model):
    text = models.CharField(max_length=255)
    amount = models.IntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
