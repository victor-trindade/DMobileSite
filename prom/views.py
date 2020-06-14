from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Colaborador

# Create your views here.

class ColaboratorListView(ListView):
    model = Colaborador
