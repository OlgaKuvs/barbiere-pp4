# Generated by Django 3.2.21 on 2023-10-16 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_auto_20230917_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='duration',
        ),
    ]