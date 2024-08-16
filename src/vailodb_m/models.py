from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

MALL_SERVICES = (
    ('Shopping', 'SHOPPING'),
    ('Movies', 'MOVIES'),
    ('Parking', 'PARKING'),
    ('Restaurant', 'RESTAURANT'),
    ('Funzone', 'FUNZONE'),
    ('Events', 'EVENTS'),
    ('Information', 'INFORMATION'),
    ('Feedback', 'FEEDBACK'),
    ('Offers', 'OFFERS')
)

SERVICE_SEETINGS_CONTROL = (
    ('Enable', 'ENABLE'),
    ('Disable', 'DISABLE')
)

SHOP_AVAILABILTY_CHOICES = (
    ('Yes', 'YES'),
    ('No', 'NO')
)
RESTAURANT_AVAILABILTY_CHOICES=(
    ('Yes', 'YES'),
    ('No', 'NO')
)

PRODUCT_AVAILABILTY_CHOICES=(
    ('Yes', 'YES'),
    ('No', 'NO')
)

CURRENCY_CHOICES = (
    ('EUR', 'Euros'),
    ('GBP', 'British Pound'),
    ('INR', 'Indian Rupees'),
    ('USD', 'US Dollar'),

)

class Malls_marketplace_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_flow_id = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    my_mall_flow_id = models.CharField(max_length=500, null=True, blank=True)
    # marketplace_welcome_image = models.ImageField(upload_to='FlowImage', null=True, blank=True)
    # marketplace_welcome_message_body = models.CharField(max_length=500, null=True, blank=True)
    # marketplace_welcome_message_footer = models.CharField(max_length=500, null=True, blank=True)
    template_id = models.CharField(max_length=500, null=True, blank=True)
    template_name = models.CharField(max_length=500, null=True, blank=True)
    template_status = models.CharField(max_length=500, null=True, blank=True)
    generic_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    mymall_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Mall_Marketplace(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    mall_name = models.CharField(max_length=500, null=True, blank=True)
    mall_type = models.CharField(max_length=500, null=True, blank=True)
    mall_category = models.CharField(max_length=500, null=True, blank=True)
    mall_location = models.CharField(max_length=500, null=True, blank=True)
    mall_description = models.CharField(max_length=500, null=True, blank=True)
    mall_url = models.CharField(max_length=500, null=True, blank=True)
    mall_link_text = models.CharField(max_length=500, null=True, blank=True)
    mall_id = models.CharField(max_length=500, null=True, blank=True)
    mall_key = models.CharField(max_length=500, null=True, blank=True)
    mall_contact_number = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Mall_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    mall_name = models.CharField(max_length=100)
    mall_address = models.CharField(max_length=500)
    mall_image = models.ImageField(upload_to='Image', null=True, blank=True)
    mall_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    mall_url = models.CharField(max_length=500, null=True, blank=True)
    mall_link_text = models.CharField(max_length=500, null=True, blank=True)
    contact_us = models.BigIntegerField(null=True, blank=True)
    contact_one = models.BigIntegerField(null=True, blank=True)
    contact_two = models.BigIntegerField(null=True, blank=True)
    contact_three = models.BigIntegerField(null=True, blank=True)
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    # checkIn = models.TimeField(null=True, blank=True)
    # checkout = models.TimeField(null=True, blank=True)
    # Reception_number = models.BigIntegerField(null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Mall_services_setting(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    key = models.CharField(max_length=100, choices=MALL_SERVICES, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    support_number = models.BigIntegerField(null=True, blank=True)
    control = models.CharField(max_length=100, choices=SERVICE_SEETINGS_CONTROL, null=True, blank=True)
    escalation_number = models.CharField(max_length=100, null=True, blank=True)
    escalation_hours = models.TimeField(null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Shop_Category(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Shop_category = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    shop_parent_id = models.CharField(max_length=300, null=True, blank=True)
    shop_reference_id = models.CharField(max_length=300, null=True, blank=True)
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Shop(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    shop_name = models.CharField(max_length=100, null=True, blank=True)
    shop_description = models.CharField(max_length=500, null=True, blank=True)
    shop_availability = models.CharField(max_length=100, choices=SHOP_AVAILABILTY_CHOICES, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    shop_category = models.ForeignKey(Shop_Category, on_delete=models.CASCADE, null=True, blank=True)
    shop_image = models.ImageField(upload_to='Image', null=True, blank=True)
    shop_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    shop_url = models.CharField(max_length=500, null=True, blank=True)
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    shoptype_parent_id = models.CharField(max_length=300, null=True, blank=True)
    shoptype_reference_id = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Movies(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    show_timing = models.CharField(max_length=500, null=True, blank=True)
    poster = models.ImageField(upload_to='Image', null=True, blank=True)
    trailer = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Restaurant_category(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    restaurant_parent_id = models.CharField(max_length=300, null=True, blank=True)
    restaurant_reference_id = models.CharField(max_length=300, null=True, blank=True)
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Restaurant(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    availability = models.CharField(max_length=100, choices=RESTAURANT_AVAILABILTY_CHOICES, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    restaurant_category = models.ForeignKey(Restaurant_category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='Image', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    url = models.CharField(max_length=500, null=True, blank=True)
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    restauranttype_parent_id = models.CharField(max_length=300, null=True, blank=True)
    restauranttype_reference_id = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Offers(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    offer_description = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='Image', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    offer_code = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Events(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='Image', null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class FunZone(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    activity_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Mall_information(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    information_name = models.CharField(max_length=100, null=True, blank=True)
    information_discription = models.CharField(max_length=500, null=True, blank=True)
    information_image = models.ImageField(upload_to='Image')
    information_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    body_text = models.CharField(max_length=1024, null=True, blank=True)
    header_text = models.CharField(max_length=300, null=True, blank=True)
    button_name = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Visitor_info(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Whatsapp_number = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Feedback_questions(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Question = models.CharField(max_length=200, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Feedback_response_header(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    visitor_info = models.ForeignKey(Visitor_info, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Feedback_responses(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    feedback_response_header = models.ForeignKey(Feedback_response_header, on_delete=models.CASCADE, null=True,
                                                 blank=True)
    feedback_question = models.ForeignKey(Feedback_questions, on_delete=models.CASCADE, null=True, blank=True)
    feedback_response = models.IntegerField(null=True, blank=True)

    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Key_products(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='Image')
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    availability = models.CharField(max_length=100,choices=PRODUCT_AVAILABILTY_CHOICES, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES, null=True, blank=True)  # INR/USD/...
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class test_model(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Mall_Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)
