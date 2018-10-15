# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.HistoryGraphView.as_view(), name='historygraph-post'),
    url(r'^list/(?P<recipient>[a-zA-Z0-9]*)/$', views.HistoryGraphListView.as_view(), name='historygraph-list'),
    url(r'^load/$', views.HistoryGraphLoadView.as_view(), name='historygraph-lost'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
