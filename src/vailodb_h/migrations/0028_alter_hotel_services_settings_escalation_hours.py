# Generated by Django 4.0.5 on 2024-07-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0027_rename_message_header_image_notification_message_image_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_services_settings',
            name='escalation_hours',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
