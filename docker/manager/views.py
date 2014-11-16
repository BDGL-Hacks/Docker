import json
import utils
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import CreateInstForm

'''
Homepage
'''
def home(request):
	return render(request, 'manager/main_panel.html')

'''
Launch new instances

TODO: Actually make the new container
'''
def create_image(request):
	if request.method == 'GET':
		form = CreateInstForm(request.GET)
		if form.is_valid():
			# Create new containers with given parameters
			return HttpResponseRedirect('/')
	else:
		form = CreateInstForm()

	return render(request, 'manager/create_instance.html', { 'form': form })

'''
Display existing instances

TODO: Add filters
	  Add ability to select container and view detailed information (CPU, disk, ip, make new image, etc. (docker inspect))
	  Fix table so that the port/name is fixed
'''
def display_instances(request):
	# Get existing containers
	status = utils.get_status()
	keys = status[status.keys()[0]].keys()
	
	return render(request, 'manager/monitor_instances.html', { 'keys': keys, 'containers': status })

'''
Display existing images

TODO: Add ability to create new image from this page
'''
def display_images(request):
	# Get existing images
	images = utils.get_images()
	keys = images[images.keys()[0]].keys()

	return render(request, 'manager/images.html', { 'keys': keys, 'images': images })