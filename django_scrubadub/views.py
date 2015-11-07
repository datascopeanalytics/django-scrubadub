from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView

from rest_framework import viewsets, renderers
from rest_framework.decorators import detail_route

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    # this exposes an endpoint of the api in which you can review a particular
    # document
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def review(self, request, *args, **kwargs):
        document = self.get_object()
        return render_to_response('django_scrubadub/document_review.html', {
            "object": document,
        })
