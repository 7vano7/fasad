from django.db import models
from django import forms
from django.forms import ModelForm

class Language (models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_DISABLE = 'disable'

    LIST_STATUSES = ((STATUS_ACTIVE, STATUS_ACTIVE), (STATUS_DISABLE, STATUS_DISABLE))
    name = models.CharField(max_length=255, unique=True)
    iso_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50)
    main = models.CharField(max_length=50)

    def get_list(status = False):
         array = [('','--Select--'),]
         languages = Language.objects.all()
         if(languages):
            for lang in languages:
                array.append((lang.iso_code, lang.iso_code))
         return array





