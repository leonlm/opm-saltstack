# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from serializers import *
from django.conf import settings


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


class SaltStackApi(object):
    def __init__(self, type):
        self.saltapi_url = settings.SALTSTACK['URL']
        self.username = settings.SALTSTACK['USERNAME']
        self.password = settings.SALTSTACK['PASSWORD']
        self.eauth = settings.SALTSTACK['EAUTH']
        self.type = type
        self.token = self._get_token()

    def _get_token(self):
        url = self.saltapi_url + "/login"
        headers = {'Accept':'application/json'}
        params = {
            'username': self.username,
            'password': self.password,
            'eauth': self.eauth
        }
        response = self._salt_api(url, headers, params)
        return response['token']

    def _salt_api(self, url, headers, data, verify=False, timeout=10):
        response = requests.post(url, headers=headers, data=data, verify=verify, timeout=timeout)
        response = json.loads(response.text)
        return response['return'][0]

    def build(self):
        if self.type == "async":
            self._async_run()
        elif self.type == "cmd":
            self._cmd_run()
        else:
            pass
            
    def _cmd_run(self, tgt='*', expr_form='glob', arg='uptime', timeout=10, **kwargs):
        url = self.saltapi_url
        headers = {'Accept':'application/json', 'X-Auth-Token':self.token}
        params = {
            'client':'local',
            'tgt': tgt,
            'expr_form':expr_form,
            'fun': 'cmd.run',
            'arg':arg
        }

        return self._salt_api(url, headers, params)

    def _async_run(self):
        return True