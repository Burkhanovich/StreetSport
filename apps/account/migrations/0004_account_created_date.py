# Generated by Django 5.2 on 2025-04-08 05:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
