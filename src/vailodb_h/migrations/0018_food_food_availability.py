# Generated by Django 4.2.3 on 2024-04-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_h', '0017_room_list_hotel_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='Food_availability',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=100, null=True),
        ),
    ]
