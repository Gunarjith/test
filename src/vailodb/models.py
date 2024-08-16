from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

CLIENT_CHOICES = (
    ('none','NONE'),
    ('online', 'ONLINE'),
    ('offline','OFFLINE'),
    ('both','BOTH'),

)
CLIENT_CHOICES1 = (
    ('commerce','COMMERCE'),
    ('ticket', 'TICKET'),
    ('scanner','SCANNER'),
    ('donation','DONATION'),
    ('appointement','APPOINTEMENT'),
    ('survey','SURVEY'),
    ('hotel','HOTEL'),
    ('campaign','CAMPAIGN'),
    ('malls','MALLS'),
    ('banking','BANKING')

)


CHOOSE_CHOICES=(
    ('none','NONE'),
    ('image','IMAGE'),
    ('text','TEXT'),
)

CHOOSE_LEVEL_SETTINGS=(
    ('none','NONE'),
    ('skiplevel1','SKIPLEVEL1'),
    ('skiplevel1and2','SKIPLEVEL1AND2'),
)

CURRENCY_CHOICES = (
    ('INR', 'Rupees'),
    ('USD', 'DOLLAR'),
    ('GBP', 'Pounds'),
    ('EUR', 'Euros'),

)
TICKET_CHOICES=(
    ('yes', 'YES'),
    ('no', 'NO'),
)

SUBCLIENT_CHOICE=(
    ('donation','Donation'),
    ('ticket','TICKET'),
    ('scanner','SCANNER'),
    ('campaign','CAMPAIGN'),
    ('hotel','HOTEL'),
    ('malls','MALLS'),
)


MARKET_CHOICES=(
    ('yes', 'YES'),
    ('no', 'NO'),
)






