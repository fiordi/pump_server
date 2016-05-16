from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel

#recupero le proprieta' legate alla strategia
import pump_site.sales_strategy
properties = pump_site.sales_strategy


"""
SalePricingStrategy class (Interface)
"""
class SalePrincingStrategy(SingletonModel):

	class Meta:
		abstract = True

"""
MorePacketsStrategy class
"""
class MorePacketsStrategy(SingletonModel):

	def getAmount(self, Sale):
		packets = Sale.packets.all()

		if len(packets) >= properties.morePacketsStrategy_properties__min_number_of_packets:
			amount = Sale.amount*(100-properties.morePacketsStrategy_properties__percentage_of_discount)/100
		else:
			amount = Sale.amount
		return amount


