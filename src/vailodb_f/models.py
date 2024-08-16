from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import pytz
from vailodb_b.models import *

# Create your models hre.
OTP_CHOICE=(
    ('Yes','Yes'),
    ('No,','no'),
)

SERVICES_CHOICE=(
    ('ATM','ATM'),
    ('BRANCH', 'BRANCH'),
    ('BOTH','BOTH'),
)

class Banking_configuration(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    calculator_status = models.CharField(max_length=20,null=True, blank=True)
    atm_branch_status = models.CharField(max_length=20,null=True, blank=True)
    atm_branch_pincode_flowid = models.CharField(max_length=100,null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
    
class Branch_ATM(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    PIN_code= models.IntegerField(null=True, blank=True)
    IFSC_code = models.CharField(max_length=50, null=True, blank=True)
    Services = models.CharField(max_length=20, choices=SERVICES_CHOICE, null=True, blank=True)
    Address= models.CharField(max_length=500, null=True, blank=True)
    landmark = models.CharField(max_length=500, null=True, blank=True)
    longitude =  models.CharField(max_length=100, null=True, blank=True)
    latitude =  models.CharField(max_length=100, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True,blank=True,null=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False,blank=True, null=True,auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)
    
class Banking_Calculators(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(campaign_marketplace, on_delete=models.CASCADE, null=True, blank=True)
    calculator_Code=models.CharField(max_length=500, null=True, blank=True)
    calculator_Name=models.CharField(max_length=500, null=True, blank=True)
    calculator_FlowID=models.CharField(max_length=500, null=True, blank=True)
    vailo_record_creation = models.DateTimeField(auto_now_add=True,blank=True,null=True, auto_now=False)
    vailo_record_last_update = models.DateTimeField(auto_now_add=False,blank=True, null=True,auto_now=True)
    vailo_record_status = models.IntegerField(null=True, blank=True)