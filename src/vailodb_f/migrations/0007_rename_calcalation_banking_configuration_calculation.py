# Generated by Django 4.0.5 on 2024-08-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_f', '0006_remove_banking_configuration_otp_required_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banking_configuration',
            old_name='calcalation',
            new_name='calculation',
        ),
    ]
