import json
import utils
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import CreateInstForm

# Homepage
def home(request):
	return render(request, 'manager/main_panel.html')

# Launch new instances
def create_image(request):
	if request.method == 'GET':
		form = CreateInstForm(request.GET)
		if form.is_valid():
			# Create new containers with given parameters
			return HttpResponseRedirect('/')
	else:
		form = CreateInstForm()

	return render(request, 'manager/create_instance.html', { 'form': form })

# Display existing instances
def display_instances(request):
	# Get existing containers
	status = utils.get_status()
	keys = status[status.keys()[0]].keys()
	
	return render(request, 'manager/monitor_instances.html', { 'keys': keys, 'containers': status })