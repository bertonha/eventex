# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Subscription(models.Model):
    name = models.CharField(_(u'Nome'), max_length=200)
    cpf = models.CharField(_(u'CPF'), max_length=11, unique=True)
    email = models.EmailField(_(u'E-mail'), blank=True, unique=True)
    phone = models.CharField(_(u'Telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_(u'Criado em'), auto_now_add=True)
    paid = models.BooleanField(_(u'Paga'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'Incrição')
        verbose_name_plural = _(u'Incrições')
