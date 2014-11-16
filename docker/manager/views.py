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
Launch new container(s) using CreateInstForm data
'''
def create_container(request):

	# If we're receiving form data, validate and process it
	if request.method == 'GET':
		form = CreateInstForm(request.GET)
		if form.is_valid():

			# Get and process the data from the form into the required format
			data = form.cleaned_data
			container_name = data["container_name"]
			image_name = data["image_name"]
			quantity = data["quantity"]
			is_interactive = data["is_interactive"]
			is_background = data["is_background"]

			# Create and start the new container
			utils.start_container(container_name, image_name, quantity, is_interactive,
				is_background)

			# Redirect back to the home page
			return HttpResponseRedirect('/')

	# Else create a blank form (this hshould never happen)
	else:
		form = CreateInstForm()

	# Render the create_instance html template and send it to the form
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

	# Set variables for template
	context = {}
	context['keys'] = keys
	context['containers'] = status

	return render(request, 'manager/monitor_instances.html', context)

'''
Show detailed container information
'''
def container_details(request):
	if request.method == 'GET':
		if "id" in request.GET:
			# Get detailed information for container
			info = utils.get_info(request.GET['id'])[0]

			# Most useful information
			container_details = {}
			container_details["cpu_shares"] = info["Config"]["CpuShares"]
			container_details["memory"] = info["Config"]["Memory"]
			container_details["memory_swap"] = info["Config"]["MemorySwap"]
			container_details["created_time"] = utils.convert_time(info["Created"])
			container_details["id"] = info["Id"][:12]  		# Use first 12 digits
			container_details["image"] = info["Image"][:12] # Use first 12 digits
			container_details["name"] = info["Name"][1:]	# First char is always a '/'
			container_details["ip"] = info["NetworkSettings"]["IPAddress"]
			container_details["is_running"] = info["State"]["Running"]
			container_details["start_time"] = utils.convert_time(info["State"]["StartedAt"])
			container_details["is_paused"] = info["State"]["Paused"]
			container_details["finish_time"] = utils.convert_time(info["State"]["FinishedAt"])

			return render(request, 'manager/details.html', { 'details': container_details })

	return HttpResponseRedirect('/manager/status/')


'''
Display existing images

TODO: Add ability to create new image from this page
'''
def display_images(request):
	# Get existing images
	images = utils.get_images()
	keys = images[images.keys()[0]].keys()

	return render(request, 'manager/images.html', { 'keys': keys, 'images': images })