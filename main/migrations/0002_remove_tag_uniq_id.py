# Generated by Django 4.2 on 2023-04-20 06:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="uniq_id",
        ),
    ]
