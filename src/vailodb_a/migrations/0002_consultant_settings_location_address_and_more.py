# Generated by Django 4.2.3 on 2023-09-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_a', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultant_settings',
            name='location_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='consultant_settings',
            name='location_latitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='consultant_settings',
            name='location_longitude',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=18, null=True),
        ),
        migrations.AddField(
            model_name='consultant_settings',
            name='location_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
