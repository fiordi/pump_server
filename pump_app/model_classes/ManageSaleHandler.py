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


    def getTotal(self, Sale):
        from pump_app.model_classes.SalePricingStrategyFactory import SalePricingStrategyFactory

        try:
            packets = Sale.packets.all()
        except:
            packets = None

        prediscount_amount = Decimal(0)
        if packets:
            for packet in packets:
                prediscount_amount = prediscount_amount + packet.price

        Sale.amount_prediscount = prediscount_amount
        Sale.amount = Sale.amount_prediscount

        #dopo aver aggiornato il timeStamp e i pacchetti, devo adottare la strategia di sconto
        CompositeBestForPricingStrategy = SalePricingStrategyFactory().getCompositeBestPricingStrategy()
        PricingStrategies = SalePricingStrategyFactory().getAllPricingStrategy()

        CompositeBestForPricingStrategy.add(PricingStrategies)

        CompositeBestForPricingStrategy.getAmount(Sale)



    """
    It automatically calculates the amount of the sale (following strategies, if available) on each save()
    """
    @receiver(post_save, sender=Sale)
    def post_save_getTotal(sender, instance, *args, **kwargs):
        from pump_app.model_classes.ManageSaleHandler import ManageSaleHandler

        ManageSaleHandler().getTotal(instance)