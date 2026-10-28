from django.db import models # type: ignore
import datetime
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User # type: ignore
# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True,)
    full_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.id}:{self.full_name}:{self.username}"