# Generated by Django 5.1.1 on 2024-09-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_bio_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='content',
            field=models.TextField(max_length=300),
        ),
    ]
