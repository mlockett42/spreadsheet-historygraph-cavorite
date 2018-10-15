# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
#from .permissions import IsOwner
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin
import copy
from django.http import Http404
from .serializers import HistoryGraphSerializer, HistoryGraphGetSerializer
import json
import hashlib
import os
from django.conf import settings


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class HistoryGraphView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, format=None):
        serializer = HistoryGraphSerializer(data=request.data, many=True)
        if serializer.is_valid():
            message_media_storage.save('private/{0}/{1}'.format(serializer.validated_data['receipient'],
                                       hashlib.sha256(serializer.validated_data['content']).hexdigest()),
                                       serializer.validated_data['content'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryGraphListView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, recipient, format=None):
        if recipient == 'public':
            full_path = os.path.join(settings.STORAGE_FILES_ROOT, 'public')
            file_names = [f for f in os.listdir(full_path)]

            return Response(file_names)
        return Response([])
