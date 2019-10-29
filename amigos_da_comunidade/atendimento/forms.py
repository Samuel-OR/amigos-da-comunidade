from .models import *
from amigos_da_comunidade.edicao.models import *
from django import forms
from dal import autocomplete
from django.contrib.auth import get_user_model
from dal import autocomplete
from .models import *

class SetorForm(forms.ModelForm):
    
	class Meta:
		model = Setor
		fields = ['nome_setor','membros']

		widgets = {
            'membros': autocomplete.ModelSelect2Multiple(url='atendimento:membros_autocomplete'),

        }
class FichaAtendimentoForm(forms.ModelForm):
    
	class Meta:
		model = FichaAtendimento

		fields = ['nome_paciente','idade','endereco']



class TriagemForm(forms.ModelForm):
    
	class Meta:
		model = Triagem
		fields = ['membros']

		widgets = {
            'membros': autocomplete.ModelSelect2Multiple(url='atendimento:membros_autocomplete'),

        }