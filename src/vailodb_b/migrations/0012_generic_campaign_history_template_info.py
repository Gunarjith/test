# Generated by Django 4.2.3 on 2024-02-28 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0011_generic_campaign_history_customer_whatsapp_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='generic_campaign_history',
            name='template_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.template_info'),
        ),
    ]
