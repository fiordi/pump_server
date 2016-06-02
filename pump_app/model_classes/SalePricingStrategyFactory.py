from django.contrib.auth.models import User
from django.db import models
from solo.models import SingletonModel

#recupero le proprieta' legate alla strategia
import pump_site.sales_strategy
properties = pump_site.sales_strategy

"""
SalePricingStrategyFactory class (Singleton)
"""

class SalePricingStrategyFactory(SingletonModel):
	id = models.AutoField(primary_key=True)

	def getAllPricingStrategy(self):
		PricingStrategy = []
		SalePricingStrategy = self.getSalePricingStrategy()
		PricingStrategy = PricingStrategy + SalePricingStrategy
		return PricingStrategy




	def getCompositeBestPricingStrategy(self):
		from pump_app.model_classes.SalePricingStrategy import CompositeBestForStorePricingStrategy, CompositeBestForCustomerPricingStrategy
		if properties.sales_strategy_properties__compositebestfor == 'store':
			return CompositeBestForStorePricingStrategy()
		if properties.sales_strategy_properties__compositebestfor == 'customer':
			return CompositeBestForCustomerPricingStrategy()





	def getSalePricingStrategy(self):
		from pump_app.model_classes.SalePricingStrategy import MorePacketsStrategy, StudentCustomerStrategy

		PricingStrategy = []
		if properties.sales_strategy_properties__morepacketsstrategy:
			PricingStrategy.append(MorePacketsStrategy())
		if properties.sales_strategy_properties__studentcustomerstrategy:
			PricingStrategy.append(StudentCustomerStrategy())
		return PricingStrategy


	def __unicode__(self):
		return "Sale Pricing Strategy Factory"