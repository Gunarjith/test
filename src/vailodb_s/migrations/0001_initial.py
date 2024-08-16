# Generated by Django 4.2.3 on 2023-10-18 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey_Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('customer_whatsapp_number', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_city', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_status', models.IntegerField(blank=True, null=True)),
                ('customer_address_line1', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_address_line2', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_address_landmark', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_address_pincode', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_state', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_country', models.CharField(blank=True, max_length=300, null=True)),
                ('customer_alternate_number', models.CharField(blank=True, max_length=300, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_image', models.ImageField(blank=True, null=True, upload_to='SurveyImage')),
                ('survey_message', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_footer', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_type', models.CharField(blank=True, max_length=500, null=True)),
                ('survey_status', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey_Question_Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('Survey_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_list')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=500, null=True)),
                ('response_option1', models.CharField(blank=True, max_length=500, null=True)),
                ('response_option2', models.CharField(blank=True, max_length=500, null=True)),
                ('response_option3', models.CharField(blank=True, max_length=500, null=True)),
                ('response_option4', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey_Customer_Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Survey_Response', models.CharField(blank=True, max_length=300, null=True)),
                ('Survey_comments', models.CharField(blank=True, max_length=300, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('Survey_Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_customer')),
                ('Survey_Question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_question')),
                ('Survey_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_list')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='survey_customer',
            name='Survey_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_s.survey_list'),
        ),
        migrations.AddField(
            model_name='survey_customer',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
