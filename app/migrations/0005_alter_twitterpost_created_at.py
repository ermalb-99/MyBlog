# Generated by Django 5.1.1 on 2024-09-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_twitterpost_author_alter_twitterpost_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
