from django.contrib.auth.models import User
from pump_app.model_classes.Subscription import Subscription
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

"""
Customer class (Abstract class)
"""
class Customer(models.Model):
	id = models.AutoField(primary_key=True)

	user = models.OneToOneField(User, null=True, blank=False, to_field='username', on_delete=models.CASCADE)

	name = models.CharField(max_length=30,null=True, blank=False, default="Name")

	surname = models.CharField(max_length=30,null=True, blank=False, default="Surname")

	email = models.EmailField(max_length=254,null=True, blank=False, default="Email")

	phone = PhoneNumberField(blank=True)

	subscription = models.ForeignKey(Subscription, null=True, blank=True, on_delete=models.SET_NULL, related_name='customer')

	type = models.TextField(null=True, blank=False, default='Type of user')

	def __unicode__(self):
		return self.name






"""
StudentCustomer class (extends Customer)
"""
class StudentCustomer(Customer):

	"""
	It automatically associates the class_name to type field on each save()
	"""
	@receiver(pre_save)
	def pre_save_handler(sender, instance, *args, **kwargs):
		instance.type = instance.__class__.__name__





"""
SeniorCustomer class (extends Customer)
"""
class SeniorCustomer(Customer):

	"""
	It automatically associates the class_name to type field on each save()
	"""
	@receiver(pre_save)
	def pre_save_handler(sender, instance, *args, **kwargs):
		instance.type = instance.__class__.__name__

