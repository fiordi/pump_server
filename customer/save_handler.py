from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver




from customer.model_classes.Customer import Customer, StudentCustomer, SeniorCustomer
"""
It automatically associates the class_name to type field on each save()
"""
@receiver(pre_save, sender=StudentCustomer)
@receiver(pre_save, sender=SeniorCustomer)
@receiver(post_save, sender=StudentCustomer)
@receiver(post_save, sender=SeniorCustomer)
def set_customer_type(sender, instance, *args, **kwargs):
    sender.type = instance.__class__.__name__
    instance.type = instance.__class__.__name__