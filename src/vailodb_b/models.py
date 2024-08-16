from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz
# Create your models here.
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
CURRENCY_CHOICES = (
    ('INR', 'Rupees'),
    ('USD', 'DOLLAR'),
    ('GBP', 'Pounds'),
    ('EUR', 'Euros'),

)

CHOOSE_CHOICES=(
    ('none','NONE'),
    ('image','IMAGE'),
    ('text','TEXT'),
    ('carousel','CAROUSEL')
)
# Create your models here.


CHOOSE_CAMPAIGN = (
    ('none','NONE'),
    ('yes','YES'),
    ('no','NO'),
)


FIELD_TYPE_CHOICES = (
        ("text", "Text"),
        ("password", "Password"),
        ("number", "Number"),
        ("email", "Email"),
        ("phone", "Phone"),
        ("radio", "radio"),
        ("checkbox", "Checkbox"),
        ("dropdown", "Dropdown"),
)

STATUS_TYPE_CHOICES =(
    ('DRAFT', 'Draft'),
    ('SUBMITTED', 'Submitted'),
    ('APPROVED', 'APPROVED'),
)


TEMPLATE_TYPE_CHOICES =(
    ('DRAFT', 'Draft'),
    ('SUBMITTED', 'Submitted'),
    ('APPROVED', 'APPROVED'),

)


FORM_HEADER_TYPE_CHOICES =(
    ('TEXT','Text'),
    ('IMAGE','Image'),

)

BUTTON_TYPE_CHOICES = (

    ('CHAIN','chain'),
    ('IMAGE','image'),
    ('VIDEO','video'),
    ('DOCUMENT','document'),
    ('FORM','form'),
    ('PHONE','phone'),
    ('TEXT','text'),
    ('CARDS','cards'),
    ('TITLE','title'),
    ('URL','url'),
    ('LOCATION','location'),
    ('MAIN','main'),
    ('ATM/BRANCH', 'ATM/Branch'),
    ('EMI_CALCULATOR','EMI Calculator'),
    ('INTEREST_CALCULATOR', 'Interest Calculator'),
    ('RD_CALCULATOR','RD Calculator'),
    ('ELIGIBILITY_CALCULATOR','Eligibility Calculator 1'),
    ('SWP_CALCULATOR','SWP Calculator'),
    ('INFLATION_CALCULATOR','Inflation Calculator'),
    ('FD_CALCULATOR','FD, Calculator'),
    ('SIP_CALCULATOR','SIP Calculator'),
)
TEMPLATE_BUTTON_TYPE_CHOICES = (

    ('URL','Url'),
    ('IMAGE','image'),
    ('VIDEO','video'),
    ('DOCUMENT','document'),
    ('LOCATION','location'),
    ('PHONE_NUMBER','Phone Number'),
    ('STOP','Stop'),
    ('FORM','form'),
    ('INFLOW','Inflow'),
    ('CAMPAIGN','Campaign'),
)
CAUROSEL_CARD_TYPE_CHOICES = (
    ('URL','Url'),
    ('IMAGE','image'),
    ('VIDEO','video'),
    ('DOCUMENT','document'),
    ('LOCATION','location'),
    ('PHONE_NUMBER','Phone Number'),
    ('STOP','Stop'),
    ('FORM','form'),
    ('INFLOW','Inflow'),
    ('CAMPAIGN','Campaign'),
)

PREOTP_CHOICES=(
    ('no','Not Required'),
    ('required by email', 'REQUIRED BY EMAIL'),
    ('required by sms','REQUIRED BY SMS'),
    
)

AUTHORIZATION_CHOICES=(
    ('NO','Not Required'),
    ('FIRSTTIME', 'First Time Required'),
    ('ALWAYS','Always Required'),
)

ACCESSTYPE_CHOICES =(
    ('PRIVATE','Private'),
    ('PUBLIC','Public'),
)




CARD_TYPES = (
    ('image','IMAGE'),
    ('video','VIDEO'),
)

