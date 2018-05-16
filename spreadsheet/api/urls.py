# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function
from django.conf.urls import include, url

app_name = 'api'

urls = [
    url(r'^accounts/', include('accounts.api.urls')),
    url(r'^historygraph/', include('historygraph_backend.api.urls')),
]

urlpatterns = [url(r'^', include(urls))]
