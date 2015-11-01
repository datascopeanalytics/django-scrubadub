from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.DocumentListView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.DocumentView.as_view()),
]
