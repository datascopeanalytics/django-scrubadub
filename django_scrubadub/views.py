from django.shortcuts import render_to_response
from django.views.generic import DetailView

from rest_framework import viewsets, renderers

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentReviewView(DetailView):
    model = Document
    template_name = 'django_scrubadub/document_review.html'
