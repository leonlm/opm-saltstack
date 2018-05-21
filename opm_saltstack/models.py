# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class SaltStackTask(models.Model):
    """
    Task Log
    """
    task_name = models.TextField(default=None, null=True, blank=True)
    params = models.TextField(default=None, null=True, blank=True)
    status = models.CharField(max_length=20, default=0, null=True, blank=True)
    result = models.TextField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'saltstack_task'
        verbose_name = 'saltstack_task'
        verbose_name_plural = 'saltstack_task'