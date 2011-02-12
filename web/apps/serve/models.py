from django.db import models

# Create your models here.
class Attachment(models.Model):
    name = models.CharField(max_length=24, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_view = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
