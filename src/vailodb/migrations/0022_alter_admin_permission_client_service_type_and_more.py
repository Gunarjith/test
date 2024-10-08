# Generated by Django 4.2.3 on 2024-04-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0021_facebook_details_fb_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_permission',
            name='client_service_type',
            field=models.CharField(choices=[('commerce', 'COMMERCE'), ('ticket', 'TICKET'), ('scanner', 'SCANNER'), ('donation', 'DONATION'), ('appointement', 'APPOINTEMENT'), ('survey', 'SURVEY'), ('hotel', 'HOTEL'), ('campaign', 'CAMPAIGN'), ('malls', 'MALLS')], default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='subuserpreference',
            name='preference',
            field=models.CharField(blank=True, choices=[('donation', 'Donation'), ('ticket', 'TICKET'), ('scanner', 'SCANNER'), ('campaign', 'CAMPAIGN'), ('hotel', 'HOTEL'), ('malls', 'MALLS')], max_length=300, null=True),
        ),
    ]
