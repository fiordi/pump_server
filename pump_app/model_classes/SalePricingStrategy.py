from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel
from decimal import *

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

		applied_strategy = {}
		if len(packets) >= properties.morePacketsStrategy_properties__min_number_of_packets:
			amount = Sale.amount*(100-properties.morePacketsStrategy_properties__percentage_of_discount)/100
			applied_strategy[self.__class__.__name__] = Sale.amount - amount
		else:
			amount = Sale.amount
			applied_strategy[self.__class__.__name__] = None
		return [applied_strategy, amount]


"""
StudentCustomerStrategy class
"""
class StudentCustomerStrategy(SingletonModel):

	def getAmount(self, Sale):
		from pump_app.model_classes.Customer import StudentCustomer

		applied_strategy = {}

		try:
			studentcustomer = StudentCustomer.objects.get(pk=Sale.user.pk)
		except:
			studentcustomer = None

		if studentcustomer:
			amount = Decimal(Sale.amount*(100-properties.studentCustomerStrategy_properties__percentage_of_discount)/100)
			applied_strategy[self.__class__.__name__] = Sale.amount - amount
		else:
			amount = Sale.amount
			applied_strategy[self.__class__.__name__] = None
		return [applied_strategy, amount]
