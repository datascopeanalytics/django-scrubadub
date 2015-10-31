from django.contrib import admin

from .models import Document, FilthType, Filth


admin.site.register(Document)
admin.site.register(FilthType)
admin.site.register(Filth)
