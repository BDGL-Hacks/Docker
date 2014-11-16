import utils
from django import forms
import utils

''' Manages the creation of a container from a previously saved image '''
class CreateInstForm(forms.Form):

	# Offer a list of images you have stored as choices to run
	image_choices = []
	stored_images_json = utils.get_images()
	for i in range(len(stored_images_json)):
		choice_object = stored_images_json[i+1]
		choice_string = choice_object["REPOSITORY"] + " - " + choice_object["TAG"]
		choice_tuple = (choice_object["REPOSITORY"], choice_string)
		image_choices.append(choice_tuple)

	# Form fields - Raw Data
	container_name = forms.CharField(label="Container Name", max_length=100)
	image_name = forms.ChoiceField(choices=image_choices)
	quantity = forms.IntegerField(min_value=1, max_value=99)
	is_interactive = forms.BooleanField(required=False)
	is_background = forms.BooleanField(required=False)

class CreateImageForm(forms.Form):
	image_tag = forms.CharField(label="Image Name", max_length=50)
	image_base = forms.ChoiceField(choices=utils.image_base_choices())

class CreateContainerForm(forms.Form):
	container_name = forms.CharField(label="Container Name", max_length=50)
	image_id = forms.ChoiceField(choices=utils.image_id_choices())
