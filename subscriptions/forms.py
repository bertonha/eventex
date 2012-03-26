from django import forms
from subscriptions.models import Subscription


class SubscritionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')
