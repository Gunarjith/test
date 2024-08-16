# Generated by Django 4.2.3 on 2023-08-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0005_alter_admin_permission_client_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subuserpreference',
            name='preference',
            field=models.CharField(blank=True, choices=[('donation', 'Donation'), ('ticket', 'TICKET'), ('scanner', 'SCANNER'), ('campaign', 'CAMPAIGN')], max_length=300, null=True),
        ),
    ]
