from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import CreateInstForm

# Create your views here.
def home(request):
	return render(request, 'manager/main_panel.html')

def create_image(request):
	if request.method == 'GET':
		form = CreateInstForm(request.GET)
		if form.is_valid():
			# Create new containers with given parameters
			return HttpResponseRedirect('/')
	else:
		form = CreateInstForm()

	return render(request, 'manager/create_instance.html', { 'form': form })