# Generated by Django 4.2.3 on 2024-03-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0012_complaint_settings_complaint_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_rooms_type',
            name='Hotel_room_image',
            field=models.ImageField(blank=True, null=True, upload_to='RoomImage'),
        ),
    ]
