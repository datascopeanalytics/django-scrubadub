from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from . import views

# this creates the urls using the rest framework's router mechanism
# http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
router = DefaultRouter()
router.register(r'documents', views.DocumentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
