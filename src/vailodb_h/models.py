from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CURRENCY_CHOICES = (
    ('EUR', 'Euros'),
    ('GBP', 'British Pound'),
    ('INR', 'Indian Rupees'),
    ('USD', 'US Dollar'),

)

FOODTYPE_CHOICES = (
    ('NONVEG', 'nonveg'),
    ('VEG', 'veg'),

)

KM_CHOICE = (
    ('KM', 'kilometers'),
    ('MILES', 'miles')
)

PLACE_TYPE_CHOICE = (
    ('AIRPORT', 'airport'),
    ('HISTORICAL', 'historical'),
    ('HOSPITAL', 'hospital'),
    ('METRO', 'metro'),
    ('MUSEUM','museum'),
    ('RAILWAY STATION', 'railway station'),
    ('TEMPLE', 'temple'),
    ('WATER FALLS', 'Water falls'),
    ('ZOO','zoo'),
)

ROOMCATGEORY_CHOICES = (
    ('AC', 'ac'),
    ('NONAC', 'nonac')
)



ROOM_AVAILABILTY_CHOICES=(
    ('YES','Yes'),
    ('NO','No')
)


HOTEL_SERVICES =(
    ('SERVICES','hotel services'),
    ('FOOD','food'),
    ('NEARBY', 'nearby place'),
    ('ROOM','room'),
    ('FACILITIES','hotel facilities'),
    ('SELP HELP', 'self help'),
    ('INFORMATION','Information'),
    ('COMPLAINTS','Complaints'),
)


Food_order_status_choices=(
    ('ORDERED', 'Ordered'),
    ('ACCEPTED', 'Accepted'),
    ('DELIVERED', 'Delivered')
)

Service_order_status_choices=(
    ('REQUESTED', 'Requested'),
    ('ACKNOWLEDGED','Acknowledged'),
    ('COMPLETED', 'Completed')
)


Complaint_status=(
    ('REQUESTED', 'Requested'),
    ('ACKNOWLEDGED','Acknowledged'),
    ('COMPLETED', 'Completed')
)

FOOD_AVAILABILTY_CHOICES=(
     ('YES','Yes'),
    ('NO','No')
)

MESSAGE_TYPE_CHOICES=(
    ('IMAGE','image'),
    ('TEXT','text'),
    ('VIDEO','Video')

)

MESSAGE_STATUS_CHOICES=(
    ('DRAFT', 'Draft'),
    ('SUBMITTED', 'Submitted'),
    ('REJECTED','Rejected'),
    ('APPROVED', 'Approved'),
    
)

class Hotel_marketplace_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_flow_id = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    multiple_hotel_checkin_specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    my_hotel_flow_id = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_image = models.ImageField(upload_to='FlowImage', null=True, blank=True)
    marketplace_welcome_message_body = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_message_footer = models.CharField(max_length=500, null=True, blank=True)
    generic_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    myhotel_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    conversation_activation_message_template_id=models.CharField(max_length=500, null=True, blank=True)
    conversation_activation_message_template_name = models.CharField(max_length=500, null=True, blank=True)
    conversation_activation_message_template_status = models.CharField(max_length=500, null=True, blank=True)
    checkin_flow_id=models.CharField(max_length=100, null=True, blank=True)
    checkout_flow_id=models.CharField(max_length=100, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Hotel_marketplace(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=500, null=True, blank=True)
    hotel_type = models.CharField(max_length=500, null=True, blank=True)
    hotel_category = models.CharField(max_length=500, null=True, blank=True)
    hotel_location = models.CharField(max_length=500, null=True, blank=True)
    hotel_description = models.CharField(max_length=500, null=True, blank=True)
    hotel_url = models.CharField(max_length=500, null=True, blank=True)
    hotel_link_text = models.CharField(max_length=500, null=True, blank=True)
    hotel_id = models.CharField(max_length=500, null=True, blank=True)
    hotel_key = models.CharField(max_length=500, null=True, blank=True)
    hotel_contact_number = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)




