from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from copy import deepcopy
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
