# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from models import SaltStackTask   
class SaltStackTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaltStackTask
        fields = '__all__'
