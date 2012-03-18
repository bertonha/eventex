from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

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
    return HttpResponseRedirect(
        reverse('subscriptions:success', args=[subscription.pk]))
