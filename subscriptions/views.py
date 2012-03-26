# encoding: utf-8

from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from subscriptions.models import Subscription
from subscriptions.forms import SubscritionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    form = SubscritionForm()

    context = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', context)


def create(request):
    form = SubscritionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscriptions/new.html', context)

    subscription = form.save()
    send_mail(
        subject=u'Cadastro com Sucesso',
        message=u'Obrigado %s pela sua inscrição' % subscription.name,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[subscription.email]
    )
    return HttpResponseRedirect(
        reverse('subscriptions:success', args=[subscription.pk]))


def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request,{'subscription': subscription})
    return render_to_response('subscriptions/success.html', context)
    
