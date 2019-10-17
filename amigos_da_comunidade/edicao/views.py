from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.http import HttpResponseRedirect, JsonResponse
from dal import autocomplete
from .models import *
from .forms import *

class EdicaoCreate(CreateView):
	model = Edicao
	template_name = 'edicao/add.html'
	form_class = EdicaoForm

class EdicaoList(ListView):
	model = Edicao
	template_name = 'edicao/list.html'
	http_method_names = ['get']
	# muda o nome do product_list gerado por padrao pela classe
	#context_object_name = 'ob'
	paginate_by = 15

	def get_queryset(self):
		self.queryset = super(EdicaoList, self).get_queryset()
		if self.request.GET.get('search_box', False) :
			self.queryset = self.queryset.filter(nome_edicao__contains = self.request.GET['search_box'])
		return self.queryset

	def get_context_data(self, **kwargs):
		_super = super(EdicaoList, self)
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

class EdicaoUpdate(UpdateView):
	model = Edicao
	template_name = 'edicao/add.html'
	form_class = EdicaoForm


def edicao_delete(request, pk):
	edicao = get_object_or_404(Edicao, pk=pk)
	edicao.delete()
	return JsonResponse({'msg': "Edição excluida com sucesso!", 'code': "1"})


