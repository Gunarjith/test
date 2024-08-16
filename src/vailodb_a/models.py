from django.db import models
from django.contrib.auth.models import User
import pytz
# Create your models here.
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
CURRENCY_CHOICES = (
    ('INR', 'Rupees'),
    ('USD', 'DOLLAR'),
    ('GBP', 'Pounds'),
    ('EUR', 'Euros'),

)

class appointment_marketplace_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_flow_id = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    my_appointment_flow_id = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_image = models.ImageField(upload_to='FlowImage', null=True, blank=True)
    marketplace_welcome_message_body = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_message_footer = models.CharField(max_length=500, null=True, blank=True)
    generic_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    myappointment_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)


class appointment_marketplace(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=500, null=True, blank=True)
    group_type = models.CharField(max_length=500, null=True, blank=True)
    group_category = models.CharField(max_length=500, null=True, blank=True)
    group_location = models.CharField(max_length=500, null=True, blank=True)
    group_description = models.CharField(max_length=500, null=True, blank=True)
    group_contact_number = models.CharField(max_length=300, null=True, blank=True)
    group_id = models.CharField(max_length=300, null=True, blank=True)
    group_key = models.CharField(max_length=300, null=True, blank=True)
    appointment_url = models.CharField(max_length=300, null=True, blank=True)
    appointment_link_text = models.CharField(max_length=300, null=True, blank=True)
    payment_link_text = models.CharField(max_length=300, null=True, blank=True)


class appointment_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    welcome_image = models.ImageField(upload_to='ConsultantWelcomeImage', null=True, blank=True)
    welcome_message = models.CharField(max_length=500, null=True, blank=True)
    booking_button_name = models.CharField(max_length=500, null=True, blank=True)
    my_bookings_button_name = models.CharField(max_length=500, null=True, blank=True)
    contact_us_button_name = models.CharField(max_length=500, null=True, blank=True)
    main_support_number = models.CharField(max_length=300, null=True, blank=True)
    consultant_list_message = models.CharField(max_length=300, null=True, blank=True)
    consultant_list_button_name = models.CharField(max_length=300, null=True, blank=True)
    contactus_address = models.CharField(max_length=300, null=True, blank=True)
    contactus_image = models.ImageField(upload_to='ContactUsImage', null=True, blank=True)
    contactus_description = models.CharField(max_length=300, null=True, blank=True)
    appointment_url = models.CharField(max_length=300, null=True, blank=True)
    appointment_link_text = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Consultant_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    consultant_name = models.CharField(max_length=500, null=True, blank=True)
    consultant_photo = models.ImageField(upload_to='ConsultantPhoto', null=True, blank=True)
    consultant_image = models.ImageField(upload_to='ConsultantImage', null=True, blank=True)
    consultant_email = models.EmailField(max_length=200,null=True, blank=True)
    consultant_phone = models.CharField(max_length=300, null=True, blank=True)
    slot_duration = models.CharField(max_length=300, null=True, blank=True)
    consultant_specialization = models.CharField(max_length=300, null=True, blank=True)
    consultant_timezone = models.CharField(max_length=300, choices=TIMEZONES,
    default='UTC',null=True, blank=True)
    location_longitude = models.DecimalField(max_digits=18,decimal_places=15,null=True, blank=True)
    location_latitude = models.DecimalField(max_digits=18,decimal_places=15,null=True, blank=True)
    location_name = models.CharField(max_length=300, null=True, blank=True)
    location_address = models.CharField(max_length=300, null=True, blank=True)
    consultant_support_number = models.CharField(max_length=300, null=True, blank=True)
    approval_mode = models.CharField(max_length=300, null=True, blank=True)
    consultant_fee = models.IntegerField(null=True, blank=True)
    consultant_details = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Consultant_holiday_leaves(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Consultant_settings = models.ForeignKey(Consultant_details, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Consultant_availablity(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Consultant_settings = models.ForeignKey(Consultant_details, on_delete=models.CASCADE, null=True, blank=True)
    day_of_week = models.IntegerField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class appointment_visitor(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Visitor_Name = models.CharField(max_length=300, null=True, blank=True)
    Visitor_email = models.EmailField(max_length=200, null=True, blank=True)
    Visitor_Whatsapp_Number = models.CharField(max_length=300, null=True, blank=True)
    Visitor_City = models.CharField(max_length=300, null=True, blank=True)
    Visitor_Address_Line1 = models.CharField(max_length=300, null=True, blank=True)
    Visitor_Address_Line2 = models.CharField(max_length=300, null=True, blank=True)
    Visitor_Address_Landmark = models.CharField(max_length=300, null=True, blank=True)
    Visitor_Address_Pincode = models.CharField(max_length=300, null=True, blank=True)
    Visitor_State = models.CharField(max_length=300, null=True, blank=True)
    Visitor_Country = models.CharField(max_length=300, null=True, blank=True)
    Visitor_Phone_Number = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class appointment_bookings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Consultant_settings = models.ForeignKey(Consultant_details, on_delete=models.CASCADE, null=True, blank=True)
    Visitor = models.ForeignKey(appointment_visitor, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    online_offline = models.CharField(max_length=300, null=True, blank=True)
    notes1 = models.CharField(max_length=300, null=True, blank=True)
    notes2 = models.CharField(max_length=300, null=True, blank=True)
    booking_reference_id = models.CharField(max_length=200, null=True, blank=True)
    customer_phone_number = models.CharField(max_length=199,null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class appointment_payment_settings(models.Model):
    contact_name=models.CharField(max_length=200,null=True, blank=True)
    contact_number=models.CharField(max_length=200,null=True, blank=True)
    payment_gateway = models.CharField(max_length=200,null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class appointment_payment_gateway_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    payment_gateway = models.CharField(max_length=200, null=True, blank=True)
    gateway_id = models.CharField(max_length=200,null=True, blank=True)
    gateway_key = models.CharField(max_length=200,null=True, blank=True)
    currency = models.CharField(max_length=200, choices=CURRENCY_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class appointment_group_type(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    appointment_group_type = models.CharField(max_length=200,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class appointment_group_category(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(appointment_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    appointment_group_category = models.CharField(max_length=200,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
