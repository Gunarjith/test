# Generated by Django 4.0.5 on 2024-07-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_b', '0040_alter_inflow_setup_details_open_button_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_field',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text'), ('password', 'Password'), ('number', 'Number'), ('email', 'Email'), ('phone', 'Phone'), ('radio', 'radio'), ('checkbox', 'Checkbox'), ('dropdown', 'Dropdown')], max_length=50),
        ),
    ]
