from .models import Location
from django.forms.utils import ErrorList
from django import forms
from dal import autocomplete


class LocationForm(forms.ModelForm):

	class Meta:
		model = Location
		fields = ['name', 'description']

	def clean(self):
		super(LocationForm, self).clean()
		name = self.cleaned_data.get('name')
		
		# Evitar que seja realizada a o cadastro de uma localização mais de uma vez
		if Location.objects.filter(name=name).exists():
			self.add_error('name', 'Já foi cadastrada uma localização com esse nome')


class LocationUpdateForm(forms.ModelForm):

	class Meta:
		model = Location
		fields = ['name', 'description']

	def clean(self):
		super(LocationUpdateForm, self).clean()
		name = self.cleaned_data.get('name')
		