# Generated by Django 4.2.3 on 2024-04-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0018_food_food_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_services_settings',
            name='Advertisement_image',
            field=models.ImageField(blank=True, null=True, upload_to='ADImage'),
        ),
    ]
