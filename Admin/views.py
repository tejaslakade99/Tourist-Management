from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template
from Admin.forms import *
from Admin.models import *
# Create your views here.

def adminweb(request):
	if request.method == 'POST':
		form = User_login_form(request.POST)
		try:
			form.save()
		except Exception as e:
			print(e)
		
		if form.is_valid():
			form.save()
			return HttpResponse('Success')
		else:
			print()
			return render(request,"adminweb.html",{'form':form})
	else:
		form = User_login_form()
		return render(request, "adminweb.html",{'form':form })


def packages(request):
	tour_form = Tour_form()
	tour_posts = Tour.objects.all()
	des_form = Destination_form()
	des_posts = Destination.objects.all()
	hotel_form = Hotel_form()
	hotel_posts = Hotel.objects.all()
	args = {'tour_form':tour_form,'tour_posts':tour_posts,'des_form':des_form,'des_posts':des_posts,'hotel_form':hotel_form,'hotel_posts':hotel_posts}
	return render(request,"packages.html",args)