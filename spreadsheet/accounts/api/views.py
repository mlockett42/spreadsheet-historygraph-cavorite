# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import PublicKeySerialiser, UserSerializer
from accounts.models import User


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

class SetPublicKeyView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.public_key != '':
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail' : 'Public key already set.'})

        serializer = PublicKeySerialiser(data=request.data)
        if serializer.is_valid():
            user.public_key = serializer.validated_data['public_key']
            user.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'detail' : 'Invalid data.'})

class UserList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, format=None):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

