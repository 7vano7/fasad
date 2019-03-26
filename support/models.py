from django.db import models
from django.utils import timezone

class Support(models.Model):
    STATUS_QUESTION = 'question'
    STATUS_ANSWERED = 'answered'

    LIST_STATUSES = ((STATUS_QUESTION, STATUS_QUESTION),(STATUS_ANSWERED, STATUS_ANSWERED))

    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    content=models.TextField()
    user=models.IntegerField(blank=True, default=None)
    question_id=models.IntegerField(default=None)
    status = models.CharField(max_length=50, choices=LIST_STATUSES, blank=True, default=None)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(blank=True, default=None)

