# Generated by Django 4.0.5 on 2024-08-02 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vailodb_b', '0055_alter_carousel_cards_carousel_button1_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pre_inflow_settings',
            name='LanguagePref',
            field=models.CharField(blank=True, choices=[('NO', 'Not Required'), ('FIRSTTIME', 'First Time Required'), ('ALWAYS', 'Always Required')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pre_inflow_settings',
            name='otp_flow_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carousel_cards',
            name='number_of_cards',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='none', max_length=100),
        ),
        migrations.CreateModel(
            name='User_Prepared_Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selected_language_name', models.CharField(blank=True, max_length=100, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('Selected_language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.language_value')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.campaign_marketplace')),
            ],
        ),
    ]
