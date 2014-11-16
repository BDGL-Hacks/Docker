import json
import utils
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from forms import CreateImageForm, CreateContainerForm

'''
Homepage
'''
def home(request):
	return render(request, 'manager/main_panel.html')

'''
Launch new image
'''
def create_image(request):
	# If we're receiving form data, validate and process it
	if request.method == 'GET':
		form = CreateImageForm(request.GET)
		if form.is_valid():

			# Create and start the new container
			utils.start_container(form.cleaned_data["container_name"],
				form.cleaned_data["image_name"])

			# Redirect back to the home page
			return HttpResponseRedirect('/')

	# Else create a blank form (this hshould never happen)
	else:
		form = CreateImageForm()

	# Render the create_instance html template and send it to the form
	return render(request, 'manager/create_image.html', { 'form': form })

'''
Create new container from template
'''
def create_container(request):
	if request.method == 'GET':
		form = CreateContainerForm(request.GET)
		if form.is_valid():
			# Call script to create new image
			return HttpResponseRedirect('/manager/containers/')
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
			if 'save' in request.GET:
				# Call function to convert existing container to image
				utils.branch_container(request.GET.get('id'), request.GET.get('id')+"branch")
				return HttpResponseRedirect('/manager/images/')
			elif 'start' in request.GET:
				# Call function to start a stopped or paused container
				utils.resume_container(request.GET.get('id'))
				pass
			elif 'pause' in request.GET:
				# Call function to pause a started container
				utils.stop_container(request.GET.get('id'))
				pass
			elif 'stop' in request.GET:
				# Call function to stop a started or paused container
				utils.remove_container(request.GET.get('id'))
				pass

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

			return render_to_response('manager/container_details.html', { 'details': container_details, 'id': request.GET['id'] })

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

'''
Delete image in the get request
'''
def delete_image(request):
	if request.method == 'GET':
		if 'id' in request.GET:
			# Call function to delete this image id
			pass

	return HttpResponseRedirect('/manager/images/')
