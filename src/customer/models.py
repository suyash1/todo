from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'customer'
