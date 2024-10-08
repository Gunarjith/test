# Generated by Django 4.0.5 on 2024-07-19 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0041_alter_form_field_field_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vailodb_f', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banking_configuration',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.campaign_marketplace'),
        ),
        migrations.CreateModel(
            name='Branch_ATM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PIN_code', models.IntegerField(blank=True, max_length=20, null=True)),
                ('IFSC_code', models.CharField(blank=True, max_length=50, null=True)),
                ('Services', models.CharField(blank=True, choices=[('ATM', 'ATM'), ('BRANCH', 'BRANCH'), ('BOTH', 'BOTH')], max_length=20, null=True)),
                ('Address', models.CharField(blank=True, max_length=500, null=True)),
                ('landmark', models.CharField(blank=True, max_length=500, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.campaign_marketplace')),
            ],
        ),
    ]
