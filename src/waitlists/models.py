from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class WaitlistEntry(models.Model):
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)