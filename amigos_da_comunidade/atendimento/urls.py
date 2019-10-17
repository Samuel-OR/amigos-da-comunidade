from django.urls import path
from .views import *

app_name = 'ensino' 
 
urlpatterns = [
	# path('adicionar/', InstituicaoCreate.as_view(), name='instituicao_create',),
	# path('listar/', InstituicaoList.as_view(), name='instituicao_list',),
	# path('editar/<int:pk>/', InstituicaoUpdate.as_view(), name='instituicao_update',),
	# path('deletar/<int:pk>/', instituicao_delete, name='instituicao_delete',),

	# path('professor/adicionar/', ProfessorCreate.as_view(), name='professor_create',),
	# path('professor/listar/', ProfessorList.as_view(), name='professor_list',),
	# path('professor/editar/<int:pk>/', ProfessorUpdate.as_view(), name='professor_update',),
	# path('professor/deletar/<int:pk>/', professor_delete, name='professor_delete',),

	# path('nucelo-autocomplete/',NucleoAutocomplete.as_view(), name='nucleo_autocomplete',),
	# path('instituicao-autocomplete/',InstituicaoAutocomplete.as_view(), name='instituicao_autocomplete',),

	# path('aluno/adicionar/',AlunoCreate.as_view(), name='aluno_create',),
	# path('aluno/listar/', AlunoList.as_view(), name='aluno_list',),
	# path('aluno/editar/<int:pk>/', AlunoUpdate.as_view(), name='aluno_update',),
	# path('aluno/deletar/<int:pk>/', aluno_delete, name='aluno_delete',), 
	
]