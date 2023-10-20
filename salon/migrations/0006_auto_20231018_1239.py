# Generated by Django 3.2.21 on 2023-10-18 12:39

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0005_remove_service_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='barber',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
    ]