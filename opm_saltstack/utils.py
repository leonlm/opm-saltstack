# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from serializers import *


def get_serializer_class():
    return SaltStackTaskSerializer

def get_model():
    return SaltStackTask

def save(method, request_data, **kwargs):
    if method == "create":
        serializer = SaltStackTaskSerializer(data=request_data)
    else:
        if kwargs.get('instance', False):
            instance = kwargs.pop('instance')
        else:
            instance = get_model().objects.get(**kwargs)
        serializer = SaltStackTaskSerializer(instance, data=request_data, partial=True)

    if serializer.is_valid():
        instance_save = serializer.save()
        retdict = {'status': 1, 'data': serializer.data, "msg": "SUCCESS", "instance": instance_save}
    else:
        retdict = {"status": 0, "data": "", "msg": "ERROR,"+json.dumps(serializer.errors)}
    return retdict

