from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel


"""
SalePricingStrategy class (Interface)
"""
class SalePrincingStrategy(SingletonModel):

	class Meta:
		abstract = True