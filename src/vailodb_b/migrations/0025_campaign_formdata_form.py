# Generated by Django 4.2.3 on 2024-03-26 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0024_campaign_groups_campaign_group_customer_mappings'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign_formdata',
            name='Form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.form'),
        ),
    ]
