# Generated by Django 4.0.5 on 2024-07-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb', '0022_alter_admin_permission_client_service_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subuserpreference',
            old_name='history_preference',
            new_name='Menu_access',
        ),
        migrations.RenameField(
            model_name='subuserpreference',
            old_name='preference',
            new_name='service_type',
        ),
        migrations.AddField(
            model_name='subuserpreference',
            name='sub_Menu_access',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
