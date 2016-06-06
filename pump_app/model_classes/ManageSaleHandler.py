from pump_app.model_classes.Sale import Sale
from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from django.shortcuts import render
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from copy import deepcopy
from collections import Counter
from decimal import *
import json

"""
ManageSaleHandler Class (Singleton)
"""
class ManageSaleHandler(View):

    """
    It handles the CRUD of Course redirecting the request to REST FRAMEWORK

    base_name => str

    :return viewsets.ModelViewSet()
    """
    def setSaleInfo(self, base_name):
        from pump_app.REST_classes.SaleViewSet import SaleViewSet
        return SaleViewSet

    """
    It evals and returns the Amount of a Sale, asking to SalePricingStrategyFactory
    if there are some possible strategies to apply

    Sale => Sale()

    :return Decimal()
    """
    def getAmount(self, Sale):
        from pump_app.model_classes.SalePricingStrategyFactory import SalePricingStrategyFactory
        from pump_app.model_classes.SaleLineItem import SaleLineItem


        #recupero tutte le SaleLineItem associate alla sale e calcolo il totale prediscount
        prediscount_amount = Decimal(0)
        salelineitems = SaleLineItem.objects.filter(sale=Sale)
        if salelineitems:
            for salelineitem in salelineitems:
                subamount = salelineitem.getSubAmount()
                prediscount_amount = prediscount_amount + subamount


        Sale.amount_prediscount = prediscount_amount
        Sale.amount = Sale.amount_prediscount
        Sale.applied_strategies = {}

        #dopo aver calcolato il prediscount_amount, valuto se ci sono strategie di sconto possibili da applicare
        CompositeBestForPricingStrategy = SalePricingStrategyFactory().getCompositeBestPricingStrategy()
        PricingStrategies = SalePricingStrategyFactory().getAllPricingStrategy()

        CompositeBestForPricingStrategy.add(PricingStrategies)

        CompositeBestForPricingStrategy.getAmount(Sale)

        return Sale.amount




    """
    It automatically calculates the amount of the sale (following strategies, if available) on each save()
    """
    @receiver(post_save, sender=Sale)
    def post_save_getTotal(sender, instance, *args, **kwargs):
        from pump_app.model_classes.ManageSaleHandler import ManageSaleHandler

        ManageSaleHandler().getAmount(instance)