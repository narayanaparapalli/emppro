from __future__ import unicode_literals
from django.db import models
# Create your models here.
import datetime as dt
mdate = dt.datetime.now()
dur = dt.datetime.now()+dt.timedelta(days=730)

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=25)
    pcost = models.DecimalField(max_digits=10,decimal_places=2)
    pcolor = models.CharField(max_length=25,default='black')
    pmfd = models.DateTimeField(default=mdate)
    pexfd = models.DateTimeField(default=dur)

class Reg(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    user = models.CharField(primary_key=True,max_length=20)
    pwd = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=20,unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=25,blank=True,null=True)