from rest_framework import serializers

from .models import Document, FilthType, Filth


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
