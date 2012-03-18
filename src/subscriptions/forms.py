from django.forms import Form
from subscriptions.models import Subscription


class SubscritionForm(Form):
    model = Subscription()

    class Meta:
        pass
