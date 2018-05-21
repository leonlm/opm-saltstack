# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from views import *


router = routers.DefaultRouter()
router.register(r'task', SaltStackTaskViewSet, base_name='saltstack_task')


urlpatterns = [
    url(r'', include(router.urls)),
]
