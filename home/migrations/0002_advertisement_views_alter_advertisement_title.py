# Generated by Django 4.1.2 on 2023-02-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="advertisement",
            name="views",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="advertisement",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
