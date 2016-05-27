from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from copy import deepcopy
from collections import Counter
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

        packets = Sale.packets.all()

        prediscount_amount = 0
        for packet in packets:
            prediscount_amount = prediscount_amount + packet.price

        Sale.amount_prediscount = prediscount_amount
        Sale.amount = Sale.amount_prediscount

        #dopo aver aggiornato il timeStamp e i pacchetti, devo adottare la strategia di sconto
        PricingStrategies = SalePricingStrategyFactory().getAllPricingStrategy()
        from pump_app.model_classes.SalePricingStrategy import MorePacketsStrategy
        for PricingStrategy in PricingStrategies:
            [applied_strategy, amount] = PricingStrategy.getAmount(Sale)
            Sale.amount = amount
            Sale.applied_strategies = Counter(Sale.applied_strategies) + Counter(applied_strategy)



    """
    DEBUG METHOD! USE IT CAREFULLY!

    request => HttpRequest()

    :return HttpResponse()
    """
    def debug(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.Sale import Sale

            sale = Sale.objects.get(pk = 1)

            packets = sale.packets.all()

            #ogni volta che arrivano i pacchetti vengono aggiornati, ricalcolo il totale PreDiscount
            prediscount_amount = 0
            for packet in packets:
                prediscount_amount = prediscount_amount + packet.price

            return HttpResponse(str(prediscount_amount))
