# Generated by Django 5.1.1 on 2024-09-11 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_twitterpost_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitterpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='twitterpost',
            name='likes',
            field=models.ManyToManyField(related_name='post', to=settings.AUTH_USER_MODEL),
        ),
    ]
