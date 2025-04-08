from django.db import models
from apps.account.models import Account

class Stadium(models.Model):
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(Account,on_delete=models.CASCADE,limit_choices_to={"role": 2},related_name="owned_stadiums")
    manager = models.ForeignKey(Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_stadiums",
        limit_choices_to={"role": 3}
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Stadium"
        verbose_name_plural = "Stadiums"


class StadiumImage(models.Model):
    stadium = models.ForeignKey(
        "Stadium",
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="media/stadium/")

    class Meta:
        verbose_name = "Stadium's image"
        verbose_name_plural = "Stadium's images"








