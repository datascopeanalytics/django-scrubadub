from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Document


class DocumentListView(ListView):
    model = Document


class DocumentView(DetailView):
    model = Document
