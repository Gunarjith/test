# Generated by Django 4.2.3 on 2024-02-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0017_alter_subuserpreference_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebook_details',
            name='dynamic_file_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
