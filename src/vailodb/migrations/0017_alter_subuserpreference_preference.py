# Generated by Django 4.2.3 on 2024-02-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0016_facebook_details_private_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subuserpreference',
            name='preference',
            field=models.CharField(blank=True, choices=[('donation', 'Donation'), ('ticket', 'TICKET'), ('scanner', 'SCANNER'), ('campaign', 'CAMPAIGN'), ('hotel', 'HOTEL')], max_length=300, null=True),
        ),
    ]
