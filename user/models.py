from django.db import models
from django import forms

class user(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=10,primary_key=True)
    password = models.CharField(max_length=8)
    balance = models.IntegerField()
    loginscu = models.BooleanField()

    def __str__(self):
        return self.name +" - "+ self.username