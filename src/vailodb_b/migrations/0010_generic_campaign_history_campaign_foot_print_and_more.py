# Generated by Django 4.2.3 on 2024-02-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0009_generic_campaign_info_default_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='generic_campaign_history',
            name='Campaign_Foot_Print',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generic_campaign_history',
            name='Campaign_Status',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
