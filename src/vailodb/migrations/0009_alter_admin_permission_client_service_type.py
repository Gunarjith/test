# Generated by Django 4.2.3 on 2023-10-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0008_alter_admin_permission_client_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_permission',
            name='client_service_type',
            field=models.CharField(choices=[('commerce', 'COMMERCE'), ('ticket', 'TICKET'), ('scanner', 'SCANNER'), ('donation', 'DONATION'), ('appointement', 'APPOINTEMENT'), ('survey', 'SURVEY')], default='none', max_length=200),
        ),
    ]
