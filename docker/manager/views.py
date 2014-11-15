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
	# Run script to get existing instances and their stats
	return render(request, 'manager/monitor_instances.html')