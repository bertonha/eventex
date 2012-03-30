# -*- coding: utf-8 -*-

import datetime

from django.conf.urls import patterns, url
from django.contrib import admin
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

from subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at',
        'subscribed_today', 'paid',)
    list_filter = ['created_at', 'paid']

    actions = ['mark_as_paid', ]

    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'created_at')

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        message = ungettext(
            u'%(count)d inscrição foi marcada como paga.',
            u'%(count)d inscrições foram marcadas como pagas.',
            count
        ) % {'count': count}

        self.message_user(request, message)
    mark_as_paid.short_description = _(u'Marcar como pagas')

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()
    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True

    def export_subscriptions(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions]

        response = HttpResponse('\r\n'.join(rows))
        response.mimetype = "text/csv"
        response['Content-Disposition'] = 'attachment; filename=incrições.csv'

        return response

    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_urls = patterns('',
            url(r'exportar-inscricoes/$',
                self.admin_site.admin_view(self.export_subscriptions),
                name='export_subscriptions')
        )

        return extra_urls + original_urls

admin.site.register(Subscription, SubscriptionAdmin)
