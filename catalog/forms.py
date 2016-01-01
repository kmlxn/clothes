from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['client_name', 'client_email',
            'client_company', 'client_phone', 'order_text']
        labels = {
            'client_name': _('Name'),
            'client_email': _('Email'),
            'client_company': _('Company'),
            'client_phone': _('Phone'),
            'order_text': _('Order Text'),
        }
