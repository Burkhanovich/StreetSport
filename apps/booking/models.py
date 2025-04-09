from django.db import models
from apps.account.models import Account
from apps.stadium.models import Stadium

class Booking(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="bookings", verbose_name="booking_user",)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name="bookings", verbose_name="Stadium",)
    start_time = models.DateTimeField()


