from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
    CHOICE_ROLE = {
        1:'Admin',
        2: 'Owner',
        3:'Manager',
        4: 'User',
    }
    role = models.SmallIntegerField(choices=CHOICE_ROLE,default=4)
    phone_number = models.CharField(max_length=15, unique=True)
    name=models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []





