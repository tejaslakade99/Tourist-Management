from django.db import models
# Create your models here.

class Destination(models.Model):
	des_name = models.CharField(max_length=100)
	des_location = models.CharField(max_length=100)
	des_duration = models.IntegerField()
	des_price = models.IntegerField()
	des_description=models.CharField(max_length=500)
	des_image = models.ImageField(upload_to='Destination_images/')
	class Meta:
		db_table = "Destination"
	def __str__(self):
		return self.des_name 

class Hotel(models.Model):
	hotel_name = models.CharField(max_length=100)
	hotel_location = models.CharField(max_length=100)
	hotel_duration = models.IntegerField()
	hotel_price = models.IntegerField()
	hotel_description=models.CharField(max_length=500)
	hotel_image = models.ImageField(upload_to='Hotel_images/')
	class Meta:
		db_table = "Hotel"
	def __str__(self):
		return self.hotel_name 

class Tour(models.Model):
	tour_name = models.CharField(max_length=100)
	tour_location = models.CharField(max_length=100)
	tour_duration = models.IntegerField()
	tour_price = models.IntegerField()
	tour_description=models.CharField(max_length=500)
	tour_image = models.ImageField(upload_to='Tour_images/')
	tour_des_id = models.ForeignKey(Destination,default=1,on_delete=models.PROTECT)
	tour_hotel_id = models.ForeignKey(Hotel,default=1,on_delete=models.PROTECT)
	class Meta:
		db_table = "Tour"
	def __str__(self):
		return self.tour_name 

