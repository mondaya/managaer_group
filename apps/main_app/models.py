from __future__ import unicode_literals
import re

from django.db import models

# Create your models here.

class Email(models.Model):
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
