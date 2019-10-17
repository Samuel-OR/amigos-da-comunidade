from django import forms
from dal import autocomplete
from .models import *

class EdicaoForm(forms.ModelForm):
	class Meta:
		model = Edicao
		fields=['nome_edicao','data_inicio','data_fim','local']






