# Generated by Django 4.2.3 on 2024-04-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0015_alter_hotel_services_settings_support_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_rooms_type',
            name='l_room_type',
        ),
        migrations.RemoveField(
            model_name='hotel_rooms_type',
            name='room_availability',
        ),
        migrations.AddField(
            model_name='hotel_rooms_type',
            name='room_category',
            field=models.CharField(blank=True, choices=[('AC', 'ac'), ('NONAC', 'nonac')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='room_list',
            name='room_availability',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hotel_rooms_type',
            name='room_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
