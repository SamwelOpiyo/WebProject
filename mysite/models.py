from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from datetime import date, datetime
from django import forms

class BookAppointment(models.Model):
    type_gender = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone Number must be entered\
        in the format: '+999999999'. Up to 15 digits allowed.")
    email_regex = RegexValidator(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , message="Invalid e-mail address entered")
    first_name = models.CharField(default=None, max_length=30)
    second_name = models.CharField(default=None, max_length=30)
    gender = models.CharField(default=None, max_length=10, choices=type_gender)
    email_address = models.EmailField(default=None, max_length=70, validators=[email_regex])
    phone_number = models.CharField(default=None, max_length=15, validators=[phone_regex])
    date = models.DateField(default=date.today)
    source = models.CharField(default=None, max_length=50)
    specification_source = models.TextField(blank=True, null=True)
    date_entry = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)   
    
    
    


class BookAppointmentForm(forms.ModelForm):
    class Meta:
        model=BookAppointment
        fields=['first_name','second_name','gender','email_address','phone_number','date','source','specification_source']    


class ContactMe(models.Model): 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone Number must be entered\
        in the format: '+999999999'. Up to 15 digits allowed.")
    email_regex = RegexValidator(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , message="Invalid e-mail address entered")
    first_name = models.CharField(default=None, max_length=30)
    second_name = models.CharField(default=None, max_length=30, blank=True)
    email_address = models.EmailField(default=None, max_length=70, validators=[email_regex])
    phone_number = models.CharField(default=None, max_length=15, blank=True, validators=[phone_regex])
    message = models.TextField(default=None)
    date_entry = models.DateTimeField(null=True, auto_now_add=True)
    last_modified = models.DateTimeField(null=True, auto_now=True)







class ContactMeForm(forms.ModelForm):
    class Meta:
        model=ContactMe
        fields=['first_name','second_name','email_address','phone_number','message',]


# Create your models here.
