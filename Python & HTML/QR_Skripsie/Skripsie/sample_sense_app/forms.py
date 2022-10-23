from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Client, Feed_sample, Residue_sample


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AddFeedSampleForm(ModelForm):
	class Meta:
		model = Feed_sample
		fields = ("sample_id", "sample_date", "sample_name", "client", "required_tests")
		labels = {
		
		}
		widgets = {

		}

class AddResidueSampleForm(ModelForm):
	class Meta:
		model = Residue_sample
		fields = ("sample_id", "sample_date", "sample_name", "client", "required_tests")
		labels = {
		
		}
		widgets = {

		}

class AddClientForm(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
		labels = {
		
		}
		widgets = {

		}

class UpdateFeedSampleForm(ModelForm):
	class Meta:
		model = Feed_sample
		fields = '__all__' 
		labels = {
		
		}
		widgets = {

		}

class UpdateResidueSampleForm(ModelForm):
	class Meta:
		model = Residue_sample
		fields = '__all__'
		labels = {
		
		}
		widgets = {

		}		