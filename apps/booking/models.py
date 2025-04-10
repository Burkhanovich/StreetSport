from django.utils import timezone

from django.db import models
from jsonschema.exceptions import ValidationError

from apps.account.models import Account
from apps.stadium.models import Stadium

class Booking(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="bookings", verbose_name="booking_user",)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name="bookings", verbose_name="Stadium",)
    start_time = models.DateTimeField(verbose_name='starting_time', )
    end_time = models.DateTimeField(verbose_name='end_time')
    created_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.start_time>=self.end_time:
            raise ValidationError('The end time must be after the start time.')
        if self.start_time<timezone.now():
            raise ValidationError("The booking time cannot be in the past.")

        overlapping_bookings = Booking.objects.filter(
            stadium=self.stadium,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(id=self.id)

        if overlapping_bookings.exists():
            raise ValidationError("The stadium is already booked for this time period.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



