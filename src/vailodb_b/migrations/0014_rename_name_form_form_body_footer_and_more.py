# Generated by Django 4.2.3 on 2024-03-06 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vailodb_b', '0013_form_form_field_form_section_form_fieldchoice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='name',
            new_name='form_body_footer',
        ),
        migrations.AddField(
            model_name='form',
            name='form_body_text',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='form_header_image',
            field=models.ImageField(blank=True, null=True, upload_to='FormImage'),
        ),
        migrations.AddField(
            model_name='form',
            name='form_header_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='form_header_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='form_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='form_open_button_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='form',
            name='form_submit_button_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='generic_campaign_history',
            name='Campaign_Form_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='template_info',
            name='template_body_message',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.CreateModel(
            name='Inflow_Setup_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parent_ID', models.CharField(blank=True, max_length=255, null=True)),
                ('open_button_type', models.CharField(blank=True, max_length=255, null=True)),
                ('open_button_name', models.CharField(blank=True, max_length=255, null=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_info', models.CharField(blank=True, max_length=300, null=True)),
                ('additional_file_path', models.FileField(blank=True, null=True, upload_to='InflowType')),
                ('inflow_header_type', models.CharField(blank=True, max_length=300, null=True)),
                ('inflow_header_text', models.CharField(blank=True, max_length=300, null=True)),
                ('inflow_header_file_path', models.FileField(blank=True, null=True, upload_to='InflowHeaderType')),
                ('inflow_body_text', models.CharField(blank=True, max_length=1024, null=True)),
                ('inflow_footer_text', models.CharField(blank=True, max_length=300, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_b.campaign_marketplace')),
            ],
        ),
    ]