REQUIRED_FIELD_CHOICES=(
    ('True','TRUE'),
    ('False','FALSE')

)
LANGUAGE_CHOICES = (
    ('af', 'Afrikaans'),
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('hy', 'Armenian'),
    ('az', 'Azerbaijani'),
    ('eu', 'Basque'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('bs', 'Bosnian'),
    ('bg', 'Bulgarian'),
    ('ca', 'Catalan'),
    ('ceb', 'Cebuano'),
    ('ny', 'Chichewa'),
    ('zh', 'Chinese'),
    ('co', 'Corsican'),
    ('hr', 'Croatian'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('nl', 'Dutch'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('fil', 'Filipino'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('fy', 'Frisian'),
    ('gl', 'Galician'),
    ('ka', 'Georgian'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('gu', 'Gujarati'),
    ('ht', 'Haitian Creole'),
    ('ha', 'Hausa'),
    ('haw', 'Hawaiian'),
    ('he', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hmn', 'Hmong'),
    ('hu', 'Hungarian'),
    ('is', 'Icelandic'),
    ('ig', 'Igbo'),
    ('id', 'Indonesian'),
    ('ga', 'Irish'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('jv', 'Javanese'),
    ('kn', 'Kannada'),
    ('kk', 'Kazakh'),
    ('km', 'Khmer'),
    ('rw', 'Kinyarwanda'),
    ('ko', 'Korean'),
    ('ku', 'Kurdish'),
    ('ky', 'Kyrgyz'),
    ('lo', 'Lao'),
    ('la', 'Latin'),
    ('lv', 'Latvian'),
    ('lt', 'Lithuanian'),
    ('lb', 'Luxembourgish'),
    ('mk', 'Macedonian'),
    ('mg', 'Malagasy'),
    ('ms', 'Malay'),
    ('ml', 'Malayalam'),
    ('mt', 'Maltese'),
    ('mi', 'Maori'),
    ('mr', 'Marathi'),
    ('mn', 'Mongolian'),
    ('my', 'Myanmar (Burmese)'),
    ('ne', 'Nepali'),
    ('no', 'Norwegian'),
    ('or', 'Odia (Oriya)'),
    ('ps', 'Pashto'),
    ('fa', 'Persian'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('pa', 'Punjabi'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('sm', 'Samoan'),
    ('gd', 'Scots Gaelic'),
    ('sr', 'Serbian'),
    ('st', 'Sesotho'),
    ('sn', 'Shona'),
    ('sd', 'Sindhi'),
    ('si', 'Sinhala'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('so', 'Somali'),
    ('es', 'Spanish'),
    ('su', 'Sundanese'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('tg', 'Tajik'),
    ('ta', 'Tamil'),
    ('tt', 'Tatar'),
    ('te', 'Telugu'),
    ('th', 'Thai'),
    ('tr', 'Turkish'),
    ('tk', 'Turkmen'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('ug', 'Uyghur'),
    ('uz', 'Uzbek'),
    ('vi', 'Vietnamese'),
    ('cy', 'Welsh'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('yo', 'Yoruba'),
    ('zu', 'Zulu'),
)

GROUP_CHOICES=(
    ('None','NONE'),
    ('Private','PRIVATE'),
    ('Public','PUBLIC')
)

OPTIN_CHOICES=(
    ('No','NO'),
    
)
AUTHORIZATION_STATUS=(
    ('Done','DONE'),
)
OTP_CHOICES=(
    ('Verified','VERIFIED'),
    ('Unverified','UNVERIFIED')
)



CARDS_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
)

USER_LANGUAGE_CHOICES=(
    ('NO','Not Required'),
    ('FIRSTTIME', 'First Time Required'),
    ('ALWAYS','Always Required'),
)

TRANSLATION_CHOICES=(
    ('BASE','Base'),
    ('AUTO TRANSLATION','Auto Translation')
)

TRANSLATION_STATUS_CHOICES = (
    ('None','NONE'),
    ('pending','PENDING'),
    ('completed','COMPLETED'),
)

class campaign_marketplace_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_flow_id = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    my_campaign_flow_id = models.CharField(max_length=500, null=True, blank=True)
    master_card_template_name = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_image = models.ImageField(upload_to='FlowImage', null=True, blank=True)
    marketplace_welcome_message_body = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_message_footer = models.CharField(max_length=500, null=True, blank=True)
    generic_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    mycampaign_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)



class campaign_marketplace(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=500, null=True, blank=True)
    campaign_type = models.CharField(max_length=500, null=True, blank=True)
    campaign_category = models.CharField(max_length=500, null=True, blank=True)
    campaign_location = models.CharField(max_length=500, null=True, blank=True)
    campaign_description = models.CharField(max_length=500, null=True, blank=True)
    campaign_contact_number = models.CharField(max_length=300, null=True, blank=True)
    campaign_id = models.CharField(max_length=300, null=True, blank=True)
    campaign_key = models.CharField(max_length=300, null=True, blank=True)
    campaign_url = models.CharField(max_length=300, null=True, blank=True)
    campaign_link_text = models.CharField(max_length=300, null=True, blank=True)




class generic_campaign_info(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Campaign_Name = models.CharField(max_length=300,null=True, blank=True)
    Campaign_short_message = models.CharField(max_length=300,null=True, blank=True)
    Campaign_message = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Image = models.ImageField(upload_to='CampaignImage', null=True, blank=True)
    Campaign_First_Button_Name = models.CharField(max_length=300,null=True, blank=True)
    Campaign_Second_Button_Name = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Third_Button_Name = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Status = models.IntegerField(null=True,blank=True)
    default_campaign = models.CharField(max_length=100, choices=CHOOSE_CAMPAIGN, default='none')
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class template_info(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    generic_campaign_info = models.ForeignKey(generic_campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    template_name = models.CharField(max_length=300,null=True, blank=True)
    template_header_text = models.CharField(max_length=300,null=True, blank=True)
    template_header_image = models.ImageField(upload_to='TemplateImage', null=True, blank=True)
    template_header_file_path=models.FileField(upload_to='TemplateHeaderFile', null=True, blank=True)
    template_body_message = models.CharField(max_length=1024,null=True, blank=True)
    template_header_type = models.CharField(max_length=100, choices=CHOOSE_CHOICES, default='none')
    status = models.CharField(max_length=255, choices=TEMPLATE_TYPE_CHOICES, default='none')
    template_footer = models.CharField(max_length=300,null=True, blank=True)


class template_info_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    template_info = models.ForeignKey(template_info, on_delete=models.CASCADE, null=True, blank=True)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    generic_campaign_info = models.ForeignKey(generic_campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    template_button_num = models.IntegerField(null=True,blank=True)
    template_button_name = models.CharField(max_length=300,null=True, blank=True)
    template_button_type = models.CharField(max_length=300,choices=TEMPLATE_BUTTON_TYPE_CHOICES,null=True, blank=True)
    template_additional_info = models.CharField(max_length=300,null=True, blank=True)
    template_file_path = models.FileField(upload_to='ButtonType', null=True, blank=True)
    additional_file_path1 = models.FileField(upload_to='SecondButtonType', null=True, blank=True)
    additional_file_path2 = models.FileField(upload_to='ThirdButtonType', null=True, blank=True)
    template_additional_info1 = models.CharField(max_length=300, null=True, blank=True)
    template_additional_info2 = models.CharField(max_length=300, null=True, blank=True)
    location_longitude = models.CharField(max_length=300, null=True, blank=True)
    location_latitude = models.CharField(max_length=300, null=True, blank=True)
    location_name = models.CharField(max_length=300, null=True, blank=True)
    location_address = models.CharField(max_length=300, null=True, blank=True)



class campaign_customer_master(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Customer_Name = models.CharField(max_length=300, null=True, blank=True)
    Customer_email = models.EmailField(max_length=200, null=True, blank=True)
    Customer_Whatsapp_Number = models.CharField(max_length=300, null=True, blank=True)
    Customer_tag = models.CharField(max_length=100, null=True, blank=True)
    Customer_City = models.CharField(max_length=300, null=True, blank=True)
    Customer_Status = models.IntegerField(null=True, blank=True)
    Customer_Address_Line1 = models.CharField(max_length=300, null=True, blank=True)
    Customer_Address_Line2 = models.CharField(max_length=300, null=True, blank=True)
    Customer_Address_Landmark = models.CharField(max_length=300, null=True, blank=True)
    Customer_Address_Pincode = models.CharField(max_length=300, null=True, blank=True)
    Customer_State = models.CharField(max_length=300, null=True, blank=True)
    Customer_Country = models.CharField(max_length=300, null=True, blank=True)
    Customer_Alternate_Number = models.CharField(max_length=300, null=True, blank=True)
    optin_status=models.CharField(max_length=30,choices=OPTIN_CHOICES, null=True, blank=True)
    authorization_status=models.CharField(max_length=30,choices=AUTHORIZATION_STATUS, null=True, blank=True)
    otp= models.CharField(max_length=10, null=True, blank=True)
    otp_generated_time= models.TimeField(null=True, blank=True)
    otp_status=models.CharField(max_length=40, choices=OTP_CHOICES,null=True, blank=True)
    preferred_language=models.CharField(max_length=40,null=True, blank=True)
    preferred_language_status=models.CharField(max_length=40,choices=AUTHORIZATION_STATUS,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)





class campaign_group_types(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    campaign_group_type = models.CharField(max_length=200,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class campaign_group_categorys(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    campaign_group_category = models.CharField(max_length=200,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class campaign_payment_settings(models.Model):
    contact_name=models.CharField(max_length=200,null=True, blank=True)
    contact_number=models.CharField(max_length=200,null=True, blank=True)
    payment_gateway = models.CharField(max_length=200,null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class campaign_payment_gateway_details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    payment_gateway = models.CharField(max_length=200, null=True, blank=True)
    gateway_id = models.CharField(max_length=200,null=True, blank=True)
    gateway_key = models.CharField(max_length=200,null=True, blank=True)
    currency = models.CharField(max_length=200, choices=CURRENCY_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Form(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    form_name = models.CharField(max_length=255, null=True, blank=True)
    flow_id = models.CharField(max_length=255, null=True, blank=True)
    screen_name = models.CharField(max_length=255, null=True, blank=True)
    form_header_type = models.CharField(max_length=255, choices=FORM_HEADER_TYPE_CHOICES,null=True, blank=True)
    form_header_text = models.CharField(max_length=255, null=True, blank=True)
    form_header_image = models.ImageField(upload_to='FormImage', null=True, blank=True)
    form_body_text = models.CharField(max_length=1024, null=True, blank=True)
    form_body_footer = models.CharField(max_length=255, null=True, blank=True)
    form_submit_button_name = models.CharField(max_length=255, null=True, blank=True)
    form_open_button_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices =STATUS_TYPE_CHOICES,default='none')
    form_header_text_key = models.CharField(max_length=255, null=True, blank=True)
    form_body_text_key = models.CharField(max_length=1024, null=True, blank=True)
    form_body_footer_key = models.CharField(max_length=255, null=True, blank=True)
    form_submit_button_name_key = models.CharField(max_length=255, null=True, blank=True)
    form_open_button_name_key = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['client', 'marketplace', 'form_name'], name='unique_form')
        ]


class Form_Section(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="sections")
    section_name_key = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Form_Field(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    field_type = models.CharField(max_length=50, choices=FIELD_TYPE_CHOICES)
    required_type= models.CharField(max_length=50, choices=REQUIRED_FIELD_CHOICES, default=None)
    section = models.ForeignKey(Form_Section, on_delete=models.CASCADE, related_name="form_fields")
    form_label_key = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Form_FieldChoice(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    field = models.ForeignKey(Form_Field, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=255, null=True, blank=True)
    choice_text_key = models.CharField(max_length=255, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class Inflow_Setup_Details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Parent_ID = models.CharField(max_length=255, null=True, blank=True)
    Reference_Id = models.CharField(max_length=100, null=True, blank=True)
    open_button_type = models.CharField(max_length=200, choices=BUTTON_TYPE_CHOICES, null=True, blank=True)
    open_button_name = models.CharField(max_length=255, null=True, blank=True)
    short_title = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    additional_info = models.CharField(max_length=300, null=True, blank=True)
    additional_info1 = models.CharField(max_length=300, null=True, blank=True)
    additional_info2 = models.CharField(max_length=300, null=True, blank=True)
    additional_file_path = models.FileField(upload_to='InflowType', null=True, blank=True)
    additional_file_path1 = models.FileField(upload_to='SecondInflowType', null=True, blank=True)
    additional_file_path2 = models.FileField(upload_to='ThirdInflowType', null=True, blank=True)
    inflow_header_type = models.CharField(max_length=100, choices=CHOOSE_CHOICES, default='none')
    inflow_header_text = models.CharField(max_length=300, null=True, blank=True)
    inflow_header_file_path = models.FileField(upload_to='InflowHeaderType', null=True, blank=True)
    inflow_body_text = models.CharField(max_length=1024, null=True, blank=True)
    inflow_footer_text = models.CharField(max_length=300, null=True, blank=True)
    longitude =  models.CharField(max_length=100, null=True, blank=True)
    latitude =  models.CharField(max_length=100, null=True, blank=True)
    location_name = models.CharField(max_length=300, null=True, blank=True)
    address= models.CharField(max_length=500, null=True, blank=True)
    short_title_key = models.CharField(max_length=255, null=True, blank=True)
    short_description_key = models.CharField(max_length=255, null=True, blank=True)
    open_button_name_key = models.CharField(max_length=255, null=True, blank=True)
    active_status = models.CharField(max_length=20, null=True, blank=True)
    inflow_header_text_key = models.CharField(max_length=300, null=True, blank=True)
    inflow_body_text_key = models.CharField(max_length=1024, null=True, blank=True)
    inflow_footer_text_key = models.CharField(max_length=300, null=True, blank=True)
    image_additional_file_path_key = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class campaign_footprint(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    From_number = models.CharField(max_length=300, null=True, blank=True)
    button = models.CharField(max_length=300, null=True, blank=True)
    campaign_name = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class campaign_formdata(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    generic_campaign_info = models.ForeignKey(generic_campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    Form = models.ForeignKey(Form, on_delete=models.CASCADE, null=True, blank=True)
    Campaign_Form_data = models.JSONField(null=True, blank=True)
    form_info = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class campaign_groups(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    group_name = models.CharField(max_length=100, null=True, blank=True)
    group_type = models.CharField(max_length=100,choices=GROUP_CHOICES ,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class campaign_group_customer_mappings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    campaign_groups = models.ForeignKey(campaign_groups, on_delete=models.CASCADE, null=True, blank=True)
    campaign_customer_master = models.ForeignKey(campaign_customer_master, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(default=timezone.now)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)



class generic_campaign_history(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    generic_campaign_info = models.ForeignKey(generic_campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    template_info = models.ForeignKey(template_info, on_delete=models.CASCADE, null=True, blank=True)
    campaign_customer_master = models.ForeignKey(campaign_customer_master, on_delete=models.CASCADE, null=True, blank=True)
    Campaign_Name = models.CharField(max_length=300, null=True, blank=True)
    Campaign_short_message = models.CharField(max_length=300, null=True, blank=True)
    Campaign_message = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Image = models.ImageField(upload_to='CampaignImage', null=True, blank=True)
    Campaign_Status = models.CharField(max_length=300, null=True, blank=True)
    Campaign_Foot_Print = models.JSONField(null=True, blank=True)
    Campaign_Form_data = models.JSONField(null=True, blank=True)
    Customer_Whatsapp_Number = models.CharField(max_length=300, null=True, blank=True)
    message_id = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
    campaign_sent_datetime = models.DateTimeField(null=True, blank=True)


class carousel_template(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    carousel_template_name = models.CharField(max_length=300, null=True, blank=True)
    carousel_buble_text = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class carousel_template_buttons(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    carousel_template = models.ForeignKey(carousel_template, on_delete=models.CASCADE, null=True, blank=True)
    carousel_button_name = models.CharField(max_length=300, null=True, blank=True)
    carousel_button_type = models.CharField(max_length=300, null=True, blank=True)
    carousel_additional_info = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Form1(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True, blank=True)

class Section(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    form1 = models.ForeignKey(Form1, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)

class Field(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,null=True, blank=True)
    label = models.CharField(max_length=100,null=True, blank=True)
    field_type = models.CharField(max_length=20,null=True, blank=True)

class Choice(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)
    choice_text = models.CharField(max_length=255, null=True, blank=True)

class Pre_Inflow_Settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Preotp = models.CharField(max_length=20, choices=PREOTP_CHOICES, null=True, blank=True)
    Preauthorization = models.CharField(max_length=20, choices=AUTHORIZATION_CHOICES, null=True, blank=True)
    AuthorizationText = models.CharField(max_length=500, null=True, blank=True)
    AccessType = models.CharField(max_length=20, choices=ACCESSTYPE_CHOICES, null=True, blank=True)
    LanguagePref = models.CharField(max_length=50, choices=USER_LANGUAGE_CHOICES, null=True, blank=True)
    otp_flow_id=models.CharField(max_length=30,null=True, blank=True)
    default_translation=models.CharField(max_length=50, choices=TRANSLATION_CHOICES, null=True, blank=True)
    authorization_text_key = models.CharField(max_length=100,null=True, blank=True)
    choose_language_body_text = models.CharField(max_length=300,null=True, blank=True)
    choose_language_body_text_key = models.CharField(max_length=100,null=True, blank=True)
    verify_otp_text = models.CharField(max_length=300,null=True, blank=True)
    verify_otp_text_key = models.CharField(max_length=100,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Carousel_Cards(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_campaign_info = models.ForeignKey(generic_campaign_info, on_delete=models.CASCADE, null=True, blank=True)
    template_info = models.ForeignKey(template_info, on_delete=models.CASCADE, null=True, blank=True)
    number_of_cards = models.CharField(max_length=100, choices=CARDS_CHOICES, default='none')
    card_header_type = models.CharField(max_length=100, choices=CARD_TYPES, default='none')
    carousel_button1_type = models.CharField(max_length=300,choices=CAUROSEL_CARD_TYPE_CHOICES,null=True, blank=True)
    carousel_button1_name = models.CharField(max_length=300,null=True, blank=True)
    carousel_button1_additional_info = models.CharField(max_length=300,null=True, blank=True)
    carousel_button1_file_path = models.FileField(upload_to='CardType', null=True, blank=True)
    carousel_button2_type = models.CharField(max_length=300,choices=CAUROSEL_CARD_TYPE_CHOICES,null=True, blank=True)
    carousel_button2_name = models.CharField(max_length=300,null=True, blank=True)
    carousel_button2_additional_info = models.CharField(max_length=300,null=True, blank=True)
    carousel_button2_file_path = models.FileField(upload_to='Card', null=True, blank=True)
    location_longitude = models.CharField(max_length=300, null=True, blank=True)
    location_latitude = models.CharField(max_length=300, null=True, blank=True)
    location_name = models.CharField(max_length=300, null=True, blank=True)
    location_address = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Carousel_Cards_Details(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    carousel_cards = models.ForeignKey(Carousel_Cards, on_delete=models.CASCADE, null=True, blank=True)
    card_header_file_path = models.FileField(upload_to='CardHeaderType', null=True, blank=True)
    card_header_body_text = models.CharField(max_length=1024, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Language_Key(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    key = models.CharField(max_length=200, null=True, blank=True)
    word = models.CharField(max_length=500, blank=True, null=True)
    translation_status = models.CharField(max_length=90, choices=TRANSLATION_STATUS_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
    
    
class Language_Value(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Key_language = models.ForeignKey(Language_Key, on_delete=models.CASCADE,null=True, blank=True)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, null=True, blank=True)
    Value = models.CharField(max_length=500, null=True, blank=True)
    auto_value = models.CharField(max_length=500, blank=True, null=True)
    languages_file_path = models.FileField(upload_to='language_file', null=True, blank=True)
    translation_status = models.CharField(max_length=90, choices=TRANSLATION_STATUS_CHOICES, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Client_Preferred_Language(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    preferred_language_Code = models.ForeignKey(Language_Value, on_delete=models.CASCADE, null=True, blank=True)
    preferred_language_name = models.CharField(max_length=100, null=True, blank=True)
    preferred_language_key = models.CharField(max_length=100, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


