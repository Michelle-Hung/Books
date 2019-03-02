from django import forms
from django.forms import ModelForm, Textarea,DateInput
from .models import Rating,UserProfile


class RatingForm( ModelForm ):
	class Meta:
		model = Rating
		#fields = {'user', 'rating', 'comment'}
		fields = {'rating', 'comment'}
		widgets = {'comment': Textarea(attrs={'cols': 63, 'rows': 5}), }
	def __init__(self, *args, **kwargs):
		super(RatingForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['comment','rating']

class ProfileForm( ModelForm ):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields.keyOrder = ['gender', 'birth_day', 'location', 'bio', 'image']
	class Meta:
		model=UserProfile
		fields = {'gender', 'birth_day', 'location', 'bio', 'image'}
		widgets = {'bio' : Textarea(attrs={'cols':68, 'rows':5}),
					'birth_day' : DateInput(attrs={'type':'date'})}

	


