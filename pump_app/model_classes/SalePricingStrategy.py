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

	def getAmount(self, sale):
		packets = sale.packets.all()

		applied_strategy = {}

		if len(packets) >= properties.morePacketsStrategy_properties__min_number_of_packets:
			amount = sale.amount_prediscount*(100-properties.morePacketsStrategy_properties__percentage_of_discount)/100
			applied_strategy[self.__class__.__name__] = sale.amount - amount
		else:
			amount = sale.amount
			applied_strategy[self.__class__.__name__] = None
		return [applied_strategy, amount]






"""
StudentCustomerStrategy class
"""
class StudentCustomerStrategy(SingletonModel):

	def getAmount(self, sale):
		from pump_app.model_classes.Customer import StudentCustomer

		applied_strategy = {}

		try:
			studentcustomer = StudentCustomer.objects.get(pk=Sale.user.pk)
		except:
			studentcustomer = None

		if studentcustomer:
			amount = Decimal(sale.amount*(100-properties.studentCustomerStrategy_properties__percentage_of_discount)/100)
			applied_strategy[self.__class__.__name__] = sale.amount - amount
		else:
			amount = sale.amount
			applied_strategy[self.__class__.__name__] = None
		return [applied_strategy, amount]


"""
CompositePricingStrategy class (composite)
"""
class CompositePricingStrategy(SingletonModel):

	pricingStrategies = []


	"""
	It adds a new SalePricingStrategy if it doesn't exist into self.pricingStrategies

	SalePricingStrategies => list(SalePricingStrategy)
	"""
	def add(self, SalePricingStrategies):
		for SalePricingStrategy in SalePricingStrategies:
			if not any(isinstance(x, SalePricingStrategy.__class__) for x in self.pricingStrategies):
				self.pricingStrategies.append(SalePricingStrategy)
		return self




	"""
	It evals the Amount of a Sale

	Sale => Sale
	"""
	def getAmount(self, sale):
		for pricingStrategy in self.pricingStrategies:
			[applied_strategy, amount] = pricingStrategy.getAmount(sale)
			sale.amount = amount
			sale.applied_strategies = Counter(sale.applied_strategies) + Counter(applied_strategy)





"""
CompositeBestForCustomerPricingStrategy class
"""
class CompositeBestForCustomerPricingStrategy(CompositePricingStrategy):

	"""
	It evals the Amount of a Sale

	Sale => Sale
	"""
	def getAmount(self, Sale):
		for pricingStrategy in self.pricingStrategies:
			[applied_strategy, amount] = pricingStrategy.getAmount(Sale)
			Sale.amount = amount
			try:
				Sale.applied_strategies = Counter(Sale.applied_strategies) + Counter(applied_strategy)
			except:
				Sale.applied_strategies = Counter(applied_strategy)





"""
CompositeBestForStorePricingStrategy class
"""
class CompositeBestForStorePricingStrategy(CompositePricingStrategy):

	"""
	It evals the Amount of a Sale

	Sale => Sale
	"""
	def getAmount(self, Sale):

		highestAmount = Decimal(0)

		for pricingStrategy in self.pricingStrategies:
			[applied_strategy, amount] = pricingStrategy.getAmount(Sale)
			if amount != Sale.amount:
				highestAmount = max(highestAmount, amount)

				if highestAmount is amount:
					Sale.applied_strategies = Counter(applied_strategy)

		Sale.amount = highestAmount