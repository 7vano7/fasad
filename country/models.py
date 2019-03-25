from django.db import models
from django import forms

class Country (models.Model):
    iso_code = models.CharField(max_length=50)
    phone_code = models.CharField(max_length=50)
    name = models.CharField(max_length=255, unique=True)

