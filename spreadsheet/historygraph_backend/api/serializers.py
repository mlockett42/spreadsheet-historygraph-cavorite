# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from rest_framework import serializers
import json
import base64


class HistoryGraphSerializer(serializers.Serializer):
    content = serializers.CharField()

    def validate_content(self, value):
        content = json.decode(value)
        if len(content) == 2:
            message = base64.b64decode(content['message'])
            signature = base64.b64decode(content['signature'])

            public_key = b64decode(self.request.user.public_key)
            public_key = rsa.PublicKey.load_pkcs1(public_key)

            if not rsa.verify(message, signature, public_key):
                raise serializers.ValidationError("User key does not match")
            return value

        raise serializers.ValidationError("Incorrectly formatted request")

class HistoryGraphGetSerializer(serializers.Serializer):
    receipient = serializers.CharField()
