# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function

from django.shortcuts import render
import os
from django.http import Http404
from django.conf import settings
from django.http import HttpResponse


def development_storage_view(request, file_path=None):
    print('settings.STORAGE_FILES_ROOT=', settings.STORAGE_FILES_ROOT)
    full_path = os.path.join(settings.STORAGE_FILES_ROOT, file_path)
    if os.path.isfile(full_path) is True:
        test_file = open(full_path, 'rb')
        return HttpResponse(content=test_file)
    if os.path.isdir(full_path) is True:
        file_names = [f for f in os.listdir(full_path)]
        result = """<?xml version="1.0" encoding="UTF-8"?><ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">"""
        result += ''.join(['<Contents><Key>{0}</Key></Contents>'.format(filename) for filename in file_names])
        result += "</ListBucketResult>"
        print('result=', result)

        return HttpResponse(content=result, content_type='text/xml')
        
    raise Http404("File does not exist")

