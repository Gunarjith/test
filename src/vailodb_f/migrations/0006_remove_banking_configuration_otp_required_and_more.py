# Generated by Django 4.0.5 on 2024-08-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_f', '0005_remove_branch_atm_pin_code_flow_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banking_configuration',
            name='Otp_required',
        ),
        migrations.RemoveField(
            model_name='banking_configuration',
            name='Terms_of_use',
        ),
        migrations.AddField(
            model_name='banking_configuration',
            name='calcalation',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
