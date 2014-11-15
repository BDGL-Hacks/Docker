from django import forms

class CreateInstForm(forms.Form):
	image_choices = (
		(1, 'Django'),
		(2, 'NodeJS'),
		(3, 'MySQL'),
		(4, 'MongoDB'),
	)

	name = forms.CharField(label="Container Name", max_length=100)
	quantity = forms.IntegerField()
	image = forms.ChoiceField(choices=image_choices)