from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel
from collections import Counter
from decimal import *
from picklefield.fields import PickledObjectField

#recupero le proprieta' legate alla strategia
import pump_site.sales_strategy
properties = pump_site.sales_strategy


"""
SalePricingStrategy class (Interface)
"""
class SalePricingStrategy(SingletonModel):

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


"""
CompositePricingStrategy class (composite)
"""
class CompositePricingStrategy(SingletonModel):

	pricingStrategies = []

	"""
	It adds a new SalePricingStrategy
	"""
	def add(self, SalePricingStrategies):
		for SalePricingStrategy in SalePricingStrategies:
			self.pricingStrategies.append(SalePricingStrategy)
		return self


	def getAmount(self, Sale):
		for pricingStrategy in self.pricingStrategies:
			[applied_strategy, amount] = pricingStrategy.getAmount(Sale)
			Sale.amount = amount
			Sale.applied_strategies = Counter(Sale.applied_strategies) + Counter(applied_strategy)





"""
CompositeBestForCustomerPricingStrategy class
"""
class CompositeBestForCustomerPricingStrategy(CompositePricingStrategy):


	def getAmount(self, Sale):
		for pricingStrategy in self.pricingStrategies:
			[applied_strategy, amount] = pricingStrategy.getAmount(Sale)
			Sale.amount = amount
			Sale.applied_strategies = Counter(Sale.applied_strategies) + Counter(applied_strategy)





"""
CompositeBestForStorePricingStrategy class
"""
class CompositeBestForStorePricingStrategy(CompositePricingStrategy):


	def getAmount(self, Sale):

		highestAmount = Decimal(0)

		for pricingStrategy in self.pricingStrategies:
			[applied_strategy, amount] = pricingStrategy.getAmount(Sale)
			highestAmount = max(highestAmount, amount)
			if applied_strategy[applied_strategy.keys()[0]] is not 0 and highestAmount == amount:
				Sale.applied_strategies = highestAmount

		Sale.amount = highestAmount