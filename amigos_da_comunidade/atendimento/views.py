from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db import IntegrityError, transaction
from django.contrib import messages
from dal import autocomplete
from django.contrib.auth.decorators import login_required
from .forms import*
from datetime import datetime , date
from django.views.generic import View
from amigos_da_comunidade.accounts.models import *


class SetorCreate(CreateView):
	model = Setor
	template_name = 'setor/add.html'
	form_class = SetorForm

	def post(self, request, *args, **kwargs):
		self.object = None
		
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):
		
		setor = form.save()

		# setor.edicao = Edicao.objects.filter(data_inicio__lte=datetime.now() , data_fim__gte=datetime.now() ).first()
		setor.edicao = Edicao.objects.filter(ativo=True).first()
		setor.save()

		return HttpResponseRedirect(reverse('atendimento:setor_list'))

class SetorUpdate(UpdateView):
	model = Setor
	template_name = 'setor/add.html'
	form_class = SetorForm

class SetorList(ListView):
	model = Setor
	template_name = 'setor/list.html'
	http_method_names = ['get']
	paginate_by = 15

	def get_queryset(self):
		self.queryset = super(SetorList, self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset = self.queryset.filter(nome_setor__contains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(SetorList, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
			startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
			endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
						if n > 0 and n <= num_pages]

		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
			})
		return context

def setor_delete(request, pk):
	setor = get_object_or_404(Setor, pk=pk)
	setor.delete()
	return JsonResponse({'msg': "Setor excluido com sucesso!", 'code': "1"})

<<<<<<< HEAD

class TriagemCreate(CreateView):
	model = Triagem
	template_name = 'triagem/add.html'
	form_class = TriagemForm

	def post(self, request, *args, **kwargs):
		self.object = None
		
		form = self.form_class(self.request.POST)

		if form.is_valid():
			return self.form_valid(form, request)

		else:
			return self.form_invalid(form, request)

	def form_valid(self, form , request):
		
		setor = form.save()

		# setor.edicao = Edicao.objects.filter(data_inicio__lte=datetime.now() , data_fim__gte=datetime.now() ).first()
		setor.edicao = Edicao.objects.filter(ativo=True).first()
		setor.save()

		return HttpResponseRedirect(reverse('atendimento:triagem_list'))



class TriagemList(ListView):
	model = Triagem
	template_name = 'triagem/list.html'
	http_method_names = ['get']
	paginate_by = 15

	def get_queryset(self):
		self.queryset = super(TriagemList, self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset = self.queryset.filter(membros__name__contains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(TriagemList, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
			startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
			endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
						if n > 0 and n <= num_pages]

		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
			})
		return context


class TriagemUpdate(UpdateView):
	model = Triagem
	template_name = 'triagem/add.html'
	form_class = TriagemForm


def triagem_delete(request, pk):
	triagem = get_object_or_404(Triagem, pk=pk)
	triagem.delete()
	return JsonResponse({'msg': "triagem excluida com sucesso!", 'code': "1"})

=======
>>>>>>> 3c0e8d8aa832a32e3ebf3f477d8c56b4825fd35c
class MembrosAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		qs = User.objects.all()

		if self.q:
			qs = qs.filter(Q(name__icontains=self.q))

		return qs

#-------------

class FichaAtendimentoCreate(CreateView):
	model = FichaAtendimento
	template_name = 'ficha_atendimento/add.html'
	form_class = FichaAtendimentoForm

class SetorUpdate(UpdateView):
	model = FichaAtendimento
	template_name = 'ficha_atendimento/add.html'
	form_class = FichaAtendimentoForm

class SetorList(ListView):
	model = FichaAtendimento
	template_name = 'ficha_atendimento/list.html'
	http_method_names = ['get']
	paginate_by = 15

	def get_queryset(self):
		self.queryset = super(SetorList, self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset = self.queryset.filter(nome_setor__contains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(SetorList, self)
		context = _super.get_context_data(**kwargs)
		adjacent_pages = 3
		page_number = context['page_obj'].number
		num_pages = context['paginator'].num_pages
		startPage = max(page_number - adjacent_pages, 1)
		if startPage <= 5:
			startPage = 1
		endPage = page_number + adjacent_pages + 1
		if endPage >= num_pages - 1:
			endPage = num_pages + 1
		page_numbers = [n for n in range(startPage, endPage) \
						if n > 0 and n <= num_pages]

		context.update({
			'page_numbers': page_numbers,
			'show_first': 1 not in page_numbers,
			'show_last': num_pages not in page_numbers,
			})
		return context

def setor_delete(request, pk):
	fichaAtendimento = get_object_or_404(Setor, pk=pk)
	fichaAtendimento.delete()
	return JsonResponse({'msg': "Ficha de atendiemnto excluida com sucesso!", 'code': "1"})