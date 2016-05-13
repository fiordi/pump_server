from django.contrib.auth.models import User
from django.db import models


"""
Customer class (extends User)
"""
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	name = models.TextField(null=True, blank=False, default="Undefined")

	def __unicode__(self):
		return self.name
