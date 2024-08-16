# Generated by Django 4.0.5 on 2024-07-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0048_form_field_required_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel_cards',
            name='location_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='carousel_cards',
            name='location_latitude',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='carousel_cards',
            name='location_longitude',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='carousel_cards',
            name='location_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='template_info_details',
            name='location_latitude',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='template_info_details',
            name='location_longitude',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
