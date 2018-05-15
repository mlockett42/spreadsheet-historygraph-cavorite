# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from django.conf.urls import url
from . import views

app_name = 'development_storage'


urlpatterns = [
    url(r'^(?P<file_path>[\w\-\/]+)$', views.development_storage_view, name='stored_file'),
]


