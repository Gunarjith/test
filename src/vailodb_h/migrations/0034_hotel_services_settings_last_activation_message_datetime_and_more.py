# Generated by Django 4.0.5 on 2024-08-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0033_hotel_settings_hotel_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_services_settings',
            name='last_activation_message_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel_services_settings',
            name='last_escalation_message_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
