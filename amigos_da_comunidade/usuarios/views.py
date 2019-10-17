from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, TemplateView, FormView
from dal import autocomplete
from .models import *
from .forms import *



