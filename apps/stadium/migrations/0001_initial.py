# Generated by Django 5.2 on 2025-04-08 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('manager', models.ForeignKey(blank=True, limit_choices_to={'role': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_stadiums', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(limit_choices_to={'role': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='owned_stadiums', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stadium',
                'verbose_name_plural': 'Stadiums',
            },
        ),
        migrations.CreateModel(
            name='StadiumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/stadium/')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='stadium.stadium')),
            ],
            options={
                'verbose_name': "Stadium's image",
                'verbose_name_plural': "Stadium's images",
            },
        ),
    ]
