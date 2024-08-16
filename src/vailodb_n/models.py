from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CURRENCY_CHOICES = (
    ('INR', 'Rupees'),
    ('USD', 'DOLLAR'),
    ('GBP', 'Pounds'),
    ('EUR', 'Euros'),

)

class donation_marketplace_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_flow_id = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    my_donation_flow_id = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_image = models.ImageField(upload_to='FlowImage', null=True, blank=True)
    marketplace_welcome_message_body = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_message_footer = models.CharField(max_length=500, null=True, blank=True)
    generic_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    mydonation_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)


class donation_marketplace(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    ngo_name = models.CharField(max_length=500, null=True, blank=True)
    ngo_type = models.CharField(max_length=500, null=True, blank=True)
    ngo_category = models.CharField(max_length=500, null=True, blank=True)
    ngo_location = models.CharField(max_length=500, null=True, blank=True)
    ngo_description = models.CharField(max_length=500, null=True, blank=True)
    ngo_contact_number = models.CharField(max_length=300, null=True, blank=True)
    ngo_id = models.CharField(max_length=300, null=True, blank=True)
    key = models.CharField(max_length=300, null=True, blank=True)
    ngo_url = models.CharField(max_length=300, null=True, blank=True)
    ngo_link_text = models.CharField(max_length=300, null=True, blank=True)
    payment_link_text = models.CharField(max_length=300, null=True, blank=True)


class donation_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    donation_image = models.ImageField(upload_to='DonationHeaderImage', null=True, blank=True)
    donation_description = models.CharField(max_length=500,null=True, blank=True)
    donation_footer = models.CharField(max_length=500,null=True, blank=True)
    donation_now_button_name = models.CharField(max_length=500,null=True, blank=True)
    my_donation_button_name = models.CharField(max_length=500,null=True, blank=True)
    contact_us_button_name = models.CharField(max_length=500,null=True, blank=True)
    donation_list_header = models.CharField(max_length=500,null=True, blank=True)
    donation_list_body = models.CharField(max_length=500,null=True, blank=True)
    donation_list_footer = models.CharField(max_length=500,null=True, blank=True)
    donation_list_button_name = models.CharField(max_length=500,null=True, blank=True)
    donation_conform_message = models.CharField(max_length=500,null=True, blank=True)
    donation_failure_message = models.CharField(max_length=500,null=True, blank=True)
    donation_contact_us_message = models.CharField(max_length=500,null=True, blank=True)
    donation_contact_us_image = models.ImageField(upload_to='ContactUsImage', null=True, blank=True)
    my_donation_details_button_name1 = models.CharField(max_length=500, null=True, blank=True)
    my_donation_details_button_name2 = models.CharField(max_length=500, null=True, blank=True)
    my_donation_details_button_name3 = models.CharField(max_length=500, null=True, blank=True)
    contact_us_details_button_name = models.CharField(max_length=500, null=True, blank=True)
    support_number = models.BigIntegerField(null=True)
    ngo_logo = models.ImageField(upload_to='DonationLogoImage', null=True, blank=True)
    ngo_name = models.CharField(max_length=500,null=True, blank=True)
    ngo_pan = models.CharField(max_length=500,null=True, blank=True)
    ngo_gstin = models.CharField(max_length=500,null=True, blank=True)
    ngo_header_notes = models.CharField(max_length=500,null=True, blank=True)
    ngo_footer_notes = models.CharField(max_length=500,null=True, blank=True)
    ngo_signature_header = models.CharField(max_length=500,null=True, blank=True)
    ngo_signature_image = models.ImageField(upload_to='SignatureImage', null=True, blank=True)
    ngo_signature_footer = models.CharField(max_length=500,null=True, blank=True)
    ngo_url = models.CharField(max_length=300, null=True, blank=True)
    ngo_link_text = models.CharField(max_length=300, null=True, blank=True)
    invoice_footer = models.CharField(max_length=500,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class donation_types(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    donation_name = models.CharField(max_length=500,null=True, blank=True)
    donation_short_description = models.CharField(max_length=500,null=True, blank=True)
    donation_description = models.CharField(max_length=500,null=True, blank=True)
    donation_type_image = models.ImageField(upload_to='DonationTypeImage', null=True, blank=True)
    donation_amount = models.FloatField(null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class donation_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    donar_name = models.CharField(max_length=500,null=True, blank=True)
    donar_email = models.EmailField(max_length=200,null=True, blank=True)
    donar_pan_number = models.CharField(max_length=500,null=True, blank=True)
    donation_amount = models.FloatField(null=True,blank=True)
    donar_phone_number = models.CharField(max_length=300, null=True, blank=True)
    receipient_pdf = models.FileField(upload_to='PDFFiles', null=True, blank=True)
    donation_date = models.DateField(null=True, blank=True)
    donation_name = models.CharField(max_length=500, null=True, blank=True)
    donation_short_description = models.CharField(max_length=500, null=True, blank=True)
    donation_description = models.CharField(max_length=500, null=True, blank=True)
    donation_type_image = models.ImageField(upload_to='DonationTypeImage', null=True, blank=True)
    donation_reference_id = models.CharField(max_length=200, null=True, blank=True)
    payment_status = models.IntegerField(null=True, blank=True)
    donation_comments_message = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class donation_payment_settings(models.Model):
    contact_name=models.CharField(max_length=200,null=True, blank=True)
    contact_number=models.CharField(max_length=200,null=True, blank=True)
    payment_gateway = models.CharField(max_length=200,null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class donation_payment_gateway_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    payment_gateway = models.CharField(max_length=200, null=True, blank=True)
    gateway_id = models.CharField(max_length=200,null=True, blank=True)
    gateway_key = models.CharField(max_length=200,null=True, blank=True)
    currency = models.CharField(max_length=200, choices=CURRENCY_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class donation_ngo_type(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    donation_ngo_type = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class donation_ngo_category(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(donation_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    donation_ngo_category = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
