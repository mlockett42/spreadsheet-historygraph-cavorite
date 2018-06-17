# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.UserList.as_view(), name='user-list'),
    url(r'^setpublickey/$', views.SetPublicKeyView.as_view(), name='set-public-key'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

