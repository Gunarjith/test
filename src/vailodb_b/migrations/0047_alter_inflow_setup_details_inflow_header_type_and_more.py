# Generated by Django 4.0.5 on 2024-07-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0046_remove_inflow_setup_details_child_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflow_setup_details',
            name='inflow_header_type',
            field=models.CharField(choices=[('none', 'NONE'), ('image', 'IMAGE'), ('text', 'TEXT'), ('carousel', 'CAROUSEL')], default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='template_info',
            name='template_header_type',
            field=models.CharField(choices=[('none', 'NONE'), ('image', 'IMAGE'), ('text', 'TEXT'), ('carousel', 'CAROUSEL')], default='none', max_length=100),
        ),
    ]
