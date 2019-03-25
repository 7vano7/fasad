from django.db import models
from django import forms

class Language (models.Model):
    name = models.CharField(max_length=255, unique=True)
    iso_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50)
    main = models.CharField(max_length=50)

