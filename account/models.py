from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid4, editable=False)
