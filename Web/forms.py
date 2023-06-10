from django import forms
from Web.models import *

class User_login_form(forms.ModelForm):
	user_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User_login
		fields = '__all__'

class Booking_form(forms.ModelForm):
	booking_name = forms.CharField(widget=forms.TextInput({ "placeholder": "Name","class":"form-control"}))
	booking_email = forms.EmailField(widget=forms.EmailInput({ "placeholder": "Email","class":"form-control","type":"email"}))
	booking_contact = forms.CharField(widget=forms. TextInput({"placeholder": "Contact","class":"form-control","type":"tel","pattern":"[0-9]{3}[0-9]{3}[0-9]{4}"}),required=True)
	booking_date = forms.CharField(widget=forms. TextInput({"placeholder": "Date","class":"form-control"}))
	booking_choices_adults = (('0','Adults'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5 or more'))
	booking_choices_kids = (('0','Kids'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5 or more'))
	booking_adults = forms.CharField(widget=forms.Select(choices=booking_choices_adults,attrs={"placeholder": "Adults","class":"form-control"}))
	booking_kids = forms.CharField(widget=forms.Select(choices=booking_choices_kids,attrs={"placeholder": "Kids","class":"form-control"}))
	booking_message = forms.CharField(widget = forms.Textarea({"placeholder": "Message","class":"form-control","rows":"3"}))
	class Meta:
		model = Booking
		fields='__all__'
		exclude = ['booking_tour_id']

class Contact_form(forms.ModelForm):
	contact_name = forms.CharField(widget=forms.TextInput({ "placeholder": "Name","class":"form-control"}))
	contact_email = forms.EmailField(widget=forms.EmailInput({ "placeholder": "Email","class":"form-control","type":"email"}))
	contact_contact = forms.CharField(widget=forms. TextInput({"placeholder": "Contact","class":"form-control","type":"tel","pattern":"[0-9]{3}[0-9]{3}[0-9]{4}"}),required=True)
	contact_message = forms.CharField(widget = forms.Textarea({"placeholder": "Message","class":"form-control","rows":"3"}))
	
	class Meta:
		model=Contact
		fields='__all__'


