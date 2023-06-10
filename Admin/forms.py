from django import forms
from Admin.models import *

class Tour_form(forms.ModelForm):
	class Meta:
		model = Tour
		fields = '__all__'

class Destination_form(forms.ModelForm):
	class Meta:
		model = Destination
		fields = '__all__'

class Hotel_form(forms.ModelForm):
	class Meta:
		model = Hotel
		fields = '__all__'
