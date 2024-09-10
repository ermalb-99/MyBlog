# Generated by Django 5.1.1 on 2024-09-10 09:53

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_twitterpost_likes_delete_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitterpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='twitterpost',
            name='likes',
            field=models.IntegerField(blank=True, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
