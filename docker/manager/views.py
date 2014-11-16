import json
import utils
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import CreateInstForm, CreateContainerForm

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
Create new container from image
'''
def create_container(request):
	if request.method == 'GET':
		form = CreateContainerForm(request.GET)
		if form.is_valid():
			# Call script to create new container from image
			return HttpResponseRedirect('/manage/containers/')
	else:
		form = CreateContainerForm()

	return render(request, 'manager/create_container.html', { 'form': form })

'''
Display existing instances

TODO: Add filters
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
		if 'id' in request.GET:
			# Get detailed information for container
			info = utils.get_info(request.GET['id'])[0]

			# Most useful information
			container_details = {}
			container_details['cpu_shares'] = info['Config']['CpuShares']
			container_details['memory'] = info['Config']['Memory']
			container_details['memory_swap'] = info['Config']['MemorySwap']
			container_details['created_time'] = utils.convert_time(info['Created'])
			container_details['id'] = info['Id'][:12]  		# Use first 12 digits
			container_details['image'] = info['Image'][:12] # Use first 12 digits
			container_details['name'] = info['Name'][1:]	# First char is always a '/'
			container_details['ip'] = info['NetworkSettings']['IPAddress']
			container_details['is_running'] = info['State']['Running']
			container_details['start_time'] = utils.convert_time(info['State']['StartedAt'])
			container_details['is_paused'] = info['State']['Paused']
			container_details['finish_time'] = utils.convert_time(info['State']['FinishedAt'])

			return render(request, 'manager/container_details.html', { 'details': container_details })

	return HttpResponseRedirect('/manager/containers/')

'''
Display existing images

TODO: Add ability to create new image from this page
'''
def display_images(request):
	# Get existing images
	images = utils.get_images()
	keys = images[images.keys()[0]].keys()

	return render(request, 'manager/images.html', { 'keys': keys, 'images': images })

'''
Show detailed image information
'''
def image_details(request):
	if request.method == 'GET':
		if 'tag' in request.GET and 'id' in request.GET:
			form = CreateContainerForm()
			return render(request, 'manager/image_details.html', { 'tag': request.GET['tag'], 'id': request.GET['id'], 'form':form })

	return HttpResponseRedirect('/manager/images/')