class vailo_leads(models.Model):
    first_name=models.CharField(max_length=199)
    last_name=models.CharField(max_length=199)
    company_name=models.CharField(max_length=199)
    business_email=models.CharField(max_length=199)
    business_number=models.CharField(max_length=199)
    job_title=models.CharField(max_length=199)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class admin_permission(models.Model):
    client_auth_key=models.CharField(max_length=250)
    client_auth_secret=models.CharField(max_length=250)
    client_billing_status=models.BooleanField(default=False)
    client_permission_status = models.BooleanField(default=False)
    client_service_type = models.CharField(max_length=200, choices=CLIENT_CHOICES1, default='none')
    client_marketplace = models.CharField(max_length=200, choices=MARKET_CHOICES, default='none')
    client_type = models.CharField(max_length=200, choices=CLIENT_CHOICES, default='none')
    login_allowed = models.BooleanField(default=False)
    billing_campaign_sent_rate = models.FloatField(null=True, blank=True)
    billing_message_sent_rate = models.FloatField(null=True, blank=True)
    billing_message_received_rate = models.FloatField(null=True, blank=True)
    billing_new_client_rate = models.FloatField(null=True, blank=True)
    billing_new_customer_lead_rate = models.FloatField(null=True, blank=True)
    billing_monthly_charge = models.FloatField(null=True, blank=True)
    billing_currency = models.CharField(
        max_length=200, choices=CURRENCY_CHOICES, default='none')
    billing_amount1 = models.FloatField(null=True, blank=True)
    billing_amount2 = models.FloatField(null=True, blank=True)
    billing_amount3 = models.FloatField(null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    client_image = models.ImageField(upload_to='clientImages', null=True, blank=True)
    client_color1 = models.CharField(default=False, null=True, max_length=200, blank=True)
    client_color2 = models.CharField(default=False, null=True, max_length=200, blank=True)
    client_color3 = models.CharField(default=False, null=True, max_length=200, blank=True)
    client_color4 = models.CharField(default=False, null=True, max_length=200, blank=True)
    client_color5 = models.CharField(default=False, null=True, max_length=200, blank=True)
    client_color6 = models.CharField(default=False, null=True, max_length=200, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Subclient(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    subclientname = models.CharField(max_length=200, null=True, blank=True)
    emailid = models.EmailField(max_length=200, null=True, blank=True, unique=True)
    password = models.CharField(max_length=200, null=True)
    re_password = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('client', 'emailid'),)


class SubUserPreference(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    subclient = models.ForeignKey(Subclient, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=300, choices=SUBCLIENT_CHOICE, null=True, blank=True)
    marketplace_id = models.CharField(max_length=200, null=True, blank=True)
    Menu_access = models.CharField(max_length=200, null=True, blank=True)
    sub_Menu_access = models.CharField(max_length=200, null=True, blank=True)
    

    class Meta:
        unique_together = (('client', 'subclient'),)


class facebook_details(models.Model):
    fb_phone_number_id=models.BigIntegerField()
    fb_whatsapp_number = models.BigIntegerField()
    fb_Whatsapp_business_account_id = models.BigIntegerField(null=True,blank=True)
    fb_access_token=models.CharField(max_length=255)
    fb_app_id = models.BigIntegerField(null=True,blank=True)
    private_dynamic_file_name = models.CharField(max_length=200,null=True,blank=True)
    public_dynamic_file_name = models.CharField(max_length=200,null=True,blank=True)
    private_key = models.CharField(max_length=2000,null=True,blank=True)
    public_key = models.CharField(max_length=2000,null=True,blank=True)
    fb_catalogId = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True,auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True,blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)


class payment_settings(models.Model):
    contact_name=models.CharField(max_length=200)
    contact_number=models.CharField(max_length=200)
    payment_gateway = models.CharField(max_length=200,null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class payment_gateway_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_gateway = models.CharField(max_length=200, null=True, blank=True)
    gateway_id = models.CharField(max_length=200,null=True, blank=True)
    gateway_key = models.CharField(max_length=200,null=True, blank=True)
    currency = models.CharField(max_length=200, choices=CURRENCY_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class event_master(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Event_Name = models.CharField(max_length=200)
    Event_Description = models.CharField(max_length=500)
    Start_Date = models.DateField( null=True, blank=True)
    End_Date = models.DateField( null=True, blank=True)
    Event_Logo = models.ImageField(upload_to='EventLogo', null=True, blank=True)
    Event_ticket_image = models.ImageField(upload_to='EventTicketImg', null=True, blank=True)
    Event_Venue = models.CharField(max_length=500,null=True, blank=True)
    Event_Terms_Conditions = models.CharField(max_length=1500,null=True, blank=True)
    Event_About = models.CharField(max_length=1500,null=True, blank=True)
    Event_Message_Header_Image = models.ImageField(upload_to='EventMessageHeaderImage', null=True, blank=True)
    Event_Message_Header_Text = models.CharField(max_length=400,null=True, blank=True)
    Event_Message_Body_Text = models.CharField(max_length=400,null=True, blank=True)
    Event_Message_Footer_Text = models.CharField(max_length=400,null=True, blank=True)
    Event_slots_button_name = models.CharField(max_length=400,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class event_slots(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    event_master = models.ForeignKey(event_master, on_delete=models.CASCADE, null=True, blank=True)
    Slot_Name = models.CharField(max_length=200)
    Slot_Description = models.CharField(max_length=500)
    Slot_message_Header_Image = models.ImageField(upload_to='SlotMessageHeaderImage', null=True, blank=True)
    Slot_Message_Header_Text = models.CharField(max_length=400,null=True, blank=True)
    Slot_Message_Body_Text = models.CharField(max_length=400,null=True, blank=True)
    Slot_Message_Footer_Text = models.CharField(max_length=400,null=True, blank=True)
    slot_category_button_name = models.CharField(max_length=400,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class event_ticket_category(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    event_master = models.ForeignKey(event_master, on_delete=models.CASCADE, null=True, blank=True)
    event_slots = models.ForeignKey(event_slots, on_delete=models.CASCADE, null=True, blank=True)
    Category_Name = models.CharField(max_length=200)
    Category_Description = models.CharField(max_length=500)
    Category_Price = models.FloatField(null=True, blank=True)
    category_ticket_image = models.ImageField(upload_to='CategoryTicketImage', null=True, blank=True)
    Category_Message_Header_Image = models.ImageField(upload_to='CategoryMessageHeaderImage', null=True, blank=True)
    Category_Message_Header_Text = models.CharField(max_length=400,null=True, blank=True)
    Category_Message_Body_Text = models.CharField(max_length=400,null=True, blank=True)
    Category_Message_Footer_Text = models.CharField(max_length=400,null=True, blank=True)
    Number_Of_Ticket_Button_Name = models.CharField(max_length=400,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class event_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    event_master = models.ForeignKey(event_master, on_delete=models.CASCADE, null=True, blank=True)
    event_slots = models.ForeignKey(event_slots, on_delete=models.CASCADE, null=True, blank=True)
    event_ticket_category = models.ForeignKey(event_ticket_category, on_delete=models.CASCADE, null=True, blank=True)
    welcome_header_image = models.ImageField(upload_to='WelcomeHeaderImage', null=True, blank=True)
    welcome_header_text = models.CharField(max_length=300,null=True, blank=True)
    welcome_message_text = models.CharField(max_length=300,null=True, blank=True)
    welcome_message_footer = models.CharField(max_length=300,null=True, blank=True)
    booking_header_image = models.ImageField(upload_to='BookingHeaderImage', null=True, blank=True)
    booking_header_text = models.CharField(max_length=300,null=True, blank=True)
    booking_message_text = models.CharField(max_length=300,null=True, blank=True)
    booking_message_footer = models.CharField(max_length=300,null=True, blank=True)
    booking_button_name = models.CharField(max_length=300,null=True, blank=True)
    booking_myticket_button_name = models.CharField(max_length=300,null=True, blank=True)
    booking_cancel_ticket_button_name = models.CharField(max_length=300,null=True, blank=True)
    event_list_event_button_name = models.CharField(max_length=300,null=True, blank=True)
    cancel_ticket_header_image = models.ImageField(upload_to='CancelTicketHeaderImage', null=True, blank=True)
    cancel_ticket_message_body = models.CharField(max_length=300,null=True, blank=True)
    ticket_conformation_header_image = models.ImageField(upload_to='TicketConformationHeaderImage', null=True, blank=True)
    ticket_conformation_message_body = models.CharField(max_length=300,null=True, blank=True)
    ticket_payment_failure_image = models.ImageField(upload_to='PaymentFailureImage', null=True, blank=True)
    ticket_failure_message_body = models.CharField(max_length=300,null=True, blank=True)
    contact_header_image = models.ImageField(upload_to='UseHeaderImage', null=True, blank=True)
    contact_message_text = models.CharField(max_length=300,null=True, blank=True)
    contact_button_name = models.CharField(max_length=300,null=True, blank=True)
    transfer_button_name = models.CharField(max_length=300,null=True, blank=True)
    tickets_not_availble_header_image = models.ImageField(upload_to='NotAvailableHeaderImage', null=True, blank=True)
    tickets_not_available_message_body = models.CharField(max_length=300,null=True, blank=True)
    second_number = models.BigIntegerField(null=True)
    ticketcount1_desc = models.CharField(max_length=300,null=True, blank=True)
    ticketcount2_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount3_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount4_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount5_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount6_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount7_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount8_desc = models.CharField(max_length=300, null=True, blank=True)
    ticketcount9_desc = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
    level_settings = models.CharField(max_length=300, choices=CHOOSE_LEVEL_SETTINGS, null=True, blank=True)
    transfer_ticket = models.CharField(max_length=200, choices=TICKET_CHOICES, default='none')



class event_ticket_cart_header(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_phone_number = models.CharField(max_length=200)
    cart_amount = models.FloatField(null=True,blank=True)
    total_tickets = models.IntegerField(null=True,blank=True)
    payment_reference_id = models.CharField(max_length=200)
    payment_status = models.IntegerField(null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class event_ticket_cart_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(event_ticket_cart_header,on_delete=models.CASCADE, null=True, blank=True)
    event_id = models.IntegerField(null=True,blank=True)
    slot_id = models.IntegerField(null=True,blank=True)
    category_id = models.IntegerField(null=True,blank=True)
    number_of_tickets = models.IntegerField(null=True,blank=True)
    ticket_price = models.FloatField(null=True,blank=True)
    ticket_sub_total = models.FloatField(null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class ticket_information(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=200)
    expiry_date = models.DateField( null=True, blank=True)
    event_master = models.ForeignKey(event_master, on_delete=models.CASCADE, null=True, blank=True)
    event_slots = models.ForeignKey(event_slots, on_delete=models.CASCADE, null=True, blank=True)
    event_ticket_category = models.ForeignKey(event_ticket_category, on_delete=models.CASCADE, null=True, blank=True)
    ticket_QR = models.ImageField(upload_to='TicketQRCode', null=True, blank=True)
    ticket_status = models.IntegerField(null=True,blank=True)
    customer_name = models.CharField(max_length=200)
    customer_phone_number = models.CharField(max_length=199)
    customer_address = models.CharField(max_length=250, default='')
    customer_email = models.CharField(max_length=200)
    last_updated_date_time = models.DateTimeField(default=datetime.now)
    payment_reference_id = models.CharField(max_length=200,null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class ticket_customer_master(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    event_master = models.ForeignKey(event_master, on_delete=models.CASCADE, null=True, blank=True)
    event_slots = models.ForeignKey(event_slots, on_delete=models.CASCADE, null=True, blank=True)
    event_ticket_category = models.ForeignKey(event_ticket_category, on_delete=models.CASCADE, null=True, blank=True)
    Customer_First_Name = models.CharField(max_length=300, null=True, blank=True)
    Customer_Middle_Name = models.CharField(max_length=300, null=True, blank=True)
    Customer_Last_Name = models.CharField(max_length=300, null=True, blank=True)
    Customer_Email = models.EmailField(max_length=200,null=True, blank=True,unique=True)
    Customer_Address_Line1 = models.CharField(max_length=300, null=True, blank=True)
    Customer_Address_Line2 = models.CharField(max_length=300, null=True, blank=True)
    Customer_Address_Landmark = models.CharField(max_length=300, null=True, blank=True)
    Customer_Address_Pincode = models.CharField(max_length=300,null=True,blank=True)
    Customer_City = models.CharField(max_length=300, null=True, blank=True)
    Customer_State = models.CharField(max_length=300, null=True, blank=True)
    Customer_Country = models.CharField(max_length=300, null=True, blank=True)
    Customer_Phone_Number = models.CharField(max_length=300, null=True, blank=True)
    Customer_Whatsapp_Number = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
    Customer_Status = models.IntegerField(null=True, blank=True)

class campaign_info(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Campaign_Name = models.CharField(max_length=300,null=True, blank=True)
    Campaign_Description = models.CharField(max_length=300,null=True, blank=True)
    Campaign_Header_Image = models.ImageField(upload_to='CampaignHeaderImage', null=True, blank=True)
    Campaign_Message_Text = models.CharField(max_length=300,null=True, blank=True)
    Campaign_Footer_Text = models.CharField(max_length=300,null=True, blank=True)
    Campaign_First_Button_Name = models.CharField(max_length=300,null=True, blank=True)
    Campaign_Second_Button_Name = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Third_Button_Name = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Status = models.IntegerField(null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class campaign_customer(models.Model):
    campaign_info = models.ForeignKey(campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    ticket_customer_master = models.ForeignKey(ticket_customer_master, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Customer_First_Name = models.CharField(max_length=300, null=True, blank=True)
    Customer_Whatsapp_Number = models.CharField(max_length=300, null=True, blank=True)
    Customer_City = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.client} - {self.Customer_First_Name} - {self.Customer_Whatsapp_Number} - {self.Customer_City}"

    class Meta:
        unique_together = ('ticket_customer_master', 'client', 'campaign_info')

class History_campaign_customer(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_info = models.ForeignKey(campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    campaign_customer = models.ForeignKey(campaign_customer, on_delete=models.CASCADE, null=True, blank=True)
    campaign_name = models.CharField(max_length=300, null=True, blank=True)
    Customer_First_Name = models.CharField(max_length=300, null=True, blank=True)
    Customer_Whatsapp_Number = models.CharField(max_length=300, null=True, blank=True)
    Customer_City = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class History_campaign_infor(models.Model):
     client = models.ForeignKey(User, on_delete=models.CASCADE)
     campaign_info = models.ForeignKey(campaign_info, on_delete=models.CASCADE, null=True, blank=True)
     Campaign_Name = models.CharField(max_length=300,null=True, blank=True)
     Campaign_Description = models.CharField(max_length=300,null=True, blank=True)
     Campaign_Header_Image = models.ImageField(upload_to='CampaignHeaderImage', null=True, blank=True)
     Campaign_Message_Text = models.CharField(max_length=300,null=True, blank=True)
     Campaign_Footer_Text = models.CharField(max_length=300,null=True, blank=True)
     Campaign_First_Button_Name = models.CharField(max_length=300,null=True, blank=True)
     Campaign_Second_Button_Name = models.CharField(max_length=300, null=True, blank=True)
     Campaign_Third_Button_Name = models.CharField(max_length=300, null=True, blank=True)
     Campaign_Status = models.IntegerField(null=True,blank=True)
     vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
     vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
     vailo_record_status = models.IntegerField(null=True, blank=True)


class ticket_billing(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=300,null=True, blank=True)
    billed_amount = models.IntegerField(null=True,blank=True)
    paid_amount = models.IntegerField(null=True,blank=True)
    status = models.IntegerField(null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class ticket_billing_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_billing = models.ForeignKey(ticket_billing, on_delete=models.CASCADE, null=True, blank=True)
    transaction_type = models.CharField(max_length=300,null=True, blank=True)
    transaction_name = models.CharField(max_length=300,null=True, blank=True)
    transaction_count = models.IntegerField(null=True,blank=True)
    transaction_amount = models.IntegerField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)














