# Generated by Django 4.1.2 on 2022-12-25 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_advertisement_price"),
    ]

    operations = [
        migrations.RemoveField(model_name="advertisement", name="comments",),
    ]
