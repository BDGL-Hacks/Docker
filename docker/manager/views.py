from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'manager/main_panel.html')

def create_image(request):
	return render(request, 'manager/create_instance.html')