# Generated by Django 4.2.3 on 2023-08-08 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0004_remove_subuserpreference_campaign_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_permission',
            name='client_service_type',
            field=models.CharField(choices=[('commerce', 'COMMERCE'), ('ticket', 'TICKET'), ('scanner', 'SCANNER'), ('donation', 'DONATION')], default='none', max_length=200),
        ),
    ]
