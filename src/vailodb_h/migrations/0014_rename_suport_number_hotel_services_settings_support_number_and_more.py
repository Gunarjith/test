# Generated by Django 4.2.3 on 2024-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0013_hotel_rooms_type_hotel_room_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel_services_settings',
            old_name='suport_number',
            new_name='support_number',
        ),
        migrations.AlterField(
            model_name='hotel_services_settings',
            name='key',
            field=models.CharField(blank=True, choices=[('SERVICES', 'hotel services'), ('FOOD', 'food'), ('NEARBY', 'nearby place'), ('ROOM', 'room'), ('FACILITIES', 'hotel facilities'), ('SELP HELP', 'self help'), ('INFORMATION', 'Information'), ('COMPLAINTS', 'Complaints')], max_length=100, null=True),
        ),
    ]
