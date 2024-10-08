# Generated by Django 4.2.3 on 2024-01-06 05:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_type', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_category', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_location', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_description', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_url', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_link_text', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_id', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_key', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_contact_number', models.CharField(blank=True, max_length=300, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Selfhelp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selfhelp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('selfhelp_discription', models.CharField(blank=True, max_length=500, null=True)),
                ('selfhelp_image', models.ImageField(upload_to='Image')),
                ('selfhelp_video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Nearby_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_type', models.CharField(blank=True, choices=[('AIRPORT', 'airport'), ('HISTORICAL', 'historical'), ('HOSPITAL', 'hospital'), ('METRO', 'metro'), ('MUSEUM', 'museum'), ('RAILWAY STATION', 'railway station'), ('TEMPLE', 'temple'), ('WATER FALLS', 'Water falls'), ('ZOO', 'zoo')], max_length=100, null=True)),
                ('place_name', models.CharField(blank=True, max_length=100, null=True)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('distance_unit', models.CharField(blank=True, choices=[('KM', 'kilometers'), ('MILES', 'miles')], max_length=200, null=True)),
                ('Discription', models.CharField(blank=True, max_length=500, null=True)),
                ('place_image', models.ImageField(blank=True, null=True, upload_to='Image')),
                ('place_video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_name', models.CharField(blank=True, max_length=100, null=True)),
                ('information_discription', models.CharField(blank=True, max_length=500, null=True)),
                ('information_image', models.ImageField(upload_to='Image')),
                ('information_video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_address', models.CharField(max_length=500)),
                ('hotel_image', models.ImageField(blank=True, null=True, upload_to='Image')),
                ('hotel_video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('hotel_url', models.CharField(blank=True, max_length=500, null=True)),
                ('hotel_link_text', models.CharField(blank=True, max_length=500, null=True)),
                ('contact_us', models.IntegerField(blank=True, null=True)),
                ('contact_one', models.IntegerField(blank=True, null=True)),
                ('contact_two', models.IntegerField(blank=True, null=True)),
                ('contact_three', models.IntegerField(blank=True, null=True)),
                ('checkIn', models.TimeField(blank=True, null=True)),
                ('checkout', models.TimeField(blank=True, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('service_discription', models.CharField(blank=True, max_length=500, null=True)),
                ('service_image', models.ImageField(upload_to='Image')),
                ('service_video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=100)),
                ('room_floor', models.CharField(max_length=100)),
                ('room_type', models.CharField(blank=True, choices=[('AC', 'ac'), ('NONAC', 'nonac')], max_length=100, null=True)),
                ('bed', models.CharField(blank=True, max_length=100, null=True)),
                ('room_price', models.IntegerField(blank=True, null=True)),
                ('room_price_unit', models.CharField(blank=True, choices=[('EUR', 'Euros'), ('GBP', 'British Pound'), ('INR', 'Indian Rupees'), ('USD', 'US Dollar')], max_length=100, null=True)),
                ('room_info', models.CharField(blank=True, max_length=500, null=True)),
                ('l_room_type', models.CharField(blank=True, max_length=100, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_marketplace_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_flow_id', models.CharField(blank=True, max_length=500, null=True)),
                ('specific_flow_id', models.CharField(blank=True, max_length=500, null=True)),
                ('my_hotel_flow_id', models.CharField(blank=True, max_length=500, null=True)),
                ('marketplace_welcome_image', models.ImageField(blank=True, null=True, upload_to='FlowImage')),
                ('marketplace_welcome_message_body', models.CharField(blank=True, max_length=500, null=True)),
                ('marketplace_welcome_message_footer', models.CharField(blank=True, max_length=500, null=True)),
                ('generic_flow_cta_name', models.CharField(blank=True, max_length=500, null=True)),
                ('specific_flow_cta_name', models.CharField(blank=True, max_length=500, null=True)),
                ('myhotel_flow_cta_name', models.CharField(blank=True, max_length=500, null=True)),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(blank=True, max_length=100, null=True)),
                ('facility_location', models.CharField(blank=True, max_length=100, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('discription', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='Image')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(blank=True, max_length=100, null=True)),
                ('food_price', models.IntegerField(blank=True, null=True)),
                ('food_type', models.CharField(blank=True, choices=[('NONVEG', 'nonveg'), ('VEG', 'veg')], max_length=100, null=True)),
                ('food_discription', models.CharField(blank=True, max_length=500, null=True)),
                ('food_category', models.CharField(blank=True, max_length=100, null=True)),
                ('food_cuisine', models.CharField(blank=True, max_length=100, null=True)),
                ('food_image', models.ImageField(blank=True, null=True, upload_to='Image')),
                ('food_video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('vailo_record_creation', models.DateTimeField(auto_now_add=True)),
                ('vailo_record_last_update', models.DateTimeField(auto_now=True)),
                ('vailo_record_status', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('marketplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vailodb_h.hotel_marketplace')),
            ],
        ),
    ]
