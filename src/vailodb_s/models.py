from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Survey_marketplace_settings(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    generic_flow_id = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_id = models.CharField(max_length=500, null=True, blank=True)
    my_survey_flow_id = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_image = models.ImageField(upload_to='FlowImage', null=True, blank=True)
    marketplace_welcome_message_body = models.CharField(max_length=500, null=True, blank=True)
    marketplace_welcome_message_footer = models.CharField(max_length=500, null=True, blank=True)
    generic_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    specific_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)
    mysurvey_flow_cta_name = models.CharField(max_length=500, null=True, blank=True)


class Survey_marketplace(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    survey_name = models.CharField(max_length=500, null=True, blank=True)
    survey_type = models.CharField(max_length=500, null=True, blank=True)
    survey_category = models.CharField(max_length=500, null=True, blank=True)
    survey_location = models.CharField(max_length=500, null=True, blank=True)
    survey_description = models.CharField(max_length=500, null=True, blank=True)
    survey_contact_number = models.CharField(max_length=300, null=True, blank=True)
    survey_id = models.CharField(max_length=300, null=True, blank=True)
    survey_key = models.CharField(max_length=300, null=True, blank=True)
    survey_url = models.CharField(max_length=300, null=True, blank=True)
    survey_link_text = models.CharField(max_length=300, null=True, blank=True)

class Survey_list(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    survey_image = models.ImageField(upload_to='SurveyImage', null=True, blank=True)
    survey_message = models.CharField(max_length=500, null=True, blank=True)
    survey_footer = models.CharField(max_length=500, null=True, blank=True)
    survey_type = models.CharField(max_length=500, null=True, blank=True)
    survey_status = models.CharField(max_length=500, null=True, blank=True)
    flow_id = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Survey_Question(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Survey_list = models.ForeignKey(Survey_list, on_delete=models.CASCADE, null=True, blank=True)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=500, null=True, blank=True)
    question_type = models.CharField(max_length=500, null=True, blank=True)
    response_option1 = models.CharField(max_length=500, null=True, blank=True)
    response_option2 = models.CharField(max_length=500, null=True, blank=True)
    response_option3 = models.CharField(max_length=500, null=True, blank=True)
    response_option4 = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


# class Survey_Question_Mapping(models.Model):
#     client = models.ForeignKey(User, on_delete=models.CASCADE)
#     Survey_list = models.ForeignKey(Survey_list,on_delete=models.CASCADE,null=True, blank=True)
#     vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
#     vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
#     vailo_record_status = models.IntegerField(null=True, blank=True)

class Survey_Customer(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Survey_list = models.ForeignKey(Survey_list, on_delete=models.CASCADE, null=True, blank=True)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    customer_name = models.CharField(max_length=300, null=True, blank=True)
    customer_email = models.EmailField(max_length=200, null=True, blank=True)
    customer_whatsapp_number = models.CharField(max_length=300, null=True, blank=True)
    customer_city = models.CharField(max_length=300, null=True, blank=True)
    customer_status = models.IntegerField(null=True, blank=True)
    customer_address_line1 = models.CharField(max_length=300, null=True, blank=True)
    customer_address_line2 = models.CharField(max_length=300, null=True, blank=True)
    customer_address_landmark = models.CharField(max_length=300, null=True, blank=True)
    customer_address_pincode = models.CharField(max_length=300, null=True, blank=True)
    customer_state = models.CharField(max_length=300, null=True, blank=True)
    customer_country = models.CharField(max_length=300, null=True, blank=True)
    customer_alternate_number = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class Survey_Customer_Response(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Survey_list = models.ForeignKey(Survey_list, on_delete=models.CASCADE, null=True, blank=True)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    Survey_Question = models.ForeignKey(Survey_Question, on_delete=models.CASCADE, null=True, blank=True)
    Survey_Customer = models.ForeignKey(Survey_Customer, on_delete=models.CASCADE, null=True, blank=True)
    Survey_Response = models.CharField(max_length=300, null=True, blank=True)
    Survey_comments = models.CharField(max_length=300, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)


class Survey_Question_Map(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    Survey_list = models.ForeignKey(Survey_list,on_delete=models.CASCADE,null=True, blank=True)
    Survey_Customer = models.ForeignKey(Survey_Customer, on_delete=models.CASCADE, null=True, blank=True)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class survey_types(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    survey_type = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

class survey_categorys(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Survey_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    survey_category = models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)

