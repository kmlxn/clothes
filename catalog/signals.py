from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.core.exceptions import PermissionDenied
from .models import Option


@receiver(pre_delete, sender=Option)
def delete_option(sender, **kwargs):
    raise PermissionDenied
