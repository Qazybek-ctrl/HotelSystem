# Generated by Django 4.1.7 on 2023-03-07 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookingapp", "0002_remove_room_amount_of_day_remove_room_start_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="is_available",
        ),
    ]
