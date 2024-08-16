# Generated by Django 4.2.3 on 2023-12-26 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vailodb_n', '0009_donation_marketplace_donation_payment_settings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_ngo_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_ngo_type', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_n.donation_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='donation_ngo_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_ngo_category', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_n.donation_marketplace')),
            ],
        ),
    ]
