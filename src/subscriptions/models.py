# -*- coding: utf-8 -*-
from django.db import models


class Subscription(models.Model):
    nome = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = u'Incrição'
        verbose_name_plural = u'Incrições'
