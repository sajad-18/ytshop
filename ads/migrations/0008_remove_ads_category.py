# Generated by Django 5.0.2 on 2024-03-21 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_ads_verification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='category',
        ),
    ]
