from django.db import models

class Page(models.Model):

    STATUS_ACTIVE = 'active'
    STATUS_DISABLE = 'disable'
    LIST_STATUSES = ((STATUS_ACTIVE, STATUS_ACTIVE), (STATUS_DISABLE, STATUS_DISABLE))

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=LIST_STATUSES)

class PageLang(models.Model):

    title=models.CharField(max_length=50, blank=True, default=None)
    content=models.TextField(blank=True, default=None)
    lang=models.CharField(max_length=3)
    page_id=models.IntegerField()
    description=models.CharField(max_length=255, blank=True, default=None)
    keywords=models.TextField(blank=True, default=None)
