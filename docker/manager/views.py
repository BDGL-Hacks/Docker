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
def create_container(request):
	if request.method == 'GET':
		form = CreateInstForm(request.GET)
		if form.is_valid():
 
 			''' 
 				TODO: This is horrible code, and not even how its going to be processed
 				when dynamic forms are introduced. When it is redone, feel free to uproot
 				this entirely... sorry
 			'''
			# Get and process the data from the form into the required format
			data = form.cleaned_data
			container_name = data["container_name"]
			image_name = data["image_name"]
			quantity = data["quantity"]
			links = [data["links"]]
			if (data["4links"] == ""):
				links = []
			host_mounts = {}
			host_mounts[data["host_mount_local_path"]] = data["host_mount_dest_path"]
			if (data["host_mount_local_path"] == ""):
				host_mounts = {}
			external_mounts = [data["external_mounts"]]
			if (data["external_mounts"] == ""): 
				external_mounts = []
			custom_mounts = [data["custom_mounts"]]
			if (data["custom_mounts"] == ""): 
				custom_mounts = []
			is_interactive = data["is_interactive"]
			is_background = data["is_background"]

			# Create and start the new container
			utils.start_container(container_name, image_name, quantity, links,
				host_mounts, external_mounts, custom_mounts, is_interactive,
				is_background)

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