class Hotel_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=500)
    hotel_image = models.ImageField(upload_to='Image', null=True, blank=True)
    hotel_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    hotel_url = models.CharField(max_length=500, null=True, blank=True)
    hotel_link_text = models.CharField(max_length=500, null=True, blank=True)
    contact_us = models.BigIntegerField(null=True, blank=True)
    contact_one = models.BigIntegerField(null=True, blank=True)
    contact_two = models.BigIntegerField(null=True, blank=True)
    contact_three = models.BigIntegerField(null=True, blank=True)
    checkIn = models.TimeField(null=True, blank=True)
    checkout = models.TimeField(null=True, blank=True)
    Reception_number = models.BigIntegerField(null=True, blank=True)
    checkin_toolkit=models.FileField(upload_to='hotel_checkin_toolkit', null=True, blank=True)
    checkin_confirmation_message=models.CharField(max_length=1024,null=True, blank=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    last_message_datetime=models.DateTimeField(null=True, blank=True)
    qr_hotel_name=models.CharField(max_length=100, null=True, blank=True)
    hotel_logo = models.ImageField(upload_to='Image', null=True, blank=True)
    country_code=models.CharField(max_length=20, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Hotel_services(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    service_name = models.CharField(max_length=100, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    service_discription = models.CharField(max_length=500, null=True, blank=True)
    service_image = models.ImageField(upload_to='Image')
    service_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    service_price = models.CharField(max_length=100, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Food_Category(models. Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    category_name = models.CharField(max_length=200, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Food(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    food_name = models.CharField(max_length=100, null=True, blank=True)
    food_price = models.IntegerField(null=True, blank=True)
    food_type = models.CharField(max_length=100, choices=FOODTYPE_CHOICES, null=True, blank=True)
    food_discription = models.CharField(max_length=500, null=True, blank=True)
    Food_availability = models.CharField(max_length=100, choices=FOOD_AVAILABILTY_CHOICES, null=True, blank=True)
    food_category = models.ForeignKey(Food_Category, on_delete=models.CASCADE, null=True, blank=True)
    food_cuisine = models.CharField(max_length=100, null=True, blank=True)
    food_image = models.ImageField(upload_to='Image', null=True, blank=True)
    food_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    custom_number_0 = models.CharField(max_length=100, null=True, blank=True)
    custom_number_1 = models.CharField(max_length=100, null=True, blank=True)
    custom_number_2 = models.CharField(max_length=100, null=True, blank=True)
    custom_number_3 = models.CharField(max_length=100, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Food_catalogue(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    catalogue_name = models.CharField(max_length=100, null=True, blank=True) # to fetch a food_category
    catalogue_discription = models.CharField(max_length=100, null=True, blank=True)
    catalogue_image = models.ImageField(upload_to='image', null=True, blank=True)
    catalogue_set_id = models.CharField(max_length=50, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Food_catalogue_items(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Food_catalogue = models.ForeignKey(Food_catalogue, on_delete=models.CASCADE, null=True, blank=True)
    Food_Item = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Nearby_place(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    place_type = models.CharField(max_length=100, choices=PLACE_TYPE_CHOICE, null=True, blank=True)
    place_name = models.CharField(max_length=100, null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
    distance_unit = models.CharField(max_length=200,choices = KM_CHOICE, null = True, blank = True)
    Discription = models.CharField(max_length=500, null=True, blank=True)
    place_image = models.ImageField(upload_to='Image', null=True, blank=True)
    place_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    address=models.CharField(max_length=800, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Hotel_rooms(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    room_number = models.CharField(max_length=100)
    room_floor = models.CharField(max_length=100)
    room_type = models.CharField(max_length=100, choices=ROOMCATGEORY_CHOICES, null=True, blank=True)
    bed = models.CharField(max_length=100, null=True, blank=True)
    room_price = models.IntegerField(null=True, blank=True)
    room_price_unit = models.CharField(max_length=100, choices=CURRENCY_CHOICES, null=True, blank=True)  # INR/USD/...
    room_info = models.CharField(max_length=500, null=True, blank=True)
    l_room_type = models.CharField(max_length=100, null=True, blank=True)  # luxury type
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Hotel_rooms_type(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    room_type = models.CharField(max_length=100, null=True, blank=True)  # luxury type
    room_category = models.CharField(max_length=100, choices=ROOMCATGEORY_CHOICES, null=True, blank=True)
    bed = models.CharField(max_length=100, null=True, blank=True)
    room_price = models.IntegerField(null=True, blank=True)
    Hotel_room_image = models.ImageField(upload_to='RoomImage', null=True, blank=True)
    room_price_unit = models.CharField(max_length=100, choices=CURRENCY_CHOICES, null=True, blank=True)  # INR/USD/...
    room_info = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Room_list(models. Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    hotel_room_type = models.ForeignKey(Hotel_rooms_type, on_delete=models.CASCADE, null=True, blank=True)
    room_number = models.CharField(max_length=100)
    room_floor = models.CharField(max_length=100)
    Hotel_room_image = models.ImageField(upload_to='RoomImage', null=True, blank=True)
    room_availability = models.CharField(max_length=100, choices=ROOM_AVAILABILTY_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)




class Hotel_facilities(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    facility_name = models.CharField(max_length=100, null=True, blank=True)
    facility_location = models.CharField(max_length=100, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    discription = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='Image')
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Selfhelp(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    selfhelp_name = models.CharField(max_length=100, null=True, blank=True)
    selfhelp_discription = models.CharField(max_length=500, null=True, blank=True)
    selfhelp_image = models.ImageField(upload_to='Image')
    selfhelp_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Information(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    information_name = models.CharField(max_length=100, null=True, blank=True)
    information_discription = models.CharField(max_length=500, null=True, blank=True)
    information_image = models.ImageField(upload_to='Image')
    information_video = models.FileField(upload_to='videos_uploaded', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Hotel_services_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    key = models.CharField(max_length=100, choices=HOTEL_SERVICES, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    support_number = models.BigIntegerField(null=True, blank=True)
    Advertisement_image = models.ImageField(upload_to='ADImage',null=True, blank=True)
    control = models.CharField(max_length=100, null=True, blank=True) # For Enable/Disable
    escalation_number = models.CharField(max_length=100, null=True, blank=True)
    escalation_hours = models.DurationField(null=True, blank=True)
    last_message_datetime=models.DateTimeField(null=True, blank=True)
    last_escalation_datetime=models.DateTimeField(null=True, blank=True)
    last_activation_message_datetime=models.DateTimeField(null=True, blank=True)
    support_number_country_code=models.CharField(max_length=20, null=True, blank=True)
    escalation_number_country_code=models.CharField(max_length=20, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Service_order (models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    customer_phone_num = models.CharField(max_length=300, null=True, blank=True)
    customer_room = models.CharField(max_length=100, blank=True, null=True)
    hotel_service = models.ForeignKey(Hotel_services,on_delete=models.CASCADE, null=True, blank=True)
    service_comments = models.CharField(max_length=200, blank=True, null=True)
    service_status = models.CharField(max_length=100,choices=Service_order_status_choices, null=True, blank=True)#for order status Accepted/Commpleted
    last_escalation_message_datetime=models.DateTimeField(null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Food_order_header(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    customer_phone_num = models.CharField(max_length=300, null=True, blank=True)
    order_delivery_room = models.CharField(max_length=200, blank=True, null=True)
    order_amount = models.IntegerField(null=True, blank=True)
    order_comments = models.CharField(max_length=200, blank=True, null=True)
    order_status = models.CharField(max_length=100,choices=Food_order_status_choices, null=True, blank=True)#for order status delivered/accepted
    last_escalation_message_datetime=models.DateTimeField(null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Food_order_details(models.Model):
    client= models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace=models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Food_order_header = models.ForeignKey(Food_order_header, on_delete=models.CASCADE, null=True, blank=True)
    Food_Item = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    Food_quantity = models.IntegerField(null=True, blank=True)
    Food_Item_Price = models.IntegerField(null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Guest_info(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    Phone_number=models.CharField(max_length=100,null=True, blank=True)
    Guest_name=models.CharField(max_length=100,null=True, blank=True)
    GovernmentId=models.CharField(max_length=100,null=True, blank=True)
    Address=models.CharField(max_length=500,null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Hotel_Room_Guest_info(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    Room_details = models.ForeignKey(Room_list, on_delete=models.CASCADE, null=True, blank=True)
    marketplace=models.ForeignKey(Hotel_marketplace,on_delete=models.CASCADE,null=True, blank=True)
    Hotel_details=models.ForeignKey(Hotel_settings,on_delete=models.CASCADE,null=True,blank=True)
    Guest_details=models.ForeignKey(Guest_info, on_delete=models.CASCADE, null=True, blank=True)
    Check_In=models.DateTimeField(null=True, blank=True)
    Check_Out=models.DateTimeField(null=True, blank=True)
    actual_check_out=models.DateTimeField(null=True, blank=True)
    Comment=models.CharField(max_length=1000,null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Checkout_questions(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Question=models.CharField(max_length=200, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Checkout_response_header(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    Room_details=models.ForeignKey(Room_list,on_delete=models.CASCADE,null=True, blank=True)
    Hotel_details=models.ForeignKey(Hotel_settings,on_delete=models.CASCADE,null=True,blank=True)
    Guest_details=models.ForeignKey(Guest_info, on_delete=models.CASCADE, null=True, blank=True)
    Comment=models.CharField(max_length=400, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Checkout_responses(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    Checkout_response_header=models.ForeignKey(Checkout_response_header,on_delete=models.CASCADE,null=True,blank=True)
    Checkout_question=models.ForeignKey(Checkout_questions, on_delete=models.CASCADE,null=True,blank=True)
    Checkout_response=models.IntegerField(null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Complaint_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Complaint_category=models.CharField(max_length=400, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Complaint_info(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    Room_details=models.ForeignKey(Room_list,on_delete=models.CASCADE,null=True, blank=True)
    Hotel_details=models.ForeignKey(Hotel_settings,on_delete=models.CASCADE,null=True,blank=True)
    Guest_details=models.ForeignKey(Guest_info, on_delete=models.CASCADE, null=True, blank=True)
    Complaint_category = models.ForeignKey(Complaint_settings,on_delete=models.CASCADE, null=True, blank=True)
    Complaint_comments = models.CharField(max_length=400, blank=True, null=True)
    Complaint_status = models.CharField(max_length=100,choices=Complaint_status, null=True, blank=True)#for order status Accepted/Commpleted
    last_escalation_message_datetime=models.DateTimeField(null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Notification_message(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Hotel_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    message_name = models.CharField(max_length=300,null=True, blank=True)
    text_message = models.CharField(max_length=1024,null=True, blank=True)
    image_message = models.ImageField(upload_to='HotelNotificationImage', null=True, blank=True)
    video_message = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    message_type = models.CharField(max_length=100, choices=MESSAGE_TYPE_CHOICES, default='none')
    status = models.CharField(max_length=255, choices=MESSAGE_STATUS_CHOICES, default='none')
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Notification_log(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    Room_details=models.ForeignKey(Room_list,on_delete=models.CASCADE,null=True, blank=True)
    Hotel_details=models.ForeignKey(Hotel_settings,on_delete=models.CASCADE,null=True,blank=True)
    Guest_details=models.ForeignKey(Guest_info, on_delete=models.CASCADE, null=True, blank=True)
    notification_message=models.ForeignKey(Notification_message, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_status = models.IntegerField(null=True, blank=True)