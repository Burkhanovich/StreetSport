from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
    CHOICE_ROLE = {
        1:'Admin',
        2:'Manager',
        3: 'User',
        4: 'Owner'
    }
    role = models.SmallIntegerField(choices=CHOICE_ROLE,default=3)
    phone_number = models.CharField(max_length=15, unique=True)
    name=models.CharField(max_length=15)






