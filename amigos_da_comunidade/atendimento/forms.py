from django import forms
from dal import autocomplete
from .models import *
from chainforeducation.nucleo.models import Nucleo

class InstituicaoForm(forms.ModelForm):
	    class Meta:
   	 		model = InstituicaoEnsino
   	 		fields=['nome']


class ProfessorForm(forms.ModelForm):
    
	nucleo = forms.ModelChoiceField(
		required=True,
		queryset = Nucleo.objects.all(),
		label = "Núcleo",
		widget = autocomplete.ModelSelect2(url='ensino:nucleo_autocomplete',attrs={'data-width': '100%'})
	)


	instituicao = forms.ModelChoiceField(
		required=True,
		queryset = InstituicaoEnsino.objects.all(),
		label = "Instituição de Ensino",
		widget = autocomplete.ModelSelect2(url='ensino:instituicao_autocomplete')
	)

	class Meta:
		model = Professor
		fields = ['nome','nucleo','instituicao']


class AlunoForm(forms.ModelForm):
	    class Meta:
   	 		model = Aluno
   	 		fields=['nome']
