from django.db import models
from Admin.models import *

# Create your models here.
class User_login(models.Model):
	user_username =  models.CharField(max_length=100)
	user_first_name = models.CharField(max_length=100)
	user_last_name = models.CharField(max_length=100)    
	user_email = models.EmailField()  
	user_contact = models.CharField(max_length=10)
	user_password = models.CharField(max_length=16)  
	class Meta:
		db_table = "User_login"  

class Booking(models.Model):
	booking_name = models.CharField(max_length=100)
	booking_email = models.EmailField(max_length=100)
	booking_contact = models.CharField(max_length=15)
	booking_date = models.CharField(max_length=200)
	booking_adults = models.CharField(max_length=5)
	booking_kids = models.CharField(max_length=5)
	booking_message = models.CharField(max_length=500)
	booking_tour_id = models.ForeignKey(Tour,default=1,on_delete=models.PROTECT)
	class Meta:
		db_table = "Booking"
	

class Contact(models.Model):
	contact_name = models.CharField(max_length=100)
	contact_email = models.EmailField()
	contact_contact = models.CharField(max_length=10)
	contact_message = models.CharField(max_length=500)
	class Meta:
		db_table="Contact"

