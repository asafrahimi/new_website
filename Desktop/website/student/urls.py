from django.conf.urls import include, url
from django.urls import path
from django.http import HttpResponse
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index_student, name='index_student'),
]
