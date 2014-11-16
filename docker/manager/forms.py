import utils
from django import forms

''' Manages the creation of a container from a previously saved image '''
class CreateInstForm(forms.Form):

	''' TODO: These should choose between a list of images you have saved '''
	# Images the user has previously saved
	image_choices = (
		('Ubuntu', 'Ubuntu'),
		('NodeJS', 'NodeJS'),
		('MySQL', 'MYSQL'),
		('MongoDB', 'MongoDB'),
	)

	''' TODO: Actually populate these with running docker containers '''
	# Currently running containers
	running_containers = (
		(1, 'base_ubuntu'),
		(2, 'fake_container')
	)

	''' 
		TODO: For links, host_mounts, external_mounts, and custom_mounts:
		Have a button that reveals (and a button that deletes) more CharFields.
		This allows the user to specify as many links or mounts as they want.
		ALTERNATIVELY: Have a for loop that gets all the running containers and
		have the user checkbox which ones they want to link / mount to.
		The code that sets the corresponding variables down here need to change
		accordingly.
	'''
	# Form fields - Raw Data
	container_name = forms.CharField(label="Container Name", max_length=100)
	image_name = forms.ChoiceField(choices=image_choices)
	quantity = forms.IntegerField(min_value=1, max_value=99)
	links = forms.CharField(label="Containers to Link to:", max_length=100)
	host_mount_local_path = forms.CharField(label="Mount from Host: Local path", max_length=100)
	host_mount_dest_path = forms.CharField(label="Destination Path", max_length=100)
	external_mounts = forms.CharField(label="Mount from another container - Container Name:", max_length=100)
	custom_mounts = forms.CharField(label="Create and Mount a new directory - Dir Path:", max_length=100)
	is_interactive = forms.BooleanField(required=False)
	is_background = forms.BooleanField(required=False)

class CreateImageForm(forms.Form):
	image_tag = forms.CharField(label="Image Name", max_length=50)
	image_base = forms.ChoiceField(choices=utils.image_base_choices())

class CreateContainerForm(forms.Form):
	container_name = forms.CharField(label="Container Name", max_length=50)
	image_id = forms.ChoiceField(choices=utils.image_id_choices())
