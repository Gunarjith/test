# Generated by Django 4.2.3 on 2024-01-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_a', '0015_appointment_marketplace_appointment_link_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_marketplace',
            name='payment_link_text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
