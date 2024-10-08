# Generated by Django 4.0.5 on 2024-08-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0063_pre_inflow_settings_default_translation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflow_setup_details',
            name='open_button_type',
            field=models.CharField(blank=True, choices=[('CHAIN', 'chain'), ('IMAGE', 'image'), ('VIDEO', 'video'), ('DOCUMENT', 'document'), ('FORM', 'form'), ('PHONE', 'phone'), ('TEXT', 'text'), ('CARDS', 'cards'), ('TITLE', 'title'), ('URL', 'url'), ('LOCATION', 'location'), ('MAIN', 'main'), ('ATM/BRANCH', 'ATM/Branch'), ('EMI_CALCULATOR', 'EMI Calculator'), ('INTEREST_CALCULATOR', 'Interest Calculator'), ('RD_CALCULATOR', 'RD Calculator'), ('ELIGIBILITY_CALCULATOR', 'Eligibility Calculator 1'), ('SWP_CALCULATOR', 'SWP Calculator'), ('INFLATION_CALCULATOR', 'Inflation Calculator'), ('FD_CALCULATOR', 'FD, Calculator'), ('SIP_CALCULATOR', 'SIP Calculator')], max_length=200, null=True),
        ),
    ]
