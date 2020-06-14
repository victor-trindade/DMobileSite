from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Doc


# Create your DOC views here.
class DocListView(ListView):
    model = Doc


class DocDatailView(DetailView):
    model = Doc
