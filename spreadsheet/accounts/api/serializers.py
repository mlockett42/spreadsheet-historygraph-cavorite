# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from rest_framework import serializers
import copy
from ..models import User


class PublicKeySerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('public_key', )

