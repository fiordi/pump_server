from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

"""
Customer class (Interface)
"""
class Customer(models.Model):
	id = models.AutoField(primary_key=True)

	user = models.OneToOneField(User, null=True, blank=False, on_delete=models.CASCADE)

	name = models.TextField(null=True, blank=False, default="Undefined")

	type = models.TextField(null=True, blank=False, default="Undefined")

	def __unicode__(self):
		return self.name

"""
StudentCustomer class (extends Customer)
"""
class StudentCustomer(Customer):

	@receiver(pre_save)
	def pre_save_handler(sender, instance, *args, **kwargs):
		instance.type = instance.__class__.__name__

"""
SeniorCustomer class (extends Customer)
"""
class SeniorCustomer(Customer):

	@receiver(pre_save)
	def pre_save_handler(sender, instance, *args, **kwargs):
		instance.type = instance.__class__.__name__

