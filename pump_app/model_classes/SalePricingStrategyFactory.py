from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel


"""
SalePricingStrategyFactory class (Singleton)
"""
class PacketCatalog(SingletonModel):
	id = models.AutoField(primary_key=True)

	name = models.TextField(null=True, blank=False, default="Sale Pricing Strategy Factory")

	def __unicode__(self):
		return self.name