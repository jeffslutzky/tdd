from django.db import models
import uuid

class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'

class Token(models.Model):
    email = models.EmailField(default='')
    uid = models.CharField(default=uuid.uuid4, max_length=40)