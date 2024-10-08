# Generated by Django 4.2.3 on 2023-12-27 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vailodb_s', '0003_survey_question_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey_marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_type', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_category', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_location', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_description', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_contact_number', models.CharField(blank=True, max_length=300, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='survey_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_type', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='survey_categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_category', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace')),
            ],
        ),
        migrations.AddField(
            model_name='survey_customer',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace'),
        ),
        migrations.AddField(
            model_name='survey_customer_response',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace'),
        ),
        migrations.AddField(
            model_name='survey_list',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace'),
        ),
        migrations.AddField(
            model_name='survey_question',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace'),
        ),
        migrations.AddField(
            model_name='survey_question_map',
            name='marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_marketplace'),
        ),
    ]
