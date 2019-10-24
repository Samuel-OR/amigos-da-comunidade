from django.urls import path
from .views import *

app_name = 'ensino' 
 
urlpatterns = [
	path('setor/adicionar/', SetorCreate.as_view(), name='setor_create',),
	path('setor/listar/', SetorList.as_view(), name='setor_list',),
	path('setor/editar/<int:pk>/', SetorUpdate.as_view(), name='setor_update',),
	path('setor/deletar/<int:pk>/', setor_delete, name='setor_delete',),

	# path('professor/adicionar/', ProfessorCreate.as_view(), name='professor_create',),
	# path('professor/listar/', ProfessorList.as_view(), name='professor_list',),
	# path('professor/editar/<int:pk>/', ProfessorUpdate.as_view(), name='professor_update',),
	# path('professor/deletar/<int:pk>/', professor_delete, name='professor_delete',),

	path('membros-autocomplete/',MembrosAutocomplete.as_view(), name='membros_autocomplete',),
	# path('instituicao-autocomplete/',InstituicaoAutocomplete.as_view(), name='instituicao_autocomplete',),

	# path('aluno/adicionar/',AlunoCreate.as_view(), name='aluno_create',),
	# path('aluno/listar/', AlunoList.as_view(), name='aluno_list',),
	# path('aluno/editar/<int:pk>/', AlunoUpdate.as_view(), name='aluno_update',),
	# path('aluno/deletar/<int:pk>/', aluno_delete, name='aluno_delete',), 
	
]