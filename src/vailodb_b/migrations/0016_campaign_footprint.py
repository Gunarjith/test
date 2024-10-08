# Generated by Django 4.2.3 on 2024-03-14 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vailodb_b', '0015_inflow_setup_details_additional_file_path1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='campaign_footprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('From_number', models.CharField(blank=True, max_length=300, null=True)),
                ('button', models.CharField(blank=True, max_length=300, null=True)),
                ('campaign_name', models.CharField(blank=True, max_length=300, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.campaign_marketplace')),
            ],
        ),
    ]
