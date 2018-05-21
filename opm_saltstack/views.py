# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from django.http.response import JsonResponse
from utils import (
    get_serializer_class,
    get_model,
    save
)


class SaltStackTaskViewSet(viewsets.ModelViewSet):
    serializer_class = get_serializer_class()
    queryset = get_model().objects.all()
