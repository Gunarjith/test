# Generated by Django 4.2.3 on 2023-08-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vailodb_n', '0002_donation_settings_donation_contact_us_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation_details',
            old_name='email',
            new_name='donar_email',
        ),
        migrations.RenameField(
            model_name='donation_details',
            old_name='name',
            new_name='donar_name',
        ),
        migrations.RenameField(
            model_name='donation_details',
            old_name='pan_number',
            new_name='donar_pan_number',
        ),
        migrations.RenameField(
            model_name='donation_details',
            old_name='amount',
            new_name='donation_amount',
        ),
        migrations.AddField(
            model_name='donation_details',
            name='donar_phone_number',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='donation_details',
            name='donation_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donation_details',
            name='donation_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donation_details',
            name='donation_short_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donation_details',
            name='donation_type_image',
            field=models.ImageField(blank=True, null=True, upload_to='DonationTypeImage'),
        ),
    ]
