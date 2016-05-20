from django.contrib.auth.models import User
from django.db import models

"""
Customer class (Interface)
"""
class Customer(models.Model):
	id = models.AutoField(primary_key=True)

	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

	name = models.TextField(null=True, blank=False, default="Undefined")

	def __unicode__(self):
		return self.name

"""
StudentCustomer class (extends Customer)
"""
class StudentCustomer(Customer):
	pass

"""
SeniorCustomer class (extends Customer)
"""
class SeniorCustomer(Customer):
	pass

