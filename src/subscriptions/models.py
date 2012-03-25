# -*- coding: utf-8 -*-
from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = u'Incrição'
        verbose_name_plural = u'Incrições'
